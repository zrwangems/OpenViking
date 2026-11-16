---
type: simulink-block
title: 'Timed Elastic Band'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Control Algorithms'
documentation_page: 'timedelasticband'
documentation_source_path: 'ref/timedelasticband.html'
language: en
---

# Timed Elastic Band

## Ports

### Input

### **Pose** — Current pose of robot three-element vector of form [*x* *y* *theta*]

Current pose of the robot, specified as a three-element vector of the form
[*x*
*y*
*theta*]. *x* and *y* specify the
robot position in meters. *theta* specifies the robot orientation in
radians.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Vel** — Current velocity of robot two-element vector of form [*v* *w*]

Current velocity of the robot, specified as a two-element vector of the form
[*v*
*w*]. *v* specifies the linear velocity of the robot
in meters per second. *w* specifies the angular velocity of the robot
in radians per second.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MapInfo** — Local map information bus

Local map information, specified as a bus. The bus comprises these fields:

- `Resolution` - Grid resolution, specified as a scalar in
  cells per meter representing the number and size of grid locations.
- `GridLocationInWorld` - [*x*,*y*] world coordinates of the
  bottom-left corner of the grid, specified as a 1-by-2 vector.
- `OccupancyMatrix` - Occupancy grid values, specified as an
  *h*-by-*w* matrix. *h* and
  *w* are defined by the two elements of the
  `GridSize` property of the occupancy grid object.
- `GridSize` - Number of rows and columns in grid, specified
  as a 1-by-2 real-valued vector representing the number of rows and columns, in
  that order.
- `GridOriginInLocal` - Location of the bottom-left corner of
  the grid in local coordinates, specified as a two-element vector,
  [*xLocal*
  *yLocal*].

**Data Types:** `bus`

### **RefPath** — Reference path to follow *N*-by-3 matrix

Reference path to follow, specified as an *N*-by-3 matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MaxVel** — Maximum limits of linear and angular velocity `[0.8, 1.6]` (default) | two-element positive vector

Maximum limits of linear and angular velocity for velocity commands, specified as
a two-element positive vector. The first element is the linear velocity limit, in
meters per second, and the second element is the angular velocity limit, in radians
per second.

#### Dependencies

To enable this input port, select the **Specify max velocity using
input port** checkbox in the `Trajectory` tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MaxRevVel** — Maximum velocity for reverse motion `NaN` (default) | positive scalar

Maximum velocity of the vehicle while moving in reverse direction, specified as a
positive scalar. The default value is `NaN`. When the property is set
to `NaN`, the value of maximum reverse velocity is same as that of
the maximum linear velocity. Units is in meters per second.

#### Dependencies

To enable this input port, select the **Specify max reverse velocity
using input port** checkbox in the `Trajectory`
tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MaxAccel** — Maximum limits of linear and angular acceleration `[2.4, 4.8]` (default) | two-element positive vector

Maximum limits of linear and angular acceleration for velocity commands, specified
as a two-element positive vector. The first element is the linear acceleration limit,
in meters per second squared, and the second element is the angular acceleration
limit, in radians per second squared.

#### Dependencies

To enable this input port, select the **Specify max acceleration using
input port** checkbox in the `Trajectory` tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MinTurnRad** — Minimum turning radius for vehicle on optimized path 0 (default) | nonnegative scalar

Minimum turning radius for the vehicle on the optimized path, specified as a
nonnegative scalar. This value corresponds to the radius of the turning circle at the
maximum steering angle of the vehicle. Units are in meters.

Decrease this value to allow sharp turns and in place rotations. Increase this
value to limit sharp turns. When you increase the value, the vehicle will make more
forward and reverse motions to turn in a restricted space.

#### Dependencies

To enable this input port, select the **Specify min turning radius
using input port** checkbox in the `Trajectory`
tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **TimeWeight** — Weight for time 10 (default) | positive scalar

Weight for time, specified as a positive scalar. To lower the travel time,
increase this weight value.

#### Dependencies

To enable this input port, select the **Specify time weight using input
port** parameter in the `Optimization` tab .

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **SmoothWeight** — Weight for smooth motion 1000 (default) | positive scalar

Cost function weight for smooth motion, specified as a positive scalar. To obtain
a smoother path, increase this weight value.

#### Dependencies

To enable this input port, select the **Specify smoothness weight using
input port** parameter in the `Optimization` tab
.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **ObstWeight** — Weight for safe distance from obstacles 50 (default) | positive scalar

Cost function weight for maintaining a safe distance from obstacles, specified as
a positive scalar.

#### Dependencies

To enable this input port, select the **Specify obstacle weight using
input port** parameter in the `Optimization`
tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **ObstMargin** — Safe distance between robot and obstacles 0.5 (default) | positive scalar

Safe distance between the robot and the obstacles, specified as a positive scalar,
in meters.

#### Dependencies

To enable this input port, select the **Specify obstacle safety margin
using input port** parameter in the `Main` tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **NumIter** — Number of iterations to optimize trajectory 2 (default) | positive integer

Number of iterations to optimize the trajectory, specified as a positive
integer.

#### Dependencies

To enable this input port, select the **Specify number of iterations
using input port** checkbox in the `Optimization`
tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **LookAheadTime** — Lookahead time 5 (default) | positive scalar

Lookahead time, specified as a positive scalar in seconds.

#### Dependencies

To enable this input port, select the **Specify lookahead time using
input port** checkbox in the `Main` tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **GoalTol** — Tolerance around goal pose `[0.1,0.1,0.1]` (default) | three-element column vector

Tolerance around the goal pose, specified as a three-element vector of the form
[*x*
*y*
*θ*]. *x* and *y* denote the
position of the robot in *x* and *y* directions,
respectively. Units are in meters. *θ* is the heading angle of the
robot in radians.

#### Dependencies

To enable this input port, select the **Specify goal tolerance using
input port**checkbox in the `Main` tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **RefDelTime** — Reference delta time `0.3` (default) | positive scalar

Reference delta time, specified as a positive scalar in seconds. It specifies the
travel time between consecutive poses.

#### Dependencies

To enable this input port, select the **Specify reference delta time
using input port** checkbox in the `Trajectory`
tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **VelCmds** — Velocity commands *N*-by-2 matrix

Velocity commands, returned as an *N*-by-2 matrix. The first
column is the linear velocity in meters per second, and the second column is the
angular velocity in radians per second.

**Data Types:** `double`

### **Timestamps** — Timestamps corresponding to velocity commands *N*-element column vector

Timestamps corresponding to velocity commands, returned as an
*N*-element column vector.

**Data Types:** `double`

### **OptPath** — Optimized path *N*-by-3 matrix

Optimized path, returned as an *N*-by-3 matrix. Each row is of
the form [*x*
*y*
*theta*], which defines the *xy*-position and
orientation angle *theta* at a point in the path.

**Data Types:** `double`

### **SolnInfo** — Extra information bus

Extra information, returned as a bus. The bus comprises these
fields:

| Field | Description |
| --- | --- |
| `LastFeasibleIdx` | Index specifying an element in the optimized path and timestamp outputs until which the trajectory is feasible. Beyond this index, the value of `ExitFlag` will be greater than zero. This implies one or more scenarios corresponding to `ExitFlag` > 0 has occurred. |
| `DistanceFromStartPose` | Distance of each pose in `optPath` from the first pose in `optPath`. The value of `curState` is always the first pose in `optPath`. |
| `HasReachedGoal` | Indicates whether the robot has successfully reached the last pose in the ReferencePath within a tolerance, and returns as `true` if successful. Otherwise, this value returns `false`. |
| `TrajectoryCost` | Cost of optimized trajectory for cost functions in the Timed Elastic Band algorithm. |
| `ExitFlag` | Scalar value indicating the exit condition of the `Timed Elastic Band` function.  - 0 — Indicates that the `Timed Elastic Band` function   returned feasible velocity commands and trajectory. - 1 — Indicates that the trajectory output returned by the   `Timed Elastic Band` function is collision free only until   the index value specified using   `LastFeasibleIdx`. - 2 — Indicates that the poses corresponding to indices after the   `LastFeasibleIdx` violates the obstacle safety   margin constraint of the TEB controller by more than 10%. - 3 — Indicates that the turning radius of the vehicle while moving   from a pose at `LastFeasibleIdx` to a subsequent pose   violates the minimum turning radius constraint by more than   10%. - 4 — Indicates that one or more time stamps returned by the   `Timed Elastic Band` function are older than the previous   time stamp. - 5 — Indicates that the robot will not reach the reference path   within a specified look-ahead time even if it travels at a maximum   linear velocity from its current position. |

**Data Types:** `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main Tab

### **Sample time (s)** — Sample time of controller 1 (default) | positive scalar

Specify sample time of the controller in seconds. This block only supports discrete
sample time.

### **Specify lookahead time using input port** — Add input port for lookahead time off (default) | on

Select this check box to add an input port for specifying the **Lookahead
time (s)** parameter.

### **Lookahead time (s)** — Lookahead time 5 (default) | positive scalar

Specify lookahead time as a positive scalar. Units in seconds. The controller
generates velocity commands and optimizes the trajectory until the controller reaches
the lookahead time. A higher lookahead time generates velocity commands further into the
future. This enables the robot to react earlier to unseen obstacles, but increases the
controller execution time. Conversely, a shorter lookahead time reduces the available
time to react to new, unknown obstacles, but enables the controller to run at a faster
rate.

#### Dependencies

To enable this parameter, clear the **Specify lookahead time using input
port** checkbox.

### **Specify goal tolerance using input port** — Add input port for goal tolerance off (default) | on

Select this checkbox to add an input port for specifying the **Goal
tolerance ([m m rad])** parameter.

### **Goal tolerance ([m m rad])** — Tolerance around goal pose `[0.1, 0.1, 0.1]` (default) | three-element column vector

Specify the tolerance around goal pose as a three-element vector of the form
[*x*
*y*
*θ*]. *x* and *y* denote the position
of the robot in *x* and *y* directions, respectively.
Units are in meters. *θ* is the heading angle of the robot in radians.
This goal tolerance value specifies the limit for determining whether the robot has
reached the goal pose.

#### Dependencies

To enable this parameter, clear the **Specify goal tolerance using input
port** checkbox.

### **Shape** — Shape of robot `Rectangle` (default) | `Point`

Specify the shape of the robot as `Rectangle` or
`Point`.

### **Dimension ([m m])** — Size of robot `[1, 0.67]` (default) | two-element positive vector

Specify the size of the robot as a two-element positive vector of the form
[*length*
*width*], in meters.

### **Fixed transform ([m m rad])** — Transformation matrix `se2` (default) | three-element row vector of form [*x*, *y*, *theta*]

Transformation matrix, specified as an `se2` object
defining an SE(2) transformation matrix or three-element row vector representing the
origin of the robot. The vector is of the form [*x*,
*y*, *theta*]. When you specify the origin as
[*x*, *y*, *theta*], the
`Timed Elastic Band` block computes the associated SE(2) transformation
matrix and stores it in the `FixedTransform` field.

The default origin is at the center of the rear end of the robot. You can use this
parameter to specify a new origin for the robot relative to the default origin.

This parameter is valid only if the robot is of rectangular shape.

### **Specify obstacle safety margin using input port** — Add input port for obstacle safety margin off (default) | on

Select this checkbox to add an input port for specifying the **Obstacle
safety margin (m)** parameter.

### **Obstacle safety margin (m)** — Safe distance between robot and obstacles 0.5 (default) | positive scalar

Safe distance between the robot and the obstacles, specified as a positive scalar,
in meters.

#### Dependencies

To enable this parameter, clear the **Specify obstacle safety margin
using input port** checkbox.

#### Trajectory Tab

### **Specify max velocity using input port** — Add input port for maximum velocity off (default) | on

Select this checkbox to add an input port for specifying the **Maximum
velocity ([m/s rad/s])** parameter.

### **Maximum velocity ([m/s rad/s])** — Maximum limits of linear and angular velocity `[0.8, 1.6]` (default) | two-element positive vector

Maximum limits of linear and angular velocity for velocity commands, specified as a
two-element positive vector. The first element is the linear velocity limit, in meters
per second, and the second element is the angular velocity limit, in radians per
second.

#### Dependencies

To enable this parameter, clear the **Specify max velocity using input
port** checkbox.

### **Specify max reverse velocity using input port** — Add input port for maximum reverse velocity off (default) | on

Select this checkbox to add an input port for specifying the **Maximum
reverse velocity (m/s)** parameter.

### **Maximum reverse velocity (m/s)** — Maximum velocity for reverse motion `NaN` (default) | positive scalar

Maximum velocity of the vehicle while moving in reverse direction, specified as a
positive scalar. The default value is `NaN`. When the property is set
to `NaN`, the value of maximum reverse velocity is same as that of the
maximum linear velocity. Units is in meters per second.

#### Dependencies

To enable this parameter, clear the **Specify max reverse velocity using
input port** checkbox.

### **Specify max acceleration using input port** — Add input port for maximum acceleration off (default) | on

Select this checkbox to add an input port for specifying the **Maximum
acceleration ([m/s^2 rad/s^2])** parameter.

### **Maximum acceleration ([m/s^2 rad/s^2])** — Maximum limits of linear and angular acceleration `[2.4,4.8]` (default) | two-element positive vector

Maximum limits of linear and angular acceleration for velocity commands, specified
as a two-element positive vector. The first element is the linear acceleration limit, in
meters per second squared, and the second element is the angular acceleration limit, in
radians per second squared.

#### Dependencies

To enable this parameter, clear the **Specify max acceleration using
input port** checkbox.

### **Specify min turning radius using input port** — Add input port for minimum turning radius off (default) | on

Select this checkbox to add an input port for specifying the **Minimum
turning radius (m)** parameter.

### **Minimum turning radius (m)** — Minimum turning radius for vehicle on optimized path 0 (default) | nonnegative scalar

Minimum turning radius for the vehicle on the optimized path, specified as a
nonnegative scalar. This value corresponds to the radius of the turning circle at the
maximum steering angle of the vehicle. Units are in meters.

Decrease this value to allow sharp turns and in place rotations. Increase this value
to limit sharp turns. When you increase the value, the vehicle will make more forward
and reverse motions to turn in a restricted space.

#### Dependencies

To enable this parameter, clear the **Specify min turning radius using
input port** checkbox.

### **Specify reference delta time using input port** — Add input port for reference delta time off (default) | on

Select this checkbox to add an input port for specifying the **Reference
delta time (s)** parameter.

### **Reference delta time (s)** — Reference delta time `0.3` (default) | positive scalar

Reference delta time, specified as a positive scalar in seconds. It specifies the
travel time between consecutive poses. This parameter affects the addition and deletion
of poses for the optimized trajectory. Increase the value of this parameter to have
fewer poses and reduce it to have more poses in the output path.

#### Dependencies

To enable this parameter, clear the **Specify reference delta time using
input port** checkbox.

#### Optimization Tab

### **Specify number of iterations using input port** — Add input port for number of iterations off (default) | on

Select this checkbox to add an input port for specifying the **Number of
iterations** parameter.

### **Number of iterations** — Number of iterations to optimize trajectory `2` (default) | positive integer

Number of iterations to optimize the trajectory, specified as a positive integer.
This value is the number of times interpolation occurs and the controller calls the
solver for trajectory optimization.

#### Dependencies

To enable this parameter, clear the **Specify number of iterations using
input port** checkbox.

### **Specify time weight using input port** — Add input port for time weight off (default) | on

Select this checkbox to add an input port for specifying the **Time
weight** parameter.

### **Time weight** — Cost function weight for time `10` (default) | positive integer

Cost function weight for time, specified as a positive scalar. To lower the travel
time, increase this weight value.

#### Dependencies

To enable this parameter, clear the **Specify time weight using input
port** checkbox.

### **Specify smoothness weight using input port** — Add input port for smoothness weight off (default) | on

Select this checkbox to add an input port for specifying the **Smoothness
weight** parameter.

### **Smoothness weight** — Weight for smooth motion 1000 (default) | positive scalar

Cost function weight for smooth motion, specified as a positive scalar. To obtain a
smoother path, increase this weight value.

#### Dependencies

To enable this parameter, clear the **Specify smoothness weight using
input port** checkbox.

### **Specify obstacle weight using input port** — Add input port for obstacle weight off (default) | on

Select this checkbox to add an input port for specifying the **Obstacle
weight** parameter.

### **Obstacle weight** — Weight for safe distance from obstacles 50 (default) | positive scalar

Cost function weight for maintaining a safe distance from obstacles, specified as a
positive scalar. To prioritize maintaining a safe distance from obstacles, increase this
weight value.

#### Dependencies

To enable this parameter, clear the **Specify obstacle weight using input
port** checkbox.

## Libraries

Navigation Toolbox / Control Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Plan path to avoid obstacles and generate time-optimal trajectories

The Timed Elastic Band (TEB) block computes a feasible path that avoids obstacles while
guiding the vehicle towards a specified reference path. The reference path is typically
computed using a global path planner like `plannerRRTStar`.

The local path planner smooths the path while optimizing travel time, and maintains a safe
distance from obstacles known or unknown to the global planner.
