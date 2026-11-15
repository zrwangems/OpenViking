---
type: simulink-block
title: 'Trace Boundary'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'traceboundary'
documentation_source_path: 'ref/traceboundary.html'
language: en
---

# Trace Boundary

## Ports

### Input

### **BW** — Input binary image matrix

Input binary image, specified as an *M*-by-*N*
matrix.

**Data Types:** `Boolean`

### **Start Pt** — Coordinate of boundary starting point two-element vector

Coordinate of the boundary starting point, specified as a two-element vector in
the form [*X*
*Y*].

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Pts** — Coordinates of boundary points *M*-by-2 matrix

Coordinates of the boundary points, returned as an *M*-by-2
matrix where each row represents a coordinate of a boundary pixel in the form
[*X*
*Y*]. *M* is the number of traced boundary pixels in
the output image. Value of *M* must be less than or equal to the
value specified by **Maximum number of boundary pixels**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Connectivity** — Type of pixel connectivity `8` (default) | `4`

Select these options to specify how the block defines which pixels are connected to
each other.

- `8` — Connect adjacent pixels in the horizontal,
  vertical, and diagonal directions.
- `4` — Connect adjacent pixels in only the horizontal
  and vertical directions.

For more information, see Connectivity.

### **Initial search direction** — Type of initial search direction `North` (default) | `East` | `South` | `West` | `Northeast` | ...

Specify the type of initial search direction to find the boundary pixel connected to
the starting pixel specified at **Start Pt** input port. These options
are dependent on the specified **Connectivity** parameter.

For **Connectivity** parameter set as `4`,
the block enables `North`, `East`,
`South`, and `West` search
directions. This figure illustrates the four possible initial search directions with
respect to the starting pixel.

Search direction with Connectivity set to 4

For **Connectivity** parameter set as `8`,
the block enables additional `Northeast`,
`Southeast`, `Southwest`, and
`Northwest` search directions. This figure illustrates the
eight possible initial search directions with respect to the starting pixel.

Search direction with Connectivity set to 8

### **Trace direction** — Boundary trace direction `Clockwise` (default) | `Counterclockwise`

Select the direction to trace the boundary as `Clockwise`
or `Counterclockwise`.

### **Maximum number of boundary pixels** — Maximum number of boundary pixels 500 (default) | scalar

Specify the maximum number of boundary pixels for the starting point as a scalar.
The number of rows at **Pts** output port must be less than or equal to
this value.

## Libraries

Computer Vision Toolbox / Analysis & Enhancement

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

## Description

Trace object boundaries in binary images

The Trace Boundary block traces object boundaries in binary images, where nonzero pixels
represent objects and zero valued pixels represent the background.
