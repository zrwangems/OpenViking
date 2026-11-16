---
type: simulink-block
title: 'Simulation 3D Dolly'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3ddolly'
documentation_source_path: 'ref/simulation3ddolly.html'
language: en
---

# Simulation 3D Dolly

## Ports

### Input

### **Translation** — Dolly translation `5`-by-`3` array (default) | `8`-by-`3` array | `11`-by-`3` array

Dolly, axle, and wheel translation along the vehicle Z-down
*X*-, *Y*-, and *Z*- axes,
respectively, in m. Array dimensions depend on the **Type**
parameter.

| Type Parameter | Array Dimension |
| --- | --- |
| `One-axle dolly` (default) | `5`-by-`3` array |
| `Two-axle dolly` | `8`-by-`3` array |
| `Three-axle dolly` | `11`-by-`3` array |

The signal contains translation information according to the dolly, axle, and
wheel locations.

| **Signal Index** | Description |
| --- | --- |
| `Translation(1,1)`  `Translation(1,2)`  `Translation(1,3)` | Dolly translation, `Vehicle`, along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(2,1)`  `Translation(2,2)`  `Translation(2,3)` | Hitch socket, `HitchSocket`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(3,1)`  `Translation(3,2)`  `Translation(3,3)` | Axle one, `Axle1`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(4,1)`  `Translation(4,2)`  `Translation(4,3)` | Axle one left wheel, `Wheel_L1`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(5,1)`  `Translation(5,2)`  `Translation(5,3)` | Axle one right wheel, `Wheel_R1`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(6,1)`  `Translation(6,2)`  `Translation(6,3)` | Axle two, `Axle2`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(7,1)`  `Translation(7,2)`  `Translation(7,3)` | Axle two left wheel, `Wheel_L2`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(8,1)`  `Translation(8,2)`  `Translation(8,3)` | Axle two right wheel, `Wheel_R2`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(9,1)`  `Translation(9,2)`  `Translation(9,3)` | Axle three, `Axle3`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(10,1)`  `Translation(10,2)`  `Translation(10,3)` | Axle three left wheel, `Wheel_L3`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(11,1)`  `Translation(11,2)`  `Translation(11,3)` | Axle three right wheel, `Wheel_R3`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |

### **Rotation** — Dolly rotation `5`-by-`3` array (default) | `8`-by-`3` array | `11`-by-`3` array

Dolly, axle, and wheel rotation about the vehicle Z-down *X*-,
*Y*-, and *Z*- axes, respectively, in m. Array
dimensions depend on the **Type** parameter.

| Type Parameter | Array Dimension |
| --- | --- |
| `One-axle dolly` (default) | `5`-by-`3` array |
| `Two-axle dolly` | `8`-by-`3` array |
| `Three-axle dolly` | `11`-by-`3` array |

The signal contains rotation information according to the dolly, axle, and wheel
locations.

| **Signal Index** | Description |
| --- | --- |
| `Rotation(1,1)`  `Rotation(1,2)`  `Rotation(1,3)` | Dolly rotation, `Vehicle`, about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(2,1)`  `Rotation(2,2)`  `Rotation(2,3)` | Hitch socket, `HitchSocket`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(3,1)`  `Rotation(3,2)`  `Rotation(3,3)` | Axle one, `Axle1`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(4,1)`  `Rotation(4,2)`  `Rotation(4,3)` | Axle one left wheel, `Wheel_L1`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(5,1)`  `Rotation(5,2)`  `Rotation(5,3)` | Axle one right wheel, `Wheel_R1`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(6,1)`  `Rotation(6,2)`  `Rotation(6,3)` | Axle two, `Axle2`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(7,1)`  `Rotation(7,2)`  `Rotation(7,3)` | Axle two left wheel, `Wheel_L2`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(8,1)`  `Rotation(8,2)`  `Rotation(8,3)` | Axle two right wheel, `Wheel_R2`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(9,1)`  `Rotation(9,2)`  `Rotation(9,3)` | Axle three, `Axle3`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(10,1)`  `Rotation(10,2)`  `Rotation(10,3)` | Axle three left wheel, `Wheel_L3`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(11,1)`  `Rotation(11,2)`  `Rotation(11,3)` | Axle three right wheel, `Wheel_R3`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |

## Parameters

### Vehicle Parameters

### **Type** — Type `One-axle dolly` (default) | `Two-axle dolly` | `Three-axle dolly`

Use the **Type** parameter to
specify the number of axles on the dolly. This table provides links to the dolly
dimensions.

| **Type** Setting | Dolly Dimensions |
| --- | --- |
| `One-axle dolly` | One-Axle Dolly |
| `Two-axle dolly` | Two-Axle Dolly |
| `Three-axle dolly` | Three-Axle Dolly |

### **Name** — Name of dolly `SimulinkVehicle1` (default) | character vector

Name of dolly. By default, when you use the block in your model, the block sets
the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of
simulation 3D vehicle blocks that you have in your model.

### **Sample time** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The
graphics frame rate is the inverse of the sample
time.

### Initial Values

### **Initial array values to translate vehicle per part, Translation** — Vehicle initial translation zeros( 5, 3 ) (default) | zeros( 8, 3 ) | zeros( 11, 3 )

Initial dolly, axle, and wheel translation along the vehicle Z-down
*X*-, *Y*-, and *Z*- axes,
respectively, in m. Array dimensions depend on the **Type**
parameter.

| Type Parameter | Array Dimension |
| --- | --- |
| `One-axle dolly` (default) | `5`-by-`3` array |
| `Two-axle dolly` | `8`-by-`3` array |
| `Three-axle dolly` | `11`-by-`3` array |

The parameter contains the initial translation values according to the dolly,
axle, and wheel locations.

| **Signal Index** | Description |
| --- | --- |
| `Translation(1,1)`  `Translation(1,2)`  `Translation(1,3)` | Dolly translation, `Vehicle`, along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(2,1)`  `Translation(2,2)`  `Translation(2,3)` | Hitch socket, `HitchSocket`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(3,1)`  `Translation(3,2)`  `Translation(3,3)` | Axle one, `Axle1`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(4,1)`  `Translation(4,2)`  `Translation(4,3)` | Axle one left wheel, `Wheel_L1`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(5,1)`  `Translation(5,2)`  `Translation(5,3)` | Axle one right wheel, `Wheel_R1`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(6,1)`  `Translation(6,2)`  `Translation(6,3)` | Axle two, `Axle2`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(7,1)`  `Translation(7,2)`  `Translation(7,3)` | Axle two left wheel, `Wheel_L2`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(8,1)`  `Translation(8,2)`  `Translation(8,3)` | Axle two right wheel, `Wheel_R2`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(9,1)`  `Translation(9,2)`  `Translation(9,3)` | Axle three, `Axle3`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(10,1)`  `Translation(10,2)`  `Translation(10,3)` | Axle three left wheel, `Wheel_L3`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Translation(11,1)`  `Translation(11,2)`  `Translation(11,3)` | Axle three right wheel, `Wheel_R3`, translation along the vehicle Z-down *X*-, *Y*-, and *Z*- axes |

### **Initial array values to rotate vehicle per part, Rotation** — Initial rotation zeros( 5, 3 ) (default) | zeros( 8, 3 ) | zeros( 11, 3 )

Initial dolly, axle, and wheel rotation about the vehicle Z-down
*X*-, *Y*-, and *Z*- axes,
respectively, in m. Array dimensions depend on the **Type**
parameter.

| Type Parameter | Array Dimension |
| --- | --- |
| `One-axle dolly` (default) | `5`-by-`3` array |
| `Two-axle dolly` | `8`-by-`3` array |
| `Three-axle dolly` | `11`-by-`3` array |

The parameter contains the initial rotation values according to the dolly, axle,
and wheel locations.

| **Signal Index** | Description |
| --- | --- |
| `Rotation(1,1)`  `Rotation(1,2)`  `Rotation(1,3)` | Dolly rotation, `Vehicle`, about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(2,1)`  `Rotation(2,2)`  `Rotation(2,3)` | Hitch socket, `HitchSocket`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(3,1)`  `Rotation(3,2)`  `Rotation(3,3)` | Axle one, `Axle1`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(4,1)`  `Rotation(4,2)`  `Rotation(4,3)` | Axle one left wheel, `Wheel_L1`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(5,1)`  `Rotation(5,2)`  `Rotation(5,3)` | Axle one right wheel, `Wheel_R1`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(6,1)`  `Rotation(6,2)`  `Rotation(6,3)` | Axle two, `Axle2`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(7,1)`  `Rotation(7,2)`  `Rotation(7,3)` | Axle two left wheel, `Wheel_L2`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(8,1)`  `Rotation(8,2)`  `Rotation(8,3)` | Axle two right wheel, `Wheel_R2`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(9,1)`  `Rotation(9,2)`  `Rotation(9,3)` | Axle three, `Axle3`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(10,1)`  `Rotation(10,2)`  `Rotation(10,3)` | Axle three left wheel, `Wheel_L3`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |
| `Rotation(11,1)`  `Rotation(11,2)`  `Rotation(11,3)` | Axle three right wheel, `Wheel_R3`, rotation about the vehicle Z-down *X*-, *Y*-, and *Z*- axes |

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Dolly block requires
Simulink
3D Animation.

## Description

Implement dolly in 3D environment

**Note**

Simulating models with the Simulation 3D Dolly block requires
Simulink®
3D Animation™.

The Simulation 3D Dolly block implements a dolly in the 3D simulation
environment.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of this block to
`-1`, the block uses the sample time specified in the Simulation 3D
Scene Configuration block.

The block input uses the vehicle Z-down *right-handed* (RH)
*Cartesian* coordinate system defined in SAE
J6701. The coordinate system is inertial and initially aligned
with the vehicle geometric center:

- *X*-axis — Along vehicle longitudinal axis, points forward
- *Y*-axis — Along vehicle lateral axis, points to the right
- *Z*-axis — Points downward

**Tip**

Verify that the Simulation 3D Dolly
block executes before the Simulation 3D Scene Configuration block. That way,
Simulation 3D Dolly prepares the signal data before the Unreal Engine® 3D visualization environment receives it. To check the block execution order,
right-click each block and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Dolly — `-1`

For more information about execution order, see Control and Display Execution Order.
