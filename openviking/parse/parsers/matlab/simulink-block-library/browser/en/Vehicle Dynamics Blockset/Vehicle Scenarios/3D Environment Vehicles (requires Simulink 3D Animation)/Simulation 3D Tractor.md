---
type: simulink-block
title: 'Simulation 3D Tractor'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dtractor'
documentation_source_path: 'ref/simulation3dtractor.html'
language: en
---

# Simulation 3D Tractor

## Ports

### Input

### **Translation** — Vehicle translation `7`-by-`3` array

Vehicle and wheel translation, in m. The array dimensions are
`7`-by-`3`, where:

- `Translation(1,1)`, `Translation(1,2)`,
  and `Translation(1,3)` — Vehicle translation along the inertial
  vehicle Z-down *X*-, *Y*-, and
  *Z*-axes, respectively.
- `Translation(...,1)`,
  `Translation(...,2)`, and `Translation(...,3)`
  — Wheel translation relative to vehicle, along the vehicle Z-down
  *X*-, *Y*-, and
  *Z*-axes, respectively.

The signal contains translation information according to the axle and wheel locations.

Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXMLYMLZMLXMRYMRZMRXRLYRLZRLXRRYRRZRR]

| Translation | Array Element | Translation Axis |
| --- | --- | --- |
| Vehicle, *Xv* | `Translation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Vehicle, *Yv* | `Translation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Vehicle, *Zv* | `Translation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Front left wheel, *XFL* | `Translation(2,1)` | Vehicle Z-down *X*-axis |
| Front left wheel, *YFL* | `Translation(2,2)` | Vehicle Z-down *Y*-axis |
| Front left wheel, *ZFL* | `Translation(2,3)` | Vehicle Z-down *Z*-axis |
| Front right wheel, *XFR* | `Translation(3,1)` | Vehicle Z-down *X*-axis |
| Front right wheel, *YFR* | `Translation(3,2)` | Vehicle Z-down *Y*-axis |
| Front right wheel, *ZFR* | `Translation(3,3)` | Vehicle Z-down *Z*-axis |
| Middle left wheel, *XML* | `Translation(4,1)` | Vehicle Z-down *X*-axis |
| Middle left wheel, *YML* | `Translation(4,2)` | Vehicle Z-down *Y*-axis |
| Middle left wheel, *ZML* | `Translation(4,3)` | Vehicle Z-down *Z*-axis |
| Middle right wheel, *XMR* | `Translation(5,1)` | Vehicle Z-down *X*-axis |
| Middle right wheel, *YMR* | `Translation(5,2)` | Vehicle Z-down *Y*-axis |
| Middle right wheel, *ZMR* | `Translation(5,3)` | Vehicle Z-down *Z*-axis |
| Rear left wheel, *XRL* | `Translation(6,1)` | Vehicle Z-down *X*-axis |
| Rear left wheel, *YRL* | `Translation(6,2)` | Vehicle Z-down *Y*-axis |
| Rear left wheel, *ZRL* | `Translation(6,3)` | Vehicle Z-down *Z*-axis |
| Rear right wheel, *XRR* | `Translation(7,1)` | Vehicle Z-down *X*-axis |
| Rear right wheel, *YRR* | `Translation(7,2)` | Vehicle Z-down *Y*-axis |
| Rear right wheel, *ZRR* | `Translation(7,3)` | Vehicle Z-down *Z*-axis |

### **Rotation** — Vehicle rotation `7`-by-`3` array

Vehicle and wheel rotation, in rad. The array dimensions are
`7`-by-`3`, where:

- `Rotation(1,1)`, `Rotation(1,2)`, and
  `Rotation(1,3)` — Vehicle rotation about the inertial vehicle
  Z-down *X*-, *Y*-, and
  *Z*-axes, respectively.
- `Rotation(...,1)`, `Rotation(...,2)`, and
  `Rotation(...,3)` — Wheel rotation relative to vehicle, about
  the vehicle Z-down *X*-, *Y*-, and
  *Z*-axes, respectively.

The signal contains rotation information according to the axle and wheel locations.

Rotation=[RollvPitchvYawvRollFLPitchFLYawFLRollFRPitchFRYawFRRollMLPitchMLYawMLRollMRPitchMRYawMRRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | Array Element | Rotation Axis |
| --- | --- | --- |
| Vehicle, *Rollv* | `Rotation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Vehicle, *Pitchv* | `Rotation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Vehicle, *Yawv* | `Rotation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Front left wheel, *RollFL* | `Rotation(2,1)` | Vehicle Z-down *X*-axis |
| Front left wheel, *PitchFL* | `Rotation(2,2)` | Vehicle Z-down *Y*-axis |
| Front left wheel, *YawFL* | `Rotation(2,3)` | Vehicle Z-down *Z*-axis |
| Front right wheel, *RollFR* | `Rotation(3,1)` | Vehicle Z-down *X*-axis |
| Front right wheel, *PitchFR* | `Rotation(3,2)` | Vehicle Z-down *Y*-axis |
| Front right wheel, *YawFR* | `Rotation(3,3)` | Vehicle Z-down *Z*-axis |
| Middle left wheel, *RollML* | `Rotation(4,1)` | Vehicle Z-down *X*-axis |
| Middle left wheel, *PitchML* | `Rotation(4,2)` | Vehicle Z-down *Y*-axis |
| Middle left wheel, *YawML* | `Rotation(4,3)` | Vehicle Z-down *Z*-axis |
| Middle right wheel, *RollMR* | `Rotation(5,1)` | Vehicle Z-down *X*-axis |
| Middle right wheel, *PitchMR* | `Rotation(5,2)` | Vehicle Z-down *Y*-axis |
| Middle right wheel, *YawMR* | `Rotation(5,3)` | Vehicle Z-down *Z*-axis |
| Rear left wheel, *RollRL* | `Rotation(6,1)` | Vehicle Z-down *X*-axis |
| Rear left wheel, *PitchRL* | `Rotation(6,2)` | Vehicle Z-down *Y*-axis |
| Rear left wheel, *YawRL* | `Rotation(6,3)` | Vehicle Z-down *Z*-axis |
| Rear right wheel, *RollRR* | `Rotation(7,1)` | Vehicle Z-down *X*-axis |
| Rear right wheel, *PitchRR* | `Rotation(7,2)` | Vehicle Z-down *Y*-axis |
| Rear right wheel, *YawRR* | `Rotation(7,3)` | Vehicle Z-down *Z*-axis |

## Parameters

#### Vehicle Parameters

### **Type** — Tractor type `Conventional tractor` (default) | `Cab-over tractor`

Type of tractor. For the dimensions, see:

- Cab-Over
  Tractor
- Conventional
  Tractor

### **Color** — Vehicle color `Red` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver` | `Dazzle camouflage`

Specify the vehicle color.

### **Name** — Name of vehicle `SimulinkVehicle1` (default) | character vector

Name of the vehicle. By default, when you use the block in your model, the block
sets the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of
Simulation 3D Vehicle with Ground Following and Simulation 3D
Vehicle blocks that you have in your model.

#### Initial Values

### **Initial array values to translate vehicle per part, Translation** — Vehicle initial translation zeros( 7, 3 ) (default) | `7`-by-`3` array

Initial vehicle and wheel translation, in m. The array dimensions are
`7`-by-`3`, where:

- `Translation(1,1)`, `Translation(1,2)`, and
  `Translation(1,3)` — Initial vehicle translation along the
  inertial vehicle Z-down coordinate system *X*-,
  *Y*-, and *Z*-axes, respectively.
- `Translation(...,1)`, `Translation(...,2)`,
  and `Translation(...,3)` — Initial wheel translation relative to
  the vehicle, along the vehicle Z-down *X*-,
  *Y*-, and *Z*-axes, respectively.

The parameter contains translation information according to the axle and wheel locations.

Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXMLYMLZMLXMRYMRZMRXRLYRLZRLXRRYRRZRR]

| Translation | Array Element | Translation Axis |
| --- | --- | --- |
| Vehicle, *Xv* | `Translation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Vehicle, *Yv* | `Translation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Vehicle, *Zv* | `Translation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Front left wheel, *XFL* | `Translation(2,1)` | Vehicle Z-down *X*-axis |
| Front left wheel, *YFL* | `Translation(2,2)` | Vehicle Z-down *Y*-axis |
| Front left wheel, *ZFL* | `Translation(2,3)` | Vehicle Z-down *Z*-axis |
| Front right wheel, *XFR* | `Translation(3,1)` | Vehicle Z-down *X*-axis |
| Front right wheel, *YFR* | `Translation(3,2)` | Vehicle Z-down *Y*-axis |
| Front right wheel, *ZFR* | `Translation(3,3)` | Vehicle Z-down *Z*-axis |
| Middle left wheel, *XML* | `Translation(4,1)` | Vehicle Z-down *X*-axis |
| Middle left wheel, *YML* | `Translation(4,2)` | Vehicle Z-down *Y*-axis |
| Middle left wheel, *ZML* | `Translation(4,3)` | Vehicle Z-down *Z*-axis |
| Middle right wheel, *XMR* | `Translation(5,1)` | Vehicle Z-down *X*-axis |
| Middle right wheel, *YMR* | `Translation(5,2)` | Vehicle Z-down *Y*-axis |
| Middle right wheel, *ZMR* | `Translation(5,3)` | Vehicle Z-down *Z*-axis |
| Rear left wheel, *XRL* | `Translation(6,1)` | Vehicle Z-down *X*-axis |
| Rear left wheel, *YRL* | `Translation(6,2)` | Vehicle Z-down *Y*-axis |
| Rear left wheel, *ZRL* | `Translation(6,3)` | Vehicle Z-down *Z*-axis |
| Rear right wheel, *XRR* | `Translation(7,1)` | Vehicle Z-down *X*-axis |
| Rear right wheel, *YRR* | `Translation(7,2)` | Vehicle Z-down *Y*-axis |
| Rear right wheel, *ZRR* | `Translation(7,3)` | Vehicle Z-down *Z*-axis |

### **Initial array values to rotate vehicle per part, Rotation** — Vehicle initial rotation zeros( 7, 3 ) (default) | `7`-by-`3` array

Initial vehicle and wheel rotation, about the vehicle Z-down
*X*-, *Y*-, and *Z*-axes, in
rad.

The array dimensions are `7`-by-`3`.

- `Rotation(1,1)`, `Rotation(1,2)`, and
  `Rotation(1,3)` — Initial vehicle rotation about the inertial
  vehicle Z-down coordinate system *X*-, *Y*-,
  and *Z*-axes, respectively.
- `Rotation(...,1)`, `Rotation(...,2)`, and
  `Rotation(...,3)` — Initial wheel rotation relative to the
  vehicle, about the vehicle Z-down *X*-,
  *Y*-, and *Z*-axes, respectively.

The parameter contains rotation information according to the axle and wheel locations.

Rotation=[RollvPitchvYawvRollFLPitchFLYawFLRollFRPitchFRYawFRRollMLPitchMLYawMLRollMRPitchMRYawMRRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | Array Element | Rotation Axis |
| --- | --- | --- |
| Vehicle, *Rollv* | `Rotation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Vehicle, *Pitchv* | `Rotation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Vehicle, *Yawv* | `Rotation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Front left wheel, *RollFL* | `Rotation(2,1)` | Vehicle Z-down *X*-axis |
| Front left wheel, *PitchFL* | `Rotation(2,2)` | Vehicle Z-down *Y*-axis |
| Front left wheel, *YawFL* | `Rotation(2,3)` | Vehicle Z-down *Z*-axis |
| Front right wheel, *RollFR* | `Rotation(3,1)` | Vehicle Z-down *X*-axis |
| Front right wheel, *PitchFR* | `Rotation(3,2)` | Vehicle Z-down *Y*-axis |
| Front right wheel, *YawFR* | `Rotation(3,3)` | Vehicle Z-down *Z*-axis |
| Middle left wheel, *RollML* | `Rotation(4,1)` | Vehicle Z-down *X*-axis |
| Middle left wheel, *PitchML* | `Rotation(4,2)` | Vehicle Z-down *Y*-axis |
| Middle left wheel, *YawML* | `Rotation(4,3)` | Vehicle Z-down *Z*-axis |
| Middle right wheel, *RollMR* | `Rotation(5,1)` | Vehicle Z-down *X*-axis |
| Middle right wheel, *PitchMR* | `Rotation(5,2)` | Vehicle Z-down *Y*-axis |
| Middle right wheel, *YawMR* | `Rotation(5,3)` | Vehicle Z-down *Z*-axis |
| Rear left wheel, *RollRL* | `Rotation(6,1)` | Vehicle Z-down *X*-axis |
| Rear left wheel, *PitchRL* | `Rotation(6,2)` | Vehicle Z-down *Y*-axis |
| Rear left wheel, *YawRL* | `Rotation(6,3)` | Vehicle Z-down *Z*-axis |
| Rear right wheel, *RollRR* | `Rotation(7,1)` | Vehicle Z-down *X*-axis |
| Rear right wheel, *PitchRR* | `Rotation(7,2)` | Vehicle Z-down *Y*-axis |
| Rear right wheel, *YawRR* | `Rotation(7,3)` | Vehicle Z-down *Z*-axis |

### **Sample time** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The
graphics frame rate is the inverse of the sample
time.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2024b: New Simulation 3D Tractor block color option

Starting in R2024b, you can specify **Color** as `Dazzle
Camouflage` for the Simulation 3D Tractor block.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Tractor block requires
Simulink
3D Animation.

## Description

Implement tractor in 3D environment

**Note**

Simulating models with the Simulation 3D Tractor block requires
Simulink®
3D Animation™.

The Simulation 3D Tractor block implements a tree-axle tractor in the 3D
simulation environment.

To use the Simulation 3D Tractor block, ensure that the Simulation
3D Scene Configuration block is in your model. If you set the **Sample
time** parameter of the Simulation 3D Tractor block to
`-1`, the block uses the sample time specified in the Simulation 3D
Scene Configuration block.

The block input uses the vehicle Z-down *right-handed* (RH)
*Cartesian* coordinate system defined in SAE
J6701. The coordinate system is inertial and initially aligned
with the vehicle geometric center:

- *X*-axis — Points forward along vehicle longitudinal axis
- *Y*-axis — Points to the right along vehicle lateral axis
- *Z*-axis — Points downward

**Tip**

Verify that the Simulation 3D Tractor
block executes before the Simulation 3D Scene Configuration block. That way,
Simulation 3D Vehicle prepares the signal data before the Unreal Engine® 3D visualization environment receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Tractor — `-1`

For more information about execution order, see Control and Display Execution Order.
