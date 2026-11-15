---
type: simulink-block
title: 'FXOS8700 6-Axes Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'fxos87006axessensor'
documentation_source_path: 'freescalefrdmk64fboard/ref/fxos87006axessensor.html'
language: en
---

# FXOS8700 6-Axes Sensor

## Ports

### Output

The block has two output ports. The number of ports varies depending
on the active sensor that you select in the **Active sensor** list.

### **Magnet** — Strength of the earth magnetic field along each axis of the chip vector

The block outputs the magnetic field as a `[1x3]` vector.
Each value represents the measurement of the magnetic field in `μT` along
the X, Y, and Z axes.

**Data Types:** `double`

### **Accel** — Acceleration applied to the sensor along each axis of the chip vector

The block outputs the acceleration as a `[1x3]` vector.
Each value represents the measurement of the acceleration in `g
(9.8 m/s2)` along the X, Y, and
Z axes.

**Data Types:** `double`

## Parameters

### **Active sensor** — Specify the active sensor on the chip `Accelerometer and Magnetometer` (default) | `Accelerometer only` | `Magnetometer only`

- `Accelerometer only` —
  When you set the **Active sensor** parameter to `Accelerometer
  only`, the block configures an output port. The port
  on the block is labeled as `Accel`, indicating that
  the block outputs the measurement of the acceleration from the accelerometer.
  The acceleration is measured along the X, Y, and Z axes of the chip.

  The ODR ranges from `1.5625 Hz` to `800
  Hz`.
- `Magnetometer only` —
  When you set the **Active sensor** parameter to `Magnetometer
  only`, the block configures an output port. The port
  on the block is labeled as `Magnet`, indicating that
  the block outputs the measurement of the earth magnetic field from
  the magnetometer. The magnetic field is measured along the X, Y, and
  Z axes of the chip.

  The ODR ranges from `1.5625 Hz` to `800
  Hz`.
- `Accelerometer and Magnetometer` —
  When you set the **Active sensor** parameter to `Accelerometer
  and Magnetometer`, the block configures two output ports.
  The ports on the block are labeled as `Magnet` and `Accel`.
  The `Magnet` port indicates that the block outputs
  the measurement of the magnetic field from the magnetometer. The `Accel` port
  indicates that the block outputs the measurement of the acceleration
  from the accelerometer. The acceleration and the magnetic field are
  measured along the X, Y, and Z axes of the chip.

  The ODR ranges from `0.7813 Hz` to `400
  Hz`.

### **Sensor output data rate (ODR)** — Rate at which data is sampled `400Hz` (default) | `800Hz` | `200Hz` | `100Hz` | `50Hz` | `25Hz` | `12.5Hz` | `6.25Hz` | `3.125Hz` | `1.5625Hz` | `0.7813Hz`

Specify the rate at which you want the sensors to read the measurement
of acceleration and the magnetic field. The values that appear in
this parameter vary depending on the active sensor that you select
in the **Active sensor** list.

### **Acceleration full scale range** — Range of acceleration deviation that the accelerometer can measure `-4g to +4g` (default) | `-2g to +2g` | `-8g to +8g`

The accelerometer sensitivity changes with the full scale range
that you select in this parameter. Accelerometer sensitivity is `0.244
mg/LSB` in `2 g` mode, `0.488 mg/LSB` in `4
g` mode, and `0.976 mg/LSB` in `8
g` mode. A small, full scale range means that the sensitivity
of the sensor is greater, resulting in a more precise reading out
of the accelerometer.

#### Dependencies

This parameter appears when you set the **Active sensor** parameter
to `Accelerometer only` or `Accelerometer
and Magnetometer`.

### **Sample time** — Specify how often the block reads data from the sensors on the chip `-1` (default)

By default, the block inherits its sample time based on the
context of the block within the model.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Get measurement of linear acceleration and magnetic field along the X, Y, and Z axes of the FXOS8700 6-Axes chip

The FXOS8700 6-Axes Sensor block measures the
linear acceleration and the magnetic field along the X, Y, and Z directions.
The block has two output ports, Magnet and Accel. The Magnet port
outputs the magnetic field from the magnetometer on the FXOS8700 6-Axes
chip as a `[1x3]` vector in `uT`.
The Accel port outputs the acceleration from the accelerometer on
the FXOS8700 6-Axes chip as a `[1x3]` vector in `g
(9.8 m/s2)`. The number of output
ports vary depending on the active sensors that you select.

Using the parameters of this block, you can change the accelerometer
sensitivity by selecting a full-scale range of `±2g`, `±4g`,
or `±8g`.

You can also select the Output Data Rates (ODR) for both of
the sensors. The Output Data Rates (ODR) for each sensor range from `1.563
Hz` to `800 Hz`. Interleaved magnetic and
acceleration data is available at ODR rates of up to 400 Hz.

### Chip Orientation and Axis Orientation Relative to Gravity

Place the board face up on a table, with the dot to the top-right
corner of the FXOS8700 6-Axes chip. At this position, the X-axis points
away from you, the Y-axis is horizontal and points to the left, and
the Z-axis is vertical and points up.

The direction of the arrows shows the positive direction of
the reading for the accelerometer and the magnetometer.

When you tilt the board along the X, Y, and Z axes of the chip,
this illustration shows the acceleration and the magnetic field.

**Acceleration of Gravity in X Direction**

Hold the board so that the board faces you and the dot is to
the top-right corner of the chip. The acceleration of gravity is static
because the chip is stationary.

In the resultant `[1x3]` vector, the first
value that represents the acceleration at the X-axis ≈`1
g (9.81 m/s2)`. The last two values
that represent the acceleration at the Y and Z axes (perpendicular
to the acceleration of earth gravity) ≈ `0.00 g`.

Push the board upward with an acceleration of `A m/s2`.
The acceleration of the gravity is dynamic and equal to the acceleration
of the block minus the force of gravity ≈ `(+A-9.81)
m/s2`. In the resultant `[1x3]` vector,
the value of the X-axis ranges between the full-scale range value
that you specify in the **Acceleration full scale range** parameter.

**Magnetic Strength in X Direction**

Hold the board so that the board faces you and the dot is to
the top-right corner of the chip. The magnetometer on the chip measures
the earth magnetic field along each sensor axis. In the resultant `[1x3]` vector,
the first value that represents the magnetic strength at the X-axis
is minimum.
