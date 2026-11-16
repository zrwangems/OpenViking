---
type: simulink-block
title: 'Sample-Rate Match'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'sampleratematch'
documentation_source_path: 'ref/sampleratematch.html'
language: en
---

# Sample-Rate Match

## Ports

### Input

### **In1** — First input signal column vector | matrix

First input signal, specified as a column vector or a
*K*1-by-*N*chan1
matrix. *K*1 is the number of rows and
*N*chan1 is the number of channels in the
input signal matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **In2** — Second input signal column vector | matrix

Second input signal, specified as a column vector or a
*K*2-by-*N*chan2
matrix. *K*2 is the number of rows and
*N*chan2 is the number of channels in the
input signal matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Out** — Output signal matrix

Output signal, returned as a
*P*-by-(*N*chan1+*N*chan2)
matrix of the same data type as the input signals. *P* is the
`Output samples per
frame` parameter value.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Input sample rate (Hz)** — Sample rate of each input signal [1 2]\*1e6 (default) | 2-element vector

Sample rate of each input signal in Hz, specified as a 2-element vector of positive
values.

### **Output samples per frame** — Number of samples output per frame 1000 (default) | positive integer

Number of samples output per frame, specified as a positive integer.

### **Output sample rate options** — Options for output sample rate `Auto` (default) | `Specify via property`

Options for the output sample rate, specified as either `Auto` or
`Specify via property`.

- `Auto` — The output sample rate is set to the highest value in
  the `Input sample rate
  (Hz)` parameter.
- `Specify via property` — Specify the output sample rate value
  using the `Output sample rate
  (Hz)` parameter.

### **Output sample rate (Hz)** — Output signal sample rate 2e6 (default) | positive scalar

Output signal sample rate in Hz, specified as a positive scalar. The value must be
greater than or equal to the `Input sample rate
(Hz)` parameter values.

#### Dependencies

To enable this parameter, set the `Output sample rate
options` parameter to `Specify via property`.

## Libraries

Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Upsample two signals to common rate

The Sample-Rate Match block upsamples the input signals, as needed, to a common output sample
rate. This block introduces delays to your simulation. Use the `srmdelay` function
to compute the delay that will be introduced.
