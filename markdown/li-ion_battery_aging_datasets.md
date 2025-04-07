# Li-ion Battery Aging Datasets

**Summary:** This data set has been collected from a custom built battery prognostics testbed at the NASA Ames Prognostics Center of Excellence (PCoE). Li-ion batteries were run through 3 different operational profiles (charge, discharge and Electrochemical Impedance Spectroscopy) at different temperatures.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Prognostics |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2010-09-13 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Li-ion Battery Aging Datasets |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | NASA |
| **Time Series** | Yes |

## Description

This data set has been collected from a custom built battery prognostics testbed at the NASA Ames Prognostics Center of Excellence (PCoE). Li-ion batteries were run through 3 different operational profiles (charge, discharge and Electrochemical Impedance Spectroscopy) at different temperatures. Discharges were carried out at different current load levels until the battery voltage fell to preset voltage thresholds. Some of these thresholds were lower than that recommended by the OEM (2.7 V) in order to induce deep discharge aging effects. Repeated charge and discharge cycles result in accelerated aging of the batteries. The experiments were stopped when the batteries reached the end-of-life (EOL) criteria of 30% fade in rated capacity (from 2 Ah to 1.4 Ah).

The testbed comprises commercially available Li-ion 18650 sized rechargeable batteries, a programmable 4-channel DC electronic load, a programmable 4-channel DC power supply, voltmeter, ammeter and thermocouple sensor suite, custom EIS equipment, environmental chamber to impose various operational conditions, PXI chassis based DAQ and experiment control. MATLAB based experiment control, data acquisition and prognostics algorithm evaluation setup (appx. data acquisition rate is 10Hz).

The data sets can serve for a variety of purposes. Because these are essentially a large number of Run-to-Failure time series, the data can be set for development of prognostic algorithms. In particular, due to the differences in depth-of-discharge (DOD), the duration of rest periods and intrinsic variability, no two cells have the same state-of-life (SOL) at the same cycle index. The aim is to be able to manage this uncertainty, which is representative of actual usage, and make reliable predictions of Remaining Useful Life (RUL) in both the End-of-Discharge (EOD) and End-of-Life (EOL) contexts.

## Tags

Aging data, Charge-discharge cycles, Electrochemical Impedance Spectroscopy, Li-ion batteries, Prognostics, Remaining Useful Life (RUL), Run-to-failure

## References

- [Data set 1](http://ti.arc.nasa.gov/c/5/)
- [http://ti.arc.nasa.gov/c/9/](/dashlink/static/media/http%3A//ti.arc.nasa.gov/c/9/)

[⬅️ Back to Index](../README.md)
