---
type: simulink-block
title: 'MAG3110 3-Axis Magnetometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Magnetometer'
documentation_page: 'mag31103axismagnetometer'
documentation_source_path: 'microbit/ref/mag31103axismagnetometer.html'
language: en
---

# MAG3110 3-Axis Magnetometer

## Ports

### Output

The block has one output port.

### **Magnet** — Strength of the earth magnetic field along each axis of the chip vector

The block outputs the magnetic field as a
`[1x3]` vector. Each value
represents the measurement of the magnetic field
in `μT` along the X, Y, and Z
axes.

**Data Types:** `double`

## Parameters

### **Sensor output data rate (ODR)** — Rate at which data is sampled `80Hz` (default) | `40Hz` | `20Hz` | `10Hz` | `5Hz` | `2.5Hz` | `1.25Hz` | `0.63Hz`

Specify the rate at which you want the
magnetometer to read the measurement of the
magnetic field.

### **Sample time** — Specify how often the block reads data from the magnetometer on the chip `0.1` (default)

When you specify this parameter
as`-1`, Simulink® determines
the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Coder Support Package for BBC micro:bit/Magnetometer

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Get measurement of magnetic field along the X, Y, and Z axes of the MAG3110 3-Axis chip

The MAG3110 3-Axis Magnetometer block measures the
magnetic field along the X, Y, and Z axes. The block has one
output port, Magnet. The Magnet port outputs the magnetic field
as a `[1x3]` vector in
`uT`.

Using the parameters of this block, you can select the Output Data
Rates (ODR) for the magnetometer. The Output Data Rates (ODR)
range from `0.63 Hz` to `80
Hz`.

### Chip Orientation and Axis Orientation Relative to Gravity

Hold the board so that the board faces you and the line to
the top of the MAG3110 3-Axis chip is aligned
horizontally to the table. At this position, the
X-axis is horizontal and points to the left, the
Y-axis is vertical and points down, and the Z-axis
points toward you.

The direction of the arrows shows the positive direction
of the reading for the magnetometer.

When you tilt the board along the X, Y, and Z axes of the
chip, this illustration shows the strength of the
magnetic field.

**Magnetic Strength in X Direction**

Hold the board so that the board faces you,
and the line to the right of the chip is aligned
vertically to the table. The magnetometer on the
chip measures the earth magnetic field along each
sensor axis. In the resultant
`[1x3]` vector, the first value
that represents the magnetic strength at the
X-axis is minimum.
