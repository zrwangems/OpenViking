---
type: simulink-block
title: 'GRT'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'grt'
documentation_source_path: 'ref/grt.html'
language: en
---

# GRT

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.

### **srcA** — First input signal scalar

Value to test against `srcB`.

**Data Types:** `int8` | `int16` | `int32` | `single`

### **srcB** — Second input signal scalar

Value to test against `srcA`.

**Data Types:** `int8` | `int16` | `int32` | `single`
### Output

### **EnableOut** — Enable Output off (default) | on

If the **EnableIn** input to the block is false, the logic
implemented by the block is not executed and **EnableOut** signal is
set to false. If **EnableIn** is true, **EnableOut**
signal is set to true, if `srcA` is greater than
`srcb`.

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

Greater than

The GRT block implements the `GRT` instruction. When the
rung conditions are true,the block verifies whether the value at source A is greater than the
value at source B.
