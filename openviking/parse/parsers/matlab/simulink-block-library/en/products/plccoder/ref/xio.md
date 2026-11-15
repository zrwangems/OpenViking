---
type: simulink-block
title: 'XIO'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'xio'
documentation_source_path: 'ref/xio.html'
language: en
---

# XIO

## Ports

Not documented in R2025b.

## Parameters

### **Operand Tag** — Bit to be tested A (default) | boolean

Specify the data bits to be tested. Data bits are specified in the format of
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

Examine If Open

`XIO` is one of the building blocks of a ladder diagram. The
XIO block implements the `XIO` ladder logic instruction. The
block examines the operand tag (data bit) for an off condition. If the bit is clear, the rung
is enabled. If the bit is set, the rung is disabled.
