---
type: simulink-block
title: 'SDL Video Display'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'beaglebone/ref/sdlvideodisplay.html'
language: en
---

# SDL Video Display

## Ports

### Input

### **R** — Red component of input video matrix

Input port at which to specify the red component of each pixel of the input
video.

#### Dependencies

- To enable this port, set **Pixel format** to
  `RGB`.

**Data Types:** `uint8`

### **G** — Green component of input video matrix

Input port at which to specify the green component of each pixel of the input
video.

#### Dependencies

- To enable this port, set **Pixel format** to
  `RGB`.

**Data Types:** `uint8`

### **B** — Blue component of input video matrix

Input port at which to specify the blue component of each pixel of the input
video.

#### Dependencies

- To enable this port, set **Pixel format** to
  `RGB`.

**Data Types:** `uint8`

### **Y** — Luminance component of input video matrix

Input port at which to specify the luma component of each pixel of the input
video.

#### Dependencies

- To enable this port, set **Pixel format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cb** — Blue difference component of input video matrix

Input port at which to specify the blue difference component of each pixel of the
input video.

#### Dependencies

- To enable this port, set **Pixel format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cr** — Red difference component of input video matrix

Input port at which to specify the red difference component of each pixel of the
input video.

#### Dependencies

- To enable this port, set **Pixel format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

## Parameters

### **Pixel format** — Input video stream format `RGB` (default) | `YCbCr 4:2:2`

Specify the format of the input video stream as `RGB` or
`YCbCr 4:2:2`.

`RGB` format uses three 8-bit values to represent the red,
green, and blue components of each pixel.

`YCbCr 4:2:2` uses three channels to represent color image
data for each pixel:

- Y is the luma component (essentially a grayscale signal).
- Cb is the blue difference chroma component.
- Cr is the red difference chroma component.

Cb and Cr are sampled at half the rate of Y. Therefore if the dimensions of Y are
M\*N, the dimensions of Cb and Cr are each (M/2) by N.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Display video using SDL

The SDL Video Display block displays video data using the Simple
DirectMedia Layer (SDL). This block accepts planar video data in the
`RGB` or `YCbCr 4:2:2` formats.
