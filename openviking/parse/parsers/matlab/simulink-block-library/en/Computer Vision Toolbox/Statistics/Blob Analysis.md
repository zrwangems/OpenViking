---
type: simulink-block
title: 'Blob Analysis'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'blobanalysis'
documentation_source_path: 'ref/blobanalysis.html'
language: en
---

# Blob Analysis

## Ports

### Input

### **BW** — Binary image vector | matrix

Binary image, specified as a vector or matrix

**Data Types:** `Boolean`
### Output

### **Area** — Number of pixels in labeled regions vector

Number of pixels in labeled regions, returned as a vector.

#### Dependencies

To enable this port, select the **Area** parameter.

**Data Types:** `int32`

### **Centroid** — Centroid coordinates *M*-by-2 matrix

*M*-by-2 matrix of *M* number of blobs.

The rows represent the coordinates of the centroid of each region, and
*M* represents the number of blobs.

For example, there are two blobs where the row and column coordinates of their
centroids are *x*1,
*y*1 and
*x*2,
*y*2. The block outputs:

[x1y1x2y2]

at the **Centroid** port.

#### Dependencies

To enable this port, select the **Centroid** parameter.

**Data Types:** `double` | `single` | `fixed point`

### **BBox** — Bounding box coordinates *M*-by-4 matrix

Bounding box coordinates, returned as an *M*-by-4 matrix of
*M* bounding boxes for blobs. Each row of the matrix defines a
bounding box as a four-element vector
[*x*,*y*,*width*,*height*]
in pixel coordinates. The rows represent the coordinates of each bounding box, where
*M* represents the number of blobs.

For example, there are two blobs, where *x* and
*y* define the location of the upper-left corner of the bounding
box, and *w* and *h* define the width and height of
the bounding box. The block outputs

[x1y1w1h1x2y2w2h2]

at the **BBox** port.

#### Dependencies

To enable this port, select the **Bounding Box**
parameter.

## Parameters

**Main Tab**

### **Area** — Number of pixels in labeled regions vector

Number of pixels in labeled regions, returned as a vector.

#### Dependencies

To enable this port, select the **Area** parameter.

### **Centroid** — Centroid coordinates *M*-by-2 matrix

*M*-by-2 matrix of *M* number of blobs.

The rows represent the coordinates of the centroid of each region, and
*M* represents the number of blobs.

For example, there are two blobs where the row and column coordinates of their
centroids are *x*1,
*y*1 and
*x*2,
*y*2. The block outputs:

[x1y1x2y2]

at the **Centroid** port.

#### Dependencies

To enable this port, select the **Centroid** parameter.

### **BBox** — Bounding box coordinates *M*-by-4 matrix

Bounding box coordinates, returned as an *M*-by-4 matrix of
*M* bounding boxes for blobs. Each row of the matrix defines a
bounding box as a four-element vector
[*x*,*y*,*width*,*height*]
in pixel coordinates. The rows represent the coordinates of each bounding box, where
*M* represents the number of blobs.

For example, there are two blobs, where *x* and
*y* define the location of the upper-left corner of the bounding box,
and *w* and *h* define the width and height of the
bounding box. The block outputs

[x1y1w1h1x2y2w2h2]

at the **BBox** port.

#### Dependencies

To enable this port, select the **Bounding Box**
parameter.

### **Major axis length** — Length of major axis of ellipses off (default) | on

Enables the **Major axis length** port. Select this check box to
output a vector that

- Represents the lengths of the major axes of ellipses
- Has the same normalized second central moments as the labeled regions

### **Minor axis length** — Length of minor axis of ellipses off (default) | on

Enables the **Minor axis length** port. Select this check box to
output a vector that

- Represents the lengths of the minor axes of ellipses
- Has the same normalized second central moments as the labeled regions

### **Orientation** — Orientation off (default) | on

Enables the **Orientation** port.

Select this check box to output a vector that represents the angles between the
major axes of the ellipses and the *x*-axis. The angle values are in
radians and range between: −π2 and π2 inclusive.

### **Eccentricity** — Eccentricity off (default) | on

Enables the **Eccentricity** port. Select this check box to output
a vector that represents the eccentricities of ellipses that have the same second
moments as the region.

### **Equivalent diameter squared** — Equivalent diameter squared off (default) | on

Enables the **Equivalent diameter squared** port. Select this check
box to output a vector that represents the equivalent diameters squared.

### **Extent** — Extent off (default) | on

Enables the **Extent** port. Select this check box to output a
vector that represents the results of dividing the areas of the blobs by the area of
their bounding boxes.

### **Perimeter** — Perimeter length off (default) | on

Enables the **Perimeter** port. Select this check box to output an
*N*-by-1 vector of the perimeter lengths, in pixels, of each blob,
where *N* is the number of blobs.

### **Statistics output data type** — Output data type double (default) | single | specify via Data Types tab

Specify the data type of the outputs as `double`,
`single`, or `Specify via Data Types
tab`.

### **Connectivity** — Number of labeled regions `8` (default) | `4`

Specify the number of labeled regions in each image.

Define which pixels connect to each other. If you want to connect pixels located on
the top, bottom, left, and right, select `4`. If you want to
connect pixels to other pixels on the top, bottom, left, right, and diagonally, select
`8`. For more information about this parameter, see the
Label block.

The **Connectivity** parameter also affects how the block
calculates the perimeter of a blob. For example, this figure illustrates how the block
calculates the perimeter when you set the **Connectivity** parameter to
`4`.

The block calculates the distance between the center of each pixel
(marked by the black dots) and estimates the perimeter to be 22.

The next figure illustrates how the block calculates the perimeter of a blob when
you set the **Connectivity** parameter to `8`.

The block takes a different path around the blob and estimates the
perimeter to be 18+22.

### **Output label matrix** — Output label matrix off (default) | on

Enable the **Label** port. Select this check box to output the
label matrix. The pixels equal to `0` represent the background. The
pixels equal to `1` represent the first object. The pixels equal to
`2` represent the second object, and so on.

**Blob Properties Tab**

### **Maximum number of blobs** — Maximum number of blobs scalar

Specify the maximum number of labeled regions in each input image. The block uses
this value to preallocate vectors and matrices to ensure that they are long enough to
hold the statistical values. The maximum number of blobs the block outputs depends on
both the value of this parameter and the size of the input image. The number of blobs
the block outputs may be limited by the input image size.

### **Warn if maximum number of blobs is exceeded** — Warn if maximum number of blobs is exceeded on (default) | off

Select this parameter to warn if maximum number of blobs is exceeded.

### **Output actual number of blobs** — Number of blobs off (default) | on

Enable the **Count** port. Select this parameter to output a scalar
value that represents the actual number of connected regions in each image.

### **Specify minimum blob area in pixels** — Minimum blob area in pixels `0` (default) | scalar

Select this parameter to specify the minimum blob area in pixels. The blob is
labeled if the number of pixels meets the minimum size specified.

**Tunable:** Yes

### **Specify maximum blob area in pixels** — Maximum blob area in pixels intmax('uint32') (default) | scalar

Select this parameter to specify the maximum blob area in pixels. The blob is
labeled if the number of pixels meets the maximum size specified. The maximum allowable
value is the maximum of the `uint32` data type.

**Tunable:** Yes

### **Exclude blobs touching image border** — Exclude blobs touching image border off (default) | on

Specify this parameter to exclude a labeled blob that contains at least one border
pixel.

### **Output blob statistics as a variable size signal** — Output blob statistics as a variable size signal off (default) | on

Specify this parameter to output blob statistics as a variable-size signal.

### **Fill empty spaces in output** — Fill empty spaces in output off (default) | on

Specify this parameter to fill empty spaces in the statistical vectors with the
values you specify in the **Fill values** parameter.

#### Dependencies

To enable this parameter, clear the **Output blob statistics as a variable
size signal** parameter.

### **Fill values** — Scalar used to fill empty spaces in output `-1` (default) | scalar | vector

Specify a scalar value to fill all the empty spaces in the statistical vectors. If
you enter a vector, it must have the same length as the number of selected statistics.
The block uses each vector element to fill a different statistics vector. If the empty
spaces do not affect your computation, you can clear the **Fill empty spaces in
outputs** parameter.

#### Dependencies

To enable this parameter, clear the **Output blob statistics as a variable
size signal** parameter.

**Data Types Tab**

To enable option on the **Data Types** tab, in the
**Main** tab, set the **Statistics output data type**
parameter to `Specify via Data Types tab`. For details on the
fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

## Libraries

Computer Vision Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `doubleb` | `fixed pointbc` | `integerb` | `singleb` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Generated code will be restricted to MATLAB host computers when you set the FFT implementation parameter to FFTW, or when the transform length is not a power of two.  b This data type is supported at the output port(s).  c Fixed-point data types are not supported at the Major Axis, Minor Axis, Orientation, and Eccentricity output ports. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Statistics for labeled regions

The Blob Analysis block calculates statistics for labeled regions in a binary image. The
block returns quantities such as the centroid, bounding box, label matrix, and blob count. The
Blob Analysis block supports input and output variable-size signals. You can also use the
Selector (Simulink) block from Simulink®, to select certain blobs based on their statistics.

For information on pixel and spatial coordinate system definitions, see Image Coordinate Systems and Coordinate Systems.
