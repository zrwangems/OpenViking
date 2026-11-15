---
type: simulink-block
title: 'NXT Gyro Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'nxtgyrosensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/nxtgyrosensor.html'
language: en
---

# NXT Gyro Sensor

## Ports

### Output

### **Rotation** — Rate of rotation of gyro sensor scalar

The block outputs the rate of rotation of a gyro sensor connected to an EV3 brick
in degrees per second.

**Data Types:** `int32`

## Parameters

### **EV3 brick input port number** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the NXT gyro sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Output mode** — Sensor rotational data output `Rotation rate (-360 to 360)` (default) | `Raw A/D (1023 to 0)`

- `Rotation rate (-360 to 360)` — The block outputs the
  rate of rotation in degrees per second.
- `Raw A/D (1023 to 0)` — The block outputs the rate of
  rotation in raw analog-to-digital values per second.

### **Offset** — Sensor bias offset value `600` (default) | positive or negative integer

Enter the positive or negative sensor bias offset value. Use the value in this
parameter until the sensor bias is nearly zero.

#### Dependencies

- To enable this parameter, set **Output mode** to
  `Rotation rate (-360 to 360)`.

### **Sample time** — Time interval at which block reads sensor values `0.1` (default) | positive integer

Specify the frequency of how often the block reads sensor values connected to the
EV3 brick. Shorter sample times, such as `0.01`, may produce unreliable
measurements.

Smaller sample times require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware / NXT Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Measure rate of rotation of NXT gyro sensor connected to EV3 brick

Use the NXT Gyro Sensor  block to measure rate of rotation (yaw) along the
single axis of the HiTechnic NXT Gyro Sensor (NGY1044) connected to LEGO®
MINDSTORMS® EV3 brick. This yaw is indicated by a circle above the vertical axis in the
image on the left, and by a double-arrow in the image on the right. Before using this sensor
for precise measurements, use the offset value to remove small positive or negative bias in
the output values, as described in the example below. For more information on NXT Gyro Sensor
NGY1044, refer to its datasheet.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.

Lego NXT Gyro Sensor
