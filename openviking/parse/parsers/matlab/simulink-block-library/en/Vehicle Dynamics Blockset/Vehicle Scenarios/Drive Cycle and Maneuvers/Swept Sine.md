---
type: simulink-block
title: 'Swept Sine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'sweptsine'
documentation_source_path: 'ref/sweptsine.html'
language: en
---

# Swept Sine

## Ports
```yaml
ports:
- name: xdot
  summary: Vehicle longitudinal velocity scalar
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
`TransCmd` bus to customize and extend the scenario.

Block diagram where the Bus Assignment block overrides the TransModeCmd output from the Swept Sine block.

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
  summary: Target velocity 30 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: velRef
  values: 30 (default) | positive scalar
- name: Longitudinal velocity setpoint units, velRefUnit []
  summary: Units mph (default)
  group: Maneuver Parameters
  block_parameter: velRefUnit
  values: mph (default) | character vector
- name: Steer amplitude, steerAmp [deg]
  summary: Handwheel steer amplitude 90 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: steerAmp
  values: 90 (default) | positive scalar
- name: Final frequency, steerFinalFreq [Hz]
  summary: Hold time after maximum steer amplitude reached 0.7 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: steerFreq
  values: 0.7 (default) | positive scalar
- name: Swept time, tSweep [s]
  summary: Duration of sweep procedure 30 (default) | positive scalar
  group: Maneuver Parameters
  block_parameter: tSweep
  values: 30 (default) | positive scalar
- name: Initial steer direction
  summary: Initial steer direction Right (default) | Left
  group: Maneuver Parameters
  block_parameter: steerDir
  values: Right (default) | Left
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

### **Steer amplitude, steerAmp [deg]** — Handwheel steer amplitude `90` (default) | positive scalar

Handwheel steer amplitude, in deg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerAmp` |
| **Values:** | `90` (default) | positive scalar |
| **Data Types:** | `double` |

### **Final frequency, steerFinalFreq [Hz]** — Hold time after maximum steer amplitude reached `0.7` (default) | positive scalar

Hold time after maximum steer amplitude is reached, in Hz.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerFreq` |
| **Values:** | `0.7` (default) | positive scalar |
| **Data Types:** | `double` |

### **Swept time, tSweep [s]** — Duration of sweep procedure `30` (default) | positive scalar

Duration of the sweep procedure, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tSweep` |
| **Values:** | `30` (default) | positive scalar |
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

Generate commands to conduct swept sine maneuver

The Swept Sine block generates steering, accelerator, and brake commands to
conduct a swept sine maneuver. Once the vehicle reaches the target longitudinal velocity, the
block initiates a swept sinusoidal steering command using the prescribed amplitude, final
frequency, and duration.

You can use the swept sine maneuver to characterize the transient vehicle response as done
in ISO 7401:2011.

**Note**

For information on the reference generator block used in the swept sine reference
application, see Swept Sine Reference Generator.
