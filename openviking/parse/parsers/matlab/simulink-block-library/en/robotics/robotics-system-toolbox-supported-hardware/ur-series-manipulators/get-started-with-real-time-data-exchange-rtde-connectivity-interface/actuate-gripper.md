---
type: simulink-block
title: 'Actuate Gripper'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'actuategripper'
documentation_source_path: 'urseries/ref/actuategripper.html'
language: en
---

# Actuate Gripper

## Ports

### Input

### **Actuation** — Close or open the gripper `1` | `0`

The Actuation port is used to pass a logical value to actuate the gripper.
`1` closes the gripper and `0` opens the
gripper.

**Data Types:** `Boolean`

### **Enable** — Enable or disable gripper actuation `1` | `0`

The Enable port is used to pass a logical value to enable or disable the block to
perform gripper actuation. `1` enables the block to accept a value at
the **Actuation** input port, whereas `0` disables the
block.

**Data Types:** `Boolean`

## Parameters

### **UR Controller IP address** — IP address of UR Controller `192.168.1.10` (default) | scalar

Specify the IP address of UR Controller corresponding to the UR Series cobot to
which you are establishing the connection.

## Libraries

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Actuate gripper connected to cobot

The Actuate Gripper block actuates the gripper that is connected to UR
Series cobot. You can actuate Robotiq Vacuum Gripper or Robotiq 2-Finger Adaptive Robot
Gripper using this block.

**Note**

The simulation and deployment using this block is applicable only for connection to an
actual UR Series cobot and not to a simulated cobot using URSim.

By default, the gripper connection is disabled even though you successfully connect to
the cobot. To enable the connection to the gripper to receive commands for actuation, you
need to modify the `URServerScript.script` available with the support
package (for more details, refer to Load and Play UR Program on Hardware).
