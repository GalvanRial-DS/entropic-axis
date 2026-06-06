# Statistical Reporting for Supplementary Figures

This document outlines the exact statistical models and values (Coefficient/Estimate, 95% CI, and p-values) used to generate the significance markers in each Supplementary Figure. 

---

## 1. Figures S1, S2, S3: Standardised Gradients (Unified LME Models)
**Statistical Model:** Unified Linear Mixed-Effects Model (LME) using Z-scored values. Formula: `Delta_Z ~ 0 + C(Condition) + (1 | Subject)`.
**Correction:** Uncorrected (raw) p-values are reported, as the model jointly estimates all conditions within a single unified framework.

### Figure S1: AAL dSW
* **Deep Anaesthesia:** Coef = -0.58, 95% CI [-1.02, -0.15], $p_{raw} = 0.013$ (*)
* **Light Anaesthesia:** Coef = -0.42, 95% CI [-0.85, 0.02], $p_{raw} = 0.073$ (†)
* **Anaes. Recovery:** Coef = -0.01, 95% CI [-0.44, 0.42], $p_{raw} = 0.955$
* **LSD:** Coef = +0.67, 95% CI [0.01, 1.34], $p_{raw} = 0.045$ (*)
* **DMT:** Coef = +0.76, 95% CI [0.08, 1.44], $p_{raw} = 0.017$ (*)
* **Modafinil:** Coef = +0.78, 95% CI [0.10, 1.46], $p_{raw} = 0.012$ (*)
* **Schizophrenia:** Coef = +0.63, 95% CI [0.27, 0.98], $p_{raw} < 0.001$ (***)

### Figure S2: AAL dFC
* **Deep Anaesthesia:** Coef = -0.66, 95% CI [-1.15, -0.18], $p_{raw} = 0.007$ (**)
* **Light Anaesthesia:** Coef = -0.64, 95% CI [-1.13, -0.16], $p_{raw} = 0.010$ (*)
* **Anaes. Recovery:** Coef = -0.16, 95% CI [-0.64, 0.33], $p_{raw} = 0.537$
* **LSD:** Coef = -1.13, 95% CI [-1.88, -0.37], $p_{raw} = 0.002$ (**)
* **DMT:** Coef = -1.54, 95% CI [-2.25, -0.83], $p_{raw} < 0.001$ (***)
* **Modafinil:** Coef = +0.12, 95% CI [-0.64, 0.88], $p_{raw} = 0.710$
* **Schizophrenia:** Coef = +0.67, 95% CI [0.27, 1.07], $p_{raw} < 0.001$ (***)

### Figure S3: Tian-Schaefer dFC
* **Deep Anaesthesia:** Coef = -0.47, 95% CI [-1.05, 0.11], $p_{raw} = 0.109$
* **Light Anaesthesia:** Coef = -0.50, 95% CI [-1.08, 0.08], $p_{raw} = 0.088$ (†)
* **Anaes. Recovery:** Coef = +0.11, 95% CI [-0.47, 0.69], $p_{raw} = 0.717$
* **LSD:** Coef = -0.42, 95% CI [-1.04, 0.19], $p_{raw} = 0.177$
* **DMT:** Coef = +0.14, 95% CI [-0.49, 0.78], $p_{raw} = 0.661$
* **Modafinil:** Coef = +0.06, 95% CI [-0.60, 0.72], $p_{raw} = 0.849$
* **Schizophrenia:** Coef = +0.46, 95% CI [0.12, 0.79], $p_{raw} = 0.008$ (**)

---

## 2. Figures S4, S5: Raw Individual Models (Rainclouds)
**Statistical Model:** Paired datasets (Anaesthesia, LSD, DMT) were modelled using a Linear Mixed-Effects model (MixedLM) with subject-specific random intercepts. Unpaired datasets (Modafinil, Schizophrenia) were modelled using Ordinary Least Squares (OLS) regression to avoid matrix singularity.
**Correction:** Uncorrected (raw) p-values are reported for all individual condition contrasts.

### Figure S4: Tian-Schaefer dSW (Raw)
* **Deep Anaesthesia:** Coef = -0.104, $p_{raw} = 0.016$ (*)
* **Light Anaesthesia:** Coef = -0.092, $p_{raw} = 0.032$ (*)
* **Anaes. Recovery:** Coef = +0.065, $p_{raw} = 0.046$ (*)
* **LSD:** Coef = +0.094, $p_{raw} = 0.111$
* **DMT:** Coef = +0.104, $p_{raw} = 0.145$
* **Modafinil:** Coef = +0.068, $p_{raw} = 0.018$ (*)
* **Schizophrenia:** Coef = +0.064, $p_{raw} = 0.011$ (*)

### Figure S5: Tian-Schaefer dFC (Raw)
* **Deep Anaesthesia:** Coef = -0.028, $p_{raw} = 0.198$
* **Light Anaesthesia:** Coef = -0.030, $p_{raw} = 0.088$ (†)
* **Anaes. Recovery:** Coef = +0.016, $p_{raw} = 0.505$
* **LSD:** Coef = -0.016, $p_{raw} = 0.281$
* **DMT:** Coef = +0.019, $p_{raw} = 0.655$
* **Modafinil:** Coef = +0.002, $p_{raw} = 0.938$
* **Schizophrenia:** Coef = +0.042, $p_{raw} = 0.008$ (**)

---

## 3. Figures 6 & S7: Leave-One-Network-Out (LONO) Analysis
**Statistical Model:** Non-parametric Wilcoxon signed-rank test (for paired datasets: Anaesthesia, LSD, DMT) and Mann-Whitney U test (for unpaired datasets: Modafinil, Schizophrenia).
**Correction:** Benjamini-Hochberg FDR correction was independently applied across the 7 resting-state networks within each dataset.

### Figure 6: LONO Sample Entropy (dSW)

### Table: Sample Entropy (SE dSW) LONO Statistics
| Dataset | Condition | Network | ΔSDI | Effect Size (r) | p (raw) | p (FDR) | Significant |
|---|---|---|---|---|---|---|---|
| LSD | LSD vs PLB | VIS | +0.0054 | +0.0667 | 0.8469 | 0.8469 | No |
| LSD | LSD vs PLB | SM | +0.0603 | +0.4167 | 0.1688 | 0.3939 | No |
| LSD | LSD vs PLB | DAN | -0.0014 | -0.1000 | 0.7615 | 0.8469 | No |
| LSD | LSD vs PLB | SAL | -0.0087 | -0.2667 | 0.3894 | 0.6815 | No |
| LSD | LSD vs PLB | LIM | -0.0069 | -0.1500 | 0.6387 | 0.8469 | No |
| LSD | LSD vs PLB | FP | -0.0219 | -0.6000 | 0.0413 | 0.1444 | No |
| LSD | LSD vs PLB | DM | -0.0378 | -0.6167 | 0.0353 | 0.1444 | No |
| DMT | DMT vs PLB | VIS | -0.0057 | -0.1053 | 0.7086 | 0.8266 | No |
| DMT | DMT vs PLB | SM | +0.0184 | +0.3053 | 0.2579 | 0.6018 | No |
| DMT | DMT vs PLB | DAN | -0.0047 | -0.1158 | 0.6794 | 0.8266 | No |
| DMT | DMT vs PLB | SAL | +0.0002 | +0.0316 | 0.9217 | 0.9217 | No |
| DMT | DMT vs PLB | LIM | -0.0175 | -0.5684 | 0.0289 | 0.1728 | No |
| DMT | DMT vs PLB | FP | -0.0246 | -0.5158 | 0.0494 | 0.1728 | No |
| DMT | DMT vs PLB | DM | -0.0208 | -0.2316 | 0.3955 | 0.6921 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | VIS | -0.0015 | +0.1029 | 0.7436 | 0.7436 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | SM | +0.0244 | +0.2647 | 0.3755 | 0.4380 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | DAN | -0.0463 | -0.7206 | 0.0092 | 0.0643 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | SAL | -0.0371 | -0.4706 | 0.1046 | 0.1464 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | LIM | -0.0254 | -0.6029 | 0.0335 | 0.0783 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | FP | -0.0541 | -0.6471 | 0.0214 | 0.0749 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | DM | -0.0450 | -0.5294 | 0.0654 | 0.1144 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | VIS | -0.0029 | -0.1176 | 0.7057 | 0.7057 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | SM | +0.0324 | +0.1471 | 0.6322 | 0.7057 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | DAN | -0.0186 | -0.2941 | 0.3225 | 0.4515 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | SAL | -0.0608 | -0.7059 | 0.0110 | 0.0385 | **Yes** |
| Anaesthesia (S) | Light Anaesthesia vs Awake | LIM | -0.0335 | -0.6176 | 0.0290 | 0.0676 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | FP | -0.0589 | -0.7647 | 0.0052 | 0.0361 | **Yes** |
| Anaesthesia (S) | Light Anaesthesia vs Awake | DM | -0.0406 | -0.4559 | 0.1167 | 0.2042 | No |
| Schizophrenia | SCHZ vs CTRL | VIS | -0.0648 | -0.3616 | 0.0019 | 0.0065 | **Yes** |
| Schizophrenia | SCHZ vs CTRL | SM | -0.0924 | -0.4112 | 0.0004 | 0.0028 | **Yes** |
| Schizophrenia | SCHZ vs CTRL | DAN | -0.0260 | -0.2048 | 0.0782 | 0.0912 | No |
| Schizophrenia | SCHZ vs CTRL | SAL | -0.0316 | -0.1544 | 0.1845 | 0.1845 | No |
| Schizophrenia | SCHZ vs CTRL | LIM | -0.0348 | -0.3208 | 0.0058 | 0.0101 | **Yes** |
| Schizophrenia | SCHZ vs CTRL | FP | -0.0362 | -0.2528 | 0.0296 | 0.0415 | **Yes** |
| Schizophrenia | SCHZ vs CTRL | DM | -0.0739 | -0.3368 | 0.0037 | 0.0087 | **Yes** |
| Modafinil | MOD vs PLB | VIS | +0.0126 | +0.1049 | 0.6851 | 0.8167 | No |
| Modafinil | MOD vs PLB | SM | +0.0123 | +0.0909 | 0.7281 | 0.8167 | No |
| Modafinil | MOD vs PLB | DAN | -0.0002 | +0.0629 | 0.8167 | 0.8167 | No |
| Modafinil | MOD vs PLB | SAL | -0.0097 | -0.1469 | 0.5623 | 0.8167 | No |
| Modafinil | MOD vs PLB | LIM | -0.0086 | -0.2168 | 0.3848 | 0.8167 | No |
| Modafinil | MOD vs PLB | FP | +0.0331 | +0.3007 | 0.2237 | 0.8167 | No |
| Modafinil | MOD vs PLB | DM | -0.0266 | -0.1888 | 0.4513 | 0.8167 | No |

### Figure S7: LONO Connectivity Magnitude (dFC)

### Table: Connectivity Magnitude Entropy (SE dFC) LONO Statistics
| Dataset | Condition | Network | ΔSDI | Effect Size (r) | p (raw) | p (FDR) | Significant |
|---|---|---|---|---|---|---|---|
| LSD | LSD vs PLB | VIS | -0.0137 | -0.3167 | 0.3028 | 0.6815 | No |
| LSD | LSD vs PLB | SM | +0.0136 | +0.3167 | 0.3028 | 0.6815 | No |
| LSD | LSD vs PLB | DAN | +0.0044 | +0.0167 | 0.9780 | 0.9780 | No |
| LSD | LSD vs PLB | SAL | -0.0109 | -0.2667 | 0.3894 | 0.6815 | No |
| LSD | LSD vs PLB | LIM | +0.0025 | +0.1500 | 0.6387 | 0.7451 | No |
| LSD | LSD vs PLB | FP | -0.0097 | -0.1500 | 0.6387 | 0.7451 | No |
| LSD | LSD vs PLB | DM | -0.0163 | -0.3000 | 0.3303 | 0.6815 | No |
| DMT | DMT vs PLB | VIS | -0.0160 | -0.5238 | 0.0400 | 0.2039 | No |
| DMT | DMT vs PLB | SM | +0.0001 | +0.0095 | 0.9854 | 0.9854 | No |
| DMT | DMT vs PLB | DAN | -0.0049 | -0.3143 | 0.2305 | 0.5379 | No |
| DMT | DMT vs PLB | SAL | -0.0058 | -0.4857 | 0.0583 | 0.2039 | No |
| DMT | DMT vs PLB | LIM | +0.0005 | -0.0190 | 0.9563 | 0.9854 | No |
| DMT | DMT vs PLB | FP | -0.0055 | -0.2095 | 0.4304 | 0.7533 | No |
| DMT | DMT vs PLB | DM | -0.0043 | -0.0762 | 0.7841 | 0.9854 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | VIS | -0.0155 | -0.2288 | 0.4307 | 0.5025 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | SM | +0.0083 | +0.1503 | 0.6112 | 0.6112 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | DAN | -0.0139 | -0.3203 | 0.2633 | 0.3686 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | SAL | -0.0113 | -0.3203 | 0.2633 | 0.3686 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | LIM | -0.0114 | -0.3464 | 0.2247 | 0.3686 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | FP | -0.0218 | -0.3464 | 0.2247 | 0.3686 | No |
| Anaesthesia (U) | Deep Anaesthesia vs Awake | DM | -0.0405 | -0.5817 | 0.0348 | 0.2435 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | VIS | -0.0161 | -0.2810 | 0.3289 | 0.9632 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | SM | -0.0013 | -0.0196 | 0.9632 | 0.9632 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | DAN | -0.0069 | -0.0850 | 0.7819 | 0.9632 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | SAL | -0.0023 | -0.0588 | 0.8536 | 0.9632 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | LIM | +0.0075 | +0.0458 | 0.8900 | 0.9632 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | FP | -0.0099 | -0.1111 | 0.7119 | 0.9632 | No |
| Anaesthesia (S) | Light Anaesthesia vs Awake | DM | -0.0258 | -0.3333 | 0.2435 | 0.9632 | No |
| Schizophrenia | SCHZ vs CTRL | VIS | +0.0150 | +0.1040 | 0.3720 | 0.5208 | No |
| Schizophrenia | SCHZ vs CTRL | SM | +0.0158 | +0.1144 | 0.3259 | 0.5208 | No |
| Schizophrenia | SCHZ vs CTRL | DAN | -0.0050 | -0.0256 | 0.8281 | 0.8281 | No |
| Schizophrenia | SCHZ vs CTRL | SAL | +0.0221 | +0.2480 | 0.0329 | 0.2301 | No |
| Schizophrenia | SCHZ vs CTRL | LIM | -0.0083 | -0.0472 | 0.6867 | 0.8012 | No |
| Schizophrenia | SCHZ vs CTRL | FP | +0.0162 | +0.1072 | 0.3574 | 0.5208 | No |
| Schizophrenia | SCHZ vs CTRL | DM | +0.0150 | +0.1472 | 0.2059 | 0.5208 | No |
| Modafinil | MOD vs PLB | VIS | +0.0086 | +0.0070 | 1.0000 | 1.0000 | No |
| Modafinil | MOD vs PLB | SM | +0.0171 | +0.2448 | 0.3247 | 0.7575 | No |
| Modafinil | MOD vs PLB | DAN | +0.0291 | +0.2448 | 0.3247 | 0.7575 | No |
| Modafinil | MOD vs PLB | SAL | +0.0039 | -0.0490 | 0.8620 | 1.0000 | No |
| Modafinil | MOD vs PLB | LIM | +0.0063 | +0.1888 | 0.4513 | 0.7899 | No |
| Modafinil | MOD vs PLB | FP | +0.0301 | +0.3846 | 0.1178 | 0.7575 | No |
| Modafinil | MOD vs PLB | DM | +0.0098 | +0.0909 | 0.7281 | 1.0000 | No |


---

## 4. Supplementary Table S1: Head-motion control

Effect of mean framewise displacement (`FD_mean`) on sample entropy, estimated separately for each dataset after controlling for condition.

| Dataset       | Model   | N   | Coef (β) | SE      | p (raw) | p (FDR) |
|:--------------|:--------|----:|---------:|--------:|--------:|--------:|
| Anaesthesia   | MixedLM |  68 |  -0.1081 |  0.0630 |  0.0865 |  0.4085 |
| Schizophrenia | OLS     | 100 |  -0.1308 |  0.1119 |  0.2451 |  0.4085 |
| Modafinil     | OLS     |  24 |   0.4539 |  0.3221 |  0.1728 |  0.4085 |
| DMT           | MixedLM |  28 |   0.0547 |  0.3507 |  0.8762 |  0.9112 |
| LSD           | MixedLM |  28 |   4.0759 | 36.5513 |  0.9112 |  0.9112 |
