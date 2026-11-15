---
type: simulink-block
title: 'Multiphase Clock'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'multiphaseclock'
documentation_source_path: 'ref/multiphaseclock.html'
language: en
---

# Multiphase Clock

## Ports

### Output

### **Port\_1** — Vector of clock signals vector

1-by-*N* vector of clock signals, where you specify
*N* using the **Number of phases**
parameter. For more information, see Description.

**Data Types:** `single` | `double` | `Boolean`

## Parameters

### **Clock frequency (Hz)** — Frequency of all clock signals `1` (default) | positive scalar

The frequency of all output clock signals, specified as a positive
scalar.

### **Number of phases, N** — Number of phases in output vector `4` (default) | positive integer

The number of different phases, *N*, in the output
vector, specified as a positive integer scalar.

### **Starting phase (1 to N)** — Vector index for starting phase `1` (default) | integer from 1 to *N*

The vector index of the output signal to first become active, specified as
a scalar integer from `1` to *N*.

### **Number of phase intervals over which clock is active (1 to N-1)** — Duration of active level for each output `3` (default) | integer from 1 to *N*-1

The duration of the active level, *D*, for every output
signal specified as a scalar integer from 1 to *N*-1. The
value you specify determines the number of phase intervals that each signal
remains in the active state after becoming active. The active duty cycle of
the signal is *D*/*N*.

### **Active level (polarity)** — Active level `High (1)` (default) | `Low (0)`

The active level of the output, specified as `High
(1)` or `Low (0)`.

### **Output data type** — Output data type `Logical` (default) | `Boolean`

The output data type, specified as `Logical` or
`Boolean`.

## Libraries

DSP System Toolbox / Signal Management / Switches and Counters DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` | `Boolean` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Generate multiple binary clock signals

The Multiphase Clock block generates a 1-by-*N* vector
of clock signals, where you specify the integer *N* in the
**Number of phases** parameter. Each of the *N*
phases has the same frequency, *f*, specified in hertz by the
**Clock frequency** parameter.

The clock signal indexed by the **Starting phase** parameter is the
first to become active, at *t*=0. The other signals in the output
vector become active in turn, each one lagging the preceding signal's activation by
1/(*N**f*) seconds, the phase interval. The period
of the output is therefore 1/(*N**f*) seconds.

The active level can be either high (`1`) or low
(`0`), as specified by the **Active level
(polarity)** parameter. You specify the duration of the active level,
*D*, as an integer between 1 and *N*-1 using the
**Number of phase intervals over which the clock is active**
parameter. This value specifies the number of phase intervals that each signal remains
in the active state after becoming active. The active duty cycle of the signal is
*D*/*N*.
