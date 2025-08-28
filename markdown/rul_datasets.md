# RUL Datasets

**Summary:** This repository provides a collection of benchmark Remaining Useful Life datasets packaged as PyTorch Lightning Data Modules for integration into PyTorch Lightning workflows.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Both |
| **Dataset Characteristics** | Time-Series, Multivariate |
| **Date Donated** | Information not available |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | RUL Datasets |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | GitHub |
| **Time Series** | Yes |

## Description

This library contains a collection of common benchmark datasets for remaining useful lifetime (RUL) estimation. They are provided as LightningDataModules to be readily used in PyTorch Lightning.

Currently, five datasets are supported: C-MAPSS Turbofan Degradation Dataset, FEMTO (PRONOSTIA) Bearing Dataset, XJTU-SY Bearing Dataset, N-C-MAPSS New Turbofan Degradation Dataset, and a Dummy dataset for testing and debugging purposes.

In addition to the basic data modules, the library offers higher-order data modules designed for advanced experiments in transfer learning, unsupervised domain adaptation, and semi-supervised learning. These higher-order modules accept one or more of the basic modules as inputs and adapt them to specific use-case requirements.

## Tags

PyTorch Lightning, bearing dataset, domain adaptation, remaining useful life, time-series data, transfer learning, turbofan engine

## References

- [GitHub Repository](https://github.com/tilman151/rul-datasets)
- [Project Website](https://krokotsch.eu/rul-datasets)

[⬅️ Back to Index](../README.md)
