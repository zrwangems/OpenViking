---
type: simulink-block
title: '2-D IDCT'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: '2didct'
documentation_source_path: 'ref/2didct.html'
language: en
---

# 2-D IDCT

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data matrix | vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Output data matrix | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Port\_1** — Input data matrix | vector

Specify input data as a vector or matrix of intensity values. The number of
elements in the input data must be a power of two.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Port\_1** — Output data matrix | vector

Output data containing the 2-D IDCT of the input, returned as a matrix or vector.
The size and data type of the output are the same as those of the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
## Parameters
```yaml
parameters:
- name: Sine and cosine computation
  summary: How the block computes sine and cosine terms Table lookup (default) | Trigonometric fcn
  group: ''
- name: Lock data type settings against change by the fixed-point tools
  summary: Data type override off (default) | on
  group: ''
```

**Main**

### **Sine and cosine computation** — How the block computes sine and cosine terms `Table lookup` (default) | `Trigonometric fcn`

Specify how the block computes the sine and cosine terms to find the 2-D IDCT.

- `Table lookup` — The block computes and stores the
  trigonometric values before the simulation starts. This option requires more
  memory than the `Trigonometric fcn` option.
- `Trigonometric fcn` — The block computes the sine and
  cosine values during the simulation.

**Data Types**

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Data type override `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Computer Vision Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute 2-D inverse discrete cosine transform (IDCT)

The 2-D IDCT block calculates the two-dimensional inverse discrete cosine transform of the
input signal. The equation for the two-dimensional IDCT of an input signal is:

f(x,y)=2MN∑m=0M−1∑n=0N−1C(m)C(n)F(m,n)cos(2x+1)mπ2Mcos(2y+1)nπ2N,

where *F*(*m*,*n*) is the discrete cosine transform (DCT) of the signal *f*(*x*,*y*). If m=n=0, then C(m)=C(n)=1/2. Otherwise C(m)=C(n)=1.
