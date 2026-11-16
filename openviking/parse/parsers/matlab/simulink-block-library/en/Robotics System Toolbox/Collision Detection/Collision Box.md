---
type: simulink-block
title: 'Collision Box'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisionboxblock'
documentation_source_path: 'ref/collisionboxblock.html'
language: en
---

# Collision Box

## Ports

### Input

### **X** — Length of box geometry along *x*-axis scalar

Side length of box geometry along the *x*-axis,
specified as a positive scalar. Units are in meters.

### **Y** — Length of box geometry along *y*-axis scalar

Side length of box geometry along the *y*-axis,
specified as a positive scalar. Units are in meters.

### **Z** — Length of box geometry along *z*-axis scalar

Side length of box geometry along the *z*-axis,
specified as a positive scalar. Units are in meters.

### **Pose** — Pose of collision geometry matrix

Pose of the collision geometry relative to the world frame, specified as a 4-by-4 homogeneous matrix.
### Output

### **CollGeom** — Collision geometry bus

Collision geometry, returned as a bus.

To perform collision checking, connect this output to a Check Collision block as input.

### **ExitFlag** — Validity of collision box dimensions scalar

Validity collision box dimensions, returned as an integer scalar where each digit
represents the validity of a dimension:

- **First Digit** — Validity of the
  *x*-axis length at the **X** port.
- **Second Digit** — Validity of the
  *y*-axis length at the **Y** port.
- **Third Digit** — Validity of the
  *z*-axis length at the **Z** port.

Each of these digits can be one of these values:

- `4` — Specified dimension value is not numeric.
- `3` — Specified dimension value is not a real number.
- `2` — Specified dimension value is nonfinite.
- `1` — Specified dimension value is not positive.
- `0` — Specified dimension value is valid.

For example, if the exit flag is `230`, then the
*x*-length of the box is nonfinite, the *y*-length
is not a real value, and the *z*-length is valid.

To validate dimensions at runtime instead, select the **Enable Runtime
Input Dimensions Error** parameter.

**Data Types:** `uint16`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Enable Runtime Input Dimensions Error** — Validation of collision box dimensions `on` (default) | `off`

Select this parameter to enable runtime validation of the collision box dimensions
and return an error if **X**, **Y**, or **Z** is
invalid.

If you clear this parameter, the block does not error during simulation, and instead
uses the **ExitFlag** port to identify invalid box dimensions.

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

Collision Box block supports code generation with
dynamic memory allocation disabled. For more information about disabling dynamic memory
allocation, see Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2025a**

## Description

Create box collision geometry

The Collision Box block outputs a box collision geometry that is axis-aligned
with its body-fixed frame and has the origin of the body-fixed frame at the center of the
box.
