# Genesis Pick-and-Place Demonstrator Dataset

**Summary:** The dataset consists of sensor and state data from a portable Genesis pick-and-place demonstrator, including normal behavior and labeled anomalies related to a linear drive.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Anomaly Detection, Classification, Predictive Maintenance |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2018-07-23 |
| **Feature Type** | Real, Integer |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Genesis Pick-and-Place Demonstrator Dataset |
| **Number of Features** | 12 (5 continuous, 13 discrete signals, 1 Unix Timestamp) - 112 columns total |
| **Number of Instances** | 16220 |
| **Source** | Kaggle |
| **Time Series** | Yes |

## Description

The Genesis Demonstrator was created during the OPAK Project and further revised during the IMPROVE project. It is a portable pick-and-place machine that uses an air tank to supply gripping and storage units. The dataset records 5 continuous signals, 13 discrete signals, and 1 Unix Timestamp, with some datasets containing labels. The demonstrator sorts two different materials (wood and metal) into their corresponding target locations using four modules: Storage Magazine, Sensor, Metal storage, and Wood storage. A pneumatic linear drive transports the materials through a defined sequence of operations controlled by a PLC.

The first labeled dataset contains 16220 observations taken every 50ms via an OPC DA server, with labels indicating the internal PLC state machine or anomalies. The anomaly labels are manually annotated and include three types: no anomaly, jammed/tilted linear drive, and a linear drive breaking free to correct lag error. Missing values and zero-variance columns have been removed. A second unlabeled dataset contains normal runs and runs with errors for predictive maintenance or anomaly detection, with impairments such as linear drive degradation or reduced air pressure. The datasets may not be fully compatible with each other.

## Tags

Anomaly detection, Industrial automation, Labeled anomalies, Pick-and-place, Pneumatic linear drive, Predictive maintenance, Time-series sensor data

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/inIT-OWL/genesis-demonstrator-data-for-machine-learning)
- [von Birgelen, Alexander; Niggemann, Oliver: Anomaly Detection and Localization for Cyber-Physical Production Systems with Self-Organizing Maps. Springer Vieweg, Aug 2018.](https://www.hs-owl.de/init/veroeffentlichungen/publikationen/a/filteroff/3373/single.html)
- [OPAK Project](https://www.hs-owl.de/init/en/forschung/projekte/b/filteroff/267/single.html)
- [IMPROVE Project](http://www.improve-vfof.eu/)

[⬅️ Back to Index](../README.md)
