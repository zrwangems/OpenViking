---
type: simulink-block
title: 'Path Following Control System'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving'
documentation_page: 'pathfollowingcontrolsystem'
documentation_source_path: 'ref/pathfollowingcontrolsystem.html'
language: en
---

# Path Following Control System

## Ports
```yaml
ports:
- name: Set velocity
  summary: Ego vehicle velocity setpoint nonnegative scalar
  direction: input
- name: Time gap
  summary: Safe time gap nonnegative scalar
  direction: input
- name: Relative distance
  summary: Distance between lead vehicle and ego vehicle positive scalar
  direction: input
- name: Relative velocity
  summary: Velocity difference between lead vehicle and ego vehicle scalar
  direction: input
- name: Longitudinal velocity
  summary: Ego vehicle velocity nonnegative scalar
  direction: input
- name: Curvature
  summary: Road curvature scalar | vector
  direction: input
- name: Lateral deviation
  summary: Ego vehicle lateral deviation scalar
  direction: input
- name: Relative yaw angle
  summary: Angle from lane centerline scalar
  direction: input
- name: Minimum longitudinal acceleration
  summary: Minimum ego vehicle acceleration scalar
  direction: input
- name: Maximum longitudinal acceleration
  summary: Maximum ego vehicle acceleration scalar
  direction: input
- name: Minimum steering angle
  summary: Minimum front steering angle scalar
  direction: input
- name: Maximum steering angle
  summary: Maximum front steering angle scalar
  direction: input
- name: Enable optimization
  summary: Controller optimization enable signal scalar
  direction: input
- name: External control signal
  summary: Control signals applied to ego vehicle vector of length two
  direction: input
- name: Vehicle dynamics matrix A
  summary: State matrix of ego vehicle predictive model square matrix
  direction: input
- name: Vehicle dynamics matrix B
  summary: Input-to-state matrix of ego vehicle predictive model matrix with two columns
  direction: input
- name: Vehicle dynamics matrix C
  summary: State-to-output matrix of ego vehicle predictive model matrix with three rows
  direction: input
- name: Longitudinal acceleration
  summary: Acceleration control signal scalar
  direction: output
- name: Steering angle
  summary: Front steering angle control signal scalar
  direction: output
```

### Input

### **Set velocity** — Ego vehicle velocity setpoint nonnegative scalar

Ego vehicle velocity setpoint in m/s. When there is no lead vehicle, the controller tracks
this velocity.

### **Time gap** — Safe time gap nonnegative scalar

Safe time gap in seconds between the lead vehicle and the ego vehicle. This time
gap is used to calculate the minimum safe following distance constraint. For more
information, see Safe Following Distance.

### **Relative distance** — Distance between lead vehicle and ego vehicle positive scalar

Distance in meters between lead vehicle and ego vehicle. To calculate this signal, subtract the ego vehicle position from the lead vehicle position.

### **Relative velocity** — Velocity difference between lead vehicle and ego vehicle scalar

Velocity difference in meters per second between lead vehicle and ego vehicle. To calculate this signal, subtract the ego vehicle velocity from the lead vehicle velocity.

### **Longitudinal velocity** — Ego vehicle velocity nonnegative scalar

Ego vehicle velocity in m/s.

### **Curvature** — Road curvature scalar | vector

Road curvature, specified as 1/*R*, where *R* is the radius of the curve in meters.

The road curvature is:

- Positive when the road curves toward the positive Y axis of the global coordinate system.
- Negative when the road curves toward the negative Y axis of the global coordinate system.
- Zero for a straight road.

The controller models the road curvature as a measured disturbance with previewing. You can specify the curvature as a:

- Scalar signal — Specify the curvature for the current control interval. The controller uses this curvature value across the prediction horizon.
- Vector signal with length less than or equal to the **Prediction
  Horizon** parameter — Specify the current and predicted curvature
  values across the prediction horizon. If the length of the vector is less than
  the prediction horizon, then the controller uses the final curvature value in
  the vector for the remainder of the prediction horizon.

### **Lateral deviation** — Ego vehicle lateral deviation scalar

Ego vehicle lateral deviation in meters from the centerline of the lane. The lateral deviation
*e*1 is positive when the ego vehicle is to
the right of the centerline and negative when the ego vehicle is to the left of the
centerline.

### **Relative yaw angle** — Angle from lane centerline scalar

Ego vehicle longitudinal axis angle in radians from the centerline of the lane, defined as:

e2=θe−θc

Here, *θe* is the ego vehicle angle and
*θc* is the centerline angle, with both
angles defined in the global coordinate frame.

### **Minimum longitudinal acceleration** — Minimum ego vehicle acceleration scalar

Minimum ego vehicle longitudinal acceleration constraint in
m/s2. Use this input port when the minimum acceleration
varies at run time.

#### Dependencies

To enable this port, select corresponding **Use external
source** parameter.

### **Maximum longitudinal acceleration** — Maximum ego vehicle acceleration scalar

Maximum ego vehicle longitudinal acceleration constraint in
m/s2. Use this input port when the maximum acceleration
varies at run time.

#### Dependencies

To enable this port, select corresponding **Use external
source** parameter.

### **Minimum steering angle** — Minimum front steering angle scalar

Minimum front steering angle constraint in radians. Use this input port when the minimum steering angle varies at run time.

#### Dependencies

To enable this port, select corresponding **Use external source**
parameter.

### **Maximum steering angle** — Maximum front steering angle scalar

Maximum front steering angle constraint in radians. Use this input port when the maximum steering angle varies at run time.

#### Dependencies

To enable this port, select corresponding **Use external source**
parameter.

### **Enable optimization** — Controller optimization enable signal scalar

Controller optimization enable signal. When this signal is:

- Nonzero, the controller performs optimization calculations and generates the
  **Longitudinal acceleration** and **Steering
  angle** control signals.
- Zero, the controller does not perform optimization calculations. In this case,
  the **Longitudinal acceleration** and **Steering
  angle** output signals remain at the values they had when the
  optimization was disabled. The controller continues to update its internal state
  estimates.

#### Dependencies

To enable this port, select the **Use external signal to enable or
disable optimization** parameter.

### **External control signal** — Control signals applied to ego vehicle vector of length two

Actual control signals applied to the ego vehicle. The first element of this
signal is the longitudinal acceleration in m/s2, and the
second element is the steering angle in radians. The controller uses these signals to
estimate the ego vehicle model states. Use this input port when the control signals
applied to the ego vehicle do not match the optimal control signals computed by the
model predictive controller. This mismatch can occur when, for example:

- The Path Following Control System is not the active controller.
  Maintaining an accurate state estimate when the controller is not active prevents
  bumps in the control signals when the controller becomes active.
- The steering or acceleration actuator fails and does not provide the correct
  control signal to the ego vehicle.

#### Dependencies

To enable this port, select the **Use external control signal for
bumpless transfer between PFC and other controllers** parameter.

### **Vehicle dynamics matrix A** — State matrix of ego vehicle predictive model square matrix

State matrix of ego vehicle predictive model. The number of rows in the state matrix
corresponds to the number of states in the predictive model. This matrix must be
square.

The ego vehicle predictive model defined by **Vehicle dynamics matrix
A**, **Vehicle dynamics matrix B**, and **Vehicle
dynamics matrix C** must be minimal.

#### Dependencies

To enable this port, select the **Use vehicle model**
parameter.

### **Vehicle dynamics matrix B** — Input-to-state matrix of ego vehicle predictive model matrix with two columns

Input-to-state matrix of ego vehicle predictive model. The number of rows in this signal must match the number of rows in **Vehicle dynamics matrix A**.

The ego vehicle predictive model defined by **Vehicle dynamics matrix A**, **Vehicle dynamics matrix B**, and **Vehicle dynamics matrix C** must be minimal.

#### Dependencies

To enable this port, select the **Use vehicle model** parameter.

### **Vehicle dynamics matrix C** — State-to-output matrix of ego vehicle predictive model matrix with three rows

State-to-output matrix of ego vehicle predictive model. The number of columns in this signal must match the number of rows in **Vehicle dynamics matrix A**.

The ego vehicle predictive model defined by **Vehicle dynamics matrix A**, **Vehicle dynamics matrix B**, and **Vehicle dynamics matrix C** must be minimal.

#### Dependencies

To enable this port, select the **Use vehicle model** parameter.
### Output

### **Longitudinal acceleration** — Acceleration control signal scalar

Acceleration control signal in m/s2 generated by the controller.

### **Steering angle** — Front steering angle control signal scalar

Front steering angle control signal in radians generated by the controller. The front steering angle is the angle of the front tires from the longitudinal axis of the vehicle. The steering angle is positive towards the positive lateral axis of the ego vehicle.
## Parameters
```yaml
parameters:
- name: Use vehicle parameters
  summary: Define ego vehicle model using vehicle properties on (default) | off
  group: Parameters Tab
  block_parameter: ModelType
  type: string, character vector
  default: '"Use vehicle parameters"'
- name: Use vehicle model
  summary: Define ego vehicle model using state-space matrices off (default) | on
  group: Parameters Tab
  block_parameter: ModelType
  type: string, character vector
  default: '"Use vehicle parameters"'
- name: Total mass
  summary: Ego vehicle mass 1575 (default) | positive scalar
  group: Parameters Tab
  block_parameter: VehicleMass
  type: string, character vector
  default: '"1575"'
- name: Yaw moment of inertia
  summary: Moment of inertia about the ego vehicle vertical axis 2875 (default) | positive scalar
  group: Parameters Tab
  block_parameter: VehicleYawInertia
  type: string, character vector
  default: '"2875"'
- name: Longitudinal distance from center of gravity to front tires
  summary: Distance from the ego vehicle center of mass to its front tires 1.2 (default) | positive scalar
  group: Parameters Tab
  block_parameter: LengthToFront
  type: string, character vector
  default: '"1.2"'
- name: Longitudinal distance from center of gravity to rear tires
  summary: Distance from the ego vehicle center of mass to its rear tires 1.6 (default) | positive scalar
  group: Parameters Tab
  block_parameter: LengthToRear
  type: string, character vector
  default: '"1.6"'
- name: Cornering stiffness of front tires
  summary: Front tire stiffness 19000 (default) | positive scalar
  group: Parameters Tab
  block_parameter: FrontTireStiffness
  type: string, character vector
  default: '"19000"'
- name: Cornering stiffness of rear tires
  summary: Rear tire stiffness 33000 (default) | positive scalar
  group: Parameters Tab
  block_parameter: RearTireStiffness
  type: string, character vector
  default: '"33000"'
- name: Longitudinal acceleration tracking time constant
  summary: Time constant for acceleration tracking 0.5 (default) | positive scalar
  group: Parameters Tab
  block_parameter: AccelTimeConstant
  type: string, character vector
  default: '"0.5"'
- name: A
  summary: Initial state matrix of ego vehicle predictive model square matrix
  group: Parameters Tab
  block_parameter: EgoModelMatrixA
  type: string, character vector
  default: '"[-4.4021 ,-12.4603;1.3913,-5.1868]"'
- name: B
  summary: Initial input-to-state matrix of ego vehicle predictive model matrix with two columns
  group: Parameters Tab
  block_parameter: EgoModelMatrixB
  type: string, character vector
  default: '"[24.1270;15.8609]"'
- name: C
  summary: Initial state-to-output matrix of ego vehicle predictive model matrix with three rows
  group: Parameters Tab
  block_parameter: EgoModelMatrixC
  type: string, character vector
  default: '"[1,0;0,1]"'
- name: Initial longitudinal velocity
  summary: Initial velocity of the ego vehicle model 15 (default) | nonnegative scalar
  group: Parameters Tab
  block_parameter: InitialLongVel
  type: string, character vector
  default: '"15"'
- name: Transport lag between model inputs and outputs
  summary: Total transport lag in ego vehicle model 0 (default) | nonnegative scalar
  group: Parameters Tab
  block_parameter: TransportLag
  type: string, character vector
  default: '"0"'
- name: Maintain safe distance between lead vehicle and ego vehicle
  summary: Enable spacing control on (default) | off
  group: Parameters Tab
  block_parameter: spaceCtrl
  type: string, character vector
  default: '"on"'
- name: Default spacing
  summary: Minimum spacing to lead vehicle 10 (default) | nonnegative scalar
  group: Parameters Tab
  block_parameter: DefaultSpacing
  type: string, character vector
  default: '"10"'
- name: Minimum steering angle
  summary: Minimum front steering angle -0.26 (default) | scalar between -pi/2 and pi/2
  group: Controller Tab
  block_parameter: MinSteering
  type: string, character vector
  default: '"-0.26"'
- name: Maximum steering angle
  summary: Maximum front steering angle 0.26 (default) | scalar between -pi/2 and pi/2
  group: Controller Tab
  block_parameter: MaxSteering
  type: string, character vector
  default: '"0.26"'
- name: Minimum longitudinal acceleration
  summary: Minimum ego vehicle acceleration -3 (default) | scalar
  group: Controller Tab
  block_parameter: MinAcceleration
  type: string, character vector
  default: '"-3"'
- name: Maximum longitudinal acceleration
  summary: Maximum ego vehicle acceleration 2 (default) | scalar
  group: Controller Tab
  block_parameter: MaxAcceleration
  type: string, character vector
  default: '"2"'
- name: Sample time
  summary: Controller sample time 0.1 (default) | positive scalar
  group: Controller Tab
  block_parameter: Ts
  type: string, character vector
  default: '"0.1"'
- name: Prediction horizon
  summary: Controller prediction horizon 10 (default) | positive integer
  group: Controller Tab
  block_parameter: PredictionHorizon
  type: string, character vector
  default: '"30"'
- name: Control horizon
  summary: Controller control horizon 3 (default) | positive integer | vector of positive integers
  group: Controller Tab
  block_parameter: ControlHorizon
  type: string, character vector
  default: '"3"'
- name: Weight on velocity tracking
  summary: Tuning weight for longitudinal velocity tracking 0.1 (default) | positive scalar
  group: Controller Tab
  block_parameter: LongWeight
  type: string, character vector
  default: '"0.1"'
- name: Weight on lateral error
  summary: Tuning weight for lateral error 1 (default) | positive scalar
  group: Controller Tab
  block_parameter: LateralWeight
  type: string, character vector
  default: '"1"'
- name: Weight on change of longitudinal acceleration
  summary: Tuning weight for change in longitudinal acceleration 0.1 (default) | positive scalar
  group: Controller Tab
  block_parameter: AccelRateWeight
  type: string, character vector
  default: '"0.1"'
- name: Weight on change of steering angle
  summary: Tuning weight for change in steering angle 0.1 (default) | positive scalar
  group: Controller Tab
  block_parameter: SteerRateWeight
  type: string, character vector
  default: '"0.1"'
- name: Use suboptimal solution
  summary: Apply suboptimal solution after specified number of iterations off (default) | on
  group: Block Tab
  block_parameter: suboptimal
  type: string, character vector
  default: '"off"'
- name: Maximum iteration number
  summary: Maximum optimization iterations 10 (default) | positive integer
  group: Block Tab
  block_parameter: maxiter
  type: string, character vector
  default: '"10"'
- name: Use external signal to enable or disable optimization
  summary: Add port for enabling optimization off (default) | on
  group: Block Tab
  block_parameter: optmode
  type: string, character vector
  default: '"off"'
- name: Use external signal for bumpless transfer between PFC and other controllers
  summary: Add external control signal input port off (default) | on
  group: Block Tab
  block_parameter: trackmode
  type: string, character vector
  default: '"off"'
- name: Create PFC subsystem
  summary: Create custom controller button
  group: Block Tab
```

### Parameters Tab

#### Ego Vehicle

### **Use vehicle parameters** — Define ego vehicle model using vehicle properties `on` (default) | `off`

Select this parameter to define the ego vehicle model used by the MPC controller
by specifying properties of the ego vehicle. The ego vehicle model is the linear model
from the longitudinal acceleration and front steering angle to the longitudinal
velocity, lateral velocity, and yaw angle rate.

To define the vehicle model, specify the following block parameters:

- **Total mass**
- **Yaw moment of inertia**
- **Longitudinal distance from center of gravity to front
  tires**
- **Longitudinal distance from center of gravity to rear
  tires**
- **Cornering stiffness of front tires**
- **Cornering stiffness of rear tires**
- **Longitudinal acceleration tracking time constant**

For more information on the ego vehicle model, see Ego Vehicle Predictive Model.

Selecting this parameter clears the **Use vehicle model**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelType` |
| **Type:** string, character vector |
| **Default:** `"Use vehicle parameters"` |

### **Use vehicle model** — Define ego vehicle model using state-space matrices `off` (default) | `on`

Select this parameter to define the state-space matrices of the ego vehicle model
used by the MPC controller. The ego vehicle model is the linear model from the
longitudinal acceleration and front steering angle to the longitudinal velocity,
lateral velocity, and yaw angle rate.

To define the initial internal model, specify the **A**,
**B**, and **C** state-space matrices. The
internal model must be a minimal realization with no direct feedthrough, and the
dimensions of **A**, **B**, and
**C** must be consistent.

Typically, the ego vehicle model is velocity-dependent, and therefore, it varies
over time. To update the internal model at run time, use the **Vehicle
dynamics A**, **Vehicle dynamics B**, and
**Vehicle dynamics C** input ports.

For more information on the ego vehicle model, see Ego Vehicle Predictive Model.

Selecting this parameter clears the **Use vehicle parameters**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelType` |
| **Type:** string, character vector |
| **Default:** `"Use vehicle parameters"` |

### **Total mass** — Ego vehicle mass `1575` (default) | positive scalar

Ego vehicle mass in kg.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VehicleMass` |
| **Type:** string, character vector |
| **Default:** `"1575"` |

### **Yaw moment of inertia** — Moment of inertia about the ego vehicle vertical axis `2875` (default) | positive scalar

Moment of inertia about the ego vehicle vertical axis in
Kg·m2.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VehicleYawInertia` |
| **Type:** string, character vector |
| **Default:** `"2875"` |

### **Longitudinal distance from center of gravity to front tires** — Distance from the ego vehicle center of mass to its front tires `1.2` (default) | positive scalar

Distance from the ego vehicle center of mass to its front tires in meters, measured along the longitudinal axis of the vehicle.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LengthToFront` |
| **Type:** string, character vector |
| **Default:** `"1.2"` |

### **Longitudinal distance from center of gravity to rear tires** — Distance from the ego vehicle center of mass to its rear tires `1.6` (default) | positive scalar

Distance from the ego vehicle center of mass to its rear tires in meters, measured along the longitudinal axis of the vehicle.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LengthToRear` |
| **Type:** string, character vector |
| **Default:** `"1.6"` |

### **Cornering stiffness of front tires** — Front tire stiffness `19000` (default) | positive scalar

Front tire stiffness in N/rad, defined as the relationship between the side force on the front tires and the angle of the tires to the longitudinal axis of the vehicle.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrontTireStiffness` |
| **Type:** string, character vector |
| **Default:** `"19000"` |

### **Cornering stiffness of rear tires** — Rear tire stiffness `33000` (default) | positive scalar

Rear tire stiffness in N/rad, defined as the relationship between the side force on the rear tires and the angle of the tires to the longitudinal axis of the vehicle.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RearTireStiffness` |
| **Type:** string, character vector |
| **Default:** `"33000"` |

### **Longitudinal acceleration tracking time constant** — Time constant for acceleration tracking `0.5` (default) | positive scalar

Time constant for tracking longitudinal acceleration, specified in seconds.

#### Dependencies

To enable this parameter, select the **Use vehicle parameters**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AccelTimeConstant` |
| **Type:** string, character vector |
| **Default:** `"0.5"` |

### **A** — Initial state matrix of ego vehicle predictive model square matrix

Initial state matrix of ego vehicle predictive model. The number of rows in the state matrix
corresponds to the number of states in the predictive model. This matrix must be
square.

The initial ego vehicle predictive model defined by **A**, **B**, and **C** must be minimal.

Typically, the ego vehicle model varies over time. To update the state matrix at run time, use the **Vehicle dynamics A** input port.

#### Dependencies

To enable this parameter, select the **Use vehicle model** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EgoModelMatrixA` |
| **Type:** string, character vector |
| **Default:** `"[-4.4021 ,-12.4603;1.3913,-5.1868]"` |

### **B** — Initial input-to-state matrix of ego vehicle predictive model matrix with two columns

Initial input-to-state matrix of ego vehicle predictive model. The number of rows in this parameter must match the number of rows in **A**.

The initial ego vehicle predictive model defined by **A**, **B**, and **C** must be minimal.

Typically, the ego vehicle model varies over time. To update the input-to-state matrix at run time, use the **Vehicle dynamics B** input port.

#### Dependencies

To enable this parameter, select the **Use vehicle model**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EgoModelMatrixB` |
| **Type:** string, character vector |
| **Default:** `"[24.1270;15.8609]"` |

### **C** — Initial state-to-output matrix of ego vehicle predictive model matrix with three rows

Initial state-to-output matrix of ego vehicle predictive model. The number of columns in this parameter must match the number of rows in **A**.

The initial ego vehicle predictive model defined by **A**, **B**, and **C** must be minimal.

Typically, the ego vehicle model varies over time. To update the state-to-output matrix at run time, use the **Vehicle dynamics C** input port.

#### Dependencies

To enable this parameter, select the **Use vehicle model**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EgoModelMatrixC` |
| **Type:** string, character vector |
| **Default:** `"[1,0;0,1]"` |

### **Initial longitudinal velocity** — Initial velocity of the ego vehicle model `15` (default) | nonnegative scalar

Initial velocity of the ego vehicle model in m/s, which can differ from the actual
ego vehicle initial velocity.

This value is used to configure the initial conditions of the model predictive
controller. For more information, see Initial Conditions.

**Note**

A very small initial velocity, for example `eps`, can produce a
nonminimal realization for the controller plant model, causing an error. To prevent
this error, set the initial velocity to a larger value, for example
`1e-3`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLongVel` |
| **Type:** string, character vector |
| **Default:** `"15"` |

### **Transport lag between model inputs and outputs** — Total transport lag in ego vehicle model `0` (default) | nonnegative scalar

Total transport lag, *τ*, in the ego vehicle model in seconds.
This lag includes actuator, sensor, and communication lags. For each input-output
channel, the transport lag model is:

1τs+1

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TransportLag` |
| **Type:** string, character vector |
| **Default:** `"0"` |

#### Spacing Control

### **Maintain safe distance between lead vehicle and ego vehicle** — Enable spacing control `on` (default) | `off`

To configure the safe following distance, set the **Default
spacing** parameter. For more information on the safe following distance
used by the controller, see Safe Following Distance.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `spaceCtrl` |
| **Type:** string, character vector |
| **Default:** `"on"` |

### **Default spacing** — Minimum spacing to lead vehicle `10` (default) | nonnegative scalar

Minimum spacing in meters between the lead vehicle and the ego vehicle. This value
corresponds to the target relative distance between the ego and lead vehicles when the
ego vehicle velocity is zero.

This value is used to calculate the:

- Minimum safe following distance. For more information, see Safe Following Distance.
- Controller initial conditions. For more information, see Initial Conditions.

#### Dependencies

To enable this parameter, select the **Maintain safe distance between
lead vehicle and ego vehicle** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DefaultSpacing` |
| **Type:** string, character vector |
| **Default:** `"10"` |

### Controller Tab

#### Path Following Controller Constraints

### **Minimum steering angle** — Minimum front steering angle `-0.26` (default) | scalar between `-pi/2` and `pi/2`

Minimum front steering angle constraint in radians.

If the minimum steering angle varies over time, add the **Minimum steering
angle** input port to the block by selecting **Use external
source**.

#### Dependencies

This parameter must be less than the **Maximum steering angle** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MinSteering` |
| **Type:** string, character vector |
| **Default:** `"-0.26"` |

### **Maximum steering angle** — Maximum front steering angle `0.26` (default) | scalar between `-pi/2` and `pi/2`

Maximum front steering angle constraint in radians.

If the maximum steering angle varies over time, add the **Maximum steering
angle** input port to the block by selecting **Use external
source**.

#### Dependencies

This parameter must be greater than the **Minimum steering angle** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxSteering` |
| **Type:** string, character vector |
| **Default:** `"0.26"` |

### **Minimum longitudinal acceleration** — Minimum ego vehicle acceleration `-3` (default) | scalar

Minimum ego vehicle longitudinal acceleration constraint in
m/s2.

If the minimum acceleration varies over time, add the **Minimum
longitudinal acceleration** input port to the block by selecting
**Use external source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MinAcceleration` |
| **Type:** string, character vector |
| **Default:** `"-3"` |

### **Maximum longitudinal acceleration** — Maximum ego vehicle acceleration `2` (default) | scalar

Maximum ego vehicle longitudinal acceleration constraint in
m/s2.

If the maximum acceleration varies over time, add the **Maximum
longitudinal acceleration** input port to the block by selecting
**Use external source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxAcceleration` |
| **Type:** string, character vector |
| **Default:** `"2"` |

#### Model Predictive Controller Settings

### **Sample time** — Controller sample time `0.1` (default) | positive scalar

Controller sample time in seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Ts` |
| **Type:** string, character vector |
| **Default:** `"0.1"` |

### **Prediction horizon** — Controller prediction horizon `10` (default) | positive integer

Controller prediction horizon steps. The controller prediction time is the product of the sample time and the prediction horizon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PredictionHorizon` |
| **Type:** string, character vector |
| **Default:** `"30"` |

### **Control horizon** — Controller control horizon `3` (default) | positive integer | vector of positive integers

Controller control horizon, specified as one of the following:

- Positive integer less than or equal to the **Prediction
  horizon** parameter. In this case, the controller computes
  *m* free control moves occurring at times *k*
  through *k*+*m*-1, and holds the controller
  output constant for the remaining prediction horizon steps from
  *k*+*m* through
  *k*+*p*-1. Here, *k* is the
  current control interval.
- Vector of positive integers, [*m*1,
  *m*2, …], where the sum of the integers
  equals the **Prediction horizon** parameter. In this case, the
  controller computes *M* blocks of free moves, where
  *M* is the length of the control horizon vector. The first free
  move applies to times *k* through
  *k*+*m*1-1, the second
  free move applies from time
  *k*+*m*1 through
  *k*+*m*1+*m*2-1,
  and so on. Using block moves can improve the robustness of your controller.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ControlHorizon` |
| **Type:** string, character vector |
| **Default:** `"3"` |

#### Controller Behavior

### **Weight on velocity tracking** — Tuning weight for longitudinal velocity tracking `0.1` (default) | positive scalar

Tuning weight for longitudinal velocity tracking. To produce smaller
velocity-tracking errors, increase this weight.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LongWeight` |
| **Type:** string, character vector |
| **Default:** `"0.1"` |

### **Weight on lateral error** — Tuning weight for lateral error `1` (default) | positive scalar

Tuning weight for lateral error. To produce smaller lateral errors, increase this
weight.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LateralWeight` |
| **Type:** string, character vector |
| **Default:** `"1"` |

### **Weight on change of longitudinal acceleration** — Tuning weight for change in longitudinal acceleration `0.1` (default) | positive scalar

Tuning weight for changes in longitudinal acceleration. To produce less-aggressive
vehicle acceleration, increase this weight.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AccelRateWeight` |
| **Type:** string, character vector |
| **Default:** `"0.1"` |

### **Weight on change of steering angle** — Tuning weight for change in steering angle `0.1` (default) | positive scalar

Tuning weight for changes in steering angle. To produce less-aggressive steering
angle changes, increase this weight.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SteerRateWeight` |
| **Type:** string, character vector |
| **Default:** `"0.1"` |

### Block Tab

### **Use suboptimal solution** — Apply suboptimal solution after specified number of iterations `off` (default) | `on`

Configure the controller to apply a suboptimal solution after a specified maximum number of iterations, which guarantees the worst-case execution time for your controller.

For more information, see Suboptimal QP Solution.

#### Dependencies

After selecting this parameter, specify the **Maximum iteration number** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `suboptimal` |
| **Type:** string, character vector |
| **Default:** `"off"` |

### **Maximum iteration number** — Maximum optimization iterations `10` (default) | positive integer

Maximum number of controller optimization iterations.

#### Dependencies

To enable this parameter, select the **Use suboptimal solution**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxiter` |
| **Type:** string, character vector |
| **Default:** `"10"` |

### **Use external signal to enable or disable optimization** — Add port for enabling optimization `off` (default) | `on`

To add the **Enable optimization** input port to the block, select this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `optmode` |
| **Type:** string, character vector |
| **Default:** `"off"` |

### **Use external signal for bumpless transfer between PFC and other controllers** — Add external control signal input port `off` (default) | `on`

To add the **External control signal** input port to the block,
select this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `trackmode` |
| **Type:** string, character vector |
| **Default:** `"off"` |

### **Create PFC subsystem** — Create custom controller button

Generate a custom PFC subsystem, which you can modify for your application. The
configuration data for the custom controller is exported to the MATLAB® workspace as a structure.

You can modify the custom controller subsystem to:

- Modify default MPC settings or use advanced MPC features.
- Modify the default controller initial conditions.
- Use different application settings, such as a custom safe following distance
  definition.
## Libraries

Model Predictive Control Toolbox / Automated Driving

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2019a**

## Description

Simulate path-following control using adaptive model predictive controller

The Path Following Control System block simulates a path-following control
(PFC) system that keeps an ego vehicle traveling along the center of a straight or curved road
while tracking a set velocity and maintaining a safe distance from a lead vehicle. To do so,
the controller adjusts both the longitudinal acceleration and front steering angle of the ego
vehicle. The block computes optimal control actions while satisfying safe distance, velocity,
acceleration, and steering angle constraints using adaptive model predictive control
(MPC).

This block combines the capabilities of the Lane Keeping Assist
System and Adaptive Cruise Control
System blocks into a single controller.

To customize your controller, for example to use advanced MPC features or modify
controller initial conditions, click **Create PFC subsystem**.
