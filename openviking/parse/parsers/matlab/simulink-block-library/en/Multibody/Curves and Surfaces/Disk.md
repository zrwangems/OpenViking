---
type: simulink-block
title: 'Disk'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'disk'
documentation_source_path: 'ref/disk.html'
language: en
---

# Disk

## Ports
```yaml
ports:
- name: R
  summary: Reference frame frame
  direction: unspecified
- name: G
  summary: Geometry geometry
  direction: unspecified
```

### Frame

### **R** — Reference frame frame

Disk reference frame. Connect this frame to another block to specify the location
and orientation of the disk.
### Geometry

### **G** — Geometry geometry

Geometry that represents the disk. Connect this port to a Spatial Contact
Force block to model contacts on the disk.
## Parameters
```yaml
parameters:
- name: Radius
  summary: Radius of disk 1 m (default) | positive integer
  group: ''
- name: Type
  summary: Visual representation of disk From Geometry (default) | None
  group: Graphic
- name: Visual Properties
  summary: Parameterizations for color and opacity Simple (default) | Advanced
  group: Graphic
- name: Diffuse Color
  summary: Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range
    of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1
  group: Graphic
- name: Opacity
  summary: Opacity of rendered object 1.0 (default) | scalar in the range of 0 to 1
  group: Graphic
- name: Specular Color
  summary: Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in
    the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1
  group: Graphic
- name: Ambient Color
  summary: Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to
    1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1
  group: Graphic
- name: Emissive Color
  summary: Self-illumination color [0 0 0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1
    or 1-by-4 vector with values in the range of 0 to 1
  group: Graphic
- name: Shininess
  summary: Shininess of rendered object 75 (default) | scalar in the range of 0 to 128
  group: Graphic
```

### **Radius** — Radius of disk 1 `m` (default) | positive integer

Radius of the disk, specified as a positive integer with a unit of length.

### Graphic

### **Type** — Visual representation of disk `From Geometry` (default) | `None`

Visual representation of the disk. Set this parameter to `From
Geometry` to show the visual representation of the disk. Set this
parameter to `None` to hide the disk in the model
visualization.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify diffuse color and opacity. Select
`Advanced` to specify more visual properties, such as
**Specular Color**, **Ambient Color**,
**Emissive Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry`.

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector.
The optional fourth element specifies the color opacity. Omitting the opacity element
is equivalent to specifying a value of 1.

The diffuse color reflects the main color of the rendered object and provides
shading that gives the rendered object a three-dimensional appearance.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry`.

### **Opacity** — Opacity of rendered object 1.0 (default) | scalar in the range of 0 to 1

Opacity of the rendered object, specified as a scalar in the range of 0 to 1. A
scalar of 0 corresponds to completely transparent, and a scalar of 1 corresponds to
completely opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B] or
[R,G,B,A] vector with values in the range of 0 to 1. The vector can be a row or column
vector. The optional fourth element specifies the color opacity. Omitting the opacity
element is equivalent to specifying a value of 1.

The specular highlight is the bright spot on the rendered object due to the
reflection of the light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A] vector with
values in the range of 0 to 1. The vector can be a row or column vector. The optional
fourth element specifies the color opacity. Omitting the opacity element is equivalent
to specifying a value of 1.

This property specifies a general level of illumination that does not come
directly from a light source. Use this property to change the shadow color of the
rendered object.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0 0 0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector with
values in the range of 0 to 1. The vector can be a row or column vector. The optional
fourth element specifies the color opacity. Omitting the opacity element is equivalent
to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Shininess of rendered object 75 (default) | scalar in the range of 0 to 128

Shininess of the rendered object, specified as a scalar in the range of 0 to 128.
This property affects the sharpness of the specular reflections of the rendered
object. An object with high shininess has a mirror-like appearance, and an object with
low shininess has a more low-gloss or satin appearance.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`
## Libraries

Simscape / Multibody / Curves and Surfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Disk for contact modeling

The Disk block creates a 2-D circular disk that you can use
to model contact problems. You can model the contact between disk and many other geometries,
including an infinite plane, brick, cylinder, ellipsoid, sphere, or convex hull.

The Disk block has two ports. The **R**
port corresponds to the reference frame that is coincident with the origin of the disk
geometry, and the disk lies on the *xy*-plane of the reference frame. The
**G** port is a geometry port that represents the geometry of the
disk.

Disk illustration

To specify the size of the disk, use the **Radius** parameter.
