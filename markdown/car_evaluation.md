# Car Evaluation

**Summary:** Derived from a simple hierarchical decision model, this database may be useful for testing constructive induction and structure discovery methods. The model evaluates cars according to price, technical characteristics, comfort and safety.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification |
| **Data Source** | Abstract |
| **Dataset Characteristics** | Multivariate |
| **Date Donated** | 1997-05-31 |
| **Feature Type** | Categorical |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Car Evaluation |
| **Number of Features** | 6 |
| **Number of Instances** | 1728 |
| **Source** | UCI Machine Learning Repository |
| **Time Series** | No |

## Description

Car Evaluation Database was derived from a simple hierarchical decision model originally developed for the demonstration of DEX, M. Bohanec, V. Rajkovic: Expert system for decision making. Sistemica 1(1), pp. 145-157, 1990.). The model evaluates cars according to the following concept structure:

CAR                      car acceptability
. PRICE                  overall price
. . buying               buying price
. . maint                price of the maintenance
. TECH                   technical characteristics
. . COMFORT              comfort
. . . doors              number of doors
. . . persons            capacity in terms of persons to carry
. . . lug_boot           the size of luggage boot
. . safety               estimated safety of the car

Input attributes are printed in lowercase. Besides the target concept (CAR), the model includes three intermediate concepts: PRICE, TECH, COMFORT. Every concept is in the original model related to its lower level descendants by a set of examples (for these examples sets see http://www-ai.ijs.si/BlazZupan/car.html).

The Car Evaluation Database contains examples with the structural information removed, i.e., directly relates CAR to the six input attributes: buying, maint, doors, persons, lug_boot, safety.

Because of known underlying concept structure, this database may be particularly useful for testing constructive induction and structure discovery methods.

## Tags

Automobile evaluation, Car acceptability, Categorical data, Constructive induction, Expert system, Hierarchical decision model, Structure discovery

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)
- [Knowledge acquisition and explanation for multi-attribute decision making](https://www.semanticscholar.org/paper/KNOWLEDGE-ACQUISITION-AND-EXPLANATION-FOR-DECISION-Bohanec-Rajkovi%C4%8D/8bab443ae322ff47c3e609272bd93fd4650555bc)

[⬅️ Back to Index](../README.md)
