# UK-DALE dataset

**Summary:** This dataset records the power demand from five houses, including whole-house mains power and individual appliance power every six seconds. In three of the houses, whole-house voltage and current are recorded at 16 kHz.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, NILM |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2017-04-01 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | UK-DALE dataset |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | Jack Kelly's website |
| **Time Series** | Yes |

## Description

The UK-DALE dataset records the power demand from five houses. In each house, both the whole-house mains power demand and the power demand from individual appliances are recorded every six seconds. In three of the five houses (houses 1, 2, and 5), the whole-house voltage and current are also recorded at 16 kHz.

The dataset is available in several formats, including ZIPPED CSV files, an HDF5 version for use with NILMTK, and FLAC files for the 16 kHz voltage and current data. The most recent release is for April 2017 and includes 4.3 years of data for house 1.

Gas and electricity utility meter readings for house 1 are also available. The 16 kHz data is stored as a sequence of stereo FLAC files, with one channel representing whole-house voltage and the other representing whole-house current.

## Tags

Appliance-level energy data, Energy disaggregation, NILM, Power demand, Residential energy consumption, Smart meters, Voltage and current data

## References

- [Jack Kelly's website](http://jack-kelly.com/data/)
- [UKERC EDC](http://data.ukedc.rl.ac.uk/simplebrowse/edc/efficiency/residential/EnergyConsumption/Domestic/UK-DALE-2017/UK-DALE-FULL-disaggregated/ukdale.zip)
- [Scientific Data Paper](http://www.nature.com/sdata)

[⬅️ Back to Index](../README.md)
