---
type: simulink-block
title: 'Collision Cylinder'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisioncylinderblock'
documentation_source_path: 'ref/collisioncylinderblock.html'
language: en
---

# Collision Cylinder

## Ports

### Input

### **Radius** — Radius of cylinder scalar

Radius of the cylinder, specified as a positive scalar. Units are in
meters.

### **Length** — Length of cylinder scalar

Length of the cylinder, specified as a nonnegative scalar. Units are in
meters.

### **Pose** — Pose of collision geometry matrix

Pose of the collision geometry relative to the world frame, specified as a 4-by-4 homogeneous matrix.
### Output

### **CollGeom** — Collision geometry bus

Collision geometry, returned as a bus.

To perform collision checking, connect this output to a Check Collision block as input.

### **ExitFlag** — Validity of collision cylinder dimensions scalar

Validity of collision cylinder dimensions, returned as an integer scalar where
each digit represents the validity of a dimension:

- **First Digit** — Validity of the radius at the
  **Radius** port.
- **Second Digit** — Validity of the length at
  the **Length** port.

Each of these digits can be one of these values:

- `4` — Specified dimension value is not numeric.
- `3` — Specified dimension value is not a real number.
- `2` — Specified dimension value is nonfinite.
- `1` — Specified radius is not positive, or the specified length is
  negative.
- `0` — Specified dimension value is valid.

For example, if the exit flag is `10`, then the radius
of the cylinder is invalid because it is not positive.

To validate dimensions at runtime instead, select the **Enable Runtime
Input Dimensions Error** parameter.

**Data Types:** `uint16`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Enable Runtime Input Dimensions Error** — Validation of collision cylinder dimensions `on` (default) | `off`

Select this parameter to enable runtime validation of the collision cylinder
dimensions and return an error if either **Radius** or **Length** is
invalid.

If you clear this parameter, the block does not error during simulation, and instead
uses the **ExitFlag** port to identify invalid cylinder dimensions.

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

Collision Cylinder block supports code generation with
dynamic memory allocation disabled. For more information about disabling dynamic memory
allocation, see Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2025a**

## Description

Create cylinder collision geometry

The Collision Cylinder block outputs a cylinder collision geometry that is
axis-aligned with the *z*-axis of its body-fixed frame and
has the origin of the body-fixed frame at the center of the cylinder.
