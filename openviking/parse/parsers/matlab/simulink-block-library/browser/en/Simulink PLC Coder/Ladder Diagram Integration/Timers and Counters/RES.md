---
type: simulink-block
title: 'RES'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'res'
documentation_source_path: 'ref/res.html'
language: en
---

# RES

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

## Parameters

### **Operand Tag To Reset** — Structure to Reset A (default) | character vector

Specify the `tag` to reset. In Ladder Diagrams, tags (variables)
are used to represent inputs, outputs, and internal memory with attributes such as
`Data Type`, `Initial Value`, and
`size`. To change the attributes of the `Operand Tag To
Reset`, open the **Program Variables** table within the
Ladder Diagram Program block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCTagToReset` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'A'` |

### **Tag Structure** — Structure Type 'TIMER or COUNTER' (default) | 'CONTROL'

Specify the structure type to reset.

| Type | Description |
| --- | --- |
| `TIMER or COUNTER` | Clears the `ACC` field of the structure. |
| `CONTROL` | Clears the `POS` field of the structure. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCTagDataType` |
| **Type**: character vector |
| **Value**: 'TIMER or COUNTER'|'CONTROL' |
| **Default**: 'TIMER or COUNTER' |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Reset

The RES block implements the `RES` ladder logic
instruction. When the rung conditions are true, the block resets the value of
`TIMER`, `COUNTER`, or a `CONTROL`
structure.
