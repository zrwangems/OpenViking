---
type: simulink-block
title: 'L293D DC Motor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'l293ddcmotor'
documentation_source_path: 'supportpkg/arduino_ref/l293ddcmotor.html'
language: en
---

# L293D DC Motor

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
same effect as the maximum or minimum input values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Enable pin** — Enable pin on DC motor `5` (default)

Specify the enable pin number on the motor driver shield to which the DC
motor is connected.

### **Input A pin** — Input A pin number for DC motor `8` (default)

Specify the Input A pin number on the motor driver shield that is
connected to the DC motor.

Do not assign the same pin number to more than one DC Motor block within
the same model.

### **Input B pin** — Input B pin number for DC motor `10` (default)

Specify the Input B pin number on the motor driver shield that is
connected to the DC motor.

Do not assign the same pin number to more than one DC Motor block within
the same model.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Control power and direction of a DC motor

The L293D DC Motor block controls power and direction of a DC motor
connected to motor driver shields such as L293D and L298N.

### Supported Hardware

The L293D DC Motor block supports all Arduino boards.
