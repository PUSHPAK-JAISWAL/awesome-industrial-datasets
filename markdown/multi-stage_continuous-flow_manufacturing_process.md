# Multi-stage continuous-flow manufacturing process

**Summary:** Real process data from a high-speed, continuous manufacturing line to predict output measurements from multiple stages.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2019-03-06 |
| **Feature Type** | Real |
| **Labeled** | Likely |
| **Missing Values** | Information not available |
| **Name** | Multi-stage continuous-flow manufacturing process |
| **Number of Features** | 116 |
| **Number of Instances** | Information not available |
| **Source** | Kaggle |
| **Time Series** | Yes |

## Description

This data was taken from an actual production line near Detroit, Michigan. The goal is to predict certain properties of the line's output from the various input data. The line is a high-speed, continuous manufacturing process with parallel and series stages.

The data comes from one production run spanning several hours. Liveline Technologies has a large quantity of this type of data from multiple production lines in various locations.

The process consists of multiple stages: In the first stage, Machines 1, 2, and 3 operate in parallel, feeding outputs into a combining step. Output from the combiner is measured in 15 locations around the material's outer surface, constituting the primary measurements to predict. Next, the output flows into a second stage where Machines 4 and 5 process the material in series. Measurements are again made in the same 15 locations after Machine 5, known as the secondary measurements to predict.

## Tags

Continuous Flow, Manufacturing Process, Multistage, Process Control, Real Production Data, Regression Task, Time-Series Data

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/supergus/multistage-continuousflow-manufacturing-process)
- [Liveline Technologies](https://www.liveline.tech)

[⬅️ Back to Index](../README.md)
