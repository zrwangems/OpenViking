---
type: simulink-block
title: 'Infinite Plane'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'infiniteplane'
documentation_source_path: 'ref/infiniteplane.html'
language: en
---

# Infinite Plane

## Ports

### Frame

### **R** — Reference frame frame

Infinite plane reference frame. Connect this frame to another block to specify the
location and orientation of the infinite plane.
### Geometry

### **G** — Geometry frame

Geometry that represents the plane defined by this block. Connect this port to a
Spatial Contact
Force block to model contacts with supported geometries.

## Parameters

### Graphic

### **Type** — Visual representation of plane `Rectangle` (default) | `None`

Visual representation of the plane. Set this parameter to
`Rectangle` to show the visual representation of the
infinite plane as a rectangle with dash-line boundaries. Set this parameter to
`None` to eliminate the plane from the model
visualization.

### **Width (X)** — Width of plane visual representation 1 `m` (default) | positive integer

Width of the plane's visual representation. Note that the actual plane has
infinite size.

#### Dependencies

To enable this parameter, set **Type** to
`Rectangle`.

### **Height (Y)** — Height of plane visual representation 1 `m` (default) | positive integer

Height of the plane's visual representation. Note that the actual plane has
infinite size.

#### Dependencies

To enable this parameter, set **Type** to
`Rectangle`.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify diffuse color and opacity. Select
`Advanced` to specify more visual properties, such as
**Specular Color**, **Ambient Color**,
**Emissive Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to
`Rectangle`.

### **Diffuse Color** — Graphic color [0.5 0.5 0.5] (default) | three-element vector | four-element vector

Color of the graphic under direct white light, specified as an [R G B] or [R G B
A] vector on a 0–1 scale. An optional fourth element (A) specifies the color opacity
on a scale of 0–1. Omitting the opacity element is equivalent to specifying a value of
1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Rectangle`
2. **Visual Properties** to
   `Simple`

### **Opacity** — Graphic opacity 0.25 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0
corresponds to completely transparent, and a scalar of 1 corresponds to completely
opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Rectangle`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Highlight color [0.5 0.5 0.5 1.0] (default) | three-element vector | four-element vector

Color of specular highlights, specified as an [R,G,B] or [R,G,B,A] vector on a 0–1
scale. The optional fourth element specifies the color opacity. Omitting the opacity
element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Rectangle`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Shadow color [0.15 0.15 0.15 1.0] (default) | three-element vector | four-element vector

Color of shadow areas in diffuse ambient light, specified as an [R,G,B] or
[R,G,B,A] vector on a 0–1 scale. The optional fourth element (A) specifies the color
opacity. Omitting the opacity element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Rectangle`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | three-element vector | four-element vector

Graphic color due to self illumination, specified as an [R,G,B] or [R,G,B,A]
vector on a 0–1 scale. The optional fourth element (A) specifies the color opacity.
Omitting the opacity element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Rectangle`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar in the range of 1 to 128

Sharpness of specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Rectangle`
2. **Visual Properties** to
   `Advanced`

## Libraries

Simscape / Multibody / Curves and Surfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Infinite plane for contact modeling

The Infinite Plane block creates an infinite plane that you
can use to model contact problems. You can model contacts between the plane and various types
of geometries. For the supported geometries, see Supported Geometries. In addition, the
Infinite Plane block supports the Custom Tire Force and
Torque and Magic Formula Tire Force and
Torque blocks.

You must use the positive normal side of the plane for contact, which is in the direction
indicated by the blue axis of the frame. Otherwise, the contacting part will be ejected to the
positive side through the plane.

Infinite Plane

The Infinite Plane block is useful in planar contact
modeling. For example, the Infinite Plane block is much more effective at modeling a ground
plane than the Brick Solid
block.

Infinite Plane Example
