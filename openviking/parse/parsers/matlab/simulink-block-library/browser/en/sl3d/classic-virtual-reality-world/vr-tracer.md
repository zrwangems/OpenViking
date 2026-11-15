---
type: simulink-block
title: 'VR Tracer'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtracer'
documentation_source_path: 'vrtracer.html'
language: en
---

# VR Tracer

## Ports

### Input

### **Position** — Position coordinates of node 3-element vector

Object position input corresponding to the placement of the object in
the scene hierarchy. If the traced object resides as a child of a parent
object, define the parent object name in the **Parent node
(leave empty for root)** parameter.

**Data Types:** `double`

### **Color** — Marker color 3-element vector

**Note**

This port is enabled when the **Marker color
selection** parameter is set to `Block
input`

Provide the color to be used for the tracer markers as a 3-element
vector of R, G, and B values.

**Data Types:** `double`

## Parameters

### **Associated VRML file** — Virtual world 3D file string scalar | character vector

Specify the virtual world file used for the 3D viewer.

### **Parent node (leave empty for root)** — — Select node from hierarchy VR node

Select the node to be traced from the scene hierarchy.

### **Marker shape** — Select marker shape `None` (default) | `Tetrahedron` | `Pyramid` | `Box` | `Octahedron` | `Sphere`

Select a shape from the provided options to mark the signal trace.

### **Connect markers with line segments** — Display traced path `on` (default) | `off`

Enable this parameter to connect the markers on the traced object's
path.

### **Place a triad at each marker position** — Provide orientation information `on` (default) | `off`

Enable this parameter to place a triad at each marker position. A triad
helps you orient the object trajectory in the *x*-*y*-*z* plane.

### **Marker scale** — Specify size of marker `[1 1 1]` (default)

Specify a 3-element vector that defines the scaling of predefined marker
shapes and triads. This parameter allows accommodation for scenes of various
sizes.

### **Marker color selection** — Specify source of marker colors `Block input` (default) | `Selected from color list` | `Defined as RGB values`

- `Block input` — Disables
  **Marker color** parameter and relies on
  the second block input to define the marker color. Selecting
  this option enables the second block input, to which you can
  connect a signal for the marker color.
- `Selected from color list` — Enables
  the **Marker color** parameter. You can select
  one color from a list for the marker.
- `Defined as RGB values` — Enables
  **Marker color** parameter to accept RGB
  values for the marker color.

### **Marker color** — Specify tracer color `yellow` (default) | `magenta` | `cyan` | `red` | `green` | `blue` | `white` | `black`

Set the tracer marker color from the provided options. This parameter is
enabled when you set **Marker color selection** to
`Selected from color list`.

### **Marker color (RGB)** — Specify tracer color `[1 0 0]` (default) | 3-element vector

Set the tracer marker color as a 3-element vector of RGB values, each
ranging from 0-255.

### **Sample time** — Block sample time for simulation 0.1 (default) | scalar | vector

Specify the sample time for the block, or specify `-1` to inherit the sample
time.

### **Ensure that a viewer window is open during simulation** — Keep viewer open `off` (default) | `on`

Select this check box to ensure that the Simulink®
3D Animation™ Viewer is open during simulation.

### **Project positions on a plane** — Project path onto plane `off` (default) | `on`

Specify whether to display line segments from an object onto a plane to
approximate the trajectory of the object.

### **Projection plane equation coefficients (ax+by+cz+d=0)** — Specify projection plane as coefficients of vector `[0 1 0 0]` (default)

When the **Project positions on a plane** parameter is
enabled, specify the plane onto which to project the position of the object.
The coefficients are in the form `ax+by+cz+d=0`.

### **Project positions to a point** — Display line segments from marker to projection `None` (default) | `Defined in the block mask` | `Defined in the block input`

Displays line segments from an object to a point to approximate the
trajectory of the object.

- `None` — (Default) No projection to a
  point.
- `Defined in block mask` — If you select
  this option, enter coordinates in the **Projection point
  coordinates** edit box.
- `Defined in the block input` — If you
  select this option, specify the coordinates of the point in the
  output of a block that inputs to the VR Tracer block.

## Libraries

Simulink 3D Animation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2008b**

### R2023b: To be removed

The `VR Tracer` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Trace trajectory of object in associated virtual scene

The VR Tracer block allows you to trace the trajectory of an object in
the associated virtual scene.

This block creates marker nodes in regular time steps either as children of the
specified parent node (**Parent node** parameter) or at the top level
of scene hierarchy (root).

You can specify one of three types of markers:

- General shape
- Line segments connecting object positions in every time step
- Axis-aligned triads for orienting the trajectory in the 3-D space

You can also project traced object positions to a plane or to a point.

Object position input must correspond to the placement of the object in the scene
hierarchy. If the traced object resides as a child of a parent object, define the parent
object DEF name in the parent node field. If the traced object resides at the top of the
scene hierarchy (its position is defined in global scene coordinates), leave this field
empty.

The first block input vector determines the position of the marker. The second block
input (if enabled by the **Marker color selection** parameter)
represents the marker color. The second or third block input vector (depending on
whether the marker color input vector is enabled) specifies the project point
coordinates.

To open the Block Parameters dialog box, double-click the block.
