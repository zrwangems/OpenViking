---
type: simulink-block
title: 'Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'encoder'
documentation_source_path: 'supportpkg/raspberrypi_ref/encoder.html'
language: en
---

# Encoder

## Ports

### Input

### **Port\_1** — External signal to reset encoder reading scalar

Use this input port to reset the Encoder block tick counter.

When the value of the signal at the input port is `0`, the block
outputs the total tick count read from the encoder. In this case, the block output is
the same as in the `No reset` mode. When the value of the
signal at the input port is a nonzero value, the block outputs the number of ticks
read from the encoder at the given sample time. In this case, the block output is the
same as in the `Reset at each Sample time` mode.

#### Dependencies

To enable this port, set **Reset mode** to `Reset
by external signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Tick** — Incremental position of rotating motor scalar

The block outputs the relative change in the position of the rotating motor in
ticks. You can find out the direction of rotation of the motor based on the previous
and current tick counts and the Reset mode selected. For example, in the `No reset`
mode, with a previous tick count of `30` and current tick count of
`20`, the motor is moving in a counterclockwise direction.

**Data Types:** `int16`

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

Select your Raspberry Pi hardware board. You can find this information on the target hardware,
product packaging, or product documentation.

### **Input A** — GPIO pin of hardware GPIO 20 (default) | GPIO pin 4 – 19 or GPIO pin 21 – 27

Select the GPIO pin on the Raspberry Pi hardware board to which the output A of the encoder is connected.

### **Input B** — GPIO pin of hardware GPIO 21 (default) | GPIO pin 4 – 19 or GPIO pin 21 – 27

Select the GPIO pin on the Raspberry Pi hardware board to which the output B of the encoder is connected.

### **Reset mode** — Reset block output `No reset` (default) | `Reset at each Sample time` | `Reset at external signal`

The block supports three reset modes.

- `No reset` — The block outputs the total tick count
  read from the encoder.
- `Reset at each Sample time`  — The block outputs the
  number of ticks read from the encoder at the given sample time.
- `Reset by external signal` — When you set the parameter
  to this mode, an input port becomes available. In this mode, when the value of the
  signal at the input port is `0`, the block output is the same as in
  the `No reset` mode. When the value of the signal at the
  input port is a nonzero value, the block output is the same as in the
  `Reset at each sample time` mode.

Assume that the encoder wheel connected to the hardware has 90 slots, which means
that the encoder tick count is 1 for every 4 degrees of rotation. Assume that the block
sample time is 1 second and the tick count at time instant *T* = 0 is
0. This table shows the tick counts that the block outputs in the three modes.

Raspberry Pi reset mode image

- Between *T* = 0 and *T* = 1, assume that the
  encoder rotates 20 degree clockwise. The output in each mode is:

  - `No reset` — The output is 20 / 4 = 5
  - `Reset at each sample time` — Assume that the
    encoder has rotated 20 degrees at the given sample time, so the output is 20 / 4
    = 5
  - `Reset by external signal` — Assume that the value
    of the external signal is 0, so the count is calculated as in the
    `No reset` mode, and the output is 20 / 4 = 5
- Between *T* = 1 and *T* = 2, assume that the
  encoder rotates 40 degrees clockwise. The output in each mode is:

  - `No reset` — In this mode, the block outputs at any
    time instant is the sum of the previous count and the current count, so the
    output is 5 + 40 / 4 = 15
  - `Reset at each sample time` — Assume that the
    encoder has rotated 40 degrees at the given sample time, so the output is 40 / 4
    = 10
  - `Reset by external signal` — Assume that the value
    of the external signal is 0, so the count is calculated as in the
    `No reset` mode, and the output is 5 + 40 / 4 =
    15
- Between *T* = 3 and *T* = 4, assume that the
  encoder rotates 20 degrees counterclockwise. The output in each mode is:

  - `No reset` — In this mode, the block output at any
    time instant is the sum of the previous count and the current count, so the
    output is 30 – 20 / 4 = 25
  - `Reset at each sample time` — Assume that the
    encoder has rotated 20 degree counterclockwise at the given sample time, so the
    output is – 20 / 4 = – 5
  - `Reset by external signal` — Assume that the value
    of the external signal is a nonzero value, so the count is calculated as in the
    `Reset at each sample time` mode, and the output is –
    20 / 4 = – 5

### **Sample time** — Time at which block reads data from encoder `-1` (default) | scalar

Enter the time interval in seconds at which the block reads values from the
encoder.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Measure incremental position and direction of rotating motor

The Encoder block outputs the tick count from a quadrature encoder on a
rotating motor connected to a Raspberry Pi® hardware board. Every increment in the tick count of the encoder indicates that
the motor is rotating clockwise. Every decrement in the tick count of the encoder indicates
that the motor is rotating counterclockwise. The total tick count represents the incremental
position of the rotating motor.

You can reset the encoder readings from the block using the **Reset
mode** parameter in the block parameters dialog box.

When simulating without hardware, this block outputs zeros. For more information, see
Block Produces Zeros or Does Nothing in Simulation.
