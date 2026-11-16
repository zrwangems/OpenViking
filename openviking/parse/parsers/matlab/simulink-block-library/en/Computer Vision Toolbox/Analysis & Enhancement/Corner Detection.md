---
type: simulink-block
title: 'Corner Detection'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'cornerdetection'
documentation_source_path: 'ref/cornerdetection.html'
language: en
---

# Corner Detection

## Ports

### Input

### **I** — Input image matrix of intensity values

Input image, specified as a matrix of intensity values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Loc** — Corner locations *M*-by-2 matrix

Corner locations, returned as an *M*-by-2 matrix of
[*x*
*y*] coordinates. *M* represents the number of
corners and is less than or equal to the **Maximum number of
corners** parameter.

#### Dependencies

To enable this port, set the **Output** parameter to one of these:

- `Corner location`
- `Corner location and metric matrix`

**Data Types:** `uint32`

### **Count** — Number of detected corners scalar

Number of detected corners, returned as a scalar.

#### Dependencies

To enable this port, set these block parameters:

- **Output**: `Corner location` |
  `Corner location and metric matrix`
- **Output variable size signal**:
  `off`

**Data Types:** `uint32`

### **Metric** — Corner metric values matrix

Corner metric values, returned as a matrix of intensity values. The returned
matrix is the same size as the input image.

#### Dependencies

To enable this port, set the **Output** parameter to one of these:

- `Corner location and metric matrix`
- `Metric matrix`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Method** — Corner detection method `Harris corner detection (Harris & Stephens)` (default) | `Minimum eigenvalue (Shi & Tomasi)` | `Local intensity comparison (Rosten & Drummond)`

Specify the corner detection method as `Harris corner detection
(Harris & Stephens)`, `Minimum eigenvalue (Shi &
Tomasi)`, or `Local intensity comparison (Rosten &
Drummond)`.

To get the most accurate results, use `Minimum eigenvalue (Shi &
Tomasi)`. For the fastest computation, use `Local intensity
comparison (Rosten & Drummond)`. For a balance between accuracy and
computation speed, use `Harris corner detection (Harris &
Stephens)`. For more information on each method, see the Algorithms section.

### **Sensitivity factor (0<k<0.25)** — Sensitivity factor 0.04 (default) | scalar

Specify the sensitivity factor, *k*. As *k*
decreases, the likelihood that the algorithm can detect sharp corners
increases.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** parameter to
`Harris corner detection (Harris & Stephens)`.

### **Coefficients for separable smoothing filter** — Filter coefficients fspecial('gaussian', [1 5], 1.5) (default) | vector

Specify a vector of filter coefficients for the smoothing filter.

#### Dependencies

To enable this parameter, set the **Method** parameter to one
of these:

- `Harris corner detection (Harris &
  Stephens)`
- `Minimum eigenvalue (Shi & Tomasi)`

### **Intensity comparison threshold** — Intensity threshold 0.1 (default) | scalar

Specify the intensity threshold value used to find valid surrounding
pixels.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** parameter to
`Local intensity comparison (Rosten &
Drummond)`.

### **Maximum angle to be considered a corner (in degrees)** — Maximum corner angle 157.5 (default) | scalar

Specify the maximum corner angle.

**Tunable:** Yes

#### Dependencies

- To enable this parameter, set the **Method** parameter to
  `Local intensity comparison (Rosten &
  Drummond)`.
- This parameter is tunable for simulation only.

### **Output** — Block output `Corner location` (default) | `Corner location and metric matrix` | `Metric matrix`

Specify the block output as `Corner location`,
`Corner location and metric matrix`, and
`Metric matrix`.

Set this parameter to `Corner location` or
`Corner location and metric matrix` to expose the
**Maximum number of corners**, **Minimum metric value that
indicates a corner**, and **Neighborhood size (suppress region
around detected corners)** parameters.

### **Maximum number of corners** — Maximum number of corners 200 (default) | integer

Specify the maximum number of corners you want the block to find.

#### Dependencies

To enable this parameter, set the **Output** parameter to one
of these:

- `Corner location`
- `Corner location and metric matrix`

### **Minimum metric value that indicates a corner** — Minimum corner metric 0.0005 (default) | scalar

Specify the minimum corner metric value.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Output** parameter to one
of these:

- `Corner location`
- `Corner location and metric matrix`

### **Neighborhood size** — Neighborhood size [11 11] (default) | 2-element vector

Specify the neighborhood size as a two-element vector of positive odd integers,
[*row*, *column*]. The block uses this parameter
to suppress the region around a valid corner point with the largest corner metric
value.

#### Dependencies

To enable this parameter, set the **Output** parameter to one
of these:

- `Corner location`
- `Corner location and metric matrix`

### **Output variable size signal** — Variable size signal `on` (default) | `off`

Select this parameter to output a variable size signal.

#### Dependencies

To enable this parameter, set the **Output** parameter to one
of these:

- `Corner location`
- `Corner location and metric matrix`

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Data type override `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

## Libraries

Computer Vision Toolbox / Analysis & Enhancement

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a This data type is not supported for the Local Intensity Comparison method. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2007b**

## Description

Calculate corner metric matrix and find corners in images

The Corner Detection block finds corners in an image by using the Harris
corner detection (by Harris and Stephens), minimum eigenvalue (by Shi and Tomasi), or local
intensity comparison (based on the *Accelerated Segment Test, (FAST)* method
by Rosten and Drummond) method. The block finds the corners in the image based on the pixels
that have the largest corner metric values.
