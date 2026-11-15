---
type: simulink-block
title: 'Accelerometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'accelerometer'
documentation_source_path: 'supportpkg/android_ref/accelerometer.html'
language: en
---

# Accelerometer

## Ports

### Output

### **X** — *X*-axis accelerometer data scalar

The block outputs the *X*-axis accelerometer data of the device.

**Data Types:** `single`

### **Y** — *Y*-axis accelerometer data scalar

The block outputs the *Y*-axis accelerometer data of the
device.

**Data Types:** `single`

### **Z** — *Z*-axis accelerometer data scalar

The block outputs the *Z*-axis accelerometer data of the
device.

**Data Types:** `single`

## Parameters

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block reads the
accelerometer sensor of the device and outputs the data.

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

Measure linear acceleration along X , Y , and Z axes in m/s 2

Use the Accelerometer block to measure linear acceleration along the
*X*, *Y*, and *Z* axes in
m/s2.

The following illustration shows the X, Y, and Z orientation axes relative to a typical
Android® mobile phone.

The following illustration shows the X, Y, and Z orientation axes relative to a typical
Android tablet.

The *X*, *Y*, and *Z* orientation axes
relative to the device remain constant. For example, if you place the device face-up on a
table, the *Z*-axis measures the acceleration of Earth gravity and outputs ≈
9.81 in m/s2. The *X* and *Y*
axes, which are perpendicular to the acceleration of Earth gravity, both output ≈ 0.00 in
m/s2.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
