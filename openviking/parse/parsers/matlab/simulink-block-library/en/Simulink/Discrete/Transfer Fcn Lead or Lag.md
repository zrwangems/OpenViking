---
type: simulink-block
title: 'Transfer Fcn Lead or Lag'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'transferfcnleadorlag'
documentation_source_path: 'slref/transferfcnleadorlag.html'
language: en
---

# Transfer Fcn Lead or Lag

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal that the block applies the discrete-time lead or lag
compensation to.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is discrete-time lead or lag compensation of the input sign.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Pole of compensator (in Z plane)** — Pole `0.95` (default) | scalar

Specify the pole of the compensator.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PoleZ` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'0.95'` |

### **Zero of compensator (in Z plane)** — Zero of compensator `0.75` (default) | scalar

Specify the zero of compensator in the Z plane.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroZ` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'0.75'` |

### **Initial condition for previous input** — Initial condition for previous input `0.0` (default) | scalar

Specify the initial condition for the previous input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ICPrevInput` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'0.0'` |

### **Initial condition for previous output** — Initial condition for previous output `0.0` (default) | scalar

Specify the initial condition for the previous output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ICPrevOutput` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'0.0'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or minimum value
that the data type can represent. Otherwise, overflows wrap.

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. In general, the code generation process can detect
when overflow is not possible. In this case, the code generator does not produce
saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Discrete

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block is not recommended for use with Boolean signals. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Implement discrete-time lead or lag compensator

The Transfer Fcn Lead or Lag block implements a discrete-time lead or lag
compensator of the input. The instantaneous gain of the compensator is 1, and the DC
gain is equal to `(1-z)/(1-p)`, where `z` is the zero
and `p` is the pole of the compensator.

The block implements a lead compensator when `0<z<p<1`, and
implements a lag compensator when `0<p<z<1`.
