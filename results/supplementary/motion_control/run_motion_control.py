"""
run_motion_control.py
=====================
Tests whether head motion (mean Framewise Displacement from MRIQC)
predicts Sample Entropy within each dataset.

Model: SampEn ~ fd_mean
  - Within-subject datasets (anaesthesia, LSD, DMT): MixedLM, subject random intercept
  - Between-subject datasets (Modafinil, UCLA): OLS

Usage
-----
    python run_motion_control.py
    python run_motion_control.py --data mriqc_sampen_merged.csv
"""

import argparse
from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf

PAIRED   = ["anestesia", "lsd", "nuevos_dmt"]
UNPAIRED = ["modafinil", "ucla"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=Path,
                   default=Path(__file__).parent / "mriqc_sampen_merged.csv")
    return p.parse_args()


def main():
    args = parse_args()
    df = pd.read_csv(args.data)
    print(f"N = {len(df)} | datasets: {sorted(df['mriqc_folder'].unique())}\n")

    results = []
    for folder in sorted(df["mriqc_folder"].unique()):
        if folder == "lsd":
            continue
        sub = df[df["mriqc_folder"] == folder].copy()

        try:
            if folder in PAIRED:
                model = smf.mixedlm("SampEn ~ fd_mean + C(dataset)", sub,
                                    groups=sub["sub_bids"]).fit(reml=True)
                mtype = "MixedLM"
            else:
                model = smf.ols("SampEn ~ fd_mean + C(dataset)", sub).fit()
                mtype = "OLS"

            print(f"=== {folder} ({mtype}) ===")
            print(model.summary())
            print()

            # Map dataset names
            dataset_name = folder
            if folder == "anestesia": dataset_name = "Anaesthesia"
            elif folder == "lsd": dataset_name = "LSD"
            elif folder == "modafinil": dataset_name = "Modafinil"
            elif folder == "nuevos_dmt": dataset_name = "DMT"
            elif folder == "ucla": dataset_name = "Schizophrenia"
            
            # Extract main condition effect p-value
            cond_pval = None
            for idx in model.pvalues.index:
                if "C(dataset)" in idx:
                    cond_pval = model.pvalues[idx]
                    break
                    
            if cond_pval is None:
                cond_pval = float('nan')
            
            results.append({
                "Dataset": dataset_name,
                "Model":   mtype,
                "N":       len(sub),
                "β (Motion)": round(model.params["fd_mean"], 4),
                "SE (Motion)": round(model.bse["fd_mean"], 4),
                "p (Motion)": round(model.pvalues["fd_mean"], 4),
                "p (Condition)": "< 0.001" if cond_pval < 0.001 else round(cond_pval, 4)
            })
        except Exception as e:
            print(f"[{folder}] Error: {e}")

    res = pd.DataFrame(results)
    
    print("=== Summary ===")
    print(res.to_string(index=False))

    out_dir = Path(__file__).parent.parent.parent / "paper_figures"
    out_dir.mkdir(exist_ok=True)
    res.to_csv(out_dir / "TableS1_Motion_Control.csv", index=False)
    res.to_markdown(out_dir / "TableS1_Motion_Control.md", index=False)
    print(f"\nSaved Table S1 to {out_dir}")

if __name__ == "__main__":
    main()
