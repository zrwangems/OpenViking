---
type: simulink-block
title: 'Find Local Maxima'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'findlocalmaxima'
documentation_source_path: 'ref/findlocalmaxima.html'
language: en
---

# Find Local Maxima

## Ports

### Input

### **I** — Input *M*-by-*N* matrix

Input, specified as the *M*-by-*N* matrix in
which you want to detect the local maxima. If the input is a Hough matrix output from
the Hough Transform block, select the **Input is Hough matrix spanning full
theta range** parameter that renames this port as
**Hough**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Th** — Threshold for detecting local maxima scalar

Threshold for the detecting local maxima, specified as a scalar.

#### Dependencies

To enable this port, set the **Source of threshold value**
parameter to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Idx** — Coordinates of local maxima *P*-by-2 matrix

Coordinates of the local maxima, returned as a *P*-by-2 matrix of
one-based [*x*
*y*] coordinates. *P* represents the number of local
maxima.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32`

### **Count** — Number of local maxima scalar

Number of local maxima, returned as a scalar.

#### Dependencies

To enable this port, clear the check box for the **Output variable size
signal** parameter.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32`

## Parameters

### **Maximum number of local maxima** — Maximum number of local maxima to detect 2 (default) | positive integer

Specify the maximum number of local maxima to detect in the input matrix. The value
must be a positive integer greater than 0.

### **Neighborhood size** — Size of neighborhood region [`5 7`] (default) | two-element vector

Specify the size of the neighborhood region as a two-element vector in the form
`[r
c]`. The vector specifies the window size
*r*×*c*, within which the block determines the local
maxima. The window size must be greater than or equal to 1×1.

### **Source of threshold value** — Source to enter the threshold value `Specify via dialog` (default) | `Input port`

Specify the source for entering the threshold value. When you select the
`Input port`, the block enables the **Th**
port. When you select the `Specify via dialog`, the block
enables the **Threshold** parameter.

### **Threshold** — Threshold for detecting local maxima 10 (default) | scalar

Specify a scalar value that represents the threshold for detecting the local maxima.

#### Dependencies

To enable this parameter, set the **Source of threshold value**
parameter to `Specify via dialog`.

### **Input is Hough matrix spanning full theta range** — Whether input is a Hough matrix off (default) | on

Select the parameter, if the input to this block is the Hough matrix output from the
Hough Transform block. The Find Local
Maxima block assumes that the input is a Hough matrix that is antisymmetric
about the rho axis, with values of theta from -pi/2 to pi/2 radians. As a result, if the
local maximum is near the boundary and its neighborhood region is outside the Hough
matrix, the block detects only one local maximum. The block ignores the corresponding
antisymmetric maximum.

### **Index output data type** — Data type for coordinates of local maximums `uint32` (default) | `double` | `single` | `uint8` | `uint16`

Specify the data type for the coordinates of local maximums returned at the output
port **Idx**.

### **Output variable size signal** — Support input signals of varying length on (default) | off

Specify if the model supports input signals of varying length.

### **Count output data type** — Data type for number of local maximums `uint32` (default) | `double` | `single` | `uint8` | `uint16`

Specify the data type for the number of local maximums returned at the output port
**Count**.

#### Dependencies

To enable this parameter, clear the **Output variable size
signal** parameter.

## Libraries

Computer Vision Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Find local maxima in matrices

The Find Local Maxima block finds the local maxima in a given input matrix.
The block finds the local maxima of values within a region specified by the neighborhood size.
The block compares the values in the search region to a user-specified threshold and
identifies a value that is greater than or equal to the threshold as the local maximum. After
finding the local maximum, the block sets all the matrix values in the neighborhood, including
the maximum value, to zero. This step ensures that subsequent searches do not include this
maximum. The process repeats until the block either finds all valid maxima or the specified
number of local maxima.

The threshold and the neighborhood size must be chosen such that the block detects only
the true local maxima and eliminates false peaks.

The input to this block can also be a Hough matrix generated from the Hough
Transform block. The Find Local Maxima block outputs the one-based
[*x*
*y*] coordinates of the detected local maxima. The data sent to all input
ports must be the same data type.
