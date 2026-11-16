---
type: simulink-block
title: 'Graphic'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Body Elements'
documentation_page: 'graphic'
documentation_source_path: 'ref/graphic.html'
language: en
---

# Graphic

## Ports

### Frame

### **R** — Reference frame frame

Local reference frame of the graphic marker. Connect to a frame line
or frame port to define the relative position and orientation of the
marker.

## Parameters

### **Shape** — Shape of the marker to show during visualization `Sphere` (default) | `Cube` | `Frame`

Shape of the marker to show in the visualization of the model, specified
as `Sphere`, `Cube`, or
`Frame`. The motion of the marker reflects the
motion of the frame to which the block is connected.

### **Size** — Width of the marker in pixels 10 `pixels` (default) | scalar

Width of the marker in pixels, specified as a scalar. This width does not
scale with zoom level. Note that the apparent size of the marker depends
partly on screen resolution, with higher resolutions packing more pixels per
unit length, and therefore producing smaller icons.

### Visual Properties

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify **Diffuse
Color** and **Opacity**. Select
`Advanced` to specify more visual
properties, such as **Specular Color**,
**Ambient Color**, **Emissive
Color**, and **Shininess**.

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B]
or [R,G,B,A] vector with values in the range of 0 to 1. The vector can
be a row or column vector. The optional fourth element specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A
scalar of 0 corresponds to completely transparent, and a scalar of 1
corresponds to completely opaque.

#### Dependencies

To enable this parameter, set **Visual
Properties** to
`Simple`.

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B]
or [R,G,B,A] vector with values in the range of 0 to 1. The vector can
be a row or column vector. The optional fourth element specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

#### Dependencies

To enable this parameter, set **Visual
Properties** to
`Advanced`.

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or
column vector. The optional fourth element specifies the color opacity.
Omitting the opacity element is equivalent to specifying a value of
1.

Ambient light refers to a general level of illumination that does not
come directly from a light source. The Ambient light consists of light
that has been reflected and re-reflected so many times that it is no
longer coming from any particular direction.

#### Dependencies

To enable this parameter, set **Visual
Properties** to
`Advanced`.

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A]
vector in the range of 0 to 1. The vector can be a row or column vector.
The optional fourth element specifies the color opacity. Omitting the
opacity element is equivalent to specifying a value of 1.

The emission color is color that does not come
from any external source, and therefore seems to be
emitted by the marker itself. When a marker has an
emissive color, the marker can be seen even if there
is no external light source.

#### Dependencies

To enable this parameter, set **Visual
Properties** to
`Advanced`.

### **Shininess** — Shininess of marker 75 (default) | scalar in the range of 1 to 128

Shininess of the marker, specified as a scalar in the range of 0 to
128. This parameter affects the sharpness of the specular reflections of
the marker. A marker with high shininess has a mirror-like appearance,
and marker with low shininess has a more low-gloss or satin
appearance.

#### Dependencies

To enable this parameter, set **Visual
Properties** to
`Advanced`.

## Libraries

Simscape / Multibody / Body Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Marker with graphic properties

The Graphic block adds a simple marker to the attached frame. The
marker has a simple geometry, color, and no inertia. You can use this block to highlight
a frame of interest in the Multibody Explorer visualization pane. The
graphic marker has no impact on model dynamics.

**Graphic Marker Geometries**
