# AITEX Fabric Image Database

**Summary:** The textile fabric database consists of 245 images of 7 different fabrics, including 140 defect-free images and 105 images with different types of defects.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Classification, Defect detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Multiclass |
| **Date Donated** | 2019 |
| **Feature Type** | Image pixels (Real) |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | AITEX Fabric Image Database |
| **Number of Features** | Information not available |
| **Number of Instances** | 245 |
| **Source** | AITEX |
| **Time Series** | No |

## Description

The AITEX Fabric Image Database contains images of textile fabrics used for defect detection. It consists of 245 images of 7 different fabric types. Among these, 140 images are defect-free (20 for each type of fabric) and 105 images contain different defect types.

Each image has a size of 4096×256 pixels. Defective images follow a naming convention of nnnn_ddd_ff.png where nnnn is the image number, ddd is the defect code, and ff is the fabric code. A corresponding defect mask image is also provided for defective images, named nnnn_ddd_ff_mask.png, where white pixels represent the defect area.

Defect-free images are coded as nnnn_000_ff.png where the defect code is replaced by 000. The dataset uses several defect codes such as Broken end (2), Broken yarn (6), Broken pick (10), Weft curling (16), Fuzzyball (19), Cut selvage (22), Crease (23), Warp ball (25), Knots (27), Contamination (29), Nep (30), and Weft crack (36).

## Tags

Defect detection, Fabric defect masks, Image dataset, Multiclass classification, Pattern recognition, Real images, Textile fabrics

## References

- [AITEX Fabric Image Database Publication](https://content.sciendo.com/view/journals/aut/ahead-of-print/article-10.2478-aut-2019-0035.xml)
- [AITEX Website - AFID](https://www.aitex.es/afid/)

[⬅️ Back to Index](../README.md)
