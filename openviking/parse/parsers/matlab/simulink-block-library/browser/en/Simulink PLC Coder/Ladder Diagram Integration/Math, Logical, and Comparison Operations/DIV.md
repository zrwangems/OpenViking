---
type: simulink-block
title: 'DIV'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'div'
documentation_source_path: 'ref/div.html'
language: en
---

# DIV

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.

### **srcA** — First input signal scalar

The first input signal to the division operation.

**Data Types:** `int8` | `int16` | `int32` | `single`

### **srcB** — Second input signal scalar

The second input signal to the division operation.

**Data Types:** `int8` | `int16` | `int32` | `single`
### Output

### **EnableOut** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

### **dest** — Output signal scalar

Output signal resulting from the division operation.

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

Divide one input by another

The DIV block implements the `DIV` ladder logic
instruction. When the rung conditions are true, the block divides the dividend at source A
(`srcA`) by the divisor at source B (`srcB`) and outputs
the result to the destination (`dest`).

**Note**

If you perform a divide by zero operation a `"Divide by zero detected"`
diagnostic message is generated during code generation.
