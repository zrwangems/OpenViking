---
type: simulink-block
title: 'Write Image'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'writeimageblock'
documentation_source_path: 'ref/writeimageblock.html'
language: en
---

# Write Image

## Ports

### Input

### **Image** — Input image signal *M*-by-*N*-by-3 matrix | *M*-by-*N* matrix

Image pixel data, specified as an
*M*-by-*N*-by-3 matrix for color images, and an
*M*-by-*N* matrix for grayscale images.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — Alpha channel for input image *M*-by-*N* matrix

Alpha channel for image, specified as an
*M*-by-*N* matrix. This matrix is the same height
and width as the image input. Each element has a value in the range
`[0,1]` that indicates the opacity of the corresponding pixel, with
a value of `0` being completely transparent.

#### Dependencies

The selected image encoding must support alpha channel.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`
### Output

### **Msg** — ROS or ROS 2 image message nonvirtual bus

ROS or ROS 2 image message, returned as a nonvirtual bus. You can use the ROS
Publish or ROS 2 Publish block
to publish the message to an active ROS or ROS 2 network respectively.

**Data Types:** `bus`

## Parameters

### **Image Encoding** — Image encoding `rgb8` (default) | `rgba8` | ...

Image encoding for the input **Image**, specified as
one of the supported options. For more information about encoding types, see `rosReadImage`.

## Libraries

ROS Toolbox / ROS ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Write image data to a ROS or ROS 2 message

The Write Image block writes image data to a ROS or ROS 2 image message.
You can specify the encoding for the output image message. Use the ROS Publish or ROS 2 Publish block to
publish the output image message to an active topic on the network.
