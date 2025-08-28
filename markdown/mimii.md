# MIMII Dataset: Sound Dataset for Malfunctioning Industrial Machine Investigation and Inspection

**Summary:** The MIMII dataset contains normal and anomalous sound recordings from four types of industrial machines to support research in sound-based machine fault diagnosis. It includes varied anomalous scenarios and mixes background noise, recorded with an eight-channel microphone array at 16 kHz sampling rate.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Anomaly Detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2019-09-20 |
| **Feature Type** | Real, Integer |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | MIMII Dataset: Sound Dataset for Malfunctioning Industrial Machine Investigation and Inspection |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | Zenodo |
| **Time Series** | Yes |

## Description

This dataset is a sound dataset for malfunctioning industrial machine investigation and inspection. It contains the sounds generated from four types of industrial machines, i.e. valves, pumps, fans, and slide rails. Each type of machine includes individual product models, and the data for each model contains normal sounds (from 5000 seconds to 10000 seconds) and anomalous sounds (about 1000 seconds). Various anomalies such as contamination, leakage, rotating unbalance, and rail damage were recorded, and background noise from multiple real factories was mixed with the machine sounds. The sounds were recorded by an eight-channel microphone array with 16 kHz sampling rate and 16 bit per sample, and the dataset assists benchmarking for sound-based machine fault diagnosis with functions like unsupervised anomaly detection and noise robustness.

This dataset is made available by Hitachi, Ltd. under a Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.

A baseline sample code for anomaly detection is available on GitHub: https://github.com/MIMII-hitachi/mimii_baseline/. This version "public 1.0" contains four models (model ID 00, 02, 04, and 06); the remaining models will be released in future editions.

## Tags

acoustic condition monitoring, anomaly detection, audio data, industrial machine, machine fault diagnosis, microphone array, unsupervised learning

## References

- [GitHub Repository](https://github.com/MIMII-hitachi/mimii_baseline/)
- [Zenodo Record](https://zenodo.org/record/3384388)

[⬅️ Back to Index](../README.md)
