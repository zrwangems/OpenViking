---
type: simulink-block
title: 'Video Capture'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Video'
documentation_page: 'videocapture'
documentation_source_path: 'ref/videocapture.html'
language: en
---

# Video Capture

## Ports

### Input

### **msg** — Data message from video capture interface scalar

This message port receives data messages from a connected Video Capture
Interface block. The messages process when the Task Manager
block triggers task containing the Video Capture block. For more
information on messages, see Messages.

**Data Types:** `SoCData`
### Output

### ***`Color`*** — Color component of image *height*-by-*width* matrix

This port outputs a *height*-by-*width* matrix
for that *`Color`* component, where the dimensions are the size
of the image. The **Image size** parameter specifies the
*height* and *width* dimensions.

#### Dependencies

The **Pixel format** parameter sets the color component format
as either `RGB` or `YCbCr
4:2:2`.

**Data Types:** `uint8`

## Parameters

### **Image size** — Image size `160x120` (default) | `320x240` | `640x480` | `800x600` | `custom`

Specify the *height* and *width* dimensions of the
image matrix emitted by the color channel ports of this block. Specify
`custom` to set custom image dimensions.

### **Image size ([width, height])** — Image size `[320, 240]` (default) | `2`-element vector of positive integers

Specify custom *height*-by-*width* dimensions of
the image matrix emitted by the color channel ports.

#### Dependencies

To enable this parameter, set the **Image size** parameter to
`custom`.

### **Pixel format** — Format of the pixel data `RGB` (default) | `YCbCr 4:2:2`

Specify the image data encoding as `RGB` or
`YCbCr 4:2:2` triplets.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

If used in a timer-driven task, enter the sample time of the task defined in the
Task Manager
block. If used in the event-driven task, enter `-1`.

## Libraries

SoC Blockset / Processor I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- To automatically generate C code for your design,
  and execute on an SoC device, use the SoC Builder tool.
  For more information on generating code for SoC designs, see Use SoC Builder to Generate SoC Design.
- To generate and execute C code for your SoC models, this block requires Embedded Coder® and SoC Blockset™ Support Package for Embedded Linux® Devices.
- To use this block, you must set **Hardware Board** to
  `Embedded Linux Board`. You can then follow the instructions
  to configure the board. For more information, see Create an Embedded Linux Device Configuration.

When deployed to a supported hardware board, this block uses the V4L2 driver framework
to capture images from video capture devices, such as a camera. To specify the video capture
device and event triggers, use the Hardware Mapping tool. For more information
on the V4L2 driver framework, see Video4Linux.

## Version History

**Introduced in R2021a**

## Description

Capture video from input video device and send to algorithm

The Video Capture block simulates behavior of the driver code that captures
images from a video device, such as a camera, on your hardware board. The input of this block
must be connected to an Video Capture Interface
block that simulates a physical video source device on the hardware board. Place this block
inside a task and connect it to an algorithm to process an image each time the task executes.
For more information on tasks, see Timer-Driven Task and Event-Driven Tasks.
