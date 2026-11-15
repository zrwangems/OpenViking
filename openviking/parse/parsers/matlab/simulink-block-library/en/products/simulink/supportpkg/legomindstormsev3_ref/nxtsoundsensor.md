---
type: simulink-block
title: 'NXT Sound Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'nxtsoundsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/nxtsoundsensor.html'
language: en
---

# NXT Sound Sensor

## Ports

### Output

### **Sound level** — Surrounding sound levels scalar

The block outputs the surrounding sound levels in either normalized or raw
analog-to-digital format.

**Data Types:** `uint16`

## Parameters

### **EV3 brick input port number** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the ultrasonic sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Output mode** — Sound level output format `Normalised (0-100)` (default) | `Raw A/D (1023-0)`

Select the type of sound data to output from the block.

- `Normalised (0-100)` — Output intensity of sound on a
  scale from 0 to 100, where 0 indicates weakest intensity sound and 100 indicates
  strongest intensity sound.
- `Raw A/D (1023-0)` — Output intensity of sound on a
  scale from 1023 to 0, where 1023 indicates weakest intensity sound and 0 indicates
  strongest intensity sound.

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

Measure surrounding sound levels using NXT sound sensor connected to EV3 brick

Use the NXT Sound Sensor block to measure the surrounding sound levels
using the NXT sound sensor connected to the LEGO®
MINDSTORMS® EV3 brick.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
