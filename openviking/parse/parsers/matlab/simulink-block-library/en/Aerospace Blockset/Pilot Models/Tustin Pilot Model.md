---
type: simulink-block
title: 'Tustin Pilot Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Pilot Models'
documentation_page: 'tustinpilotmodel'
documentation_source_path: 'tustinpilotmodel.html'
language: en
---

# Tustin Pilot Model

## Ports

### Input

### **x com** — Signal command scalar

Signal command that the pilot model controls, specified as a scalar.

**Data Types:** `double`

### **x** — Signal controlled by pilot scalar

Signal controlled by pilot, specified as a scalar.

**Data Types:** `double`
### Output

### **u** — Aircraft command scalar

Aircraft command, returned as a scalar.

**Data Types:** `double`

## Parameters

### **Pilot gain** — Pilot gain `1` (default) | scalar

Pilot gain, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Kp` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Pilot time delay(s)** — Pilot time delay `0.1` (default) | scalar

Total pilot time delay, specified as a double scalar, in seconds. This value typically
ranges from 0.1 s to 0.2 s.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `time_delay` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.1'` |

### **Pilot lead constant** — Pilot lead constant `5` (default) | scalar

Pilot lead constant, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `T` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'5'` |

## Libraries

Aerospace Blockset / Pilot Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Represent Tustin pilot model

The Tustin Pilot Model block represents the pilot model that A. Tustin describes in
*The Nature of the Operator’s Response in Manual Control, and its
Implications for Controller Design*
[1]. When modeling
human pilot models, use this block for the least accuracy, compared to that provided by
the Crossover Pilot Model and Precision Pilot Model blocks. This block requires less input than those
blocks, and provides better performance. However, the results might be less
accurate.

This pilot model is a single input, single output (SISO) model that represents human
behavior, and is based on the transfer function described in Algorithms.

This block has nonlinear behavior. If you want to linearize the block (for example, with the
`linearize` (Simulink Control Design) function or one of the
`linmod` functions), you might need to
change the Pade approximation order. The Tustin Pilot Model block implementation
incorporates the Transport Delay block with the
**Pade order (for linearization)** parameter set to
`2` by default. To change this value, use the `set_param` function, for example:

```
set_param(gcb,'pade','3')
```

**Note**

The `linmod` function provides only basic linearization
capabilities. For full linearization functionality, use Simulink®
Control Design™ software. For more information, see Choose Linearization Tools (Simulink Control Design).
