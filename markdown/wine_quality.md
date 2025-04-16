# Wine Quality

**Summary:** Two datasets are included, related to red and white vinho verde wine samples, from the north of Portugal. The goal is to model wine quality based on physicochemical tests.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2009-10-06 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Wine Quality |
| **Number of Features** | 11 |
| **Number of Instances** | 4898 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | No |

## Description

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, it could be interesting to test feature selection methods.

Input variables (based on physicochemical tests): fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol. Output variable (based on sensory data): quality (score between 0 and 10).

## Tags

Classification, Physicochemical tests, Portuguese Vinho Verde, Red and white wine, Regression, Wine quality, Wine samples

## References

- [Modeling wine preferences by data mining from physicochemical properties - P. Cortez et al., 2009](https://www.semanticscholar.org/paper/Modeling-wine-preferences-by-data-mining-from-Cortez-Cerdeira/bf15a0ccc14ac1deb5cea570c870389c16be019c)
- [Wine Quality Dataset at UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)

[⬅️ Back to Index](../README.md)
