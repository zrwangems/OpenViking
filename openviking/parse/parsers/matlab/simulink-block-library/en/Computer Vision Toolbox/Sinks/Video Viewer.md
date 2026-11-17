---
type: simulink-block
title: 'Video Viewer'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'videoviewer'
documentation_source_path: 'ref/videoviewer.html'
language: en
---

# Video Viewer

## Ports
```yaml
ports:
- name: Image
  summary: Input image or video matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | Simulink.ImageType
- name: R
  summary: Red color component of image or video matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: G
  summary: Green color component of image or video matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: B
  summary: Blue color component of image or video matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### Input

### **Image** — Input image or video matrix | array

Input image or video, specified as an *M*-by-*N*
matrix, *M*-by-*N*-by-*T* array, or
*M*-by-*N*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

#### Dependencies

To enable this port, select the **One Multi-Dimensional Signal** parameter. This parameter is enabled by default.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `Simulink.ImageType`

### **R** — Red color component of image or video matrix | array

Red color component of the image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array.
*T* is the number of frames in a video or image sequence.

**Note**

Inputs to the **R**, **G**, and
**B** ports must all have the same dimensions and data
type.

#### Dependencies

To enable this port, select the  **Separate Color Signals** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — Green color component of image or video matrix | array

Green color component of the image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array.
*T* is the number of frames in a video or image sequence.

**Note**

Inputs to the **R**, **G**, and
**B** ports must all have the same dimensions and data
type.

#### Dependencies

To enable this port, select the  **Separate Color Signals** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — Blue color component of image or video matrix | array

Blue color component of the image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array.
*T* is the number of frames in a video or image sequence.

**Note**

Inputs to the **R**, **G**, and
**B** ports must all have the same dimensions and data
type.

#### Dependencies

To enable this port, select the  **Separate Color Signals** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
## Parameters
```yaml
parameters:
- name: Open at Start of Simulation
  summary: Open video viewer window at start of simulation on (default) | off
  group: File
- name: Separate Color Signals
  summary: Enable separate R, G, and B color channels as input off (default) | on
  group: File
- name: One Multi-Dimensional Signal
  summary: Enable one multi-dimensional signal as input on (default) | off
  group: File
- name: Display the full path
  summary: Display full path of source data in the title bar off (default) | on
  group: File > Configuration > Edit > Core
- name: Open new Image Viewer window for each export
  summary: Open new Image Viewer window for each exported video frame on (default) | off
  group: File > Configuration > Edit > Tools
- name: Colormap
  summary: Set colormap gray(256) (default) | parula(256) | jet(256) | hot(256) | bone(256) | cool(256) | copper(256)
  group: Tools > Colormap
- name: Specify range of displayed pixel values [-Inf to Inf]
  summary: Specify range of intensity value to display off (default) | on
  group: Tools > Colormap
- name: Min
  summary: Minimum intensity value 0 (default) | numeric scalar
  group: Tools > Colormap
- name: Max
  summary: Maximum intensity value 255 (default) | numeric scalar
  group: Tools > Colormap
- name: Drop Frames to Improve Performance
  summary: Drop frame rate of input video signal on (default) | off
  group: Simulation
```

### File

To access these parameters, select the **File** menu in the Video
Viewer window

### **Open at Start of Simulation** — Open video viewer window at start of simulation `on` (default) | `off`

Select this parameter to automatically open the Video Viewer window at the start
of the simulation. Clear this parameter to prevent the Video Viewer window from
opening at the start of the simulation.

### **Separate Color Signals** — Enable separate R, G, and B color channels as input `off` (default) | `on`

Select this parameter to enable the **R**,
**G**, and **B** input ports for separate color
channels. If you select this parameter, the **One Multi-Dimensional
Signal** parameter clears automatically.

### **One Multi-Dimensional Signal** — Enable one multi-dimensional signal as input `on` (default) | `off`

Select this parameter to enable the **Image** input port for one
multi-dimensional signal. If you select this parameter, the **Separate Color
Signals** parameter clears automatically.

### File > Configuration > Edit > Core

The Video Viewer **Configuration** parameters enable you to change the
behavior and appearance of the graphic user interface (GUI).

- To open the Configuration dialog box and edit parameters, select **File** > **Configuration**  > **Edit**.

The **Core** tab in the Configuration dialog box lists the general
settings of the GUI.

- In the **Core** tab, select `General UI`
  item and click the **Properties** button to open the General UI
  Properties dialog box.

### **Display the full path** — Display full path of source data in the title bar `off` (default) | `on`

Select this parameter to display the model name and full path to the source data
in the title bar of the Video Viewer window. If you clear this parameter, the window
displays a shortened name.

### File > Configuration > Edit > Tools

The Video Viewer **Configuration** parameters enable you to change the
behavior and appearance of the graphic user interface (GUI).

- To open the Configuration dialog box and edit parameters, select **File** > **Configuration**  > **Edit**.

The **Tools** tab in the Configuration dialog box lists the tools
associated with the Video Viewer block.

- In the **Tools** tab, select the `Image
  Viewer` item and click the **Properties** button to
  open the Image Viewer Properties dialog box.

### **Open new Image Viewer window for each export** — Open new Image Viewer window for each exported video frame `on` (default) | `off`

Select this parameter to open a new **Image Viewer** window for
each exported video frame or image in an image sequence.

### Tools > Colormap

The **Colormap** parameters enable you to display an intensity image in
various colormap formats and control the output intensity range. To access these parameters,
select **Tools** > **Colormap** or press **C**.

**Note**

The **Colormap** parameters are available for intensity images
only.

### **Colormap** — Set colormap `gray(256)` (default) | `parula(256)` | `jet(256)` | `hot(256)` | `bone(256)` | `cool(256)` | `copper(256)`

This parameter specifies the colormap in which to display the input intensity
image. This block supports the `gray(256)`,
`parula(256)`, `jet(256)`,
`hot(256)`, `bone(256)`, and
`copper(256)` colormaps.

### **Specify range of displayed pixel values [-Inf to Inf]** — Specify range of intensity value to display `off` (default) | `on`

Select this parameter to enable the **Min** and
**Max** parameters, through which you can specify the display range
of pixel intensities.

### **Min** — Minimum intensity value `0` (default) | numeric scalar

If a pixel has an intensity value less than or equal to the value of this
parameter, **Video Viewer** displays it as the first color in the
selected colormap.

**Note**

When specifying a value for **Min**, remember that the data
type of the input image or video determines the range of intensity values
representing that image or video.

#### Dependencies

To enable this parameter, select the **Specify range of displayed pixel
values [-Inf to Inf]** parameter.

### **Max** — Maximum intensity value `255` (default) | numeric scalar

If a pixel has an intensity value higher than or equal to the value of this
parameter, **Video Viewer** displays it as the last color in the
selected colormap.

**Note**

When specifying a value for **Max**, remember that the data
type of the input image or video determines the range of intensity values
representing that image or video.

#### Dependencies

To enable this parameter, select the **Specify range of displayed pixel
values [-Inf to Inf]** parameter.

### Simulation

To access this parameter, select the **Simulation** menu in the Video
Viewer window.

### **Drop Frames to Improve Performance** — Drop frame rate of input video signal `on` (default) | `off`

Select this parameter to reduce the frame rate of the input video signal to
improve performance of the simulation. If you unselect this parameter, the block
displays all the frames in the input video signal during simulation.
## Libraries

Computer Vision Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Display images or video frames

The Video Viewer block displays images or video frames. This block provides
simulation controls to play, pause, and step while streaming a video or image sequence. This
block also provides tools to analyze the pixels of a region of interest.

Video Viewer Window

### Features of Video Viewer

- Playback control — Control video playback using the Run, Step Forward, and Stop
  buttons.
- Export to **Image Viewer** — To open the displayed image in a
  separate window using the **Image Viewer** app, select **File** >  **Export to Image Viewer**. Alternatively, select the Export to Image Viewer button in the toolbar.
  For more information, see Get Started with Image Viewer App.
- Pixel region analysis— To open the displayed image in a separate window using the
  Pixel Region tool, select **Tools** >  **Pixel Region**. Alternatively, select the Inspect pixel values button in the toolbar.
  For more information about Pixel Region tool, see `impixelregion`.
