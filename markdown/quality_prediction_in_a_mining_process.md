# Quality Prediction in a Mining Process

**Summary:** This dataset is about a flotation plant which is a process used to concentrate the iron ore. The target is to predict the % of Silica (impurity) in the end of the process.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2017-12-06 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Quality Prediction in a Mining Process |
| **Number of Features** | 24 |
| **Number of Instances** | Approximately 158,000+ per large time chunks, total count likely over 400,000 |
| **Source** | Kaggle |
| **Time Series** | Likely |

## Description

This dataset comes from one of the most important parts of a mining process: a flotation plant used to concentrate iron ore. The data covers a time range from March 2017 until September 2017. The dataset includes measurements taken every 20 seconds for some features and hourly for others. The columns include quality measures of the iron ore pulp before entering the flotation plant, process variables that impact ore quality such as reagent flow and air flow inside flotation columns, and process data. The target variable to predict is the percentage of silica in the iron ore concentrate, representing the impurity level.

The motivation behind predicting the silica concentration is that its lab measurement (last column) takes about one hour to be available, and predicting it earlier can empower engineers to take corrective actions proactively, reducing impurities and environmental impact. This dataset has been used for research purposes to explore predictions of impurity levels in the flotation process with goals like multi-step ahead predictions and evaluating models that exclude highly correlated features.

The dataset has been used for learning, research, and application purposes and includes well-documented and well-maintained data suitable for developing machine learning models in the manufacturing and mining domain. Related research includes deep learning techniques applied to purity prediction in froth flotation and soft sensors for process quality prediction.

## Tags

Flotation plant, Industrial manufacturing, Iron ore quality, Mining process, Process engineering, Silica impurity prediction, Time series data

## References

- [Kaggle Dataset - Quality Prediction in a Mining Process](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process)
- [Purities prediction in a manufacturing froth flotation plant: the deep learning techniques](https://link.springer.com/article/10.1007/s00521-020-04773-2)
- [Soft Sensor: Traditional Machine Learning or Deep Learning](https://www.researchgate.net/publication/329260095_Soft_Sensor_Traditional_Machine_Learning_or_Deep_Learning)
- [Machine Learning-based Quality Prediction in the Froth Flotation Process of Mining](https://www.diva-portal.org/smash/get/diva2:1386720/FULLTEXT01.pdf)

[⬅️ Back to Index](../README.md)
