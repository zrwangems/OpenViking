---
type: simulink-block
title: 'Probabilistic Rule Agg'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'probabilisticruleagg'
documentation_source_path: 'probabilisticruleagg.html'
language: en
---

# Probabilistic Rule Agg

## Ports

### Input

### **In1** — Input values row vector

Input values, specified as a row vector with the same number of elements as
**In2**.

### **In2** — Input values row vector

Input values, specified as a row vector with the same number of elements as
**In1**.
### Output

### **Out1** — Probabilistic OR values row vector

Probabilistic OR values, returned as a row vector *y* with the
same number of elements as both **In1** and **In2**.
Each element of *y* contains the probabilistic OR of the
corresponding elements from the input vectors.

Let `A` = **In1** and `B` =
**In2**. Then, the probabilistic OR of the *i*th
elements of the input vectors is the following algebraic sum.

```
y(i) = A(i) + B(i) - A(i)*B(i);
```

## Parameters

Not documented in R2025b.

## Libraries

Fuzzy Logic Toolbox / Membership Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**

## Description

Probabilistic OR function for rule aggregation

The Probabilistic Rule Agg block returns the element-wise probabilistic OR,
or algebraic sum, of the two input vectors.
