---
type: simulink-block
title: 'Ladder Diagram Subroutine'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Organizational Units'
documentation_page: 'subroutine'
documentation_source_path: 'ref/subroutine.html'
language: en
---

# Ladder Diagram Subroutine

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.
### Output

### **EnableOut** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

## Parameters

### **Routine Name** — Name of the routine R (default) | character vector

Specify the name of the ladder logic subroutine.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCPOUName` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'R'` |

### **Routine Logic** — Open ladder logic boolean

Button that opens the ladder logic subroutine.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCOpenRoutine` |
| **Type**: button |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Ladder Diagram Subroutine

Ladder Diagram Subroutine allows you to create and define a named ladder
logic routine. You can edit the logic implemented by the subroutine by clicking on the
`Routine Logic` button found under the block parameters menu of this
block.
