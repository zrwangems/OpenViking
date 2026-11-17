---
type: simulink-block
title: 'General Flexible Plate'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Flexible Bodies / Plates and Shells'
documentation_page: 'generalflexibleplate'
documentation_source_path: 'ref/generalflexibleplate.html'
language: en
---

# General Flexible Plate

## Ports
```yaml
ports:
- name: FN
  summary: Custom frame frame
  direction: unspecified
- name: R
  summary: Reference frame frame
  direction: unspecified
```

### Frame

### **FN** — Custom frame frame

Custom body-attached frames. Specified the name of the port using the New Frame parameter. If you do
not specify the name of the custom frame, the block names the frame
**FN**, where `N` is an identifying number.

#### Dependencies

To enable a custom frame port, create a frame by clicking **New
Frame**.

### **R** — Reference frame frame

Reference frame of the fictitious undeformed body that represents the
overall rigid-body motion of the flexible body. The
**R** frame is not physically
attached to the flexible body.

The **R** port must not be rigidly connected to any
blocks that exert forces and torques or possess inertia.
## Parameters
```yaml
parameters:
- name: Midsurface
  summary: Coordinates of plate midsurface [1 1; -1 1; -1 -1; 1 -1] m | *N*-by-2 matrix | *M*-by-1 or 1-by-*M* cell array
    of *N*-by-2 matrices
  group: Geometry
- name: Thickness
  summary: Plate thickness 0.1 m (default) | positive scalar
  group: Geometry
- name: Density
  summary: Mass per unit volume of material 2700 kg/m^3 (default) | positive scalar
  group: Stiffness and Inertia
- name: Specify
  summary: Elastic properties used to parameterize plate Young's Modulus and Poisson's Ratio (default) | Young's and Shear
    Modulus
  group: Stiffness and Inertia
- name: Young's Modulus
  summary: Ratio of axial stress to axial strain 70 GPa (default) | positive scalar
  group: Stiffness and Inertia
- name: Poisson's Ratio
  summary: Ratio of transverse to normal strains 0.33 (default) | scalar in the range [0, 0.5)
  group: Stiffness and Inertia
- name: Shear Modulus
  summary: Ratio of shear stress to engineering shear strain 26 GPa (default) | positive scalar
  group: Stiffness and Inertia
- name: Type
  summary: Type of damping method Proportional (default) | Uniform Modal | None
  group: Damping
- name: Mass Coefficient
  summary: Coefficient of mass matrix 0 1/s (default) | nonnegative scalar
  group: Damping
- name: Stiffness Coefficient
  summary: Coefficient of stiffness matrix 0.001 s (default) | nonnegative scalar
  group: Damping
- name: Damping Ratio
  summary: Damping ratio for uniform modal damping method 0.01 (default) | unitless nonnegative scalar
  group: Damping
- name: Type
  summary: Type of reference conditions Linearized Mean Axes (default) | Body-Fixed
  group: Reference Conditions
- name: Frame
  summary: Connection frame used for body-fixed reference conditions frame name
  group: Reference Conditions
- name: Show Port R
  summary: Show reference frame port off (default) | on
  group: Reference Conditions
- name: Reduction
  summary: Method to model flexible bodies None (default) | Modally Reduced
  group: Fidelity
- name: Number of Retained Modes
  summary: Retained modes 1 (default) | nonnegative integer
  group: Fidelity
- name: Type
  summary: Graphic to use in the visualization of plate From Geometry (default) | None
  group: Graphic
- name: Visual Properties
  summary: Parameterizations for color and opacity Simple (default) | Advanced
  group: Graphic
- name: Color
  summary: Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range
    of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1
  group: Graphic
- name: Opacity
  summary: Graphic opacity 1.0 (default) | scalar in the range of 0 to 1
  group: Graphic
- name: Diffuse Color
  summary: Graphic Color [0.5 0.5 0.5] (default) | three-element vector | three-element vector
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
- name: New Frame
  summary: Create custom frame for connection to other blocks button
  group: Frames
- name: FrameN
  summary: Edit or delete existing custom frame frame name
  group: Frames
```

### Geometry

### **Midsurface** — Coordinates of plate midsurface [1 1; -1 1; -1 -1; 1 -1] `m` | *N*-by-2 matrix | *M*-by-1 or 1-by-*M* cell array of *N*-by-2 matrices

Coordinates used to specify the midsurface boundaries of the plate on the local
*xy* plane. You can specify the midsurface by using:

- An *N*-by-2 matrix of *xy* coordinates to specify a
  midsurface. Each row gives the [*x*,*y*] coordinates of a point on the mid-surface boundaries. The points
  connect in the specified order to form a closed polyline. To ensure that the
  polyline is closed, the block inserts a line segment between the last and first
  points.
- An *M*-by-1 or 1-by-*M* cell array of
  *N*-by-2 matrices of *xy* coordinates to
  specify a midsurface with holes. The first element in the array represents the
  outer boundary and subsequent elements specify the hole boundaries.

**Note**

Ensure that any two boundaries do not intersect, overlap, or touch.

Additionally, each individual boundary must have:

- No repeated vertices
- No self-intersections
- At least three non-collinear points

### **Thickness** — Plate thickness 0.1 `m` (default) | positive scalar

Thickness of the plate. The block models the plate by extruding the specified
midsurface along the local *z* axis of the plate. The extrusion is
symmetric about the local *xy* plane of the pate. The thickness
should be much smaller than the overall midsurface dimensions for plate theory to
apply.

### Stiffness and Inertia

### **Density** — Mass per unit volume of material 2700 `kg/m^3` (default) | positive scalar

Mass per unit volume of material. The default value corresponds to aluminum.

### **Specify** — Elastic properties used to parameterize plate `Young's Modulus and Poisson's Ratio` (default) | `Young's and Shear Modulus`

Elastic properties used to parameterize the plate. You can specify either
`Young's Modulus and Poisson's Ratio` or `Young's and Shear
Modulus`. These properties are commonly available in materials
databases.

### **Young's Modulus** — Ratio of axial stress to axial strain 70 `GPa` (default) | positive scalar

Young's modulus of the elasticity of the plate. The greater the value of this
parameter, the stronger the resistance to bending and in-plane normal deformation. The
default value corresponds to aluminum.

### **Poisson's Ratio** — Ratio of transverse to normal strains 0.33 (default) | scalar in the range [0, 0.5)

Poisson's ratio of the plate. The value specified must be greater than or equal to 0
and smaller than 0.5. The default value corresponds to aluminum.

#### Dependencies

To enable this parameter, set **Specify** to `Young's
Modulus and Poisson's Ratio`.

### **Shear Modulus** — Ratio of shear stress to engineering shear strain 26 `GPa` (default) | positive scalar

Shear modulus, also known as the modulus of rigidity, of the plate. The larger value
correlates to a stronger resistance to shearing and twisting. The default value
corresponds to aluminum.

#### Dependencies

To enable this parameter, set **Specify** to `Young's
and Shear Modulus`.

### Damping

### **Type** — Type of damping method `Proportional` (default) | `Uniform Modal` | `None`

Damping method for the plate:

- Select `None` to model undamped plates.
- Select `Proportional` to apply the proportional
  (or Rayleigh) damping method. This method defines the damping matrix
  [*C*] as a linear combination of the mass matrix
  [*M*] and stiffness matrix
  [*K*]:

  [C]=α[M]+β[K],

  where *α* and *β* are the scalar
  coefficients.
- Select `Uniform Modal` to apply the uniform modal
  damping method. This method applies a single damping ratio to all the
  vibration modes of the plate. The larger the value, the faster vibrations
  decay.

  The chosen reference conditions impact the types of modes to which the
  damping ratio applies. For details on reference conditions, see Reference Conditions. When you
  use modal reduction for the flexible body, only a subset of modes is
  retained. For details on modal reduction, see Reduce the Degrees of Freedom for a Flexible Body.

### **Mass Coefficient** — Coefficient of mass matrix 0 `1/s` (default) | nonnegative scalar

Coefficient *α* of the mass matrix. This parameter defines damping
proportional to the mass matrix [*M*].

#### Dependencies

To enable this parameter, set **Type** to
`Proportional`.

### **Stiffness Coefficient** — Coefficient of stiffness matrix 0.001 `s` (default) | nonnegative scalar

Coefficient *β* of the stiffness matrix. This parameter defines
damping proportional to the stiffness matrix [*K*].

#### Dependencies

To enable this parameter, set **Type** to
`Proportional`.

### **Damping Ratio** — Damping ratio for uniform modal damping method 0.01 (default) | unitless nonnegative scalar

Damping ratio *ζ* applied to all vibration modes of a plate. The
larger the value, the faster vibrations decay. If the boundary conditions applied to the
plate exactly match the chosen reference conditions, *ζ* < 1 yields underdamped modal decay, while *ζ* > 1 yields overdamped dissipation. When the boundary conditions and
reference conditions do not match, the effect of the chosen damping ratio varies. For
details of reference condition, see Reference Conditions.

#### Dependencies

To enable this parameter, set **Type** to `Uniform
Modal`.

**Data Types:** `double`

### Reference Conditions

### **Type** — Type of reference conditions `Linearized Mean Axes` (default) | `Body-Fixed`

Specify the type of reference conditions to apply. For details, see Reference Conditions.

- `Linearized Mean Axes`: The body frame of
  reference follows the instantaneous center of mass and the flexible
  body exhibits unconstrained vibration modes of deformation.
- `Body-Fixed`: Choose a body-attached frame as the
  body frame of reference. The deformation of the flexible body
  exhibits free vibration mode shapes with zero translational and
  rotational deformation at the location of the body frame of
  reference.

### **Frame** — Connection frame used for body-fixed reference conditions frame name

Enter the name of the connection frame to use as the body frame of reference.
The frame name is case-sensitive. Ensure the selected frame is exposed as a port
on the block. You cannot use the **R** frame, which is the
reference frame of the fictitious undeformed body.

#### Dependencies

To enable this parameter, set **Type** to
`Body-Fixed`.

### **Show Port R** — Show reference frame port off (default) | on

Select to expose the **R** port, which represents the
reference frame of the fictitious undeformed body. Note that the
**R** frame is not physically attached to the flexible
body.

The **R** port must not be rigidly connected to any blocks
that exert forces and torques or possess inertia.

### Fidelity

### **Reduction** — Method to model flexible bodies `None` (default) | `Modally Reduced`

Method to use to model flexible bodies, specified as
`None` or `Modally Reduced`. Set
the parameter to `None` to use full nodal elastic coordinates
generated by the finite-element method or set the parameter to `Modally
Reduced` to use the modal transformation method to reduce the elastic
coordinates of the body. For both settings, the block uses the floating frame of the
reference formulation [5-6] to couple the body with its elastic deformation.

### **Number of Retained Modes** — Retained modes 1 (default) | nonnegative integer

Retained modes, specified as an integer in range [0, *n*], where
*n* is the number of elastic degrees of freedom of the body. If you
set the number to 0 the flexible body is treated as a rigid body.

#### Dependencies

To enable this parameter, set **Reduction** to
`Modally Reduced`.

### Graphic

### **Type** — Graphic to use in the visualization of plate `From Geometry` (default) | `None`

Type of the visual representation of the plate, specified as `From
Geometry` or `None`. Set the parameter to
`From Geometry` to show the visual representation of the
plate. Set the parameter to `None` to hide the plate in the
model visualization.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterization for specifying visual properties. Select
`Simple` to specify color and opacity. Select
`Advanced` to specify more visual properties, such as
**Specular Color**, **Ambient Color**, **Emissive
Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry`.

### **Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the graphic under direct white light, specified as an [R G B] or [R G B A]
vector on a 0–1 scale. An optional fourth element (A) specifies the color opacity on a
scale of 0–1. Omitting the opacity element is equivalent to specifying a value of
1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Simple`

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0
corresponds to completely transparent, and a scalar of 1 corresponds to completely
opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Simple`

### **Diffuse Color** — Graphic Color [0.5 0.5 0.5] (default) | three-element vector | three-element vector

Color of the graphic under direct white light, specified as an [R G B] or [R G B A]
vector on a 0–1 scale. The optional fourth element specifies the color opacity on a
scale of 0–1. Omitting the opacity element is equivalent to specifying a value of
1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to
   `Advanced`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector. The
optional fourth element specifies the color opacity. Omitting the opacity element is
equivalent to specifying a value of 1. This parameter changes the color of the specular
highlight, which is the bright spot on the rendered beam due to the reflection of the
light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
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
You can adjust this parameter to change the shadow color of the rendered beam.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector in the
range of 0 to 1. The vector can be a row or column vector. The optional fourth element
specifies the color opacity. Omitting the opacity element is equivalent to specifying a
value of 1.

The emission color is color that does not come from any external
source, and therefore seems to be emitted by the beam itself. When a
beam has an emissive color, the beam can be seen even if there is no
external light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From
   Geometry`
2. **Visual Properties** to
   `Advanced`

### Frames

### **New Frame** — Create custom frame for connection to other blocks button

Click the Create button Create to open a pane for creating a new body-attached
frame. In this pane, you can specify the name, origin, and orientation for the
frame.

- To name the custom frame, enter a name in the **Frame
  Name** parameter. The name identifies the port on the block and in
  the tree view pane of the Multibody Explorer.
- Select a frame origin in the **Frame Origin** section:

  - **At Reference Frame Origin**: Make the new frame
    origin coincident with the origin of the reference frame of the undeformed
    plate.
  - **Based on Geometric Feature**: Make the new frame
    origin coincident with the center of the selected undeformed geometry
    feature. Valid features include surfaces, lines, and points. Select a
    feature from the visualization pane, then click **Use Selected
    Feature** button to confirm the location of the origin. The
    name of the origin location appears in the field below this option.
- To define the orientation of the custom frame, under the **Frame
  Axes** section, select the **Primary Axis** and
  **Secondary Axis** of the custom frame and then specify their
  directions.

  Use the following methods to select a vector for specifying the directions
  of the primary and secondary axes. The primary axis is parallel to the selected
  vector and constrains the remaining two axes to its normal plane. The secondary
  axis is parallel to the projection of the selected vector onto the normal
  plane.

  - **Along Reference Frame Axis**: Selects an axis of
    the reference frame of the undeformed plate.
  - **Based on Geometric Feature**: Selects the vector
    associated with the chosen geometry feature of the undeformed plate. Valid
    features include surfaces and lines. The corresponding vector is indicated
    by a white arrow in the visualization pane. You can select a feature from
    the visualization pane and then click **Use Selected
    Feature** button to confirm the selection. The name of the
    selected feature appears in the field below this option.

### **FrameN** — Edit or delete existing custom frame frame name

Frames that you created. Specified the name of the port using the New Frame parameter. If you do
not specify the name of the custom frame, the block names the frame
**FN**, where `N` is an identifying number.

- Click the text field to edit the name of an existing custom frame.

- Click the Edit button Edit to edit other aspects of the custom frame, such
  as the origin and axes.
- Click the Delete button Delete to delete the custom frame.

#### Dependencies

To enable this parameter, create a frame by clicking **New
Frame**.
## Libraries

Simscape / Multibody / Body Elements / Flexible Bodies / Plates and Shells

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Thin plate with elastic properties for deformation

The General Flexible Plate block models thin, flat
structure capable of elastic deformations, including stretch, bending, and shear effects. The
block applies the shear deformation Mindlin plate theory [1][2][3] and uses the
finite element method [4] for its solution. You
can use this block to model thin, flat structures, such as linkages and satellite solar
panels.

General Flexible Plate

To specify the geometry of a plate, use the **Midsurface** and
**Thickness** parameters. The midsurface of the plate is in the
*xy* plane and the thickness is along the *z* axis. The
thickness must be much smaller than the width and length of the plate, and the plate is
symmetric about the midsurface. See the Geometry section for more
details.

The block models a flexible plate made of homogeneous, isotropic, and linearly elastic
materials. You can specify the density, Young's modulus, and Poisson's ratio or shear modulus
of the plate in the **Stiffness and Inertia** section. Additionally, the
block supports two damping methods to control the performance of the modeling. To add custom
frames to the plate, specify parameters in the **Frames** section.
