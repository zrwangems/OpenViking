---
type: simulink-block
title: 'Read Point Cloud'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Access in Simulink'
documentation_page: 'readpointcloudros1'
documentation_source_path: 'ref/readpointcloudros1.html'
language: en
---

# Read Point Cloud

## Ports

### Input

### **Msg** — ROS `sensor_msgs/PointCloud2` message nonvirtual bus

ROS `sensor_msgs/PointCloud2` message, specified as
a nonvirtual bus. You can use the Subscribe block to get a
message from the ROS network.

**Data Types:** `bus`
### Output

### **XYZ** — XYZ coordinates matrix | array

*x-*, *y-*, and
*z-* coordinates of each point in the point cloud
data, returned as either an *N*-by-3 matrix or
*h*-by-*w*-by-3 array.
*N* is the number of points in the point cloud.
*h* and *w* are the height and
width of the image, in pixels. To get the *x-*,
*y-*, and *z-* coordinates as an
array, select the **Preserve point cloud
structure** parameter.

**Data Types:** `single`

### **RGB** — RGB values for each point matrix | array

RGB values for each point of the point cloud data, output as either an
*N*-by-3 matrix or
*h*-by-*w*-by-3 array.
*N* is the number of points in the point cloud.
*h* and *w* are the height and
width of the image in pixels. The RGB values specify the red, green, and
blue color intensities in the range of `[0,1]`.To
return the RGB values as an array, select the **Preserve point cloud structure** parameter.

**Data Types:** `double`

### **Intensity** — Intensity values for each point array | matrix

Intensity value for each point of the point cloud data, returned as
either an array or a *h*-by-*w*
matrix. *h* and *w* are the height and
width of the image in pixels. To return the intensity values as a
matrix, select the **Preserve point cloud
structure** parameter.

**Data Types:** `single`

### **ErrorCode** — Error code for image conversion scalar

Error code for image conversion, returned as a scalar. The error code
values are:

- `0` – Successfully converted the point
  cloud message.
- `1` – The dimensions of the incoming
  point cloud exceed the limits set in the **Maximum point cloud size**
  parameter.
- `2` – One of the variable-length arrays
  in the incoming message was truncated. For more information
  on increasing the maximum length of the array, see Manage Array Sizes for ROS Messages in Simulink.
- `3` – The `X`,
  `Y`, or `Z` field of
  the point cloud message is missing.
- `4` – The point cloud does
  not contain any RGB color data. This error only occurs if
  you enable the **Show RGB output
  port** parameter.
- `5` – The point cloud does
  not contain any intensity data. This error only occurs if
  you enable the **Show Intensity output
  port** parameter.

For certain error codes, the block truncates the data or populates
with `NaN` values where appropriate.

**Data Types:** `uint8`

## Parameters

### **Maximum point cloud size** — Maximum point cloud image size `[480 640]` (default) | two-element vector

Maximum point cloud image size, specified as a two-element `[height width]` vector.

Select **Configure using ROS** to set this parameter
automatically using an active topic on a ROS network. You must be connected
to the ROS network.

### **Preserve point cloud structure** — Point cloud data output shape preservation `off` (default) | `on`

When this parameter is selected, the block preserves the point cloud data
output shape for **XYZ**, **RGB**, and **Intensity** outputs.
Each output corresponds to the resolution of the original image. The
**XYZ** and **RGB** outputs become multidimensional arrays, and the
**Intensity** output becomes a
matrix.

### **Show RGB output port** — `RGB` port toggle `off` (default) | `on`

Select this parameter to enable the **RGB**
port. If you enable this parameter, the message must contain RGB data or the
block returns an error code.

### **Show Intensity output port** — `Intensity` port toggle `off` (default) | `on`

Select this parameter to enable the **Intensity** port. If you enable this parameter, the message
must contain intensity data or the block returns an error code.

### **Show ErrorCode output port** — `ErrorCode` port toggle `on` (default) | `off`

Select this parameter to enable the **ErrorCode** port and monitor errors.

### **Output variable-size signals** — Variable-size signal output toggle `off` (default) | `on`

Toggle whether to output a variable-size signal. Use variable-sized
signals only if you expect the image size to change over time. For more
information about variable-size signals, see Variable-Size Signal Basics (Simulink).

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Extract point cloud from ROS PointCloud2 message

The Read Point Cloud block extracts a point cloud from a ROS
`sensor_msgs/PointCloud2` message. You can select the ROS message
parameters of a topic active on a live ROS network or specify the message parameters
separately. The ROS messages are specified as a nonvirtual bus. Use the Subscribe block to receive a message from a ROS network and input the
message to the Read Point Cloud block.

**Note**

When reading ROS point cloud messages from the network, the
`Data` property of the message can exceed the maximum array
length set in Simulink®. To increase the maximum array length for all message types in the
model, from the **Prepare** section under
**Simulation** tab, select **ROS Toolbox**  > **Variable Size Messages**. Uncheck **Use default limits for this message type**
and then in the **Maximum length** column, increase the length
based on the number of points in the point cloud.
