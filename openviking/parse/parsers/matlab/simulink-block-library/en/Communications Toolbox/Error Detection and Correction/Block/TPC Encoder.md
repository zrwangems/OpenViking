---
type: simulink-block
title: 'TPC Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'tpcencoder'
documentation_source_path: 'ref/tpcencoder.html'
language: en
---

# TPC Encoder

## Ports

### Input

### **In** — Message to encode column vector

Input message bits to encode, specified as a column vector.

- For full-length input messages, the length of the column vector must be the
  product of Number of rows in message, Kr and Number of columns in message, Kc.
- For shortened input messages, the length of the column vector must be the
  product of Number of rows in shortened message, Sr and Number of columns in shortened message, Sc.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — TPC-encoded message column vector

TPC-encoded message, returned as a column vector with the same data type as the
input signal.

- For full-length input messages, the length of the column vector is the
  product of Number of rows in code, Nr and Number of columns in code, Nc.
- For shortened input messages, the length of the column vector is the product
  of
  (*N*R–*K*R+*S*R)
  and
  (*N*C–*K*C+*S*C), where:

  - *N*R is the value of Number of rows in code, Nr.
  - *K*R is the value of Number of rows in message, Kr.
  - *S*R is the value of Number of rows in shortened message, Sr.
  - *N*C is the value of Number of columns in code, Nc.
  - *K*C is the value of Number of columns in message, Kc.
  - *S*C is the value of Number of columns in shortened message, Sc.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Row TPC parameters

### **Extended codes** — Extended codes indicator for TPC row parameters `on` (default) | `off`

- When Extended codes is selected, the lists for Number of rows in code, Nr and Number of rows in message, Kr contain the valid values for extended
  individual code pairs (*N*R,*K*R).
- When Extended codes is cleared, the lists for Number of rows in code, Nr and Number of rows in message, Kr contain the valid values for nonextended
  individual code pairs (*N*R,*K*R).

### **Number of rows in code, Nr** — Number of rows in product code matrix `16` (default) | integer

Number of rows in the product code matrix, *N*R. The
list of integer values varies depending on the setting for Extended codes.

### **Number of rows in message, Kr** — Number of rows in message matrix `11` (default) | integer

Number of rows in the message matrix, *K*R. The list
of integer values varies depending on the setting for Extended codes and Number of rows in code, Nr.

### **Specify shortened message length** — Specify shortened message length for rows `off` (default) | `on`

Select **Specify shortened message length** to specify a value
for Number of rows in shortened message, Sr.

### **Number of rows in shortened message, Sr** — Number of rows in shortened message matrix `9` (default) | integer

Number of rows in the shortened message matrix, *S*R,
specified as an integer less than or equal to
*K*R. When you specify this parameter,
provide full-length *N*R and
*K*R values to specify the
(*N*R,*K*R)
code pair. This code pair is then shortened to the
(*N*R–*K*R+*S*R,*S*R)
code pair, where:

- *N*R is the value of Number of rows in code, Nr.
- *K*R is the value of Number of rows in message, Kr.
- *S*R is the value of Number of rows in shortened message, Sr.

#### Dependencies

To enable this parameter, select Specify shortened message length.

#### Column TPC parameters

### **Extended codes** — Extended codes indicator for TPC column parameters `on` (default) | `off`

- When Extended codes is selected, the lists for Number of columns in code, Nc and Number of columns in message, Kc contain the valid values for extended
  individual code pairs (*N*C,*K*C).
- When Extended codes is cleared, the lists for Number of columns in code, Nc and Number of columns in message, Kc contain the valid values for
  nonextended individual code pairs (*N*C,*K*C).

### **Number of columns in code, Nc** — Number of columns in product code matrix `32` (default) | integer

Number of columns in the product code matrix, *N*C.
The list of integer values varies depending on the setting for Extended codes.

### **Number of columns in message, Kc** — Number of columns in message matrix `26` (default) | integer

Number of columns in the message matrix, *K*C. The
list of integer values varies depending on the setting for Extended codes and Number of columns in code, Nc.

### **Specify shortened message length** — Specify shortened message length for columns `off` (default) | `on`

Select **Specify shortened message length** to specify a value
for Number of columns in shortened message, Sc.

### **Number of columns in shortened message, Sc** — Number of columns in shortened message matrix `22` (default) | integer

Number of columns in the shortened message matrix,
*S*C, specified as an integer. When you
specify this parameter, provide full-length
*N*C and
*K*C values to specify the
(*N*C,*K*C)
code pair. This code pair is then shortened to the
(*N*C–*K*C+*S*C,
*S*C) code pair, where:

- *N*C is the value of Number of columns in code, Nc.
- *K*C is the value of Number of columns in message, Kc.
- *S*C is the value of Number of columns in shortened message, Sc.

#### Dependencies

To enable this parameter, select Specify shortened message length.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / Error Detection and Correction / Block

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Turbo product code (TPC) encoder

The TPC Encoder block performs 2-D turbo product code (TPC) encoding of an
input message. The product code is a 2-D concatenation of linear block codes. The linear block
codes can be a parity check code, a Hamming code, or a BCH code capable of correcting two
errors. Extended and shortened codes can be applied independently on each dimension. For a
description of 2-D TPC encoding, see Turbo Product Code Construction.

For information about valid code pairs and the error-correcting capability for each valid
code pair, see Component Code Pairs.
