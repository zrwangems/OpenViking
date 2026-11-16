---
type: simulink-block
title: 'Video Capture Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'videocaptureinterface'
documentation_source_path: 'ref/videocaptureinterface.html'
language: en
---

# Video Capture Interface

## Ports

### Input

### **data** — Image data `3`*M**N*-length vector

Specify a `3`*M**N*-length
vector as the unwrapped images matrices.

#### Dependencies

To enable this port, set the **Input** parameter to
`From input port`.

**Data Types:** `uint8`
### Output

### **event** — Task event signal scalar

This port sends a message at each new image event. This output connects to the
input of the Task Manager
block to execute the associated event-driven task after receiving the new
image.

#### Dependencies

To enable this port, select the **Show event port**
parameter.

**Data Types:** `rteEvent`

### **msg** — SoC message data scalar

This port outputs data messages containing image data to a connected Video Capture
block.

**Data Types:** `SoCData`

## Parameters

### **Input** — Source of simulated video data `From dialog` (default) | `From input port` | `From timeseries object`

Specify the source of the simulated image data.

### **Value** — Image to be imported `uint8(floor(rand(1,3*160*120)*255))` (default) | 3*M**N*-element vector

Specify the simulated image as a vector. The vector gets transformed into three
*M*-by-*N* matrices representing the color channels
of the image source.

### **Object name** — Timeseries object name [] (default) | MATLAB workspace variable

Specify the video source as a timeseries object in the MATLAB® workspace.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

Enter the sample time defining the rate at which to output the message containing
video data.

### **Show event port** — Option to enable task event ports `off` (default) | `on`

Select this parameter to enable an event port that, when connected to the Task Manager
block, can execute event-driven tasks.

## Libraries

SoC Blockset / Peripherals

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

Embedded Coder does not generate code for this block. In the
generated code,the V4L2 driver framework performs the video capture on the device. The
related Video Capture block represents the V4L2 driver. For more information
on the V4L2 driver framework, see Video4Linux.

## Version History

**Introduced in R2021a**

## Description

Simulate capture of images from video stream on hardware

The Video Capture Interface block simulates the behavior of a video input
device. The block emits the captured image in message for a connected Video Capture block
that can be used in an algorithm. The block can also emit an event that, when connected a
Task Manager block, can
trigger a task containing the Video Capture block.
