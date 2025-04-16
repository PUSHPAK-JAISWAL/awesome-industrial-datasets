# Maintenance Action Recommendation

**Summary:** The data challenge focused on maintenance action recommendation from industrial remote monitoring and diagnostics data. Participants were tasked to recommend maintenance actions accurately based on cases and event data.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Recommendation |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series, Classification |
| **Date Donated** | 2013-08-14 |
| **Feature Type** | Integer, Real |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Maintenance Action Recommendation |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | PHM Society |
| **Time Series** | Likely |

## Description

The PHM Data Challenge was part of the 2013 Annual Conference of the Prognostics and Health Management Society. The challenge is centered on the problem of maintenance action recommendation, a common issue in industrial remote monitoring and diagnostics. Participants needed to recommend confirmed problem types while avoiding recommendations on historical nuisance cases.

There are four data sets: 'Train – Case to Problem.csv' which links cases to maintenance actions, 'Train – Nuisance Cases.csv' which contains cases not instructive enough to require action, 'Train – Case to Events and Parameters.csv' which includes event codes and parameters for training, and 'Test – Case to Events and Parameters.csv' which holds test cases for evaluation. The data originates from an industrial piece of equipment where event codes are generated based on onboard conditions along with parameters snapshots.

Participants submitted CSV files with their recommendations that were scored based on the correctness and avoidance of nuisance outputs. The competition winners were invited to submit papers and present their results at the PHM conference and in the International Journal of Prognostics and Health Management (IJPHM).

## Tags

Diagnostics, Event codes, Industrial equipment, Maintenance recommendation, PHM Society data challenge, Parameter data, Remote monitoring

## References

- [PHM Society Data Challenge 2013](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2013/phm-data-challenge/)
- [International Journal of Prognostics and Health Management](https://www.phmsociety.org/journal)

[⬅️ Back to Index](../README.md)
