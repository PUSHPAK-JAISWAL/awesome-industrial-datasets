# SECOM

**Summary:** Data from a semi-conductor manufacturing process where each sample represents a production entity with associated measured features and pass/fail labels.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Causal-Discovery |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2008-11-18 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Yes |
| **Name** | SECOM |
| **Number of Features** | 591 |
| **Number of Instances** | 1567 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Information not available |

## Description

A complex modern semi-conductor manufacturing process is monitored using signals collected from sensors and process measurement points. These signals contain a mixture of useful, irrelevant information, and noise, with many more signals measured than those actually needed. Feature selection is applied to identify the most relevant signals, which helps process engineers determine key factors contributing to yield variations.

The dataset consists of 1567 examples, each with 591 features, and an associated label indicating pass (-1) or fail (1) for in-house line testing along with a date/time stamp. The data contains missing values represented as 'NaN', which must be handled in pre-processing or during analysis.

Feature selection techniques are investigated as intelligent systems methods to rank features by their impact on overall yield. Baseline results from various feature selection methods using a simple kernel ridge classifier and 10-fold cross-validation are provided to guide initial analyses.

## Tags

Classification, Feature selection, Missing values, Multivariate data, Semi-conductor manufacturing, Sensor data, Yield prediction

## References

- [McCann, M. & Johnston, A. (2008). SECOM [Dataset]. UCI Machine Learning Repository.](https://doi.org/10.24432/C54305)
- [UCI SECOM Dataset](http://archive.ics.uci.edu/ml/datasets/SECOM)

[⬅️ Back to Index](../README.md)
