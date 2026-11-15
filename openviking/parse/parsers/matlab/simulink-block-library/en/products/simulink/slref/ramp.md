---
type: simulink-block
title: 'Ramp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'ramp'
documentation_source_path: 'slref/ramp.html'
language: en
---

# Ramp

## Ports

### Output

### **Port\_1** — Output signal scalar | vector | matrix

Generated output ramp signal characterized by the **Slope**,
**Start time**, and **Initial
output** parameters.

**Data Types:** `double`

## Parameters

### **Slope** — Slope of signal 1 (default) | scalar | vector | matrix

Specify the rate of change of the generated signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `slope` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

### **Start time** — Time output begins 0 (default) | scalar

Specify the time at which the block begins generating the signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `start` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Initial output** — Initial value of output signal 0 (default) | scalar | vector | matrix

Specify the initial value of the output signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if
the **Slope**, **Start time**, or
**Initial output** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of
  length `N` if the **Slope**,
  **Start time**, or **Initial
  output** parameter evaluates to an
  `N`-element row or column vector. For example, the
  block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector
  of length `N` if the **Slope**,
  **Start time**, or **Initial
  output** parameter evaluates to an
  `N`-element row or column vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

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

## Version History

**Introduced before R2006a**

## Description

Generate constantly increasing or decreasing signal

The Ramp block generates a signal that starts at a specified time and value
and changes by a specified rate. The block's **Slope**, **Start
time**, and **Initial output** parameters determine the
characteristics of the output signal. All must have the same dimensions after scalar
expansion.
