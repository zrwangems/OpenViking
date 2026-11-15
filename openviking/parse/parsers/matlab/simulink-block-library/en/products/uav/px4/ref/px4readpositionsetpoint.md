---
type: simulink-block
title: 'PX4 Read Position Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4readpositionsetpoint'
documentation_source_path: 'px4/ref/px4readpositionsetpoint.html'
language: en
---

# PX4 Read Position Setpoint

## Ports

### Output

### **Previous** — Coordinates of last traversed setpoint by vehicle Vector

This port outputs the coordinates of the last traversed setpoint by the vehicle
either in the WGS84 (latitude, longitude, and altitude) coordinate system or as local
coordinates (`x`, `y`, and `z`) in
the NED and ENU coordinate systems.

**Data Types:** `double`

### **Current** — Coordinates of current destination setpoint of vehicle Vector

This port outputs the coordinates of the current destination setpoint of the
vehicle either in the WGS84 (latitude, longitude, and altitude) coordinate system or
as local coordinates (x, y, and z) in NED and ENU coordinate systems.

**Data Types:** `double`

### **Next** — Coordinates of next setpoint of vehicle Vector

This port outputs the coordinates of the next setpoint after the current
destination of the vehicle either in the WGS84 (latitude, longitude, and altitude)
coordinate system or as local coordinates (x, y, and z) in NED and ENU coordinate
systems.

**Data Types:** `double`

### **Type** — Waypoint mode for the Current setpoint Scalar

The **Type** output port provides information on the waypoint
mode or mission command for the current setpoint that is set in the mission created
and uploaded from QGroundControl. The port outputs one of the following types.

| Waypoint Type or Mission Command | Type Output |
| --- | --- |
| Takeoff | `3` |
| Land | `4` |
| Waypoint | `0` |
| Loiter | `2` |
| Idle | `5` |

**Data Types:** `uint8`

### **Position Setpoint** — Simulink bus for the position\_setpoint\_triplet uORB topic Bus

This port outputs the Simulink bus for the `position_setpoint_triplet uORB` topic. Use
this port to avail other information that is published as part of the
`position_setpoint_triplet` topic by the navigator module.

#### Dependencies

To enable this port, select the **Output Simulink bus for
position\_setpoint\_triplet** parameter.

**Data Types:** `Bus`

### **Trajectory Waypoint** — Simulink bus for the vehicle\_trajectory\_waypoint uORB topic Bus

This port outputs the Simulink bus for the `vehicle_trajectory_waypoint uORB` topic.
Use this port to avail other information that is published as part of the
`vehicle_trajectory_waypoint` topic such as yaw setpoint, velocity
setpoint and so on.

#### Dependencies

To enable this port, select the **Output Simulink bus for
vehicle\_trajectory\_waypoint** parameter.

**Data Types:** `Bus`

### **Onboard Failsafe** — failsafe flag for onboard computer Boolean

The port returns value `1` when there is no new waypoint received
from the onboard computer during the last `0.5` seconds. Use this
flag to enable any specific onboard failsafe action that is modelled with the
controller.

#### Dependencies

To enable this port, select the **Output onboard computer failsafe
flag** parameter.

**Data Types:** `Boolean`

### **Onboard Status** — Onboard computer enabled status Boolean

This port outputs the status flag to indicate if the onboard computer workflow is
enabled or not.

The port returns value `1` when the onboard computer is enabled
with PX4 and `0` otherwise.

#### Dependencies

To enable this port, select the **Output onboard computer enabled
status** parameter.

**Data Types:** `Boolean`

## Parameters

#### Main

### **coordinate Format** — Coordinate system for setpoints `Local Coordinates (NED)` (default) | `WGS84` | `Local Coordinates (ENU)`

Use this port to specify the desired coordinate format for the previous, current and
next waypoints. The format can be specified as one of the following:

- `Local Coordinates (NED)`: Use this option to output
  the previous, current, and next setpoints as local coordinates (x, y, and z) in the
  NED frame. The transformation method that is used to convert the Geodetic
  coordinates provided by the PX4 to local coordinates is
  *flat*.
- `Local Coordinates (ENU)`: Use this option to output
  the previous, current, and next setpoints as local coordinates
  (`x`, `y`, and `z`) in the ENU
  frame. The transformation method that is used to convert the Geodetic coordinates
  provided by PX4 to local coordinates is *flat*.
- `WGS84`: Use this option to output the previous,
  current, and next setpoints as the original Geodetic coordinates (latitude,
  longitude, and altitude) returned by PX4.

### **Sample time** — Interval between outputs `0.01` (default) | any nonnegative integer that is a multiple of 0,001 | `-1`

Specify the time interval at which the block reads values from the uORB network.
When you specify this parameter as `-1`, Simulink determines the best
sample time for the block based on the context of the block within the model.

#### Advanced

### **Output Simulink bus for position\_setpoint\_triplet** — Bus for position\_setpoint\_triplet uORB topic `off` (default) | `on`

Select this parameter to enable **Position Setpoint** port. This
port contains the full Simulink bus for the `position_setpoint_triplet`
uORB topic. Use this port to avail other information that is published as part of the
position\_setpoint\_triplet topic by the navigator module.

### **Output Simulink bus for vehicle\_trajectory\_waypoint** — Bus for vehicle trajectory waypoint `off` (default) | `on`

Select this parameter to enable **Trajectory Waypoint**
port.

### **Output onboard computer failsafe flag** — Onboard computer failsafe flag status `off` (default) | `on`

Select this parameter to enable **Onboard Failsafe** port. Use this
port to model your own failsafe condition.

### **Output onboard computer enabled status** — Onboard computer enable status `off` (default) | `on`

Select this parameter to enable **Onboard Status** port.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Read the position setpoints published by the PX4 Navigator module in the uORB topic position_setpoint_triplet

The PX4 Read Position Setpoint block outputs the position setpoints
published by the PX4 navigator module in the `position_setpoint_triplet` uORB
topic. The block outputs the coordinates of the current destination setpoint (Current), the
next setpoint after the current destination (Next) and the most recent setpoint that was
traversed (Previous). The block outputs the Previous, Current and Next position setpoints as
coordinates in either the World Geodetic System of 1984 (WGS 84), local north-east-down (NED),
or local east-north-up (ENU) coordinate systems.

You can create an autonomous mission in the plan view of the QGroundControl (QGC) and
upload the mission to the PX4 Autopilot over MAVLink. For information on creating missions,
see Plan View. The mission consists of waypoints such as TakeOff, Position (also known
as Waypoint), Land and so on. The MAVLink module on the PX4 Autopilot decodes the mission data
and stores it in the memory. The navigator module in PX4 retrieves the waypoints from the
onboard memory and publishes them in the `position_setpoint_triplet` uORB
topic. The Previous, Current, and Next setpoints are automatically updated by the navigator
module when the vehicle reaches those waypoints.

**Note**

If the onboard companion computer is enabled with PX4 (PX4 parameter COM\_OBS\_AVOID is
set to 1), the current waypoint will be updated using the waypoint data received from the
onboard computer. The updated waypoint from the onboard computer is communicated to PX4
using the Path
Planning Interface over MAVLink. The PX4 MAVLink module receives the waypoint and
publishes the waypoint in vehicle\_trajectory\_waypoint uORB topic. When onboard computer
workflow is enabled, this block reads the waypoint from vehicle\_trajectory\_waypoint uORB
topic and outputs it as current waypoint.

The block also outputs the waypoint mode for the current position setpoint which indicates
the corresponding waypoint type that has been set in the mission uploaded from QGroundControl
(QGC). This helps in distinguishing the Current Waypoint types (TakeOff, Waypoint, Land) in
Simulink®.

Feed the coordinates that the block outputs directly to the controller algorithm designed
in Simulink as input commands. Use the **Type** output to distinguish between
waypoints and take corresponding appropriate action in the controller.

This block also reads the setpoint data for missions created in the QGC, for which the
mission type is Flight plan. However, you cannot use this block to read setpoint data for
geofencing and rally missions.

Among the flight plan missions, the supported mission commands whose waypoint data can be
retrieved by the block are Takeoff, Land and Waypoint. Return to Launch (RTL) is not
supported.

**Note**

The PX4 Read Position Setpoint block is supported only when you select
**Use default startup script (rcS)** as the startup script option for the
PX4 Autopilot during the **Select System Startup Script in PX4** step of
the Hardware Setup process. For more information, see Selecting Startup Script for PX4 Autopilot.

**Note**

The PX4 Read Position Setpoint block requires you to connect an SD card
to the PX4 Autopilot. Ensure that the connected SD card does not contain any custom startup
script (rc.txt) in the `etc` folder.

**Note**

The PX4 Read Position Setpoint  block cannot determine if the ongoing
mission in QGroundControl is paused. You need to find a separate logic to determine if the
mission is paused in QGroundControl.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
