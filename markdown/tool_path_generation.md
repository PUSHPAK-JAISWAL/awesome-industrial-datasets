# Tool Path Generation

**Summary:** Shape deviation measurements and corresponding simulated cutting conditions for self-optimizing tool path generation in 5-axis machining processes. The dataset includes measurements from pocket A and pocket B configurations, with and without compensation.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2018-04-19 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Tool Path Generation |
| **Number of Features** | 7 |
| **Number of Instances** | Information not available |
| **Source** | Mendeley Data |
| **Time Series** | No |

## Description

Shape deviation measurements and corresponding simulated cutting conditions.
Please refer to the corresponding paper for the experimental setup.

Feature Description:
MeasuredDeviation - Actual measured deviation [mm]
WidthOfCut - Width of cut determined with process parallel material simuation [mm]
DepthOfCut - Width of cut determined with process parallel material simuation [mm]
HeightAtTool - Projected distance from probed surface point to tool tip along tool axis determined with process parallel material simuation [mm]
MaterialRemovalRate - Material removal ratedetermined with process parallel material simuation [cm^3/min]
Feedrate - Feedrate determined with process parallel material simuation [m/min]
X,Y,Z - Location of probed point in workpiece coordinates [mm]

The dataset includes measurements from Pocket A and Pocket B, both with and without compensation. The data was collected using systematic and random point selection methods.

## Tags

5-axis machining, Computer-Aided Manufacturing, Cutting conditions, Machining, Manufacturing, Shape deviation, Tool path optimization

## References

- [Mendeley Data](https://data.mendeley.com/datasets/smyg6cfwpk/1)

[⬅️ Back to Index](../README.md)
