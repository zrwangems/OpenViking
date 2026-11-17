---
type: simulink-block
title: 'Fishhook'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'fishhook'
documentation_source_path: 'ref/fishhook.html'
language: en
---

# Fishhook

## Ports
```yaml
ports:
- name: xdot
  summary: Vehicle longitudinal velocity scalar
  direction: input
  data_types: double
- name: p
  summary: Vehicle roll rate scalar
  direction: input
  data_types: double
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

**Data Types:** `double`

### **p** — Vehicle roll rate scalar

Vehicle roll rate, specified as a scalar, in rad/s.

#### Dependencies

To enable this parameter, select **Use roll rate to determine initial
steer dwell time**.

**Data Types:** `double`
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
| `TransCmd` | `TransModeCmd` | Transmission or drive mode command | one |
| `GearCmd` | Command to specify manual gear or automatic transmission shifter position | one |
| `UpShiftCmd` | Command to upshift | one |
| `DwnShiftCmd` | Command to downshift | one |
| `ClutchCmd` | Normalized clutch pedal command for manual transmissions | one |

**Note**

By default, the `TransCmd` bus is not actively used. Use a
Bus Assignment block to override the
`TransCmd` bus to customize and extend the scenario.

Block diagram where the Bus Assignment block overrides the TransModeCmd output from the Fishhook block.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Maneuver start time, tStart [s]
  summary: Start time 2 (default) | positive scalar
  group: ''
  block_parameter: tStart
  values: 2 (default) | positive scalar
- name: Longitudinal velocity setpoint, velRef
  summary: Target velocity 30 (default) | positive scalar
  group: ''
  block_parameter: velRef
  values: 30 (default) | positive scalar
- name: Longitudinal velocity setpoint units, velRefUnit []
  summary: Units mph (default)
  group: ''
  block_parameter: velRefUnit
  values: mph (default) | character vector
- name: Steer and countersteer speed, steerRate [deg/s]
  summary: Steer and countersteer rate 720 (default) | positive scalar
  group: ''
  block_parameter: steerRate
  values: 720 (default) | positive scalar
- name: Steer amplitude, steerAmp [deg]
  summary: Handwheel steer amplitude 540 (default) | positive scalar
  group: ''
  block_parameter: steerAmp
  values: 540 (default) | positive scalar
- name: Use roll rate to determine initial steer dwell time
  summary: Option to use roll rate to determine initial steer dwell time off (default) | on
  group: ''
  block_parameter: pFdbk
  values: off (default) | on
- name: Initial dwell time, tDwellSteer [s]
  summary: Initial dwell time 0.5 (default) | positive scalar
  group: ''
  block_parameter: tDwellSteer
  values: 0.5 (default) | positive scalar
- name: Countersteer dwell time, tDwellCntrSteer [s]
  summary: Countersteer dwell time 3 (default) | positive scalar
  group: ''
  block_parameter: tDwellCntrSteer
  values: 3 (default) | positive scalar
- name: Return to center time, tZero [s]
  summary: Time to return countersteer amplitude to zero steer 2 (default) | positive scalar
  group: ''
  block_parameter: tZero
  values: 2 (default) | positive scalar
- name: Roll rate countersteer initiation zero crossing threshold, pZero [deg/s]
  summary: Roll rate tolerance 1.5 (default) | positive scalar
  group: ''
  block_parameter: pZero
  values: 1.5 (default) | positive scalar
- name: Initial steer direction
  summary: Initial steer direction Right (default) | Left
  group: ''
  block_parameter: steerDir
  values: Right (default) | Left
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

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

### **Longitudinal velocity setpoint, velRef** — Target velocity `30` (default) | positive scalar

Target velocity.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `velRef` |
| **Values:** | `30` (default) | positive scalar |
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

### **Steer and countersteer speed, steerRate [deg/s]** — Steer and countersteer rate `720` (default) | positive scalar

Steer and countersteer rate, in deg/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerRate` |
| **Values:** | `720` (default) | positive scalar |
| **Data Types:** | `double` |

### **Steer amplitude, steerAmp [deg]** — Handwheel steer amplitude `540` (default) | positive scalar

Steer amplitude, in deg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerAmp` |
| **Values:** | `540` (default) | positive scalar |
| **Data Types:** | `double` |

### **Use roll rate to determine initial steer dwell time** — Option to use roll rate to determine initial steer dwell time `off` (default) | `on`

Select this parameter to use the roll rate to determine the initial steer dwell
time.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `pFdbk` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Initial dwell time, tDwellSteer [s]** — Initial dwell time `0.5` (default) | positive scalar

Dwell period the initial steer amplitude is held, specified as a positive scalar, in
s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tDwellSteer` |
| **Values:** | `0.5` (default) | positive scalar |
| **Data Types:** | `double` |

### **Countersteer dwell time, tDwellCntrSteer [s]** — Countersteer dwell time `3` (default) | positive scalar

Dwell period for which the countersteer amplitude is held.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tDwellCntrSteer` |
| **Values:** | `3` (default) | positive scalar |
| **Data Types:** | `double` |

### **Return to center time, tZero [s]** — Time to return countersteer amplitude to zero steer `2` (default) | positive scalar

Time to return the countersteer amplitude to zero steer, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tZero` |
| **Values:** | `2` (default) | positive scalar |
| **Data Types:** | `double` |

### **Roll rate countersteer initiation zero crossing threshold, pZero [deg/s]** — Roll rate tolerance `1.5` (default) | positive scalar

Roll rate tolerance around zero from which to initiate the countersteer, in
deg/s.

#### Dependencies

To enable this parameter, select **Use roll rate to determine initial
steer dwell time**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `pZero` |
| **Values:** | `1.5` (default) | positive scalar |
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
## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Generate commands to conduct fishhook maneuver

The Fishhook block generates parametric steer and countersteer commands
upon reaching the target longitudinal velocity. Note that either time or roll rate feedback
can trigger the countersteer action, optimizing the severity of the countersteer. This
procedure is valuable for assessing rollover propensity and is typically parameterized by
conducting a Slowly Increasing Steer test initially to determine the steering
amplitude.
