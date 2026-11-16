---
type: simulink-block
title: 'Vehicle Terrain Sensor'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Sensors (requires Simulink 3D Animation)'
documentation_page: 'vehicleterrainsensor'
documentation_source_path: 'ref/vehicleterrainsensor.html'
language: en
---

# Vehicle Terrain Sensor

## Ports

### Input

### **VehCntr** — Vehicle distance from center to front `scalar`

Distance from the vehicle center to front, *VehCntrLngthVal*, in
m.

#### Dependencies

| **Distance to vehicle center** | Creates Port | Creates Parameter |
| --- | --- | --- |
| `Constant` | None | **Distance from vehicle center to front, VehCntrLngthVal** |
| `External input` | `VehCntr` | *None* |

### **TireRadii** — Tire radii `array`

Tire radii, *TireRadiiVal*, in m.

#### Dependencies

| **Distance to tire center** Setting | Creates Port | Creates Parameter |
| --- | --- | --- |
| `Constant` | None | **Distance from tire center to ground, TireRadiiVal** |
| `External input` | `TireRadii` | None |
### Output

### **Info** — Bus signal bus

Bus signal containing block values. The signals are arrays that depend on the
wheel location.

| Signal | Description | Variable | Units |
| --- | --- | --- | --- |
| `HitFlg` | Vehicle and wheel hit flag:  - Hit an object – `1` - Miss an object – `0` | [VehicleFrontLeftFrontRightRearLeftRearRight] | NA |
| `HitLoc` | Vehicle, *HitLocVh*, and tire, *HitLocTr*, hit locations, in world coordinate system *X*-, *Y*, and *Z*- axes, respectively | [VehicleXVehicleYVehicleZFrontLeftXFrontLeftYFrontLeftZFrontRightXFrontRightYFrontRightZRearLeftXRearLeftYRearLeftZRearRearXRearRearYRearRearZ] | m |
| `StartLoc` | Vehicle, *StartLocVh*, and tire, *StartLocTr*, ray trace start locations, in world coordinate system *X*-, *Y*, and *Z*- axes, respectively | m |

### **VehHitDist** — Front of vehicle distance to object `scalar`

Distance from the front of the vehicle to object,
*DistToHitVhAdjust*, in m.

### **TireHitDist** — Tire distance to terrain `vector`

Distance from tire to terrain, *DistToHitTrAdjust*, in m.

*DistToHitTrAdjust* = [FrontLeftFrontRightRearLefRearRight]

## Parameters

#### Actor Setup

### **Tag for actor in 3D scene, ActorTag** — Name `SimulinVehicle1` (default) | character vector

Actor name.

Actors are scene objects that support 3D translation, rotation,
and scale. Parts are actor components. Components do not exist by themselves; they are
associated with an actor.

The block does not support multiple instances of the same actor tag. To refer to the same
scene actor when you use the 3D block pairs (e.g. Simulation 3D Actor Transform
Get and Simulation 3D Actor Transform Set), specify the same
**Tag for actor in 3D scene, ActorTag** parameter.

### **Distance to vehicle center** — Selection `Constant` (default) | `External input`

Configure how to provide the distance to the vehicle center.

#### Dependencies

| **Distance to vehicle center** | Creates Port | Creates Parameter |
| --- | --- | --- |
| `Constant` | None | **Distance from vehicle center to front, VehCntrLngthVal** |
| `External input` | `VehCntr` | *None* |

### **Distance to tire center** — Selection `Constant` (default) | `External input`

Configure how to provide the distance to the tire center.

#### Dependencies

| **Distance to tire center** Setting | Creates Port | Creates Parameter |
| --- | --- | --- |
| `Constant` | None | **Distance from tire center to ground, TireRadiiVal** |
| `External input` | `TireRadii` | None |

### **Distance from vehicle center to front, VehCntrLngthVal** — Vehicle center `0` (default) | `scalar`

Distance from the vehicle center to front, *VehCntrLngthVal*, in m.

#### Dependencies

| **Distance to vehicle center** | Creates Port | Creates Parameter |
| --- | --- | --- |
| `Constant` | None | **Distance from vehicle center to front, VehCntrLngthVal** |
| `External input` | `VehCntr` | *None* |

### **Distance from tire center to ground, TireRadiiVal** — Tire radii `0` (default) | `scalar`

Tire radius, *TireRadiiVal*, in m.

#### Dependencies

| **Distance to tire center** Setting | Creates Port | Creates Parameter |
| --- | --- | --- |
| `Constant` | None | **Distance from tire center to ground, TireRadiiVal** |
| `External input` | `TireRadii` | None |

#### Trace Lengths

### **Vehicle body x-axis trace length, VehRayLngth** — Trace length `5` (default) | `scalar`

Vehicle body trace length, *VehRayLngth*, in m.

### **Left front wheel z-axis trace length, LfRayLngth** — Trace length `5` (default) | `scalar`

Left front wheel trace length, *LfRayLngth* and
*LengthTr*, in m.

### **Right front wheel z-axis trace length, RfRayLngth** — Trace length `5` (default) | `scalar`

Right front wheel trace length, *RfRayLngth* and
*LengthTr*, in m.

### **Left rear wheel z-axis trace length, LrRayLngth** — Trace length `5` (default) | `scalar`

Left rear wheel trace length, *LrRayLngth* and
*LengthTr*, in m.

### **Right rear wheel z-axis trace length, RrRayLngth** — Trace length `5` (default) | `scalar`

Right rear wheel trace length, *RrRayLngth* and
*LengthTr*, in m.

#### Starting Point Offsets

### **Vehicle body x-axis trace offset, VehRayOffset** — Offset the vehicle ray trace `0` (default) | `scalar`

Vehicle body trace offset, *OffsetVh*, in m.

### **Left front wheel z-axis trace offset, LfRayOffset** — Offset the left front wheel ray trace `0` (default) | `scalar`

Left front wheel trace offset, *LfRayOffset* and
*OffsetTr*, in m.

### **Right front wheel z-axis trace offset, RfRayOffset** — Offset the right front wheel ray trace `0` (default) | `scalar`

Right front wheel trace offset, *RfRayOffset* and
*OffsetTr*, in m.

### **Left rear wheel z-axis trace offset, LrRayOffset** — Offset the left rear wheel ray trace `0` (default) | `scalar`

Left rear wheel trace offset, *LrRayOffset* and
*OffsetTr*, in m.

### **Right rear wheel z-axis trace offset, RrRayOffset** — Offset the right rear wheel ray trace `0` (default) | `scalar`

Right rear wheel trace offset, *RrRayOffset* and
*OffsetTr*, in m.

#### Enable Traces

### **Vehicle body** — Enable vehicle body ray tracing on (default) | off

Enable vehicle body ray tracing.

### **Left front tire** — Enable left front tire ray tracing on (default) | off

Enable left front tire ray tracing.

### **Right front tire** — Enable right front tire ray tracing on (default) | off

Enable right front tire ray tracing.

### **Left rear tire** — Enable left rear tire ray tracing on (default) | off

Enable left rear tire ray tracing.

### **Right rear tire** — Enable right rear tire ray tracing on (default) | off

Enable right rear tire ray tracing.

### **Trace line visualization** — Visualize ray traces on (default) | off

Enable trace line visualization.

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

**Introduced in R2018a**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Vehicle Terrain Sensor block requires
Simulink
3D Animation.

### R2024a: To be removed

The Vehicle Terrian Sensor block will be removed in a future release.
Instead, use the Simulation 3D Terrain
Sensor block to implement ray tracing to detect the terrain below vehicle
tires.

## Description

Vehicle and tire distances to objects

**Note**

Simulating models with the Vehicle Terrain Sensor block requires
Simulink®
3D Animation™.

The Vehicle Terrain Sensor block implements ray tracing to detect the
terrain below the tires and objects in front of the vehicle. Specifically, for these actor
components, the block returns the hit location (in the world coordinate system) and the
distance to an object.

- Vehicle body
- Left front wheel
- Right front wheel
- Left rear wheel
- Right rear wheel

**Tip**

Verify that the Vehicle Terrain Sensor
block executes before the Simulation 3D Fisheye Camera block. That way, the
Unreal Engine® 3D visualization environment prepares the data before the Vehicle
Terrain Sensor block receives it. To check the block execution order, right-click
the blocks and select **Properties**. On the **General**
tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Vehicle Terrain Sensor — `1`

For more information about execution order, see Control and Display Execution Order.

Actors are scene objects that support 3D translation, rotation,
and scale. Parts are actor components. Components do not exist by themselves; they are
associated with an actor.

### Hit Distance

To calculate the hit distances shown in the illustration, the
block implements these equations.

|  |  |
| --- | --- |
| Front of vehicle to object, *DistToHitVhAdjust* | ``` DistToHitVh = GetLength(CntrLocVh,HitLocVh) DistToHitVhAdjust = DistToHitVh - VehCntrLngthVal  EndLocVh = CntrLocVh + VehRayLngth - VehRayOffset VehRayOffset = CntrLocVh - StartLocVh VehRayLngth = StartLocVh - EndLocVh ``` |
| Tires to terrain, *DistToHitTrAdjust* | ``` DistToHitTr = GetLength(CntrLocTr, HitLocTr) DistToHitTrAdjust = DistToHitTr - TireRadiiVal  EndLocTr = CntrLocTr + LengthTr - OffsetTr OffsetTr = CntrLocTr - StartLocTr LengthTr = StartLocTr - EndLocTr ``` |

Image of vehicle showing object and terrain

This illustration and equations use these variables.

|  |  |
| --- | --- |
| *CntrLocVh* | Vehicle center location |
| *DistToHitVh* | Distance from vehicle center location to object |
| *DistToHitVhAdjust* | Distance from the front of the vehicle to object |
| *EndLocVh* | Vehicle ray trace end |
| *HitLocVh* | Vehicle hit location |
| *OffsetVh* | Vehicle trace offset |
| *StartLocVh* | Vehicle ray trace start |
| *VehRayLngth* | Vehicle trace length |
| *VehCntrLngthVal* | Distance from vehicle center to front |
| *CntrLocTr* | Tire center location |
| *DistToHitTr* | Distance from tire center location to terrain |
| *DistToHitTrAdjust* | Distance from tire to terrain |
| *HitLocTr* | Tire hit location |
| *EndLocTr* | Tire ray trace end |
| *OffsetTr* | Tire trace offset |
| *StartLocTr* | Tire ray trace start |
| *LengthTr* | Tire trace length |
| *TireRadiiVal* | Tire radius |

### Hit Event

To determine a hit event, the block uses the ray trace. The block provides the hit location in the world coordinate system.

Illustration of start location, hit location, and object

### Miss Event

To determine a miss event, the block uses the ray trace.

Illustration of start location and object
