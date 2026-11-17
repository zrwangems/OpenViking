---
type: simulink-block
title: 'Collision Sphere'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisionsphereblock'
documentation_source_path: 'ref/collisionsphereblock.html'
language: en
---

# Collision Sphere

## Ports
```yaml
ports:
- name: Radius
  summary: Radius of sphere scalar
  direction: input
- name: Pose
  summary: Pose of collision geometry matrix
  direction: input
- name: CollGeom
  summary: Collision geometry bus
  direction: output
- name: ExitFlag
  summary: Validity of collision sphere radius scalar
  direction: output
  data_types: uint16
```

### Input

### **Radius** — Radius of sphere scalar

Radius of the sphere, specified as a positive scalar. Units are in meters.

### **Pose** — Pose of collision geometry matrix

Pose of the collision geometry relative to the world frame, specified as a 4-by-4 homogeneous matrix.
### Output

### **CollGeom** — Collision geometry bus

Collision geometry, returned as a bus.

To perform collision checking, connect this output to a Check Collision block as input.

### **ExitFlag** — Validity of collision sphere radius scalar

Validity of collision sphere radius, returned as an integer scalar:

- `4` — Specified dimension value is not numeric.
- `3` — Specified dimension value is not a real number.
- `2` — Specified dimension value is nonfinite.
- `1` — Specified dimension value is not positive.
- `0` — Specified dimension value is valid.

To validate the radius at runtime instead, select the **Enable Runtime
Input Dimensions Error** parameter.

**Data Types:** `uint16`
## Parameters
```yaml
parameters:
- name: Enable Runtime Input Dimensions Error
  summary: Validation of collision sphere dimensions on (default) | off
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Enable Runtime Input Dimensions Error** — Validation of collision sphere dimensions `on` (default) | `off`

Select this parameter to enable runtime validation of the collision sphere
dimensions and error during simulation if **Radius** is invalid.

If you clear this parameter, the block does not error during simulation, and instead
uses the **ExitFlag** port to identify if the radius is invalid.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The block reuses the C code for
  subsequent simulations, as long as the model does not change.
- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. For more information, see Interpreted Execution vs. Code Generation (Simulink).
## Libraries

Robotics System Toolbox / Collision Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Collision Sphere block supports code generation with
dynamic memory allocation disabled. For more information about disabling dynamic memory
allocation, see Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2025a**

## Description

Create sphere collision geometry

The Collision Sphere block outputs a sphere collision geometry with the origin
of the geometry-fixed frame at the center of the sphere.
