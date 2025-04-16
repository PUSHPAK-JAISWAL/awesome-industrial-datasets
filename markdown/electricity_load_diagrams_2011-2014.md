# Electricity Load Diagrams 2011-2014

**Summary:** This data set contains electricity consumption of 370 points/clients recorded every 15 minutes from 2011 to 2014.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Clustering |
| **Data Source** | Real |
| **Dataset Characteristics** | Time-Series |
| **Date Donated** | 2015-03-12 |
| **Feature Type** | Real |
| **Labeled** | Likely |
| **Missing Values** | No |
| **Name** | Electricity Load Diagrams 2011-2014 |
| **Number of Features** | 140256 |
| **Number of Instances** | 370 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Yes |

## Description

The data set includes electricity consumption data for 370 clients, recorded every 15 minutes with values in kW. To convert these values into kWh, values should be divided by 4. Each column represents one client. Some clients were created after 2011; for those clients, consumption values before creation are considered zero. All time labels correspond to Portuguese local time, with adjustments for daylight saving time where applicable.

The data set was saved as a text file in CSV format using a semicolon (;) as the delimiter. The first column presents date and time as a string in the format 'yyyy-mm-dd hh:mm:ss'. All other columns contain float values indicating consumption in kW. The dataset contains no missing values.

During the daylight saving time changes, peculiarities are noted: in March, the day with only 23 hours has zero consumption values between 1:00 am and 2:00 am for all points; in October, the day with 25 hours aggregates consumption of two hours between 1:00 am and 2:00 am.

## Tags

Client consumption profiles, Daylight saving time adjustments, Electricity consumption, Energy data, Portuguese local time, Smart grid, Time-series data

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014)
- [Dataset DOI](https://doi.org/10.24432/C58C86)

[⬅️ Back to Index](../README.md)
