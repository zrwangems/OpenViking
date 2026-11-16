---
type: simulink-block
title: 'Hough Transform'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'houghtransform'
documentation_source_path: 'ref/houghtransform.html'
language: en
---

# Hough Transform

## Ports

### Input

### **BW** — Binary image matrix

Binary image, specified as a matrix of `Boolean` values.

**Data Types:** `Boolean`
### Output

### **Hough** — Parameter space matrix matrix

Parameter space matrix, returned as a numeric matrix. The values in the parameter
space matrix are in the (*rho, theta*) space.

**Data Types:** `single` | `double` | `fixed point`

### **Theta** — Theta values vector

Theta values, returned as a numeric vector. Each element represents the rotation
angle of the corresponding line, in radians.

#### Dependencies

To enable this port, you must select the **Output theta and rho
values** parameter.

**Data Types:** `single` | `double` | `fixed point`

### **Rho** — Rho values vector

Rho values, returned as a numeric vector. Each element represents the distance of
the corresponding line from the top-left point of the image.

#### Dependencies

To enable this port, you must select the **Output theta and rho
values** parameter.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### Main

### **Theta resolution (radians)** — Theta resolution `pi/180` (default) | positive scalar

Specify the spacing of the Hough transform bins along the
*theta*-axis. This value must be less than
`pi/2`.

### **Rho resolution (pixels)** — Rho resolution `1` (default) | positive scalar

Specify the spacing of the Hough transform bins along the
*rho*-axis.

### **Output theta and rho values** — Enable Theta and Rho output ports `off` (default) | `on`

Select this parameter to enable the **Theta** and
**Rho** output ports. The block outputs the
*theta*-axis and *rho*-axis vectors,
respectively, at these ports.

### **Output data type** — Output data type `double` (default) | `single` | `Specify via Fixed-point tab`

Specify the data type of your output signal. If you select
`double` or `single`, all the outputs are of the
specified data type. If you select `Specify via Fixed-point tab`, you
can specify the word length of each output in the **Data
Types** tab.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

## Libraries

Computer Vision Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `doublea` | `fixed point` | `integer` | `singlea` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a This data type is supported at the output port(s). | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Find lines in images

Use the Hough Transform block to find straight lines in an image. The block outputs the
Hough space matrix and, optionally, the *rho*-axis and
*theta*-axis vectors. Peak values in the matrix represent potential
straight lines in the input image. You can use the output of the Hough
Transform block to find straight lines in the image by using the Hough
Lines block. Alternatively, you can use a custom algorithm to identify potential
straight lines by locating peaks in the Hough space matrix.
