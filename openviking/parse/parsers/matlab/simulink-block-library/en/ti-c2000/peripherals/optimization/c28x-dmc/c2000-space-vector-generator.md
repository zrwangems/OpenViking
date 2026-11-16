---
type: simulink-block
title: 'C2000 Space Vector Generator'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000spacevectorgenerator'
documentation_source_path: 'ref/c2000spacevectorgenerator.html'
language: en
---

# C2000 Space Vector Generator

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Duty ratios for stator reference voltage

# C2000 Space Vector Generator

Duty ratios for stator reference voltage

Replace the existing DMC blocks with MCB blocks for improved usability and future
compatibility. It is recommended that you use blocks from Control Algorithm Design (Motor Control Blockset). While these blocks
are not one-to-one replacements, they enable you to achieve the same functionality.

| C28x DMC lib | C28x DMC lib equivalent in MCB |
| --- | --- |
| C2000 Clarke Transformation | Clarke Transform (Motor Control Blockset) |
| C2000 Inverse Park Transformation | Inverse Park Transform (Motor Control Blockset) |
| C2000 Park Transformation | Park Transform (Motor Control Blockset) |
| C2000 PID Controller | PI Controller (Motor Control Blockset) |
| C2000 Ramp Control | Position Generator (Motor Control Blockset) |
| C2000 Ramp Generator | Position Generator (Motor Control Blockset) |
| C2000 Space Vector Generator | PWM Reference Generator (Motor Control Blockset) |
| C2000 Speed Measurement | Speed Measurement (Motor Control Blockset) |

This block calculates duty ratios that generate a given stator reference voltage
using space vector PWM technique. Space vector pulse width modulation is a switching
sequence of the upper three power devices of a three-phase voltage source inverter and is
used in applications such as AC induction and permanent magnet synchronous motor drives. The
switching scheme results in three pseudosinusoidal currents in the stator phases. This
technique approximates a given stator reference voltage vector by combining the switching
pattern corresponding to the basic space vectors.

The inputs to this block are

- Alpha component — the reference stator voltage vector on the direct axis
  stationary reference frame (`Ua`)
- Beta component — the reference stator voltage vector on the direct axis
  quadrature reference frame (`Ub`)

The alpha and beta components are transformed via the inverse Clarke equation and
projected into reference phase voltages. These voltages are represented in the outputs as
the duty ratios of the PWM1 (`Ta`), PWM3 (`Tb`), and PWM5
(`Tc`).

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 Space Vector Generator block
