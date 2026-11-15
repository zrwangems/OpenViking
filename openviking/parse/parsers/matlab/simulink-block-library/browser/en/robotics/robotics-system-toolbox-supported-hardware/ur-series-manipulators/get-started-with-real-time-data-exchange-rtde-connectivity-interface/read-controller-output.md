---
type: simulink-block
title: 'Read Controller Output'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'readcontrolleroutput'
documentation_source_path: 'urseries/ref/readcontrolleroutput.html'
language: en
---

# Read Controller Output

## Ports

### Output

### **q** — Current joint configuration numeric vector

Current joint configuration (in radians) of the cobot in the range [-2π,
2π], specified as a 1-by-6 vector.

**Data Types:** `double`

### **qd** — Current joint velocities numeric vector

Current joint velocities (in radians per second) of the cobot, specified as
a 1-by-6 vector.

#### Dependencies

To enable this port, select the **Enable joint velocity
output** parameter.

**Data Types:** `double`

### **qdd** — Current joint accelerations numeric vector

Current joint accelerations (in radians per second squared) of the cobot,
specified as a 1-by-6 vector.

#### Dependencies

To enable this port, select the **Enable joint acceleration
output** parameter.

**Data Types:** `double`

## Parameters

### **UR Controller IP address** — IP address of UR Controller `192.168.1.10` (default) | scalar

Specify the IP address of UR Controller corresponding to the UR Series cobot to
which you are establishing the connection.

### **Enable joint velocity output** — Obtain joint velocity through output port `off` (default) | on

Enable output port **qd** to obtain joint velocities.

### **Enable joint acceleration output** — Obtain joint acceleration through output port `off` (default) | on

Enable output port **qdd** to obtain joint accelerations.

### **Sample time** — Sample time `0.1` (default) | any non-negative value that is a multiple of 0.1 | `-1`

Enter the time interval at which the block reads values from the UR RTDE
Controller.

When you set this parameter to -1, Simulink determines the best sample time for
the block based on the block context within the model.

## Libraries

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Read specified signals from UR Controller using RTDE interface

The Read Controller Output block reads the specified output signals
generated from the UR Controller of the UR Series cobot using RTDE interface. The values
can be read for both trapezoidal or non-trapezoidal motion of the cobot.
