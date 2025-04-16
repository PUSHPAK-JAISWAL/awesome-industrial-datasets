# Laser Welding

**Summary:** Dataset from screening experiments evaluating the influence of six factors on weld depth and geometrical dimensions in laser welded steel-copper lap joints with additional data on cracking.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression, Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2021-02-01 |
| **Feature Type** | Real, Categorical |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Laser Welding |
| **Number of Features** | 7 |
| **Number of Instances** | 360 |
| **Source** | Mendeley Data |
| **Time Series** | No |

## Description

The dataset shows a definitive screening design to evaluate the influence of six factors: laser beam power (W), welding speed (m/min), angular position in welding direction (°), focal position (mm), gas flow rate (l/min), and material thickness of the steel sheet (mm). These factors are tested in three levels and 18 parameter combinations on the weld depth and the geometrical dimensions of the weld metal in laser welded steel-copper joints in the lap configuration with steel on the top side. Each parameter combination was repeated 5 times and every sheet was cut 4 times, generating 360 cross sections. Each line in the dataset represents a cross section evaluated regarding dimensions of the weld metal, including a dichotomous column for welding metal cracking (yes/no).

The dataset is not suitable for modeling a precise predictive model of weld depth in the copper sheet but shows correlation between cracking and weld depth, which can be described well in a binominal logistic regression. Furthermore, average crack length and count of cracks were added in version 1.1.

Version 2 of the dataset presents the same screening experiments with adjusted laser power levels to guarantee sufficient weld depth for all parameter combinations, targeting the average weld depth in the bottom copper sheet. The data can be used to calculate the parameter effect strength of the factors on weld depth and to build a simple linear model of the relationships. Version 2.1 includes the resulting copper dilution instead of weld depth.

## Tags

Cracking detection, Laser beam welding, Material thickness, Screening design, Steel-copper lap joints, Weld depth analysis, Welding parameters

## References

- [Mendeley Data - Screening datasets for laser welded steel-copper lap joints](http://dx.doi.org/10.17632/2s5m3crbkd.2)

[⬅️ Back to Index](../README.md)
