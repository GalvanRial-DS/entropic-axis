import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plot settings
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
os.makedirs(out_dir, exist_ok=True)

dataset_color = {
    "anestesia":  "#E69F00",
    "dmt":        "#CC79A7",
    "lsd":        "#009E73",
    "modafinil":  "#F0E442",
    "ucla":       "#0072B2",
}

def get_family(label):
    for key in dataset_color:
        if key in label:
            return key
    return "ucla"

labels_map = {
    "anestesia_block3": "Deep Anaesthesia",
    "anestesia_block2": "Light Anaesthesia",
    "anestesia_block4": "Recovery",
    "anestesia_block1": "Wakefulness",
    "lsd_plcb": "LSD Placebo",
    "dmt_pcb": "DMT Placebo",
    "dmt_plcb": "DMT Placebo",
    "ucla_control": "UCLA Control",
    "modafinil_condition2": "Modafinil Placebo",
    "modafinil_placebo": "Modafinil Placebo",
    "dmt_dmt": "DMT",
    "lsd": "LSD",
    "lsd_lsd": "LSD",
    "modafinil_condition1": "Modafinil",
    "modafinil": "Modafinil",
    "ucla_schz": "Schizophrenia"
}

study_defs_dsw = {
    "anestesia": {
        "control": "anestesia_block1",
        "conditions": ["anestesia_block1", "anestesia_block2", "anestesia_block3", "anestesia_block4"],
        "labels": {"anestesia_block1": "Wakefulness", "anestesia_block2": "Light Anaesthesia", "anestesia_block3": "Deep Anaesthesia", "anestesia_block4": "Recovery"}
    },
    "lsd": {
        "control": "lsd_plcb",
        "conditions": ["lsd_plcb", "lsd"],
        "labels": {"lsd_plcb": "LSD Placebo", "lsd": "LSD"}
    },
    "dmt": {
        "control": "dmt_pcb",
        "conditions": ["dmt_pcb", "dmt_dmt"],
        "labels": {"dmt_pcb": "DMT Placebo", "dmt_dmt": "DMT"}
    },
    "modafinil": {
        "control": "modafinil_condition2",
        "conditions": ["modafinil_condition2", "modafinil_condition1"],
        "labels": {"modafinil_condition2": "Modafinil Placebo", "modafinil_condition1": "Modafinil"}
    },
    "ucla": {
        "control": "ucla_control",
        "conditions": ["ucla_control", "ucla_schz"],
        "labels": {"ucla_control": "UCLA Control", "ucla_schz": "Schizophrenia"}
    }
}

study_defs_dfc = {
    "anestesia": {
        "control": "anestesia_block1",
        "conditions": ["anestesia_block1", "anestesia_block2", "anestesia_block3", "anestesia_block4"],
        "labels": {"anestesia_block1": "Wakefulness", "anestesia_block2": "Light Anaesthesia", "anestesia_block3": "Deep Anaesthesia", "anestesia_block4": "Recovery"}
    },
    "lsd": {
        "control": "lsd_plcb",
        "conditions": ["lsd_plcb", "lsd_lsd"],
        "labels": {"lsd_plcb": "LSD Placebo", "lsd_lsd": "LSD"}
    },
    "dmt": {
        "control": "dmt_plcb",
        "conditions": ["dmt_plcb", "dmt_dmt"],
        "labels": {"dmt_plcb": "DMT Placebo", "dmt_dmt": "DMT"}
    },
    "modafinil": {
        "control": "modafinil_placebo",
        "conditions": ["modafinil_placebo", "modafinil"],
        "labels": {"modafinil_placebo": "Modafinil Placebo", "modafinil": "Modafinil"}
    },
    "ucla": {
        "control": "ucla_control",
        "conditions": ["ucla_control", "ucla_schz"],
        "labels": {"ucla_control": "UCLA Control", "ucla_schz": "Schizophrenia"}
    }
}

FIXED_ORDER = [
    "anestesia_block1", "anestesia_block2", "anestesia_block3", "anestesia_block4",
    "modafinil_condition2", "modafinil_placebo", "modafinil_condition1", "modafinil",
    "lsd_plcb", "lsd", "lsd_lsd",
    "dmt_pcb", "dmt_plcb", "dmt_dmt",
    "ucla_control", "ucla_schz"
]

def plot_raw_axis(ax, metric, letter):
    path = os.path.join(main_dir, "data/AAL/all_data.csv") if metric == "dSW" else os.path.join(main_dir, "data/AAL/dFC_all_data.csv")
    df = pd.read_csv(path)

    
    means = df.groupby('dataset')['SampEn'].mean().sort_values()
    ordered_conds = means.index.tolist()
    
    series_list = [df[df['dataset'] == c]['SampEn'].dropna() for c in ordered_conds]
    labels = [labels_map.get(c, c) for c in ordered_conds]
    
    x = np.arange(len(series_list))
    
    parts = ax.violinplot(series_list, positions=x, widths=0.8, showmeans=False, showextrema=False)
    for i, body in enumerate(parts["bodies"]):
        cond = ordered_conds[i]
        col = dataset_color[get_family(cond)]
        body.set_facecolor(col)
        body.set_alpha(0.3)
        body.set_edgecolor("none")
        verts = body.get_paths()[0].vertices
        xm = verts[:, 0].mean()
        verts[:, 0] = np.maximum(verts[:, 0], xm)
        
    np.random.seed(42)
    for i, s in enumerate(series_list):
        if len(s) == 0: continue
        col = dataset_color[get_family(ordered_conds[i])]
        jitter = (np.random.rand(len(s)) - 0.5) * 0.10
        ax.scatter(x[i] + jitter, s, s=40, alpha=0.6, color=col, edgecolors="none", zorder=2)
        
    means_val = [s.mean() for s in series_list]
    sems_val = [s.std() / np.sqrt(len(s)) for s in series_list]
    ax.errorbar(x, means_val, yerr=sems_val, fmt="none", ecolor="black", capsize=5, lw=2, zorder=3)
    ax.scatter(x, means_val, s=80, color="black", zorder=4)
    
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=13)
    ax.set_ylabel("Raw Sample Entropy", fontsize=15, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(letter, loc='left', fontsize=20, fontweight='bold', pad=10)

def load_zscored_data(csv_path, study_defs):
    df = pd.read_csv(csv_path)

    
    aligned_df = df.copy()
    aligned_df["SampEn_zscored"] = np.nan
    
    for family, info in study_defs.items():
        ctrl_cond = info["control"]
        ctrl_vals = df[df["dataset"] == ctrl_cond]["SampEn"]
        ctrl_mean = ctrl_vals.mean()
        ctrl_std = ctrl_vals.std()
        if ctrl_std == 0 or np.isnan(ctrl_std):
            ctrl_std = 1.0
            
        idx = aligned_df["dataset"].isin(info["conditions"])
        aligned_df.loc[idx, "SampEn_zscored"] = (aligned_df.loc[idx, "SampEn"] - ctrl_mean) / ctrl_std
        
    results = {}
    for family, info in study_defs.items():
        for cond in info["conditions"]:
            vals = aligned_df[aligned_df["dataset"] == cond]["SampEn_zscored"].dropna()
            results[cond] = {
                "cond_raw": cond,
                "label": info["labels"][cond],
                "color": dataset_color[family],
                "vals": vals,
                "mean": vals.mean()
            }
            
    results_sorted = list(results.values())
    results_sorted.sort(key=lambda x: x["mean"])
    return results_sorted

def plot_entropic_axis(ax, metric, letter):
    if metric == "dSW":
        csv_path = os.path.join(main_dir, "data/AAL/all_data.csv")
        study_defs = study_defs_dsw
    else:
        csv_path = os.path.join(main_dir, "data/AAL/dFC_all_data.csv")
        study_defs = study_defs_dfc

    results = load_zscored_data(csv_path, study_defs)
    
    series_list = [r["vals"] for r in results]
    labels = [r["label"] for r in results]
    colors = [r["color"] for r in results]
    
    x = np.arange(len(results))
    
    ax.axhline(0, color="gray", linestyle="--", linewidth=1.5, alpha=0.7)
    
    parts = ax.violinplot(series_list, positions=x, widths=0.7, showmeans=False, showextrema=False)

    for i, body in enumerate(parts["bodies"]):
        body.set_facecolor(colors[i])
        body.set_alpha(0.3)
        body.set_edgecolor("none")
        verts = body.get_paths()[0].vertices
        xm = verts[:, 0].mean()
        verts[:, 0] = np.maximum(verts[:, 0], xm)

    np.random.seed(42)
    for i, s in enumerate(series_list):
        if len(s) == 0: continue
        jitter = (np.random.rand(len(s)) - 0.5) * 0.10
        ax.scatter(x[i] + jitter, s, s=40, alpha=0.6, color=colors[i], edgecolors="none", zorder=2)

    m = [s.mean() for s in series_list]
    se = [s.std() / np.sqrt(len(s)) for s in series_list]
    ax.errorbar(x, m, yerr=se, fmt="none", ecolor="black", capsize=8, lw=2, zorder=3)
    ax.scatter(x, m, s=80, color="black", zorder=4)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=13)
    ax.set_ylabel("Sample Entropy (Z-score)", fontsize=17, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(letter, loc='left', fontsize=20, fontweight='bold', pad=10)

def main():
    # Figure S4: Raw dSW
    fig2, ax2 = plt.subplots(figsize=(12, 6), constrained_layout=True)
    plot_raw_axis(ax2, "dSW", "") # No letter needed for single panel
    fig2.savefig(os.path.join(out_dir, "FigureS4.png"), dpi=300, bbox_inches="tight")
    plt.close(fig2)
    print("Saved FigureS4.png (Raw dSW)")

    # Figure S5: Raw dFC
    fig3, ax3 = plt.subplots(figsize=(12, 6), constrained_layout=True)
    plot_raw_axis(ax3, "dFC", "")
    fig3.savefig(os.path.join(out_dir, "FigureS5.png"), dpi=300, bbox_inches="tight")
    plt.close(fig3)
    print("Saved FigureS5.png (Raw dFC)")

if __name__ == "__main__":
    main()
