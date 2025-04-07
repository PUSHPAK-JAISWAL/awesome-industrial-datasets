# Degradation Measurement of Robot Arm Position Accuracy

**Summary:** Data collected on a UR robot to measure the degradation of robot arm position accuracy for robot system health assessment. The data sets provide both the robot high level TCP positional health data and the controller level components’ detail information.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Prognostics |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2017-10-05 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Degradation Measurement of Robot Arm Position Accuracy |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | NIST |
| **Time Series** | Yes |

## Description

A grid moment of the universal robot (UR5*) is planned. The tool center positions (TCP) (x,y,z) of the robot are measured by a 7-D measurement system developed at NIST. Differences are compared from the nominal positions to the measured positions. Controller level sensing data are also collected from each joint, to understand the influences of position degradation from temperature, payload, and speed.

Controller level information provides clues about the root causes of the robot performance degradation, by providing information about the actual and joint positions, velocities, currents, accelerations, torques, and temperatures.

The data sets can help to build the matrix of robot health monitoring algorithms and tools, support the research of robot prognostic, and health management (PHM), and support the validation and verification of the industrial PHM implementation.

## Tags

Controller data, Health assessment, Payload effects, Position accuracy, Prognostics and health management (PHM), Robot arm, Temperature effects

## References

- [NIST](https://www.nist.gov/el/intelligent-systems-division-73500/degradation-measurement-robot-arm-position-accuracy)
- [Degradation Analysis for Industrial Robot Systems](https://www.nist.gov/publications/accuracy-degradation-analysis-industrial-robot-systems)
- [Quick Positional Health Assessment for Industrial Robot Prognostics and Health Management](https://www.nist.gov/publications/quick-positional-health-assessment-industrial-robot-prognostics-and-health-management)

[⬅️ Back to Index](../README.md)
