---
type: simulink-block
title: 'Video Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'videoread'
documentation_source_path: 'nvidia/ref/videoread.html'
language: en
---

# Video Read

## Ports

### Output

### **Image** — Color image or video frame array

Color image or video frame, returned as an
*M*-by-*N*-by-*P* array.
*M* and *N* are the number of rows and columns in
each image. *P* is the number of color channels in each image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Simulink.ImageType`

### **R** — Red color component of image or video frame matrix

Red color component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **G** — Green color component of image or video frame matrix

Green color component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **B** — Blue color component of image or video frame matrix

Blue color component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **EOF** — End-of-file indicator scalar

End-of-file indicator, returned as a logical scalar for each video frame. The
end-of-file indicator is `1` when the block outputs the final video
frame from the file, and is `0` otherwise.

#### Dependencies

To enable this port, select the **Output end-of-file
indicator** parameter.

**Data Types:** `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### General Parameters

### **File name** — Name of multimedia file no default

Name of the multimedia file on the target for the block to read.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **Values:** | ' ' (default) | character vector |

### **Sample time** — Block sample time `0.033333333333333333` (default) | real positive scalar

Sample time for the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `1/30` (default) | real positive scalar |

#### Video Parameters

### **Image size** — Resolution of the image or video frame `[640, 480]` (default) | `[width, height]`

Resolution of the image or video frame, in pixels.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ImageSize` |
| **Values:** | `'[640, 480]'` (default) | `[width, height]` |

### **Image signal** — Output port configuration `One multidimensional signal` (default) | `Separate color signal`

How the block outputs the RGB color video. If you select `One
multidimensional signal`, the block outputs the video data using only the
**Image** port. If you select `Separate color
signal`, the block outputs the video data using three separate color
channels, divided across the **R**, **G**, and
**B** ports.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ImageSignal` |
| **Values:** | `'One multidimensional signal'` (default) | `'Separate color signal'` |

### **Output end-of-file indicator** — End-of-file indicator `off` (default) | `on`

Select this parameter to enable the **EOF** port, which indicates
whether the output frame or sample is the final video frame in the multimedia
file.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputEOFIndicator` |
| **Values:** | `'off'` (default) | `'on'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Read video frames from multimedia file on NVIDIA target

The Video Read block reads video frames from a multimedia file on the
NVIDIA® target platform.

This block uses the GStreamer
framework to handle data streaming. You can use the video formats supported by your installed
plug-ins for GStreamer 1.0 or higher, as listed on Plugins.
