---
type: simulink-block
title: 'Real Cepstrum'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'realcepstrum'
documentation_source_path: 'ref/realcepstrum.html'
language: en
---

# Real Cepstrum

## Ports
```yaml
ports:
- name: Input
  summary: Input vector | matrix
  direction: input
  data_types: single | double
- name: Output
  summary: Real cepstrum output vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **Input** — Input vector | matrix

Specify the input *u* as a vector or a matrix of size
*M*-by-*N*. The block treats each
column of the input as an independent channel containing
*M* consecutive samples. The block always processes
unoriented vector inputs as a single channel, and returns the result as
a length-*M* column vector. The block does not accept
complex-valued inputs.

**Data Types:** `single` | `double`
### Output

### **Output** — Real cepstrum output vector | matrix

Real cepstrum output, returned as an
*Mo*-by-*N*
matrix.

When you clear the **Inherit FFT length from input port
dimensions** parameter,
*Mo* is the value you
specify in the **FFT length** parameter. When you
select the **Inherit FFT length from input port
dimensions** parameter,
*Mo* = *M*,
where *M* is the frame size (number of rows) of the
input signal.

Each output column contains the
length-*Mo* real
cepstrum of the corresponding input column.

The output port rate is the same as the input port rate.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Inherit FFT length from input port dimensions
  summary: Match the FFT length to the dimensions of the input port on (default) | off
  group: ''
- name: FFT length
  summary: Compute FFT length 64 (default) | positive integer
  group: ''
```

### **Inherit FFT length from input port dimensions** — Match the FFT length to the dimensions of the input port `on` (default) | `off`

When you select this check box, the output frame size
*Mo* matches the input frame
size *M*.

### **FFT length** — Compute FFT length `64` (default) | positive integer

The number of frequency points at which to compute the FFT, which is also the output
frame size *Mo*.

#### Dependency

To enable this parameter, clear the **Inherit FFT length from
input port dimensions** parameter.
## Libraries

DSP System Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Compute real cepstrum of input

The Real Cepstrum block computes the real cepstrum of the input.
