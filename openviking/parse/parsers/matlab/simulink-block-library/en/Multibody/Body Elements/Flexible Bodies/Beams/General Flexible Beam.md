---
type: simulink-block
title: 'General Flexible Beam'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Flexible Bodies / Beams'
documentation_page: 'generalflexiblebeam'
documentation_source_path: 'ref/generalflexiblebeam.html'
language: en
---

# General Flexible Beam

## Ports

### Frame

### **A** — Connection frame frame

Frame by which to connect the beam in a model. In the undeformed configuration, this frame
is at half the beam length in the -*z* direction relative to the origin of
the local reference frame.

### **B** — Connection frame frame

Frame by which to connect the beam in a model. In the undeformed configuration, this frame
is at half the beam length in the +*z* direction relative to the origin of
the local reference frame.

### **R** — Reference frame frame

Reference frame of the fictitious undeformed body that represents the
overall rigid-body motion of the flexible body. The
**R** frame is not physically
attached to the flexible body.

The **R** port must not be rigidly connected to any
blocks that exert forces and torques or possess inertia.

## Parameters

### Geometry

### **Cross-section** — Cross-section coordinates specified on the `XY` plane [0.5 0.5; -0.5 0.5; -0.5 -0.5; 0.5 -0.5] `m` (default) | *N*-by-2 matrix | *M*-by-1 or 1-by-*M* cell array of *N*-by-2 matrices

Coordinates used to specify the boundaries of a beam cross-section.
Specify the beam cross-section using one of the following
methods:

- Use an *N*-by-2 matrix of *xy* coordinates to
  specify a simply connected section. Each row gives the [*x*,*y*] coordinates of a point on the cross-section
  boundary. The points connect in the order given to form a closed
  polyline. To ensure that the polyline is closed, a line segment
  is always inserted between the last and first points.
- Use an *M*-by-1 or 1-by-*M*
  cell array of *N*-by-2 matrices of
  *xy* coordinates to specify a multiply
  connected section. The first entry in the cell represents the
  outer boundary and subsequent entries specify the hole
  boundaries.

**Note**

To properly define the cross-section of beams, any two boundaries
should not intersect, overlap, or touch.

Additionally, each individual boundary should have:

- No repeated vertices.
- No self-intersections.
- At least three non-collinear points.

### **Length** — Extrusion length of beam 10 `m` (default) | positive scalar

The beam's length. The beam is modeled by extruding the specified
cross-section along the *z*-axis of the local reference
frame. The extrusion is symmetric about the *xy*-plane,
with half of the beam being extruded in the negative direction of the
*z*-axis and half in the positive direction.

### Stiffness and Inertia

### **Type** — Method to use to specify stiffness and inertia properties `Calculate from Geometry` (default) | `Custom`

Method to use to specify the stiffness and inertia properties, specified as `Calculate from Geometry` or `Custom`.

When you set the parameter to `Calculate from Geometry`, the block
calculates the stiffness and inertia properties based on the specified density,
Young’s modulus, and Poisson’s ratio or shear modulus. Set the parameter to
`Custom` to manually specify the stiffness and
inertia properties.

### **Density** — Mass per unit volume of material 2700 `kg/m^3` (default) | positive scalar

Mass per unit volume of material—assumed here to be distributed uniformly throughout
the beam. The default value corresponds to aluminum.

#### Dependencies

To enable this parameter, under the **Stiffness and Inertia**
section, set **Type** parameter to `Calculate from
Geometry`.

### **Specify** — Elastic properties in terms of which to parameterize the beam `Young's Modulus and Poisson's Ratio` (default) | `Young's and Shear Modulus`

Elastic properties in terms of which to parameterize the beam. These properties are
commonly available from materials databases.

#### Dependencies

To enable this parameter, under the **Stiffness and Inertia**
section, set **Type** parameter to `Calculate from
Geometry`.

### **Young's Modulus** — Ratio of axial stress to axial strain 70 `GPa` (default) | positive scalar

Young's modulus of elasticity of the beam. The greater its value, the stronger the
resistance to bending and axial deformation. The default value corresponds to
aluminum.

#### Dependencies

To enable this parameter, under the **Stiffness and Inertia**
section, set **Type** parameter to `Calculate from
Geometry`.

### **Poisson's Ratio** — Ratio of transverse to longitudinal strains 0.33 (default) | scalar in the range [0, 0.5)

Poisson's ratio of the beam. The value specified must be greater than or equal to
`0` and smaller than `0.5`. The default value
corresponds to aluminum.

#### Dependencies

To enable this parameter, under the **Stiffness and Inertia**
section, set **Type** parameter to `Calculate from
Geometry` and set the **Specify** parameter to
**Young's Modulus and Poisson's Ratio**.

### **Shear Modulus** — Ratio of shear stress to engineering shear strain 26 `GPa` (default) | positive scalar

Shear modulus (or modulus of rigidity) of the beam. The greater its value, the
stronger the resistance to torsional deformation. The default value corresponds to
aluminum.

#### Dependencies

To enable this parameter, under the **Stiffness and Inertia**
section, set **Type** parameter to `Calculate from
Geometry` and set the **Specify** parameter to
**Young's and Shear Modulus**.

### **Derived Values** — Calculated values of mass and stiffness sectional properties button

Calculated values of the mass and stiffness sectional properties of the beam. Click
**Update** to calculate and display those values.

The properties given include **Centroid** and **Shear
Center**. The centroid is the point at which an axial force extends (or
contracts) the beam without bending. The shear center is that through which a transverse
force must pass to bend the beam without twisting.

The stiffness sectional properties are computed as follows:

- **Axial Rigidity**: *E**A*
- **Flexural Rigidity**: [*E**I*x,
  *E**I*y]
- **Cross Flexural Rigidity**: *E**I*xy
- **Torsional Rigidity**: *G**J*

The mass sectional properties are computed as follows:

- **Mass per Unit Length**: *ρ**A*
- **Mass Moment of Inertia Density**: [*ρ**I*x,
  *ρ**I*y]
- **Mass Product of Inertia Density**: *ρ**I*xy
- **Polar Mass Moment of Inertia Density**: *ρ**I*p

The equation parameters include:

- *A* — Cross-sectional area
- *ρ* — Density
- *E* — Young's modulus
- *G* — Shear modulus
- *J* — Torsional constant (obtained from the solution of
  Saint-Venant's warping partial differential equation)

The remaining parameters are the relevant moments of area of the beam.
These are calculated about the axes of a centroidal frame—one aligned with the local
reference frame but located with its origin at the centroid. The moments of area are:

- *I*x,
  *I*y — Centroidal second moments
  of area:

  [Ix,Iy]=[∫A(y−yc)2dA,∫A(x−xc)2dA],
- *I*xy — Centroidal product moment
  of area:

  Ixy=∫A(x−xc)(y−yc)dA,
- *I*p — Centroidal polar moment of
  area:

  IP=Ix+Iy,

where *x*c and
*y*c are the coordinates of the
centroid.

### **Geometric Centroid** — Centroid of beam cross section [0 0] `m` (default) | 2-by-1 array

Centroid of the beam cross section, specified as a 2-by-1 array. The array specifies the *x* and *y* coordinates of the centroid with respect to the beam reference frame.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Bending Centroid** — Intersection of neutral axis and cross section [0 0] `m` (default) | 2-by-1 array

Intersection of the neutral axis and cross section, specified as a 2-by-1 array. The array specifies the *x* and *y* coordinates of the centroid with respect to the beam reference frame.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Shear Center** — Beam shear center [0 0] `m` (default) | 2-by-1 array

Beam shear center, specified as a 2-by-1 array. The array specifies the *x* and *y* coordinates of the point with respect to the beam reference frame.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Axial Rigidity** — Resistance against axial deformation 1 `Pa*m^2` (default) | scalar

Resistance against the deformation along the beam longitudinal direction, specified as a scalar. This parameter specifies the Sb element of the stiffness matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Flexural Rigidity** — Resistance against bending deformations [1 1] `Pa*m^4` (default) | 2-by-1 array

Resistance against bending deformations, specified as a 2-by-1 array. The array specifies the Hxb and Hyb elements of the stiffness matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Cross Flexural Rigidity** — Resistance against bending deformation about x-axis in response to bending moment about the y-axis 0 `Pa*m^4` (default) | scalar

Resistance against the bending deformation about the *x*-axis in response to bending moment about the *y*-axis, specified as a scalar. This parameter specifies the Hxyb element of the stiffness matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Torsional Rigidity** — Resistance against twisting 1 `Pa*m^4` (default) | scalar

Resistance against twisting about the longitudinal axis of the beam, specified as a scalar.
This parameter specifies the Hzb element of the stiffness matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Center of Mass** — Center of Mass [0 0] `m` (default) | 2-by-1 array

Center of mass, specified as a 2-by-1 array. The array specifies the
*x* and *y* coordinates of the point
with respect to the beam reference frame.

#### Dependencies

To enable this parameter, in the **Stiffness and
Inertia** section, set **Type** to
`Custom`.

### **Mass Per Unit Length** — Mass per unit length 1 `kg/m` (default) | scalar

Mass per unit length, specified as a scalar. This parameter specifies the mc element of the mass matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and Inertia** section, set **Type** to `Custom`.

### **Mass Moment of Inertia Density** — Resistance against rotation about `x` and `y` axes [1 1] `kg*m` (default) | 2-by-1 array

Resistance against rotation about the *x* and
*y* axes, specified as a 2-by-1 array. The array
specifies the ixc and iyc elements of the mass matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and
Inertia** section, set **Type** to
`Custom`.

### **Mass Product of Inertia Density** — Resistance against rotation about `x`-axis due to moment about `y`-axis 0 `kg*m` (default) | scalar

Resistance against rotation about the *x*-axis due to the
moment about the *y*-axis, specified as a scalar. This
parameter specifies the ixyc element of the mass matrix.

#### Dependencies

To enable this parameter, in the **Stiffness and
Inertia** section, set **Type** to
`Custom`.

### Damping

### **Type** — Type of damping method `Proportional` (default) | `Uniform Modal` | `None`

Damping method to apply to the beam:

- Select `None` to model undamped beams.
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
  vibration modes of the beam. The larger the value, the faster vibrations
  decay.

  The chosen reference conditions impact the types of modes to which the
  damping ratio applies. For details on reference conditions, see Reference Conditions. When you
  use modal reduction for the flexible body, only a subset of modes is
  retained. For details on modal reduction, see Reduce the Degrees of Freedom for a Flexible Body.

### **Mass Coefficient** — Coefficient of mass matrix 0 `1/s` (default) | nonnegative scalar

Coefficient, *α*, of the mass matrix. This parameter defines damping
proportional to the mass matrix [*M*].

#### Dependencies

To enable this parameter, set **Type** to
`Proportional`.

### **Stiffness Coefficient** — Coefficient of stiffness matrix 0.001 `s` (default) | nonnegative scalar

Coefficient, *β*, of the stiffness matrix. This parameter defines
damping proportional to the stiffness matrix [*K*].

#### Dependencies

To enable this parameter, set **Type** to
`Proportional`.

### **Damping Ratio** — Damping ratio for uniform modal damping method 0.01 (default) | unitless nonnegative scalar

Damping ratio, *ζ*, applied to all beam vibration modes in the
uniform modal damping model. The larger the value, the faster beam vibrations
decay.

When *ζ* = 0, the beam is undamped. If the boundary conditions applied to the beam
exactly match the chosen reference conditions, *ζ* < 1 yields underdamped modal decay, *ζ* = 1 corresponds to critical damping, and *ζ* > 1 yields overdamped dissipation. When the boundary conditions and
reference conditions do not match, the effect of the chosen damping ratio varies. For
details of reference condition, see Reference Conditions.

#### Dependencies

To enable this parameter, set **Type** to `Uniform
Modal`.

### Discretization

### **Number of Elements** — Number of beam finite elements 1 (default) | positive integer

Number of finite elements in the beam model. Increasing the number of elements always
improves accuracy of the simulation. But practically, at some point, the increase in
accuracy is negligible when there are many elements. Additionally, a higher number of
elements increases the computational cost and slows down the speed of the
simulation.

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
`None` or `Modally
Reduced`. Set the parameter to `None`
to use full nodal elastic coordinates generated by the finite-element method or
set the parameter to `Modally Reduced` to use the modal
transformation method to reduce the elastic coordinates of the body. For both
settings, the block uses the floating frame of the reference formulation [1-2]
to couple the body with its elastic deformation.

### **Number of Retained Modes** — Retained modes 1 (default) | nonnegative integer

Retained modes, specified as an integer in range [0, *n*], where
*n* is the number of elastic degrees of freedom of the
body. If you set the number to 0 the flexible body is treated as a rigid
body.

#### Dependencies

To enable this parameter, set **Reduction** to `Modally
Reduced`.

### Graphic

### **Type** — Graphic to use in the visualization of beam `From Geometry` (default) | `None`

Type of the visual representation of the beam, specified as `From Geometry` or `None`. Set the parameter to `From Geometry` to show the visual representation of the beam. Set the parameter to `None` to hide the beam in the model visualization.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select `Simple` to specify **Color** and **Opacity**. Select `Advanced` to specify more visual properties, such as **Specular Color**, **Ambient Color**, **Emissive Color**, and **Shininess**.

#### Dependencies

To enable this parameter, set **Type** to `From Geometry`.

### **Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the graphic under direct white light, specified as an [R G B] or [R G B A] vector on a 0–1 scale. An optional fourth element (A) specifies the color opacity on a scale of 0–1. Omitting the opacity element is equivalent to specifying a value of 1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Simple`

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0 corresponds to completely transparent, and a scalar of 1 corresponds to completely opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Simple`

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B] or [R,G,B,A] vector with values in the range of 0 to 1. The vector can be a row or column vector. The optional fourth element specifies the color opacity. Omitting the opacity element is equivalent to specifying a value of 1.

The diffuse color reflects the main color of the rendered beam and provides shading that gives the rendered object a three-dimensional appearance.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Advanced`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B] or [R,G,B,A] vector with values in the range of 0 to 1. The vector can be a row or column vector. The optional fourth element specifies the color opacity. Omitting the opacity element is equivalent to specifying a value of 1. This parameter changes the color of the specular highlight, which is the bright spot on the rendered beam due to the reflection of the light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Advanced`

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A] vector with values in the range of 0 to 1. The vector can be a row or column vector. The optional fourth element specifies the color opacity. Omitting the opacity element is equivalent to specifying a value of 1.

Ambient light refers to a general level of illumination that does not come directly from a
light source. The ambient light is light that has been reflected and
re-reflected so many times that it is no longer coming from any particular
direction. You can adjust this parameter to change the shadow color of the
rendered beam.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector in the range of 0 to 1. The vector can be a row or column vector. The optional fourth element specifies the color opacity. Omitting the opacity element is equivalent to specifying a value of 1.

The emission color is color that does not come from any external source,
and therefore seems to be emitted by the
beam itself. When a beam has an emissive
color, the beam can be seen even if
there is no external light
source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of the specular light reflections, specified as a scalar number on a 0–128 scale.
Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry`
2. **Visual Properties** to `Advanced`

### Frames

### **Show Port A** — Show port A for connection to other blocks on (default) | off

Select to expose the **A** port.

### **Show Port B** — Show port B for connection to other blocks on (default) | off

Select to expose the **B** port.

### **New Frame** — Create custom frame for connection to other blocks button

Click the Create button Create to open a pane for creating a new
body-attached frame. In this pane, you can specify the name, origin, and
orientation for the frame.

- To name the custom frame, click the text field of the
  **Frame Name** parameter. The name identifies
  the corresponding port on the beam block and in the tree view pane
  of the Multibody Explorer.
- To select the **Frame Origin** for the custom
  frame, use one of the following methods:

  - **At Reference Frame Origin**: Make
    the new frame origin coincident with the origin of the
    reference frame of the undeformed beam.
  - **Based on Geometric Feature**: Make
    the new frame origin coincident with the center of the
    selected undeformed geometry feature. Valid features
    include surfaces, lines, and points. Select a feature
    from the visualization pane, then click **Use
    Selected Feature** to confirm the location
    of the origin. The name of the origin location appears
    in the field below this option.
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
    Selects an axis of the reference frame of the undeformed
    beam.
  - **Based on Geometric Feature**:
    Selects the vector associated with the chosen geometry
    feature of the undeformed beam. Valid features include
    surfaces and lines. The corresponding vector is
    indicated by a white arrow in the visualization pane.
    You can select a feature from the visualization pane and
    then click **Use Selected Feature** to
    confirm the selection. The name of the selected feature
    appears in the field below this option.

### **FrameN** — Edit or delete existing custom frame frame name

Frames that you have created. `N` is a unique identifying
number for each custom frame.

- Click the text field to edit the name of an existing custom
  frame.

- Click the Edit button Edit to edit other aspects of the
  custom frame, such as origin and axes.
- Click the Delete button Delete to delete the custom
  frame.

#### Dependencies

To enable this parameter, create a frame by clicking **New
Frame**.

## Libraries

Simscape / Multibody / Body Elements / Flexible Bodies / Beams

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Slender extrusion with elastic properties for deformation

The General Flexible Beam block models a slender beam
of constant, general cross-section that can have small and linear deformations. These
deformations include extension, bending, and torsion. The block calculates the beam
cross-sectional properties, such as the axial, flexural, and torsional rigidities, based
on the geometry and material properties that you specify.

The geometry of the flexible beam is an extrusion of its cross-section. The beam
cross-section, defined in the *xy*-plane, is extruded
along the *z*-axis. You can use this block to create
flexible beams with simply or multiply connected cross-sections. For example, you can
create the beam shown in the figure by entering these values for the **Cross-section** in the block's dialog box:
`{[-0.25,-0.50;0.25,-0.50;0.25,0.50;-0.25,0.50],[-0.15,-0.40;0.15,-0.40;0.15,-0.05;-0.15,-0.05],[-0.15,0.05;0.15,0.05;0.15,0.40;-0.15,0.40]}`.

For more information on modeling flexible beams, see Overview of Flexible Beams.
