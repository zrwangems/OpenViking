---
type: simulink-block
title: 'Camera'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'nvidiacamera'
documentation_source_path: 'nvidia/ref/nvidiacamera.html'
language: en
---

# Camera

## Ports

### Output

### **R** — Red component of the output video stream matrix

This port outputs the red component of each pixel.

**Data Types:** `uint8`

### **G** — Green component of the output video stream matrix

This port outputs the green component of each pixel.

**Data Types:** `uint8`

### **B** — Blue component of the output video stream matrix

This port outputs the blue component of each pixel.

**Data Types:** `uint8`

## Parameters

### **Name** — Name of connected video device `My Camera` (default)

Enter the path and name of the video device.

The Linux® kernel creates a video device file when you connect a supported USB or CSI
video camera to the target hardware. To see the list of video device files, open a
command line session with the target hardware and enter: `ls -al
/dev/video*`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CameraName` |
| **Type:** character vector |
| **Values:** `valid name`| |
| **Default:**  `'My Camera'` |

### **Image size** — Display resolution `[320, 240]` (default) | `[width, height]`

Specify the display resolution of the image to be captured, in pixels.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ImageSize` |
| **Type:** character vector |
| **Values:** `[width, height]`| |
| **Default:**  `'[320, 240]'` |

### **Sample time** — Frequency at which a new image is captured `0.1` (default) | scalar | `vector`

Select the sample time of the video device.

Smaller values require the processor to complete the same number of instructions in
less time, which can cause task overruns.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0.1'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Capture video from a USB or CSI camera connected to the NVIDIA target

Capture live video from a USB or CSI camera. The output is in row major format. During
simulation, the model outputs a moving colorbar image.

Install the GStreamer library, V4L2 library, and V4L2 utilities on the target. You must
also install the development packages for these libraries. For more information, see Prerequisites for Generating Code for NVIDIA Boards
