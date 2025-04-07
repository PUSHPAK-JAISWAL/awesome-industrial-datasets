# Kolektor Surface-Defect Dataset (KolektorSDD)

**Summary:** The dataset is constructed from images of defective production items that were provided and annotated by Kolektor Group d.o.o.. The images were captured in a controlled industrial environment in a real-world case.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Object Detection, Segmentation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Defect Detection |
| **Date Donated** | Information not available |
| **Feature Type** | Image |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Kolektor Surface-Defect Dataset (KolektorSDD) |
| **Number of Features** | Information not available |
| **Number of Instances** | 399 |
| **Source** | ViCoS Lab |
| **Time Series** | No |

## Description

The dataset is constructed from images of defective production items that were provided and annotated by Kolektor Group d.o.o.. The images were captured in a controlled industrial environment in a real-world case.

The dataset consists of 399 images, with 52 images containing visible defects and 347 images without any defect. The original images have a width of 500 pixels and a height ranging from 1240 to 1270 pixels. For training and evaluation, the images should be resized to 512 x 1408 pixels.

For each item, the defect is only visible in at least one image, while two items have defects on two images, which means there were 52 images where the defects are visible. The remaining 347 images serve as negative examples with non-defective surfaces.

## Tags

Image classification, Industrial inspection, Manufacturing defects, Object detection, Real-world data, Segmentation, Surface defect detection

## References

- [ViCoS Lab - KolektorSDD](https://www.vicos.si/resources/kolektorsdd/)
- [DOWNLOAD HERE with fine annotations (for JIM2019 paper)](https://go.vicos.si/kolektorsdd)
- [DOWNLOAD HERE with box annotations (for ICPR2021 and COMIND 2021 papers)](https://go.vicos.si/kolektorsddboxes)
- [KolektorSDD-training-splits.zip](https://data.vicos.si/datasets/KSDD/KolektorSDD-training-splits.zip)
- [KolektorSDD-dilate=5-tensorflow.zip](https://data.vicos.si/datasets/KSDD/KolektorSDD-dilate=5-tensorflow.zip)

[⬅️ Back to Index](../README.md)
