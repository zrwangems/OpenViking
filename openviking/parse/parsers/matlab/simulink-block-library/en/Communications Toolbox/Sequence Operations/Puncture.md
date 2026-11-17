---
type: simulink-block
title: 'Puncture'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'puncture'
documentation_source_path: 'ref/puncture.html'
language: en
---

# Puncture

## Ports
```yaml
ports:
- name: In
  summary: Input signal column vector
  direction: input
  data_types: double | single
- name: Out
  summary: Output signal column vector
  direction: output
```

### Input

### **In** — Input signal column vector

Input signal, specified as a column vector. The input length must be
an integer multiple of the **Puncture vector**
parameter length.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Output signal column vector

Output signal, returned as a column vector. The length of the output
vector is an integer multiple of the number of 1s in the
**Puncture vector** parameter. The output signal
contains only elements from the input signal that align with integer
multiples of the element location of 1s in the **Puncture
vector**.
## Parameters
```yaml
parameters:
- name: Puncture vector
  summary: Puncture pattern [1 1 0 1 0 1]' (default) | column vector of binary values
  group: ''
```

### **Puncture vector** — Puncture pattern `[1 1 0 1 0 1]'` (default) | column vector of binary values

Puncture pattern, specified as a column vector of binary values. The input
signal length must be an integer multiple of the **Puncture
vector** parameter length. The block repeats the puncturing
pattern, as necessary, to include all input elements.

- The element locations of 0s in **Puncture
  vector** indicate which elements are removed from
  the input signal to construct the output signal.
- The element locations of 1s in **Puncture
  vector** indicate which elements are preserved from
  the input signal to construct the output signal.
## Libraries

Communications Toolbox / Sequence Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Output elements that correspond to 1s in binary puncture vector

The Puncture block creates an output vector by removing selected
elements of the input vector and preserving others. The block determines which elements
to remove and preserve by using the binary **Puncture vector**
parameter. The block repeats the puncturing pattern, as necessary, to include all input
elements. The preserved elements appear in the output vector in the same order in which
they appear in the input vector.
