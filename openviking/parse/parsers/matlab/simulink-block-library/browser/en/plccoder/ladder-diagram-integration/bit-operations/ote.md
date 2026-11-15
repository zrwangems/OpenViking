---
type: simulink-block
title: 'OTE'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'ote'
documentation_source_path: 'ref/ote.html'
language: en
---

# OTE

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

Output Energize

`OTE` is one of the building blocks of a ladder diagram. The
OTE block implements the `OTE` ladder logic instruction. The
block examines the state of the `rung-condition-in` and sets or clears the
operand tag (data bit). If rung condition is true, the block sets the data bit to true.
