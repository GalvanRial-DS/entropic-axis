import os
import sys
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import fdrcorrection

def calculate_deltas(df):
    """
    Cleans the dataframe, calculates Z-scores relative to controls, 
    and computes the Delta (Active - Control) for each subject.
    """
    df = df.copy()
    
    # 1. Standardize naming across different atlases
    df.loc[df['dataset'] == 'dmt_pcb', 'dataset'] = 'dmt_plcb'
    df.loc[df['dataset'] == 'modafinil_condition2', 'dataset'] = 'modafinil_placebo'
    df.loc[df['dataset'] == 'placebo_modafinil', 'dataset'] = 'modafinil_placebo'
    df.loc[df['dataset'] == 'modafinil_condition1', 'dataset'] = 'modafinil'
    df.loc[df['dataset'] == 'lsd', 'dataset'] = 'lsd_lsd'
    

    
    # 2. Define families and their control conditions
    families = {
        "anestesia": "anestesia_block1",
        "dmt": "dmt_plcb",
        "lsd": "lsd_plcb",
        "modafinil": "modafinil_placebo",
        "ucla": "ucla_control"
    }
    
    # Handle TianSchaefer alternative names
    if 'anestesia_baseline' in df['dataset'].values:
        families['anestesia'] = 'anestesia_baseline'
    
    # 3. Z-score within family using Control Mean & Std
    df['SampEn_Z'] = np.nan
    for prefix, ctrl_cond in families.items():
        subset = df[df['dataset'].str.startswith(prefix)]
        if subset.empty: continue
        
        ctrl_vals = subset[subset['dataset'] == ctrl_cond]['SampEn']
        m, s = ctrl_vals.mean(), ctrl_vals.std()
        if pd.isna(s) or s == 0: s = 1.0
        
        df.loc[subset.index, 'SampEn_Z'] = (subset['SampEn'] - m) / s
        
    # 4. Calculate Deltas
    baselines = list(families.values())
    df_base = df[df['dataset'].isin(baselines)].copy()
    df_active = df[~df['dataset'].isin(baselines)].copy()
    
    delta_records = []
    
    # Map for clean output names
    cond_map = {
        "anestesia_block2": "Light Anaesthesia",
        "anestesia_light": "Light Anaesthesia",
        "anestesia_block3": "Deep Anaesthesia",
        "anestesia_deep": "Deep Anaesthesia",
        "anestesia_block4": "Anaes. Recovery",
        "anestesia_recovery": "Anaes. Recovery",
        "dmt_dmt": "DMT",
        "lsd_lsd": "LSD",
        "modafinil": "Modafinil",
        "ucla_schz": "Schizophrenia"
    }
    
    for _, row in df_active.iterrows():
        subj = row['Subject']
        cond = row['dataset']
        z_val = row['SampEn_Z']
        
        # Determine if paired or unpaired design
        if cond.startswith('ucla') or cond.startswith('modafinil'):
            delta = z_val - 0  # Unpaired: control mean is 0 by definition of Z-score
        else:
            # Paired: Subtract the subject's own baseline
            prefix = cond.split('_')[0]
            ctrl_cond = families[prefix]
            base_row = df_base[(df_base['Subject'] == subj) & (df_base['dataset'] == ctrl_cond)]
            
            if not base_row.empty:
                delta = z_val - base_row['SampEn_Z'].values[0]
            else:
                continue # Skip if missing baseline
                
        display_cond = cond_map.get(cond, cond)
        delta_records.append({
            "Subject": subj,
            "Condition": display_cond,
            "Delta_Z": delta
        })
        
    return pd.DataFrame(delta_records)

def run_all_models():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.dirname(os.path.dirname(script_dir))
    out_dir = os.path.join(main_dir, "results/statistical_review")
    os.makedirs(out_dir, exist_ok=True)
    out_md = os.path.join(out_dir, "omnibus_categorical_results.md")
    
    configs = [
        ("AAL", "dSW", "data/AAL/all_data.csv"),
        ("AAL", "dFC", "data/AAL/dFC_all_data.csv"),
        ("Tian_Schaefer", "dSW", "data/Tian_Schaefer/dSW_all_data.csv"),
        ("Tian_Schaefer", "dFC", "data/Tian_Schaefer/dFC_all_data.csv")
    ]
    
    with open(out_md, "w") as f:
        f.write("# Categorical Omnibus LME Results (Delta Z-Scores)\n\n")
        f.write("This report tests whether the entropy of each state significantly differs from baseline (0), without imposing any a priori gradient order.\n\n")
        f.write("**Formula:** `Delta_Z ~ 0 + C(Condition) + (1 | Subject)`\n\n")
        
        for atlas, metric, rel_path in configs:
            csv_path = os.path.join(main_dir, rel_path)
            if not os.path.exists(csv_path):
                print(f"File missing: {csv_path}")
                continue
                
            df_raw = pd.read_csv(csv_path)
            df_deltas = calculate_deltas(df_raw)
            
            f.write(f"## {atlas} - {metric}\n\n")
            f.write("```text\n")
            
            try:
                # 0 + C(Condition) removes global intercept so coefficients are exact means
                model = smf.mixedlm("Delta_Z ~ 0 + C(Condition)", df_deltas, groups=df_deltas["Subject"])
                result = model.fit()
                
                # Extract table as DataFrame (mixedlm returns pandas DF for table 1)
                df_res = result.summary().tables[1].copy()
                
                # Extract p-values for conditions
                cond_pvals = result.pvalues[result.pvalues.index.str.startswith('C(Condition)')]
                
                # Apply FDR
                _, pvals_fdr = fdrcorrection(cond_pvals.values)
                
                # Add FDR column
                df_res['p_FDR'] = ""
                for i, cond in enumerate(cond_pvals.index):
                    df_res.loc[cond, 'p_FDR'] = f"{pvals_fdr[i]:.3f}"
                
                f.write(df_res.to_string())
                f.write("\n")
            except Exception as e:
                f.write(f"Model failed: {e}\n")
            f.write("```\n\n")
            
    print(f"Success! Full markdown report saved to:\n{out_md}")

if __name__ == "__main__":
    run_all_models()
