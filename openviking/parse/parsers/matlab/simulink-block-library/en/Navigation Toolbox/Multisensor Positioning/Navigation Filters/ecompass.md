---
type: simulink-block
title: 'ecompass'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'ecompassblock'
documentation_source_path: 'ref/ecompassblock.html'
language: en
---

# ecompass

## Ports
```yaml
ports:
- name: Accel
  summary: Accelerometer readings *N*-by-3 matrix of real scalar
  direction: input
  data_types: single | double
- name: Mag
  summary: Magnetometer readings *N*-by-3 matrix of real scalar
  direction: input
  data_types: single | double
- name: Orientation
  summary: Orientation that rotates quantities from global coordinate system to sensor body coordinate system *N*-by-4 matrix
    of quaternions (default) | 3-by-3-by-*N* array
  direction: output
  data_types: single | double
```

### Input

### **Accel** — Accelerometer readings *N*-by-3 matrix of real scalar

Accelerometer readings in sensor body coordinate system in
m/s2, specified as an *N*-by-3 matrix of
real scalar. The columns of the matrix correspond to the *x*-,
*y*-, and *z*-axes of the sensor body. The rows in
the matrix, *N*, correspond to individual samples.

**Data Types:** `single` | `double`

### **Mag** — Magnetometer readings *N*-by-3 matrix of real scalar

Magnetometer readings in sensor body coordinate system in µT, specified as an
*N*-by-3 matrix. The columns of the matrix correspond to the
*x*-, *y*-, and *z*-axes of the
sensor body. The rows in the matrix, *N*, correspond to individual
samples.

**Data Types:** `single` | `double`
### Output

### **Orientation** — Orientation that rotates quantities from global coordinate system to sensor body coordinate system *N*-by-4 matrix of quaternions (default) | 3-by-3-by-*N* array

Orientation that can rotate quantities from a global coordinate system to a sensor
body coordinate system, returned as an *N*-by-4 matrix of quaternions
or 3-by-3-by-*N* array of rotation matrices. *N*
denotes the number of samples. Orientations are the rotation that takes a quantity
from the local navigation coordinate system to the body coordinate system.

- If the **Orientation format** is specified as
  `quaternion`, the block returns the orientation as an
  *N*-by-4 matrix of quaternions.
- If the **Orientation format** is specified as
  `Rotation matrix`, the block returns the orientation
  as an 3-by-3-by-*N* array of rotation matrices.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Reference frame
  summary: Navigation reference frame NED (default) | ENU
  group: ''
- name: Orientation format
  summary: Format used to describe orientation quaternion (default) | Rotation matrix
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Reference frame** — Navigation reference frame `NED` (default) | `ENU`

Navigation reference frame, specified as `NED` for North-East-Down
frame or `ENU` for East-North-Up frame.

### **Orientation format** — Format used to describe orientation `quaternion` (default) | `Rotation matrix`

Format used to describe orientation, specified as `'quaternion'` or
`'Rotation matrix'`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time that you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations if the model does not change. This option requires additional startup
  time.
## Libraries

Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters Navigation Toolbox / Multisensor Positioning / Navigation Filters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Compute orientation from accelerometer and magnetometer readings

The ecompass
Simulink® block computes orientation using accelerometer and magnetometer readings. You
can use the computed orientation to rotate quantities from global coordinate system to sensor
body coordinate system.
