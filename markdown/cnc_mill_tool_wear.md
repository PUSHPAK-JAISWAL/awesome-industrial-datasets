# CNC Mill Tool Wear

**Summary:** A series of machining experiments run on wax blocks in a CNC milling machine, collecting data to study variations in tool condition, feed rate, and clamping pressure.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2018-04 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | CNC Mill Tool Wear |
| **Number of Features** | 871 |
| **Number of Instances** | Information not available |
| **Source** | Kaggle |
| **Time Series** | Yes |

## Description

A series of machining experiments were run on 2" x 2" x 1.5" wax blocks in a CNC milling machine in the System-level Manufacturing and Automation Research Testbed (SMART) at the University of Michigan. Machining data was collected from a CNC machine for variations of tool condition, feed rate, and clamping pressure. Each experiment produced a finished wax part with an "S" shape carved into the top face.

General data from each of the 18 different experiments are contained in train.csv and include the experiment number, material (wax), feed rate, and clamp pressure. Outputs per experiment include tool condition (unworn and worn tools) and whether or not the tool passed visual inspection. Time series data was collected from the 18 experiments at a sampling rate of 100 ms and reported separately in files experiment_01.csv to experiment_18.csv with measurements from the 4 motors in the CNC machine.

The dataset can be used for classification studies such as tool wear detection—binary classification for worn and unworn cutting tools—and detection of inadequate clamping pressure that affects the machining outcome. The data includes various sensor measurements related to position, velocity, acceleration, current, voltage, power from the CNC machine motors and spindle.

## Tags

CNC machining, Classification, Industrial process monitoring, Manufacturing, Sensor data, Time series data, Tool wear detection

## References

- [Kaggle Dataset Page](https://www.kaggle.com/shasun/tool-wear-detection-in-cnc-mill)

[⬅️ Back to Index](../README.md)
