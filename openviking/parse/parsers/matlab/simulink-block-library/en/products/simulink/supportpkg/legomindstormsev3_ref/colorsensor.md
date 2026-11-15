---
type: simulink-block
title: 'Color Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'colorsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/colorsensor.html'
language: en
---

# Color Sensor

## Ports

### Output

### **Color** — Color data color mode, color intensity

The block outputs color data the sensor detects of an object or its
surrounding.

#### Dependencies

The block outputs these color values based on the mode you select.

- `Color` — The block outputs the color of an
  object.
- `Reflected light intensity` — The block outputs
  color intensity of an object.
- `Ambient light intensity` — The block outputs
  ambient light intensity of the surrounding.

**Data Types:** `uint8`

## Parameters

### **EV3 brick input port** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the color sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Mode** — Light detection mode of sensor `Color` (default) | `Reflected light intensity` | `Ambient light intensity`

Select the light detection mode of the sensor that is connected to the EV3 brick.

- `Color` — In this mode, the sensor evaluates the
  color of an object and outputs one of these values on the output port of the block.

  - `0` — Indicates that the sensor detects no
    color.
  - `1` — Indicates that the sensor detects the color
    black.
  - `2` — Indicates that the sensor detects the color
    blue.
  - `3` — Indicates that the sensor detects the color
    green.
  - `4` — Indicates that the sensor detects the color
    yellow.
  - `5` — Indicates that the sensor detects the color
    red.
  - `6` — Indicates that the sensor detects the color
    white.
  - `7` — Indicates that the sensor detects the color
    brown.

  For example, you can use this mode for EV3-based robots to solve
  Rubik's cube puzzles.
- `Reflected light intensity` — In this mode, the
  sensor flashes the LED and measures the amount of light reflected on the nearby
  surfaces. The block outputs values from `0` to
  `100` where `0` indicates a dark surface and
  `100` indicates a light surface. For example, you can use this
  mode for EV3-based robots that to detect and follow a black line around an
  obstacle course.
- `Ambient light intensity` — In this mode, the sensor
  measures the surrounding ambient light. The block outputs values from
  `0` to `100` where `0`
  indicates a dark surrounding ambience and `100` indicates a
  bright surrounding ambience. For example, you can use this mode for EV3-based
  robots to follow a light source.

### **Sample time** — Time interval at which block reads sensor values `0.1` (default) | positive integer

Specify the frequency of how often the block reads values from the sensor connected
to the EV3 brick. Shorter sample times, such as `0.01`, may produce
unreliable measurements.

Smaller sample times require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Detect color, reflected light, or ambient light using EV3 brick

Use the Color Sensor block to detect the color of an object, measure
reflected light, or measure ambient light using a color sensor connected to the LEGO®
MINDSTORMS® EV3 brick.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
