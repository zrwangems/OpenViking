---
type: simulink-block
title: 'Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Sensors'
documentation_page: 'encoder'
documentation_source_path: 'beagleboneblue/ref/encoder.html'
language: en
---

# Encoder

## Ports

### Input

### **Port\_1** — Input signal to reset encoder reading scalar

When the value of the signal at the input port is
`0`, the block outputs the total tick count read from
the encoder. The block output is the same as in the `No
reset` mode.

When the value of the signal at the input port is a nonzero value, the
block outputs the number of ticks read from the encoder at the given
sample time. The block output is the same as in the `Reset
at each sample time` mode.

For more information on reset modes, see Reset mode in Parameters.

#### Dependencies

This port appears only when you set the **Reset
mode** parameter to `Reset by external
signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Tick** — Incremental position of rotating motor scalar

The port outputs the relative change in position of the rotating
motor, measured in ticks.

**Data Types:** `int16`

## Parameters

### **Channel** — Channel number on hardware `1` (default) | `2` | `3` | `4`

Select the channel on the hardware to which the encoder is
connected.

### **Reset mode** — Reset mode for resetting the block output `No reset` (default) | `Reset at each sample time` | `Reset by external signal`

This block supports three different reset modes.

- `No reset` – The block outputs the total
  tick count read from the encoder.
- `Reset at each sample time`  – The block
  outputs the number of ticks read from the encoder at the given
  sample time.
- `Reset by external signal` – When you set
  the **Reset mode** parameter to `Reset
  by external signal`, an input port becomes
  available. In this mode, when the value of the signal at the input
  port is `0`, the block output is the same as in the
  `No reset` mode. When the value of the
  signal at the input port is a nonzero value, the block output is the
  same as in the `Reset at each sample time`
  mode.

For example, assume that the encoder wheel connected to the hardware has
90 slots. This means that, the encoder tick count is one for every 4 degrees
of rotation. Assume that the block sample time is 1 second, and the tick
count at time instant *T* = 0 is 0.

- `No reset` – Between *T*
  = 0 and *T* = 1, the encoder rotates 20 degrees
  clockwise. Each tick represents 4 degrees, so the output is 20 / 4 =
  `5`.

  Between *T* = 1 and *T* = 2, the
  encoder rotates 40 degrees clockwise, so the output is
  `15` at *T* = 2 (5 from
  *T* = 1 plus 10 from *T* = 2).

  In this mode, the block output at any time instant is the sum of
  the previous count and the current count.
- `Reset at each sample time`  – Between
  *T* = 0 and *T* = 1, the
  encoder rotates 20 degrees clockwise. The output is
  `5`.

  Between *T* = 1 and *T* = 2, the
  encoder rotates 40 degrees clockwise. The output is
  `10`.
- `Reset by external signal` – From
  *T* = 0 to *T* = 2, the value
  of the input signal is `0`. During this period, the
  output is the same as in the `No reset`
  mode. At *T* = 3 and *T* = 4, the
  value of the input signal changes to a nonzero value. During this
  period, output is the same as in the `Reset at each
  sample time` mode.

  In the table, between *T* = 0 and
  *T* = 1, the encoder rotates 20 degrees
  clockwise. The output is `5` at
  *T* = 1.

  Between *T* = 1 and *T* = 2, the
  encoder rotates 40 degrees clockwise. The output is
  `15` at *T* = 2 (5 from
  *T* = 1 plus 10 from *T* =
  2).

  Between *T* = 2 and *T* = 3, the
  encoder rotates 60 degrees in clockwise direction. The output is
  `30` at *T* = 3 (15 from
  *T* = 2 plus 15 from *T* =
  3).

  Between *T* = 3 and *T* = 4, the
  encoder rotates 20 degrees counterclockwise. At *T*
  = 3 the value of the input signal changes to a nonzero value. The
  output is `–5` at *T* = 4 (0 from
  *T* = 3 plus –5 from *T* =
  4).

### **Sample time** — How often to read value from encoder `0.1` (default)

Specify how often the block reads the tick count from the encoder, in
seconds.

#### Dependencies

This parameter appears only when you set the **Reset
mode** parameter to `No reset` or
`Reset at each sample time`.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Measure incremental position and direction of a rotating motor

The Encoder block outputs the tick count from a quadrature encoder on a
rotating motor that is connected to BeagleBone® Blue. Every increment in the tick count from the encoder indicates that
the motor is rotating clockwise. Every decrement in the tick count from the encoder
indicates that the motor is rotating counterclockwise. The tick count total represents
the incremental position of the rotating motor.

Using the **Reset mode** parameter in the Block Parameters dialog
box, you can reset the encoder readings that the block outputs. For more information on
reset modes, see Reset mode in Parameters.

During simulations without hardware, this block outputs zeros. See Block Produces Zeros or Does Nothing in Simulation.
