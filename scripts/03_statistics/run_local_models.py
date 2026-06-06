import os
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy.stats import zscore
from statsmodels.stats.multitest import fdrcorrection

script_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(os.path.dirname(script_dir))

def main():
    out_md = os.path.join(main_dir, 'results/statistical_review/local_models_raw.md')
    metrics = {
        'AAL_dSW': os.path.join(main_dir, 'data/AAL/all_data.csv'),
        'AAL_dFC': os.path.join(main_dir, 'data/AAL/dFC_all_data.csv'),
        'TianSchaefer_dSW': os.path.join(main_dir, 'data/Tian_Schaefer/dSW_all_data.csv'),
        'TianSchaefer_dFC': os.path.join(main_dir, 'data/Tian_Schaefer/dFC_all_data.csv')
    }
    
    # Inclusive list covering both datasets
    families = {
        'Anaesthesia (Paired)': ['anestesia_block1', 'anestesia_block2', 'anestesia_block3', 'anestesia_block4', 'anestesia_baseline', 'anestesia_light', 'anestesia_deep', 'anestesia_recovery'],
        'LSD (Paired)': ['lsd_plcb', 'lsd', 'lsd_lsd'],
        'DMT (Paired)': ['dmt_pcb', 'dmt_plcb', 'dmt_dmt'],
        'Modafinil (Unpaired)': ['modafinil_condition2', 'modafinil_placebo', 'placebo_modafinil', 'modafinil_condition1', 'modafinil'],
        'Schizophrenia (Unpaired)': ['ucla_control', 'ucla_schz']
    }
    
    md_content = "# Local Models (Raw Output)\n\n"
    md_content += "Note: Paired designs use MixedLM (random subject intercepts). Unpaired designs use OLS to avoid mathematically invalid singular covariance matrices.\n\n"

    for metric, path in metrics.items():
        if not os.path.exists(path): continue
        df = pd.read_csv(path)

        
        md_content += f"---\n\n## METRIC: {metric}\n\n---\n\n"

        for name, conditions in families.items():
            valid_conds = [c for c in conditions if c in df['dataset'].values]
            if not valid_conds: continue
            
            df_local = df[df['dataset'].isin(valid_conds)].copy()
            df_local['dataset'] = pd.Categorical(df_local['dataset'], categories=valid_conds, ordered=True)
            
            is_paired = 'Paired' in name
            md_content += f"### {name} ({metric})\n\n"
            
            try:
                if is_paired:
                    model = smf.mixedlm('SampEn ~ dataset', df_local, groups=df_local['Subject']).fit()
                else:
                    model = smf.ols('SampEn ~ dataset', data=df_local).fit()
                
                summary_str = model.summary().as_text()
                md_content += f"```text\n{summary_str}\n```\n\n"
                
                # Apply FDR only to the Propofol dataset (3 tests against baseline)
                if 'Anaesthesia' in name:
                    p_vals = []
                    names = []
                    for param_name, p_val in model.pvalues.items():
                        if 'dataset' in param_name: # Only the active contrasts
                            p_vals.append(p_val)
                            names.append(param_name)
                    
                    if p_vals:
                        _, fdr_p = fdrcorrection(p_vals)
                        md_content += "#### FDR Correction (Benjamini-Hochberg)\n\n"
                        for n, raw_p, adj_p in zip(names, p_vals, fdr_p):
                            md_content += f"- **{n}**: Raw p = {raw_p:.4f} --> **FDR Corrected p = {adj_p:.4f}**\n"
                        md_content += "\n"
                        
            except Exception as e:
                md_content += f"```text\nERROR fitting model: {e}\n```\n\n"

    with open(out_md, 'w') as f:
        f.write(md_content)
        
    print(f"Local models raw MD saved to: {out_md}")

if __name__ == "__main__":
    main()
