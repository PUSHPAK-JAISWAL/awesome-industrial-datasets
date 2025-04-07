# Mechanical Analysis

**Summary:** Fault diagnosis problem of electromechanical devices; also PUMPS DATA SET is newer version with domain theory and results.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 1990-05-31 |
| **Feature Type** | Categorical, Integer, Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Mechanical Analysis |
| **Number of Features** | 8 |
| **Number of Instances** | 209 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | No |

## Description

F. Bergadano supplied this database. Each instance contains many components, each of which has 8 attributes. Different instances in this database have different numbers of components.

It was impossible to put one instance on one line. He originally had one instance per file, but this makes it difficult to ftp them (imagine ftp'ing 222 or so files!). I bundled the set of 209 instances into a single data file, prefixing each with the line:

===== Instance number 1: =====

where "n" is a number in [1,221]. However, they are NOT, repeat NOT in sequential order. Twelve (12) of the instances are missing. Bergadano supplied these additional 12 instances (numbers 8,12,32,33,66,69,73,152,167,194,203,208) in a "notused" sub-directory. I bundled these up with the same format in the "notused-instances" file.

A quick scan of their file didn't reveal what the purpose is for these twelve instances.

## Tags

Categorical features, Electromechanical devices, Fault diagnosis, Integer features, Mechanical engineering, Pumps data, Real features

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/64/mechanical+analysis)

[⬅️ Back to Index](../README.md)
