---
type: simulink-block
title: 'Float Extract Bits'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'floatextractbits'
documentation_source_path: 'slref/floatextractbits.html'
language: en
---

# Float Extract Bits

## Ports
```yaml
ports:
- name: Port_1
  summary: Signal containing floating-point data scalar | vector | matrix
  direction: input
  data_types: single | double | half | bus
- name: Port_1
  summary: Binary representation of data scalar | vector | matrix
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Signal containing floating-point data scalar | vector | matrix

Signal containing floating-point data, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `half` | `bus`
### Output

### **Port\_1** — Binary representation of data scalar | vector | matrix

Binary representation of data, returned as a scalar, vector, or matrix.
Float Extract Bits calculates the fixed point output based on the **Output
mode** parameter.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Output mode
  summary: Parts of data to output All bits (default) | Range of bits | Sign | Mantissa | Exponent
  group: ''
  block_parameter: OutputMode
  type: character vector
  values: '''All bits'' | ''Range of bits'' | ''Sign'' | ''Mantissa'' | ''Exponent'''
  default: '''All bits'''
- name: Bit range ([start end], 0-based relative to LSB)
  summary: Range of bits to return [0 15] (default) | vector
  group: ''
  block_parameter: BitRange
  type: character vector
  values: '''[0 15]'' | vector'
  default: '''[0 15]'''
```

### **Output mode** — Parts of data to output `All bits` (default) | `Range of bits` | `Sign` | `Mantissa` | `Exponent`

Parts of data to output as its binary representation, specified as:

- `All bits`
- `Range of bits`
- `Sign`
- `Mantissa`
- `Exponent`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputMode` |
| **Type**: character vector |
| **Values**: `'All bits'` | `'Range of bits'` | `'Sign'` | `'Mantissa'` | `'Exponent'` |
| **Default**: `'All bits'` |

### **Bit range ([start end], 0-based relative to LSB)** — Range of bits to return `[0 15]` (default) | vector

Range of bits of the signal to return, specified as a vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitRange` |
| **Type**: character vector |
| **Values**: `'[0 15]'` | vector |
| **Default**: `'[0 15]'` |
## Libraries

Simulink / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `half` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Extract bits from floating-point input samples

The Float Extract Bits block accepts a signal containing floating-point
data and outputs a signal containing the binary representation of the data. For more
information on this binary representation, see the IEEE Standard for Floating Point
Arithmetic.
