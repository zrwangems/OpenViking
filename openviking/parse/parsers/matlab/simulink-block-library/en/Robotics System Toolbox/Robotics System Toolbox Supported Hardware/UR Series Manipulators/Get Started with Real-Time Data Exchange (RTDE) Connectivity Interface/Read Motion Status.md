---
type: simulink-block
title: 'Read Motion Status'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'readmotionstatus'
documentation_source_path: 'urseries/ref/readmotionstatus.html'
language: en
---

# Read Motion Status

## Ports

### Output

### **Port\_1** — Status of motion of the cobot scalar

Status of motion of the cobot, specified as a scalar. The block outputs the
result as one of these values:

- **2** – motion is completed by the cobot
- **1** – motion execution is in progress
- **0** – motion has not started

**Data Types:** `double`

## Parameters

### **UR Controller IP address** — IP address of UR Controller `192.168.1.10` (default) | scalar

Specify the IP address of UR Controller corresponding to the UR Series cobot to
which you are establishing the connection.

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

Read motion status of cobot from UR Controller using RTDE interface

The Read Motion Status block reads motion status of cobot as read from UR
Controller using RTDE interface.
