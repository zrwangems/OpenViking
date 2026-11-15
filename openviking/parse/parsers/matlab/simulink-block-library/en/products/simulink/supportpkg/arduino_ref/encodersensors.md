---
type: simulink-block
title: 'Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Motor and Vehicle Sensors'
documentation_page: 'encodersensors'
documentation_source_path: 'supportpkg/arduino_ref/encodersensors.html'
language: en
---

# Encoder

## Ports

### Input

### **Port\_1** — External signal to reset encoder reading scalar

Use this input port to reset the Encoder block tick counter.

When the value of the signal at the input port is `0`, the block
outputs the total tick count it reads from the encoder. In this case, the block output
is the same as in the `No reset` mode. When the value of the
signal at the input port is a nonzero value, the block outputs the number of ticks it
reads from the encoder at the at the sample time you set in the **Sample
time** parameter. In this case, the block output is the same as in the
`Reset at each Sample time` mode.

#### Dependencies

To enable this port, set **Reset mode** to `Reset
by external signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Tick** — Incremental position of rotating motor scalar

The block outputs the relative change in the position of the rotating motor in
ticks. You can determine the direction of rotation based on the previous and current
tick counts and the mode you select in the Reset mode parameter. For
example, in the `No reset` mode, with a previous tick count
of `30` and current tick count of `20`, the motor is
moving in the counterclockwise direction.

**Data Types:** `int16`

## Parameters

### **Input A** — Pin of Arduino hardware `2` (default) | Pins supported by External Interrupt block

Select pin on the Arduino board to which you have connected output A of the encoder.

### **Input B** — Pin of Arduino hardware `3` (default) | Pin supported by External Interrupt block

Select pin on the Arduino board to which you have connected output B of the encoder.

### **Reset mode** — Reset block output `No reset` (default) | `Reset at each Sample time` | `Reset at external signal`

The block supports three reset modes.

- `No reset` — The block outputs the total tick count it
  reads from the encoder.
- `Reset at each Sample time`  — The block outputs the
  number of ticks it reads from the encoder at the sample time you set in the
  **Sample time** parameter.
- `Reset by external signal` — When you set the parameter
  to this mode, an input port becomes available. In this mode, when the value of the
  signal at the input port is `0`, the block output is the same as in
  the `No reset` mode. When the value of the signal at the
  input port is a nonzero value, the block output is the same as in the
  `Reset at each sample time` mode.

Assume that the encoder wheel that you have connected to your Arduino hardware has
90 slots, which means that the encoder tick count is 1 for every 4 degrees of rotation.
Assume that the block sample time is 1 second and the tick count at time instant
*T* = 0 is 0. This table shows the tick counts that the block outputs
in the three modes.

Arduino reset mode image

- Between *T* = 0 and *T* = 1, assume that the
  encoder rotates 20 degrees clockwise.

  - `No reset` — The output is 20/4 = 5
  - `Reset at each sample time` — Assume that the
    encoder has rotated 20 degrees at the given sample time, so the output is 20/4 =
    5
  - `Reset by external signal` — Assume that the value
    of the external signal is 0, so the count is calculated as in the
    `No reset` mode, and the output is 20/4 = 5
- Between *T* = 1 and *T* = 2, assume that the
  encoder rotates 40 degrees clockwise.

  - `No reset` — In this mode, the block output at any
    time instant is the sum of the previous count and the current count, so the
    output is 5+40/4 = 15
  - `Reset at each sample time` — Assume that the
    encoder has rotated 40 degrees at the given sample time, so the output is 40/4 =
    10
  - `Reset by external signal` — Assume that the value
    of the external signal is 0, so the block calculates the count as in the
    `No reset` mode, and the output is 5+40/4 = 15
- Between *T* = 3 and *T* = 4, assume that the
  encoder rotates 20 degrees counterclockwise.

  - `No reset` — In this mode, the block output at any
    time instant is the sum of the previous count and the current count, so the
    output is 30–20/4 = 25
  - `Reset at each sample time` — Assume that the
    encoder has rotated 20 degree counterclockwise at the given sample time, so the
    output is – 20/4 = – 5
  - `Reset by external signal` — Assume that the value
    of the external signal is a nonzero value, so the block calculates the count as
    in the `Reset at each sample time` mode, and the output
    is – 20/4 = – 5

### **Sample time** — Time at which block reads data from encoder `-1` (default) | scalar

Enter the time interval in seconds at which the block reads values from the
encoder.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Measure incremental position and direction of rotating motor

The Encoder block outputs the tick count from a quadrature encoder on a
rotating motor connected to an Arduino® board. Every increment in the tick count of the encoder indicates that the motor
is rotating clockwise. Every decrement in the tick count of the encoder indicates that the
motor is rotating counterclockwise. The total tick count represents the incremental position
of the rotating motor.

You can reset the encoder readings from the block using the **Reset
mode** parameter in the block parameters dialog box.

When simulating without hardware, this block outputs zeros. For more information, see
Block Produces Zeros or Does Nothing in Simulation.

**Note**

The Encoder block does not support the connected IO workflow on the
Arduino Nano 33 BLE Sense board currently.
