# Severstal Steel Defect Detection

**Summary:** In this competition you will be predicting the location and type of defects found in steel manufacturing. Images are named with a unique ImageId. You must segment and classify the defects in the test set.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Segmentation |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Image data |
| **Date Donated** | 2019-10-24 |
| **Feature Type** | Image (jpg), Categorical (csv) |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Severstal Steel Defect Detection |
| **Number of Features** | 6 columns (including ImageId, ClassId, and EncodedPixels) |
| **Number of Instances** | Information not available |
| **Source** | Kaggle |
| **Time Series** | No |

## Description

In this competition, the goal is to predict the location and type of defects found in steel manufacturing. Each image might have no defects, a defect of a single class, or defects of multiple classes. For each image, you must segment defects of each class (ClassId = [1, 2, 3, 4]). The segment for each defect class will be encoded into a single row, even if there are several non-contiguous defect locations on an image.

The dataset consists of folders of training images (train_images/) and test images (test_images/) which participants are to segment and classify. Annotations for training images are provided in train.csv, which includes segments for defects with ClassId values from 1 to 4. Additionally, there is a sample submission file that shows the correct format.

Submissions to this competition must be made through Kernels, which will rerun automatically against the entire Public and Private test sets after submission. Participants need to accept the competition rules to access the data. The dataset includes 18,076 files totaling approximately 1.7 GB in size, with image files and CSV annotations.

## Tags

Defect detection, Image classification, Image segmentation, Kaggle competition, Manufacturing quality control, Multiclass defects, Steel manufacturing

## References

- [Severstal Steel Defect Detection - Kaggle](https://www.kaggle.com/c/severstal-steel-defect-detection/data)
- [Competition Rules](https://www.kaggle.com/c/severstal-steel-defect-detection/rules)
- [Evaluation Details](https://www.kaggle.com/c/severstal-steel-defect-detection/overview/evaluation)
- [Kernels Requirement Page](https://www.kaggle.com/c/severstal-steel-defect-detection/overview/kernels-requirements)

[⬅️ Back to Index](../README.md)
