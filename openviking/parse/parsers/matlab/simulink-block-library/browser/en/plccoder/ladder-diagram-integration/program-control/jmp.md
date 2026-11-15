---
type: simulink-block
title: 'JMP'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'jmp'
documentation_source_path: 'ref/jmp.html'
language: en
---

# JMP

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

### **Jump to Label** — Name of the label L (default) | character vector

Specify the name for associated `LBL` instruction.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCLabelTag` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'L'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Jump

The JMP block implements the `JMP` ladder logic
instruction. When the rung conditions are true, the block skips a part of ladder logic and the
rung execution moves to the block referenced by the label block. Jump block can only skip the
rungs after it. The block does not support a backward jump.
