"""
Plot Delta Gradient
===================
Calculates the delta (Experimental - Placebo/Baseline) of the Z-scored data 
for each dataset and plots the entropic gradient in a single multi-dataset panel.
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

script_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(os.path.dirname(script_dir))
out_dir = os.path.join(main_dir, "results/paper_figures")

dataset_color = {
    "Deep Anaesthesia": "#E69F00",
    "Light Anaesthesia": "#E69F00",
    "Anaes. Recovery": "#E69F00",
    "DMT": "#CC79A7",
    "LSD": "#009E73",
    "Modafinil": "#F0E442",
    "Schizophrenia": "#0072B2"
}

def load_z_deltas(csv_path, metric="dSW"):
    df = pd.read_csv(csv_path)
    
    # Standardize names just in case
    df.loc[df['dataset'] == 'dmt_pcb', 'dataset'] = 'dmt_plcb'
    df.loc[df['dataset'] == 'modafinil_condition2', 'dataset'] = 'modafinil_placebo'
    df.loc[df['dataset'] == 'modafinil_condition1', 'dataset'] = 'modafinil'
    df.loc[df['dataset'] == 'placebo_modafinil', 'dataset'] = 'modafinil_placebo'
    df.loc[df['dataset'] == 'anestesia_baseline', 'dataset'] = 'anestesia_block1'
    df.loc[df['dataset'] == 'anestesia_light', 'dataset'] = 'anestesia_block2'
    df.loc[df['dataset'] == 'anestesia_deep', 'dataset'] = 'anestesia_block3'
    df.loc[df['dataset'] == 'anestesia_recovery', 'dataset'] = 'anestesia_block4'
    
    if metric == "dSW":
        df.loc[df['dataset'] == 'lsd', 'dataset'] = 'lsd_lsd'
    
    # 1. Z-score within dataset BEFORE calculating delta
    aligned_df = df.copy()
    aligned_df["SampEn_Z"] = np.nan
    
    families = {
        "anestesia": "anestesia_block1",
        "dmt": "dmt_plcb",
        "lsd": "lsd_plcb",
        "modafinil": "modafinil_placebo",
        "ucla": "ucla_control"
    }
    
    for prefix, ctrl_cond in families.items():
        subset = df[df['dataset'].str.startswith(prefix)]
        if subset.empty: continue
        
        ctrl_vals = subset[subset['dataset'] == ctrl_cond]['SampEn']
        ctrl_mean = ctrl_vals.mean()
        ctrl_std = ctrl_vals.std()
        if pd.isna(ctrl_std) or ctrl_std == 0: ctrl_std = 1.0
        
        idx = subset.index
        aligned_df.loc[idx, "SampEn_Z"] = (aligned_df.loc[idx, "SampEn"] - ctrl_mean) / ctrl_std
    
    # 2. Calculate deltas on the Z-scored values (SampEn_Z)
    deltas = {}
    
    # Anaesthesia (Paired)
    df_anes = aligned_df[aligned_df['dataset'].str.startswith('anestesia')]
    if not df_anes.empty:
        base = df_anes[df_anes['dataset'] == 'anestesia_block1'].set_index('Subject')['SampEn_Z']
        for name, block in [("Light Anaesthesia", "anestesia_block2"), ("Deep Anaesthesia", "anestesia_block3"), ("Anaes. Recovery", "anestesia_block4")]:
            exp = df_anes[df_anes['dataset'] == block].set_index('Subject')['SampEn_Z']
            common = base.index.intersection(exp.index)
            deltas[name] = (exp[common] - base[common]) # Returning Series to preserve Subject index

    # DMT (Paired)
    df_dmt = aligned_df[aligned_df['dataset'].str.startswith('dmt')]
    if not df_dmt.empty:
        base = df_dmt[df_dmt['dataset'] == 'dmt_plcb'].set_index('Subject')['SampEn_Z']
        exp = df_dmt[df_dmt['dataset'] == 'dmt_dmt'].set_index('Subject')['SampEn_Z']
        common = base.index.intersection(exp.index)
        deltas["DMT"] = (exp[common] - base[common])

    # LSD (Paired)
    df_lsd = aligned_df[aligned_df['dataset'].str.startswith('lsd')]
    if not df_lsd.empty:
        base = df_lsd[df_lsd['dataset'] == 'lsd_plcb'].set_index('Subject')['SampEn_Z']
        exp = df_lsd[df_lsd['dataset'] == 'lsd_lsd'].set_index('Subject')['SampEn_Z']
        common = base.index.intersection(exp.index)
        deltas["LSD"] = (exp[common] - base[common])

    # Modafinil (Between-Subjects)
    df_mod = aligned_df[aligned_df['dataset'].str.startswith('modafinil')]
    if not df_mod.empty:
        exp = df_mod[df_mod['dataset'] == 'modafinil'].set_index('Subject')['SampEn_Z']
        deltas["Modafinil"] = exp - 0

    # Schizophrenia (Between-Subjects)
    df_schz = aligned_df[aligned_df['dataset'].str.startswith('ucla')]
    if not df_schz.empty:
        exp = df_schz[df_schz['dataset'] == 'ucla_schz'].set_index('Subject')['SampEn_Z']
        deltas["Schizophrenia"] = exp - 0
        
    return deltas

def generate_delta_gradient(metric, atlas="AAL"):
    if atlas == "AAL":
        fname = 'all_data.csv' if metric == 'dSW' else 'dFC_all_data.csv'
    else:
        fname = f'{metric}_all_data.csv'
    csv_path = os.path.join(main_dir, f"data/{atlas}/{fname}")
    deltas = load_z_deltas(csv_path, metric)
    
    labels = ["Deep Anaesthesia", "Light Anaesthesia", "Anaes. Recovery", "DMT", "LSD", "Modafinil", "Schizophrenia"]
    series_list = [deltas.get(lbl, pd.Series(dtype=float)).dropna().values for lbl in labels]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(labels))
    
    parts = ax.violinplot(series_list, positions=x, widths=0.7, showmeans=False, showextrema=False)
    for i, body in enumerate(parts["bodies"]):
        col = dataset_color[labels[i]]
        body.set_facecolor(col)
        body.set_alpha(0.3)
        body.set_edgecolor("none")
        verts = body.get_paths()[0].vertices
        xm = verts[:, 0].mean()
        verts[:, 0] = np.maximum(verts[:, 0], xm)

    np.random.seed(42)
    for i, s in enumerate(series_list):
        if len(s) == 0: continue
        col = dataset_color[labels[i]]
        jitter = (np.random.rand(len(s)) - 0.5) * 0.12
        ax.scatter(x[i] + jitter, s, s=40, alpha=0.7, color=col, edgecolors="none", zorder=2)

    means = [s.mean() if len(s) > 0 else np.nan for s in series_list]
    sems = [s.std() / np.sqrt(len(s)) if len(s) > 0 else np.nan for s in series_list]
    
    ax.errorbar(x, means, yerr=sems, fmt="none", ecolor="black", capsize=8, lw=2, zorder=3)
    ax.scatter(x, means, s=90, color="black", zorder=4)

    ax.axhline(0, color="gray", linestyle="--", linewidth=1.5, zorder=0)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=14)
    ax.set_ylabel(r"$\Delta$ Z-score", fontsize=18, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    if atlas == "AAL":
        if metric == "dSW":
            sig_map = {
                "Deep Anaesthesia": "*",
                "Light Anaesthesia": "†",
                "LSD": "*",
                "DMT": "*",
                "Modafinil": "*",
                "Schizophrenia": "***"
            }
        else:
            sig_map = {
                "Deep Anaesthesia": "**",
                "Light Anaesthesia": "*",
                "LSD": "**",
                "DMT": "***",
                "Schizophrenia": "***"
            }
    else:
        if metric == "dSW":
            sig_map = {
                "Deep Anaesthesia": "*",
                "Light Anaesthesia": "*",
                "Anaes. Recovery": "*",
                "Modafinil": "*",
                "Schizophrenia": "*"
            }
        else:
            sig_map = {
                "Light Anaesthesia": "†",
                "Schizophrenia": "**"
            }

    for i, lbl in enumerate(labels):
        if lbl in sig_map:
            sym = sig_map[lbl]
            font_s = 20 if sym == "†" else 18
            local_y_max = max(series_list[i]) if len(series_list[i]) > 0 else 0
            ax.text(i, local_y_max + 0.05, sym, ha='center', va='bottom', fontsize=font_s, fontweight='bold', color='black')

    if atlas == "AAL":
        tag = "Figure3" if metric == "dSW" else "FigureS1"
    else:
        tag = "FigureS2" if metric == "dSW" else "FigureS3"
    
    for ext in ["png"]:
        fig.savefig(os.path.join(out_dir, f"{tag}.{ext}"), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {tag} (.png) (Z-scored)")

if __name__ == "__main__":
    generate_delta_gradient("dSW", "AAL")
    generate_delta_gradient("dFC", "AAL")
    generate_delta_gradient("dSW", "Tian_Schaefer")
    generate_delta_gradient("dFC", "Tian_Schaefer")
