# Business and Industry Reports

**Summary:** 7,000 economics time series from 16 US Census Bureau economic reports covering the period 1956-2017.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Likely Regression, Time Series Analysis |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2017-10-17 |
| **Feature Type** | Real |
| **Labeled** | Likely |
| **Missing Values** | Information not available |
| **Name** | Business and Industry Reports |
| **Number of Features** | 18 columns |
| **Number of Instances** | 10952 unique time series codes approximately |
| **Source** | Kaggle |
| **Time Series** | Yes |

## Description

Along with their core mission of counting the US population, the United States Census Bureau gathers a wide range of economic data. This dataset comprises 16 different economic reports and surveys from the Census Bureau, covering numerous economic indicators.

The data is provided in a long format CSV, with a time_series_code column linking the data to a metadata CSV. The time series data includes error codes for some series, reflecting confidence intervals and other measures. Dates are stored as complete beginning of period dates, with series at monthly, quarterly, or annual resolutions. Multiple series exist under given categories, often split by states or tax types.

Values with non-numeric entries, such as 'Less than .05 percent', should be filtered out for numerical analysis. The dataset has been reformatted from original Census Bureau presentations to enhance usability, and the data preparation script is also provided.

## Tags

Business and industry, Economic indicators, Economic reports, Monthly and quarterly data, Multivariate data, Time series data, US Census Bureau

## References

- [Kaggle Dataset Page](https://www.kaggle.com/datasets/census/business-and-industry-reports)
- [United States Census Bureau Original Data](https://www.census.gov/econ/currentdata/datasets/index)
- [Data Preparation Script on GitHub](https://gist.github.com/SohierDane/2c1b36f653724fbc7d8f26501ef4b88d)

[⬅️ Back to Index](../README.md)
