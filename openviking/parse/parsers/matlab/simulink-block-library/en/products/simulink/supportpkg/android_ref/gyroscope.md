---
type: simulink-block
title: 'Gyroscope'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'gyroscope'
documentation_source_path: 'supportpkg/android_ref/gyroscope.html'
language: en
---

# Gyroscope

## Ports

### Output

### **X** — *X*-axis gyroscope data scalar

The block outputs the *X*-axis gyroscope data of the
device.

**Data Types:** `single`

### **Y** — *Y*-axis gyroscope data scalar

The block outputs the *Y*-axis gyroscope data of the
device.

**Data Types:** `single`

### **Z** — *Z*-axis gyroscope data scalar

The block outputs the *Z*-axis gyroscope data of the
device.

**Data Types:** `single`

## Parameters

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block reads the gyroscope
sensor of the device and outputs the data.

**Note**

Smaller values for **Sample time** require the processor to
complete the same number of instructions in less time, which can cause task
overruns.

## Libraries

Simulink Support Package for Android Devices / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Measure rotational speed around X , Y , and Z axes in rad/s

Use the Gyroscope block measure rotational speed around
*X*, *Y*, and *Z* axes of the device.
This data is acquired from the gyroscope sensor of the device.

For any positive axis on the device, clockwise rotation outputs negative values, and
counterclockwise rotation outputs positive values. For example, if you place the device face
up on a table and spin it clockwise, the block outputs negative values for the
*Z*-axis.

The following illustration shows the orientation of the positive *X*,
*Y*, and *Z* axes for a typical Android® mobile phone.

The following illustration shows the orientation of the positive *X*,
*Y*, and *Z* axes for a typical Android tablet.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
