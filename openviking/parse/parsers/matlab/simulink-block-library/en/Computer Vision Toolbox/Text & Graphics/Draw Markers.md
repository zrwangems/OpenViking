---
type: simulink-block
title: 'Draw Markers'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'drawmarkers'
documentation_source_path: 'ref/drawmarkers.html'
language: en
---

# Draw Markers

## Ports

### Input

### **Image** — Input Image matrix | array

Specify the input image as either an *M*-by-*N*
matrix of intensity values or an
*M*-by-*N*-by-*P* array of color
values with *P* color planes.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — Red color component of image matrix

Specify the red color component of the input RGB image as an
*M*-by-*N* matrix. The **R**,
**G**, and **B** ports must have the same
dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — Green color component of image matrix

Specify the green color component of the input RGB image as an
*M*-by-*N* matrix. The **R**,
**G**, and **B** ports must have the same
dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — Blue color component of image matrix

Specify the blue color component of the input RGB image as an
*M*-by-*N* matrix. The **R**,
**G**, and **B** ports must have the same
dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Pts** — Marker coordinates vector | matrix

Specify the coordinates of markers as one of these options:

- Single marker — Two-element vector that specifies the *x*-
  and *y*- coordinates for the center of the marker.
- Multiple markers — *K*-by-2 matrix. *K* is
  the number of markers. Each row of the matrix specifies the
  *x*- and *y*- coordinates for the center of a
  marker.

**Note**

The block does not support single-precision or double-precision floating-point
data types for this parameter unless the input image is also floating point.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Clr** — Marker color scalar | vector | matrix

Specify the color values for the markers. Use this table to determine the type of
value to input at this port.

| **Type of Input Image** | Same Color for All Markers | Different Color for Each Marker |
| --- | --- | --- |
| Intensity image | scalar value | *K*-element vector. *K* is the number of markers. |
| Color image | *P*-element vector. *P* is the number of color planes. | *K*-by-*P* matrix. *P* is the number of color planes and *K* is the number of markers. |

#### Dependencies

To enable this port, use one of these options:

- The **Marker shape** parameter is set to
  `X-mark`, `Plus`, or
  `Star`, or the **Filled**
  parameter is cleared — Set the **Border color source**
  parameter to `Input port`.
- The **Marker shape** parameter is set to
  `Circle` or `Square` and
  the **Filled** parameter is selected — Set the **Fill
  color source** parameter to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **ROI** — Region of interest vector

Specify a rectangular region of interest (ROI) as a four-element vector of form
[*x*
*y*
*width*
*height*]. The *x* and *y* elements
are the coordinates of the top-left corner of the ROI.

#### Dependencies

To enable this port, set the **Draw markers in** parameter to
`Specify region of interest via port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output image matrix | array

Output image, returned as an *M*-by-*N* matrix
of intensity values or an
*M*-by-*N*-by-*P* array of color
values. *P* is the number of color planes in the output image. The
output image has the same size and data type as the input image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — Red color component of output image matrix

Red color component of the output RGB image, returned as an
*M*-by-*N* matrix. The red color component of the
output image has the same dimensions and data type as the red color component of the
input image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — Green color component of output image matrix

Green color component of the output RGB image, returned as an
*M*-by-*N* matrix. The green color component of
the output image has the same dimensions and data type as the green color component of
the input image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — Blue color component of output image matrix

Blue color component of the output RGB image, returned as an
*M*-by-*N* matrix. The blue color component of the
output image has the same dimensions and data type as the blue color component of the
input image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Main**

### **Marker shape** — Shape of marker `Circle` (default) | `X-mark` | `Plus` | `Star` | `Square`

Specify the shape of the marker to draw. You can render the
`Circle` and`Square` markers as
outlines or as filled shapes.

### **Marker size** — Size of marker `3` (default) | positive integer

Specify the size of the marker as a positive integer, *M*, that
defines a square area, with sides of length 2*M*+1, into which the
marker fits.

### **Filled** — Filled marker `off` (default) | `on`

Select this parameter to fill the marker with the specified intensity value or
color.

#### Dependencies

To enable this parameter, set the **Marker shape** parameter to
`Circle` or `Square`.

### **Border color source** — Color source of marker border `Specify via dialog` (default) | `Input port`

Specify the source of the color for the border of the marker as one of these options:

- `Specify via dialog` — Use the **Border
  color** parameter to specify a color for the border of the
  marker.
- `Input port` — Use the **Clr**
  input port to specify a color for the border of the marker.

#### Dependencies

To enable this parameter, clear the **Filled** parameter or set
the **Marker shape**  parameter to
`X-mark`, `Plus`, or
`Star`.

### **Border color** — Color value of marker `Black` (default) | `White` | `User-specified value`

Specify the color value for the border of the marker as
`Black`, `White`, or
`User-specified value`.

#### Dependencies

To enable this parameter, clear the **Filled** parameter and
set the **Border color source** parameter to `Specify
via dialog`.

### **Fill color source** — Color source of filled marker `Specify via dialog` (default) | `Input port`

Specify the source of the color with which to fill the marker as one of these options:

- `Specify via dialog` — Use the **Fill
  color** parameter to specify a color with which to fill the
  marker.
- `Input port` — Use the **Clr**
  input port to specify a color with which to fill the marker.

#### Dependencies

To enable this parameter, set the **Marker shape** parameter to
`Circle` or `Square` and select
the **Filled** parameter.

### **Fill color** — Color value of filled marker `Black` (default) | `White` | `User-specified value`

Specify the color value with which to fill the marker as
`Black`, `White`, or
`User-specified value`.

#### Dependencies

To enable this parameter, set the **Marker shape** parameter to
`Circle` or `Square`, select the
**Filled** parameter, and set the **Fill color
source** parameter to `Specify via
dialog`.

### **Opacity factor (between 0 and 1)** — Opacity factor `0.6` (default) | scalar in range [`0`, `1`] | *K*-element vector

Specify the opacity factor for the marker in the range [`0`,
`1`], where `0` is completely transparent and
`1` is completely opaque. Specify this parameter as one of these options:

- Scalar — Apply the specified opacity factor to all markers.
- *K*-element Vector — Apply a different opacity factor to
  each marker. *K* is the number of markers.

#### Dependencies

To enable this parameter, set the **Marker shape** parameter to
`Circle` or `Square` and select
the **Filled** parameter.

### **Color value(s)** — User-specified color values `[200 255 100]` (default) | scalar | *P*-element vector | *K*-by-*P* matrix

Specify the color values for the markers. Use this table to determine the type of
value to enter for this parameter.

| **Type of Input Image** | Same Color for All Markers | Different Color for Each Marker |
| --- | --- | --- |
| Intensity image | scalar value | *K*-element vector. *K* is the number of markers. |
| Color image | *P*-element vector. *P* is the number of color planes. | *K*-by-*P* matrix. *P* is the number of color planes and *K* is the number of markers. |

#### Dependencies

To enable this parameter, use one of these options:

- The **Marker shape** parameter is set to
  `X-mark`, `Plus`, or
  `Star`, or the **Filled**
  parameter is cleared — Set the **Border color source**
  parameter to `Specify via dialog` and the
  **Border color** parameter to `User-specified
  value`.
- The **Marker shape** parameter is set to
  `Circle` or `Square` and
  the **Filled** parameter is selected — Set the **Fill
  color source** parameter to `Specify via
  dialog` and the **Fill color** parameter to
  `User-specified value`.

### **Draw Markers in** — Area for markers `Entire image` (default) | `Specify region of interest via port`

Specify where to draw the markers. By default, you can draw markers in the entire
image. To specify markers within a rectangular ROI, set this parameter to
`Specify region of interest via port`, and specify a
four-element vector of the form [*x*
*y*
*width*
*height*] to the **ROI** input port.

### **Use antialiasing** — Smoothing algorithm `off` (default) | `on`

Select this parameter to perform a smoothing algorithm on the
`Circle`, `X-mark`, or
`Star` marker shapes.

#### Dependencies

To enable this parameter, set the **Marker shape** parameter to
`Circle`, `X-mark`, or
`Star`.

### **Image signal** — Port configuration for RGB image `One multidimensional signal` (default) | `Separate color signals`

Specify how to input and output an RGB color image.

- `One multidimensional signal` — The block accepts
  input using only the **Image** port and returns the output
  using only the **Port\_1** port.
- `Separate color signals` — The block accepts and
  returns the color image using three separate color channels, divided across the
  **R**, **G**, and **B**
  input and output ports.

### **Data Types**

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

## Libraries

Computer Vision Toolbox / Text & Graphics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Draw markers on image

The Draw Markers block draws markers on an image or video frame by overwriting pixel
values in the input image. This embeds the markers in the output image. The block supports
five types of markers: `Circle`, `X-mark`,
`Plus`, `Star`, and
`Square`.

The block uses Bresenham's circle drawing algorithm to draw circles and Bresenham's line
drawing algorithm to draw all other markers.
