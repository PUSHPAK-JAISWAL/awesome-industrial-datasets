# AI4I 2020 Predictive Maintenance Dataset

**Summary:** The AI4I 2020 Predictive Maintenance Dataset is a synthetic dataset that reflects real predictive maintenance data encountered in industry.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Regression, Causal-Discovery |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2020-08-29 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | AI4I 2020 Predictive Maintenance Dataset |
| **Number of Features** | 6 |
| **Number of Instances** | 10000 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Yes |

## Description

Since real predictive maintenance datasets are generally difficult to obtain and in particular difficult to publish, we present and provide a synthetic dataset that reflects real predictive maintenance encountered in industry to the best of our knowledge.

The dataset consists of 10,000 data points stored as rows with 14 features in columns. UID is a unique identifier ranging from 1 to 10000. Product ID consists of letter L, M, or H indicating product quality variants and variant-specific serial number. Air temperature [K] and Process temperature [K] are generated using a random walk process with normalization. Rotational speed [rpm] is calculated with noise, Torque [Nm] values are normally distributed. Tool wear [min] is modified according to product quality variant.

The machine failure label indicates if the machine has failed based on five independent failure modes: tool wear failure (TWF), heat dissipation failure (HDF), power failure (PWF), overstrain failure (OSF), and random failures (RNF). A failure occurs if any one of these modes is true and the machine failure label is set to 1. This makes it non-transparent to machine learning methods which failure mode caused the failure.

## Tags

Classification, Machine failure detection, Multivariate data, Predictive maintenance, Regression, Synthetic data, Time-series data

## References

- [AI4I 2020 Predictive Maintenance Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset)
- [Explainable Artificial Intelligence for Predictive Maintenance Applications](https://www.semanticscholar.org/paper/b609c8e9ec6a2b8c642810953ef6dffe5766f7c1)
- [DOI: 10.24432/C5HS5C](https://doi.org/10.24432/C5HS5C)

[⬅️ Back to Index](../README.md)
