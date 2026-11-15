---
type: simulink-block
title: 'Algebraic Constraint'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'algebraicconstraint'
documentation_source_path: 'slref/algebraicconstraint.html'
language: en
---

# Algebraic Constraint

## Ports

### Input

### **f(z)** — Input signal real scalar or vector

Signal is subjected to the constraint *f(z) = 0* or
*f(z) = z* to solve the algebraic loop.

**Data Types:** `double`
### Output

### **z** — Output state real scalar or vector

Solution to the algebraic loop when the input signal
**f(z)** is subjected to the constraint
*f(z) = 0* or *f(z) =
z*.

**Data Types:** `double`

## Parameters

### **Constraint** — Constraint on input signal `f(z) = 0` (default) | `f(z) = z`

Type of constraint for which to solve. You can solve for `f(z)
= 0` or `f(z) = z`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Constraint` |
| **Type:** character vector |
| **Values:** `'f(z) = 0' | 'f(z) = z'` |
| **Default:** `'f(z) = 0'` |

### **Solver** — Algebraic Loop Solver `auto` (default) | `Trust region` | `Line search`

Choose between the Trust region [1], [2] or Line search [3] algorithms to
solve the algebraic loop. By default this value is set to
`auto`, which selects the algebraic loop solver based on the
model configuration and switches the solver between the Trust region and Line search algorithm during simulation

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Solver` |
| **Type:** character vector |
| **Values:** `'auto' | 'Trust region' | 'Line search'` |
| **Default:** `'auto'` |

### **Tolerance** — Solver Tolerance `auto` (default) | positive scalar

This option is visible when you explicitly specify a solver to be used
(Trust region or Line Search) in the **Solver** drop-down
menu. Specify a smaller value for higher accuracy or a larger value for
faster execution. By default it is set to
`auto`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Tolerance` |
| **Type:** character vector |
| **Values:** `'auto'` | positive scalar |
| **Default:** `'auto'` |

### **Initial Guess** — Initial guess of solution value 0 (default) | scalar

Initial guess for the algebraic state *z* that is close
to the expected solution value to improve the efficiency of the algebraic
loop solver. By default, this value is set to 0

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialGuess` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

## Libraries

Simulink / Math Operations

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

Constrain input signal

The Algebraic Constraint block constrains the input signal f(*z*)
to *z* or 0 and outputs an algebraic state *z*.
The block outputs a value that produces 0 or *z* at the input. The
output must affect the input through a direct feedback path. In other words, the
feedback path only contains blocks with direct feedthrough. For example, you can specify
algebraic equations for index 1 differential-algebraic systems (DAEs).
