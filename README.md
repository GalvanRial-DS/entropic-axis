# A Shared Entropic Axis Spans States of Consciousness Across Pharmacological and Clinical Conditions

![Analysis Pipeline](results/paper_figures/Figure1.png)

This repository contains the processing scripts and processed datasets to reproduce all statistical analyses and figures for the manuscript investigating the shared entropic axis across altered states of consciousness (Psychedelics, Anaesthesia, Modafinil, and Schizophrenia).

---

## Repository Structure

* **`data/`**: Processed tables (`all_data.csv`, LONO CSVs, and summaries) needed to reproduce statistics and figures.
* **`requirements/`**:
* **`versions_info.txt`**: Detailed system, MATLAB, Python, and package version specifications. See [versions_info.txt](requirements/versions_info.txt).
* **`scripts/`**:
* **`01_parcelling/`**: Extraction of regional BOLD time-series from fMRI data. 
  * `run_parcelling.m`, `bold_to_networks.m`. Requires SPM12.
* **`03_graph_analysis/`**: Dynamic Small-World Propensity and Functional Connectivity calculation. 
  *`run_dynamic_metrics.m` and `run_dynamic_metrics_LONO.m`.
* **`03_statistics/`**: Local and global statistical models, and LONO group-level stats (Python).
  * `run_local_models.py`: Local condition effects per dataset.
  * `run_omnibus_model.py`: Global linear mixed-effects model.
  * `process_lono.py`: Leave-One-Network-Out statistics.
* **`04_visualization/`**: Main manuscript figures (Glass Brains, Raincloud Plots, composite figures).
  * **`results/`**: Main outputs and figures.
  * **`paper_figures/`**: Final manuscript figures (Figure1–6, FigureS1–S5).
  * **`statistical_review/`**: Raw model outputs (local models, omnibus model).
* **`supplementary/motion_control/`**: Head motion control analysis.
  * `mriqc_sampen_merged.csv`: Subject-level MRIQC metrics + SampEn (all datasets).
  * `run_motion_control.py`: LME/OLS models testing whether FD predicts SampEn.
  * `motion_control_results.md`: Raw model outputs and FDR-corrected results.

---

## Installation & Requirements

### Python Environment
Install all required Python packages via pip:
```bash
pip install -r requirements.txt
```

### MATLAB Environment
The preprocessing pipeline uses **MATLAB** for Sample Entropy results, here we provide examples for the scripts that were adapted to the different datasets, we also used the following external third-party dependencies (which should be downloaded and added to your MATLAB path):

1. **SPM12** (Statistical Parametric Mapping): Required for parcellation. [Download from SPM Website](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/).
2. **Brain Connectivity Toolbox (BCT)** (Release 2019_03_03): Required by SWP for network metrics. [Download from BCT Website](https://sites.google.com/site/bctnet/).
3. **Small-World Propensity (SWP)** (Muldoon et al., 2016): Required for dSW. [Download from GitHub](https://github.com/dbs-upenn/small-world-propensity).
4. **Physionet Sample Entropy (sampen)**: Required for entropy. [Download from PhysioNet](https://physionet.org/content/sampen/1.0.0/).

Add these directories to your MATLAB path (`pathtool` or `addpath`) before executing the unified `run_*.m` scripts.

---

## Reproducing Figures & Statistics

To reproduce the main results of the manuscript:

1. **Local and Global Statistical Models (Shared Entropic Axis):**

First, evaluate the local condition effects within each individual dataset. This generates the statistical significance markers used in the subject-level raincloud plots (Figures 2 and 3):
```bash
python scripts/03_statistics/run_local_models.py
```

Next, evaluate the global macroscopic gradient. This runs the omnibus linear mixed-effects model over the Z-scored raw entropic values to test the overarching entropic axis hypothesis:
```bash
python scripts/03_statistics/run_omnibus_model.py
```
*(Note: The main text (Figure 4) visualizes this axis using condition deltas derived from the local models. The global omnibus statistics correspond to the Z-scored gradients visualized in Supplementary Figure S3).*

2. **LONO Statistics:**
```bash
python scripts/03_statistics/process_lono.py
```

3. **Generate Main Manuscript Figures:**
```bash
# Generate Per-Dataset Subject-Level Rainclouds (Figure 2 & 3)
python scripts/04_visualization/plot_dataset_rainclouds.py

# Generate Delta Entropic Gradients (Figure 4 & S1)
python scripts/04_visualization/plot_delta_gradient.py

# Generate 2D State Space Maps (Figure 5 & S4)
python scripts/04_visualization/plot_2d_state_space.py

# Generate Composite Brain Map and LONO Rainclouds (Figure 6 & S5)
python scripts/04_visualization/plot_Figure6.py
python scripts/04_visualization/plot_FigureS5.py
```

4. **Generate Supplementary Figures:**
```bash
# Generate Continuous Entropic Gradients (Figure S2)
python scripts/04_visualization/plot_raw_gradient.py

# Generate Z-Scored Entropic Gradient (Figure S3)
python scripts/04_visualization/plot_entropic_gradient.py
```

For further details regarding exact software versions and computational configurations, please refer to [requirements/versions_info.txt](requirements/versions_info.txt).

---

## Acknowledgements & Atlas Citations

This repository includes derived NIfTI atlas masks (in `scripts/01_parcelling/masks/`) strictly for reproducibility purposes. If you use this pipeline, please ensure you cite the original creators of these open-science resources:

1. **AAL Atlas**: Tzourio-Mazoyer, N., et al. (2002). Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. *Neuroimage*, 15(1), 273-289.
2. **Schaefer 1000 Parcellation**: Schaefer, A., et al. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28(9), 3095-3114.
3. **Tian Subcortical Atlas**: Tian, Y., et al. (2020). Topographic organization of the human subcortex unveiled with functional connectivity gradients. *Nature Neuroscience*, 23(11), 1421-1432.
4. **Brain Connectivity Toolbox**: Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: uses and interpretations. *Neuroimage*, 52(3), 1059-1069.

---

## Contact

For questions, issues, or collaborations regarding this repository and the manuscript, please contact:
* **Dante Sebastian Galvan Rial** — [sebas.galvan@mi.unc.edu.ar](mailto:sebas.galvan@mi.unc.edu.ar)

