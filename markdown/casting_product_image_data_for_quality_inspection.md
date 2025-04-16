# Casting product image data for quality inspection

**Summary:** This dataset contains grayscale images of submersible pump impellers for automatic quality inspection to detect casting defects.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Binary Classification |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Multiclass, Classification |
| **Date Donated** | Information not available |
| **Feature Type** | Image (Grayscale) |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Casting product image data for quality inspection |
| **Number of Features** | Information not available |
| **Number of Instances** | 7348 |
| **Source** | Kaggle |
| **Time Series** | No |

## Description

This dataset is of casting manufacturing product. Casting is a manufacturing process in which a liquid material is usually poured into a mould, which contains a hollow cavity of the desired shape, and then allowed to solidify.

The reason for collecting this data is casting defects, which are undesired irregularities in a metal casting process. There are many types of defects in casting like blow holes, pinholes, burr, shrinkage defects, mould material defects, pouring metal defects, metallurgical defects, etc. Defects are unwanted in the casting industry. The inspection process is usually done manually, which is time-consuming and not 100% accurate, potentially causing large losses for companies.

The dataset contains a total of 7348 grey-scaled images of size 300x300 pixels, with augmentation already applied. There is also a set of 512x512 grayscale images without augmentation with 519 ok_front and 781 def_front images. The images are top view photos of submersible pump impellers captured with a stable lighting arrangement. The data is split into training and testing folders containing defective (def_front) and ok (ok_front) images for classification model development.

## Tags

Binary classification, Casting manufacturing, Deep learning dataset, Grayscale images, Image classification, Industrial defect detection, Quality inspection

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product)
- [YouTube Prototype Demonstration](https://www.youtube.com/watch?v=4sDfwS48p0A)

[⬅️ Back to Index](../README.md)
