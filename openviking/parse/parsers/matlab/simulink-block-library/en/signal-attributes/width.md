---
type: simulink-block
title: 'Width'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'width'
language: en
---

# Width

Output width of input vector

## Libraries

Simulink / Signal Attributes

## Description

The Width block generates as output the width of its input
vector.

You can use an array of buses as an input signal to a Width block. For
details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal specified as a scalar, vector, matrix, or N-D
array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Width of input signal scalar

Output is the width of the input signal, specified as a scalar.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Output data type mode** — Output data type mode `Choose intrinsic data type` (default) | `Inherit via back propagation` | `All ports same datatype`

Specify the output data type to be the same as the input, or inherit the
data type by back propagation. You can also choose to specify a built-in
data type from the drop-down list in the **Output data
type** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputDataTypeScalingMode` |
| **Type:** character vector |
| **Values:** `'Choose intrinsic data type' | 'Inherit via back propagation' | 'All ports same datatype'` |
| **Default:** `'Choose intrinsic data type'` |

### **Output data type** — Output data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

This parameter is visible when you select `Choose intrinsic
data type` for **Output data type mode**.
Select a built-in data type from the drop-down list.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Type:** character vector |
| **Values:** `'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32'` |
| **Default:** `'double'` |

### **Always use constant sample time** — Always use constant sample time off (default) | on

To always use a constant sample time, select this parameter. To inherit
the sample time, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AlwaysUseConstantSampleTime` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Width Block Supports Symbolic Dimensions

The Width block has these changes:

- Support for symbolic dimensions.
- New parameter, **Always use constant sample
  time**.
