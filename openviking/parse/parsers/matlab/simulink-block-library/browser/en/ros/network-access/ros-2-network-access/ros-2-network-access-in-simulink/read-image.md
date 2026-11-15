---
type: simulink-block
title: 'Read Image'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'readimageros2'
documentation_source_path: 'ref/readimageros2.html'
language: en
---

# Read Image

## Ports

### Input

### **Msg** — ROS 2 `sensor_msgs/Image` or `sensor_msgs/CompressedImage` message nonvirtual bus

ROS 2 `sensor_msgs/Image` or
`sensor_msgs/CompressedImage` message, specified as a nonvirtual
bus. You can use the Subscribe block
to get a message from an active ROS 2 network.

**Data Types:** `bus`
### Output

### **Image** — Extracted image signal *M*-by-*N*-by-3 matrix | *M*-by-*N* matrix

Extracted image signal from a ROS 2 message, returned as an
*M*-by-*N*-by-3 matrix for color images, and an
*M*-by-*N* matrix for grayscale images. The matrix
contains the pixel data from the `Data` property of the ROS 2
message.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — Alpha channel for image *M*-by-*N* matrix

Alpha channel for image, returned as an
*M*-by-*N* matrix. This matrix is the same height
and width as the image output. Each element has a value in the range
`[0,1]` that indicates the opacity of the corresponding pixel, with
a value of `0` being completely transparent.

**Note**

For `CompressedImage` messages, the alpha channel returns all
zeros if the `Show Alpha output port` is enabled.

#### Dependencies

Enable `Show Alpha output port` parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **ErrorCode** — Error code for image conversion scalar

Error code for image conversion, returned as a scalar. The error code values are:

- `0` — Successfully converted the image message.
- `1` — Incorrect image encoding. Check that the incoming
  message encoding matches the **Image Encoding**
  parameter.
- `2` — The dimensions of the image message exceed the limits
  specified in the **Maximum Image Size**
  parameter.
- `3` — The `Data` field of the image
  message was truncated. See Manage Array Sizes for ROS Messages in Simulink
  to increase the maximum length of the array.
- `4` — Image decompression failed.

**Data Types:** `uint8`

## Parameters

### **Maximum image size** — Maximum image size `[2000 2000]` (default) | two-element vector

Maximum image size, specified as a two-element `[height width]`
vector.

Select **Configure using ROS 2...** to set this parameter
automatically using an active topic on a ROS 2 network. You must be connected to the ROS
2 network.

### **Image encoding** — Image encoding `rgb8` (default) | `rgba8` | ...

Image encoding for the input **ImageMsg**. Select the
encoding type that matches the `Encoding` property of the message. For
more information about encoding types, see `rosReadImage`.

### **Show Alpha output port** — AlphaChannel port toggle `off` (default) | `on`

Toggle alpha channel output port on or off, if the selected encoding type supports
alpha channels.

#### Dependencies

To enable this parameter, set the **Image Encoding**
parameter to an encoding type that supports alpha channels.

### **Show ErrorCode output port** — Toggle ErrorCode port `on` (default) | `off`

Toggle the **ErrorCode** port on or off, to monitor
errors.

### **Output variable-size signals** — Variable-size signal output toggle `off` (default) | `on`

Toggle whether to output a variable-size signal. Use variable-sized signals only if
you expect the image size to change over time. For more information about variable-size
signals, see Variable-Size Signal Basics (Simulink).

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Code generation and deployment of models involving
  `sensor_msgs/CompressedImage` message workflows requires a
  valid version of OpenCV and `cv_bridge` packages to be
  installed.

  For code generation and deployment of models involving
  `sensor_msgs/Image` message workflows, installation of OpenCV
  and `cv_bridge` are not required.

- Local host deployment is not supported for models involving
  `sensor_msgs/CompressedImage` message workflows.
- Bayer encoding is not supported.

## Version History

**Introduced in R2021b**

## Description

Extract image from ROS 2 Image message

The Read Image block extracts an image from a ROS
2 `sensor_msgs/Image` or `sensor_msgs/CompressedImage`
message. You can select the message parameters of a topic active on a live ROS 2 network, or
specify the message parameters separately. The ROS 2 messages are specified as a nonvirtual
bus. Use the Subscribe block output
to receive a message from a ROS 2 network and input the message to the Read
Image block.

**Note**

When reading ROS 2 image messages from the network, the `Data` property
of the message can exceed the maximum array length set in Simulink®. Follow the steps below to increase the maximum array length for all message
types in the model:

1. Enable ROS options by selecting the **Robot Operating System
   (ROS)** app under the **Apps** tab and configure the ROS
   network parameters appropriately.
2. From the **Prepare** section under
   **Simulation** tab, select **ROS Toolbox** > **Variable Size Messages**.
3. Uncheck **Use default limits for this message type** and then in
   the **Maximum length** column, increase the length based on the
   number of pixels in the image.
