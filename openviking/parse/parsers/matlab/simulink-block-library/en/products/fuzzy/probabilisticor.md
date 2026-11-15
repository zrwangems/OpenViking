---
type: simulink-block
title: 'Probabilistic OR'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'probabilisticor'
documentation_source_path: 'probabilisticor.html'
language: en
---

# Probabilistic OR

## Ports

### Input

### **In1** — Input values array | row vector

Input values, specified as an array or row vector *x*.
### Output

### **Out1** — Probabilistic OR values row vector

Probabilistic OR values, returned as a row vector *y* with the
same number of columns as the input *x*. Each element of
*y* contains the probabilistic OR value for the corresponding
column in *x*.

If *x* has one row, then *y* =
*x*.

If *x* = `[A;B]`, where `A` and
`B` are row vectors, then the *i*th element of
*y* is the following algebraic sum.

```
y(i) = A(i) + B(i) - A(i)*B(i);
```

If *x* has more than two rows, the probabilistic OR is initially
calculated for the first two rows. Then, the probabilistic OR is computed between the
result and the next row. This process repeats for each subsequent row.

```
x = [A;B;C;D]
y(i) = A(i) + B(i) - A(i)*B(i);
y(i) = y(i) + C(i) - y(i)*C(i);
y(i) = y(i) + D(i) - y(i)*D(i);
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

Probabilistic OR function

The Probabilistic OR block returns the probabilistic OR value, or algebraic
sum, for the input signal.
