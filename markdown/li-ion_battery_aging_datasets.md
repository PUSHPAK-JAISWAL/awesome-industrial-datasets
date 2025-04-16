# Li-ion Battery Aging Datasets

**Summary:** This data set has been collected from a custom built battery prognostics testbed and includes Li-ion batteries run through different operational profiles at various temperatures and current loads until end-of-life.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Prognostics, Remaining Useful Life prediction, Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Time-Series, Multivariate, Run-to-Failure |
| **Date Donated** | 2010-09-13 |
| **Feature Type** | Real |
| **Labeled** | Likely |
| **Missing Values** | Information not available |
| **Name** | Li-ion Battery Aging Datasets |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | NASA Prognostics Center of Excellence (PCoE) |
| **Time Series** | Yes |

## Description

The Li-ion Battery Aging Datasets were collected at the NASA Ames Prognostics Center of Excellence using a custom-built battery prognostics testbed. The batteries were subjected to charge, discharge, and Electrochemical Impedance Spectroscopy operations at different temperatures and varying current load levels. Discharge tests continued until the battery voltage dropped to preset thresholds, including some lower than recommended by the OEM to induce deep discharge aging effects. The experiments continued until the batteries reached end-of-life criteria of a 30% fade in rated capacity (from 2 Ah to 1.4 Ah).

The testbed setup included commercially available Li-ion 18650 rechargeable batteries, programmable electronic loads and power supplies, sensor suites (voltmeter, ammeter, thermocouples), custom EIS equipment, environmental chambers, and PXI chassis-based data acquisition and experiment control systems with MATLAB-based controls. The data acquisition rate is approximately 10Hz.

The dataset structure includes cycle-based data with charge, discharge, and impedance operation types. Parameters recorded encompass battery terminal voltage, current, temperature, charger/load currents and voltages, capacity, and various impedance measurements with estimated electrolyte resistance and charge transfer resistance. These Run-to-Failure time series datasets serve for developing prognostic algorithms aimed at predicting Remaining Useful Life (RUL) under varying operational conditions and inherent variability among cells.

## Tags

Battery aging, Electrochemical Impedance Spectroscopy, Li-ion batteries, NASA PCoE, Prognostics testbed, Remaining Useful Life prediction, Run-to-Failure data

## References

- [NASA Prognostics Center of Excellence Dataset](http://ti.arc.nasa.gov/c/5/)
- [Supporting Documentation](http://ti.arc.nasa.gov/c/9/)

[⬅️ Back to Index](../README.md)
