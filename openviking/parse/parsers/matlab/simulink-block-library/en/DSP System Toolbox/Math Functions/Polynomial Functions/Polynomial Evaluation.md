---
type: simulink-block
title: 'Polynomial Evaluation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Polynomial Functions'
documentation_page: 'polynomialevaluation'
documentation_source_path: 'ref/polynomialevaluation.html'
language: en
---

# Polynomial Evaluation

## Ports
```yaml
ports:
- name: In
  summary: Input data vector | matrix
  direction: input
  data_types: single | double
- name: Coeffs
  summary: Polynomial coefficients vector
  direction: input
  data_types: single | double
- name: Out
  summary: Output of the polynomial evaluation vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **In** — Input data vector | matrix

Specify the input data on which the block applies the polynomial
function as a vector or a matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Coeffs** — Polynomial coefficients vector

Specify a vector of coefficients in order of descending exponents. For
more information on how the block operates for various coefficient
vectors, see **Constant coefficients**.

#### Dependencies

To enable this port, clear the **Use constant coefficients**
parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Out** — Output of the polynomial evaluation vector | matrix

The block applies the polynomial function on the input data and
outputs a vector or a matrix of the same size and complexity as the
input data.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Use constant coefficients
  summary: Use constant coefficients off (default) | on
  group: ''
- name: Constant coefficients
  summary: Constant coefficients [5 4 3 2 1] (default) | vector
  group: ''
```

### **Use constant coefficients** — Use constant coefficients `off` (default) | `on`

When you select the **Use constant coefficients** parameter, you specify
the polynomial expression in the **Constant coefficients**
parameter. When you do not select the **Use constant
coefficients** parameter, you specify a variable polynomial
expression through the **Coeffs** port. In both cases, the
polynomial is specified as a vector of real or complex coefficients in the
order of descending exponents.

### **Constant coefficients** — Constant coefficients `[5 4 3 2 1]` (default) | vector

Specify the vector of polynomial coefficients to apply to the input in
order of descending exponents.

This table shows how the block operates with different coefficient vectors.

| Coefficient Vector | Equivalent Polynomial Expression |
| --- | --- |
| `[1 2 3 4 5]` | y=u4+2u3+3u2+4u+5 |
| `[1 0 3 0 5]` | y=u4+3u2+5 |
| `[1 2+i 3 4-3i 5i]` | y=u4+(2+i)u3+3u2+(4−3i)u+5i |

#### Dependencies

To enable this parameter, select the **Use constant
coefficients** check box.

**Complex Number Support:** Yes
## Libraries

DSP System Toolbox / Math Functions / Polynomial Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Evaluate polynomial expression

The Polynomial Evaluation block applies a polynomial function to the
real or complex input at the **In** port.

The equivalent MATLAB® code is shown here.

```
y = polyval(u)
```

The Polynomial Evaluation block performs this operation more
efficiently than the equivalent construction using the Sum (Simulink) and Math Function (Simulink) blocks.
