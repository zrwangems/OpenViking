---
type: simulink-block
title: 'Motor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'motor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/motor.html'
language: en
---

# Motor

## Ports

### Input

### **Port\_1** — Direction and power to EV3 motor integer [`-100`, `100`]

The block inputs these values that determine the direction and power of an EV3 motor.

- `1` to `100` — Input the values to the
  block in this range to move the motor in the forward direction.
  `1` indicates minimum power and `100`
  indicates maximum power in the forward direction.
- `-1` to `-100` — Input the values to the
  block in this range to move the motor in the reverse direction.
  `-1` indicates minimum power and `-100`
  indicates maximum power in the reverse direction.
- `0` — No power

**Data Types:** `int8`

## Parameters

### **EV3 brick output port** — Output port number of EV3 brick `A` (default) | `B` | `C` | `D`

Select the EV3 brick output port to which the motor is connected. If your
Simulink® model contains both the Motor and Encoder
blocks, set the **EV3 brick output port** parameter in both the blocks
to the same port.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Control power and direction of EV3 motor

Use the Motor block to control the power and direction of an EV3 motor. You
can use this block with the Encoder block to measure the rotation
of a motor connected to an EV3 brick.

This block converts the data type of the values it receives. You do not need to convert
the data type of the input signal.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
