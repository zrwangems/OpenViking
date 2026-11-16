---
type: simulink-block
title: 'Variable Write'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Input/Output'
documentation_page: 'variablewrite'
documentation_source_path: 'ref/variablewrite.html'
language: en
---

# Variable Write

## Ports

Not documented in R2025b.

## Parameters

### **Data Tag** — Data to be written A (default) | boolean

Specify the data bits to be written, specified in the format of
`tags`. In Ladder Diagrams, tags (variables) are used to represent
inputs, outputs, and internal memory with attributes such as `Data
Type`, `Initial Value`, and `size`. To
change the attributes of the `Data Tag`, open the **Program
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

Variable Write

The block is used as an output variable assignment.
