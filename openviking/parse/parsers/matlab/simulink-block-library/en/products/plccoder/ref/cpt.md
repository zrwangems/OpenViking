---
type: simulink-block
title: 'CPT'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'cpt'
documentation_source_path: 'ref/cpt.html'
language: en
---

# CPT

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.
### Output

### **EnableOut** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

### **dest** — Output Signal scalar

The result obtained after computing the expression is placed at the
destination.

**Data Types:** `int8` | `int16` | `int32` | `single`

## Parameters

### **Expression to Evaluate** — Expression to evaluate 'Expr' (default) | character vector

Specify the expression to be evaluated. An expression consisting of
`tags` and/or immediate values separated by operators. In Ladder
Diagrams, tags (variables) are used to represent inputs, outputs, and internal memory
with attributes such as `Data Type`, `Initial Value`,
and `size`. To change the attributes of the `Expression to
Evaluate`, open the **Program Variables** table within the
Ladder Diagram Program block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCOperandTag` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'Expr'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Evaluate expression

The CPT block implements the `CPT` ladder logic
instruction. When the rung conditions are true, the block evaluates the expression
**Expr** and outputs the result to the destination
(`dest`).
