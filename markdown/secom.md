# SECOM

**Summary:** Data from a semi-conductor manufacturing process. The dataset represents a selection of features where each example represents a single production entity with associated measured features and the labels represent a simple pass/fail yield for in house line testing, and associated date time stamp.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Causal-Discovery |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2008-11-18 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Yes |
| **Name** | SECOM |
| **Number of Features** | 591 |
| **Number of Instances** | 1567 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | No |

## Description

A complex modern semi-conductor manufacturing process is normally under consistent surveillance via the monitoring of signals/variables collected from sensors and or process measurement points. However, not all of these signals are equally valuable in a specific monitoring system. The measured signals contain a combination of useful information, irrelevant information as well as noise. It is often the case that useful information is buried in the latter two. Engineers typically have a much larger number of signals than are actually required.

Using feature selection techniques it is desired to rank features according to their impact on the overall yield for the product; causal relationships may also be considered with a view to identifying the key features.

Key facts: Data Structure: The data consists of 2 files the dataset file SECOM consisting of 1567 examples each with 591 features a 1567 x 591 matrix and a labels file containing the classifications and date time stamp for each example. As with any real life data situations this data contains null values varying in intensity depending on the individuals features. This needs to be taken into consideration when investigating the data either through pre-processing or within the technique applied.

## Tags

Classification, Feature selection, Manufacturing process data, Process monitoring, Semiconductor manufacturing, Sensor data, Yield prediction

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/SECOM)

[⬅️ Back to Index](../README.md)
