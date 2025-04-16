# Manufacturing Defects

**Summary:** Ten days of data on parts defects, one item tested every fifteen minutes during an eight-hour shift.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Regression |
| **Data Source** | Real |
| **Dataset Characteristics** | Univariate, Time-Series |
| **Date Donated** | Information not available |
| **Feature Type** | Integer |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Manufacturing Defects |
| **Number of Features** | 3 |
| **Number of Instances** | 3200 |
| **Source** | Kaggle |
| **Time Series** | Yes |

## Description

Defect sampling is used in industrial settings to determine the types and amounts of defects in manufactured items. Items at various stages of production are removed from the process and inspected for defects. Sustained testing allows operations managers to discover whether some part of the manufacturing process is failing to meet performance criteria and product standards. To minimize manufacturing defects, early detection and problem resolution are critical.

In the current sampling plan, one component from the production line is randomly selected every 15 minutes. Each component is inspected and tested for major and minor defects. Major defects, which affect component performance, must be addressed immediately. Fortunately, major defects are rare and are generally contained and corrected early in the process. Minor defects, such as nicks and scratches, are those that affect the appearance of a component but not its functionality.

The data set contains ten days of data on minor defects. Each day, one item is tested every fifteen minutes during an eight-hour shift. The variables in the data set are Day (day of the test: 1-10), Sample (time of the day that sample was taken in military time), and Defects (number of minor defects detected on the sampled item).

## Tags

Defect detection, Industrial data, Inspection data, Manufacturing, Minor defects, Quality control, Time series analysis

## References

- [Kaggle Dataset - Manufacturing Defects Industry Dataset](https://www.kaggle.com/datasets/gabrielsantello/manufacturing-defects-industry-dataset)

[⬅️ Back to Index](../README.md)
