---
type: simulink-block
title: 'CTU'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'ctu'
documentation_source_path: 'ref/ctu.html'
language: en
---

# CTU

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.
### Output

### **CU** — Count Up Enable Output off (default) | on

The count up enable output contains the rung-in condition when the instruction was
last executed. By default, **CU** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**CU** signal is set to false.

## Parameters

### **Counter Tag** — Counter Structure C (default) | character vector

Specify the counter parameters in the format of `tags`. In Ladder
Diagrams, tags (variables) are used to represent inputs, outputs, and internal memory
with attributes such as `Data Type`, `Initial Value`,
and `size`. To change the attributes of the `Operand
Tag`, open the **Program Variables** table within the
Ladder Diagram Program block. The `Data Type` of the
timer tag is of the `Bus:COUNTER` type with its initial value specified
as a structure containing the following fields:

| Field | Description | Default Value |
| --- | --- | --- |
| `PRE` | The preset value specifies the value which the accumulated value must reach before the instruction indicates it is done | 0 |
| `ACC` | The accumulated value specifies the number of transitions the instruction has counted. | 0 |
| `CU` | The count up enable contains `rung-condition-in` when the instruction was last executed. | 1 |
| `CD` | Count down enabled. | 1 |
| `DN` | The done bit when set indicates the counting operation is complete | 0 |
| `OV` | The overflow bit when set indicates the counter incremented past the upper limit of 2,147,483,647 | 0 |
| `UN` | The underflow when set indicates the counter decremented past the lower limit of -2,147,483,648. | 0 |

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

Count Up

The CTU block implements the `CTU` ladder logic
instruction. When the rung conditions are true, the block counts upwards.
