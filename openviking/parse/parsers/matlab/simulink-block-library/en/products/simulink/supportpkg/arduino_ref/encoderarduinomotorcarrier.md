---
type: simulink-block
title: 'Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'encoderarduinomotorcarrier'
documentation_source_path: 'supportpkg/arduino_ref/encoderarduinomotorcarrier.html'
language: en
---

# Encoder

## Ports

### Output

### **Position** — Position of rotating motor scalar

The **Position** port outputs the relative change in
the position of the rotating motor, measured in ticks. For more
information, see Calculate Position
and Rotational Speed of the Motor.

**Data Types:** `int32`

### **Speed** — Speed of rotating motor scalar

The **Speed** port outputs the rotational speed of
the motor, measured in ticks per second. For more information, see Calculate Position
and Rotational Speed of the Motor.

#### Dependencies

The **Speed** port is available only when you
select the **Show Speed output port**
parameter.

**Data Types:** `int32`

## Parameters

### **Encoder** — Encoder channel number `1` (default) | `2`

Select the channel number of the encoder that is connected to the MKR or
Nano Motor Carrier.

### **Show Speed output port** — Speed of rotation off (default) | on

When you select the **Show Speed output port** parameter,
the **Speed** port becomes available. The port outputs the
rotational speed of the motor, measured in ticks per second.

### **Reset count at initialization** — Reset tick counts each time model starts running `on` (default) | `off`

When you select the **Reset count at initialization**
parameter, the block resets the tick count to 0 each time the Simulink® model runs on the hardware.

### **Sample time** — Time interval to read value from encoder `0.1` (default) | `-1` | nonnegative real value

Specify how often the block reads the tick count from the encoder, in
seconds. When you specify this parameter as `-1`,
Simulink determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Measure rotation of motor in ticks

The Encoder block reads the position and rotational speed of the motor
from an encoder that is connected to an MKR or Nano Motor Carrier. The position is
measured in ticks, and the speed is measured in ticks per second. Every increment in the
tick count indicates a clockwise rotation, and every decrement in the tick count
indicates a counterclockwise rotation.

If you simulate a model that contains the Encoder block without
connecting the hardware, the block outputs zeroes. For more information, see Block Produces Zeros or Does Nothing in Simulation.
