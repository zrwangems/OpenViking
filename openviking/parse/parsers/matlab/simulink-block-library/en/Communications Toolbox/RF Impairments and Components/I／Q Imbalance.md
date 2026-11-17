---
type: simulink-block
title: 'I/Q Imbalance'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'iqimbalance'
documentation_source_path: 'ref/iqimbalance.html'
language: en
---

# I/Q Imbalance

## Ports
```yaml
ports:
- name: In1
  summary: Complex signal scalar | vector
  direction: input
  data_types: double | single
- name: Out1
  summary: Output signal scalar | vector
  direction: output
```

### Input

### **In1** — Complex signal scalar | vector

Complex signal, specified as a scalar or vector.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out1** — Output signal scalar | vector

Output signal, returned as a scalar or vector. This output is the same dimension and
data type as the input signal.
## Parameters
```yaml
parameters:
- name: I/Q amplitude imbalance (dB)
  summary: I/Q amplitude imbalance 0 (default) | scalar
  group: ''
- name: I/Q phase imbalance (deg)
  summary: I/Q phase imbalance 0 (default) | scalar
  group: ''
- name: I dc offset
  summary: In-phase component DC offset 0 (default) | scalar
  group: ''
- name: Q dc offset
  summary: Quadrature component DC offset 0 (default) | scalar
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **I/Q amplitude imbalance (dB)** — I/Q amplitude imbalance `0` (default) | scalar

I/Q amplitude imbalance in decibels of signal power, specified as a scalar. For more
information, see Algorithms.

### **I/Q phase imbalance (deg)** — I/Q phase imbalance `0` (default) | scalar

I/Q amplitude imbalance in degrees, specified as a scalar.

### **I dc offset** — In-phase component DC offset `0` (default) | scalar

In-phase component DC offset, specified as a scalar.

### **Q dc offset** — Quadrature component DC offset `0` (default) | scalar

Quadrature component DC offset, specified as a scalar.
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

**Introduced before R2006a**

## Description

Apply I/Q imbalances to complex signal

The I/Q Imbalance block applies in-phase and quadrature imbalances to a complex signal. This
block applies an amplitude imbalance, a phase imbalance, and a DC offset to the in-phase and
quadrature signal components. For more information, see I/Q Imbalance Implementation and Algorithms.
