---
type: simulink-block
title: 'Sine With Dwell'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'sinewithdwell'
documentation_source_path: 'ref/sinewithdwell.html'
language: en
---

# Sine With Dwell

## Ports

### Input

### **xdot** — Vehicle longitudinal velocity scalar

Vehicle longitudinal velocity in the body fixed frame, specified as a scalar, in
m/s.

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
| `TransCmd` | `TransModeCmd` | Command to specify the transmission mode | one |
| `GearCmd` | Command to specify manual gear number or automatic transmission shifter position | one |
| `UpShiftCmd` | Command to upshift | one |
| `DwnShiftCmd` | Command to downshift | one |
| `ClutchCmd` | Normalized clutch open command for manual transmissions | one |

**Note**

By default, the `TransCmd` bus is not actively used. Use a
Bus Assignment block to override the
`TransCmd` bus to customize and extend the scenario.

Block diagram where the Bus Assignment block overrides the TransModeCmd output from the Sine With Dwell block.

**Data Types:** `bus`

## Parameters

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

### **Steer frequency, steerFreq [Hz]** — Handwheel frequency `0.7` (default) | positive scalar

Handwheel frequency that defines the sine wave form, in Hz.

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

### **Steer amplitude, steerAmp [deg]** — Handwheel steer amplitude `90` (default) | positive scalar

Steer amplitude, in deg.

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

### **Countersteer dwell time, tDwellCntrSteer [s]** — Countersteer dwell time `0.5` (default) | positive scalar

Dwell period for which the countersteer amplitude is held.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tDwellCntrSteer` |
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

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Generate single sinusoidal steering command

The Sine With Dwell block generates a single sinusoidal steering command
with a pause at the ¾ period time point for the specified duration once the target
longitudinal velocity is reached, before returning to a neutral steer command. This behavior
simulates a rapid steer-countersteer scenario, representing a driver's actions to avoid an
obstacle and evaluates the electronic stability control system as per ISO 19365:2016. A
driving robot typically performs this procedure due to the required handwheel speed and the
test's need for repeatability.
