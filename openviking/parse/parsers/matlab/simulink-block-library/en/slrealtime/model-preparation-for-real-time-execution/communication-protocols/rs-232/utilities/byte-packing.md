---
type: simulink-block
title: 'Byte Packing'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Utilities'
documentation_page: 'bytepacking'
documentation_source_path: 'io_ref/bytepacking.html'
language: en
---

# Byte Packing

## Ports

### Input

### **Port\_1** — First of *N* input ports scalar | vector

The block has from `1` to *N* input
ports. Specify the number of input ports and their types by entering
them as a cell array in the parameter **Input port (unpacked)
data types (cell array)**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### Output

### **Port\_1** — Output port containing packed data vector

The block displays one output port that transmits a vector of packed
data. You determine the data type of the packed data by setting
**Output port (packed) data type**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## Parameters

### **Output port (packed) data type** — Data type for the packed output signal `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

From the list, select a data type for the output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaskPackedDataType` |

### **Input port (unpacked) data types (cell array)** — Data types for the unpacked input signals `{'uint8'}` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify as a cell array the data types of the input ports (unpacked) for
the different input signals. The number of elements in the cell array
determines the number of input ports shown by this block instance. To
represent vector elements, use square brackets in the cell array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaskUnpackedDataTypes` |

### **Byte Alignment** — Alignment of the input signal data types after packing `1` (default) | `2` | `4` | `8`

Each element in the input signals list starts at a multiple of the
alignment value, specified from the start of the vector. If the alignment
value is larger than the size of the data type in bytes, the block fills the
space with pad bytes of value `0`.

For example, if the alignment value is `4`:

- `uint32` receives
  no padding
- `uint16` receives `2` bytes of
  padding
- `uint8` receives `3` bytes of
  padding

If the model accesses the data items frequently, consider selecting an
alignment value equal to the largest data type that you want to access. If
the model transfers data items frequently as a group, consider an alignment
value of `1`, which packs the data into as small a
space as possible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaskAlignment` |

## Libraries

Simulink Real-Time / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Byte Packing block supports C++ code generation only.

## Version History

**Introduced in R2006a**

## Description

Construct data frames

The Byte Packing block converts one or more signals of user-selectable
data types to a single vector of varying data types. The output of this block typically
connects to an input port of a Send block.

The Byte Packing block and the Byte Unpacking block support the
Simulink®
Real-Time™ STF code generation targets and generate code that runs on Speedgoat
target machines. Due to considerations such as endianness and addressable word size,
these blocks can generate incorrect results for other code generation targets or target
computers.

For example, suppose that you are packing three signals into a vector of
`uint8`. The signals have the following attributes:

| Dimension | Size | Type |
| --- | --- | --- |
| Scalar | `1` | `single` |
| Vector | `3` | `uint8` |
| Vector | `3` | `uint8` |

1. Set the packed output port data type to `uint8`.
2. Set the input port data type to a cell array encoding the data types:

   ```
   {'single', ['uint8'], ['uint8']}
   ```

   Use square brackets to represent vectors.
3. Set the byte alignment value to `1`.
4. Connect the signals to the Byte Packing block.
