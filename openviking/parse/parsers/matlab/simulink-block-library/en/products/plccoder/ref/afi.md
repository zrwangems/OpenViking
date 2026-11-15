---
type: simulink-block
title: 'AFI'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'afi'
documentation_source_path: 'ref/afi.html'
language: en
---

# AFI

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.
### Output

### **EnableOut** — Enable Output off (default) | on

When the block executes, it automatically sets the **EnableOut**
to false. This disables the subsequent blocks on the rung.

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

Always False

The AFI block implements the `AFI` ladder logic
instruction. This block sets its **EnableOut** signal to false. Use this
block to temporarily disable a rung while you are debugging.
