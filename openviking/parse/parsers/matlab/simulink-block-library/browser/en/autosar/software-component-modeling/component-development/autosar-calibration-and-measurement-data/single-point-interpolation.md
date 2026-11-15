---
type: simulink-block
title: 'Single Point Interpolation'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Calibration and Measurement Data'
documentation_page: 'singlepointinterpolation'
documentation_source_path: 'ref/singlepointinterpolation.html'
language: en
---

# Single Point Interpolation

## Ports

### Input

### **u1** — First input signal scalar | vector

Input signal, specified as a scalar or vector.

**Data Types:** `single`

### **u2** — Second input signal scalar | vector

Input signal, specified as a scalar or vector.

**Data Types:** `single`

### **f** — Fraction value scalar

Coefficient for the `Ifl_Interpolate_f32` routine.

#### Dependencies

To enable this port, set the Source field of the Fraction parameter to
Input port.

**Data Types:** `single`
### Output

### **y** — Output signal scalar | vector

Output signal, returned as a scalar or vector.

**Data Types:** `single`

## Parameters

### **Fraction** — Fraction source and value `0` (default) | scalar

Source and value of the coefficient for the `Ifl_Interpolate_f32`
routine.

Specify the **Source** field of this parameter as one of these values.

- `Dialog` — Set the coefficient using the
  **Value** field of this parameter.
- `Input port` — Set the coefficient using the
  `f` port. The block uses the value of this port as the
  coefficient.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FractionValue` |
| **Type:** character vector |
| **Values:** `'0' |` scalar |
| **Default:** `'0'` |

## Libraries

AUTOSAR Blockset / Classic Platform / Library Routines / Interpolation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: AUTOSAR Code Replacement Library Supports Schema After Release 4.0

Starting in 25a, the AUTOSAR code replacement library supports AUTOSAR schema versions
after AUTOSAR 4.0. To use the latest AUTOSAR routines, in the model Configuration Parameters
dialog box in the **Code Generation** > **Interface** pane, specify **Code replacement libraries** as
`AUTOSAR 4.x`.

## Description

Perform single point interpolation

The Single Point Interpolation block performs linear interpolation using
the AUTOSAR `Ifl_Interpolate_f32` routine. The Single Point
Interpolation block performs interpolation using inputs
*u*1 and
*u*2 and a fraction source parameter
*f* according to this equation: y=u1+f(u2−u1)

You can specify the fraction source using the Block Parameters dialog box or an Input
port. The Single Point Interpolation block supports software-in-the-loop (SIL)
mode.

When you select the AUTOSAR 4.x code replacement library (CRL) for your AUTOSAR model,
your model replaces code that you generate for this block with a call to the
`Ifl_Interpolate_f32` AUTOSAR library routine.
