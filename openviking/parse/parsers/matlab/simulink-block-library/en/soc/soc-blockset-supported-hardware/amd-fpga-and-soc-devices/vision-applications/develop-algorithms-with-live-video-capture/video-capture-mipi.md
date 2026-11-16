---
type: simulink-block
title: 'Video Capture MIPI'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'videocapturemipi'
documentation_source_path: 'ref/videocapturemipi.html'
language: en
---

# Video Capture MIPI

## Ports

### Output

### **R, G, B** — Color components of input video frame matrix

The block returns one matrix for each color component of the input video. The dimensions
of each matrix match the frame size.

#### Dependencies

To enable these ports, set **Pixel format** to
`RGB` and **Image signal** to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Image** — Color input video frame matrix

The block returns a 3-by-*height*-by-*width* matrix,
where *height* and *width* match the frame size.

#### Dependencies

To enable this port, set **Pixel format** to
`RGB` and **Image signal** to `One
multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Video source** — Source of video stream `IMX274 sensor`

The video stream originates from the IMX274 camera board. Set the **Frame
size** parameter to match the resolution of your attached camera.

### **Frame size** — Resolution of input video `1280x720p` (default) | `1920x1080p`

Select 720p HDTV format (`1280x720p`) or 1080p HDTV format
(`1920x1080p`).

### **Frame rate** — Rate at which consecutive images are displayed (frames per second) `120 fps` (default) | `60 fps`

The block sets the Simulink sample time for the captured video frames to 1/**Frame
rate**.

Frame size `1920x1080p` supports only `60
fps`.

### **Pixel format** — Format of pixel stream `RGB`

The `RGB` pixel stream format returns three 8-bit color
components per pixel, which is 24 bits per pixel total. You can also select whether the block
returns a multidimensional signal or three separate color signals. For details, see the
**Image signal** parameter.

### **Image signal** — RGB output stream format `Separate color signals` (default) | `One multidimensional signal`

Specify the RGB output stream format as one of these values.

- `Separate color signals` — The block returns separate
  *height*-by-*width* matrices for each color component.
  In this case, the block has **R**, **G**, and
  **B** output ports.
- `One multidimensional signal` — The block returns a
  single 3-by-*height*-by-*width* matrix. In this case, the
  block has an **Image** output port.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Import live video frames from MIPI CSI-2 card on Zynq-based hardware

The Video Capture MIPI block captures video frames from an IMX274 FMC
MIPI®
CSI-2® card connected to a Zynq®-based board and imports the frames into your Simulink® model. The reference design programs the FPGA with an image that demosaics and
gamma-corrects the video input from the sensor, and allows capture of the video from Simulink.
You can control the frame size and Simulink video signal format options from the Video Capture MIPI
block.

The FPGA image also contains an IP core called the FPGA user logic that you
can generate from your design by using HDL Workflow Advisor. The block captures the input video
after the FPGA user logic.

The video data is in AXI4-Stream Video format on the FPGA. When you import the video into
Simulink, the stream converts to frame-based video.

The `MIPI Receive path` reference design requires the same video
resolution and color format for the entire data path.
The design you target to the FPGA user logic must not modify the frame size or format of the
data.
