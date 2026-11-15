---
type: simulink-block
title: 'OSR'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'osr'
documentation_source_path: 'ref/osr.html'
language: en
---

# OSR

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.
### Output

### **EN** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

### **OB** — Output Bit boolean

Bit to be modified when the `rung-condition-in` transitions from
false to true.

**Data Types:** `Boolean`

## Parameters

### **Storage Bit** — Internal storage bit SB (default) | boolean

Internal storage bit that retains the `rung-condition-in` from the
last time the instruction was executed. Specified in the format of
`tags`. In Ladder Diagrams, tags (variables) are used to represent
inputs, outputs, and internal memory with attributes such as `Data
Type`, `Initial Value`, and `size`. To
change the attributes of the `Operand Tag`, open the **Program
Variables** table within the Ladder Diagram Program
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCOperandTag` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'SB'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

One Shot Rising

The OSR block implements the `OSR` instruction. The block
sets the output bit for one scan when the `rung-condition-in` transitions
from false to true.
