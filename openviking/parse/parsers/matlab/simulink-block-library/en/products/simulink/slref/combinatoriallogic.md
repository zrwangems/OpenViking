---
type: simulink-block
title: 'Combinatorial Logic'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'combinatoriallogic'
documentation_source_path: 'slref/combinatoriallogic.html'
language: en
---

# Combinatorial Logic

## Ports

### Input

### **Port\_1** — Input signal vector

Input signal, specified as a vector. The type of signals accepted by a
Combinatorial Logic block depends on whether you
selected the Boolean logic signals option (see Implement logic signals as Boolean data (vs. double)). If
this option is enabled, the block accepts real signals of type
`Boolean` or `double`.

**Data Types:** `double` | `Boolean`
### Output

### **Port\_2** — Output signal scalar | vector

Output signal, `double` if the truth table contains
non-Boolean values of type `double`;
`Boolean` otherwise. The type of the output is the
same as that of the input except that the block outputs
`double` if the input is `Boolean`
and the truth table contains non-Boolean values.

**Data Types:** `double` | `Boolean`

## Parameters

### **Truth table** — Matrix of outputs matrix

You specify a matrix that defines all possible block outputs as the
**Truth table** parameter. Each row of the matrix
contains the output for a different combination of input elements. You must
specify outputs for every combination of inputs. The number of columns is
the number of block outputs.

The **Truth table** parameter can have Boolean values (0
or 1) of any data type, including fixed-point data types. If the table
contains non-Boolean values, the data type of the table must be
`double`.

The relationship between the number of inputs and the number of rows
is:

`number of rows = 2(number of
inputs)`

Simulink® returns a row of the matrix by computing the row's index from
the input vector elements. Simulink computes the index by building a binary number where input
vector elements having zero values are 0 and elements having nonzero values
are 1, then adding 1 to the result. For an input vector,
`u`, of `m` elements:

`row index = 1 +
u(m)*2`0 `+
u(m-1)*2`1 `+ ... +
u(1)*2`m-1

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TruthTable` |
| **Type**: character vector |
| **Values**: matrix |
| **Default**: `'[0 0;0 1;0 1;1 0;0 1;1 0;1 0;1 1]'` |

## Libraries

Simulink / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement truth table

The Combinatorial Logic block implements a standard truth table for
modeling programmable logic arrays (PLAs), logic circuits, decision tables, and other
Boolean expressions. You can use this block in conjunction with Memory blocks to implement finite-state machines or flip-flops.

**Tip**

To programmatically add this block to a model named `untitled`,
use a command such as:

```
open_system(new_system);
add_block(sprintf('simulink/Logic and Bit\nOperations/Combinatorial \nLogic'),...
'untitled/Combinatorial Logic');
```
