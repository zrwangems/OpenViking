---
type: simulink-block
title: 'Point Cloud'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Curves and Surfaces'
documentation_page: 'pointcloud'
documentation_source_path: 'ref/pointcloud.html'
language: en
---

# Point Cloud

## Ports

### Frame

### **R** — Local reference frame frame

Point cloud reference frame. To specify the location and orientation
of the point cloud, connect this frame to another block.
### Geometry

### **G** — Geometry frame frame

Geometry frame that represents the points defined by this block. To model contacts on
the points, connect this port to a Spatial
Contact Force or a Planar Contact
Force block.

## Parameters

### **Coordinates Matrix** — Coordinates of points [0 0 0 ] `m` (default) | *N*-by-2 matrix | *N*-by-3 matrix

Coordinates of the points, specified as an *N*-by-2 or an
*N*-by-3 matrix.

- To create a 2-D point cloud, use an *N*-by-2
  matrix that specifies the *x* and
  *y* Cartesian coordinates of each point
  with respect to the local reference frame.
- To create a 3-D point cloud, use an *N*-by-3
  matrix that specifies the *x*,
  *y*, and *z* Cartesian
  coordinates of each point with respect to the local reference
  frame.

When modeling contacts, use the Planar Contact
Force block for 2-D point clouds and the
Spatial Contact Force block for 3-D point
clouds.

**Data Types:** `double`

### Graphic

### **Type** — Graphic to use in visualization of point cloud `Marker Cloud` (default) | `None`

Graphic used to visualize the point cloud. To eliminate the point cloud from the model
visualization, set this parameter to
`None`.

### **Sphere Radius** — Marker radius 1e-2 `m` (default) | positive scalar

Radius of the marker for each point of the point cloud.

#### Dependencies

To enable this parameter, set **Type** to
`Marker Cloud`.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify diffuse color and
opacity. Select `Advanced` to specify more
visual properties, such as **Specular Color**,
**Ambient Color**, **Emissive
Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to
`Marker Cloud`.

### **Diffuse Color** — Graphic color [0.5 0.5 0.5] (default) | three-element vector | four-element vector

Color of the graphic under direct white light, specified as an [R G B] or [R G B A]
vector on a 0–1 scale. The optional fourth element (A) specifies the
color opacity on a scale of 0–1. Omitting the opacity element is
equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set **Type** to
`Marker Cloud`.

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A
scalar of 0 corresponds to completely transparent, and a scalar of 1
corresponds to completely opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Marker
   Cloud`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Highlight color [0.5 0.5 0.5 1.0] (default) | three-element vector | four-element vector

Color of specular highlights, specified as an [R,G,B] or [R,G,B,A]
vector on a 0–1 scale. The optional fourth element specifies the color
opacity. Omitting the opacity element is equivalent to specifying a
value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Marker
   Cloud`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Shadow color [0.15 0.15 0.15 1.0] (default) | three-element vector | four-element vector

Color of shadow areas in diffuse ambient light, specified as an
[R,G,B] or [R,G,B,A] vector on a 0–1 scale. The optional fourth element
(A) specifies the color opacity. Omitting the opacity element is
equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Marker
   Cloud`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | three-element vector | four-element vector

Graphic color due to self illumination, specified as an [R,G,B] or
[R,G,B,A] vector on a 0–1 scale. The optional fourth element (A)
specifies the color opacity. Omitting the opacity element is equivalent
to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Marker
   Cloud`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar in the range of 0 to 128

Sharpness of specular light reflections, specified as a scalar number on a 0–128 scale.
This parameter increases the shininess value for smaller but sharper
highlights. Decrease the value for larger but smoother
highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Marker
   Cloud`
2. **Visual Properties** to
   `Advanced`

## Libraries

Simscape / Multibody / Curves and Surfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Point cloud geometry

The Point Cloud block creates a set of points in space. Each
point has a rigid offset with respect to the reference frame of the Point
Cloud block. You can use a Point
Cloud block to approximate a geometry, such as a body with concave
shape, for contacts. When modeling certain sustained and distributed contact problems,
the Spatial Contact
Force block might perform better with a Point
Cloud block than with a geometry block, such as Brick
Solid or File Solid. This image
demonstrates how to use a point cloud to approximate the bottom of a robot foot.

Point Cloud Example

When modeling contacts for a point cloud, the Spatial Contact
Force and Planar Contact Force blocks
treat a point cloud as an aggregation of *N*-point geometries and
applies contact forces to each point independently. Each contact force is based on the
penetration and velocity of the individual point of the cloud.

You can create a 2-D or 3-D point cloud by using an *N*-by-2 or
*N*-by-3 matrix. Each row of the matrix specifies the Cartesian
coordinates of a point with respect to the reference frame of the Point
Cloud block. An error occurs if the matrix has any repeated
rows.

**Tip**

You can use the `unique` function to remove repeated
rows from an input matrix.
