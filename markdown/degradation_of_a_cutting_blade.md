# One Year Industrial Component Degradation

**Summary:** This dataset contains machine data of a degrading cutting blade component recorded over the duration of 12 months, aiming to show component degradation for predictive maintenance.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Predictive Maintenance, Remaining Useful Life Prediction, Time Series Analysis |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | Information not available |
| **Feature Type** | Real |
| **Labeled** | No |
| **Missing Values** | Information not available |
| **Name** | One Year Industrial Component Degradation |
| **Number of Features** | 9 per file (total 4671 columns across files) |
| **Number of Instances** | 519 files (samples) |
| **Source** | Kaggle |
| **Time Series** | Yes |

## Description

This dataset contains the machine data of a degrading component recorded over a total duration of 12 months. It was initiated in the European research and innovation project IMPROVE. The dataset consists of 519 files each representing an ~8 second sample recorded at 4 ms resolution resulting in 2048 time-samples per file.

The data is collected from the Vega shrink-wrapper machine deployed in large production lines in the food and beverage industry by OCME. This machine groups loose bottles or cans into set package sizes, wraps them in plastic film, and heat-shrinks the film to form a package. The cutting blade assembly is crucial for machine availability and cannot be visually inspected during operation due to its enclosure and fast rotation speed. Monitoring blade degradation with this data can help improve machine reliability and reduce unexpected downtime.

The dataset includes 8 different operational modes and several machine speeds, which may be inferred using time series analysis. The data is intended for anomaly localization and predictive maintenance to estimate the remaining useful life of the component. Data files are named in a format encoding recording date, sample number, and mode. The dataset is public under a Creative Commons BY-SA 3.0 license.

## Tags

Cutting blade, Industrial component degradation, Manufacturing, Multivariate time series, Predictive maintenance, Remaining useful life prediction, Sensor data

## References

- [IMPROVE Project](http://www.improve-vfof.eu/)
- [OCME Vega shrink-wrapper](http://www.ocme.com/en/our-solutions/secondary-packaging/vega)
- [Dataset on Kaggle](https://www.kaggle.com/inIT-OWL/one-year-industrial-component-degradation)
- [von Birgelen, Alexander et al.: Self-Organizing Maps for Anomaly Localization and Predictive Maintenance in Cyber-Physical Production Systems. 51st CIRP Conference on Manufacturing Systems (CIRP CMS 2018)](https://authors.elsevier.com/sd/article/S221282711830307X)
- [Creative Commons BY-SA 3.0 License](https://creativecommons.org/licenses/by-sa/3.0/)

[⬅️ Back to Index](../README.md)
