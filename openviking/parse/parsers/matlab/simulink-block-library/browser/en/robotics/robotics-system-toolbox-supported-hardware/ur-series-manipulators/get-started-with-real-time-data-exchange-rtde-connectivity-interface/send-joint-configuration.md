---
type: simulink-block
title: 'Send Joint Configuration'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'sendjointconfiguration'
documentation_source_path: 'urseries/ref/sendjointconfiguration.html'
language: en
---

# Send Joint Configuration

## Ports

### Input

### **q** — Joint configuration to complete the trajectory numeric vector

Joint configuration (in radians) to complete the trajectory, specified as a
1-by-6 vector, where N is the dimension of the trajectory.

**Data Types:** `double`

### **Enable** — Enable block to accept joint configuration `1` | `0`

Enable the block and activate the motion of cobot based on joint waypoints.
Set the port to one of these values:

- `1` – Enable the block to accept **q** input
  and execute the motion
- `0` – Disable the block and ignore **q**
  input

**Data Types:** `Boolean`

## Parameters

### **UR Controller IP address** — IP address of UR Controller `192.168.1.10` (default) | scalar

Specify the IP address of UR Controller corresponding to the UR Series cobot to
which you are establishing the connection.

### **Wait until the motion is complete** — Wait until the motion is complete based on previous joint configuration `on` (default) | `off`

Wait until the motion of cobot is completed based on the previous joint
configuration sent to the cobot. When this parameter is selected, the send
operation runs in blocking mode (it suspends all the other MATLAB tasks from
running until the cobot's motion is completed). When you clear this parameter, the
send operation runs in the non-blocking mode.

### **Mode of control** — Mode of control for trapezoidal motion of the cobot `Time-Based Control` (default) | `Acceleration and Velocity based Control`

Mode of control for the trapezoidal motion of the cobot based on the specified
joint configuration.

### **Enable End Time input port** — Enable additional input port to specify end time `off` (default) | on

Enable additional input port **End Time** to specify the end time to
complete the motion. Selecting this parameter disables the option to manually
enter the end time value using the **End Time to complete the
motion** parameter.

#### Dependencies

This parameter appears only if you select `Time-Based
Control` for the **Mode of control**
parameter.

### **End Time to complete the motion** — End time to complete the motion based on the specified joint configuration `5` (default) | numeric scalar

End time (in seconds) to complete the cobot's motion based on the specified
joint configuration, specified as a numeric scalar.

#### Dependencies

This parameter appears only if the **Enable End Time input
port** parameter is not selected.

### **Enable Acceleration input port** — Enable input port for acceleration `off` (default) | `on`

Enable additional input port for providing the acceleration value. Selecting
this parameter disables the option to manually enter the acceleration value using
the **Acceleration to control speed profile** parameter.

#### Dependencies

This parameter appears only if you select `Acceleration and
Velocity based Control` for **Mode of
Control**.

### **Enable Velocity input port** — Enable input port for velocity `off` (default) | `on`

Enable additional input port for providing the velocity value. Selecting this
parameter disables the option to manually enter the velocity value using the
**Velocity to control speed profile** parameter.

#### Dependencies

This parameter appears only if you select `Acceleration and
Velocity based Control` for **Mode of
Control**.

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

Command the UR cobot using the RTDE interface to move to a specified joint configuration

The Send Joint Configuration block commands the UR cobot using the RTDE
interface to move to a specified joint configuration for completing a trajectory. The block
also allows you to specify additional constraints like end time, velocity or acceleration
to complete the motion; else, it uses default values for these constraints.

The block sends the commands either in blocking mode or in non-blocking mode. In
blocking mode, the model blocks the execution while it waits for the motion to complete. In
non-blocking mode, the model runs continuously.
