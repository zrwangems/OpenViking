---
type: simulink-block
title: 'Line Segment'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'linesegment'
documentation_source_path: 'ref/linesegment.html'
language: en
---

# Line Segment

## Ports

### Frame

### **R** — Local reference frame frame

Reference frame of the line segment. Connect this frame to another block to
specify the location and orientation of the line segment.
### Geometry

### **G** — Geometry geometry

Geometry that represents the line segment. You can connect this port to a
Planar Contact Force block to model contacts on the
line segment.

## Parameters

### **Length** — Line segment length 1 `m` (default) | positive scalar

Length of the line segment, specified as a positive scalar. The line segment is
along the *x*-axis of the local reference frame.

#### Graphic

### **Type** — Visualization setting `From Geometry` (default) | `None`

Visualization setting for the line segment. Use the default setting,
`From Geometry`, to show the line segment. Select
`None` to disable visualization for the line segment.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify **Diffuse Color** and
**Opacity**. Select `Advanced` to specify
more visual properties, such as **Specular Color**, **Ambient
Color**, **Emissive Color**, and
**Shininess**.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry`.

### **Diffuse Color** — Line segment color [0.5 0.5 0.5] (default) | three-element vector | four-element vector

True color under direct white light, specified as an [R,G,B] or [R,G,B,A] vector on
a 0–1 scale. An optional fourth element specifies the color opacity on a scale of 0–1.
Omitting the opacity element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry`.

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0
corresponds to completely transparent, and a scalar of 1 corresponds to completely
opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector. The
optional fourth element specifies the color opacity. Omitting the opacity element is
equivalent to specifying a value of 1. This parameter changes the color of the specular
highlight, which is the bright spot on the rendered solid due to the reflection of the
light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A] vector with values
in the range of 0 to 1. The vector can be a row or column vector. The optional fourth
element specifies the color opacity. Omitting the opacity element is equivalent to
specifying a value of 1.

Ambient light refers to a general level of illumination that does not come directly
from a light source. The ambient light is light that has been reflected and re-reflected
so many times that it is no longer coming from any particular direction. You can adjust
this parameter to change the shadow color of the rendered object.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector in the
range of 0 to 1. The vector can be a row or column vector. The optional fourth element
specifies the color opacity. Omitting the opacity element is equivalent to specifying a
value of 1.

The emission color is color that does not come from any external
source, and therefore seems to be emitted by the object itself. When
an object has an emissive color, the object can be seen even if
there is no external light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of the specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

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

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Line segment geometry

The Line Segment block creates a line segment. The line segment is along the
*x*-axis of the local reference frame located at the midpoint of the line
segment.

Line segment illustration
