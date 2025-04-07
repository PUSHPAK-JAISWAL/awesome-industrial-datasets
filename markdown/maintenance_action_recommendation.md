# Maintenance Action Recommendation

**Summary:** The PHM Data Challenge is focused on maintenance action recommendation, a common problem in industrial remote monitoring and diagnostics. Participants are scored on their ability to accurately recommend confirmed problem types and not make any recommendations for historical nuisance cases.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Recommendation |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 2013-08-15 |
| **Feature Type** | Real, Categorical |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Maintenance Action Recommendation |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | PHM Society |
| **Time Series** | No |

## Description

The PHM Data Challenge is a competition open to all potential conference attendees. This year the challenge is focused on maintenance action recommendation, a common problem in industrial remote monitoring and diagnostics. Participants will be scored on their ability to accurately recommend confirmed problem types and not make any recommendations for historical nuisance cases.

There are 4 data sets provided for the challenge. The Train – Case to Problem.csv file contains the different problems associated with each case, where a case can be created by an automated system or manually by an engineer. The problem is a number that specifies a particular maintenance action that should be implemented to correct the symptom/problem. The Train – Nuisance Cases.csv file contains a set of cases that were not instructive enough to be acted on, useful for determining what features are not useful for classifying problems.

The Train – Case to Events and Parameters.csv file contains all of the event codes and parameters that are associated with all of the cases in the previous files and should be used to train/develop the recommender. The Test – Case to Events and Parameters.csv file contains all of the event codes and parameters for all of the test cases and should be used to generate the file that will be used to evaluate the recommender.

## Tags

Diagnostics, Event codes, Fault identification, Industrial remote monitoring, Maintenance action recommendation, Parameter data, Prognostics and Health Management

## References

- [PHM Data Challenge](https://www.phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2013/phm-data-challenge/)
- [here](https://www.phmsociety.org/events/conference/phm/13/challenge)
- [International Journal of Prognostics and Health Management(IJPHM)](https://www.phmsociety.org/journal)

[⬅️ Back to Index](../README.md)
