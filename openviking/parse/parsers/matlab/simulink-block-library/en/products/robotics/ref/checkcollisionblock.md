---
type: simulink-block
title: 'Check Collision'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'checkcollisionblock'
documentation_source_path: 'ref/checkcollisionblock.html'
language: en
---

# Check Collision

## Ports

### Input

### **Geom1** — First collision geometry to check bus

First collision geometry, specified as a bus created by any of these collision
geometry blocks:

- Collision
  Box
- Collision
  Capsule
- Collision
  Cylinder
- Collision
  Mesh
- Collision
  Sphere

### **Geom2** — Second collision geometry to check bus

Second collision geometry, specified as a bus created by any of these collision
geometry blocks:

- Collision
  Box
- Collision
  Capsule
- Collision
  Cylinder
- Collision
  Mesh
- Collision
  Sphere
### Output

### **CollStatus** — Collision status scalar

Collision status, returned as a Boolean `0` or
`1`. If the two geometries are in collision,
**CollStatus** outputs `1`. Otherwise, the value is
`0`.

### **SepDist** — Minimum distance between collision geometries scalar

Minimum distance between the two collision geometries, returned as a scalar. The
line segment that connects the witness points **WitnessPts**, determines the
minimum distance between the two geometries. When the two geometries are in collision,
**SepDist** outputs `NaN`.

### **WitnessPts** — Witness points on each geometry matrix

Witness points on each geometry, returned as a 3-by-2 matrix. The first column is
the location of the witness point on the geometry **Geom1**, and the second
column is the location of the witness point on the other geometry **Geom2**.
The length of the line segment that connects the two witness points determines the
value from the **SepDist** port. When the two geometries are in collision,
every element of **WitnessPts** is `NaN`.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

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

Check Collision block supports code generation with
dynamic memory allocation disabled. For more information about disabling dynamic memory
allocation, see Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2025a**

## Description

Check if two convex collision geometries are in collision

The Check Collision block checks for collision between two convex collision
geometries and additionally outputs the separation distance and corresponding witness points
between the collision geometries.
