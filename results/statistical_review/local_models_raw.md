# Local Models (Raw Output)

Note: Paired designs use MixedLM (random subject intercepts). Unpaired designs use OLS to avoid mathematically invalid singular covariance matrices.

---

## METRIC: AAL_dSW

---

### Anaesthesia (Paired) (AAL_dSW)

```text
                Mixed Linear Model Regression Results
======================================================================
Model:                   MixedLM      Dependent Variable:      SampEn 
No. Observations:        68           Method:                  REML   
No. Groups:              17           Scale:                   0.0185 
Min. group size:         4            Log-Likelihood:          31.1596
Max. group size:         4            Converged:               Yes    
Mean group size:         4.0                                          
----------------------------------------------------------------------
                            Coef.  Std.Err.   z    P>|z| [0.025 0.975]
----------------------------------------------------------------------
Intercept                    1.156    0.033 35.014 0.000  1.091  1.221
dataset[T.anestesia_block2] -0.098    0.047 -2.094 0.036 -0.189 -0.006
dataset[T.anestesia_block3] -0.135    0.047 -2.899 0.004 -0.227 -0.044
dataset[T.anestesia_block4] -0.003    0.047 -0.066 0.947 -0.095  0.088
Group Var                    0.000    0.025                           
======================================================================

```

#### FDR Correction (Benjamini-Hochberg)

- **dataset[T.anestesia_block2]**: Raw p = 0.0363 --> **FDR Corrected p = 0.0544**
- **dataset[T.anestesia_block3]**: Raw p = 0.0037 --> **FDR Corrected p = 0.0112**
- **dataset[T.anestesia_block4]**: Raw p = 0.9473 --> **FDR Corrected p = 0.9473**

### LSD (Paired) (AAL_dSW)

```text
         Mixed Linear Model Regression Results
========================================================
Model:             MixedLM  Dependent Variable:  SampEn 
No. Observations:  30       Method:              REML   
No. Groups:        15       Scale:               0.0094 
Min. group size:   2        Log-Likelihood:      20.2197
Max. group size:   2        Converged:           Yes    
Mean group size:   2.0                                  
--------------------------------------------------------
               Coef. Std.Err.   z    P>|z| [0.025 0.975]
--------------------------------------------------------
Intercept      1.186    0.028 42.674 0.000  1.131  1.240
dataset[T.lsd] 0.078    0.035  2.201 0.028  0.009  0.148
Group Var      0.002    0.038                           
========================================================

```

### DMT (Paired) (AAL_dSW)

```text
           Mixed Linear Model Regression Results
============================================================
Model:               MixedLM   Dependent Variable:   SampEn 
No. Observations:    28        Method:               REML   
No. Groups:          14        Scale:                0.0071 
Min. group size:     2         Log-Likelihood:       24.4050
Max. group size:     2         Converged:            Yes    
Mean group size:     2.0                                    
------------------------------------------------------------
                   Coef. Std.Err.   z    P>|z| [0.025 0.975]
------------------------------------------------------------
Intercept          1.205    0.023 52.700 0.000  1.160  1.249
dataset[T.dmt_dmt] 0.057    0.032  1.777 0.076 -0.006  0.119
Group Var          0.000    0.025                           
============================================================

```

### Modafinil (Unpaired) (AAL_dSW)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.125
Model:                            OLS   Adj. R-squared:                  0.086
Method:                 Least Squares   F-statistic:                     3.156
Date:                Fri, 05 Jun 2026   Prob (F-statistic):             0.0895
Time:                        22:45:19   Log-Likelihood:                 13.147
No. Observations:                  24   AIC:                            -22.29
Df Residuals:                      22   BIC:                            -19.94
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
===================================================================================================
                                      coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------------
Intercept                           1.0318      0.044     23.417      0.000       0.940       1.123
dataset[T.modafinil_condition1]     0.1064      0.060      1.777      0.089      -0.018       0.231
==============================================================================
Omnibus:                        2.450   Durbin-Watson:                   2.066
Prob(Omnibus):                  0.294   Jarque-Bera (JB):                1.440
Skew:                           0.313   Prob(JB):                        0.487
Kurtosis:                       1.976   Cond. No.                         2.73
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

### Schizophrenia (Unpaired) (AAL_dSW)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.159
Model:                            OLS   Adj. R-squared:                  0.150
Method:                 Least Squares   F-statistic:                     18.48
Date:                Fri, 05 Jun 2026   Prob (F-statistic):           4.05e-05
Time:                        22:45:19   Log-Likelihood:                 23.516
No. Observations:                 100   AIC:                            -43.03
Df Residuals:                      98   BIC:                            -37.82
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                1.1818      0.027     43.254      0.000       1.128       1.236
dataset[T.ucla_schz]     0.1661      0.039      4.299      0.000       0.089       0.243
==============================================================================
Omnibus:                        0.762   Durbin-Watson:                   2.425
Prob(Omnibus):                  0.683   Jarque-Bera (JB):                0.834
Skew:                           0.080   Prob(JB):                        0.659
Kurtosis:                       2.582   Cond. No.                         2.62
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

---

## METRIC: AAL_dFC

---

### Anaesthesia (Paired) (AAL_dFC)

```text
                Mixed Linear Model Regression Results
======================================================================
Model:                   MixedLM      Dependent Variable:      SampEn 
No. Observations:        68           Method:                  REML   
No. Groups:              17           Scale:                   0.0053 
Min. group size:         4            Log-Likelihood:          70.9103
Max. group size:         4            Converged:               Yes    
Mean group size:         4.0                                          
----------------------------------------------------------------------
                            Coef.  Std.Err.   z    P>|z| [0.025 0.975]
----------------------------------------------------------------------
Intercept                    0.733    0.018 41.304 0.000  0.698  0.767
dataset[T.anestesia_block2] -0.061    0.025 -2.419 0.016 -0.110 -0.012
dataset[T.anestesia_block3] -0.063    0.025 -2.522 0.012 -0.112 -0.014
dataset[T.anestesia_block4] -0.015    0.025 -0.578 0.563 -0.064  0.035
Group Var                    0.000    0.011                           
======================================================================

```

#### FDR Correction (Benjamini-Hochberg)

- **dataset[T.anestesia_block2]**: Raw p = 0.0156 --> **FDR Corrected p = 0.0233**
- **dataset[T.anestesia_block3]**: Raw p = 0.0117 --> **FDR Corrected p = 0.0233**
- **dataset[T.anestesia_block4]**: Raw p = 0.5632 --> **FDR Corrected p = 0.5632**

### LSD (Paired) (AAL_dFC)

```text
            Mixed Linear Model Regression Results
=============================================================
Model:                MixedLM   Dependent Variable:   SampEn 
No. Observations:     30        Method:               REML   
No. Groups:           15        Scale:                0.0023 
Min. group size:      2         Log-Likelihood:       36.7101
Max. group size:      2         Converged:            Yes    
Mean group size:      2.0                                    
-------------------------------------------------------------
                   Coef.  Std.Err.   z    P>|z| [0.025 0.975]
-------------------------------------------------------------
Intercept           0.693    0.016 43.350 0.000  0.662  0.725
dataset[T.lsd_lsd] -0.059    0.017 -3.406 0.001 -0.094 -0.025
Group Var           0.002    0.030                           
=============================================================

```

### DMT (Paired) (AAL_dFC)

```text
            Mixed Linear Model Regression Results
=============================================================
Model:                MixedLM   Dependent Variable:   SampEn 
No. Observations:     28        Method:               REML   
No. Groups:           14        Scale:                0.0055 
Min. group size:      2         Log-Likelihood:       28.2033
Max. group size:      2         Converged:            Yes    
Mean group size:      2.0                                    
-------------------------------------------------------------
                   Coef.  Std.Err.   z    P>|z| [0.025 0.975]
-------------------------------------------------------------
Intercept           0.687    0.020 34.783 0.000  0.648  0.726
dataset[T.dmt_dmt] -0.057    0.028 -2.029 0.042 -0.111 -0.002
Group Var           0.000    0.021                           
=============================================================

```

### Modafinil (Unpaired) (AAL_dFC)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.000
Model:                            OLS   Adj. R-squared:                 -0.045
Method:                 Least Squares   F-statistic:                  0.001392
Date:                Fri, 05 Jun 2026   Prob (F-statistic):              0.971
Time:                        22:45:19   Log-Likelihood:                 29.892
No. Observations:                  24   AIC:                            -55.78
Df Residuals:                      22   BIC:                            -53.43
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                0.7448      0.022     33.962      0.000       0.699       0.790
dataset[T.modafinil]     0.0011      0.030      0.037      0.971      -0.061       0.063
==============================================================================
Omnibus:                        6.167   Durbin-Watson:                   1.991
Prob(Omnibus):                  0.046   Jarque-Bera (JB):                2.507
Skew:                           0.471   Prob(JB):                        0.285
Kurtosis:                       1.727   Cond. No.                         2.73
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

### Schizophrenia (Unpaired) (AAL_dFC)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.136
Model:                            OLS   Adj. R-squared:                  0.127
Method:                 Least Squares   F-statistic:                     15.39
Date:                Fri, 05 Jun 2026   Prob (F-statistic):           0.000162
Time:                        22:45:19   Log-Likelihood:                 90.875
No. Observations:                 100   AIC:                            -177.7
Df Residuals:                      98   BIC:                            -172.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                0.7306      0.014     52.445      0.000       0.703       0.758
dataset[T.ucla_schz]     0.0773      0.020      3.923      0.000       0.038       0.116
==============================================================================
Omnibus:                        4.727   Durbin-Watson:                   1.864
Prob(Omnibus):                  0.094   Jarque-Bera (JB):                4.252
Skew:                           0.365   Prob(JB):                        0.119
Kurtosis:                       3.698   Cond. No.                         2.62
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

---

## METRIC: TianSchaefer_dSW

---

### Anaesthesia (Paired) (TianSchaefer_dSW)

```text
                 Mixed Linear Model Regression Results
========================================================================
Model:                   MixedLM       Dependent Variable:       SampEn 
No. Observations:        68            Method:                   REML   
No. Groups:              17            Scale:                    0.0239 
Min. group size:         4             Log-Likelihood:           18.9290
Max. group size:         4             Converged:                Yes    
Mean group size:         4.0                                            
------------------------------------------------------------------------
                              Coef.  Std.Err.   z    P>|z| [0.025 0.975]
------------------------------------------------------------------------
Intercept                      0.712    0.040 17.588 0.000  0.633  0.792
dataset[T.anestesia_light]    -0.092    0.053 -1.736 0.082 -0.196  0.012
dataset[T.anestesia_deep]     -0.104    0.053 -1.956 0.050 -0.208  0.000
dataset[T.anestesia_recovery]  0.086    0.053  1.617 0.106 -0.018  0.190
Group Var                      0.004    0.026                           
========================================================================

```

#### FDR Correction (Benjamini-Hochberg)

- **dataset[T.anestesia_light]**: Raw p = 0.0825 --> **FDR Corrected p = 0.1058**
- **dataset[T.anestesia_deep]**: Raw p = 0.0505 --> **FDR Corrected p = 0.1058**
- **dataset[T.anestesia_recovery]**: Raw p = 0.1058 --> **FDR Corrected p = 0.1058**

### LSD (Paired) (TianSchaefer_dSW)

```text
           Mixed Linear Model Regression Results
============================================================
Model:                MixedLM   Dependent Variable:   SampEn
No. Observations:     30        Method:               REML  
No. Groups:           15        Scale:                0.0284
Min. group size:      2         Log-Likelihood:       4.5175
Max. group size:      2         Converged:            Yes   
Mean group size:      2.0                                   
------------------------------------------------------------
                   Coef. Std.Err.   z    P>|z| [0.025 0.975]
------------------------------------------------------------
Intercept          1.021    0.049 20.937 0.000  0.926  1.117
dataset[T.lsd_lsd] 0.094    0.062  1.527 0.127 -0.027  0.215
Group Var          0.007    0.068                           
============================================================

```

### DMT (Paired) (TianSchaefer_dSW)

```text
           Mixed Linear Model Regression Results
===========================================================
Model:              MixedLM   Dependent Variable:   SampEn 
No. Observations:   28        Method:               REML   
No. Groups:         14        Scale:                0.0355 
Min. group size:    2         Log-Likelihood:       -7.6142
Max. group size:    2         Converged:            Yes    
Mean group size:    2.0                                    
-----------------------------------------------------------
                   Coef. Std.Err.   z   P>|z| [0.025 0.975]
-----------------------------------------------------------
Intercept          0.634    0.093 6.807 0.000  0.452  0.817
dataset[T.dmt_dmt] 0.127    0.071 1.781 0.075 -0.013  0.266
Group Var          0.086    0.305                          
===========================================================

```

### Modafinil (Unpaired) (TianSchaefer_dSW)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.061
Model:                            OLS   Adj. R-squared:                  0.016
Method:                 Least Squares   F-statistic:                     1.364
Date:                Fri, 05 Jun 2026   Prob (F-statistic):              0.256
Time:                        22:45:19   Log-Likelihood:                 13.922
No. Observations:                  23   AIC:                            -23.84
Df Residuals:                      21   BIC:                            -21.57
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                0.8114      0.044     18.561      0.000       0.720       0.902
dataset[T.modafinil]     0.0679      0.058      1.168      0.256      -0.053       0.189
==============================================================================
Omnibus:                        8.643   Durbin-Watson:                   2.277
Prob(Omnibus):                  0.013   Jarque-Bera (JB):                6.500
Skew:                          -1.006   Prob(JB):                       0.0388
Kurtosis:                       4.654   Cond. No.                         2.80
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

### Schizophrenia (Unpaired) (TianSchaefer_dSW)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.053
Model:                            OLS   Adj. R-squared:                  0.044
Method:                 Least Squares   F-statistic:                     5.518
Date:                Fri, 05 Jun 2026   Prob (F-statistic):             0.0208
Time:                        22:45:19   Log-Likelihood:                 58.194
No. Observations:                 100   AIC:                            -112.4
Df Residuals:                      98   BIC:                            -107.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                0.8385      0.019     43.411      0.000       0.800       0.877
dataset[T.ucla_schz]     0.0642      0.027      2.349      0.021       0.010       0.118
==============================================================================
Omnibus:                        7.549   Durbin-Watson:                   1.894
Prob(Omnibus):                  0.023   Jarque-Bera (JB):               10.693
Skew:                          -0.313   Prob(JB):                      0.00476
Kurtosis:                       4.474   Cond. No.                         2.62
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

---

## METRIC: TianSchaefer_dFC

---

### Anaesthesia (Paired) (TianSchaefer_dFC)

```text
                Mixed Linear Model Regression Results
======================================================================
Model:                   MixedLM      Dependent Variable:      SampEn 
No. Observations:        68           Method:                  REML   
No. Groups:              17           Scale:                   0.0033 
Min. group size:         4            Log-Likelihood:          85.2043
Max. group size:         4            Converged:               No     
Mean group size:         4.0                                          
----------------------------------------------------------------------
                            Coef.  Std.Err.   z    P>|z| [0.025 0.975]
----------------------------------------------------------------------
Intercept                    0.622    0.014 43.773 0.000  0.594  0.650
dataset[T.anestesia_block2] -0.030    0.020 -1.531 0.126 -0.069  0.008
dataset[T.anestesia_block3] -0.028    0.020 -1.439 0.150 -0.067  0.010
dataset[T.anestesia_block4]  0.006    0.020  0.325 0.745 -0.032  0.045
Group Var                    0.000    0.011                           
======================================================================

```

#### FDR Correction (Benjamini-Hochberg)

- **dataset[T.anestesia_block2]**: Raw p = 0.1258 --> **FDR Corrected p = 0.2253**
- **dataset[T.anestesia_block3]**: Raw p = 0.1502 --> **FDR Corrected p = 0.2253**
- **dataset[T.anestesia_block4]**: Raw p = 0.7451 --> **FDR Corrected p = 0.7451**

### LSD (Paired) (TianSchaefer_dFC)

```text
            Mixed Linear Model Regression Results
=============================================================
Model:                MixedLM   Dependent Variable:   SampEn 
No. Observations:     30        Method:               REML   
No. Groups:           15        Scale:                0.0019 
Min. group size:      2         Log-Likelihood:       42.6426
Max. group size:      2         Converged:            Yes    
Mean group size:      2.0                                    
-------------------------------------------------------------
                   Coef.  Std.Err.   z    P>|z| [0.025 0.975]
-------------------------------------------------------------
Intercept           0.592    0.012 47.535 0.000  0.568  0.617
dataset[T.lsd_lsd] -0.016    0.016 -1.019 0.308 -0.048  0.015
Group Var           0.000    0.017                           
=============================================================

```

### DMT (Paired) (TianSchaefer_dFC)

```text
           Mixed Linear Model Regression Results
============================================================
Model:               MixedLM   Dependent Variable:   SampEn 
No. Observations:    28        Method:               REML   
No. Groups:          14        Scale:                0.0139 
Min. group size:     2         Log-Likelihood:       16.0219
Max. group size:     2         Converged:            Yes    
Mean group size:     2.0                                    
------------------------------------------------------------
                   Coef. Std.Err.   z    P>|z| [0.025 0.975]
------------------------------------------------------------
Intercept          0.553    0.032 17.540 0.000  0.492  0.615
dataset[T.dmt_dmt] 0.019    0.045  0.425 0.671 -0.068  0.106
Group Var          0.000    0.044                           
============================================================

```

### Modafinil (Unpaired) (TianSchaefer_dFC)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.000
Model:                            OLS   Adj. R-squared:                 -0.045
Method:                 Least Squares   F-statistic:                  0.006260
Date:                Fri, 05 Jun 2026   Prob (F-statistic):              0.938
Time:                        22:45:20   Log-Likelihood:                 36.567
No. Observations:                  24   AIC:                            -69.13
Df Residuals:                      22   BIC:                            -66.78
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                0.6078      0.017     36.605      0.000       0.573       0.642
dataset[T.modafinil]     0.0018      0.023      0.079      0.938      -0.045       0.049
==============================================================================
Omnibus:                        1.487   Durbin-Watson:                   2.422
Prob(Omnibus):                  0.476   Jarque-Bera (JB):                0.997
Skew:                          -0.495   Prob(JB):                        0.607
Kurtosis:                       2.864   Cond. No.                         2.73
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

### Schizophrenia (Unpaired) (TianSchaefer_dFC)

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 SampEn   R-squared:                       0.056
Model:                            OLS   Adj. R-squared:                  0.047
Method:                 Least Squares   F-statistic:                     5.861
Date:                Fri, 05 Jun 2026   Prob (F-statistic):             0.0173
Time:                        22:45:20   Log-Likelihood:                 103.08
No. Observations:                 100   AIC:                            -202.2
Df Residuals:                      98   BIC:                            -196.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept                0.6051      0.012     49.070      0.000       0.581       0.630
dataset[T.ucla_schz]     0.0422      0.017      2.421      0.017       0.008       0.077
==============================================================================
Omnibus:                        3.473   Durbin-Watson:                   1.958
Prob(Omnibus):                  0.176   Jarque-Bera (JB):                2.814
Skew:                          -0.371   Prob(JB):                        0.245
Kurtosis:                       3.353   Cond. No.                         2.62
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

