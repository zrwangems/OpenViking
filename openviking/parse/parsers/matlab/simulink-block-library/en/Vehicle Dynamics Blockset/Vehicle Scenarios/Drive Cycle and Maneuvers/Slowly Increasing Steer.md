---
type: simulink-block
title: 'Slowly Increasing Steer'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'slowlyincreasingsteer'
documentation_source_path: 'ref/slowlyincreasingsteer.html'
language: en
---

# Slowly Increasing Steer

## Ports
```yaml
ports:
- name: xdot
  summary: Vehicle longitudinal velocity scalar
  direction: input
  data_types: single | double
- name: ay
  summary: Vehicle lateral acceleration threshold scalar
  direction: input
  data_types: single | double
- name: DrvRef
  summary: Driver reference data bus
  direction: output
  data_types: bus
- name: DrvCmd
  summary: Driver command data bus
  direction: output
  data_types: bus
```

### Input

### **xdot** — Vehicle longitudinal velocity scalar

Vehicle longitudinal velocity in the body fixed frame, specified as a scalar, in
m/s.

**Data Types:** `single` | `double`

### **ay** — Vehicle lateral acceleration threshold scalar

Vehicle lateral acceleration needed to stop the simulation, specified as a scalar,
in m/s^2.

#### Dependencies

To enable this parameter, select **Stop simulation at lateral
acceleration threshold**.

**Data Types:** `single` | `double`
### Output

### **DrvRef** — Driver reference data bus

Driver reference data, returned as a bus containing these block values.

| Signal | Description | Units |
| --- | --- | --- |
| `LngRef` | Longitudinal reference velocity | m/s |
| `LtrRef` | Lateral reference displacement | m |
| `XRef` | Vehicle global longitudinal reference position | m |
| `YRef` | Vehicle global lateral reference position | m |
| `PhiRef` | Vehicle global yaw reference position | rad |
| `CurvRef` | Reference path curvature | 1/m |
| `CurvGradRef` | Reference path curvature gradient | 1/m^2 |

**Data Types:** `bus`

### **DrvCmd** — Driver command data bus

Driver command data, returned as a bus containing these block values.

| Signal | | Description | Units |
| --- | --- | --- | --- |
| `SteerCmd` | `EnblSteerCmd` | Boolean signal used to override driver model steering commands | one |
| `SteerCmd` | Handwheel angle | one |
| `SteerZero` | Boolean signal used to override driver model steering commands with zero when value is `true` | one |
| `SteerHld` | Boolean signal used to hold the current driver model steering output when `true` | one |
| `AccelCmd` | `EnblAccelCmd` | Boolean signal used to override driver model acceleration commands | one |
| `AccelCmd` | Normalized accelerator input | one |
| `AccelHld` | Boolean signal used to hold the current driver model acceleration output when `true` | one |
| `AccelZero` | Boolean signal used to override driver model acceleration commands with zero when value is `true` | one |
| `DecelCmd` | `EnblDecelCmd` | Boolean signal used to override driver model deceleration commands | one |
| `DecelCmd` | Normalized decelerator or brake input | one |
| `DecelHld` | Boolean signal used to hold the current driver model deceleration output when `true` | one |
| `DecelZero` | Boolean signal used to override driver model deceleration commands with zero when value is `true` | one |
| `HndBrkCmd` | Normalized handbrake or park brake input | one |
| `TransCmd` | `TransModeCmd` | Command to specify the transmission mode | one |
| `GearCmd` | Command to specify manual gear number or automatic transmission shifter position | one |
| `UpShiftCmd` | Command to upshift | one |
| `DwnShiftCmd` | Command to downshift | one |
| `ClutchCmd` | Normalized clutch open command for manual transmissions | one |

**Note**

By default, the `TransCmd` bus is not actively used. Use a
Bus Assignment block to override the
`TransCmd` signal to customize and extend the scenario.

Block diagram where the Bus Assignment block overrides the TransModeCmd output from the Slowly Increasing Steer block.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Maneuver start time, tStart [s]
  summary: Start time 2 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: tStart
  values: 2 (default) | positive scalar
- name: Longitudinal velocity setpoint, velRef
  summary: Target velocity 50 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: velRef
  values: 50 (default) | positive scalar
- name: Longitudinal velocity setpoint units, velRefUnit []
  summary: Units mph (default)
  group: Maneuver Parameters
  block_parameter: velRefUnit
  values: mph (default) | character vector
- name: Steer and countersteer speed, steerRate [deg/s]
  summary: Steer and countersteer rate 13.5 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: steerRate
  values: 13.5 (default) | positive scalar
- name: Steer amplitude, steerAmp [deg]
  summary: Handwheel steer amplitude 270 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: steerAmp
  values: 270 (default) | positive scalar
- name: Steering hold time after max angle reached, tStop [s]
  summary: Steering hold time 2 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: tStop
  values: 2 (default) | positive scalar
- name: Lateral acceleration absolute threshold, ay_max [g]
  summary: Lateral acceleration threshold 0.5 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: ay_max
  values: 0.5 (default) | positive scalar
- name: Initial steer direction
  summary: Initial steer direction Right (default) | Left
  group: Maneuver Parameters
  block_parameter: steerDir
  values: Right (default) | Left
- name: Stop simulation at lateral acceleration threshold
  summary: Option to stop simulation at lateral acceleration threshold off (default) | on
  group: Maneuver Parameters
  block_parameter: ayStop
  values: off (default) | on
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Maneuver Parameters

### **Maneuver start time, tStart [s]** — Start time `2` (default) | positive scalar

Maneuver start time, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tStart` |
| **Values:** | `2` (default) | positive scalar |
| **Data Types:** | `double` |

### **Longitudinal velocity setpoint, velRef** — Target velocity `50` (default) | positive scalar

Target velocity.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `velRef` |
| **Values:** | `50` (default) | positive scalar |
| **Data Types:** | `double` |

### **Longitudinal velocity setpoint units, velRefUnit []** — Units `mph` (default)

Units for target velocity.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `velRefUnit` |
| **Values:** | `mph` (default) | character vector |
| **Data Types:** | `character vector` |

### **Steer and countersteer speed, steerRate [deg/s]** — Steer and countersteer rate `13.5` (default) | positive scalar

Steer and countersteer rate, in deg/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerRate` |
| **Values:** | `13.5` (default) | positive scalar |
| **Data Types:** | `double` |

### **Steer amplitude, steerAmp [deg]** — Handwheel steer amplitude `270` (default) | positive scalar

Handwheel steer amplitude, in deg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerAmp` |
| **Values:** | `270` (default) | positive scalar |
| **Data Types:** | `double` |

### **Steering hold time after max angle reached, tStop [s]** — Steering hold time `2` (default) | positive scalar

Steering hold time after maximum steer amplitude is reached, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tStop` |
| **Values:** | `2` (default) | positive scalar |
| **Data Types:** | `double` |

### **Lateral acceleration absolute threshold, ay\_max [g]** — Lateral acceleration threshold `0.5` (default) | positive scalar

Lateral acceleration threshold at which the simulation is stopped, in gee.

#### Dependencies

To enable this parameter, select **Stop simulation at lateral
acceleration threshold**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ay_max` |
| **Values:** | `0.5` (default) | positive scalar |
| **Data Types:** | `double` |

### **Initial steer direction** — Initial steer direction `Right` (default) | `Left`

Set the initial steer direction as `Right` or
`Left`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerDir` |
| **Values:** | `Right` (default) | `Left` |
| **Data Types:** | `character vector` |

### **Stop simulation at lateral acceleration threshold** — Option to stop simulation at lateral acceleration threshold `off` (default) | `on`

Select this parameter to stop the simulation at the input lateral acceleration
threshold.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ayStop` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |
## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Generate commands to conduct linearly increasing steering maneuver

The Slowly Increasing Steer block generates steering, accelerator, and
brake commands to conduct a linearly increasing steering maneuver. The steering command begins
at the specified rate once the vehicle reaches the longitudinal velocity setpoint. After the
vehicle achieves the maximum steering angle, the vehicle maintains the steering angle for a
set duration. The block then reduces the steering angle to zero at the same rate. A
longitudinal controller regulates the vehicle at the prescribed speed throughout the maneuver.
You have the option to stop the simulation at a lateral acceleration threshold.

The slowly increasing steer maneuver is a foundational test to help assess the vehicle's
lateral dynamics and understeer characteristics. You can also use the maneuver to set up
additional tests such as swept sine, sine with dwell, and fishhook.

**Note**

For information on the reference generator block used in the slowly increasing steer
reference application, see Slowly Increasing Steer Reference Generator.
