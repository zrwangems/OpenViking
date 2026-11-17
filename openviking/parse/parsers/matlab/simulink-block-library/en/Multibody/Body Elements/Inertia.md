---
type: simulink-block
title: 'Inertia'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'inertia'
documentation_source_path: 'ref/inertia.html'
language: en
---

# Inertia

## Ports
```yaml
ports:
- name: R
  summary: Reference frame frame
  direction: unspecified
```

### Frame

### **R** — Reference frame frame

Local reference frame of the inertia element. Connect to a frame line
or frame port to define the relative position and orientation of the
inertia.
## Parameters
```yaml
parameters:
- name: Type
  summary: Inertia parameterization to use Point Mass (default) | Custom
  group: Inertia
- name: Mass
  summary: Total mass of the solid element 1 kg (default) | scalar with units of mass
  group: Inertia
- name: 'Custom: Center of Mass'
  summary: Center-of-mass coordinates [0 0 0] m (default) | three-element vector with units of length
  group: Inertia
- name: 'Custom: Moments of Inertia'
  summary: Diagonal elements of inertia tensor [1 1 1] kg*m^2 (default) | three-element vector with units of mass\*length^2
  group: Inertia
- name: 'Custom: Products of Inertia'
  summary: Off-diagonal elements of inertia tensor [0 0 0] kg*m^2 (default) | three-element vector with units of mass\*length^2
  group: Inertia
- name: Type
  summary: Graphic to use in the visualization of the inertia Marker (default) | None
  group: Graphic
- name: Shape
  summary: Shape of marker to represent to the inertia Inertia Icon (default) | Sphere | Cube | Frame
  group: Graphic
- name: Size
  summary: Width of the marker in pixels 20 pixels (default) | scalar
  group: Graphic
- name: Visual Properties
  summary: Parameterizations for color and opacity Simple (default) | Advanced
  group: Graphic
- name: Diffuse Color
  summary: Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range
    of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1
  group: Graphic
- name: Opacity
  summary: Graphic opacity 1.0 (default) | scalar in the range of 0 to 1
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
  summary: Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to
    1
  group: Graphic
- name: Shininess
  summary: Shininess of marker 75 (default) | scalar in the range of 1 to 128
  group: Graphic
```

### Inertia

### **Type** — Inertia parameterization to use `Point Mass` (default) | `Custom`

Inertia parameterization to use. Select `Point
Mass` to represent a mass with no rotational inertia.
Select `Custom` to represent a distributed mass
with rotational inertia.

### **Mass** — Total mass of the solid element `1 kg` (default) | scalar with units of mass

Total mass to attribute to the solid element. This parameter can be positive or
negative. Use a negative value to capture the effect of a void or cavity in a compound
body (one comprising multiple solids and inertias), being careful to ensure that the
mass of the body is on the whole positive.

### **Custom: Center of Mass** — Center-of-mass coordinates `[0 0 0] m` (default) | three-element vector with units of length

[x y z] coordinates of the center of mass relative to the block
reference frame. The center of mass coincides with the center of gravity
in uniform gravitational fields only.

### **Custom: Moments of Inertia** — Diagonal elements of inertia tensor `[1 1 1] kg*m^2` (default) | three-element vector with units of mass\*length^2

Three-element vector with the [Ixx Iyy
Izz] moments of inertia specified relative to a frame with
origin at the center of mass and axes parallel to the block reference frame. The moments
of inertia are the diagonal elements of the inertia tensor

(IxxIyyIzz),

where:

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

### **Custom: Products of Inertia** — Off-diagonal elements of inertia tensor `[0 0 0] kg*m^2` (default) | three-element vector with units of mass\*length^2

Three-element vector with the [Iyz Izx Ixy]
products of inertia specified relative to a frame with origin at the
center of mass and axes parallel to the block reference frame. The
products of inertia are the off-diagonal elements of the inertia tensor

(IxyIzxIxyIyzIzxIyz),

where:

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

### Graphic

### **Type** — Graphic to use in the visualization of the inertia `Marker` (default) | `None`

Type of graphic to use in the visualization of the inertia, specified
as `Marker` or `None`.
Set this parameter to `Marker` to represent the
inertia as a marker, and set this parameter to
`None` to hide the inertia from the model
visualization.

### **Shape** — Shape of marker to represent to the inertia `Inertia Icon` (default) | `Sphere` | `Cube` | `Frame`

Shape of the marker, specified as `Inertia
Icon`, `Sphere`,
`Cube`, or
`Frame`. The motion of the marker reflects the
motion of the inertia itself.

#### Dependencies

To enable this parameter, set **Type** to
`Marker`.

### **Size** — Width of the marker in pixels 20 `pixels` (default) | scalar

Width of the marker in pixels, specified as a scalar. This width does
not scale with zoom level. Note that the apparent size of the marker
depends partly on screen resolution, with higher resolutions packing
more pixels per unit length, and therefore producing smaller
icons.

#### Dependencies

To enable this parameter, set **Type** to
`Marker`.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify **Diffuse
Color** and **Opacity**. Select
`Advanced` to specify more visual
properties, such as **Specular Color**,
**Ambient Color**, **Emissive
Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to
`Marker`.

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B]
or [R,G,B,A] vector with values in the range of 0 to 1. The vector can
be a row or column vector. The optional fourth element specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

#### Dependencies

To enable this parameter, set **Type** to
`Marker`.

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A
scalar of 0 corresponds to completely transparent, and a scalar of 1
corresponds to completely opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to
   `Marker`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B]
or [R,G,B,A] vector with values in the range of 0 to 1. The vector can
be a row or column vector. The optional fourth element specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to
   `Marker`
2. **Visual Properties** to
   `Advanced`

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

To enable this parameter, set:

1. **Type** to
   `Marker`
2. **Visual Properties** to
   `Advanced`

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

To enable this parameter, set:

1. **Type** to
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Shininess of marker 75 (default) | scalar in the range of 1 to 128

Shininess of the marker, specified as a scalar in the range of 0 to
128. This parameter affects the sharpness of the specular reflections of
the marker. A marker with high shininess has a mirror-like appearance,
and marker with low shininess has a more low-gloss or satin
appearance.

#### Dependencies

To enable this parameter, set:

1. **Type** to
   `Marker`
2. **Visual Properties** to
   `Advanced`
## Libraries

Simscape / Multibody / Body Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Mass element with fixed inertial properties

The Inertia block adds to the attached frame a point or distributed
mass with fixed inertial properties. The type of mass (point or distributed) depends on
the parameterization selected for the block. A selection of `Point
Mass` assumes the mass to be concentrated at a point and therefore
devoid of rotational inertia. A selection of `Custom` assumes
the mass to be distributed in space, allowing it to possess nonzero moments of inertia,
products of inertia, and center-of-mass coordinates (the latter against the reference
frame of the block).

A choice of marker provides a means to identify the inertia in the model
visualization. The visualization opens (by default) in Multibody Explorer
at the start of simulation or upon diagram update. Use the marker to track the motion of
the inertia against the remainder of the model. Various marker shapes are available—an
inertia icon, a sphere, a cube, a frame—each with configurable dimensions. To eliminate
the inertia from the model visualization (while retaining its effects on the model
dynamics), the block provides an option of `None`.
