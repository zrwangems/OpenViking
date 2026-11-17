---
type: simulink-block
title: 'Obstacle Avoidance'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'obstacleavoidance'
documentation_source_path: 'ref/obstacleavoidance.html'
language: en
---

# Obstacle Avoidance

## Ports
```yaml
ports:
- name: Position
  summary: Position of UAV vector
  direction: input
  data_types: double
- name: Orientation
  summary: Orientation of UAV vector
  direction: input
  data_types: double
- name: ObstaclePoints
  summary: Positions of obstacles matrix
  direction: input
  data_types: double
- name: TargetPostion
  summary: Position of target vector
  direction: input
  data_types: double
- name: DesiredDirection
  summary: Desired direction vector
  direction: output
  data_types: double
- name: DesiredYaw
  summary: Desired yaw scalar
  direction: output
  data_types: double
- name: Status
  summary: Status of obstacle-free direction 0 | 1 | 2 | 3
  direction: output
  data_types: uint8
```

### Input

### **Position** — Position of UAV vector

Position of the UAV, specified as a vector of the form
`[x; y;
z]`. `x`,
`y`, and
`z` define the xyz-position of the UAV in any
right-handed coordinate frame, such as NED and ENU. Units are in meters.

**Example:**
`[1; 1; 1]`

**Data Types:** `double`

### **Orientation** — Orientation of UAV vector

Orientation of the UAV in any right-handed coordinate frame, such as NED and ENU,
specified as a quaternion vector of the form `[w;
x; y;
z]`.

**Example:** `[1; 0; 0; 0]`

**Data Types:** `double`

### **ObstaclePoints** — Positions of obstacles matrix

Obstacle points locations, specified as an *N*-by-3 matrix with
rows of the form `[x
y
z]`. `x`,
`y`, and
`z` define the xyz-position of the obstacle
point in the reference frame of the range sensor. *N* is the number
of obstacle points. Units are in meters.

You can obtain the obstacle points using sensors such as the UAV Scenario
Lidar which outputs obstacle points as a point cloud data.

**Example:** `[1 1 1; 2 2 2]`

**Data Types:** `double`

### **TargetPostion** — Position of target vector

Position of the target, specified as a vector of the form
`[x; y;
z]`. `x`,
`y`, and
`z` define the xyz- position of the target in
any right-handed coordinate frame, such as NED and ENU. Units are in meters.

**Example:** `[2; 3; 4]`

**Data Types:** `double`
### Output

### **DesiredDirection** — Desired direction vector

Desired direction, returned as a unit vector of the form
`[x; y;
z]`. `x`,
`y`, and
`z` define the desired direction in the
right-handed coordinate frame that you specified in the position input. Units are in
meters.

**Data Types:** `double`

### **DesiredYaw** — Desired yaw scalar

Desired yaw in the right-handed coordinate frame that you specified in the
position input, returned as numeric scalar in radians in the range of `[-pi,
pi]` .

**Data Types:** `double`

### **Status** — Status of obstacle-free direction `0` | `1` | `2` | `3`

Status of the obstacle-free direction, returned as `0`,
`1`, `2`, or `3`.

- `0` — An obstacle-free direction is found.
- `1` — No obstacle-free direction is found.
- `2` — An obstacle-free direction is found but is close to the
  obstacle.
- `3` — No obstacle-free direction is found and is close to
  obstacle.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Sensor range limits (m)
  summary: Limits of range sensor [0.2 10] (default) | vector of form [min max]
  group: ''
- name: Sensor horizontal field of view (deg)
  summary: Horizontal field of view limits of range sensor [-60 60] (default) | vector of form [min max]
  group: ''
- name: Sensor vertical field of view (deg)
  summary: Vertical field of view limits of range sensor [-30 30] (default) | vector of form [min max]
  group: ''
- name: Sensor location [X, Y, Z] (m)
  summary: Sensor mounting location on UAV [0 0 0] (default) | vector of form [x y z]
  group: ''
- name: Sensor orientation [Roll, Pitch, Yaw] (deg)
  summary: Orientation of sensor mounted on UAV [0 0 0] (default) | vector of form [roll pitch yaw]
  group: ''
- name: Vehicle radius (m)
  summary: Radius of UAV 1 (default) | numeric scalar
  group: ''
- name: Minimum distance to obstacle (m)
  summary: Safety distance around UAV to obstacle 1 (default) | numeric scalar
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
- name: Histogram resolution (deg)
  summary: Histogram grid resolution 5 (default) | 1 | 3 | 6 | 10 | 15 | 18 | 30 | 45 | 60
  group: ''
- name: Histogram window size
  summary: Histogram window size 1 (default) | odd integer
  group: ''
- name: Histogram threshold
  summary: Threshold for computing histogram 1 (default) | positive integer
  group: ''
- name: Maximum age of obstacle point
  summary: Maximum age of remembered obstacle point 0 (default) | numeric scalar
  group: ''
- name: Target direction weight
  summary: Cost function weight for target direction 5 (default) | numeric scalar
  group: ''
- name: Current direction weight
  summary: Cost function weight for current direction 2 (default) | numeric scalar
  group: ''
- name: Previous direction weight
  summary: Cost function weight for previous direction 2 (default) | numeric scalar
  group: ''
```

#### Main

### **Sensor range limits (m)** — Limits of range sensor `[0.2 10]` (default) | vector of form `[min max]`

Specify the minimum and maximum limits of the range sensor as a vector of the form
`[min
max]`, with values in meters.

**Data Types:** `double`

### **Sensor horizontal field of view (deg)** — Horizontal field of view limits of range sensor `[-60 60]` (default) | vector of form `[min max]`

Specify the minimum and maximum horizontal field of view limits of the range sensor
as a vector of the form `[min
max]`, with values in degrees.

**Data Types:** `double`

### **Sensor vertical field of view (deg)** — Vertical field of view limits of range sensor `[-30 30]` (default) | vector of form `[min max]`

Specify the minimum and maximum vertical field of view limits of the range sensor as
a vector of the form `[min
max]`, with values in degrees.

**Data Types:** `double`

### **Sensor location [X, Y, Z] (m)** — Sensor mounting location on UAV `[0 0 0]` (default) | vector of form `[x y z]`

Specify the mounting location of the sensor on the UAV body frame as a vector of the
form `[x
y
z]`, with values in meters.

The configuration of the UAV body frame orients the *x*-axis as forward-positive, the *y*-axis
as right-positive, and the *z*-axis
downward-positive.

**Data Types:** `double`

### **Sensor orientation [Roll, Pitch, Yaw] (deg)** — Orientation of sensor mounted on UAV `[0 0 0]` (default) | vector of form `[roll pitch yaw]`

Specify the orientation of the sensor on the UAV body frame as a vector of the form
`[roll
pitch
yaw]`, with values in degrees.

**Data Types:** `double`

### **Vehicle radius (m)** — Radius of UAV `1` (default) | numeric scalar

This dimension defines the smallest circle that can circumscribe your vehicle, in
meters. The vehicle radius is used to account for vehicle size when computing the
obstacle-free direction.

**Data Types:** `double`

### **Minimum distance to obstacle (m)** — Safety distance around UAV to obstacle `1` (default) | numeric scalar

The safety distance specifies, in meters, the space accounted for between the UAV
and obstacles in addition to the vehicle radius. The vehicle radius and safety distance
are used to compute the obstacle-free direction.

**Data Types:** `double`

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify whether to simulate the model using `Interpreted execution`
or `Code generation`.

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option reduces startup time, but has a slower
  simulation speed than `Code generation`. In this mode, you can
  debug the source code of the block.
- `Code generation` — Simulate the model using generated C
  code. The first time you run a simulation, Simulink® generates C code for this block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of subsequent simulations is faster than
  `Interpreted execution`.

**Tunable:** No

#### Histogram

### **Histogram resolution (deg)** — Histogram grid resolution `5` (default) | `1` | `3` | `6` | `10` | `15` | `18` | `30` | `45` | `60`

To change the histogram grid resolution, select a value from the list. All values
are in degrees.

### **Histogram window size** — Histogram window size `1` (default) | odd integer

The histogram window size determines the angular width of an obstacle-free opening
in the azimuth and elevation directions. This value is unitless.

**Data Types:** `uint8`

### **Histogram threshold** — Threshold for computing histogram `1` (default) | positive integer

The threshold for computing the histogram specifies the minimum number of obstacle
points that should be in an histogram cell to be considered as obstacle. If a cell
contains fewer than this number of obstacle points, the cell is considered as
obstacle-free.

**Data Types:** `uint8`

### **Maximum age of obstacle point** — Maximum age of remembered obstacle point `0` (default) | numeric scalar

Specifies the maximum age of a remembered obstacle point as a numeric scalar. This
value specify the number of previous time steps for which the obstacle points from those
time steps is remembered.

**Data Types:** `double`

#### Cost

### **Target direction weight** — Cost function weight for target direction `5` (default) | numeric scalar

Specifies the function weight for moving toward the target direction. To follow a
target direction, set this weight to be greater than the sum of `Current direction
weight` and `Previous direction
weight`. To ignore the target direction cost, set this weight to
`0`.

**Data Types:** `double`

### **Current direction weight** — Cost function weight for current direction `2` (default) | numeric scalar

Specifies the function weight for moving the vehicle in the current heading
directions. Higher values of this weight produce more efficient paths. To ignore the
current direction cost, set this weight to `0`.

**Data Types:** `double`

### **Previous direction weight** — Cost function weight for previous direction `2` (default) | numeric scalar

Specifies the function weight for moving in the previously selected steering
direction. Higher values of this weight produce smoother paths. To ignore the previous
direction cost, set this weight to `0`.

**Data Types:** `double`
## Libraries

UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Compute obstacle-free direction using range sensor data and target position

The Obstacle Avoidance block computes an obstacle-free direction using
range sensor data and target position.
