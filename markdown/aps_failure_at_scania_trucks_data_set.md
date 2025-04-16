# APS Failure at Scania Trucks

**Summary:** The datasets' positive class consists of component failures for a specific component of the Air Pressure system (APS) in Scania trucks. The negative class consists of trucks with failures for components not related to the APS.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2017-12-07 |
| **Feature Type** | Integer, Real |
| **Labeled** | Yes |
| **Missing Values** | Yes |
| **Name** | APS Failure at Scania Trucks |
| **Number of Features** | 171 |
| **Number of Instances** | 60000 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Information not available |

## Description

The dataset consists of data collected from heavy Scania trucks in everyday usage. The system in focus is the Air Pressure system (APS) which generates pressurized air that is utilized in various functions in a truck, such as braking and gear changes. The dataset's positive class consists of component failures for a specific component of the APS system, while the negative class consists of trucks with failures for components not related to the APS. The data is a subset selected by experts from all available data.

The training set contains 60,000 examples in total: 59,000 belonging to the negative class and 1,000 to the positive class. The test set contains 16,000 examples. The attributes of the data have been anonymized for proprietary reasons and comprise both single numerical counters and histograms consisting of bins with different conditions. There are 171 attributes in total, of which 7 are histogram variables. Missing values are denoted by 'na'.

The dataset was part of an Industrial Challenge 2016 at the 15th International Symposium on Intelligent Data Analysis (IDA). The evaluation metric is a cost-based misclassification metric, where costs for false positives and false negatives differ significantly, reflecting the practical consequences of errors in a maintenance context.

## Tags

Air Pressure System, Anonymized features, Component failure, Fault detection, Heavy trucks, Industrial challenge dataset, Scania trucks

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks)
- [Dataset DOI](https://doi.org/10.24432/C51S51)

[⬅️ Back to Index](../README.md)
