---
type: simulink-block
title: 'Video Display'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Video'
documentation_page: 'videodisplay'
documentation_source_path: 'ref/videodisplay.html'
language: en
---

# Video Display

## Ports

### Input

### ***`Color`*** — Color component of image *height*-by-*width* size matrix

Specify a *height*-by-*width* matrix, where the
dimensions are the size of the image.

#### Dependencies

Use the **Pixel format** parameter to specify the color
component format as either `RGB` or `YCbCr
4:2:2`.

**Data Types:** `uint8`
### Output

### **msg** — Data message to the video display interface scalar

This port outputs data messages containing image data to a connected Video Display
Interface block. For more information on messages, see Messages.

**Data Types:** `SoCData`

## Parameters

### **Pixel format** — Format of pixel data `RGB` (default) | `YCbCr 4:2:2`

Specify the input image data encoding as `RGB` or
`YCbCr 4:2:2` triplets.

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

Display image samples from an algorithm to an output video device

The Video Display block simulates behavior of the driver code that displays
images to a video output, such as an LCD screen, on a hardware board. The output of this block
must be connected to a Video Display Interface
block that simulates a physical display screen on the hardware board. Place this block inside
a task and connect to an algorithm to output an image each time the task executes. For more
information on tasks, see Timer-Driven Task and Event-Driven Tasks.
