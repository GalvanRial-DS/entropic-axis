"""
Per-Dataset Raincloud Plots — SE values by condition
=====================================================
Generates Figure 2 (SE dSW) and Figure 4 (SE dFC).

Each panel shows the distribution of sample entropy for one dataset,
comparing conditions (e.g., placebo vs drug, awake vs anaesthesia).
Statistical significance is annotated with bracket-and-asterisk notation.

Usage:
    python plot_dataset_rainclouds.py          # both dSW and dFC
    python plot_dataset_rainclouds.py dSW      # Figure 2 only
    python plot_dataset_rainclouds.py dFC      # Figure 4 only
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon, mannwhitneyu
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# Plot settings
# ============================================================
plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

# ============================================================
# Paths
# ============================================================
script_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(os.path.dirname(script_dir))
out_dir = os.path.join(main_dir, "results/paper_figures")
os.makedirs(out_dir, exist_ok=True)

# ============================================================
# Colour palette
# ============================================================
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

def significance_symbol(p):
    if p < 0.001: return "***"
    if p < 0.01:  return "**"
    if p < 0.05:  return "*"
    if p < 0.1:   return "†"
    return ""

def add_stat_bracket(ax, x1, x2, y, h, p_val):
    """Draw a significance bracket if p < 0.1."""
    sym = significance_symbol(p_val)
    if not sym:
        return
    ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c="k")
    font_s = 20 if sym == "†" else 15
    ax.text((x1 + x2) * 0.5, y + h + 0.01*(ax.get_ylim()[1]-ax.get_ylim()[0]), sym, ha="center", va="bottom",
            color="k", fontsize=font_s, fontweight="bold")

# Define exact uncorrected p-values derived from LME/OLS models
p_vals_dsw = {
    "anestesia_block2": 0.0363,
    "anestesia_block3": 0.0037,
    "anestesia_block4": 0.9473,
    "modafinil_condition1": 0.0895,
    "lsd": 0.028,
    "dmt_dmt": 0.076,
    "ucla_schz": 4.05e-5,
}
p_vals_dfc = {
    "anestesia_block2": 0.0156,
    "anestesia_block3": 0.0117,
    "anestesia_block4": 0.5632,
    "modafinil": 0.971,
    "lsd_lsd": 0.001,
    "dmt_dmt": 0.042,
    "ucla_schz": 0.000162,
}


# ============================================================
# Panel definitions — condition labels differ between dSW and dFC CSVs
# ============================================================
panels_dsw = [
    {
        "title": "Anaesthesia",
        "conditions": ["anestesia_block1", "anestesia_block2",
                        "anestesia_block3", "anestesia_block4"],
        "labels": ["Wake", "Light", "Deep", "Recovery"],
        "paired": True,
        "panel_letter": "A",
    },
    {
        "title": "Modafinil",
        "conditions": ["modafinil_condition2", "modafinil_condition1"],
        "labels": ["Placebo", "Modafinil"],
        "paired": False,
        "panel_letter": "B",
    },
    {
        "title": "LSD",
        "conditions": ["lsd_plcb", "lsd"],
        "labels": ["Placebo", "LSD"],
        "paired": True,
        "panel_letter": "C",
    },
    {
        "title": "DMT",
        "conditions": ["dmt_pcb", "dmt_dmt"],
        "labels": ["Placebo", "DMT"],
        "paired": True,
        "panel_letter": "D",
    },
    {
        "title": "Schizophrenia",
        "conditions": ["ucla_control", "ucla_schz"],
        "labels": ["Control", "Schizophrenia"],
        "paired": False,
        "panel_letter": "E",
    },
]

panels_dfc = [
    {
        "title": "Anaesthesia",
        "conditions": ["anestesia_block1", "anestesia_block2",
                        "anestesia_block3", "anestesia_block4"],
        "labels": ["Wake", "Light", "Deep", "Recovery"],
        "paired": True,
        "panel_letter": "A",
    },
    {
        "title": "Modafinil",
        "conditions": ["modafinil_placebo", "modafinil"],
        "labels": ["Placebo", "Modafinil"],
        "paired": False,
        "panel_letter": "B",
    },
    {
        "title": "LSD",
        "conditions": ["lsd_plcb", "lsd_lsd"],
        "labels": ["Placebo", "LSD"],
        "paired": True,
        "panel_letter": "C",
    },
    {
        "title": "DMT",
        "conditions": ["dmt_plcb", "dmt_dmt"],
        "labels": ["Placebo", "DMT"],
        "paired": True,
        "panel_letter": "D",
    },
    {
        "title": "Schizophrenia",
        "conditions": ["ucla_control", "ucla_schz"],
        "labels": ["Control", "Schizophrenia"],
        "paired": False,
        "panel_letter": "E",
    },
]


def plot_panel(ax, df, panel, metric):
    """Draw a single panel (raincloud + stats)."""
    conditions = panel["conditions"]
    labels = panel["labels"]
    is_paired = panel["paired"]

    series_list = [df[df["dataset"] == c]["SampEn"] for c in conditions]
    x = np.arange(len(conditions))

    # Half-violin
    parts = ax.violinplot(series_list, positions=x, widths=0.8,
                          showmeans=False, showextrema=False)
    for i, body in enumerate(parts["bodies"]):
        col = dataset_color[get_family(conditions[i])]
        body.set_facecolor(col)
        body.set_alpha(0.25)
        body.set_edgecolor("none")
        verts = body.get_paths()[0].vertices
        xm = verts[:, 0].mean()
        verts[:, 0] = np.maximum(verts[:, 0], xm)

    # Jittered dots
    np.random.seed(42)
    for i, s in enumerate(series_list):
        if len(s) == 0:
            continue
        col = dataset_color[get_family(conditions[i])]
        jitter = (np.random.rand(len(s)) - 0.5) * 0.12
        ax.scatter(x[i] + jitter, s, s=60, alpha=0.6,
                   color=col, edgecolors="none", zorder=2)

    # Mean + SEM
    means = [s.mean() if len(s) > 0 else np.nan for s in series_list]
    sems = [s.std() / np.sqrt(len(s)) if len(s) > 0 else np.nan for s in series_list]
    ax.errorbar(x, means, yerr=sems, fmt="none", ecolor="black",
                capsize=8, lw=2, zorder=3)
    ax.scatter(x, means, s=100, color="black", zorder=4)

    # Statistics: compare each condition vs control (index 0)
    all_vals = pd.concat(series_list)
    y_max = all_vals.max()
    rng = all_vals.max() - all_vals.min()
    curr_y = y_max + 0.10 * rng
    step = 0.12 * rng

    p_map = p_vals_dsw if metric == "dSW" else p_vals_dfc
    for i in range(1, len(conditions)):
        c = conditions[i]
        p = p_map.get(c, 1.0)
        if p < 0.1:
            add_stat_bracket(ax, 0, i, curr_y, step * 0.4, p)
            curr_y += step

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=14)
    ax.set_title(panel['panel_letter'], loc='left',
                 fontsize=19, fontweight="bold", pad=12)
    ax.set_ylabel("SE", fontsize=17, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def generate_figure(metric):
    """Generate the 5-panel figure for one metric."""
    if metric == "dSW":
        path = os.path.join(main_dir, "data/AAL/all_data.csv")
        panels = panels_dsw
        tag = "Figure2"
    else:
        path = os.path.join(main_dir, "data/AAL/dFC_all_data.csv")
        panels = panels_dfc
        tag = "Figure4"

    df = pd.read_csv(path)

    fig, axes = plt.subplots(1, 5, figsize=(18, 6), constrained_layout=True)
    for i, panel in enumerate(panels):
        plot_panel(axes[i], df, panel, metric)

    for ext in ["png"]:
        fig.savefig(os.path.join(out_dir, f"{tag}.{ext}"),
                    dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {tag} (.png)")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    metrics = sys.argv[1:] if len(sys.argv) > 1 else ["dSW", "dFC"]
    for m in metrics:
        generate_figure(m)
