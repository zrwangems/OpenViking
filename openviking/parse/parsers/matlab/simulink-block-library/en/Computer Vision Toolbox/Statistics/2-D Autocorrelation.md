---
type: simulink-block
title: '2-D Autocorrelation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dautocorrelation'
documentation_source_path: 'ref/2dautocorrelation.html'
language: en
---

# 2-D Autocorrelation

## Ports
```yaml
ports:
- name: Port_1
  summary: Input array vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Autocorrelation of input vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Port\_1** — Input array vector | matrix

Input array, specified as a vector or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Autocorrelation of input vector | matrix

Autocorrelation of the input array, returned as a vector or matrix. The data type
of the output is the same as that of the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Lock data type settings against change by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: ''
```

For details on fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Computer Vision Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

2-D autocorrelation of input matrix

The 2-D Autocorrelation block computes the 2-D autocorrelation of the input
vector or matrix.
