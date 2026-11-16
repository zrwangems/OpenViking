---
type: simulink-block
title: 'Repeating Sequence'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'repeatingsequence'
documentation_source_path: 'slref/repeatingsequence.html'
language: en
---

# Repeating Sequence

## Ports

### Output

### **Port\_1** — Periodic output signal scalar

Output signal specified by the **Time values** and
**Output values** parameters to create a periodic
scalar signal.

**Data Types:** `double`

## Parameters

### **Time values** — Vector of output times `[0 2]` (default) | vector

Vector of strictly monotonically increasing time values. The period of the generated
waveform is the difference of the last and first values of this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rep_seq_t` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `[0 2]` |

### **Output values** — Vector of output values `[0 2]` (default) | vector

Vector of output values that specify the output waveform. Each element corresponds to the
time value in the **Time values**parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rep_seq_y` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `[0 2]` |

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

Consider using Repeating Sequence Stair or Repeating
Sequence Interpolated blocks for code generation.

## Version History

**Introduced before R2006a**

## Description

Generate arbitrarily shaped periodic signal

The Repeating Sequence block outputs a periodic scalar signal having a
waveform that you specify using the **Time values** and
**Output values** parameters. The **Time values**
parameter specifies a vector of output times. The **Output values**
parameter specifies a vector of signal amplitudes at the corresponding output times.
Together, the two parameters specify a sampling of the output waveform at points
measured from the beginning of the interval over which the waveform repeats (the period
of the signal).

By default, both parameters are `[0 2]`. These default settings specify a
sawtooth waveform that repeats every `2` seconds from the start of the
simulation and has a maximum amplitude of `2`.
