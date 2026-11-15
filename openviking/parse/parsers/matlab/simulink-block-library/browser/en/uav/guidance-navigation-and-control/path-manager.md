---
type: simulink-block
title: 'Path Manager'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control'
documentation_page: 'pathmanager'
documentation_source_path: 'ref/pathmanager.html'
language: en
---

# Path Manager

## Ports

### Input

### **Pose** — Current UAV pose four-element column vector

Current UAV pose, specified as a four-element column vector of
`[x;y;z;courseAngle]`.
*x*, *y*, and *z* is the current
position of the UAV in north-east-down (NED) coordinates specified in meters.
*courseAngle* specifies the course angle in radians in the range
`[-pi, pi]`.

**Data Types:** `single` | `double`

### **MissionData** — UAV mission data `UAVPathManagerBus` bus

UAV mission data, specified as a `UAVPathManagerBus` bus. The
`UAVPathManagerBus` bus has the three bus elements
`mode`, `position`, and
`params`.

You can use the Constant (Simulink) block to specify the mission
data as an *n*-by-1 array of structures and set the output data type
to `Bus:UAVPathManagerBus`. *n* is the number of
mission points. The fields of each structure are:

- `mode` — Mode of the mission point, specified as an 8-bit
  unsigned integer between 1 and 6.
- `position` — Position of the mission point, specified as a
  three-element column vector of
  `[x;y;z]`.
  *x*, *y*, and *z* is the
  position in north-east-down (NED) coordinates specified in meters.
- `params` — Parameters of the mission point, specified as a
  four-element column vector.

The values assigned to the fields, in turn, are assigned to their corresponding
bus elements in the `UAVPathManagerBus` bus.

This table describes the types of `mode` and the corresponding
values for the `position` and `params` fields in a
mission point structure.

| `mode` | `position` | `params` | Mode description |
| --- | --- | --- | --- |
| `uint8(1)` | `[x;y;z]` | `[p1;p2;p3;p4]` | **Takeoff** — Take off from the ground and travel toward the specified position |
| `uint8(2)` | `[x;y;z]` | `[yaw;radius;p3;p4]`  *yaw* — Yaw angle in radians in the range `[-pi, pi]`  *radius* — Transition radius in meters | **Waypoint** — Navigate to waypoint |
| `uint8(3)` | `[x;y;z]`  *x*, *y*, and *z* is the center of the circular orbit in NED coordinates specified in meters | `[radius;turnDir;numTurns;p4]`  *radius* — Radius of the orbit in meters  *turnDir* — Turn direction, specified as one of these:  - `1` — Clockwise turn - `—1` — Counter-clockwise turn - `0` — Automatic selection of turn   direction    *numTurns* — Number of turns | **Orbit** — Orbit along the circumference of a circle defined by the parameters |
| `uint8(4)` | `[x;y;z]` | `[p1;p2;p3;p4]` | **Land** — Land at the specified position |
| `uint8(5)` | `[x;y;z]`  The launch position is specified in the `Home` input port | `[p1;p2;p3;p4]` | **RTL** — Return to launch position |
| `uint8(6)` | `[x;y;z]` | `[p1;p2;p3;p4]`  *p1*, *p2*, *p3*, and *p4* are user-specified parameters corresponding to a custom mission point | **Custom** — Custom mission point |

**Note**

*p1*, *p2*, *p3*, and
*p4* are user-specified parameters.

**Example:** `[struct('mode',uint8(1),'position',[0;0;100],'params',[0;0;0;0])]`

**Data Types:** `bus`

### **IsModeDone** — Determine if mission point was executed `0` (default) | `1`

Determine if the mission point was executed, specified as `0`
(`false`) or `1` (`true`).

**Data Types:** `Boolean`

### **MissionCmd** — Command to change mission `uint8(0)` (default) | 8-bit unsigned integer between 0 and 3

Command to change mission at runtime, specified as an 8-bit unsigned integer
between 0 and 3.

This table describes the possible mission commands.

| Mission Command | Description |
| --- | --- |
| `uint8(0)` | **Default** — Execute the mission from first to the last mission point in the sequence |
| `uint8(1)` | **Hold** — Hold at the current mission point  Loiter around the current position for fixed-wing and hover at the current position for multirotor UAVs |
| `uint8(2)` | **Repeat** — Repeat the mission after reaching the last mission point |
| `uint8(3)` | **RTL** — Execute return to launch (RTL) mode  After **RTL**, the mission resumes if the `MissionCmd` input is changed to **Default** or **Repeat** |

**Data Types:** `uint8`

### **Home** — UAV home location three-element column vector

UAV home location, specified as a three-element column vector of
`[x;y;z]`.
*x*, *y*, and *z* is the position
in north-east-down (NED) coordinates specified in meters.

**Data Types:** `single` | `double`
### Output

### **MissionParams** — UAV mission parameters `UAVPathManagerBus` bus

UAV mission parameters, returned as a 2-by-1 array of buses of the type
`UAVPathManagerBus`. The first element of the bus array is the
current mission point, and the second element of the bus array is the previous mission
point.

This table describes the output mission parameters depending on the mission
mode.

| Current Mission Mode | Output Mission Parameters | | | |
| --- | --- | --- | --- | --- |
| Mission Points | `mode` | `position` | `params` |
| **Takeoff** | First bus element: Current | `uint8(1)` | `[x;y;z]` | `[p1;p2;p3;p4]` |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |
| **Waypoint** | First bus element: Current | `uint8(2)` | `[x;y;z]` | `[yaw;radius;p3;p4]`  *yaw* — Yaw angle in radians in the range `[-pi, pi]`  *radius* — Transition radius in meters |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | - `[yaw;radius;p3;p4]`   if the previous mission point was   **Takeoff** - `[courseAngle;25;p3;p4]`   otherwise    *courseAngle* — Angle of the line segment between the previous and the current position, specified in radians in the range `[-pi, pi]` |
| **Orbit** | First bus element: Current | `uint8(3)` | `[x;y;z]`  *x*, *y*, and *z* is the center of the circular orbit in NED coordinates specified in meters | `[radius;turnDir;numTurns;p4]`  *radius* — Radius of the orbit in meters  *turnDir* — Turn direction, specified as one of these:  - `1` — Clockwise turn - `—1` — Counter-clockwise turn - `0` — Automatic selection of turn   direction    *numTurns* — Number of turns |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |
| **Land** | First bus element: Current | `uint8(4)` | `[x;y;z]` | `[p1;p2;p3;p4]` |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |
| **RTL** | First bus element: Current | `uint8(5)` | `[x;y;z]`  The launch position is specified in the `Home` input port | `[p1;p2;p3;p4]` |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |
| **Custom** | First bus element: Current | `uint8(6)` | `[x;y;z]` | `[p1;p2;p3;p4]`  *p1*, *p2*, *p3*, and *p4* are user-specified parameters corresponding to a custom mission point |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |

**Note**

*p1*, *p2*, *p3*, and
*p4* are user-specified parameters.

At start of simulation, the previous mission point is set to the
**Armed** mode.

| mode | position | params |
| --- | --- | --- |
| `uint8(0)` | `[x;y;z]`  `position` of the UAV at simulation start. | `[-1;-1;-1;-1]` |

Set the end mission point to **RTL** or **Land**
mode, else the end mission point is automatically set to **Hold**
mode.

This table describes the output mission parameters when the input to the
**MissionCmd** input port is set to **Hold**
mode.

| UAV Type | Output Mission Parameters | | | |
| --- | --- | --- | --- | --- |
| Mission Points | `mode` | `position` | `params` |
| **Multirotor** | First bus element: Current | `uint8(7)` | `[x;y;z]` | `[-1;-1;-1;-1]` |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |
| **Fixed-Wing** | First bus element: Current | `uint8(7)` | `[x;y;z]`  *x*, *y*, and *z* is the center of the circular orbit in NED coordinates specified in meters | `[radius;turnDir;-1;-1]`  *radius* — Loiter radius is specified in the `Loiter radius` parameter  *turnDir* — Turn direction is specified as `0` for automatic selection of turn direction |
| Second bus element: Previous | `mode` of the previous mission point | `position` of the previous mission point | `params` of the previous mission point |

**Data Types:** `bus`

## Parameters

### **UAV type** — Type of UAV `multirotor` (default) | `fixed-wing`

Type of UAV, specified as either `multirotor` or
`fixed-wing`.

**Tunable:** No

### **Loiter radius** — Loiter radius for fixed-wing UAV 25 (default) | positive numeric scalar

Loiter radius for the fixed-wing UAV, specified as a positive numeric scalar in
meters.

**Dependencies:** To enable this parameter, set the **UAV
type** parameter to `fixed-wing`.

**Tunable:** No

### **Data type** — Data type of input mission bus `double` (default) | `single`

Data type of the input mission bus, specified as either `double` or
`single`.

**Tunable:** No

### **Mission bus name** — Name of input mission bus `'UAVPathManagerBus'` (default)

Name of the input mission bus, specified as
`'UAVPathManagerBus'`.

**Tunable:** No

## Libraries

UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Compute and execute a UAV autonomous mission

The Path Manager block computes mission parameters for an unmanned aerial vehicle (UAV) by
sequentially switching between mission points specified in the
**MissionData** input port. The **MissionCmd** input port
changes the execution order at runtime. The block supports both multirotor and fixed-wing UAV
types.
