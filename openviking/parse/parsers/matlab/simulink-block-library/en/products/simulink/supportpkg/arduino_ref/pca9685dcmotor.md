---
type: simulink-block
title: 'PCA9685 DC Motor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'pca9685dcmotor'
documentation_source_path: 'supportpkg/arduino_ref/pca9685dcmotor.html'
language: en
---

# PCA9685 DC Motor

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

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino® hardware to communicate with sensor peripherals. For more
information on the Arduino pin mapping and modules that hardware boards support, see
Pin Mapping for Arduino Timer-Independent Blocks.

### **PCA9685 address** — Address on PCA9685 PWM chip-based shields `0X60` (default)

Enter the PCA9685 address on the PCA9685 PWM chip-based shield that is
connected to the DC motor.

### **PWM frequency (Hz)** — PWM frequency for DC motor `1200` (default)

Specify the frequency (in hertz) on the PCA9685 PWM chip-based shield that
is connected to the DC motor for generating the pulse-width modulated
signal.

### **Motor Channel** — Motor channel for DC motor `1` (default) | `1` to `4`

Specify the motor channel on the PCA9685 PWM chip-based shield that is
connected to the DC motor.

Do not assign the same channel number to more than one DC Motor block
within the same model.

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

The PCA9685 DC Motor block controls the power and direction of a DC
motor connected to PCA9685 PWM chip-based shields such as Adafruit Motor Shield V2. The
input signal determines the power supplied to the motor and the direction of rotation of
the motor.

### Supported Hardware

The PCA9685 DC Motor block supports all Arduino boards.
