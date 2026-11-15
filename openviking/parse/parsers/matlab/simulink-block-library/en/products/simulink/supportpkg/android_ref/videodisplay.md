---
type: simulink-block
title: 'Video Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'videodisplay'
documentation_source_path: 'supportpkg/android_ref/videodisplay.html'
language: en
---

# Video Display

## Ports

### Input

### **R** — Red component of image numeric matrix

Red component of an image, specified as a numeric matrix. This matrix must be of
the same size as inputs **G** and **B**.

**Data Types:** `uint8`

### **G** — Green component of image numeric matrix

Green component of an image, specified as a numeric matrix. This matrix must be of
the same size as inputs **R** and **B**.

**Data Types:** `uint8`

### **B** — Blue component of image numeric matrix

Blue component of an image, specified as a numeric matrix. This matrix must be of
the same size as inputs **R** and **G**.

**Data Types:** `uint8`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Support Package for Android Devices / Audio & Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Display video on device screen

Use the Video Display block to display the video on the device screen by
using the red, blue, and green component values of an input image. The dimensions of all the
three input ports **R**,**G**, and **B**
must be equal.
