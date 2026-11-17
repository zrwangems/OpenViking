---
type: simulink-block
title: 'Video Display Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'videodisplayinterface'
documentation_source_path: 'ref/videodisplayinterface.html'
language: en
---

# Video Display Interface

## Ports
```yaml
ports:
- name: msg
  summary: SoC message data vector
  direction: input
  data_types: SoCData
- name: data
  summary: Image data 3\height*\width*-element vector
  direction: output
  data_types: uint8
```

### Input

### **msg** — SoC message data vector

This port receives the image data as a message from the **msg**
port of a connected Video Display
block.

**Data Types:** `SoCData`
### Output

### **data** — Image data 3\**height*\**width*-element vector

The port outputs the unwrapped image matrix data as three
*height**width*-element vectors where
*height* and *width* are the dimensions of the
image matrix defined by the `Image Size` parameter. The
`3` is the multiplier for the RGB channels.

#### Dependencies

To enable this port, set the **Output** parameter to
`To output port`.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Output
  summary: Output type To terminator (default) | To output port
  group: ''
- name: Image size
  summary: Image size 160x120 (default) | 320x240 | 640x480 | 800x600 | custom
  group: ''
- name: Image size ([width, height])
  summary: Image size [320, 240] (default) | two-element vector of positive integers
  group: ''
- name: Pixel format
  summary: Format of the pixel data RGB (default) | YCbCr 4:2:2
  group: ''
- name: Sample time
  summary: Sample time in seconds -1 (default) | positive scalar
  group: ''
```

### **Output** — Output type `To terminator` (default) | `To output port`

Specify if the block acts as a terminator, similar to the Terminator block, or produces data to an output port.

### **Image size** — Image size `160x120` (default) | `320x240` | `640x480` | `800x600` | `custom`

Specify the height and width dimensions of the image emitted as a vector by the
`data` port of this block. Specify `custom` to set
custom image dimensions.

### **Image size ([width, height])** — Image size `[320, 240]` (default) | two-element vector of positive integers

Specify custom height and width dimensions of the image matrix emitted by the data
port of this block.

#### Dependencies

To enable this parameter, set the **Image size** parameter to
`custom`.

### **Pixel format** — Format of the pixel data `RGB` (default) | `YCbCr 4:2:2`

Specify the image data output encoding as `RGB` or
`YCbCr 4:2:2` triplets.

#### Dependencies

To enable this parameter, set the **Image size** parameter to
`custom`.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

Enter the sample time defining the rate at which to receive the message containing
video data.
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
generated code,the V4L2 driver framework performs the video display on the device. The
related Video Display block represents the V4L2 driver. For more information
on the V4L2 driver framework, see Video4Linux.

## Version History

**Introduced in R2021a**

## Description

Simulate display of images to video screen on device

The Video Display Interface block simulates the behavior of a video output
device. This block receives image samples as messages from a connected Video Display block
that simulates the video driver code connected to your algorithm.
