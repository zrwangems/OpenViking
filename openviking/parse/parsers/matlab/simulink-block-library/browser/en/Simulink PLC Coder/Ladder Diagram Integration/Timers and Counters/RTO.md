---
type: simulink-block
title: 'RTO'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'rto'
documentation_source_path: 'ref/rto.html'
language: en
---

# RTO

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

### **Timer Tag** — Timer Structure T (default) | character vector

Specify the timer parameters in the format of `tags`. In Ladder
Diagrams, tags (variables) are used to represent inputs, outputs, and internal memory
with attributes such as `Data Type`, `Initial Value`,
and `size`. To change the attributes of the `Operand
Tag`, open the **Program Variables** table within the
Ladder Diagram Program block. The `Data Type` of the
timer tag is of the `Bus:TIMER` type with its initial value specified
as a structure containing the following fields:

| Field | Description | Default Value |
| --- | --- | --- |
| `PRE` | The preset value specifies the value (1 millisecond units) which the accumulated value must reach before the instruction indicates it is done | 0 |
| `ACC` | The accumulated value specifies the number of milliseconds that have elapsed since the `RTO` instruction was enabled. | 0 |
| `EN` | The enable bit contains rung-condition-in when the instruction was last executed. | 0 |
| `TT` | The timing bit when set indicates the timing operation is in process. | 0 |
| `DN` | The done bit when set indicates the timing operation is complete (or paused). | 0 |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCOperandTag` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'T'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Retentive Timer On

The RTO block implements the `RTO` ladder logic
instruction. When the rung conditions are true, the block accumulates time until:

- The timer is disabled
- The timer completes
