---
type: simulink-block
title: 'M1M2DCMotors'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'm1m2dcmotors'
documentation_source_path: 'supportpkg/arduino_ref/m1m2dcmotors.html'
language: en
---

# M1M2DCMotors

## Ports

### Input

### **Port\_1** — Input signal value between `–100` and `100`

The sign of the input signal determines the direction of rotation of
the DC motor. A positive sign indicates a forward rotation, whereas a
negative sign indicates a reverse rotation. The amplitude determines the
power supplied to the motor.

- `1` to `100`: Forward
  rotation, minimum to maximum power.
- `–1` to `–100`: Reverse
  rotation, minimum to maximum power.
- `0`: No power is supplied.

Any out-of-range values, at the block input port has the
same effect as the maximum or minimum input values. For example, a value
of `500` is interpreted as the maximum value, 100.The
block input inherits the data type of the upstream block and internally
converts the input to `uint8`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Motor port** — Port number on MKR or Nano Motor Carrier `M1` (default) | `M2`

Select the port number on the MKR or Nano Motor Carrier to which the DC
motor is connected.

## Libraries

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Control power and direction of DC motor on port M1 or M2

The M1 M2 DC Motors block controls the power and direction of a DC
motor connected to an MKR or Nano Motor Carrier. The input signal determines the power
supplied to the motor and the direction of rotation of the motor.

If you simulate a model that contains the M1 M2 DC Motors block without
connecting the hardware, the block outputs zeros. See Block Produces Zeros or Does Nothing in Simulation.

### Supported Hardware

You can use the M1 M2 DC Motors block only with MKR and Nano 33 IoT
boards.
