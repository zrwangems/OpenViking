---
type: simulink-block
title: 'ROS Write Point Cloud, ROS 2 Write Point Cloud'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'writepointcloudblock'
documentation_source_path: 'ref/writepointcloudblock.html'
language: en
---

# ROS Write Point Cloud, ROS 2 Write Point Cloud

## Ports

### Input

### **XYZ** — XYZ coordinates matrix | array

*x-*, *y-*, and *z-*
coordinates of each point in the point cloud data, specified as either an
*N*-by-3 matrix or
*h*-by-*w*-by-3 array. *N* is the
number of points in the point cloud. *h* and *w* are
the height and width of the image, in pixels.

**Data Types:** `single`

### **RGB** — RGB values for each point matrix | array

RGB values for each point of the point cloud data, specified as either an
*N*-by-3 matrix or
*h*-by-*w*-by-3 array. *N* is the
number of points in the point cloud. *h* and *w* are
the height and width of the image in pixels. The RGB values specify the red, green,
and blue color intensities in the range of `[0,1]`.

#### Dependencies

The selected color field must support rgb values.

**Data Types:** `double`

### **Alpha** — Alpha channel for input image *N*-by-1 vector | *h*-by-*w* matrix

Alpha channel for image, specified as an *N*-by-1 vector or
*h*-by-*w* matrix. Each element has a value in the
range `[0,1]` that indicates the opacity of the corresponding pixel,
with a value of `0` being completely transparent.

#### Dependencies

The selected color field must support alpha channel.

**Data Types:** `double`

### **Intensity** — Intensity values for each point matrix | array

Intensity values for each point in the point cloud data, specified as either an
*N*-by-3 matrix or
*h*-by-*w*-by-3 array. *N* is the
number of points in the point cloud. *h* and *w* are
the height and width of the image, in pixels.

#### Dependencies

You must select the **Write to Intensity Field**
parameter.

**Data Types:** `single` | `double`
### Output

### **Msg** — ROS or ROS 2 point cloud message nonvirtual bus

ROS or ROS 2 point cloud message, returned as a nonvirtual bus. You can use the
ROS Publish or ROS 2 Publish block
to publish the message to an active ROS or ROS 2 network respectively.

**Data Types:** `bus`

## Parameters

### **Select color field** — Color field for the point cloud image `none` (default) | `rgb` | `rgba`

Color field of the point cloud image, specified as one of the supported options.
Choose the appropriate option to specify color and alpha values corresponding to the
point cloud image.

### **Write to Intensity field** — Write intensity values off (default) | on

Select whether to write intensity values to the output message.

## Libraries

ROS Toolbox / ROS ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Write point cloud data to a ROS or ROS 2 message

The Write Point Cloud block writes point cloud data to a ROS or ROS 2 point
cloud message. You can specify the appropriate color encoding for the point cloud image and
write the corresponding color and alpha values to the output message. You can also write
intensity values to the output message. Use the ROS Publish or ROS 2 Publish block to
publish the output image message to an active topic on the network.
