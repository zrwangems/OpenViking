---
type: simulink-block
title: 'Inertia Sensor'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'inertiasensor'
documentation_source_path: 'ref/inertiasensor.html'
language: en
---

# Inertia Sensor

## Ports

### Input

### **S** — Sensor port frame

Sensor port to attach to a frame in the model. Use this port to determine which
body group or mechanism is measured.

### **M** — Custom measurement frame port frame

When `Custom` is selected, a second port, M, appears on
the Inertia Sensor block. The Inertia Sensor block measures inertial properties
relative to the frame connected to the M port.

#### Dependencies

To enable this port, set the **Measurement Frame** parameter to
`Custom`.
### Output

### **m** — Mass scalar

Total mass for the collection of body elements.

#### Dependencies

To enable this port, select the **Mass** check box.

### **com** — Center of Mass vector

The center of mass for the collection of body elements.

#### Dependencies

To enable this port, select the **Center of Mass** check
box.

### **I** — Inertia Matrix matrix

The inertia matrix for the collection of body elements.

#### Dependencies

To enable this port, select the **Inertia Matrix** check
box.

### **Ic** — Centered Inertia Matrix matrix

The centered inertia matrix for the collection of body elements.

#### Dependencies

To enable this port, select the **Centered Inertia Matrix**
check box.

### **Ip** — Principal Inertia Matrix matrix

The principal inertia matrix for the collection of body elements.

#### Dependencies

To enable this port, select the **Principal Inertia Matrix**
check box.

### **R** — Rotation Matrix matrix

The rotation matrix for orientation of principal inertia frame relative to
measurement frame.

#### Dependencies

To enable this port, select the **Rotation Matrix** check
box.

## Parameters

### Sensor Extent

### **Sensor Extent** — Determine the extent that the Inertia Sensor block measures `Body Group` (default) | `Mechanism`

Extent that the Inertia Sensor block measures, defined as Body Group or
Mechanism.

`Body Group`
:   When `Body Group` is selected, the
    Inertia Sensor block measures inertial
    properties for the collection of body elements that are connected to each
    other directly or through rigid transforms. This includes solid, inertia,
    variable mass, or flexible bodies.

`Mechanism`
:   When `Mechanism` is selected, the
    Inertia Sensor block measures inertial
    properties for all connected body elements within the model.

### **Sensor Extent: Span Weld Joints** — Include bodies connected by weld joints in a body group `cleared` (default) | checked

If selected, this option causes body groups to include body elements that are
connected via a weld joint.

#### Dependencies

To enable this option, set **Sensor Extent** to
`Body Group`.

### **Sensor Extent: Exclude Grounded Bodies** — Do not measure inertial properties of grounded bodies `cleared` (default) | checked

If selected, this option causes the Inertia Sensor
block to measure inertial properties for the collection of body elements connected to
the same mechanism as the Inertia Sensor block
excluding any grounded bodies.

#### Dependencies

To enable this option, set **Sensor Extent** to
`Mechanism`.

### **Measurement Frame** — Determine the frame that the Inertia Sensor block uses for measurements `Attached` (default) | `World` | `Custom`

The measurement frame specifies the frame the sensor uses to measure the center of
mass, inertia matrix, and centered inertia matrix.

`Attached`
:   When `Attached` is selected, the
    Inertia Sensor block measures inertial
    properties relative to the same frame that is connected to the S port.

`World`
:   When `World` is selected, the
    Inertia Sensor block measures inertial
    properties relative to the World Frame.

`Custom`
:   When `Custom` is selected, the M port is exposed.
    The Inertia Sensor block measures inertial properties relative to the frame
    connected to the M port.

### **Mass** — Total mass of measured bodies `cleared` (default) | checked

Select the **Mass** check box to measure the mass of the
collection of body elements.

### **Center of Mass** — Center of mass coordinates `cleared` (default) | checked

Select the **Center of Mass** check box to measure the
center of mass of the collection of body elements, output as a 3-by-1 vector relative
to the measurement frame. If the mass of the measured body group or mechanism is zero,
the center of mass is undefined and a runtime error occurs.

### **Inertia Matrix** — Measurement of the inertia tensor `cleared` (default) | checked

Select the **Inertia Matrix** check box to measure the
inertia tensor of the collection of body elements, output as a 3-by-3 matrix relative
to the measurement frame.

### **Centered Inertia Matrix** — Measurement of the inertia tensor relative to the centered frame `cleared` (default) | checked

Select the **Centered Inertia Matrix** check box to measure
the inertia tensor of the collection of body elements, output as a 3-by-3 matrix
relative to the centered frame. The centered frame is a frame whose origin coincides
with the center of mass and whose axes are aligned with those of the measurement
frame. If the mass of the measured body group or mechanism is zero, the centered
inertia matrix is undefined and a runtime error occurs.

### **Principal Inertia Matrix** — Measurement of the inertia tensor with respect to the principal inertia frame `cleared` (default) | checked

Select the **Principal Inertia Matrix** check box to
measure the inertia tensor of the collection of body elements, output as a 3-by-3
matrix with respect to the principal inertia frame. The principal inertia matrix is a
diagonal matrix.

The principal inertia frame is a frame with an origin that coincides with the
center of mass and axes that are aligned with the principal axes of inertia. If the
mass of the measured body group or mechanism is zero, the principal inertia matrix is
undefined and a runtime error occurs.

### **Rotation Matrix** — Orientation of the principal inertia frame `cleared` (default) | checked

Select the **Rotation Matrix** check box to measure the
orientation of the principal axes of inertia with respect to the measurement frame as
a 3-by-3 matrix. In other words, the rotation matrix maps vectors in the principal
inertia frame to the vectors in the measurement frame.

If the mass of the measured body group or mechanism is zero, the rotation matrix
is undefined and a runtime error occurs.

### Graphic

### **Type** — Sensor visualization setting `Principal Inertia Frame` (default) | `Equivalent Inertia Ellipsoid` | `None`

Display of the inertial properties for the sensed collection of body elements,
specified as `Principal Inertia Frame`,
`Equivalent Inertia Ellipsoid`, or
`None`.

Set the parameter to `Principal Inertia Frame` to
represent the sensed inertial properties as the principal inertia frame. The principal
inertia frame is a frame with an origin that coincides with the center of mass and
axes that are aligned with the principal axes of inertia.

Set the parameter to `Equivalent Inertia Ellipsoid` to
represent the inertia properties as an ellipsoid that has the same mass, moments, and
products of inertia as the group of bodies being sensed.

Set the parameter to `None` to hide the visualization of
the sensed inertia properties.

### **Size** — Display size for the principal inertia frame 20 `pixels` (default) | positive scalar

Display size for the principal inertia frame, specified as a positive
scalar.

#### Dependencies

To enable this parameter, set **Type** to
`Principal Inertia Frame`.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify **Diffuse Color** and
**Opacity**. Select `Advanced` to specify
more visual properties, such as **Specular Color**, **Ambient
Color**, **Emissive Color**, and
**Shininess**.

#### Dependencies

To enable this parameter, set **Type** to
`Principal Inertia Frame` or `Equivalent
Inertia Ellipsoid`.

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector.
The optional fourth element specifies the color opacity. Omitting the opacity element
is equivalent to specifying a value of 1.

The diffuse color reflects the main color of the graphic and provides shading that
gives the rendered object a three-dimensional appearance.

#### Dependencies

To enable this parameter, set **Type** to
`Principal Inertia Frame` or `Equivalent
Inertia Ellipsoid`.

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0
corresponds to completely transparent, and a scalar of 1 corresponds to completely
opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Principal Inertia
   Frame` or `Equivalent Inertia
   Ellipsoid`
2. **Visual Properties** to
   `Simple`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B] or
[R,G,B,A] vector with values in the range of 0 to 1. The vector can be a row or column
vector. The optional fourth element specifies the color opacity. Omitting the opacity
element is equivalent to specifying a value of 1. This parameter changes the color of
the specular highlight, which is the bright spot on the graphic due to the reflection
of the light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Principal Inertia
   Frame` or `Equivalent Inertia
   Ellipsoid`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A] vector with
values in the range of 0 to 1. The vector can be a row or column vector. The optional
fourth element specifies the color opacity. Omitting the opacity element is equivalent
to specifying a value of 1.

Ambient light refers to a general level of illumination that does not come
directly from a light source. The Ambient light consists of light that has been
reflected and re-reflected so many times that it is no longer coming from any
particular direction. You can adjust this parameter to change the shadow color of the
graphic.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Principal Inertia
   Frame` or `Equivalent Inertia
   Ellipsoid`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector in the
range of 0 to 1. The vector can be a row or column vector. The optional fourth element
specifies the color opacity. Omitting the opacity element is equivalent to specifying
a value of 1.

The emission color is color that does not come from any
external source, and therefore seems to be emitted by the graphic
itself. When a graphic has an emissive color, the graphic can be
seen even if there is no external light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Principal Inertia
   Frame` or `Equivalent Inertia
   Ellipsoid`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Principal Inertia
   Frame` or `Equivalent Inertia
   Ellipsoid`
2. **Visual Properties** to
   `Advanced`

## Libraries

Simscape / Multibody / Body Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Sensor to measure the inertial properties of body groups or mechanisms

Use the Inertia Sensor block to measure the inertial
properties for collections of body elements in the Simscape Multibody model. Parameters that
the Inertia Sensor block can measure include:

- Mass
- Center of mass
- Inertia matrix
- Centered inertia matrix
- Principal inertia matrix
- Orientation of principal inertia frame

A body group is the set of all body elements that are connected to each other directly or
through rigid transforms. The body group may include solid blocks, inertia blocks, variable
mass blocks, or flexible body blocks. By default, two body elements that are connected by a
joint block are not considered to be a part of the same body group.

A mechanism is the set of all connected body elements within the model. With mechanisms,
you can choose to exclude grounded bodies by enabling the **Exclude Grounded
Bodies** parameter. A grounded body is any rigid body that is rigidly connected to
a World Frame block.
