# Electrical Grid Stability Simulated Data

**Summary:** The local stability analysis of the 4-node star system (electricity producer is in the center) implementing Decentral Smart Grid Control concept.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Regression |
| **Data Source** | Simulated |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2018-11-15 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Electrical Grid Stability Simulated Data |
| **Number of Features** | 12 |
| **Number of Instances** | 10000 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | No |

## Description

The analysis is performed for different sets of input values using the methodology similar to that described in [SchÃÂ¤fer, Benjamin, et al. 'Taming instabilities in power grid networks by decentralized control.' The European Physical Journal Special Topics 225.3 (2016): 569-582.]. Several input values are kept the same: averaging time: 2 s; coupling strength: 8 s^-2; damping: 0.1 s^-1

11 predictive attributes, 1 non-predictive(p1), 2 goal fields: 
1. tau[x]: reaction time of participant (real from the range [0.5,10]s). Tau1 - the value for electricity producer. 
2. p[x]: nominal power consumed(negative)/produced(positive)(real). For consumers from the range [-0.5,-2]s^-2; p1 = abs(p2 + p3 + p4) 
3. g[x]: coefficient (gamma) proportional to price elasticity (real from the range [0.05,1]s^-1). g1 - the value for electricity producer. 
4. stab: the maximal real part of the characteristic equation root (if positive - the system is linearly unstable)(real) 
5. stabf: the stability label of the system (categorical: stable/unstable)

## Tags

Classification, Decentralized control, Electrical grid stability, Power system dynamics, Regression, Simulation data, Smart grid control

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Electrical+Grid+Stability+Simulated+Data)

[⬅️ Back to Index](../README.md)
