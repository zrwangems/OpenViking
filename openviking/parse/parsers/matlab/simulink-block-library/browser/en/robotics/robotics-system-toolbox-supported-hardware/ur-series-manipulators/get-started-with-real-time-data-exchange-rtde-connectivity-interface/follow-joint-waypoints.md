---
type: simulink-block
title: 'Follow Joint Waypoints'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'followjointwaypoints'
documentation_source_path: 'urseries/ref/followjointwaypoints.html'
language: en
---

# Follow Joint Waypoints

## Ports

### Input

### **Waypoints** — Joint space waypoints to complete the trajectory numeric vector

Joint space waypoints (in radians) to complete the trajectory, specified as
a `N`-by-6 numeric vector, where `N` is the
dimension of the trajectory.

**Data Types:** `double`

### **Valid Waypoints** — Number of valid waypoints for the cobot to follow numeric scalar

Number of valid waypoints that you want the cobot to follow (N) if the
required joint space waypoints (using the **Waypoints** input port) is
not provided directly; but, they are generated from another block.

#### Dependencies

This port appears only if you select the parameter **Enable Valid
Number of Waypoints input port**.

.

**Data Types:** `double`

### **Waypoint Times** — Absolute time for each waypoint segment to complete the motion numeric vector

Absolute time (time from start), in seconds, for each waypoint segment to
complete the motion, specified as a 1-by-N numeric vector.

#### Dependencies

This port appears only if you select both these options:
`Trapezoidal Motion` for **Type of
Motion** and `Time-based control` for
**Mode of Control**.

.

**Data Types:** `double`

### **Enable** — Enable block to accept waypoints `1` | `0`

Enable the block and activate the motion of cobot based on joint waypoints.
Set the port to one of these values:

- `1` – Enable the block to accept
  **Waypoints** input and execute the motion
- `0` – Disable the block and ignore
  **Waypoints** input

**Data Types:** `Boolean`

## Parameters

### **UR Controller IP address** — IP address of UR Controller `192.168.1.10` (default) | scalar

Specify the IP address of UR Controller corresponding to the UR Series cobot to
which you are establishing the connection.

### **Cobot model** — Model name of UR Series cobot `UR5e` (default) | `UR3` | `UR3e` | `UR5` | `UR10` | `UR10e` | `UR16e`

Model name of UR Series cobot to which you are establishing the
connection.

### **Enable Valid Number of Waypoints input port** — Enable additional input port to specify number of valid waypoints `off` (default) | on

Enable additional input port **Valid Number of Waypoints** to specify
the number of valid waypoints (N) to consider if the **Waypoints** input
is generated from another block.

### **Type of motion** — Type of motion to consider for completing the trajectory `Smooth Motion` (default) | `Trapezoidal Motion`

Type of motion to consider for completing the trajectory based on the specified
joint space waypoints:

- If you select the `Smooth motion` option,
  either use the default value specified for **Blend radius for
  waypoints to pass through** parameter or specify a different
  value for this parameter. Specifying acceleration and velocity for smooth
  motion is optional and the can be done using the options under the
  **Motion Control** tab of the block.
- If you select the `Trapezoidal motion`
  option, use the **Mode of control** parameter to further
  select between acceleration and velocity control or time-based control,
  using the options under the **Motion Control** tab of
  the block.

### **Mode of control** — Mode of control for trapezoidal motion of the cobot `Acceleration and Velocity based Control` (default) | `Time-Based Control`

Mode of control for trapezoidal motion of the cobot based on the specified
joint space waypoints.

#### Dependencies

To enable this parameter, select the option `Trapezoidal
Motion` for the **Type of Motion**
parameter.

### **Blend radius for waypoints to pass through** — Blend radius for completing a smooth motion `0.05` (default) | numeric scalar

Blend radius (in meters) for completing a smooth motion of the cobot, based on
the joint waypoints input, specified as numeric scalar.

#### Dependencies

To enable this parameter, select the option `Smooth
Motion` for the **Type of Motion**
parameter.

### **Enable Acceleration input port** — Enable input port for acceleration `off` (default) | `on`

Enable additional input port for providing the acceleration value, for either
smooth motion or trapezoidal motion of cobot. Selecting this parameter disables
the option to manually enter acceleration value using the **Acceleration
to control speed profile** parameter.

#### Dependencies

This parameter appears for these options:

- Select `Smooth Motion` for **Type
  of Motion**
- Select `Trapezoidal Motion` for
  **Type of Motion** and select
  `Acceleration and Velocity based Control`
  for **Mode of Control**

### **Enable Velocity input port** — Enable input port for velocity `off` (default) | `on`

Enable additional input port for providing the velocity value, for either
smooth motion or trapezoidal motion of cobot. Selecting this parameter disables
the option to manually enter the velocity value using the **Velocity to
control speed profile** parameter.

#### Dependencies

This parameter appears for these options:

- Select `Smooth Motion` for **Type
  of Motion**
- Select `Trapezoidal Motion` for
  **Type of Motion** and select
  `Acceleration and Velocity based Control`
  for **Mode of Control**

### **Acceleration to control speed profile** — Acceleration to control speed profile `1` (default) | numeric scalar

Acceleration (in rad/s²) to control speed profile of the trajectory, specified
as a numeric scalar.

#### Dependencies

This parameter appears only if the **Enable Acceleration input
port** parameter is not selected.

### **Velocity to control speed profile** — Velocity to control speed profile `1` (default) | numeric scalar

Velocity (in rad/s) to control speed profile of the trajectory, specified as a
numeric scalar.

#### Dependencies

This parameter appears only if the **Enable Velocity input
port** parameter is not selected.

## Libraries

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Command UR Series cobot using the RTDE interface to follow a specified set of joint positions

The Follow Joint Waypoints block commands the UR Series cobot using the
RTDE interface to follow a specified set of joint positions for completing a trajectory.
The block allows you to select between smooth motion or trapezoidal motion, and provides
additional control options for trapezoidal motion.
