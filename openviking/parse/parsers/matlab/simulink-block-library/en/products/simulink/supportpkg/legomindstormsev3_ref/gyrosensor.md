---
type: simulink-block
title: 'Gyro Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'gyrosensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/gyrosensor.html'
language: en
---

# Gyro Sensor

## Ports

### Output

### **Rotation** — Rate of rotation of gyro sensor scalar

The block outputs the rate of rotation of a gyro sensor connected to an EV3 brick
in degrees per second.

**Data Types:** `int32`

## Parameters

### **EV3 brick input port** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the gyro sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Sample time** — Time interval at which block reads sensor values `0.1` (default) | positive integer

Specify the frequency of how often the block reads sensor values connected to the
EV3 brick. Shorter sample times, such as `0.01`, may produce unreliable
measurements.

Smaller sample times require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Measure rate of rotation of gyro sensor connected to EV3 brick

Use the Gyro Sensor block to measure the rate of rotation of gyro sensor
connected to EV3 brick in degrees per second.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
