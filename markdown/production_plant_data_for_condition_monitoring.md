# Production Plant Data for Condition Monitoring

**Summary:** The dataset focuses on the prediction of the condition of an important component within production lines, based on data from 8 run-to-failure experiments and 8 features related to the component.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Predictive Maintenance |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2018-09-19 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Production Plant Data for Condition Monitoring |
| **Number of Features** | 260 |
| **Number of Instances** | Information not available |
| **Source** | Kaggle |
| **Time Series** | Likely |

## Description

This dataset was used in previous research projects, including the IMPROVE project funded by the European Union's Horizon 2020 program.

The use case addresses the prediction of the condition of a critical component in production lines, which affects both plant functioning and product quality. The dataset contains data from 8 run-to-failure experiments and features related to the component. Training and prediction were performed using a leave-one-out method whereby data from the component under test served as the prediction target, and data from other components served as training data to represent the 'new' condition. A Self-Organizing Map (SOM) was trained on the training data to model the 'new' condition and to visualize degradation.

The prediction was successful in identifying wear types labeled by experts, and correctly identified a component without wear signs as confirmed by expert assessment. The dataset is publicly available under the Creative Commons BY-SA 3.0 license.

## Tags

Condition monitoring, Degradation prediction, Industrial process data, Predictive maintenance, Production plant, Run-to-failure, Self-Organizing Map

## References

- [IMPROVE Project](http://improve-vfof.eu/)
- [Self-Organizing Maps for Anomaly Localization and Predictive Maintenance in Cyber-Physical Production Systems. 51st CIRP Conference on Manufacturing Systems (CIRP CMS 2018)](https://authors.elsevier.com/sd/article/S221282711830307X)
- [Creative Commons BY-SA 3.0 License](https://creativecommons.org/licenses/by-sa/3.0/)
- [Kaggle Dataset Page](https://www.kaggle.com/inIT-OWL/production-plant-data-for-condition-monitoring)

[⬅️ Back to Index](../README.md)
