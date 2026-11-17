---
type: simulink-block
title: 'Collision Mesh'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisionmeshblock'
documentation_source_path: 'ref/collisionmeshblock.html'
language: en
---

# Collision Mesh

## Ports
```yaml
ports:
- name: Vertices
  summary: Vertices of mesh matrix
  direction: input
- name: Pose
  summary: Pose of collision geometry matrix
  direction: input
- name: CollGeom
  summary: Collision geometry bus
  direction: output
- name: ExitFlag
  summary: Validity of collision mesh vertices scalar
  direction: output
  data_types: uint16
```

### Input

### **Vertices** — Vertices of mesh matrix

Vertices of the mesh, specified as an *N*-by-3 matrix, where
*N* is the number of vertices and must greater than or equal to 1.
Each row of **Vertices** represents the coordinates of a point in 3-D space.
Note that some of the points can be inside the constructed convex mesh.

### **Pose** — Pose of collision geometry matrix

Pose of the collision geometry relative to the world frame, specified as a 4-by-4 homogeneous matrix.
### Output

### **CollGeom** — Collision geometry bus

Collision geometry, returned as a bus.

To perform collision checking, connect this output to a Check Collision block as input.

### **ExitFlag** — Validity of collision mesh vertices scalar

Validity of collision mesh vertices, returned as one of these values:

- `4` — Vertices matrix contains values nonnumeric.
- `3` — Vertices matrix contains values that are not
  real.
- `2` — Vertices matrix contains nonfinite values.
- `1` — Vertices matrix does not have three columns.
- `0` — Vertices are valid.

To validate vertices at runtime instead, select the **Enable
Runtime Input Dimensions Error** parameter.

**Data Types:** `uint16`
## Parameters
```yaml
parameters:
- name: Enable Runtime Input Dimensions Error
  summary: Validation of collision mesh vertices on (default) | off
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Enable Runtime Input Dimensions Error** — Validation of collision mesh vertices `on` (default) | `off`

Select this parameter to enable runtime validation of the collision mesh vertices
and return an error if **Vertices** is invalid.

If you clear this parameter, the block does not error during simulation, and instead
uses the **ExitFlag** port to identify invalid mesh vertices.

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

Collision Mesh block supports code generation with
dynamic memory allocation disabled. For more information about disabling dynamic memory
allocation, see Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2025a**

## Description

Create convex mesh collision geometry

The Collision Mesh block outputs a convex mesh collision geometry using a list
of 3-D vertices relative to a pose specified in relation to the world frame.
