# Categorical Omnibus LME Results (Delta Z-Scores)

This report tests whether the entropy of each state significantly differs from baseline (0), without imposing any a priori gradient order.

**Formula:** `Delta_Z ~ 0 + C(Condition) + (1 | Subject)`

## AAL - dSW

```text
                                  Coef. Std.Err.       z  P>|z|  [0.025  0.975]  p_FDR
C(Condition)[Anaes. Recovery]    -0.018    0.322  -0.057  0.955  -0.650   0.614  0.955
C(Condition)[DMT]                 0.832    0.347   2.395  0.017   0.151   1.513  0.029
C(Condition)[Deep Anaesthesia]   -0.801    0.322  -2.483  0.013  -1.433  -0.169  0.029
C(Condition)[LSD]                 0.678    0.338   2.007  0.045   0.016   1.341  0.063
C(Condition)[Light Anaesthesia]  -0.578    0.322  -1.794  0.073  -1.210   0.054  0.085
C(Condition)[Modafinil]           0.906    0.360   2.520  0.012   0.201   1.611  0.029
C(Condition)[Schizophrenia]       1.015    0.188   5.399  0.000   0.647   1.383  0.000
Group Var                         0.595    0.301                                      
```

## AAL - dFC

```text
                                  Coef. Std.Err.       z  P>|z|  [0.025  0.975]  p_FDR
C(Condition)[Anaes. Recovery]    -0.192    0.286  -0.671  0.502  -0.752   0.369  0.586
C(Condition)[DMT]                -0.704    0.308  -2.289  0.022  -1.307  -0.101  0.031
C(Condition)[Deep Anaesthesia]   -0.837    0.286  -2.926  0.003  -1.397  -0.276  0.008
C(Condition)[LSD]                -0.927    0.298  -3.106  0.002  -1.511  -0.342  0.007
C(Condition)[Light Anaesthesia]  -0.802    0.286  -2.807  0.005  -1.363  -0.242  0.009
C(Condition)[Modafinil]          -0.024    0.318  -0.075  0.940  -0.648   0.600  0.940
C(Condition)[Schizophrenia]       0.739    0.167   4.435  0.000   0.413   1.066  0.000
Group Var                         0.460    0.217                                      
```

## Tian_Schaefer - dSW

```text
                                  Coef. Std.Err.       z  P>|z|  [0.025  0.975]  p_FDR
C(Condition)[Anaes. Recovery]     0.502    0.251   1.997  0.046   0.009   0.994  0.064
C(Condition)[DMT]                 0.449    0.276   1.628  0.103  -0.091   0.989  0.106
C(Condition)[Deep Anaesthesia]   -0.607    0.251  -2.416  0.016  -1.099  -0.114  0.042
C(Condition)[LSD]                 0.428    0.265   1.614  0.106  -0.092   0.948  0.106
C(Condition)[Light Anaesthesia]  -0.539    0.251  -2.145  0.032  -1.031  -0.046  0.056
C(Condition)[Modafinil]           0.672    0.284   2.366  0.018   0.115   1.229  0.042
C(Condition)[Schizophrenia]       0.373    0.146   2.546  0.011   0.086   0.660  0.042
Group Var                         0.245    0.133                                      
```

## Tian_Schaefer - dFC

```text
                                  Coef. Std.Err.       z  P>|z|  [0.025 0.975]  p_FDR
C(Condition)[Anaes. Recovery]     0.107    0.295   0.363  0.717  -0.472  0.686  0.842
C(Condition)[DMT]                 0.115    0.324   0.356  0.722  -0.519  0.749  0.842
C(Condition)[Deep Anaesthesia]   -0.474    0.295  -1.605  0.109  -1.053  0.105  0.253
C(Condition)[LSD]                -0.421    0.313  -1.346  0.178  -1.033  0.192  0.312
C(Condition)[Light Anaesthesia]  -0.504    0.295  -1.707  0.088  -1.083  0.075  0.253
C(Condition)[Modafinil]           0.007    0.336   0.020  0.984  -0.651  0.665  0.984
C(Condition)[Schizophrenia]       0.456    0.172   2.648  0.008   0.119  0.794  0.057
Group Var                         0.271    0.178                                     
```

