---
type: simulink-block
title: 'Video Capture USB'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'videocaptureusb'
documentation_source_path: 'ref/videocaptureusb.html'
language: en
---

# Video Capture USB

## Ports

### Output

### **Y, Cb, Cr** — Color components of input video frame matrix

The block returns one matrix for each color component of the input video. The dimensions
of the **Y** matrix match the frame size. The dimensions of the
**Cb** and **Cr** matrices are
*height*-by-`width/2` because the
4:2:2 format alternates **Cb** and **Cr** values for each
pixel in the frame.

#### Dependencies

To enable these ports, set **Pixel format** to `YCbCr
4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

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

### **IP address** — Address of SoC device 192.168.1.101 (default)

Ethernet address of an SoC device connected to your host machine.

### **Video source** — Source of video stream *detected UVC camera name* | `USB 3.0 Basler Camera` | `Test pattern generator`

The video stream through the FPGA logic and ARM® processor can start with input video from the USB port of the SoC device or with
generated video from the test pattern generator (TPG). Use the **Scan**
button to detect one or more cameras connected to the USB port of your SoC device. The
drop-down menu updates with the names of the detected cameras.

- *detected UVC camera name* — Camera connected to the USB input
  port on the SoC device. The **Frame size** parameter menu updates to match
  the available resolutions from the detected camera.
- `USB 3.0 Basler Camera` — Camera connected to the USB
  input port on the SoC device. The **Frame size** parameter menu updates to
  the list of supported resolutions.
- `Test pattern generator` — On-board TPG. The TPG on the
  SD card creates input frames at the requested resolution. Select a fixed color bar pattern
  or a moving ball in the **Test pattern** parameter. When you select the
  TPG, you do not need a camera connected to the USB port on the SoC device.

### **Test pattern** — On-board video source `SMPTE color bars` | `Moving ball`

The test pattern generator on the SD card creates input frames at the requested
resolution.

- `SMPTE color bars` —

  Color bar test pattern captured when you set Test pattern to SMPTE color bars.
- `Moving ball` —

  Color bar test pattern captured when you set Test pattern to Moving ball.

### **Frame size** — Resolution of input video *detected from camera* | `320x240p` | `640x480p` | `1280x720p` | `1920x1080p`

Select from the supported resolutions available on your detected camera.

To use a frame size greater than 2k resolution, you must configure the FPGA reference
design to use 2-pixel-per-clock streaming. The default reference design loaded during setup
uses 2-pixel-per-clock streaming. You can configure the number of pixels per clock in Step 1.2
of the HDL Workflow Advisor. For details, see Target FPGA on Zynq Hardware.

For a Basler USB 3.0 camera, or the test pattern generator, these resolutions are available:

- `320x240p`
- `640x480p`
- `1280x720p`
- `1920x1080p`

### **Frame rate** — Rate at which consecutive images are displayed (frames per second) *calculated from resolution*

The block calculates available frame rates based on the supported resolutions available
from the detected camera. The block can achieve up to 120 fps for resolutions below
1080p.

The block sets the Simulink sample time for the captured video frames to 1/**Frame
rate**.

### **Host pixel format** — Format of pixel stream imported to Simulink `YCbCr 4:2:2` (default) | `RGB`

Specify the format of the pixel stream as one of these values.

- `RGB` — Three 8 bit color components per pixel, which
  is 24 bits per pixel total.
- `YCbCr 4:2:2` (default) — Also known as YUYV. An 8 bit
  Y component and an interleaved 8 bit CbCr component. The effective pixel size is 16 bits.
  The block returns the component frames on the **Y**,
  **Cb**, and **Cr** output ports.

### **DUT pixel format** — Format of pixel stream in user logic `YCbCr 4:2:2` (default) | `RGB`

Specify the format of the pixel stream as one of these values.

- `RGB` — Three 8 bit color components per pixel, which
  is 24 bits per pixel total.
- `YCbCr 4:2:2` (default) — Also known as YUYV. An 8 bit
  Y component and an interleaved 8 bit CbCr component. The effective pixel size is 16 bits.
  The block returns the component frames on the **Y**,
  **Cb**, and **Cr** output ports.

### **Bypass FPGA user logic** — Send input frames directly to host `off` (default) | `on`

Select this parameter to bypass the user logic section of the FPGA and send the input
video frames directly to the host.

### **Image signal** — RGB output stream format `Separate color signals` (default) | `One multidimensional signal`

Specify the RGB output stream format as one of these values.

- `Separate color signals` — The block returns separate
  *height*-by-*width* matrices for each color component.
  In this case, the block has **R**, **G**, and
  **B** output ports.
- `One multidimensional signal` — The block returns a
  single 3-by-*height*-by-*width* matrix. In this case, the
  block has an **Image** output port.

#### Dependencies

To enable this parameter, set **Pixel format** to
`RGB`.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106 SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Import live video frames from one or more USB cameras on Zynq -based hardware

The Video Capture USB block captures video frames from a Zynq®-based board that has one or more USB video device class (UVC) cameras or
Basler USB 3.0 cameras, and imports the frames into your Simulink® model. The reference design programs the FPGA with an image that includes a USB
camera interface, data path multiplexers, video format conversions, and a video test pattern
generator (TPG). You can control these data path and conversion options from the Video
Capture USB block.
