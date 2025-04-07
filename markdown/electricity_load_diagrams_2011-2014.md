# Electricity Load Diagrams 2011-2014

**Summary:** This data set contains electricity consumption of 370 points/clients. Values are in kW of each 15 min.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Clustering |
| **Data Source** | Real |
| **Dataset Characteristics** | Time-Series |
| **Date Donated** | 2015-03-12 |
| **Feature Type** | Real |
| **Labeled** | No |
| **Missing Values** | No |
| **Name** | Electricity Load Diagrams 2011-2014 |
| **Number of Features** | 140256 |
| **Number of Instances** | 370 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Yes |

## Description

This data set contains electricity consumption of 370 points/clients.

Data set has no missing values. Values are in kW of each 15 min. To convert values in kWh values must be divided by 4. Each column represents one client. Some clients were created after 2011. In these cases consumption were considered zero.

All time labels report to Portuguese hour. However all days present 96 measures (24*4). Every year in March time change day (which has only 23 hours) the values between 1:00 am and 2:00 am are zero for all points. Every year in October time change day (which has 25 hours) the values between 1:00 am and 2:00 am aggregate the consumption of two hours.

## Tags

Electricity consumption, Energy data, Load diagrams, Portuguese hour, Real-world data, Time series analysis, kW values

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014)

[⬅️ Back to Index](../README.md)
