---
type: simulink-block
title: 'Orbit Follower'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'orbitfollower'
documentation_source_path: 'ref/orbitfollower.html'
language: en
---

# Orbit Follower

## Ports
```yaml
ports:
- name: Pose
  summary: Current UAV pose [x y z course] vector
  direction: input
  data_types: single | double
- name: Center
  summary: Center of orbit [x y z] vector
  direction: input
  data_types: single | double
- name: Radius
  summary: Radius of orbit positive scalar
  direction: input
  data_types: single | double
- name: TurnDirection
  summary: Direction of orbit scalar
  direction: input
  data_types: single | double
- name: LookaheadDistance
  summary: Lookahead distance for tracking orbit positive scalar
  direction: input
  data_types: single | double
- name: ResetNumTurns
  summary: Reset for counting turns numeric signal
  direction: input
  data_types: single | double
- name: LookaheadPoint
  summary: Lookahead point on path [x y z] position vector
  direction: output
  data_types: double
- name: DesiredCourse
  summary: Desired course numeric scalar
  direction: output
  data_types: double
- name: DesiredYaw
  summary: Desired yaw numeric scalar
  direction: output
  data_types: double
- name: OrbitRadiusFlag
  summary: Orbit radius flag 0 (default) | 1
  direction: output
  data_types: uint8
- name: LookaheadDistFlag
  summary: Lookahead distance flag 0 (default) | 1
  direction: output
  data_types: uint8
- name: CrossTrackError
  summary: Cross track error from UAV position to path positive numeric scalar
  direction: output
  data_types: double
- name: NumTurns
  summary: Number of times the UAV has completed the orbit numeric scalar
  direction: output
```

### Input

### **Pose** — Current UAV pose `[x y z course]` vector

Current UAV pose, specified as an `[x y z course]` vector.
`[x y z]` is the position of the UAV in NED coordinates
(north-east-down) specified in meters. `course` is the angle between
ground velocity and north direction in radians per second.

**Example:**
`[1,1,-10,pi/4]`

**Data Types:** `single` | `double`

### **Center** — Center of orbit `[x y z]` vector

Center of orbit, specified as an `[x y z]` vector. `[x y
z]` is the orbit center position in NED coordinates (north-east-down)
specified in meters.

**Example:**
`[5,5,-10]`

**Data Types:** `single` | `double`

### **Radius** — Radius of orbit positive scalar

Radius of orbit, specified as a positive scalar in meters.

**Example:**
`5`

**Data Types:** `single` | `double`

### **TurnDirection** — Direction of orbit scalar

Direction of orbit, specified as a scalar. Positive values indicate a clockwise
turn as viewed from above. Negative values indicate a counter-clockwise turn. A value
of `0` automatically determines the value based on the input to
**Pose**.

**Example:**
`-1`

**Data Types:** `single` | `double`

### **LookaheadDistance** — Lookahead distance for tracking orbit positive scalar

Lookahead distance for tracking the orbit, specified as a positive scalar. Tuning
this value helps adjust how tightly the UAV follows the orbit circle. Smaller values
improve tracking, but can lead to oscillations in the path.

**Example:**
`2`

**Data Types:** `single` | `double`

### **ResetNumTurns** — Reset for counting turns numeric signal

Reset for counting turns, specified as a numeric signal. Any rising signal
triggers a reset of the **NumTurns** output.

**Example:**
`2`

#### Dependencies

To enable this input, select `rising` for **External
reset**.

**Data Types:** `single` | `double`
### Output

### **LookaheadPoint** — Lookahead point on path `[x y z]` position vector

Lookahead point on path, returned as an `[x y z]` position vector
in meters.

**Data Types:** `double`

### **DesiredCourse** — Desired course numeric scalar

Desired course, returned as numeric scalar in radians in the range of
`[-pi, pi]`. The UAV course is the angle of direction of the
velocity vector relative to north measured in radians. For fixed-wing type UAV, the
values of desired course and desired yaw are equal.

**Data Types:** `double`

### **DesiredYaw** — Desired yaw numeric scalar

Desired yaw, returned as numeric scalar in radians in the range of `[-pi,
pi]`. The UAV yaw is the forward direction of the UAV (regardless of the
velocity vector) relative to north measured in radians. For fixed-wing type UAV, the
values of desired course and desired yaw are equal.

**Data Types:** `double`

### **OrbitRadiusFlag** — Orbit radius flag `0` (default) | `1`

Orbit radius flag, returned as `0` or `1`.
`0` indicates orbit radius is not saturated, `1`
indicates orbit radius is saturated to minimum orbit radius value specified.

**Data Types:** `uint8`

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

**Data Types:** `double`

### **NumTurns** — Number of times the UAV has completed the orbit numeric scalar

Number of times the UAV has completed the orbit, returned as a numeric scalar. As
the UAV circles the center point, this value increases or decreases based on the
specified **Turn Direction**. Decimal values indicate partial
completion of a circle. If the UAV cross track error exceeds the lookahead distance,
the number of turns is not updated.

**NumTurns** is reset whenever **Center**,
**Radius**, or **TurnDirection** are changed. You
can also use the **ResetNumTurns** input.

#### Dependencies

This port is only visible if **Show NumTurns output port** is
checked.
## Parameters
```yaml
parameters:
- name: UAV type
  summary: Type of UAV fixed-wing (default) | multirotor
  group: ''
- name: Minimum orbit radius (m)
  summary: Minimum orbit radius 1 (default) | positive numeric scalar
  group: ''
- name: Minimum lookahead distance (m)
  summary: Minimum lookahead distance 0.1 (default) | positive numeric scalar
  group: ''
- name: External reset
  summary: Reset trigger source none (default) | rising
  group: ''
- name: Show CrossTrackError output port
  summary: Output cross track error off (default) | on
  group: ''
- name: Show NumTurns output port
  summary: Output UAV waypoint status off (default) | on
  group: ''
```

### **UAV type** — Type of UAV `fixed-wing` (default) | `multirotor`

Type of UAV, specified as either `fixed-wing` or
`multirotor`.

This parameter is non-tunable.

### **Minimum orbit radius (m)** — Minimum orbit radius `1` (default) | positive numeric scalar

Minimum orbit radius, specified as a positive numeric scalar in meters.

When input to the orbit **Radius** port is less than the minimum
orbit radius, the **OrbitRadiusFlag** is returned as
`1` and the orbit radius value is specified as the value of minimum
orbit radius.

This parameter is non-tunable.

### **Minimum lookahead distance (m)** — Minimum lookahead distance `0.1` (default) | positive numeric scalar

Minimum lookahead distance, specified as a positive numeric scalar in meters.

When input to the **LookaheadDistance** port is less than the
minimum lookahead distance, the **LookaheadDistFlag** is returned as
`1` and the lookahead distance value is specified as the value of
minimum lookahead distance.

This parameter is non-tunable.

### **External reset** — Reset trigger source `none` (default) | `rising`

Select `rising` to enable the **ResetNumTurns**
block input.

This parameter is non-tunable.

### **Show CrossTrackError output port** — Output cross track error `off` (default) | `on`

Output cross track error from the **CrossTrackError** port.

This parameter is non-tunable.

### **Show NumTurns output port** — Output UAV waypoint status `off` (default) | `on`

Output UAV waypoint status from the **Status** port.

This parameter is non-tunable.
## Libraries

UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Orbit location of interest using UAV

The Orbit Follower block generates course and yaw controls for following a
circular orbit around a location of interest based on the current pose of the unmanned aerial
vehicle (UAV). Select a **UAV type** of fixed-wing or multirotor UAVs. You
can specify any orbit center location, orbit radius, and turn direction. A lookahead distance,
**LookaheadDistance**, is used for tuning the path tracking and generating
the **LookaheadPoint** output.
