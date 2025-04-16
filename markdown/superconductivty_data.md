# Superconductivty Data

**Summary:** Two files contain data on 21263 superconductors and their relevant features. The goal is to predict the critical temperature based on the features extracted.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2018-10-11 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Superconductivty Data |
| **Number of Features** | 81 |
| **Number of Instances** | 21263 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | No |

## Description

There are two files: (1) train.csv contains 81 features extracted from 21263 superconductors along with the critical temperature in the 82nd column, (2) unique_m.csv contains the chemical formula broken up for all the 21263 superconductors from the train.csv file. The last two columns have the critical temperature and chemical formula. The original data comes from http://supercon.nims.go.jp/index_en.html which is public.

The goal here is to predict the critical temperature based on the features extracted. The dataset includes features such as number_of_elements, mean_atomic_mass, and various weighted means, geometric means, and entropies of atomic mass among others.

The dataset is labeled and contains no missing values, and is used for regression tasks related to superconductivity in physics and chemistry.

## Tags

Chemical formula data, Critical temperature prediction, Multivariate data, No missing values, Physics and Chemistry, Real-valued features, Superconductors

## References

- [A data-driven statistical model for predicting the critical temperature of a superconductor by K. Hamidieh (2018)](https://www.semanticscholar.org/paper/A-data-driven-statistical-model-for-predicting-the-Hamidieh/b3bea0ac481f0869cb746f3b44d5689bf1a9b924)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Superconductivty+Data)
- [Dataset DOI](https://doi.org/10.24432/C53P47)

[⬅️ Back to Index](../README.md)
