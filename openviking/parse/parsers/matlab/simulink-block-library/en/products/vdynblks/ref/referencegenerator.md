---
type: simulink-block
title: 'Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'referencegenerator'
documentation_source_path: 'ref/referencegenerator.html'
language: en
---

# Reference Generator

## Ports

### Input

### **VehFdbk** — Vehicle feedback `Bus`

Bus containing vehicle feedback signals, including velocity, acceleration, and
steering wheel torque.
### Output

### **Vis** — Visualization reference signals `Bus`

Bus containing the visualization reference signals, including longitudinal and
lateral displacement, and steering.

### **Ref** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral
displacement, and steering.

### **Fdbk** — Vehicle location feedback signals `Bus`

Bus containing vehicle location feedback signals, including position.

## Parameters

#### Configuration

### **Maneuver** — Select maneuver `Constant Radius` (default) | `Double Lane Change` | `Increasing Steer` | `Swept Sine` | `Sine with Dwell`

Specify the scene type.

### **Maneuver start time** — Start time `scalar`

Maneuver start time, in s.

### **Longitudinal velocity reference** — Target velocity `scalar`

Target velocity.

### **Longitudinal entrance velocity setpoint units** — Units `mph` (default)

Units for target velocity.

### **Simulation time** — Simulation time `scalar`

Time, in s.

#### Constant Radius

### **Radius value** — Radius `scalar`

Radius value, in m.

### **Turn direction** — Turn direction `Right` (default) | `Left`

Turn direction.

### **Lateral acceleration threshold** — Lateral acceleration `scalar`

Lateral acceleration threshold, in g.

### **Stop simulation at lateral acceleration threshold** — Selection `off` (default) | `on`

Stop simulation if vehicle exceeds lateral acceleration threshold.

#### Double Lane Change

### **Inertial longitudinal position of gate entrance** — Position `scalar`

Inertial longitudinal position of gate entrance, in m.

### **Distance after target speed to begin reference** — Start distance `scalar`

Distance after target speed to begin reference, in m.

### **Vehicle width** — Vehicle width `scalar`

Vehicle width, in m.

The left and right lane boundaries are a function of the **Vehicle
width** parameter.

### **Lateral offset** — Lateral offset `scalar`

Lateral offset, in m.

### **Lateral reference position breakpoints** — Breakpoints `scalar`

Lateral reference position breakpoints, in m.

Use the **Lateral reference position breakpoints** and
**Lateral reference data** parameters to specify the lateral
reference trajectory as a function of the longitudinal distance.

### **Lateral reference data** — Lateral data `scalar`

Use the **Lateral reference position breakpoints** and
**Lateral reference data** parameters to specify the lateral
reference trajectory as a function of the longitudinal distance.

#### Increasing Steer

### **Handwheel rate** — Handwheel rate `scalar`

Handwheel rate, in deg/s.

### **Maximum handwheel angle** — Maximum handwheel `scalar`

Maximum handwheel angle, in deg.

### **Steering hold time after max angle reached** — Steering hold `scalar`

Steering hold, in s.

### **Lateral acceleration threshold** — Lateral acceleration `scalar`

Lateral acceleration threshold, in g.

### **Stop simulation at lateral acceleration threshold** — Selection `off` (default) | `on`

Stop simulation if vehicle exceeds lateral acceleration threshold.

#### Swept Sine

### **Swept time** — Sweep time `scalar`

Sweep time, in s.

### **Steering amplitude** — Steering amplitude `scalar`

Sinusoidal steering amplitude, in deg.

### **Final frequency** — Final frequency `scalar`

Cut off frequency to stop the maneuver, in Hz.

#### Fishhook

### **Steer and countersteer speed, steerRate** — Steer and countersteer speed `scalar`

Steer and countersteer speed, in deg/s.

### **Steer amplitude, steerAFH** — Steer amplitude `scalar`

Steer amplitude, in deg.

### **Initial dwell time, tDwell1** — Initial dwell time `scalar`

Initial dwell time, in s.

### **Countersteer dwell time, tDwell2** — Countersteer dwell time `scalar`

Countersteer dwell time, in s.

### **Return to center time, tSteer3** — Return to center time `scalar`

Return to center time, in s.

### **Roll rate countersteer initiation zero crossing threshold, pZero** — Crossing threshold `scalar`

Roll rate countersteer initiation zero crossing threshold, in deg.

#### 3D Engine

### **3D Engine** — Enable 3D visualization `off` (default) | `on`

Enable 3D visualization.

### **Scene** — 3D scene `Straight road` | `Curved road` | `Parking lot` | `Double lane change` | `Open surface` | `US city block` | `US highway` | `Virtual Mcity` | `Large parking lot`

Specify the name of the 3D scene.

### **Engine frame rate, dt3D** — Graphics `.03` (default)

Graphics frame rate, in s. The graphics frame rate is the inverse of the sample time.

### **Recommended for scene** — Initial vehicle position `on` (default) | `off`

Use vehicle positions that are recommended for the scene.

### **User-specified** — Initial vehicle position `off` (default) | `on`

Specify to set your own initial vehicle position values.

### **Initial longitudinal position, X\_o** — Initial longitudinal position `off` (default) | `on`

Initial vehicle CG position along the earth-fixed *X*-axis, in m.

### **Initial lateral position, Y\_o** — Initial lateral position `off` (default) | `on`

Initial vehicle CG position along the earth-fixed *Y*-axis, in m.

### **Initial vertical position, Z\_o** — Initial vertical position `off` (default) | `on`

Initial vehicle CG position along the earth-fixed *Z*-axis, in m.

### **Initial roll angle, phi\_o** — Roll `off` (default) | `on`

Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll), in rad.

### **Initial pitch angle, theta\_o** — Pitch `off` (default) | `on`

Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch), in rad.

### **Initial yaw angle, psi\_o** — Yaw `off` (default) | `on`

Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw), in rad.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Generate maneuver reference signals

The Reference Generator block sets the parameters that configure the
maneuver and 3D simulation environment. By default, the block is set for the constant radius
maneuver with the 3D simulation engine environment disabled.

### Model

Use the **Maneuver** parameter to specify the type of maneuver. After
you select the maneuver, use the parameters to specify the maneuver settings. By default:

- **Use maneuver-specific driver, initial position, and scene** —
  Set to `on`
- **Maneuver start time** — Set to 3s
- **Longitudinal velocity reference** — Set to 30s
- **Longitudinal entrance velocity setpoint units** — Set to
  mph

| **Maneuver** Setting | Implementation |
| --- | --- |
| `Double Lane Change` | Double-Lane Change Maneuver    - **Vehicle width** — Lane signals for the   Visualization subsystem; used for the left and right lane   boundaries - **Lateral reference data** — Lateral reference   trajectory as a function of the longitudinal distance - **Distance after target speed to begin reference** —   Start the maneuver at specified distance after the vehicle reaches the   target speed |
| `Increasing Steer` | Slowly Increasing Steering Maneuver    - **Handwheel rate** — Linear rate to increase steering   wheel angle - **Maximum handwheel angle** — Maximum steering wheel   angle |
| `Swept Sine` | Swept-Sine Steering Maneuver    - **Steering amplitude** — Sinusoidal wave   amplitude - **Final frequency** — Cut off frequency to stop the   maneuver |
| `Sine with Dwell` | In the test, the vehicle:  - Accelerates until it hits a target velocity. - Maintains the target velocity. - Responds to a sinusoidal with dwell steering command.      - **Steer frequency** — Sinusoidal wave   frequency - **Steer amplitude** — Sinusoidal wave   amplitude - **Dwell time** — Dwell time |
| `Constant Radius` | Constant Radius Maneuver    - **Radius value** — Turn radius |
| `Fishhook` | In the test, the vehicle:  - Accelerates until it hits a target velocity. - Maintains the target velocity. - Responds to initial rapid steering input. - Responds to steering overcorrection.      - **Steer and countersteer speed** — Steering   rate - **Initial dwell time** — Initial steer time - **Countersteer dwell time** — Countersteer   time |

### 3D Engine

The 3D engine implements the 3D simulation environment. Vehicle Dynamics Blockset™ integrates the 3D simulation environment with Simulink® so that you can query the world around the vehicle for virtually testing
perception, control, and planning algorithms. For 3D engine requirements, see Unreal Engine Simulation Environment Requirements and Limitations. To enable the 3D
engine, on the **3D Engine** tab, select
**Enabled**.

To position the vehicle in the scene:

1. Select the position initialization method:

   - **Recommended for scene** — Set the initial vehicle
     position to values recommended for the scene
   - **User-specified** — Set your own initial vehicle
     position
2. Click **Update the model workspaces with the initial values** to
   overwrite the initial vehicle position in the model workspaces with the applied
   values.
