---
type: simulink-block
title: 'General Variable Mass'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Variable Mass'
documentation_page: 'generalvariablemass'
documentation_source_path: 'ref/generalvariablemass.html'
language: en
---

# General Variable Mass

## Ports
```yaml
ports:
- name: m
  summary: Mass physical signal specified as a scalar with units of mass
  direction: input
- name: com
  summary: Center of mass physical signal specified as a 3-by-1 or 1-by-3 vector with units of length
  direction: input
- name: I
  summary: Inertia physical signal specified as a 3-by-3 matrix with units of mass × length^2
  direction: input
- name: R
  summary: Reference frame frame
  direction: input
```

### Input

### **m** — Mass physical signal specified as a scalar with units of mass

Input port for the time-varying mass.

#### Dependencies

This port is enabled when the **Inertia** > **Mass** parameter is set to
`Time-Varying`.

### **com** — Center of mass physical signal specified as a 3-by-1 or 1-by-3 vector with units of length

Input port for the time-varying center-of-mass coordinates. Specify
the coordinates in the order `[x y z]` relative to the
block reference frame.

#### Dependencies

This port is enabled when the **Inertia** > **Center of Mass** parameter is set to
`Time-Varying`.

### **I** — Inertia physical signal specified as a 3-by-3 matrix with units of mass × length^2

Input port for the time-varying inertia tensor. Specify the tensor
elements in the order `[Ixx Ixy I xz; Iyx Iyy Iyz; Izx Izy
Izz]`. The elements are defined relative to a frame with
origin at the center of mass and axes aligned with the reference frame.
See the **Inertia tensor** parameter description for
the definitions of the moments and products of inertia.

#### Dependencies

This port is enabled when the **Inertia** > **Type** parameter is set to
`Custom`.
### Frame

### **R** — Reference frame frame

Local reference frame of the variable mass element. Connect the port
to a frame line or another frame port to define the relative position
and orientation of the variable mass.
## Parameters
```yaml
parameters:
- name: Type
  summary: Choice of point or distributed mass Custom (default) | Point Mass
  group: Inertia
- name: Mass
  summary: Mass parameterization Time-Varying (default) | Constant
  group: Inertia
- name: 'Mass: Value'
  summary: Aggregate mass of the mass element 1 kg (default) | scalar with units of mass
  group: Inertia
- name: Center of Mass
  summary: Center-of-mass parameterization Time-Varying (default) | Constant
  group: Inertia
- name: 'Center of Mass: Value'
  summary: Center-of-mass coordinates [0 0 0] m (default) | three-element vector with units of length
  group: Inertia
- name: Inertia Matrix
  summary: Inertia-matrix parameterization Time-Varying (default) | Constant
  group: Inertia
- name: 'Inertia Matrix: Moments of Inertia'
  summary: Diagonal elements of the inertia matrix [1 1 1] kg * m^2 (default) | three-element vector with units of mass\*length^2
  group: Inertia
- name: 'Inertia Matrix: Products of Inertia'
  summary: Off-diagonal elements of the inertia matrix [0 0 0] kg * m^2 (default) | 3-element array with units of mass \*
    length^2
  group: Inertia
- name: Type
  summary: Geometry type to use in model visualizations Equivalent Inertia Ellipsoid (default) | Marker | None
  group: Graphic
- name: Shape
  summary: Shape of marker to represent to variable mass Sphere (default) | Cube | Frame
  group: Graphic
- name: Size
  summary: Width of the marker in pixels 10 pixels (default) | scalar
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
  summary: Highlight sharpness 75 (default) | scalar with value constrained to 0–128
  group: Graphic
```

### Inertia

### **Type** — Choice of point or distributed mass `Custom` (default) | `Point Mass`

Choice of point or distributed mass. Select `Point
Mass` to model a concentrated mass with no rotational
inertia. Select `Custom` to model a distributed
mass with the specified inertia tensor and center of mass.

### **Mass** — Mass parameterization `Time-Varying` (default) | `Constant`

Choice of fixed or variable mass. Select
`Time-Varying` to specify the mass as a
variable using physical signal input port **m**. Select
`Constant` to specify the mass as a
constant parameter.

### **Mass: Value** — Aggregate mass of the mass element `1 kg` (default) | scalar with units of mass

Aggregate mass of the mass element. The mass can be a positive or
negative value. Specify a negative mass to model the aggregate effect of
voids and cavities in a compound body. The mass is constant when this
parameter is active.

#### Dependencies

This parameter is enabled when the **Mass**
parameter is set to `Constant`.

### **Center of Mass** — Center-of-mass parameterization `Time-Varying` (default) | `Constant`

Choice of fixed or variable center of mass. Select
`Time-Varying` to specify the center of
mass as a variable using physical signal input port
**com**. Select `Constant`
to specify the center of mass as a constant parameter.

### **Center of Mass: Value** — Center-of-mass coordinates `[0 0 0] m` (default) | three-element vector with units of length

[*x*
*y*
*z*] coordinates of the center of mass relative to the
origin of the reference frame. The center of mass coincides with the
center of gravity in uniform gravitational fields only. The center of
mass is constant when this parameter is active.

#### Dependencies

This parameter is enabled when the **Center of
Mass** parameter is set to
`Constant`.

### **Inertia Matrix** — Inertia-matrix parameterization `Time-Varying` (default) | `Constant`

Choice of a variable or fixed inertia matrix. Select
`Time-Varying` to specify the inertia
matrix as a variable using physical signal input port
**I**. Select `Constant`
to specify the moments and products of inertia separately as constant
block parameters.

### **Inertia Matrix: Moments of Inertia** — Diagonal elements of the inertia matrix `[1 1 1] kg * m^2` (default) | three-element vector with units of mass\*length^2

Moments of inertia of the variable mass element specified in the order
[*I*xx
*I*yy
*I*zz]. The moments of inertia
are defined relative to a frame with origin at the center of mass and
with axes parallel to the reference frame axes. The moments of inertia
are the diagonal elements of the inertia tensor,

(IxxIyyIzz),

where:

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

#### Dependencies

This parameter is enabled when the **Inertia
Matrix** parameter is set to
`Constant`.

### **Inertia Matrix: Products of Inertia** — Off-diagonal elements of the inertia matrix `[0 0 0] kg * m^2` (default) | 3-element array with units of mass \* length^2

Products of inertia of the variable mass element specified in the
order [*I*yz
*I*zx
*I*xy]. The products of inertia
are defined relative to a frame with origin at the center of mass and
with axes parallel to the reference frame axes. The products of inertia
are the off-diagonal elements of the inertia matrix,

(IxyIzxIxyIyzIzxIyz),

where:

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

#### Dependencies

This parameter is enabled when the **Inertia
Matrix** parameter is set to
`Constant`.

### Graphic

### **Type** — Geometry type to use in model visualizations `Equivalent Inertia Ellipsoid` (default) | `Marker` | `None`

Visualization setting for this variable mass, specified as
`Equivalent Inertia Ellipsoid`,
`Marker`, or
`None`. Set the parameter to
`Equivalent Inertia Ellipsoid` to represent
the variable mass as an ellipsoid. Set the parameter to
`Marker` to represent the variable mass as
a marker. Set the parameter to `None` to hide
the variable mass in the model visualization.

### **Shape** — Shape of marker to represent to variable mass `Sphere` (default) | `Cube` | `Frame`

Shape of the marker by means of which to visualize the variable mass,
specified as `Sphere`,
`Cube`, or
`Frame`. The motion of the marker reflects the
motion of the variable mass itself.

#### Dependencies

To enable this parameter, set **Type** to
`Marker`.

### **Size** — Width of the marker in pixels 10 `pixels` (default) | scalar

Width of the marker in pixels. This width does not scale with zoom
level. Note that the apparent size of the marker depends partly on
screen resolution, with higher resolutions packing more pixels per unit
length, and therefore producing smaller icons.

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
`Equivalent Inertia Ellipsoid` or
`Marker`.

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B]
or [R,G,B,A] vector with values in the range of 0 to 1. The vector can
be a row or column vector. The optional fourth element specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

The diffuse color reflects the main color of the graphic and provides
shading that gives the graphic a three-dimensional appearance.

#### Dependencies

To enable this parameter, set **Type** to
`From Geometry` or
`Marker`

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A
scalar of 0 corresponds to completely transparent, and a scalar of 1
corresponds to completely opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Equivalent
   Inertia Ellipsoid` or
   `Marker`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B]
or [R,G,B,A] vector with values in the range of 0 to 1. The vector can
be a row or column vector. The optional fourth element specifies the
color opacity. Omitting the opacity element is equivalent to specifying
a value of 1. This parameter changes the color of the specular
highlight, which is the bright spot on the graphic due to the reflection
of the light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Equivalent
   Inertia Ellipsoid` or
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
longer coming from any particular direction. You can adjust this
parameter to change the shadow color of the graphic.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Equivalent
   Inertia Ellipsoid` or
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
emitted by the graphic itself. When a graphic has an
emissive color, the graphic can be seen even if
there is no external light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Equivalent
   Inertia Ellipsoid` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of specular light reflections, specified as a scalar number
on a 0–128 scale. Increase the shininess value for smaller but sharper
highlights. Decrease the value for larger but smoother
highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Equivalent
   Inertia Ellipsoid` or
   `Marker`
2. **Visual Properties** to
   `Advanced`
## Libraries

Simscape / Multibody / Body Elements / Variable Mass

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Mass element with variable inertial properties

The General Variable Mass block adds to the attached frame a mass
element with constant or time-varying inertial properties. The mass element can be a
point mass without rotational inertia or a custom mass with rotational inertia. The
inertial properties include mass, center of mass, moments of inertia, and products of
inertia. Each inertial property can be independently configured as constant or
time-varying.

The geometry of the mass element is unspecified. A marker or equivalent inertia
ellipsoid identifies the mass element in the visualization pane of Multibody
Explorer. An inertia ellipsoid provides a graphical representation of the
principal moments of inertia of the mass element. The block includes an option to hide
the variable mass element in the Multibody Explorer visualization window.
