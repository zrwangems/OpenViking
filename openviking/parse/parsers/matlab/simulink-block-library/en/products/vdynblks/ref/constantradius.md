---
type: simulink-block
title: 'Constant Radius'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'constantradius'
documentation_source_path: 'ref/constantradius.html'
language: en
---

# Constant Radius

## Ports

### Input

### **X** — Longitudinal position vehicle center of mass scalar

Longitudinal position of the vehicle center of mass in the global coordinate
frame, specified as a scalar, in m.

**Data Types:** `double`

### **Y** — Lateral position vehicle center of mass scalar

Lateral position of the vehicle center of mass in the global coordinate frame,
specified as a scalar, in m.

**Data Types:** `double`

### **psi** — Vehicle yaw angle scalar

Vehicle yaw angle with respect to the global coordinate system, specified as a
scalar, in m.

**Data Types:** `double`

### **ay** — Vehicle lateral acceleration scalar

Vehicle lateral acceleration needed to stop the simulation, specified as a scalar,
in gee.

#### Dependencies

To enable this parameter, select **Stop simulation at lateral
acceleration threshold**.

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

Block diagram where the Bus Assignment block overrides the TransCmd output from the Constant Radius block.

**Data Types:** `bus`

## Parameters

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

### **Longitudinal velocity setpoint, velRef** — Target velocity `35` (default) | positive scalar

Target velocity.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `velRef` |
| **Values:** | `35` (default) | positive scalar |
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

### **R** — Radius to be tracked `100` (default) | positive scalar

Radius to be tracked, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R` |
| **Values:** | `100` (default) | positive scalar |
| **Data Types:** | `double` |

### **Initial longitudinal position, X\_o [m]** — Initial longitudinal start point `0` (default) | scalar

Initial longitudinal start point of the circular reference in global coordinates, in
m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `X_o` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Initial lateral position, Y\_o [m]** — Initial lateral start point `0` (default) | scalar

Initial lateral start point of the circular reference in global coordinates, in
m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Y_o` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Initial yaw angle, psi\_o [rad]** — Starting heading angle `0` (default) | scalar

Starting heading angle of the circular reference in global coordinates, in
rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `psi_o` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Distance between inside and outside cone boundaries, radialConeDist [m]** — Radial distance between cones `6` (default) | positive scalar

Radial distance between cones, in m.

#### Dependencies

To enable this parameter, select **Instantiate 3D cones (Simulation 3D
Scene Configuration required)**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `radialConeDist` |
| **Values:** | `6` (default) | positive scalar |
| **Data Types:** | `double` |

### **Lateral acceleration absolute threshold, ayMax [g]** — Maximum allowable lateral acceleration before simulation is stopped `0.5` (default) | positive scalar

Maximum allowable lateral acceleration before the simulation is stopped, in
g.

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
| **Parameter:** | `ayMax` |
| **Values:** | `0.5` (default) | positive scalar |
| **Data Types:** | `double` |

### **Maneuver direction, steerDir** — Maneuver direction `Right` (default) | `Left`

Set the maneuver direction as `Right` or
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

Select this parameter to stop the simulation at the lateral acceleration
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

### **Instantiate 3D cones (Simulation 3D Scene Configuration required)** — Option to instantiate 3D cones `off` (default) | `on`

Select this parameter to instantiate 3D cones. The Simulation 3D Scene
Configuration block is required.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `use3DCones` |
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

Generate commands for tracking constant radius path

The Constant Radius block generates an open-loop longitudinal velocity
reference and a reference pose using vehicle feedback to track a constant radius path, which
is helpful to characterize a vehicle’s roll and understeer responses, usually at various
speeds. You can use these references directly with the Predictive Driver
block with the **Lateral control type, controlTypeLat** parameter set to
`Stanley`. You can also vary the radius and direction of travel and
optionally stop the simulation at a specified lateral acceleration limit.
