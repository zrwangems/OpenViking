---
type: simulink-block
title: 'NOT'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'not'
documentation_source_path: 'ref/not.html'
language: en
---

# NOT

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.

### **src** — Input signal scalar

The input signal on which to perform the bitwise NOT operation. If the datatype is
`single` (`REAL` – ladder logic equivalent), the
input value is converted to `int32` (`DINT` – ladder
logic equivalent). `int8, int16` (`SINT,INT` –
ladder logic equivalent) datatypes are converted to `int32`
(`DINT` – ladder logic equivalent) by filling the upper bits with
0s.

**Data Types:** `int8` | `int16` | `int32` | `single`
### Output

### **EnableOut** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

### **dest** — Output signal scalar

Output signal resulting from the bitwise NOT operation. If the datatype is
`single` (`REAL` – ladder logic equivalent), the
resultant `int32` (`DINT` – ladder logic equivalent)
is converted to `REAL` (`single` – ladder logic
equivalent).

**Data Types:** `int8` | `int16` | `int32` | `single`

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Bitwise NOT

The NOT block implements the `NOT` ladder logic
instruction. When the rung conditions are true, the block performs bitwise NOT operation on
the values at source. The result of this operation is available at the destination port
(`dest`).
