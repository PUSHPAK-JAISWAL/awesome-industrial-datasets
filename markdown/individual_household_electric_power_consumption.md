# Individual Household Electric Power Consumption

**Summary:** Measurements of electric power consumption in one household with a one-minute sampling rate over a period of almost 4 years. Different electrical quantities and some sub-metering values are available.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Clustering |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2012-08-29 |
| **Feature Type** | Real |
| **Labeled** | Likely Yes |
| **Missing Values** | Yes |
| **Name** | Individual Household Electric Power Consumption |
| **Number of Features** | 9 |
| **Number of Instances** | 2075259 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Yes |

## Description

This archive contains 2,075,259 measurements gathered in a house located in Sceaux (7 km of Paris, France) between December 2006 and November 2010 (47 months).

Note that (global_active_power*1000/60 - sub_metering_1 - sub_metering_2 - sub_metering_3) represents the active energy consumed every minute (in watt hour) in the household by electrical equipment not measured in sub-meterings 1, 2 and 3. The dataset contains some missing values in the measurements (nearly 1.25% of the rows). All calendar timestamps are present in the dataset but for some timestamps, the measurement values are missing: a missing value is represented by the absence of value between two consecutive semicolon attribute separators. For instance, the dataset shows missing values on April 28, 2007.

The variables include date, time, global active and reactive power, voltage, global intensity, and three energy sub-meterings corresponding to different household areas and devices, all recorded in specific units such as kilowatt, volt, ampere, and watt-hour.

## Tags

Electric power consumption, Household energy data, Minute sampling rate, Missing values present, Multivariate data, Sub-metering, Time series

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption)
- [Dataset DOI](https://doi.org/10.24432/C58K54)

[⬅️ Back to Index](../README.md)
