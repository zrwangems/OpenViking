---
type: simulink-block
title: 'Collision Capsule'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisioncapsuleblock'
documentation_source_path: 'ref/collisioncapsuleblock.html'
language: en
---

# Collision Capsule

## Ports

### Input

### **Radius** — Radius of spherical ends of capsule scalar

Radius of the spherical ends of the capsule, specified as a positive scalar. Units
are in meters.

### **Length** — Length of central line segment of capsule scalar

Length of the central line segment of the capsule, specified as a nonnegative
scalar. Units are in meters.

**Note**

This is not the length from end-to-end of the capsule. The total length of the
capsule is `Length + 2*Radius`.

### **Pose** — Pose of collision geometry matrix

Pose of the collision geometry relative to the world frame, specified as a 4-by-4 homogeneous matrix.
### Output

### **CollGeom** — Collision geometry bus

Collision geometry, returned as a bus.

To perform collision checking, connect this output to a Check Collision block as input.

### **ExitFlag** — Validity of collision capsule dimensions scalar

Validity of collision capsule dimensions, returned as an integer scalar where each
digit represents the validity of a dimension:

- **First Digit** — Validity of the radius at
  **Radius** port.
- **Second Digit** — Validity of the length at
  **Length** port.

Each of these digits can be one of these values:

- `4` — Specified dimension value is not numeric.
- `3` — Specified dimension value is not a real number.
- `2` — Specified dimension value is nonfinite.
- `1` — Specified radius is not positive, or the specified length is
  negative.
- `0` — Specified dimension value is valid.

For example, if the exit flag is `10`, then the radius
of the capsule is invalid because it is not positive.

To validate dimensions at runtime instead, select the **Enable Runtime
Input Dimensions Error** parameter.

**Data Types:** `uint16`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Enable Runtime Input Dimensions Error** — Validation of collision capsule dimensions `on` (default) | `off`

Select this parameter to enable runtime validation of the collision capsule
dimensions and return an error if either **Radius** or **Length** is
invalid.

If you clear this parameter, the block does not error during simulation, and instead
uses the **ExitFlag** port to identify invalid capsule dimensions.

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

Collision Capsule block supports code generation with
dynamic memory allocation disabled. For more information about disabling dynamic memory
allocation, see Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2025a**

## Description

Create capsule collision geometry

The Collision Capsule block outputs a capsule primitive collision geometry
defined by a radius and length, with the central line segment of the capsule aligning with its
*z*-axis. The origin of the body-fixed frame is located at
the midpoint of the central line segment.
