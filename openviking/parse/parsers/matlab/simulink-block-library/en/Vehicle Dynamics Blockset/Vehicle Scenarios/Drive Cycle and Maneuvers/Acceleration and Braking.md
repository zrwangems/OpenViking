---
type: simulink-block
title: 'Acceleration and Braking'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'accelerationandbraking'
documentation_source_path: 'ref/accelerationandbraking.html'
language: en
---

# Acceleration and Braking

## Ports

### Input

### **xdot** — Vehicle longitudinal velocity scalar

Vehicle longitudinal velocity in the body fixed frame, specified as a scalar, in
m/s.

**Data Types:** `double`

### **r** — Vehicle yaw rate scalar

Vehicle yaw rate, specified as a scalar, in rad/s.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

**Data Types:** `double`

### **SteerCmd** — Vehicle handwheel angle scalar

Vehicle handwheel angle, specified as a scalar, in rad.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

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

Driver reference data, returned as a bus containing these block values.

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
| `DecelCmd` | Normalized decelerator or brake input. | one |
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

Block diagram where the Bus Assignment block overrides the TransModeCmd output from the Acceleration and Braking block.

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

### **Longitudinal acceleration at tStart, ax [g]** — Longitudinal acceleration at simulation start `0.5` (default) | positive scalar

Longitudinal acceleration at the simulation start time,
**tStart**, in m/s^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ax` |
| **Values:** | `0.5` (default) | positive scalar |
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

### **Brake pedal actuation** — Brake pedal actuation `Time` (default) | `Longitudinal displacement`

Method to start deceleration. To specify a time to start decelerating the vehicle,
select `Time`. To specify a displacement to start decelerating the
vehicle, select `Longitudinal displacement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brakingType` |
| **Values:** | `Time` (default) | `Longitudinal displacement` |
| **Data Types:** | `character vector` |

### **Brake actuation time, tBrake [s]** — Brake actuation time `15` (default) | positive scalar

Simulation time when braking is initiated, in s.

#### Dependencies

To enable this parameter, set **Brake pedal actuation** to
`Time`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tBrake` |
| **Values:** | `15` (default) | positive scalar |
| **Data Types:** | `double` |

### **Longitudinal displacement of vehicle CG, xBrake [m]** — Nominal lateral offset `200` (default) | positive scalar

The longitudinal displacement of the vehicle when braking is initiated, in
m.

#### Dependencies

To enable this parameter, set **Brake pedal actuation** to
`Longitudinal displacement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `xBrake` |
| **Values:** | `200` (default) | positive scalar |
| **Data Types:** | `double` |

### **Longitudinal deceleration at tBrake, axDecel [g]** — Deceleration rate `1` (default) | positive scalar

Deceleration rate when braking is initiated, in g.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `axDecel` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Set handwheel angle to 0 deg after braking** — Option to set handwheel angle to zero degrees after braking `on` (default) | `off`

Select this parameter to set the handwheel angle to zero degrees after
braking.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerZero` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

### Tracking Parameters

### **Enable fault tracking before braking** — Option to enable fault tracking before braking `off` (default) | `on`

Select this parameter to enable fault tracking before braking.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `faultTracking` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Transport delay buffer size, bufferSize []** — Transport delay buffer size `4096` (default) | positive scalar

Transport delay buffer size. This parameter is used for the online diagnostic
calculations. Use the simulation step size or hardware memory availability to specify
the buffer size.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bufferSize` |
| **Values:** | `4096` (default) | positive scalar |
| **Data Types:** | `double` |

### **Longitudinal velocity and mean longitudinal velocity, velMaxDiff** — Velocity difference `1` (default) | positive scalar

Maximum allowable difference between the longitudinal velocity and the mean
longitudinal velocity during the eight-second time interval prior to when braking is
initiated, in m/s.

Set value to comply with ISO 14512 for braking on surfaces with split coefficient
of friction.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `velMaxDiff` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Mean longitudinal velocity and longitudinal velocity reference, velMeanDiff** — Velocity tolerance `2` (default) | positive scalar

Maximum allowable difference between the mean longitudinal velocity and
longitudinal velocity reference during the eight-second time interval prior to when
braking is initiated, in m/s.

Set value to comply with ISO 14512 for braking on surfaces with split coefficient
of friction.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `velMeanDiff` |
| **Values:** | `2` (default) | positive scalar |
| **Data Types:** | `double` |

### **Yaw velocity and mean yaw velocity, rMaxDiff [deg/s]** — Velocity tolerance `1` (default) | positive scalar

Maximum allowable difference between the yaw velocity and mean yaw velocity during
the eight-second time interval prior to when braking is initiated, in deg/s.

Set value to comply with ISO 14512 for braking on surfaces with split coefficient
of friction.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rMaxDiff` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Handwheel angle and mean handwheel angle, steerMaxDiff [deg]** — Handwheel angle tolerance `3` (default) | positive scalar

Maximum allowable difference between the handwheel angle and the mean handwheel
angle during the eight-second time interval prior to when braking is initiated, in
deg.

Set value to comply with ISO 14512 for braking on surfaces with split coefficient
of friction.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `steerMaxDiff` |
| **Values:** | `3` (default) | positive scalar |
| **Data Types:** | `double` |

### **Stop Simulation when fault occurs** — Option to stop simulation when fault occurs `off` (default) | `on`

Select this parameter to stop simulation when fault occurs.

#### Dependencies

To enable this parameter, select **Enable fault tracking before
braking**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `stopOnFault` |
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

Generate steering, accelerator, and brake commands

The Acceleration and Braking block generates a straight reference
trajectory as a function of longitudinal displacement or time. Initial reference acceleration
and deceleration are tunable. Once the target longitudinal velocity is achieved, the block
executes a deceleration signal. This deceleration signal can be executed either with specified
time or longitudinal displacement.

An additional option for fault tracking allows you to monitor the uniformity of parameters
just before braking. The default set values are upper bounds for the standard split-mu test
(ISO Standard 141512).

**Note**

For information on the reference generator block used in the braking test reference
application, see Straight Maneuver Reference Generator.
