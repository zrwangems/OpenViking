---
type: simulink-block
title: 'Read Image'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'readimageros1'
documentation_source_path: 'ref/readimageros1.html'
language: en
---

# Read Image

## Ports
```yaml
ports:
- name: Msg
  summary: ROS sensor_msgs/Image or sensor_msgs/CompressedImage message nonvirtual bus
  direction: input
  data_types: bus
- name: Image
  summary: Extracted image signal *M*-by-*N*-by-3 matrix | *M*-by-*N* matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16
- name: AlphaChannel
  summary: Alpha channel for image *M*-by-*N* matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16
- name: ErrorCode
  summary: Error code for image conversion scalar
  direction: output
  data_types: uint8
```

### Input

### **Msg** — ROS `sensor_msgs/Image` or `sensor_msgs/CompressedImage` message nonvirtual bus

ROS `sensor_msgs/Image` or
`sensor_msgs/CompressedImage` message, specified as
a nonvirtual bus. You can use the Subscribe block to get a
message from an active ROS network.

**Data Types:** `bus`
### Output

### **Image** — Extracted image signal *M*-by-*N*-by-3 matrix | *M*-by-*N* matrix

Extracted image signal from ROS message, returned as an *M*-by-*N*-by-3 matrix for color images, and an *M*-by-*N* matrix for grayscale images. The matrix contains the pixel data from the `Data` property of the ROS message.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — Alpha channel for image *M*-by-*N* matrix

Alpha channel for image, returned as an
*M*-by-*N* matrix. This matrix is
the same height and width as the image output. Each element has a value
in the range `[0,1]` that indicates the opacity of the
corresponding pixel, with a value of `0` being
completely transparent.

**Note**

For `CompressedImage` messages, the alpha
channel returns all zeros if the `Show Alpha output
port` is enabled.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **ErrorCode** — Error code for image conversion scalar

Error code for image conversion, returned as a scalar. The error code
values are:

- `0` — Successfully converted the image
  message.
- `1` — Incorrect image encoding. Check
  that the incoming message encoding matches the **Image Encoding** parameter.
- `2` — The dimensions of the image message
  exceed the limits specified in the **Maximum Image Size** parameter.
- `3` — The `Data` field
  of the image message was truncated. See Manage Array Sizes for ROS Messages in Simulink to increase the maximum
  length of the array.
- `4` — Image decompression
  failed.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Maximum Image Size
  summary: Maximum image size [2000 2000] (default) | two-element vector
  group: ''
- name: Image Encoding
  summary: Image encoding rgb8 (default) | rgba8 | ...
  group: ''
- name: Show Alpha output port
  summary: Toggle AlphaChannel port off (default) | on
  group: ''
- name: Show ErrorCode output port
  summary: Toggle ErrorCode port on (default) | off
  group: ''
- name: Output variable-size signals
  summary: Toggle variable-size signal output off (default) | on
  group: ''
```

### **Maximum Image Size** — Maximum image size `[2000 2000]` (default) | two-element vector

Maximum image size, specified as a two-element `[height width]` vector.

Click **Configure using ROS** to set this parameter
automatically using an active topic on a ROS network. You must be connected
to the ROS network.

### **Image Encoding** — Image encoding `rgb8` (default) | `rgba8` | ...

Image encoding for the input **ImageMsg**.
Select the supported encoding type which matches the
`Encoding` property of the message. For more
information about encoding types, see `rosReadImage`.

### **Show Alpha output port** — Toggle AlphaChannel port off (default) | on

Toggle Alpha channel output port if your encoding supports an Alpha channel.

#### Dependencies

Only certain encoding types support alpha channels. The **Image Encoding** parameter determines if this
parameter appears in the block mask.

### **Show ErrorCode output port** — Toggle ErrorCode port on (default) | off

Toggle the **ErrorCode** port to monitor
errors.

### **Output variable-size signals** — Toggle variable-size signal output off (default) | on

Toggle variable-size signal output. Variable-sized signals should only be used if the image size is expected to change over time. For more information about variable sized signals, see Variable-Size Signal Basics (Simulink).
## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Code generation and deployment of models involving
  `sensor_msgs/CompressedImage` messages workflow
  requires a valid version of OpenCV and `cv_bridge`
  packages to be installed.

  For code generation and deployment of models involving
  `sensor_msgs/Image` message workflows, installation
  of OpenCV and `cv_bridge` are not required.
- Local host deployment is not supported for models involving
  `sensor_msgs/CompressedImage` message
  workflows.
- Bayer encoding is not supported.

## Version History

**Introduced in R2019b**

## Description

Extract image from ROS Image message

The Read Image block extracts an image from a
ROS `sensor_msgs/Image` or
`sensor_msgs/CompressedImage` message. You can select the ROS
message parameters of a topic active on a live ROS network or specify the message
parameters separately. The ROS messages are specified as a nonvirtual bus. Use the
Subscribe block output to receive a message from a ROS network and input
the message to the Read Image block.

**Note**

When reading ROS image messages from the network, the `Data`
property of the message can exceed the maximum array length set in Simulink®. To increase the maximum array length for all message types in the
model, from the **Prepare** section under
**Simulation** tab, select **ROS Toolbox**  > **Variable Size Messages**. Uncheck **Use default limits for this message type**
and then in the **Maximum length** column, increase the length
based on the number of pixels in the image.
