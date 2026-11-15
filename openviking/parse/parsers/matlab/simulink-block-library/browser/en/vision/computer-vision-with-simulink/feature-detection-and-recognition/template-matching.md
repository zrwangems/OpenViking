---
type: simulink-block
title: 'Template Matching'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'templatematching'
documentation_source_path: 'ref/templatematching.html'
language: en
---

# Template Matching

## Ports

### Input

### **I** — Image image

Input image to use with the template. The block does not pad the input data.
Therefore, it can only compute values for the match metrics between the input image
and the template, where the template is positioned such that it falls entirely on the
input image. A set of all such positions of the template is termed as the
*valid* region of the input image. The size of the valid region
is the difference between the sizes of the input and template images plus
one.

|  |  |
| --- | --- |
| sizevalid=sizeinput – sizetemplate+1 | **(1)** |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **T** — Template *M*-by-*N* matrix

Template, specified as an *M*-by-*N*
matrix

The Template Matching block does not pad the input data. Therefore,
it can only compute values for the match metrics between the input image and the
template, where the template is positioned such that it falls entirely on the input
image. A set of all such positions of the template is termed as the
*valid* region of the input image. The size of the valid region
is the difference between the sizes of the input and template images plus
one.

|  |  |
| --- | --- |
| sizevalid=sizeinput – sizetemplate+1 | **(2)** |

**Data Types:** `single` | `double` | `uint8` | `Boolean` | `fixed point`

### **ROI** — Region of interest four-element vector

Region of interest vector in the format
(*x*,*y*,*width*,*height*),
where (*x*,*y*) are one-based coordinates for the
upper-left corner of the region. The block outputs the best match location index
relative to the top left corner of the input image.

**Data Types:** `single` | `double` | `uint8` | `Boolean` | `fixed point`
### Output

### **Metric** — Match metric values matrix

Matrix of match metric values. The matrix of the match metrics always implements
single-step exhaustive window iteration. Therefore, the block computes the metric
values at every pixel.

#### Dependencies

When you set the **Output** parameter to `Metric
matrix`, the block outputs the valid image size.

**Data Types:** `single` | `double` | `uint8` | `Boolean` | `fixed point`

### **Loc** — Best match locations two-element vector

Best template match located at the one-based
(*x*,*y*) coordinates. When in the ROI processing
mode, the block treats the image around the ROI as an extension of the ROI subregion.
Therefore, it computes the best match locations true to the actual boundaries of the
ROI. The block outputs the best match coordinates, relative to the top-left corner of
the image. The one-based [x y] coordinates of the location correspond to the center of
the template. The following table shows how the block outputs the center coordinates
for odd and even templates:

| Odd number of pixels in template | Even number of pixels in template |
| --- | --- |
|  |  |

**Data Types:** `uint32`

### **NMetric** — Metric values in neighborhood of best match *N*-by-*N* matrix

Metric values in the neighborhood of the best match, returned as an
*N*-by-*N* matrix. *N*, specified
in the mask, must be an odd number. When you select **Best match
location** to return the matrix of metrics in a neighborhood around the
best match, an exhaustive loop computes all the metric values for the
*N*-by-*N* neighborhood. This output is
particularly useful for performing template matching with subpixel accuracy.

**Data Types:** `single` | `double` | `uint8` | `Boolean` | `fixed point`

### **NValid** — Valid neighborhood off | on

Enable to track the valid neighborhood region. The neighborhood matrix of metric
values is valid inside of the ROI. The block sets the **NValid**
output as follows:

- `1` — The neighborhood containing the best match is
  completely inside the region of interest.
- `0` — The neighborhood containing the best match is
  completely or partially outside of the region of interest.

#### Dependencies

This port appears when you enable the **Output NxN matrix of metric
values around best match** parameter.

**Data Types:** `Boolean`

### **ROIValid** — Valid region of interest off | on

Enable to track the valid region of interest. If the ROI lies partially outside
the valid image, the block only processes the intersection of the ROI and the valid
image. The block sets the **ROIValid** output as follows:

- `1` — The ROI lies completely inside the valid part of the
  input image.
- `0` — The ROI lies completely or partially outside of the
  valid part of the input image.

#### Dependencies

This port appears when you enable the **Output flag indicating if ROI is
valid** parameter.

**Data Types:** `Boolean`

## Parameters

**Main Tab**

### **Match metric** — Match metric `Sum of absolute differences` (default) | `Sum of squared differences` | `Maximum absolute difference`

Select match metric as one of:

- `Sum of absolute differences` (SAD)
- `Sum of squared differences` (SSD)
- `Maximum absolute difference` (MaxAD)

The block computes the match metric at each step of the iteration. Choose the match
metric that best suits your application. The block calculates the global optimum for the
best metric value. It uses the valid subregion of the input image intersected by the
ROI, if provided.

### **Output** — Match metric `Match metric` (default) | `Best match location`

Select the type of output as one of:

- `Match metric` — Output the match metric matrix. This
  option adds the **Metric** output port to the block.
- `Best match location` — Output the
  [*x*,*y*] coordinates for the location of the
  best match. This option adds the **Loc** output port to the
  block. It also makes the **Search method**, **Output NxN
  matrix of metric values around best match**, and **Enable ROI
  processing** parameters available.

  The **Output** parameter on the Data Types pane appears when
  you set the **Output** parameter on the **Main
  tab** to `Metric matrix` or if you set it to
  `Best match location` and you enable the
  **Output NxN matrix of metric values around best match**
  parameter.

### **Search method** — Search method `Exhaustive` (default) | `Three-step`

Specify the search method as either `Exhaustive` or
`Three-step`. The `Exhaustive`
search method is computationally intensive because it searches at every pixel location
of the image. However, this method provides a more precise result.

The `Three-step` search method is a fast search that uses a
neighborhood approach versus a search at every pixel. The search starts with a step size
equal to or slightly greater than half of the maximum search range and then employs the
following steps:

1. The block compares nine search points in each step. There is a central point
   and eight search points located on the search area boundary.
2. The block decrements the step size by one, after each step, ending the search
   with a step size of one pixel.
3. At each new step, the block moves the search center to the best matching point
   resulting from the previous step. The number one blue circles in the figure below
   represent a search with a starting step size of three. The number two green
   circles represent the next search, with step size of two, centered around the best
   match found from the previous search. Finally, the number three orange circles
   represent the final search, with step size of one, centered around the previous
   best match.

#### Dependencies

This parameter appears when you set the **Output** parameter to
`Best match location`.

### **Output NxN matrix of metric values around best match** — Output *N*-by-*N* matrix on (default) | off

Enable to add the **NMetric** and **NValid**
ports.

#### Dependencies

This parameter appears when you set the **Output** parameter to
`Best match location`.

### **N** — Size of output matrix `3` (default) | integer

Size of output matrix. This value determines the size of the
*N*-by-*N* output matrix centered around the best
match location index. *N* must be an odd number.

#### Dependencies

This parameter appears when you enable the **Output NxN matrix of metric
values around best match** parameter.

### **Enable ROI processing** — Enable ROI processing on (default) | off

Enable ROI processing.

#### Dependencies

- This parameter appears when you set the **Output** parameter
  to `Best match location`.
- When you enable this parameter, the block adds the **ROI**
  input port, and the **Output flag indicating if ROI is valid**
  parameter appears.

### **Output flag indicating if ROI is valid** — Valid ROI off (default) | on

Enable to add the **ROIValid** port.

#### Dependencies

This parameter appears when you enable the **Enable ROI
processing** parameter.

**Data Types Tab**

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

## Libraries

Computer Vision Toolbox / Analysis & Enhancement

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2009b**

## Description

Locate a template in an image

The Template Matching block finds the best match of a template within an
input image. The block computes match metric values by shifting a template over a region of
interest or the entire image, and then finds the best match location.

The block outputs either the match metric values or the one-based
(*x*,*y*) coordinates of the best template match.
Optionally the block can output an *N*-by-*N* matrix of the
match metric values centered around the best match location.
