---
type: simulink-block
title: 'PX4 Write Parameter'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4writeparameter'
documentation_source_path: 'px4/ref/px4writeparameter.html'
language: en
---

# PX4 Write Parameter

## Ports

### Input

### **Data** — Parameter data vector

Specify the data to write to the PX4 parameter.

**Data Types:** `int32` | `float`

## Parameters

### **Parameter Name** — Name of the PX4 parameter `SL_FLOAT_PARAM` (default) | one of the parameter name

Select the required PX4 system parameter from the drop-down list. The
**Parameter Name** selected in this field must be one of the
PX4 parameters; otherwise, the `Status` port outputs a value of
`1`, indicating that the parameter handle is invalid.
Additionally, parameters requiring a system reboot are not supported.

### **Data Type** — Data type of the PX4 parameter `FLOAT` (default)

The data type is autopopulated based on the parameter you selected in the
**Parameter Name** field.

**Note**

If the **Data type** that you select in this field does not
match the actual data type of the PX4 parameter, the values written might lead
to data type mismatch.

### **Output Status** — Status of data transmission `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port. The output status indicates if the parameter that you
specified is valid or not. A value of `0` indicates that the
parameter handle is valid, and a value of `1` indicates that the
parameter handle is invalid.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Write PX4 system parameters

The Write Parameter block writes to the PX4 system parameter you specify, allowing easy
parameter modification.

The block supports the parameters listed in PX4
Parameter Reference. You can also use your own custom parameters that align with
the PX4 guidelines. For more information, see PX4
guidelines.

During Connected IO simulation, this block writes data to the peripherals of the
hardware.
