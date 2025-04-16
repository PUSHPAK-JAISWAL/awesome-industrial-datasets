# Air Quality

**Summary:** Contains the responses of a gas multisensor device deployed on the field in an Italian city. Hourly responses averages are recorded along with gas concentrations references from a certified analyzer.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2016-03-22 |
| **Feature Type** | Real |
| **Labeled** | Likely |
| **Missing Values** | Yes |
| **Name** | Air Quality |
| **Number of Features** | 15 |
| **Number of Instances** | 9358 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Yes |

## Description

The dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level, within an Italian city. Data were recorded from March 2004 to February 2005 (one year) representing the longest freely available recordings of on field deployed air quality chemical sensor devices responses. Ground Truth hourly averaged concentrations for CO, Non Metanic Hydrocarbons, Benzene, Total Nitrogen Oxides (NOx) and Nitrogen Dioxide (NO2) were provided by a co-located reference certified analyzer.

Evidences of cross-sensitivities as well as both concept and sensor drifts are present as described in De Vito et al., Sens. And Act. B, Vol. 129,2,2008 (citation required) eventually affecting sensors concentration estimation capabilities. Missing values are tagged with -200 value. This dataset can be used exclusively for research purposes. Commercial purposes are fully excluded.

The data include features such as date, time, true hourly averaged concentrations of various gases, hourly averaged sensor responses, temperature, relative humidity, and absolute humidity.

## Tags

Air Quality Monitoring, Chemical Sensors, Cross-sensitivity and Sensor Drift, Environmental Sensor, Gas Sensor Data, Multivariate Time-Series, Pollution Measurement

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Air+Quality)
- [On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario - Sensors and Actuators B: Chemical, 2008](https://www.semanticscholar.org/paper/a90a54a39ff934772df57771a0012981f355949d)
- [DOI: 10.24432/C59K5F](https://doi.org/10.24432/C59K5F)

[⬅️ Back to Index](../README.md)
