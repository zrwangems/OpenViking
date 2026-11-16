---
type: simulink-block
title: 'Brick Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'bricksolid'
documentation_source_path: 'ref/bricksolid.html'
language: en
---

# Brick Solid

## Ports

### Frame

### **R** — Reference frame frame

Local reference frame of the brick solid. This frame is fixed with
respect to the solid geometry. Connect this port to a frame entity—port,
line, or junction—to resolve the placement of the reference frame in a
model. For more information, see Working with Frames.
### Geometry

### **G** — Geometry geometry

Geometry that represents the solid. Connect this port to a Spatial Contact Force block to model contacts on the solid.

#### Dependencies

To enable this port, under **Geometry**, expand **Export**
and select **Entire Geometry**.

## Parameters

### Geometry

### **Dimensions** — Width, thickness, and height of the brick `[1 1 1] m` (default) | scalar with units of length

Lengths of the brick sides along the *x*-,
*y*-, and *z*-axes of the solid
reference frame. These lengths give, in no specific order, the width,
thickness, and height of the brick.

### **Entire Geometry** — Export the true geometry of the block `off` (default) | `on`

Select **Entire Geometry** to export the true
geometry of the Brick Solid block which
can be used for other blocks, such as the Spatial
Contact Force block.

#### Dependencies

To enable this option, select **Entire
Geometry** under the
**Export**.

### Inertia

### **Type** — Inertia parameterization to use `Calculate from Geometry` (default) | `Point Mass` | `Custom`

Inertia parameterization to use. Select `Point
Mass` to model a concentrated mass with negligible
rotational inertia. Select `Custom` to model a
distributed mass with the specified moments and products of inertia. The
default setting, `Calculate from Geometry`,
enables the block to automatically calculate the rotational inertia
properties from the solid geometry and specified mass or mass
density.

### **Based on** — Parameter to base inertia calculation on `Density` (default) | `Mass`

Parameter to use in inertia calculation. The block obtains the inertia
tensor from the solid geometry and the parameter selected. Use
`Density` if the material properties are
known. Use `Mass` if the total solid mass is
known.

### **Density** — Mass per unit volume of material `1000 kg/m^3` (default)

Mass per unit volume of material. The mass density can take on a
positive or negative value. Specify a negative mass density to model the
effects of a void or cavity in a solid body.

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

### **Calculate from Geometry: Derived Values** — Display of calculated values of mass properties button

Display of the calculated values of the solid mass properties—mass,
center of mass, moments of inertia, and products of inertia. Click the
**Update** button to calculate and display the mass
properties of the solid. Click this button following any changes to the
block parameters to ensure that the displayed values are still
current.

The center of mass is resolved in the local reference frame of the
solid. The moments and products of inertia are each resolved in the
inertia frame of resolution—a frame whose axes are parallel to those of
the reference frame but whose origin coincides with the solid center of
mass.

#### Dependencies

The option to calculate and display the mass properties is active
when the **Inertia** > **Type** block parameter is set to `Calculate from
Geometry`.

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

### **Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the graphic under direct white light, specified as an [R G B] or [R G B A]
vector on a 0–1 scale. An optional fourth element (A) specifies the color opacity on a
scale of 0–1. Omitting the opacity element is equivalent to specifying a value of
1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Simple`

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

### Frames

### **Show Port R** — Show reference frame port for connection to other blocks on (default) | off

Select to expose the **R** port.

### **New Frame** — Create custom frame for connection to other blocks button

Click the Create button Create to open a pane for creating a new
body-attached frame. In this pane, you can specify the name, origin, and
orientation for the frame.

- To name the custom frame, click the text field of the
  **Frame Name** parameter. The name identifies
  the corresponding port on the solid block and in the tree view pane
  of the Multibody Explorer.
- To select the **Frame Origin** of the custom
  frame, use one of the following methods:

  - **At Reference Frame Origin**: Make
    the new frame origin coincident with the origin of the
    reference frame of the solid.
  - **At Center of Mass**: Make the new
    frame origin coincident with the center of mass of the
    solid.
  - **Based on Geometric Feature**: Make
    the new frame origin coincident with the center of the
    selected feature. Valid features include surfaces,
    lines, and points. Select a feature from the
    visualization pane, then click **Use Selected
    Feature** to confirm the location of the
    origin. The name of the origin location appears in the
    field below this option.
- To define the orientation of the custom frame, under the
  **Frame Axes** section, select the
  **Primary Axis** and **Secondary
  Axis** of the custom frame and then specify their
  directions.

  Use the following methods to select a vector for specifying the
  directions of the primary and secondary axes. The primary axis is
  parallel to the selected vector and constrains the remaining two
  axes to its normal plane. The secondary axis is parallel to the
  projection of the selected vector onto the normal plane.

  - **Along Reference Frame Axis**:
    Selects an axis of the reference frame of the solid.
  - **Along Principal Inertia Axis**:
    Selects an axis of the principal inertia axis of the
    solid.
  - **Based on Geometric Feature**:
    Selects the vector associated with the chosen geometry
    feature of the solid. Valid features include surfaces
    and lines. The corresponding vector is indicated by a
    white arrow in the visualization pane. You can select a
    feature from the visualization pane and then click
    **Use Selected Feature** to confirm
    the selection. The name of the selected feature appears
    in the field below this option.

### **FrameN** — Edit or delete existing custom frame frame name

Frames that you have created. `N` is a unique identifying number for each
custom frame.

- Click the text field to edit the name of an existing custom
  frame.

- Click the Edit button Edit to edit other aspects of the
  custom frame, such as origin and axes.
- Click the Delete button Delete to delete the custom
  frame.

#### Dependencies

To enable this parameter, create a frame by clicking **New Frame**.

## Libraries

Simscape / Multibody / Body Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Solid brick element with geometry, inertia, and color

The Brick Solid block is a prismatic shape with
geometry center coincident with the reference frame origin and prismatic surfaces normal
to the reference frame x, y, and z axes.

The Brick Solid block adds to the attached frame a solid element with
geometry, inertia, and color. The brick solid element can be a simple rigid body or part
of a compound rigid body—a group of rigidly connected solids, often separated in
space through rigid transformations. Combine Brick Solid and other
solid blocks with the Rigid Transform
blocks to model a compound rigid body.

A reference frame encodes the position and orientation of the solid. In the default
configuration, the block provides only the reference frame. A frame-creation interface
provides the means to define additional frames based on solid geometry features. You
access this interface by selecting the Create button  in the **Frames** expandable area.
