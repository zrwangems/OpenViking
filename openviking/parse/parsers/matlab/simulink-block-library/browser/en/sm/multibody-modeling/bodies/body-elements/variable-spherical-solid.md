---
type: simulink-block
title: 'Variable Spherical Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Body Elements'
documentation_page: 'variablesphericalsolid'
documentation_source_path: 'ref/variablesphericalsolid.html'
language: en
---

# Variable Spherical Solid

## Ports

### Frame

### **R** — Reference frame frame

Local reference frame of the solid. This frame is fixed with respect
to the solid geometry. The frame origin is located at the center of
geometry. Connect this port to a frame entity—port, line, or junction—to
resolve the frame placement in a model. For more information, see Working with Frames.
### Physical Signal Input

### **r** — Radius of the sphere physical signal

Input port for the radius of the sphere.

### **m** — Mass of the sphere physical signal

Input port for the mass of the sphere.
### Physical Signal Output

### **r** — Radius of the sphere physical signal

Output port for the radius of the sphere.

### **m** — Mass of the sphere physical signal

Output port for the mass of the sphere.

### **com** — Center-of-mass coordinates of the sphere physical signal

Output port for the center of mass of the sphere, reported as a
three-element vector with Cartesian coordinates resolved in the
reference frame of the solid.

### **I** — Inertia matrix of the sphere physical signal

Output port for the inertia matrix of the sphere, reported as a
nine-element matrix resolved in the inertia frame of resolution of the
solid—a virtual copy of the reference frame whose origin has been
shifted to the center of mass. The axes of the inertia frame of
resolution are parallel to the axes of the reference frame. The diagonal
elements of the matrix are the moments of inertia and the off-diagonal
elements are the products of inertia.

## Parameters

#### Geometry and Inertia

### **Radius** — Radius parameterization `Calculate from Mass` (default) | `Constant` | `Provided by Input`

Parameterization of the radius of the solid. Select
`Constant` to specify a fixed value as a block
parameter. Select `Provided by Input` to specify a
variable value as a physical signal input. Use the default setting
(`Calculated from Mass`) to obtain this
parameter from the specified solid density and remaining dimensions.
Selecting `Provided by Input` exposes a new
physical signal input port, labeled **r**, through which to
specify the variable value.

### **Radius: Value** — Value of the radius `1 m` (default) | scalar with units of length

Radius of the solid. The longitudinal axis of the solid is aligned with
the *z*-axis of the local reference frame. The
*z* dimension is constant when this block parameter is
active.

#### Parameter Dependencies

This parameter is active when the **Radius**
parameter is set to `Constant`.

### **Mass** — Mass parameterization `Provided by Input` (default) | `Calculate from Geometry`

Parameterization of the mass of the solid. Select `Calculate
from Geometry` to obtain this parameter from the specified
solid density and dimensions. Use the default setting (`Provided
by Input`) to specify this parameter directly as a
time-variable physical signal. This option exposes a new physical signal
input port, labeled **M**, through which to specify the
time-variable solid mass.

### **Mass: Density** — Mass per unit volume of material `1000 kg/m^3` (default) | scalar in units of mass per unit volume

Mass per unit volume of material. The mass density can take on a positive
or negative value. Specify a negative mass density to model the effects of a
void or cavity in a solid body. The default value, `1000
kg/m^3`, is characteristic of polymers such as ABS
plastic.

#### Parameter Dependencies

This parameter is active when the **Mass** parameter
is set to `Calculate from Geometry`.

#### Sensing

### **Radius** — Sensing selection for the radius cleared (default) | checked

Sensing selection for the radius of the solid. Check to expose a new
physical signal output port, labeled **r**, through which
to output the time-varying value of the radius.

### **Mass** — Sensing selection for the total mass cleared (default) | checked

Sensing selection for the total mass of the solid. Check to expose a new
physical signal output port, labeled **m**, through which
to output the time-varying value of the solid mass.

### **Center of Mass** — Sensing selection for the center-of-mass coordinates cleared (default) | checked

Sensing selection for the coordinates of the center of mass of the solid.
Check to expose a new physical signal output port, labeled
**com**, through which to output the time-varying
coordinates. The output is a three-element vector with Cartesian coordinates
resolved in the reference frame of the solid.

### **Inertia Matrix** — Sensing option for the inertia matrix cleared (default) | checked

Sensing selection for the inertia matrix of the solid. Check to expose a
new physical signal output port, labeled **I**, through
which to output the time-varying inertia matrix. The output is a
nine-element matrix with the moments of inertia in the diagonal positions
and the products of inertia in the off-diagonal positions. The moments and
products of inertia are resolve in the inertia frame of resolution—a frame
with axes parallel to those of the reference frame but origin at the center
of mass.

### Graphic

### **Type** — Graphic to use for visualization `From Geometry` (default) | `Marker` | `None`

Type of the visual representation of the solid, specified as `From Geometry`, `Marker`, or `None`. Set the parameter to `From Geometry` to show the visual representation of the solid. Set the parameter to `Marker` to represent the solid as a marker. Set the parameter to `None` to hide the solid in the model visualization.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify **Diffuse
Color** and **Opacity**. Select
`Advanced` to specify more visual
properties, such as **Specular Color**, **Ambient
Color**, **Emissive Color**, and
**Shininess**.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry` or
`Marker`.

### **Shape** — Shape of marker to represent to the solid `Sphere` (default) | `Cube` | `Frame`

Shape of the marker by means of which to visualize the solid. The motion of the marker reflects the motion of the solid itself.

#### Dependencies

To enable this parameter, set **Type** to `Marker`.

### **Size** — Width of the marker in pixels 10 `pixels` (default) | scalar

Width of the marker in pixels. This width does not scale with zoom level. Note that the apparent size of the marker depends partly on screen resolution, with higher resolutions packing more pixels per unit length, and therefore producing smaller icons.

#### Dependencies

To enable this parameter, set **Type** to `Marker`.

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector. The
optional fourth element specifies the color opacity. Omitting the opacity element is
equivalent to specifying a value of 1.

The diffuse color reflects the main color of the rendered solid and provides shading
that gives the rendered object a three-dimensional appearance.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0
corresponds to completely transparent, and a scalar of 1 corresponds to completely
opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
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

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A] vector with values in
the range of 0 to 1. The vector can be a row or column vector. The optional fourth
element specifies the color opacity. Omitting the opacity element is equivalent to
specifying a value of 1.

Ambient light refers to a general level of illumination that does not come directly
from a light source. The Ambient light consists of light that has been reflected and
re-reflected so many times that it is no longer coming from any particular direction.
You can adjust this parameter to change the shadow color of the rendered solid.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector in the
range of 0 to 1. The vector can be a row or column vector. The optional fourth element
specifies the color opacity. Omitting the opacity element is equivalent to specifying a
value of 1.

The emission color is color that does not come from any external
source, and therefore seems to be emitted by the solid itself. When
a solid has an emissive color, the solid can be seen even if there
is no external light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
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

**Introduced in R2017b**

## Description

Solid sphere with variable mass and size

The Variable Spherical Solid block adds to the attached frame a solid
sphere with variable mass and size. The mass and radius of the sphere can each be
constant or vary with time. A variable quantity can be specified directly as a physical
signal or it can be calculated as a function of the remaining quantity. Only one
quantity, mass or radius, can be calculated during simulation.

A reference frame encodes the position and orientation of the solid relative to other
components in a model. The frame is defined relative to the solid geometry so that its
origin is located at the center of the sphere. This relationship is preserved during
simulation. The radius increases symmetrically in all directions with respect to the
frame origin.

**Variable Sphere with Radius Calculated from Mass**

Visualization is dynamic. Solid dimensions update continuously as they occur, in the
visualization pane of Multibody Explorer. The initial dimensions of the
solid depend on the parameters and physical signals that you specify. It is possible for
a variable dimension to begin with a zero value—for example, if it derives from a
physical signal whose initial value is zero also.

Density can itself be constant or variable. This quantity is specified as a constant
if either mass or radius is calculated during simulation. It is calculated as a variable
if both mass and radius are explicitly specified, either as (constant) block parameters
or as physical signals. As in the case of the solid blocks, you can specify a negative
density, for example, to model voids in compound bodies.
