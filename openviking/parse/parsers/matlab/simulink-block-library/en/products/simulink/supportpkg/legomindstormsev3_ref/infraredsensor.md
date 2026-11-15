---
type: simulink-block
title: 'Infrared Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'infraredsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/infraredsensor.html'
language: en
---

# Infrared Sensor

## Ports

### Output

### **Button ID** — Button identification number positive integer

The block outputs these identification number of the button pressed on the
LEGO® remote infrared sensor.

Button ID Table

#### Dependencies

- To enable this port, set **Mode** to
  `Remote`.

**Data Types:** `int8`

### **Heading** — Beacon proximity angle integer [`-25`, `25`]

The block outputs the angle from the direction the infrared sensor is pointing
to.

#### Dependencies

- To enable this port, set **Mode** to `Beacon
  Proximity`.

**Data Types:** `int8`

### **Proximity** — Beacon proximity percentage positive integer [`0`, `100`]

The block outputs the proximity of the object in front of the infrared sensor in
percentage.

#### Dependencies

- To enable this port, set **Mode** to `Beacon
  Proximity` or `Proximity`.

**Data Types:** `uint8`

## Parameters

### **EV3 brick input port number** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the infrared sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Mode** — Sensor infrared sensor operation mode `Remote` (default) | `Beacon Proximity` | `Proximity`

### **Channel** — EV3 brick infrared beacon channel number `1` (default) | `2` | `3` | `4`

Select the infrared beacon channel number on the EV3 brick.

#### Dependencies

- To enable this parameter, set **Mode** to
  `Remote` or `Beacon
  Proximity`.

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

Detect button status on LEGO remote infrared beacon, measure beacon proximity and heading, and measure object proximity using infrared sensor connected to EV3 brick

Use the Infrared Sensor block to measure and detect these parameters using
the infrared sensor connected to an EV3 brick.

- detect the button pressed on the remote infrared beacon
- measure beacon proximity and heading
- measure object proximity using infrared sensor

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
