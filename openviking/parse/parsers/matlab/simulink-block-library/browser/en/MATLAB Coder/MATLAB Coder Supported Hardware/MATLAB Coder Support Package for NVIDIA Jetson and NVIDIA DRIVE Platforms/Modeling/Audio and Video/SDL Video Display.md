---
type: simulink-block
title: 'SDL Video Display'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'nvidia/ref/sdlvideodisplay.html'
language: en
---

# SDL Video Display

## Ports

### Input

### **R** — Red component of the input video stream matrix

Input port to specify red component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **G** — Green component of the input video stream matrix

Input port to specify green component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **B** — Blue component of the input video stream matrix

Input port to specify blue component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **Y** — Luminance component of the input video stream matrix

Input port to specify the luma component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

### **Cb** — Blue difference component of the input video stream matrix

Input port to specify the blue difference component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

### **Cr** — Red difference component of the input video stream matrix

Input port to specify the red difference component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

## Parameters

### **Pixel format** — Input video stream format `RGB` (default) | `YCbCr 4:2:2`

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

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pixelFormat` |
| **Type:** character vector |
| **Values:** `'RGB'`|`'YCbCr 4:2:2'` |
| **Default:**  `'RGB'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Display video on a monitor connected to the NVIDIA target

Display video data using the Simple DirectMedia Layer (SDL) multimedia library. A
Simulink® model can contain only one SDL Video Display block.

This block takes planar video data in `YCbCr 4:2:2` or
`RGB` formats.

Install the Simple DirectMedia Layer (SDL) library on the target. For more information,
see Prerequisites for Generating Code for NVIDIA Boards.
