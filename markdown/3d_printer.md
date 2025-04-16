# 3D Printer

**Summary:** Dataset to find relations between the input parameters of 3D printers, aiming to determine how adjustment parameters affect print quality, accuracy, and strength.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2018-09-14 |
| **Feature Type** | Real, Categorical |
| **Labeled** | Likely |
| **Missing Values** | Information not available |
| **Name** | 3D Printer |
| **Number of Features** | 12 |
| **Number of Instances** | Information not available |
| **Source** | Kaggle |
| **Time Series** | No |

## Description

This dataset comes from research by TR/Selcuk University Mechanical Engineering department. The aim of the study is to determine how much of the adjustment parameters in 3D printers affect the print quality, accuracy, and strength. There are nine setting parameters and three measured output parameters.

The input setting parameters include Layer Height (mm), Wall Thickness (mm), Infill Density (%), Infill Pattern (), Nozzle Temperature (Cº), Bed Temperature (Cº), Print Speed (mm/s), Material (), and Fan Speed (%).

The output parameters measured are Roughness (µm), Tension (ultimate) Strength (MPa), and Elongation (%). The work is based on the Ultimaker S5 3-D printer settings and filaments. Material and strength tests were carried out on a Sincotec GMBH tester capable of pulling 20 kN. The study attempts to estimate which material is used from the input and output parameters using kNN and DNN algorithms.

## Tags

3D printing, Classification, Material strength, Mechanical engineering, Print quality, Printer settings, Regression

## References

- [3D Printer Dataset on Kaggle](https://www.kaggle.com/datasets/afumetto/3dprinter)
- [Research blog (Turkish)](https://medium.com/@ahmet17/makina-m%C3%BChendisleri-i%C3%A7in-derin-%C3%B6%C4%9Frenme-3d-printer-veri-setinin-i%CC%87ncelenmesi-6fe1f48e0cdb)

[⬅️ Back to Index](../README.md)
