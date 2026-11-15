---
type: simulink-block
title: 'OTU'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'otu'
documentation_source_path: 'ref/otu.html'
language: en
---

# OTU

## Ports

Not documented in R2025b.

## Parameters

### **Operand Tag** — Bit to be tested A (default) | boolean

Specify the data bits to be modified. Data bits are specified in the format of
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
| **Default**: `'A'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Output Unlatch

`OTU` is one of the building blocks of a ladder diagram. The
OTU block implements the `OTU` ladder logic instruction.
When the rung condition is true, the block clears the operand tag (data bit) to false. When
the rung condition is changed to false, the block does not change the status of the data bit.
It is generally used after the OTL block to unlatch the state and disable the rung.
