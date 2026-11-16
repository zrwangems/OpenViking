---
type: simulink-block
title: 'Byte Unpacking'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Utilities'
documentation_page: 'byteunpacking'
documentation_source_path: 'io_ref/byteunpacking.html'
language: en
---

# Byte Unpacking

## Ports

### Input

### **Port\_1** — Input port containing packed data vector

The block displays one input port that receives a vector of packed
data. The source of the packed data determines by inheritance the data
type of the packed data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### Output

### **Port\_1** — First of *N* output ports scalar | vector

The block displays from `1` to *N*
output ports, as specified by elements of the cell array in the
parameter **Output port (unpacked) data types (cell
array)**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## Parameters

### **Output port (unpacked) data types (cell array)** — Data types for the unpacked output signals `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify as a cell array the data types of the output ports (unpacked) for
the different output signals. The number of elements in the cell array
determines the number of output ports shown by this block instance. To
represent vector elements, use square brackets in the cell array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaskUnpackedDataTypes` |

### **Output port (unpacked) dimensions (cell array)** — Dimensions of each output port (unpacked) `{[1]}` (default) | `{[N], [M], ...}`

Specify the dimensions of the output ports as a cell array of
vectors.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaskUnpackedDataSizes` |

### **Byte Alignment** — Alignment of the output signal data types before unpacking `1` (default) | `2` | `4` | `8`

Each element in the output signals list starts at a multiple of the
alignment value, specified from the start of the input vector. If the
alignment value is larger than the size of the data type in bytes, the
vector contains pad bytes of value `0`.

For example, if the alignment value is `4`:

- `uint32` receives
  no padding
- `uint16` receives `2` bytes of
  padding
- `uint8` receives `3` bytes of
  padding

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

The Byte Unpacking block supports C++ code generation only.

## Version History

**Introduced in R2006a**

## Description

Deconstruct data frames

The Byte Unpacking block converts a vector of varying data types into
one or more signals of user-selectable data types. The input of this block typically
connects to an output port of a Receive block.

The Byte Packing block and the Byte Unpacking block support
Simulink®
Real-Time™ STF code generation targets and generate code that runs on Speedgoat
target machines. Due to considerations such as endianness and addressable word size,
these blocks can generate incorrect results for other code generation targets or target
computers.

For example, suppose that you are unpacking a `uint8` vector signal
into three signals. The signals have these attributes:

| Dimension | Size | Type |
| --- | --- | --- |
| Scalar | `1` | `single` |
| Vector | `3` | `uint8` |
| Vector | `3` | `uint8` |

1. Set the output port data type to:

   ```
   {'single', ['uint8'], ['uint8']}
   ```

   Use square brackets to represent vectors.
2. Set the output port dimension to:

   ```
   {[1],[3],[3]}
   ```
3. Set the alignment value to `1`.
4. Connect the output signals to the Byte Unpacking block.
