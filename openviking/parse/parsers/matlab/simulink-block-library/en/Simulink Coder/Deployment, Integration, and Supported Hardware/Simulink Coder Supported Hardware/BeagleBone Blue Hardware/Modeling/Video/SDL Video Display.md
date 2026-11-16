---
type: simulink-block
title: 'SDL Video Display'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Video'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'beagleboneblue/ref/sdlvideodisplay.html'
language: en
---

# SDL Video Display

## Ports

### Input

### **R** — Red component of pixel matrix

Input port to specify red component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **G** — Green component of pixel matrix

Input port to specify green component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **B** — Blue component of pixel matrix

Input port to specify blue component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **Y** — Luma component of pixel matrix

Input port to specify the luma component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

### **Cb** — Blue difference component of pixel matrix

Input port to specify the blue difference component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

### **Cr** — Red difference component of pixel matrix

Input port to specify the red difference component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

## Parameters

### **Pixel format** — Format of input video stream RGB (default) | YCbCr 4:2:2

Specify the format of the input video stream: `YCbCr 4:2:2`
or `RGB`.

`YCbCr 4:2:2` uses three channels to represent color image
data for each pixel:

- Y is the luma component (essentially a grayscale signal).
- Cb is the blue-difference chroma component.
- Cr is the red-difference chroma component.

Cb and Cr are sampled at half the rate of Y. Therefore, if the dimensions of Y are
M\*N, the dimensions of Cb and Cr are each (M/2) by N.

`RGB` uses three 8-bit values to represent the red, green,
and blue components of each pixel.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Display video using SDL

Display video data using the Simple Directmedia Layer (SDL) multimedia library. A
Simulink® model can contain only one SDL Video Display block.

This block takes planar video data in YCbCr 4:2:2 or RGB formats.
