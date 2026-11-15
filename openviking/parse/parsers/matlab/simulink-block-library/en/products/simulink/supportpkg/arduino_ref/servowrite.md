---
type: simulink-block
title: 'Servo Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'servowrite'
documentation_source_path: 'supportpkg/arduino_ref/servowrite.html'
language: en
---

# Servo Write

## Ports

### Input

### **Port\_1** — Rotational angle of shaft value between `0` and `180`

The input signal is the angle of rotation of the shaft, in degrees.
The shaft angle that you specify must be any value between
`0` degrees and `180` degrees. Any
out-of-range values at the block input port has the same effect as the
maximum or minimum input values. For example, `500` is
treated as 180, and `-500` is treated as 0.

The block input inherits the data type of the upstream block and
internally converts the input to `uint8`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Motor port** — Port number on MKR Motor Carrier `1` (default) | `2` | `3` | `4`

Select the port number on the MKR Motor Carrier to which the servo motor
is connected.

## Libraries

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Set servo motor to specified angle

The Servo Write block sets the shaft angle of a servo motor connected
to an MKR Motor Carrier. To rotate the motor shaft, provide an input value ranging
between `0` degrees and `180` degrees.

If you simulate a model that contains the Servo Write block without
connecting the hardware, the block does nothing. For more information, see Block Produces Zeros or Does Nothing in Simulation.

### Supported Hardware

You can use the Servo Write block only with MKR and Nano 33 IoT
boards.
