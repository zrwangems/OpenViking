---
type: simulink-block
title: 'SUB'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'sub'
documentation_source_path: 'ref/sub.html'
language: en
---

# SUB

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.

### **srcA** — First input signal scalar

The first input signal to the subtraction operation.

**Data Types:** `int8` | `int16` | `int32` | `single`

### **srcB** — Second input signal scalar

The second input signal to the subtraction operation.

**Data Types:** `int8` | `int16` | `int32` | `single`
### Output

### **EnableOut** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

### **dest** — Output signal scalar

Output signal resulting from the subtraction operation.

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

Subtract inputs

The SUB block implements the `SUB` ladder logic
instruction. When the rung conditions are true, the block subtracts source B
(`srcB`) from source A (`srcA`) and outputs the result to
the destination (`dest`).
