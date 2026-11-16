---
type: simulink-block
title: 'UAV Animation'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'uavanimation'
documentation_source_path: 'ref/uavanimation.html'
language: en
---

# UAV Animation

## Ports

### Input

### **Translation** — *xyz*-positions of UAVs matrix

*xyz*-positions of the UAVs, specified as an
*m*-by-3 matrix, where *m* is the total number of
UAVs that you want to animate. Each row of the matrix specifies the
*xyz*-position of a UAV in the coordinate frame that you specify in
the  **Inertial frame z-axis direction** property.

**Example:** `[1 1 1]`

### **Rotation** — Rotations of UAV body frames matrix | *m*-by-4 matrix

Rotations of UAV body frames relative to the inertial frame, specified as an
*m*-by-3 or *m*-by-4 matrix.

- If you specify the **Rotation format** parameter as
  `Euler ZYX`, specify this input as an
  *m*-by-3 matrix, where *m* is the total number
  of UAVs that you want to animate. Each row of the matrix represents the rotation
  angles about the *z*-, *y*-, and
  *x*-axes of the inertial frame for a UAV, in radians.
- If you specify this **Rotation format** parameter as
  `Quaternion`, specify the input as an
  *m*-by-4 matrix, where *m* is the total number
  of UAVs that you want to animate. Each row of the matrix represents the
  quaternion vector of a UAV.

### **UAV Type** — UAV mesh type vector

UAV mesh type, specified as an *m*-element vector of integers,
where *m* is the total number of UAVs that you want to animate. Each
element specifies the mesh type of a UAV, where `1` is a quadcopter
mesh and `2` is a fixed-wing mesh.

#### Dependencies

To enable this port, select the **Enable dynamic UAV mesh
configuration** parameter.

### **UAV Mesh Configuration** — UAV mesh configuration vector | matrix

UAV mesh configuration, specified as an *m*-element column vector
or an *m*-by-4 or *m*-by-5 matrix.
*m* is the total number of UAVs that you want to animate, and each
row corresponds to the mesh configuration of a UAV. The size of this input depends on
the parameters that you want to configure for the UAVs:

- *m*-element column vector — Each element specifies the mesh
  size of a UAV, and must be a positive value. Each UAV has the default color of
  `[1 0 0]` and alpha of `1`.
- *m*-by-4 matrix — Each row specifies the mesh size and
  color of a UAV, where the first element is the size and the other three specify
  the color as an RGB triplet.
- *m*-by-5 matrix — Each row specifies the mesh size, color,
  and transparency of a UAV, where the first element is the size, the next three
  specify the color, and the last element specifies the alpha value of the UAV
  mesh as a value in the range `[0, 1]`. A value of
  `0` is completely transparent, and a value of
  `1` is completely opaque.

**Example:** `[10 1 0 0 0.5; 20 0 1 0 0.5]` sets the first UAV mesh
size to 10 and color to red, and the second UAV mesh size to 20 and color to green.
Both UAV meshes have a transparency of 0.5.

#### Dependencies

To enable this port, select the **Enable dynamic UAV mesh
configuration** parameter.

### **Marker** — UAV Marker configuration matrix

Marker configuration, specified as a *n*-row matrix.
*n* is the total number of markers that you want to draw, and each
row corresponds to the configuration of a marker. The size of the input depends on the
parameters that you want to configure for the markers:

- *n*-by-3 matrix — Each row specifies the
  *xyz*-position of a marker. Each row has the default size,
  color, type, and filled status.
- *n*-by-4 matrix— Each row specifies the
  *xyz*- position and size of a marker, where the first 3
  elements specify the position, and the last element specifies the size.
- *n*-by-7 matrix — The first three elements specifies the
  *xyz*- position, next element specifies the size, and the
  other three specifies the color of a marker as a RGB triplet.
- *n*-by-8 matrix — The first three elements specifies the
  *xyz*- position, next element specifies the size, the next
  three element specifies the color, and the last element specifies the type of a
  marker as follows:

  - 1 — Round marker
  - 2 — Square marker
  - 3 — Triangle marker
- *n*-by-9 matrix — The first three elements specifies the
  *xyz*- position, next element specifies the size, the next
  three element specifies the color, the next element specifies the marker type, and
  the last element specifies the filled status for a marker as a positive integer,
  with 1 being filled, and 0 being not filled.

#### Dependencies

To enable this port, select the **Draw marker**
parameter.

## Parameters

### **Number of UAVs** — Number of UAV to display `1` (default) | positive integer

The number of UAV to display, specified as a positive integer.

### **Enable dynamic UAV mesh configuration** — Dynamic UAV mesh configuration `off` (default) | `on`

Select this parameter to enable the **UAV Type** and **UAV
Mesh Configuration** input ports, which enable you to configure different
meshes for each UAV in your simulation.

### **UAV Type** — Type of UAV mesh to display `Multirotor` (default) | `FixedWing`

Specify the mesh to display for the simulated UAVs as either
`FixedWing` or `Multirotor`. Use this parameter to
set a uniform mesh type for all UAV.

#### Dependencies

To enable this parameter, clear the **Enable dynamic UAV mesh
configuration** parameter.

### **UAV size** — Size of frames and attached meshes `1` (default) | positive numeric scalar

Use this parameter to set a uniform mesh size for all simulated UAVs. Specify the
value as a positive numeric scalar.

#### Dependencies

To enable this parameter, clear the **Enable dynamic UAV mesh
configuration** parameter.

### **UAV mesh color** — Color of UAV meshes `[1 0 0]` (default) | RGB triplet

Specify the color for the UAV meshes as an RGB triplet. Use this parameter to set a
uniform mesh color for all the UAVs in your simulation.

#### Dependencies

To enable this parameter, clear the **Enable dynamic UAV mesh
configuration** parameter.

### **UAV mesh and trajectory alpha** — Transparency of UAV mesh and trajectory `1` (default) | positive numeric scalar

Use this parameter to set a uniform a transparency for the meshes and trajectories
of all the UAVs in your simulation.

#### Dependencies

To enable this parameter, clear the **Enable dynamic UAV mesh
configuration** parameter.

### **Inertial frame z-axis direction** — Direction of positive *z*-axis of inertial frame `Down` (default) | `Up`

Specify the positive direction of the *z*-axis of the inertial
frame as either `Up` or `Down`. In the plot, the
positive *z*-axis always points up. The parameter defines the rotation
between the inertial frame and plot frame. Set this parameter to `Down`
if the inertial frame follows the north-east-down (NED) configuration.

### **Rotation format** — Format of rotation input `Quaternion` (default) | `Euler ZYX`

Specify the rotation input format as one of these options:

- `Euler ZYX` — The rotation input must be an
  *m*-by-3 matrix of Euler *zyx*-angles in
  radians, where *m* is the total number of UAV that you want to
  animate.
- `Quaternion`— The rotation input must be an
  *m*-by-4 matrix of quaternion vectors, in which each row is a
  quaternion. *m* is the total number of UAVs that you want to
  animate.

### **Draw marker** — Enable markers `off` (default) | `on`

Select this parameter to enable the **Marker** input port, which
enables you to draw markers in your simulation.

### **Sample time** — Interval between outputs `–1` (default) | scalar

Specify the interval between outputs as a scalar, in seconds. In the simulation, the
sample time follows simulation time and not actual wall-clock time.

The default value indicates that the block sample time is
*inherited*.

For more information about the inherited sample time type, see Specify Sample Time (Simulink).

## Libraries

UAV Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for animating UAV flights in systems that generate code. However,
this block is not included in the generated code.

## Version History

**Introduced in R2018b**

### R2024b: Animate multiple UAVs, Draw Markers, and Dynamically Configure Mesh

- The UAV Animation block now supports animating multiple UAVs. Specify the number of
  UAVs to animate by using the **Number of UAVs** parameter.
- You can now draw markers by selecting the **Draw marker**
  parameter and specifying marker configurations to the **Marker**
  input port. Use markers to visualize waypoints or lookahead distance in waypoint
  following missions.
- The UAV Animation block now supports dynamic mesh configurations which enable you to
  specify a different mesh configuration for each UAV in your simulation. To enable
  dynamic mesh configuration, select the **Enable dynamic UAV mesh
  configuration** parameter.

## Description

Animate UAV flight path using translations and rotations

The UAV Animation block animates one or multiple unmanned aerial vehicle
(UAV) flight paths based on an input array of translations and rotations. The output figure
displays a visual mesh for either a fixed-wing or multirotor UAV at the given position and
orientation. To bring up the figure after simulation, click **Show
animation** in the block mask.
