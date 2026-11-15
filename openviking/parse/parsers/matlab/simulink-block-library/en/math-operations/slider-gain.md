---
type: simulink-block
title: 'Slider Gain'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'slidergain'
language: en
---

# Slider Gain

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

The Slider Gain block accepts real or complex-valued scalar, vector, or
matrix input. The block supports fixed-point data types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Input multiplied by gain scalar | vector | matrix

The Slider Gain block outputs the input multiplied by a constant gain
value. When the input to the block is real and gain is complex, the
output is complex.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Slider gain** — Gain value `0` (default) | real value

Chose the gain value applied to the input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gain` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'1'` |

### **Low** — Lower limit of slider range `0` (default) | real value

Specify the lower limit of the slider range.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `low` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0'` |

### **High** — Upper limit of slider range `2` (default) | real value

Specify the upper limit of the slider range.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `high` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'2'` |

## Libraries

Simulink / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Vary scalar gain using slider

The Slider Gain block performs a scalar gain that you can modify during simulation.
Modify the gain using the slider parameter.
