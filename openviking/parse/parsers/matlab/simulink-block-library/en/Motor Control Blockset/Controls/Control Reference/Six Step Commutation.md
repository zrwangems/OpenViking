---
type: simulink-block
title: 'Six Step Commutation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'sixstepcommutation'
documentation_source_path: 'ref/sixstepcommutation.html'
language: en
---

# Six Step Commutation

## Ports

### Input

### **Hall** — Hall sensor sequence scalar

The Hall sensor sequence. If the Hall sensors are placed `120`
degrees apart, the sequence number is between `1` to
`6`. For a custom Hall sensor sequence (when the Hall sensors are
placed `60` degrees apart), the sequence number is between
`0` to `7`.

**Note**

If you provide an invalid Hall sequence to this port, the block sets the output
port **Ctrl** to zero.

#### Dependencies

To enable this port, set **Input type** to
`Hall`.

**Data Types:** `single` | `double` | `fixed point`

### **Position** — Rotor position scalar

Position detected by either the Hall or quadrature encoder sensor in radians
(`0` to `2π`), degrees (`0` to
`360`), or per unit (`0` to
`1`).

#### Dependencies

To enable this port, set **Input type** to
`Position`.

**Data Types:** `single` | `double` | `fixed point`

### **TorqueSign** — Direction of rotation scalar

Torque sign (`+1` or `-1`) indicating the
direction of rotation of the BLDC motor.

When you change the torque sign from `+1` to
`-1`, the block uses a switching pattern that is complementary to
the one used for the `+1` torque sign. Similarly, when you change the
torque sign from `-1` to `+1`, the block uses a
switching pattern that is complementary to the one used for the `-1`
torque sign.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32`
### Output

### **Ctrl** — Motor control switching sequence scalar

Switching sequence signals to implement six-step commutation (or trapezoidal
commutation) on the BLDC motor.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Input type** — Block input type `Hall` (default) | `Position`

Type of position sensor feedback connected to the block input.

### **Position Unit** — Unit of position input `Per-unit` (default) | `Degrees` | `Radians`

Unit of position feedback input.

#### Dependencies

To enable this parameter, set **Input type** to
`Position`.

### **Hall Sequence number** — Hall sequence `[5,4,6,2,3,1]` (default) | vector

Customized Hall sequence.

If the Hall sensors are placed 120 degrees apart, the sequence number is between 1
to 6. If the Hall sensors are placed 60 degrees apart, the sequence number is between 0
to 7.

#### Dependencies

To enable this parameter, set **Input type** to
`Hall`.

### **Enable custom commutation** — Enable **Commutation switching** parameter `off` (default) | `on`

Select this parameter for the block to enable the **Commutation
switching** parameter.

#### Dependencies

To enable this parameter, set **Input type** to
`Hall`.

### **Commutation switching** — Commutation switching sequence `[0 0 1 0 0 1;0 1 1 0 0 0;0 1 0 0 1 0;0 0 0 1 1 0;1 0 0 1 0 0;1 0 0 0 0 1]` (default) | vector

Customized switching sequence for commutation of the BLDC motor.

#### Dependencies

To enable this parameter, set **Input type** to
`Hall` and select **Enable custom
commutation** parameter.

## Libraries

Motor Control Blockset / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020b**

## Description

Generate switching sequence for six-step commutation of brushless DC (BLDC) motor

The Six Step Commutation block uses a 120-degree conduction mode to
generate a switching sequence to implement six-step commutation (or trapezoidal commutation)
on a three-phase BLDC motor. You can use the switching signals to operate switches and control
the stator currents, and therefore, control motor speed and direction of rotation.

The block accepts the Hall sequence number or rotor position (from a position sensor such
as a Hall or a quadrature encoder sensor) and the direction of torque as inputs. It uses the
Hall sequence or position input to determine the sector where the rotor is present. The block
computes the switching sequence such that it energizes the corresponding phases to maintain
the torque angle (angle between rotor d-axis and stator magnetic field) of 90 degrees (with a
deviation of 30 degrees). For example, as shown in the below figure, for hall state 5, phase A
and phase C are triggered to spin the motor.

This figure is an example that shows the stator magnetic field phasors along with their
default Hall sequence. It is recommended that you use Hall Sensor Sequence Calibration of BLDC Motor to obtain hall sequence and
use this hall sequence with the block to achieve the six step commutation.

The block uses a commutation logic based on the Hall sequence to generate switching
sequences.

| Hall State (Hall a, Hall b, Hall c) | Switching Sequence (AA' BB' CC') | | |
| --- | --- | --- | --- |
| AA' | BB' | CC' |
| 4 (100) | 00 | 10 | 01 |
| 6 (110) | 01 | 10 | 00 |
| 2 (010) | 01 | 00 | 10 |
| 3 (011) | 00 | 01 | 10 |
| 1 (001) | 10 | 01 | 00 |
| 5 (101) | 10 | 00 | 01 |

This figure shows the stator magnetic field phasors along with the possible sectors
(determined from the input rotor position).

The block uses a commutation logic based on the position sensor signals to generate
switching sequences.

| Position (θ) | Sector | Switching Sequence (AA' BB' CC') | | |
| --- | --- | --- | --- | --- |
| AA' | BB' | CC' |
| (-30°, 30°] | 1 | 00 | 10 | 01 |
| (30°, 90°] | 2 | 01 | 10 | 00 |
| (90°, 150°] | 3 | 01 | 00 | 10 |
| (150°, 210°] | 4 | 00 | 01 | 10 |
| (210°, 270°] | 5 | 10 | 01 | 00 |
| (270°, 330°] | 6 | 10 | 00 | 01 |
