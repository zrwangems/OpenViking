---
type: simulink-block
title: 'VR RigidBodyTree'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrrigidbodytree'
documentation_source_path: 'vrrigidbodytree.html'
language: en
---

# VR RigidBodyTree

## Ports

### Input

### **Input 1** — Joint Positions scalar | vector

Robot configuration that solves the desired end-effector pose,
specified as a vector. A robot configuration is a vector of joint
positions for the `rigidBodyTree` model. The number of
positions is equal to the number of non-fixed joints in the
`rigidBodyTree` parameter.

**Data Types:** `single` | `double`

## Parameters

### **Associated VRML File** — 3D World 3D world file name

Specify the virtual world in which the `rigidBodyTree` is
visualized

### **Parent node (leave empty for root)** — Scene hierarchy location character vector | string

Specify the location of the `rigidBodyTree` object in the scene
hierarchy.

### **Rigid Body Tree** — robot pose `rigidBodyTree`

Specify the name of the Robotics System Toolbox
`rigidBodyTree` object to be used in the virtual world. If
a robot with an identical name is already present in the virtual world, it
is used for visualization by default.

You can enable the **Always use robot definition from the
RigidBodyTree object** parameter to overwrite the existing
robot, if present, with the robot specified by the
`rigidBodyTree` object.

### **Always use robot definition from the RigidBodyTree object** — create robot `‘off’` (default) | `’on’`

Enable this parameter to always create a robot from the
`rigidBodyTree` object specified by the **Rigid
Body Tree** parameter.

By default, the virtual world uses an existing robot by the same name, if
it exists.

### **Sample time** — Block sample time for simulation 0.1 (default) | scalar | vector

Specify the sample time for the block, or specify `-1` to inherit the sample
time.

### **Ensure that a viewer window is open during simulation** — Open 3D world viewer `‘off’` (default) | `’on’`

Enable this parameter to ensure that the Simulink
3D Animation Viewer is open during simulation.

## Libraries

Simulink 3D Animation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2018b**

### R2025a: Warns

The `VR RigidBodyTree` block will be removed in a
future release. The Simulink
3D Animation Viewer has been removed so `VR RigidBodyTree` does not open the
virtual world. For alternate functionality, see Transition Virtual Reality World to Unreal Engine 3D Environment.

### R2023b: To be removed

The `VR RigidBodyTree` runs without warning and will be removed in a future release.

## Description

(To be removed) Visualize Robotics System Toolbox rigidBodyTree objects in Simulink

Use the VR RigidBodyTree block to visualize
`rigidBodyTree` objects from Robotics System Toolbox™ in the Simulink®
3D Animation™ viewer.
