---
type: simulink-block
title: 'COP'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Memory and File Operations'
documentation_page: 'cop'
documentation_source_path: 'ref/cop.html'
language: en
---

# COP

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

Controls the execution of the block. **EnableIn** reflects the
rung state preceding the block. If the rung state preceding the block is false,
**EnableIn** is false, the block does not execute and the outputs
are not updated.

### **src** — Source scalar | vector | matrix

It gives the value stored at source. This data is copied into destination.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `single` | `String` | `Structure`

### **length** — Length of elements scalar

It gives the number or source elements to copy.

**Data Types:** `int8` | `int16` | `int32`
### Output

### **EnableOut** — Enable Output off (default) | on

By default, **EnableOut** follows the state of
**EnableIn**. If the **EnableIn** input to the
block is false, the logic implemented by the block is not executed and
**EnableOut** signal is set to false.

## Parameters

### **Source Initial Element Index** — Source Start Index 1 (default) | scalar

Source Start Index is used only when the source is an array. It specifies the index
of the first element to be copied into destination. If the source is not an array, then
the value of `Source Initial Element Index` is 1.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCSRCArrayIndex` |
| **Type**: scalar |
| **Value**: scalar |
| **Default**: `1` |

**Data Types:** `int8` | `int16` | `int32` | `single`

### **Destination Array Name** — Destination A (default) | boolean

The data copied from source is stored in destination. The destination is specified
in the format of `tags`. In Ladder Diagrams, tags (variables) are used
to represent inputs, outputs, and internal memory with attributes such as `Data
Type`, `Initial Value`, and `size`. To
change the attributes of the `Destination Array Name`, open the
**Program Variables** table within the Ladder Diagram
Program block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCOperandTag` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'A'` |

### **Destination Initial Element Index** — Destination Start Index scalar

Destination Start Index is used only when the source is an array. It specifies the
start index of destination where the data is copied. If the source and destination data
is not stored in an array, then the value of `Destination Initial Element
Index` is 1.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCDestArrayIndex` |
| **Type**: scalar |
| **Value**: scalar |
| **Default**: `0` |

**Data Types:** `int8` | `int16` | `int32` | `single`

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Copy File

The COP block implements the `COP` instruction. When the
rung conditions are true, the block is used to copy the data of the source and store it at the
destination, keeping the source unchanged.
