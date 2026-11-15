---
type: simulink-block
title: 'NXT Touch Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'nxttouchsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/nxttouchsensor.html'
language: en
---

# NXT Touch Sensor

## Ports

### Output

### **Status** — Status of NXT touch sensor `0` | `1`

The block outputs the status of the LEGO
MINDSTORMS EV3 NXT touch sensor.

- `0` — Indicates that the NXT touch sensor is not
  pressed.
- `1` — Indicates that the NXT touch sensor is
  pressed.

**Data Types:** `uint8`

## Parameters

### **EV3 brick input port number** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the NXT touch sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Sample time** — Time interval at which block reads EV3 brick touch sensor status `0.1` (default) | positive integer

Specify the frequency of how often the block reads the NXT touch sensor status.
Shorter sample times, such as `0.01`, may produce unreliable
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

Detect status of EV3 brick NXT touch sensor

Use the NXT Touch Sensor block to detect whether the NXT touch sensor
connected to the LEGO®
MINDSTORMS® EV3 brick is pressed or not.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
