# Oil Storage Tanks

**Summary:** Image data of industrial tanks with bounding box annotations for floating head oil storage tanks.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Object Detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Image data, Multivariate |
| **Date Donated** | 2019-06-05 |
| **Feature Type** | Image |
| **Labeled** | Yes |
| **Missing Values** | Information not available |
| **Name** | Oil Storage Tanks |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | Kaggle |
| **Time Series** | No |

## Description

Oil storage tanks play an important role in the global economy. Crude oil is stored in tanks at many points between extraction and sale. Storage tanks are also used by nations to stockpile oil reserves. The volume of oil in storage is an important economic indicator. It indicates which oil producing nations are increasing or decreasing production and gives a window into the global demand for energy. At the same time, oil storage information is not transparent. Nations may hide information about oil production, consumption and storage for economic or military reasons. For this reason, companies like Planet and Orbital Insight have made a business of collecting satellite imagery of oil storage tanks and estimating reserve volumes.

Tank volume estimation is possible because oil is typically stored in floating head tanks. This particular tank type has a head that sits directly on top of the crude oil to prevent buildup of fumes. As a result, the height of the tank head rises and falls with the volume of oil in the tank. The relative sizes of the exterior shadow cast by the tank itself and the interior shadow cast by the height of the tank head can be used to estimate the tank volume.

The dataset contains satellite images taken from Google Earth of tank-containing industrial areas around the world. Images are annotated with bounding box information for floating head tanks in the image. Fixed head tanks are not annotated. The large_images directory contains the raw 4800x4800 images saved from Google Earth. The image_patches directory contains 512x512 patches generated from the large image. Labels are provided in labels.json and labels_coco.json files with bounding box coordinates. Additional metadata is contained in large_image_data.csv, including geographic coordinates and altitude. This dataset was made possible by Google Earth.

## Tags

Bounding box annotations, Energy sector, Floating head tanks, Google Earth images, Object detection, Oil storage tanks, Satellite imagery

## References

- [Kaggle Dataset: Oil Storage Tanks](https://www.kaggle.com/datasets/towardsentropy/oil-storage-tanks)
- [Planet](https://www.planet.com/)
- [Orbital Insight](https://orbitalinsight.com/)
- [COCO label format](http://cocodataset.org/#format-data)

[⬅️ Back to Index](../README.md)
