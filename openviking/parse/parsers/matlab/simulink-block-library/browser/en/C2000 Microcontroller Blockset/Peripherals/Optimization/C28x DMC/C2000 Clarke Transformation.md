---
type: simulink-block
title: 'C2000 Clarke Transformation'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000clarketransformation'
documentation_source_path: 'ref/c2000clarketransformation.html'
language: en
---

# C2000 Clarke Transformation

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

Convert balanced three-phase quantities to balanced two-phase quadrature quantities

# C2000 Clarke Transformation

Convert balanced three-phase quantities to balanced two-phase quadrature
quantities

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

This block converts balanced three-phase quantities into balanced two-phase
quadrature quantities. The transformation implements these equations

and is illustrated in the following figure.

The inputs to this block are the phase a (`As`) and phase b
(`Bs`) components of the balanced three-phase quantities and the outputs
are the direct axis (`Alpha`) component and the quadrature axis
(`Beta`) of the transformed signal.

The instantaneous outputs are defined by the following equations and are shown in the
following figure:

The variables used in the preceding equations and figures correspond to the variables on
the block as shown in the following table:

|  | Equation Variables | Block Variables |
| --- | --- | --- |
| Inputs | ia | As |
|  | ib | Bs |
| Outputs | id | Alpha |
|  | iq | Beta |

**Note**

- To generate optimized code from this block, enable the `TI
  C28x` or `TI C28x (ISO)` CRL.
- The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
  setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the
  block input. See Using the IQmath Library for more
  information.

- C2000 Clarke Transformation block
