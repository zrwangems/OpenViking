---
type: simulink-block
title: 'Binary File Writer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'binaryfilewriter'
documentation_source_path: 'ref/binaryfilewriter.html'
language: en
---

# Binary File Writer

## Ports

### Input

### **Port\_1** — Data to write column vector | row vector | matrix

The writer block writes the data to the file specified in the
**File name** parameter. If the **File
header** structure is not empty, then the writer writes the
header before writing the data. The block can write floating-point data
and integer data. The input data can be real or complex. When the data
is complex, the block writes the data as interleaved real and imaginary
components. The writer assumes the default endianness of the host
machine.

The input can be a variable-size
signal, that is, you can change the frame size (number of rows) of the
signal during simulation but the number of channels (columns) must
remain constant. *(since R2025a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes

## Parameters

### **File name** — Name of the file `'Untitled.bin'` (default) | character vector

Name of the file to which the block writes the data.

### **File header** — Size of the header `struct([])` (default) | structure

The structure can have an arbitrary number of fields. Each field of the
structure must be a real matrix of a built-in type. For example, if
**File header** is set to
`struct('field1',1:10,'field2',single(1))`, the block
writes a header formed by 10 double-precision values,
`(1:10)`, followed by 1 single precision value,
`single(1)`. If there is no header to write, set this
parameter to an empty structure, `struct([])`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2025a: Support for variable-size signals

The Binary File Writer block supports variable-size input signals,
that is, you can change the frame size (number of rows) of the signal during
simulation but the number of channels (columns) must remain constant.

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Write data to binary files

The Binary File Writer block writes multichannel signal data to a
binary file. The block specifies the name of the file and the structure of the header
that precedes the signal data. If there is no header to write, the block specifies an
empty structure, `struct([])`. The first time you write to the file,
the block writes the header, followed by the data. On subsequent calls, the block writes
the remaining data. If the header is empty, then no header is written.

The block writes the data in a row-major format. For example, if the input array is
`[1 2 4 5; 8 7 9 2]`, the block writes the data as `[1 2 4
5 8 7 9 2]`.
