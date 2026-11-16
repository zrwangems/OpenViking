---
type: simulink-block
title: 'Ramp'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Library Routines / Math Operations'
documentation_page: 'ramp'
documentation_source_path: 'ref/ramp.html'
language: en
---

# Ramp

## Ports

### Input

### **u** — Input signal scalar

Input signal used to generate ramp signal, specified as a scalar.

**Data Types:** `single`

### **R** — Reset port scalar

Option to reset the output signal to the initial condition, specified as a
scalar.

#### Dependencies

To enable this port, select the **Show reset port**
parameter.

**Data Types:** `Boolean`

### **rs** — Rise slope scalar

The rate at which the output signal is increased, specified as a scalar.

#### Dependencies

To enable this port, set the **Source** field of the **Rise
slope** parameter to `Input port`.

**Data Types:** `single`

### **fs** — Fall slope scalar

The rate at which the output signal is decreased, specified as a scalar.

#### Dependencies

To enable this port, set the **Source** field of the
**Fall
Slope** parameter to `Input port`.

**Data Types:** `single`
### Output

### **Port\_1** — Output signal scalar

Output signal, returned as a scalar.

**Data Types:** `single`

## Parameters

### **Rise slope** — Increase value of output `Dialog` | `Input port`

Specify the **Source** field of this parameter as one the following values.

- `Dialog` — Set the slope using the
  **Value** field of this parameter.
- `Input port` — Set the slope using the
  **rs** port. The block uses the value from this port as the
  slope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RiseSlope` |
| **Type:** character vector |
| **Values:** real finite nonnegative values |
| **Default:** `'1'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RiseSlopeSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Fall slope** — Decrease value of output scalar

Specify the **Source** field of this parameter as one the following values.

- `Dialog` — Set the slope using the
  **Value** field of this parameter.
- `Input port`  — Set the slope using the
  **fs** port. The block uses the value from this port as the
  slope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FallSlope` |
| **Type:** character vector |
| **Values:** real finite nonnegative values |
| **Default:** `'1'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FallSlopeSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input Port'` |
| **Default:** `'Dialog'` |

### **Show reset port** — Option to add `R` input port `'off'` (default) | `'on'`

Enable the **R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowResetPort` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Initial condition** — Initial value of output signal `0` (default) | double

The initial condition of the output signal, specified as a double. The default is
`0`.

When **Show reset port** is selected, the initial condition is set
to the value specified in the **Initial Condition** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** real finite values |
| **Default:** `'0'` |

### **Sample time** — Sample period `-1` (default) | `[-1, 0]` | vector

Specify the sample period in seconds.

For more information specifying discrete sample times, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** real finite values |
| **Default:** `'-1'` |

## Libraries

AUTOSAR Blockset / Classic Platform / Library Routines / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

### R2025a: AUTOSAR Code Replacement Library Supports Schema After Release 4.0

Starting in 25a, the AUTOSAR code replacement library supports AUTOSAR schema versions
after AUTOSAR 4.0. To use the latest AUTOSAR routines, in the model Configuration Parameters
dialog box in the **Code Generation** > **Interface** pane, specify **Code replacement libraries** as
`AUTOSAR 4.x`.

## Description

Generate signal that follows input value bound by rising or falling slope

The Mathematical Floating point Library (MFL) Ramp block generates a signal
that starts at a specified value and changes by a specified rate until the value of the input
signal is reached. The block parameters **Rise slope**, **Fall
slope**, **Initial condition**, and **Sample
time**, and the input signal **u** determine the characteristics
of the output signal.

When you select the `AUTOSAR 4.x` Code Replacement Library (CRL) for your
AUTOSAR model, your model replaces code that you generate for this block with calls to the
following AUTOSAR library routines:

- `Mfl_Ramp_InitState`
- `Mfl_Ramp_SetParam`
- `Mfl_RampCalc`
- `Mfl_RampOut_f32`
