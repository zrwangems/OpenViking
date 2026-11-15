---
type: simulink-block
title: 'PARROT Image Conversion'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'parrotimageconversion'
documentation_source_path: 'supportpkg/parrot_ref/parrotimageconversion.html'
language: en
---

# PARROT Image Conversion

## Ports

### Input

### **Port\_1** — Image in Y1UY2V format 4x9600 array

The input image is obtained from the downward-facing camera of
Parrot minidrone, and it is represented as a 4-by-9600 array.
This input is encoded in the Y1UY2V format.

**Data Types:** `uint8`
### Output

### **Y** — Luminance of image when converted to YUV format 120x160 array

**Data Types:** `uint8`

### **U** — U chrominance of image when converted to YUV format 120x160 array

**Data Types:** `uint8`

### **V** — V chrominance of image when converted to YUV format 120x160 array

**Data Types:** `uint8`

### **R** — Red color in image when converted to RGB format 120x160 array

**Data Types:** `uint8`

### **G** — Green color in image when converted to RGB format 120x160 array

**Data Types:** `uint8`

### **B** — Blue color in image when converted to RGB format 120x160 array

**Data Types:** `uint8`

## Parameters

### **Output color space** — Select color space for conversion `YUV` (default) | `RGB`

Select the color space, either YUV or RGB, for converting the image from
the encoded Y1UY2V format.

When you set this parameter to `YUV`, the Y, U, and V
components are available as separate output ports.

When you set this parameter to `RGB`, the R, G, and B
components are available as separate output ports.

## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Convert the encoded Y1UY2V image format to YUV or RGB format

The PARROT Image Conversion block converts an image that is encoded in
Y1UY2V format, as obtained from the Parrot® minidrone's downward-facing camera, to either YUV or RGB format. The block
separates the color components and provides them as the output.
