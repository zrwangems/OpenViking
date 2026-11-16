---
type: simulink-block
title: 'HDL Combinatorial Logic'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'RCP and HIL'
documentation_page: 'hdlcombinatoriallogic'
documentation_source_path: 'ref/hdlcombinatoriallogic.html'
language: en
---

# HDL Combinatorial Logic

## Ports

### Input

### **u** — Input signal vector

Input signal, specified as a vector. The type of signals accepted by an HDL
Combinatorial Logic block depends on whether you selected the Boolean logic
signals option (see Implement logic signals as Boolean data (vs. double)). If this option is
enabled, the block accepts real signals of type `Boolean` or
`double`.

**Data Types:** `double` | `Boolean`
### Output

### **v** — Output signal scalar | vector

Output signal, returned as a `double` scalar or vector if the
truth table represented by **Input table** and **Output
table** contains non-Boolean values of type `double`; or
returned as `Boolean` scalar or vector otherwise. The type of the
output is the same as that of the input except that the block outputs
`double` if the input is `Boolean` and the truth
table contains non-Boolean values.

**Data Types:** `double` | `Boolean`

## Parameters

### **Input table** — Matrix of input permutations matrix

The **Input table** parameter can have Boolean values (0 or 1) of
any data type, including fixed-point data types. If the table contains non-Boolean
values, the data type of the table must be `double`.

The relationship between the number of inputs and the number of rows is:

number of rows = 2(number of inputs)

Simulink® returns a row of the output matrix specified by **Output
table** by computing number based on the input vector elements. Simulink computes the index by building a binary number where input vector elements
having zero values are 0 and elements having nonzero values are 1, then adding 1 to the
result. For an input vector, `u`, of `m`
elements:

row index = 1 +
*u*(*m*)×20+
*u*(*m*-1)×21+ ... +
*u*(1)×2m-1

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `inputTable` |
| **Type**: character vector |
| **Values**: matrix |
| **Default**: `logical([0 1; 1 0; 1 1])` |

### **Output table** — Matrix of outputs matrix

The **Output table** parameter can have Boolean values (0 or 1) of
any data type, including fixed-point data types. If the table contains non-Boolean
values, the data type of the table must be `double`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outputTable` |
| **Type**: character vector |
| **Values**: matrix |
| **Default**: `logical([1 0; 1 0; 1 1])` |

## Libraries

HDL Coder / RCP and HIL

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

## Version History

**Introduced in R2024b**

## Description

Implement truth table

The HDL Combinatorial Logic block implements a standard truth table for
modeling programmable logic arrays (PLAs), logic circuits, decision tables, and other Boolean
expressions. You can use this block in conjunction with Memory blocks to implement finite-state machines or flip-flops.
