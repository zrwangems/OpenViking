---
type: simulink-block
title: 'Read Parameter'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'readparameter'
documentation_source_path: 'px4/ref/readparameter.html'
language: en
---

# Read Parameter

## Ports

### Output

### **Data** — Value of the parameter scalar

Value of the specified PX4 system parameter

**Data Types:** `int32` | `float`

### **Status** — Status of the received parameter value `0` | `1`

The Status output indicates if the parameter that you specified is valid or not. A
value of `0` indicates that the parameter handle is valid, and a
value of `1` indicates that the parameter handle is invalid.

**Data Types:** `Boolean`

## Parameters

### **Parameter Name** — Name of the PX4 parameter `ATT_BIAS_MAX` (default) | One of the parameter

Enter the name of the PX4 system parameter.

**Note**

The **Parameter Name** that you enter in this field must match
one of the PX4 parameters; otherwise, the `Status` port outputs
`1`, indicating that the parameter handle is invalid.

### **Data Type** — Data type of the PX4 parameter `FLOAT` (default) | int32

Select the data type of the parameter that you entered in the `Parameter
Name` field.

**Note**

If the **Data type** that you select in this field does not match
the actual data type of the PX4 parameter, the values read may lead to data type
mismatch.

### **Sample time** — Interval at which the block reads values `0.5` (default) | any non-negative value that is a multiple of 0.5 | -1

Enter the time interval at which the block reads values from the uORB
network.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read PX4 system parameters

The Read Parameter block reads the specified PX4 system parameter, and provides its value
as output.

The block supports all parameters listed in PX4
Parameter Reference page. You can also use custom parameters that you have developed
using the guidelines.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
