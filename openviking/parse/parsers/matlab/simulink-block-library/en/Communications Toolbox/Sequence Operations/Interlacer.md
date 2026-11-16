---
type: simulink-block
title: 'Interlacer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'interlacer'
documentation_source_path: 'ref/interlacer.html'
language: en
---

# Interlacer

## Ports

### Input

### **O** — Odd-numbered elements vector

Odd-numbered elements, specified as a vector. The complexity of inputs
`O` and `E` must match.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **E** — Even-numbered elements vector

Even-numbered elements, specified as a vector. The complexity of
inputs `O` and `E` must
match.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Output signal column vector

Output signal, returned as an even length column vector. Odd numbered
elements in the output vector contain the elements from input
`O` and even numbered elements in the output
vector contain the elements from input `E`. The
output vector has the same data type and sample time as the
input.

## Parameters

Not documented in R2025b.

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

Alternately select elements from two input vectors to generate output vector

The Interlacer block accepts two vector with the size, complexity, and
sample time. It produces one output vector by alternating elements from the first input
(labeled `O` for odd) and the second input (labeled
`E` for even).
