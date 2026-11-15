---
type: simulink-block
title: 'Read Joint Configuration'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'readjointconfiguration'
documentation_source_path: 'urseries/ref/readjointconfiguration.html'
language: en
---

# Read Joint Configuration

## Ports

### Output

### **q** — Current joint configuration numeric vector

Current joint configuration (in radians) of the cobot in the range [-2π,
2π], specified as a 1-by-6 vector.

**Data Types:** `double`

### **Status** — Status of read operation numeric scalar

Status of read operation, specified as a numeric scalar. The block outputs
the result as one of these values:

- **0** – read operation is successful
- **1** – read operation failed

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

Read current joint configuration from UR Controller using RTDE interface

The Read Joint Configuration block reads the current joint configuration
of the cobot from UR Controller using RTDE interface.
