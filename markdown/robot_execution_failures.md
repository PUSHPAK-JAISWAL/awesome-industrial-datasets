# Robot Execution Failures

**Summary:** This dataset contains force and torque measurements on a robot after failure detection. Each failure is characterized by 15 force/torque samples collected at regular time intervals.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 1999-04-22 |
| **Feature Type** | Integer |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Robot Execution Failures |
| **Number of Features** | 90 |
| **Number of Instances** | 463 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | Yes |

## Description

The Robot Execution Failures dataset includes 5 datasets, each defining a different learning problem related to failures in robot operations: failures in approach to grasp position, failures in transfer of a part, position of part after a transfer failure, failures in approach to ungrasp position, and failures in motion with part.

Each failure instance is characterized by 15 force/torque samples collected at regular time intervals starting immediately after failure detection, spanning a total observation window of 315 milliseconds. The features are integer-valued and represent the evolution of forces and torques (Fx, Fy, Fz, Tx, Ty, Tz) over these time intervals.

To improve classification accuracy on these problems, various feature transformation strategies such as statistical summary features and discrete Fourier transform were evaluated, leading to an average improvement of 20% in accuracy according to the reference by Seabra Lopes and Camarinha-Matos (1998).

## Tags

Classification tasks, Force and torque measurements, Integer features, Multivariate time-series, Physical sensor data, Robot failure detection, Short time window data

## References

- [Lopes, L. & Camarinha-Matos, L. (1998). Robot Execution Failures [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5M89N.](https://doi.org/10.24432/C5M89N)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Robot+Execution+Failures)

[⬅️ Back to Index](../README.md)
