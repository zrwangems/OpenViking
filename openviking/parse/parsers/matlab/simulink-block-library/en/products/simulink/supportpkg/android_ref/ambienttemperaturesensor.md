---
type: simulink-block
title: 'Ambient Temperature Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'ambienttemperaturesensor'
documentation_source_path: 'supportpkg/android_ref/ambienttemperaturesensor.html'
language: en
---

# Ambient Temperature Sensor

## Ports

### Output

### **Port\_1** — Temperature data scalar

The block outputs the data read from the temperature sensor of the device.

**Data Types:** `single`

## Parameters

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block reads the
temperature sensor of the device and outputs the data.

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

Measure ambient temperature in degree Celsius

Use the Ambient Temperature Sensor block to measure ambient temperature in
degree Celsius from the temperature sensor on the Android® device.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
