# Maintenance of Naval Propulsion Plants Data Set

**Summary:** The dataset contains measurements from a numerical simulator of a naval vessel's Gas Turbine propulsion plant and is used for predicting the propulsion plant's decay state coefficient.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2014-09-11 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | N/A |
| **Name** | Maintenance of Naval Propulsion Plants Data Set |
| **Number of Features** | 16 |
| **Number of Instances** | 11934 |
| **Source** | Kaggle, originally from UCI Machine Learning Repository |
| **Time Series** | Likely |

## Description

The experiments have been conducted using a numerical simulator of a naval vessel (Frigate) characterized by a Gas Turbine (GT) propulsion plant. The simulator consists of several blocks including Propeller, Hull, GT, Gear Box, and Controller, developed and fine-tuned based on similar real propulsion plants, making the data closely representative of actual vessels.

This release of the simulator enables modeling performance decay over time of GT components such as the GT compressor and turbines. The propulsion system's behavior is characterized by parameters including ship speed and degradation coefficients for the compressor and turbine. The dataset contains a 16-feature vector representing GT measures at steady state of the physical asset, along with the GT compressor and turbine decay state coefficients.

The range of decay for compressor and turbine states is finely sampled, and the ship speed is sampled over a range from 3 to 27 knots. This granularity allows a good representation of possible degradation states, facilitating tasks like regression to estimate the decay state based on sensor measurements.

## Tags

Gas Turbine, Multivariate data, Naval propulsion, Performance decay, Regression task, Simulator data, Synthetic data

## References

- [UCI Machine Learning Repository - Maintenance of Naval Propulsion Plants Data Set](http://archive.ics.uci.edu/ml/datasets/condition+based+maintenance+of+naval+propulsion+plants)
- [Kaggle Dataset Page](https://www.kaggle.com/datasets/elikplim/maintenance-of-naval-propulsion-plants-data-set)

[⬅️ Back to Index](../README.md)
