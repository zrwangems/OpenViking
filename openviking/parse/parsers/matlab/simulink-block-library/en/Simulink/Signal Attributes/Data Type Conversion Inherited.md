---
type: simulink-block
title: 'Data Type Conversion Inherited'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypeconversioninherited'
documentation_source_path: 'slref/datatypeconversioninherited.html'
language: en
---

# Data Type Conversion Inherited

## Ports
```yaml
ports:
- name: Port_1
  summary: Reference signal scalar | vector | matrix | N-D array
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: u
  summary: Input signal to convert scalar | vector | matrix | N-D array
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: y
  summary: Output signal scalar | vector | matrix | N-D array
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
```

### Input

### **Port\_1** — Reference signal scalar | vector | matrix | N-D array

Reference signal, defining the data type used to convert input signal
**u**.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — Input signal to convert scalar | vector | matrix | N-D array

Input signal to convert to the reference data type, specified as a
scalar, vector, matrix, or N-D array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **y** — Output signal scalar | vector | matrix | N-D array

Output is the input signal **u**, converted to the reference data
type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
## Parameters
```yaml
parameters:
- name: Input and Output to have equal
  summary: Constraint for converting fixed-point data types Real World Value (default) | Stored Integer
  group: ''
  block_parameter: ConvertRealWorld
  type: character vector
  values: '''Real World Value'' | ''Stored Integer'''
  default: '''Real World Value'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: ''
  block_parameter: RndMeth
  type: character vector
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate to max or min when overflows occur
  summary: Method of overflow action off (default) | on
  group: ''
  block_parameter: DoSatur
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Input and Output to have equal** — Constraint for converting fixed-point data types `Real World Value` (default) | `Stored Integer`

Specify which type of input and output must be equal, in the context of fixed-point data
representation.

- `Real World Value` — Specifies the goal
  of making the `Real World Value` of the
  input equal to the `Real World Value` of
  the output.
- `Stored Integer` — Specifies the goal of
  making the `Stored Integer` value of the
  input equal to the `Stored Integer` value
  of the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConvertRealWorld` |
| **Type:** character vector |
| **Values:** `'Real World Value' | 'Stored Integer'` |
| **Default:** `'Real World Value'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

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

Simulink / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Convert from one data type to another using inherited data type and scaling

The Data Type Conversion Inherited block converts one input to the data type
and scaling of the other input. The first input is used as the reference signal. The
second input, **u**, is converted to the reference type by inheriting
the data type and scaling information. (For a description of the port order for various
block orientations, see Identify Port Location on Rotated or Flipped Block.)

Inheriting the data type and scaling provides these advantages:

- It makes reusing existing models easier.
- It allows you to create new fixed-point models with less effort since you can avoid the detail of specifying the associated parameters.
