---
type: simulink-block
title: 'Waypoint Follower'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control'
documentation_page: 'waypointfollower'
documentation_source_path: 'ref/waypointfollower.html'
language: en
---

# Waypoint Follower

## Ports

### Input

### **Pose** — Current UAV pose `[x y z chi]` vector

Current UAV pose, specified as a `[x y z chi]` vector. This pose
is used to calculate the lookahead point based on the input to the
**LookaheadDistance** port. `[x y z]` is the
current position in meters. `chi` is the current course in radians.
The course input is used only when the waypoints are empty. The UAV course is the
angle of direction of the velocity vector relative to north measured in
radians.

**Example:**
`[0.5;1.75;-2.5;pi]`

**Data Types:** `single` | `double`

### **Waypoints** — Set of waypoints *n*-by-3 matrix | *n*-by-4 matrix | *n*-by-5 matrix

Set of waypoints for the UAV to follow, specified as a matrix with number of rows,
*n*, equal to the number of waypoints. The number of columns depend
on the **Show Yaw input variable** and the **Transition
radius source** parameter.

Each row in the matrix has the first three elements as an `[x y
z]` position in the sequence of waypoints.

If **Show Yaw input variable** is checked, specify the desired
yaw angle, `yaw`, as the fourth element in radians.

If **Show Yaw input variable** is unchecked, and
**Transition radius source** is `external`, the
transition radius is the fourth element of the vector in meters.

If **Show Yaw input variable** is checked, and
**Transition radius source** is `external`, the
transition radius is the fifth element of the vector in meters.

The block display updates as the size of the waypoint matrix changes.

**Data Types:** `single` | `double`

### **LookaheadDistance** — Lookahead distance positive numeric scalar

Lookahead distance along the path, specified as a positive numeric scalar in
meters.

**Data Types:** `single` | `double`
### Output

### **LookaheadPoint** — Lookahead point on path `[x y z]` position vector

Lookahead point on path, returned as an `[x y z]` position vector
in meters.

**Data Types:** `single` | `double`

### **DesiredCourse** — Desired course numeric scalar

Desired course, returned as numeric scalar in radians in the range of
`[-pi, pi]`. The UAV course is the angle of direction of the
velocity vector relative to north measured in radians. For fixed-wing type UAV, the
values of desired course and desired yaw are equal.

**Data Types:** `single` | `double`

### **DesiredYaw** — Desired yaw numeric scalar

Desired yaw, returned as numeric scalar in radians in the range of `[-pi,
pi]`. The UAV yaw is the forward direction of the UAV regardless of the
velocity vector relative to north measured in radians. The desired yaw is computed
using linear interpolation between the yaw angle for each waypoint. For fixed-wing
type UAV, the values of desired course and desired yaw are equal.

**Data Types:** `single` | `double`

### **LookaheadDistFlag** — Lookahead distance flag `0` (default) | `1`

Lookahead distance flag, returned as `0` or `1`.
`0` indicates lookahead distance is not saturated,
`1` indicates lookahead distance is saturated to minimum lookahead
distance value specified.

**Data Types:** `uint8`

### **CrossTrackError** — Cross track error from UAV position to path positive numeric scalar

Cross track error from UAV position to path, returned as a positive numeric scalar
in meters. The error measures the perpendicular distance from the UAV position to the
closest point on the path.

#### Dependencies

This port is only visible if **Show CrossTrackError output
port** is checked.

**Data Types:** `single` | `double`

### **Status** — Status of waypoint navigation `0` | `1`

Status of waypoint navigation, returned as `0` or
`1`. When the follower has navigated all waypoints, the block
outputs `1`. Otherwise, the block outputs
`0`.

#### Dependencies

This port is only visible if **Show UAV Status output port** is
checked.

**Data Types:** `uint8`

## Parameters

### **UAV type** — Type of UAV `fixed-wing` (default) | `multirotor`

Type of UAV, specified as either `fixed-wing` or
`multirotor`.

This parameter is non-tunable.

### **StartFrom** — Waypoint start behavior `first` (default) | `closest`

Waypoint start behavior, specified as either `first` or
`closest`.

When set to `first`, the UAV flies to the first path segment
between waypoints. If the set of waypoints input in `Waypoints`
changes, the UAV restarts at the first path segment.

When set to `closest`, the UAV flies to the closest path segment
between waypoints. When the waypoints input changes, the UAV recalculates the closest
path segment.

This parameter is non-tunable.

### **Transition radius source** — Source of transition radius `internal` (default) | `external`

Source of transition radius, specified as either `internal` or
`external`. If specified as `internal`, the
transition radius for each waypoint is set using the **Transition radius
(r)** parameter in the block mask. If specified as
`external`, specify each waypoints transition radius independently
using the input from the **Waypoints** port.

When the UAV is within the transition radius, the block transitions to following the
next path segment between waypoints.

This parameter is non-tunable.

### **Transition radius (r)** — Transition radius for waypoints `10` (default) | positive numeric scalar

Transition radius for waypoints, specified as a positive numeric scalar in
meters.

When the UAV is within the transition radius, the block transitions to following the
next path segment between waypoints.

This parameter is non-tunable.

### **Minimum lookahead distance (m)** — Minimum lookahead distance `0.1` (default) | positive numeric scalar

Minimum lookahead distance, specified as a positive numeric scalar in meters.

When input to the **LookaheadDistance** port is less than the
minimum lookahead distance, the **LookaheadDistFlag** is returned as
`1` and the lookahead distance value is specified as the value of
minimum lookahead distance.

This parameter is non-tunable.

### **Hover at last waypoint** — Lookahead point location at last waypoint `off` (default) | `on`

The location of Lookahead point at the end of waypoint navigation. If enabled, the
lookahead point remains stationary at the last waypoint. If disabled, the lookahead
point continues to traverse the straight-line path connecting the last two
waypoints.

This parameter is non-tunable.

#### Dependencies

To enable this parameter, set **UAV type** to
`multirotor`

### **Show Yaw input variable** — Accept yaw input for waypoints `off` (default) | `on`

Accept yaw inputs for waypoints when selected. If selected, the
**Waypoints** input accepts yaw inputs for each waypoint.

### **Show CrossTrackError output port** — Output cross track error `off` (default) | `on`

Output cross track error from the **CrossTrackError** port.

This parameter is non-tunable.

### **Show UAV Status output port** — Output UAV waypoint status `off` (default) | `on`

Output UAV waypoint status from the **Status** port.

This parameter is non-tunable.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode, you
  can debug the source code of the block.
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

This parameter is non-tunable.

**Tunable:** No

## Libraries

UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2024b: Hover at last waypoint

You can now configure the lookahead point to remain stationary at the final waypoint by
enabling the **Hover at last waypoint** parameter. This parameter is only
available when you set **UAV Type** as
`multirotor`.

## Description

Follow waypoints for UAV

The Waypoint Follower block generates a lookahead point, desired course,
desired yaw, and cross track. The block accepts a UAV pose, a set of waypoints and a lookahead
distance.

Specify the **UAV type** parameter to select your UAV type.
Use the **StartFrom** parameter to specify the waypoint start
behaviour. Specify the **Transition radius source** parameter to
select between a uniform and varying transition radius for each waypoint.
