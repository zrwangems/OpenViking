---
type: simulink-block
title: 'Coordinate Transformation Conversion'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'coordinatetransformationconversion'
documentation_source_path: 'ref/coordinatetransformationconversion.html'
language: en
---

# Coordinate Transformation Conversion

## Ports
```yaml
ports:
- name: Input transformation
  summary: Coordinate transformation column vector | 3-by-3 matrix | 4-by-4 matrix
  direction: input
- name: TrVec
  summary: Translation vector 3-element column vector
  direction: input
- name: Output transformation
  summary: Coordinate transformation column vector | 3-by-3 matrix | 4-by-4 matrix
  direction: input
- name: TrVec
  summary: Translation vector three-element column vector
  direction: input
```

### Input

### **Input transformation** — Coordinate transformation column vector | 3-by-3 matrix | 4-by-4 matrix

Input transformation, specified as a coordinate transformation. The
following representations are supported:

- Axis-Angle (`AxAng`) – `[x y z
  theta]`
- Euler Angles (`Eul`) – Three-element
  vector. For example `[z y x]`.
- Homogeneous Transformation (`TForm`) –
  4-by-4 matrix
- Quaternion (`Quat`) – `[w x y
  z]`
- Rotation Matrix (`RotM`) – 3-by-3
  matrix
- Translation Vector (`TrVec`) –
  `[x y z]`

All vectors must be **column
vectors**.

To accommodate representations that only contain position or
orientation information (`TrVec` or
`Eul`, for example), you can specify two inputs or
outputs to handle all transformation information. When you select the
Homogeneous Transformation as an input or output, the optional
**Show TrVec input port** or **Show
TrVec output port** parameters can be selected on the
block mask to toggle the multiple ports.

### **TrVec** — Translation vector 3-element column vector

Translation vector, specified as a 3-element column vector,
`[x y z]`, which corresponds to a translation in
the *x*, *y*, and
*z* axes respectively. This port can be used to
input or output the translation information separately from the rotation
vector.

#### Dependencies

You must select `Homogeneous Transformation` for
the output **Representation** parameter to get
the option to show the additional **TrVec** input port.
Enable the port by clicking **Show TrVec input
port**.
### Output Arguments

### **Output transformation** — Coordinate transformation column vector | 3-by-3 matrix | 4-by-4 matrix

Output transformation, returned as a coordinate transformation with
the specified representation. The following representations are
supported:

- Axis-Angle (`AxAng`) – `[x y z
  theta]`
- Euler Angles (`Eul`) – Three-element
  vector. For example `[z y x]`.
- Homogeneous Transformation (`TForm`) –
  4-by-4 matrix
- Quaternion (`Quat`) – `[w x y
  z]`
- Rotation Matrix (`RotM`) – 3-by-3
  matrix
- Translation Vector (`TrVec`) –
  `[x y z]`

To accommodate representations that only contain position or
orientation information (`TrVec` or
`Eul`, for example), you can specify two inputs or
outputs to handle all transformation information. When you select
`Homogeneous Transformation` as an input or output,
the optional **Show TrVec input port** or
**Show TrVec output port** parameters can be
selected on the block mask to toggle the multiple ports.

### **TrVec** — Translation vector three-element column vector

Translation vector, returned as a three-element column vector,
`[x y z]`, which corresponds to a translation in
the *x*, *y*, and *z*
axes respectively. This port can be used to input or output the
translation information separately from the rotation vector.

#### Dependencies

You must select `Homogeneous Transformation` for
the input **Representation** parameter to get the
option to show the additional **TrVec** output port. Enable
the port by clicking **Show TrVec output
port**.
## Parameters
```yaml
parameters:
- name: Representation
  summary: Input representation Axis-Angle | Euler Angles | Homogeneous Transformation | Quaternion | Rotation Matrix | Translation
    Vector
  group: ''
- name: Axis rotation sequence
  summary: Order of Euler angle axis rotations ZYX (default) | ZYZ | XYZ
  group: ''
- name: Show TrVec input port
  summary: Toggle TrVec port off (default) | on
  group: ''
- name: Representation
  summary: Output representation Axis-Angle | Euler Angles | Homogeneous Transformation | Quaternion | Rotation Matrix | Translation
    Vector
  group: ''
- name: Axis rotation sequence
  summary: Order of Euler angle axis rotations ZYX (default) | ZYZ | XYZ
  group: ''
- name: Show TrVec output port
  summary: Toggle TrVec port off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

#### Input

### **Representation** — Input representation `Axis-Angle` | `Euler Angles` | `Homogeneous Transformation` | `Quaternion` | `Rotation Matrix` | `Translation Vector`

Select the representation for the input port for the block. If you are
using a transformation with only orientation information, you can also
select the **Show TrVec input port** or **Show
TrVec output port** when converting to or from a homogeneous
transformation.

### **Axis rotation sequence** — Order of Euler angle axis rotations `ZYX` (default) | `ZYZ` | `XYZ`

Order of the Euler angle axis rotations, specified as one of these string scalars:

- `ZYX` (default)
- `ZYZ`
- `ZXY`
- `ZXZ`
- `YXY`
- `YZX`
- `YXZ`
- `YZY`
- `XYX`
- `XYZ`
- `XZX`
- `XZY`

The order of the angles in the input port
`Eul` must match this rotation sequence. Each
character indicates the corresponding axis. For example, if the sequence is
`ZYX`, then the three specified Euler angles are
interpreted in order as a rotation around the *z*-axis, a
rotation around the *y*-axis, and a rotation around the
*x*-axis. When applying this rotation to a point, it
will apply the axis rotations in the order *x*, then
*y*, then *z*.

#### Dependencies

You must select `Euler Angles` for the input
**Representation** parameter. The axis rotation
sequence only applies to Euler angle rotations.

### **Show TrVec input port** — Toggle `TrVec` port off (default) | on

Toggle the **TrVec** input port when you want to specify a
separate translation vector for position information along with an
orientation representation.

#### Dependencies

You must select `Homogeneous Transformation` for the
output **Representation** parameter to get the option
to show the additional **TrVec** input port. Enable the port by
clicking **Show TrVec input port**.

#### Output

### **Representation** — Output representation `Axis-Angle` | `Euler Angles` | `Homogeneous Transformation` | `Quaternion` | `Rotation Matrix` | `Translation Vector`

Select the representation for the output port for the block. If you are
using a transformation with only orientation information, you can also
select the **Show TrVec input port** or **Show
TrVec output port** when converting to or from a homogeneous
transformation.

### **Axis rotation sequence** — Order of Euler angle axis rotations `ZYX` (default) | `ZYZ` | `XYZ`

Order of the Euler angle axis rotations, specified as one of these string scalars:

- `ZYX` (default)
- `ZYZ`
- `ZXY`
- `ZXZ`
- `YXY`
- `YZX`
- `YXZ`
- `YZY`
- `XYX`
- `XYZ`
- `XZX`
- `XZY`

The order of the angles in the output port
`Eul` must match this rotation sequence. Each
character indicates the corresponding axis. For example, if the sequence is
`ZYX`, then the three returned Euler angles are
interpreted in order as a rotation around the *z*-axis, a
rotation around the *y*-axis, and a rotation around the
*x*-axis. When applying this rotation to a point, it
will apply the axis rotations in the order *x*, then
*y*, then *z*.

#### Dependencies

You must select `Euler Angles` for the output
**Representation** parameter. The axis rotation
sequence only applies to Euler angle rotations.

### **Show TrVec output port** — Toggle `TrVec` port off (default) | on

Toggle the **TrVec** output port when you want to receive
a separate translation vector for position information along with an
orientation representation.

#### Dependencies

You must select `Homogeneous Transformation` for the
input **Representation** parameter to get the option
to show the additional **TrVec** output port. Enable the port
by clicking **Show TrVec output port**.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate
  model using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed than `Code
  generation`. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate model
  using generated C code. The first time you run a simulation,
  Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.

**Tunable:** No
## Libraries

Robotics System Toolbox / Utilities Navigation Toolbox / Utilities ROS Toolbox / Utilities UAV Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024b: Additional Euler sequence support

The Coordinate Transformation Conversion block supports additional Euler sequences for the
**Axis rotation sequence** parameter. These are all the
supported Euler sequences:

- `ZYX`
- `ZYZ`
- `ZXY`
- `ZXZ`
- `YXY`
- `YZX`
- `YXZ`
- `YZY`
- `XYX`
- `XYZ`
- `XZX`
- `XZY`

## Description

Convert to a specified coordinate transformation representation

The Coordinate Transformation Conversion block converts a coordinate
transformation from the input representation to a specified output representation. The
input and output representations use the following forms:

- Axis-Angle (`AxAng`) – `[x y z
  theta]`
- Euler Angles (`Eul`) – Three-element vector. For example
  `[z y x]`.
- Homogeneous Transformation (`TForm`) – 4-by-4
  matrix
- Quaternion (`Quat`) – `[w x y z]`
- Rotation Matrix (`RotM`) – 3-by-3 matrix
- Translation Vector (`TrVec`) – `[x y
  z]`

All vectors must be **column vectors**.

To accommodate representations that only contain position or orientation information
(`TrVec` or `Eul`, for example), you can specify
two inputs or outputs to handle all transformation information. When you select the
Homogeneous Transformation as an input or output, the optional **Show TrVec
input port** or **Show TrVec output port** parameters
can be selected on the block mask to toggle the multiple ports.
