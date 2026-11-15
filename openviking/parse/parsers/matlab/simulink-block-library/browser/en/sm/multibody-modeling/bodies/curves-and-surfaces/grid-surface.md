---
type: simulink-block
title: 'Grid Surface'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Curves and Surfaces'
documentation_page: 'gridsurface'
documentation_source_path: 'ref/gridsurface.html'
language: en
---

# Grid Surface

## Ports

### Frame

### **R** — Local reference frame frame

Grid surface reference frame. Connect this frame to another block to
specify the location and orientation of the grid surface.
### Geometry

### **G** — Geometry geometry

Geometry that represents the grid surface defined by this block. Connect this port to a
Spatial
Contact Force block to model contacts with supported
geometries.

## Parameters

### **X Grid Vector** — Coordinates in *x*-direction [0 1 2 3] `m` (default) | *1-by-m* vector

Coordinates in the *x*-direction of the grid surface, specified as a
real *1-by-m* vector. *m* must be greater
than 2, and the vector elements must be strictly monotonic and increasing.
This vector corresponds to the rows of the matrix specified in the
**Z Heights** parameter.

Illustration of the relationship between x grid vector and z height matrix

### **Y Grid Vector** — Coordinates in *y*-direction [0 1 2 3] `m` (default) | *1-by-n* vector

Coordinates in the *y*-direction of the grid surface, specified as a
real *1-by-n* vector. *n* must be greater
than 2, and the vector elements must be strictly monotonic and increasing.
This vector corresponds to the columns of the matrix specified in the
**Z Heights** parameter.

Illustration of the relationship between y grid vector and z height matrix

### **Z Heights** — Elevations of grid points [0 0 .5 .5; 0 0 .5 .5; 0 0 0 0; 0 0 0 0] `m` (default) | *m-by-n* matrix

Elevations of the grid points in the grid surface, specified as a real
*m-by-n* matrix. *m* and
*n* are the lengths of the vectors for the **X
Grid Vector** and **Y Grid Vector**
parameters.

### Graphic

### **Type** — Visual representation of grid surface `From Geometry` (default) | `None`

Visual representation of the grid surface. Set this parameter to `From
Geometry` to show the visual representation of the grid
surface. Set this parameter to `None` to hide
the grid surface in the model visualization.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify diffuse color and
opacity. Select `Advanced` to specify more
visual properties, such as **Specular Color**,
**Ambient Color**, **Emissive
Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to
`From Geometry`.

### **Diffuse Color** — Graphic color [0.5 0.5 0.5] (default) | three-element vector | four-element vector

Color of the graphic under direct white light, specified as an [R G B]
or [R G B A] vector on a 0–1 scale. An optional fourth element (A)
specifies the color opacity on a scale of 0–1. Omitting the opacity
element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry`.

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A
scalar of 0 corresponds to completely transparent, and a scalar of 1
corresponds to completely opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Highlight color [0.5 0.5 0.5 1.0] (default) | three-element vector | four-element vector

Color of the specular highlights, specified as an [R,G,B] or [R,G,B,A] vector on a 0–1
scale. The optional fourth element specifies the color opacity. Omitting
the opacity element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Shadow color [0.15 0.15 0.15 1.0] (default) | three-element vector | four-element vector

Color of the shadow areas in diffuse ambient light, specified as an [R,G,B] or [R,G,B,A]
vector on a 0–1 scale. The optional fourth element (A) specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | three-element vector | four-element vector

Graphic color due to self illumination, specified as an [R,G,B] or
[R,G,B,A] vector on a 0–1 scale. The optional fourth element (A)
specifies the color opacity. Omitting the opacity element is equivalent
to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar in the range of 1 to 128

Sharpness of the specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights.
Decrease the value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

## Libraries

Simscape / Multibody / Curves and Surfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Grid surface for contact modeling

The Grid Surface block creates a Cartesian grid surface that
you can use to model contact problems. You can model contacts between the grid surface
and various types of geometries. For the supported geometries, see Supported Geometries. In addition, the
Grid Surface block supports the Custom Tire Force and
Torque and Magic Formula Tire Force
and Torque blocks.

You must use the positive normal side of the grid surface for contact, which the positive
*z*-axis of the reference frame points to. Otherwise, the block
ejects the contacting part through the surface to the positive side.

Illustration of the positive normal side of a grid surface

The grid surface has a similar format to the grid generated by the `ndgrid` function in MATLAB®. To model a grid surface, use the X Grid Vector and Y Grid Vector parameters to specify
the coordinates in the *x* and *y* directions of the
grid surface, then use the Z Heights parameter to specify
the elevations of the grid points in the *z* direction. You can use the
block to create a surface that represents a square, rectangular, or non-uniform
grid.

Grid types

The image shows an illustration of a grid surface whose **Z Heights**
parameter is `[0 0 0.5 0.5; 0 0 0.5 0.5; 0 0 0 0; 0 0 0 0]`. The
columns of the matrix are along the *x-*axis, and the rows of the
matrix are along the *y-*axis.

Grid parameters

To create a grid surface using LiDAR data, you must convert the scattered data to gridded
data before using it in the Grid Surface block. To
convert the data, you can use a `scatteredInterpolant` object to create an
interpolant function by using the *x*, *y*, and
*z* values of the LiDAR data, create *x* and
*y* grid vectors that represent the domain of the grid, and then
use the grid vectors as the query points of the interpolant function to produce
*z* values for the grid surface. The produced *z*
values form a matrix in the `ndgrid` format that you can use to
specify the **Z Heights** parameter. You can also use the `griddata` function to produce *z* values for a grid
surface, but you need to transpose the output matrix to the `ndgrid`
format.

**Note**

For the best simulation performance, make the spacing in the *x*
and *y* grid vectors as large as possible while also being small
enough to represent the surface with sufficient accuracy. To change the spacing of
the grid vectors and compute the corresponding *z* values , use the
`griddedInterpolant` object or `interp2` function.

Generally, you need to clean the LiDAR data before converting it to gridded data, such as
removing outliers or *NaN* values. To clean the data, use the `isnan` and `isoutlier` functions.
