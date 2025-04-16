# UK-DALE dataset

**Summary:** This dataset records the power demand from five houses, including whole-house mains power demand and power demand from individual appliances, with data collected at resolutions of one and six seconds, and high frequency data at 16 kHz for some houses.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2017-04 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | UK-DALE dataset |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | UK Energy Research Council's Energy Data Centre (UKERC EDC) |
| **Time Series** | Yes |

## Description

The UK Domestic Appliance-Level Electricity (UK-DALE) dataset contains detailed electricity usage data from five UK houses. It includes whole-house power demand recorded every six seconds, as well as appliance-level power demand also recorded every six seconds. For three houses (1, 2 and 5), the dataset features high-frequency recordings of whole-house voltage and current sampled at 16 kHz stored as FLAC files. These high frequency FLAC files are around 200 MB each and the entire 16 kHz dataset for April 2017 occupies 7.6 TB.

The dataset has been released multiple times, with the final and most recent release dated April 2017, providing up to 4.3 years of data for house 1. The data is available in several formats including CSV files for 1-second and 6-second resolution data and an HDF5 format compatible with the NILMTK toolkit. Additional utility meter readings and metadata about houses are also provided.

The dataset is made freely available under the Creative Commons Attribution 4.0 International license (CC BY 4.0). It has been described in the publication "The UK-DALE dataset, domestic appliance-level electricity demand and whole-house demand from five UK homes" published in Scientific Data in 2015. Users are encouraged to cite this paper and the dataset DOIs when using UK-DALE data.

## Tags

Appliance-level data, Domestic electricity usage, Energy consumption, High-frequency power data, Multivariate, Time-series data, United Kingdom

## References

- [UK-DALE Dataset Paper](http://dx.doi.org/10.1038/sdata.2015.7)
- [UKERC Energy Data Centre - Dataset DOI 1 second & 6 second data](http://dx.doi.org/10.5286/UKERC.EDC.000001)
- [UKERC Energy Data Centre - Dataset DOI 16 kHz data](http://dx.doi.org/10.5286/UKERC.EDC.000003)
- [UK-DALE Dataset Download and Info Page](http://jack-kelly.com/data/)
- [snd_card_power_meter GitHub Repository](https://github.com/JackKelly/snd_card_power_meter)

[⬅️ Back to Index](../README.md)
