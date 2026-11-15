---
type: simulink-block
title: 'Deinterlacer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Signal Operations'
documentation_page: 'deinterlacer'
documentation_source_path: 'ref/deinterlacer.html'
language: en
---

# Deinterlacer

## Ports

### Input

### **In** — Input signal column vector

Input signal, specified as an even length column vector.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **O** — Odd-numbered elements vector

Odd-numbered elements of the input vector, returned as a vector. If
the input is a vector of length *N*, the output length
is *N*/2.

### **E** — Even-numbered elements vector

Even-numbered elements of the input vector, returned as a vector. If
the input is a vector of length *N*, the output length
is *N*/2.

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

Distribute elements of input vector alternately between two output vectors

The Deinterlacer block accepts an even length column vector input
signal. The block alternately places the elements in two output vectors. As a result,
each output vector size is half the input vector size. The outputs inherit the sample
time from the **Sample time** parameter of the input block.
