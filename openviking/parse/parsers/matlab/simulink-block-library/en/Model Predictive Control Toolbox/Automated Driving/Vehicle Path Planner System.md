---
type: simulink-block
title: 'Vehicle Path Planner System'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving'
documentation_page: 'vehiclepathplannersystem'
documentation_source_path: 'ref/vehiclepathplannersystem.html'
language: en
---

# Vehicle Path Planner System

## Ports
```yaml
ports:
- name: Pose
  summary: Initial vehicle pose three-element row vector
  direction: input
- name: Target Pose
  summary: Target vehicle pose three-element row vector
  direction: input
- name: Enable
  summary: Enable planning logical scalar
  direction: input
- name: Obstacles
  summary: List of obstacles five-column matrix
  direction: input
- name: Velocity range
  summary: Velocity range two-element vector
  direction: input
- name: Steering angle range
  summary: Front steering angle range two-element vector
  direction: input
- name: Path
  summary: Planned vehicle path three-column matrix
  direction: output
- name: Exitflag
  summary: Optimization status integer
  direction: output
```

### Input

### **Pose** — Initial vehicle pose three-element row vector

Specify the initial vehicle pose as the vector signal
[*x*0
*y*0
*θ*0], where:

- (*x*0,
  *y*0) is the initial position for the
  center of the vehicle rear axle.
- *θ*0 is the initial vehicle yaw
  angle.

### **Target Pose** — Target vehicle pose three-element row vector

Specify the target vehicle pose as the vector signal
[*xt*
*yt*
*θt*], where:

- (*xt*,
  *yt*) is the target position for the
  center of the vehicle rear axle.
- *θt* is the initial vehicle yaw
  angle.

### **Enable** — Enable planning logical scalar

To plan a path using the current pose, target pose, and obstacles, enable the path
planner by setting this signal to a positive value.

When planning is complete, set the enable signal to zero, which resets the
nonlinear MPC controller.

The time for which the path planner block is enabled must be:

- Longer than the worst-case execution time of the planner. To guarantee a
  worst-case execution time, configure the planning controller to apply a suboptimal
  solution after a specified maximum number of iterations by selecting the
  **Use suboptimal solution** parameter.
- Shorter than the sample time of the controller, as specified using the
  **Sample time** parameter.

### **Obstacles** — List of obstacles five-column matrix

Specify obstacle information as a matrix with *N* rows, where
*N* is equal to the **Number of obstacles**
parameter. Each row contains the following information for an obstacle in the order
[*X*
*Y*
*Φ*
*L*
*W*]:

- (*X*, *Y*) — Position, specified in
  meters
- *Φ* — Yaw angle, specified in radians
- *L* — Length, specified in meters
- *W* — Width, specified in meters

#### Dependencies

To enable this port, select the corresponding **Use external
source** parameter.

### **Velocity range** — Velocity range two-element vector

Vehicle velocity range in meters per second, specified as the two-element row
vector [*Vmin*
*Vmax*], where:

- *Vmin* is the minimum vehicle
  velocity.
- *Vmax* is the maximum vehicle
  velocity.

#### Dependencies

To enable this port, select the corresponding **Use external
source** parameter.

### **Steering angle range** — Front steering angle range two-element vector

Front steering angle range in radians, specified as the two-element row vector
[*ψmin*
*ψmax*], where:

- *ψmin* is the minimum steering
  angle.
- *ψmax* is the maximum steering
  angle.

The front steering angle is the angle between the front tires and the longitudinal
axis of the vehicle. The steering angle is positive towards the positive lateral axis
of the ego vehicle.

#### Dependencies

To enable this port, select the corresponding **Use external
source** parameter.
### Output

### **Path** — Planned vehicle path three-column matrix

Planned vehicle path, output as a three column matrix. Each row contains one
vehicle pose [*x*
*y*
*θ*] along the vehicle path, where:

- (*x*, *y*) is the position for the center of
  the vehicle rear axle.
- *θ* is the vehicle yaw angle.

### **Exitflag** — Optimization status integer

The optimization status of the nonlinear MPC controller, output as an integer as
follows:

- Positive — Optimal solution found
- `0` — Maximum number of optimization iterations reached,
  solution might not be optimal
- Negative — Infeasible optimization problem

#### Dependencies

To enable this port, select the **Optimization status**
parameter.
## Parameters
```yaml
parameters:
- name: Length
  summary: Vehicle length 4.7 (default) | nonnegative scalar
  group: ''
  block_parameter: egoLength
  type: string, character vector
  default: '"4.7"'
- name: Width
  summary: Vehicle width 1.8 (default) | nonnegative scalar
  group: ''
  block_parameter: egoWidth
  type: string, character vector
  default: '"1.8"'
- name: Wheelbase
  summary: Distance between front and rear axles 2.8 (default) | nonnegative scalar
  group: ''
  block_parameter: wheelbase
  type: string, character vector
  default: '"2.8"'
- name: Center to rear axle
  summary: Distance from center of vehicle to rear axle 1.4 (default) | nonnegative scalar
  group: ''
  block_parameter: dist2Center
  type: string, character vector
  default: '"1.4"'
- name: Number of obstacles
  summary: Number of obstacles in environment 0 (default) | nonnegative integer
  group: ''
  block_parameter: numObs
  type: string, character vector
  default: '"0"'
- name: Obstacle list
  summary: Obstacles in environment zeros(1,5) (default) | five-column matrix
  group: ''
  block_parameter: obs_ext
  type: string, character vector
  default: '"off"'
  values: '"off" | "on"'
- name: Minimum distance from ego vehicle to obstacles
  summary: Minimum safe distance between vehicle and any obstacle 0.1 (default) | positive scalar
  group: ''
  block_parameter: minDist
  type: string, character vector
  default: '"0.1"'
- name: Sample time
  summary: Controller sample time 1 (default) | positive scalar
  group: ''
  block_parameter: Ts
  type: string, character vector
  default: '"1"'
- name: Prediction horizon
  summary: Prediction horizon 20 (default) | positive integer
  group: ''
  block_parameter: pPlanning
  type: string, character vector
  default: '"20"'
- name: Velocity range
  summary: Velocity range [-6.5 6.5] (default) | two-element row vector
  group: ''
  block_parameter: v_ext
  type: string, character vector
  default: '"off"'
  values: '"off" | "on"'
- name: Steering angle range
  summary: Front steering angle range [-pi/4 pi/4] | two-element row vector
  group: ''
  block_parameter: steer_ext
  type: string, character vector
  default: '"off"'
  values: '"off" | "on"'
- name: Use suboptimal solution
  summary: Apply suboptimal solution after specified number of iterations off (default) | on
  group: ''
  block_parameter: suboptimal
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Maximum iteration number
  summary: Maximum optimization iterations 200 (default) | positive integer
  group: ''
  block_parameter: maxIter
  type: string, character vector
  default: '"200"'
- name: Optimization status
  summary: Add optimization status output port off (default) | on
  group: ''
  block_parameter: output_exitflag
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Create VPP subsystem
  summary: Create custom planner button
  group: ''
```

#### Parameters Tab

### **Length** — Vehicle length `4.7` (default) | nonnegative scalar

Vehicle length, specified in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `egoLength` |
| **Type:** string, character vector |
| **Default:** `"4.7"` |

### **Width** — Vehicle width `1.8` (default) | nonnegative scalar

Vehicle width, specified in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `egoWidth` |
| **Type:** string, character vector |
| **Default:** `"1.8"` |

### **Wheelbase** — Distance between front and rear axles `2.8` (default) | nonnegative scalar

The distance between the front and rear axles, specified in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `wheelbase` |
| **Type:** string, character vector |
| **Default:** `"2.8"` |

### **Center to rear axle** — Distance from center of vehicle to rear axle `1.4` (default) | nonnegative scalar

The longitudinal distance from the center of the vehicle to the rear axle, specified
in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dist2Center` |
| **Type:** string, character vector |
| **Default:** `"1.4"` |

### **Number of obstacles** — Number of obstacles in environment `0` (default) | nonnegative integer

The number of obstacles in the environment.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numObs` |
| **Type:** string, character vector |
| **Default:** `"0"` |

### **Obstacle list** — Obstacles in environment `zeros(1,5)` (default) | five-column matrix

Specify obstacle information as a matrix with *N* rows, where
*N* is equal to the **Number of obstacles**
parameter. Each row contains the following information for an obstacle in the order
[*X*
*Y*
*Φ*
*L*
*W*]:

- (*X*, *Y*) — Position, specified in
  meters
- *Φ* — Yaw angle, specified in radians
- *L* — Length, specified in meters
- *W* — Width, specified in meters

If the obstacle positions and orientations vary over time, add the
**Obstacles** input port to the block by selecting **Use
external source**.

#### Dependencies

To enable this parameter, set the **Number of obstacles**
parameter to a nonzero value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `obsMat` |
| **Type:** string, character vector |
| **Default:** `"zeros(1,5)"` |

#### Programmatic Use: Use external source

|  |
| --- |
| **Block Parameter:** `obs_ext` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Minimum distance from ego vehicle to obstacles** — Minimum safe distance between vehicle and any obstacle `0.1` (default) | positive scalar

Minimum safe distance between the ego vehicle and any obstacle in the environment,
specified in meters.

#### Dependencies

To enable this parameter, set the **Number of obstacles**
parameter to a nonzero value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `minDist` |
| **Type:** string, character vector |
| **Default:** `"0.1"` |

### **Sample time** — Controller sample time `1` (default) | positive scalar

Controller sample time, specified in seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Ts` |
| **Type:** string, character vector |
| **Default:** `"1"` |

### **Prediction horizon** — Prediction horizon `20` (default) | positive integer

Prediction horizon steps for planning. The total prediction time is the product of
the sample time and the prediction horizon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pPlanning` |
| **Type:** string, character vector |
| **Default:** `"20"` |

### **Velocity range** — Velocity range `[-6.5 6.5]` (default) | two-element row vector

Vehicle velocity range in meters per second, specified as the two-element row vector
[*Vmin*
*Vmax*], where:

- *Vmin* is the minimum vehicle
  velocity.
- *Vmax* is the maximum vehicle
  velocity.

If the velocity range varies over time, add the **Velocity range**
input port to the block by selecting **Use external source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `v_range` |
| **Type:** string, character vector |
| **Default:** `"[-6.5,6.5]"` |

#### Programmatic Use: Use external source

|  |
| --- |
| **Block Parameter:** `v_ext` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Steering angle range** — Front steering angle range `[-pi/4 pi/4]` | two-element row vector

Front steering angle range in radians, specified as the two-element row vector
[*ψmin*
*ψmax*], where:

- *ψmin* is the minimum steering
  angle.
- *ψmax* is the maximum steering
  angle.

The front steering angle is the angle of the front tires from the longitudinal axis
of the vehicle. The steering angle is positive towards the positive lateral axis of the
ego vehicle.

If the steering angle range varies over time, add the **Steering angle
range** input port to the block by selecting **Use external
source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `steer_range` |
| **Type:** string, character vector |
| **Default:** `"[-pi/4,pi/4]"` |

#### Programmatic Use: Use external source

|  |
| --- |
| **Block Parameter:** `steer_ext` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

#### Block Tab

### **Use suboptimal solution** — Apply suboptimal solution after specified number of iterations `off` (default) | `on`

Configure the controller to apply a suboptimal solution after a specified maximum
number of iterations, which guarantees the worst-case execution time for your planning
controller. To set the maximum number of iterations, use the **Maximum iteration
number** parameter.

For more information, see Suboptimal QP Solution.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `suboptimal` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Maximum iteration number** — Maximum optimization iterations `200` (default) | positive integer

Maximum number of optimization iterations.

#### Dependencies

To enable this parameter, select the **Use suboptimal solution**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxIter` |
| **Type:** string, character vector |
| **Default:** `"200"` |

### **Optimization status** — Add optimization status output port off (default) | on

Select this parameter to add the **Exitflag** output port to the
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `output_exitflag` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Create VPP subsystem** — Create custom planner button

Generate a custom VPP subsystem, which you can modify for your application. The
configuration data for the custom controller is exported to the MATLAB® workspace as a structure.
## Libraries

Model Predictive Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Code generation for single-precision or fixed-point computations is not
  supported.
- In the Configuration Parameters dialog box, on the **Code Generation >
  Interface** pane, you must select the following parameters.

  - **Support non-finite numbers** — This parameter is selected by
    default.
  - **Support variable-size signals** when using Embedded Coder® — This parameter is not selected by default.

## Version History

**Introduced in R2022b**

## Description

Plan collision-free path from initial pose to target pose

The Vehicle Path Planner System block simulates a vehicle path planner
(VPP) system that plans a collision-free trajectory from an initial pose to a target pose
using a multistage nonlinear MPC controller. You can use this block to plan a path for a
vehicle, such as a vehicle entering and exiting a parking spot or a robot moving in a
warehouse.

Once you plan a path, you can have the vehicle track the path using a path-following
control system.

To customize your controller, for example to modify the controller cost function or change
the controller initial conditions, click **Create VPP subsystem**.
