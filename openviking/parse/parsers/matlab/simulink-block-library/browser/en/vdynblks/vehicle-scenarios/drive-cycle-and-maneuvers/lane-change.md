---
type: simulink-block
title: 'Lane Change'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'lanechange'
documentation_source_path: 'ref/lanechange.html'
language: en
---

# Lane Change

## Ports

### Input

### **xdot** — Vehicle longitudinal velocity scalar

Vehicle longitudinal velocity in the body fixed frame, specified as a scalar, in
m/s.

**Data Types:** `double`

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

Block diagram where the Bus Assignment block overrides the TransModeCmd output from the Lane Change block.

**Data Types:** `bus`

### **Info** — Information data bus

Information data, returned as a bus containing these block values.

| Signal | Description | Units |
| --- | --- | --- |
| `LeftBnd` | Left lane boundary | m |
| `RightBnd` | Right lane boundary | m |
| `LtrlRef` | Lateral reference displacement | m |
| `XRef` | Vehicle global longitudinal reference position | m |
| `YRef` | Vehicle global lateral reference position | m |

#### Dependencies

To enable this parameter, select **Output info bus**.

**Data Types:** `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Lane change type, changeType** — Type of lane change to conduct `Double lane change (ISO 3888-1)` (default) | `Obstacle avoidance (ISO 3888-2)` | `Obstacle avoidance truck-trailer (SAE J2179)`

Type of lane change to conduct [[1],[2],[3],[4]].

Use the **Lane change type, changeType** parameter to select the desired lane change type.

| Action | Lane Change Type Setting |
| --- | --- |
| Simulate a double-lane change. The block holds the acceleration constant. | `Double lane change (ISO 3888-1)` |
| Simulate a lane change with obstacle avoidance. The block commands zero-acceleration. | `Obstacle avoidance (ISO 3888-2)` |
| Simulate a lane change with obstacle avoidance for a truck-trailer. The block does not override the acceleration command. | `Obstacle truck-trailer (SAE J2179)` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `changeType` |
| **Values:** | `Double lane change (ISO 3888-1)` (default) | `Obstacle avoidance (ISO 3888-2)` | `Obstacle avoidance truck-trailer (SAE J2179)` |
| **Data Types:** | `character vector` |

### **Maneuver start time, tStart [s]** — Start time `3` (default) | positive scalar

Maneuver start time, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tStart` |
| **Values:** | `3` (default) | positive scalar |
| **Data Types:** | `double` |

### **Inertial longitudinal position of gate extrance, XGate [m]** — Global longitudinal position of start of gate entry `176` (default) | scalar

Global longitudinal position of the start of the gate entry, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `XGate` |
| **Values:** | `176` (default) | scalar |
| **Data Types:** | `double` |

### **Longitudinal entrance velocity setpoint, velRef** — Target velocity `35` (default) | positive scalar

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

### **Longitudinal entrance velocity setpoint units, velRefUnit []** — Units `mph` (default)

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

### **Distance after target speed to begin reference, xStart [m]** — Longitudinal offset `2` (default) | scalar

Longitudinal offset from which to shift the nominal path, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `xStart` |
| **Values:** | `2` (default) | scalar |
| **Data Types:** | `double` |

### **Vehicle width, vehWidth [m]** — Nominal vehicle width `2` (default) | positive scalar

Nominal vehicle width, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `vehWidth` |
| **Values:** | `2` (default) | positive scalar |
| **Data Types:** | `double` |

### **Lateral offset, nomLatOffset [m]** — Nominal lateral offset `0` (default) | scalar

Nominal lateral offset, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `nomLatOffset` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Lateral reference position breakpoints, latRefbp [m]** — Longitudinal path breakpoints 1-by-*n* vector (default)

Longitudinal path breakpoints that correspond to the lateral reference points
**latRef**, specified as a 1-by-*n* vector, in
m.

#### Dependencies

To enable this parameter, set **Lane change type, changeType** to
one of these types:

- `Double lane change (ISO 3888-1)`
- `Obstacle avoidance (ISO 3888-2)`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `latRefbp` |
| **Values:** | 1-by-7 vector (default) |
| **Data Types:** | `double` |

### **Lateral reference data, latRef [m]** — Lateral path reference points 1-by-7 vector (default)

Lateral path reference points that correspond to the path longitudinal breakpoints
**latRefbp**, specified as a 1-by-7 vector, in m.

#### Dependencies

To enable this parameter, set **Lane change type, changeType** to
one of these types:

- `Double lane change (ISO 3888-1)`
- `Obstacle avoidance (ISO 3888-2)`

#### Dependencies

To enable this parameter, select **Use reference data**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `latRef` |
| **Values:** | 1-by-7 vector (default) |
| **Data Types:** | `double` |

### **Use reference data** — Option to use reference data `on` (default) | `off`

Select this parameter to use reference data.

#### Dependencies

To enable this parameter, set **Lane change type, changeType** to
one of these types:

- `Double lane change (ISO 3888-1)`
- `Obstacle avoidance (ISO 3888-2)`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `centerSwitch` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

### **Stop simulation on course exit** — Option to stop simulation on course exit `off` (default) | `on`

Select this parameter to stop simulation on course exit.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `xSimStop` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Output info bus** — Option to output info bus `off` (default) | `on`

Select this parameter to output info bus.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `extInfo` |
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

### **Show Maneuver Plot** — Option to visualize maneuver button

Click **Show Maneuver Plot** to visualize the maneuver specified by
**Lane change type, changeType**.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To do an ERT build, after specifying **System target file** as
`ert.tlc`, you must select the **Dynamic memory allocation in MATLAB functions
(Simulink)** parameter in the **Advanced
parameters** section of the **Simulation Target**
pane.

## Version History

**Introduced in R2024b**

### R2025a: Additional lane change type

Starting in R2025a, you can simulate a test maneuver to evaluate the performance of
obstacle avoidance for truck-trailers. To simulate this maneuver, set **Lane change
type, changeType** to `Obstacle avoidance truck-trailer (SAE
J2179)`.

## Description

Generate commands to conduct lane change maneuvers

The Lane Change block generates commands to conduct lane change maneuvers
and adjusts the acceleration command according to the selected maneuver, after the vehicle
reaches the target longitudinal velocity. Then, the block generates a lateral reference
trajectory as a function of the longitudinal displacement. The block also generates signals
indicating the left and right lane boundaries as a function of the specified track
width.

Use the **Lane change type, changeType** parameter to select the desired lane change type.

| Action | Lane Change Type Setting |
| --- | --- |
| Simulate a double-lane change. The block holds the acceleration constant. | `Double lane change (ISO 3888-1)` |
| Simulate a lane change with obstacle avoidance. The block commands zero-acceleration. | `Obstacle avoidance (ISO 3888-2)` |
| Simulate a lane change with obstacle avoidance for a truck-trailer. The block does not override the acceleration command. | `Obstacle truck-trailer (SAE J2179)` |

You must set the initial longitudinal position of the vehicle in your model to a
reasonable distance from the gate and specify these block parameters to ensure the vehicle
reaches the target velocity before arriving at the gate:

- **Inertial longitudinal position of gate entrance, XGate
  [m]**
- **Longitudinal entrance velocity setpoint, velRef**
- **Distance after target speed to begin reference, xStart
  [m]**

**Note**

For information on the reference generator block used in the double-lane change
reference application, see Reference Generator.
