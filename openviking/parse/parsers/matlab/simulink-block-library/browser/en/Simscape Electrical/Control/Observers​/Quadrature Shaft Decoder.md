---
type: simulink-block
title: 'Quadrature Shaft Decoder'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Observers\u200b'
documentation_page: 'quadratureshaftdecoder'
documentation_source_path: 'ref/quadratureshaftdecoder.html'
language: en
---

# Quadrature Shaft Decoder

## Ports

### Input

### **A** — Digital signal *A* scalar

Simulink digital signal *A*, specified as a scalar, which is 90°
out-of-phase with digital signal *B*.

**Data Types:** `single` | `double`

### **B** — Digital signal *B* scalar

Simulink digital signal *B*, specified as a scalar, which is 90°
out-of-phase with digital signal *A*.

**Data Types:** `single` | `double`

### **Z** — Index pulse scalar

Simulink signal, specified as a scalar, associated with the decoder index pulse that is
used to reset the position calculation.

**Data Types:** `single` | `double`
### Output

### **Velocity** — Shaft rotational velocity scalar

Simulink signal, specified as a scalar, associated with the shaft rotational
velocity.

**Data Types:** `single` | `double`

### **Position** — Shaft angle of rotation scalar

Simulink signal, specified as a scalar, associated with the shaft angle of
rotation.

**Data Types:** `single` | `double`

## Parameters

### **Pulses per revolution** — Pulses per revolution 4 (default) | integer > 0

Number of pulses per revolution of the encoder shaft.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time between consecutive block executions, in s. During
execution, the block produces outputs and, if appropriate, updates its
internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

If this block is inside a triggered subsystem, you can set
this block to inherit the sample time by setting this parameter to
`-1`. If this block is in a continuous variable-step
model, specify the sample time explicitly by using a positive scalar.

## Libraries

Simscape / Electrical / Control / Observers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Decode incremental shaft encoder output

The Quadrature Shaft Decoder block measures the shaft rotation from an
encoder block, such as the Incremental Shaft Encoder, and outputs the velocity and
position.

The block counts the transitions of a pair of digital signals, *A* and
*B*, that are positioned 90° out of phase. The block determines the
direction and relative position by counting only one of the two signals changes per
tick. The angular velocity is obtained by measuring the frequency of either
signal.
