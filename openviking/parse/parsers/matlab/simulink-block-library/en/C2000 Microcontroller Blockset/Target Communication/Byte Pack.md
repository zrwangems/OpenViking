---
type: simulink-block
title: 'Byte Pack'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Target Communication'
documentation_page: 'bytepack'
documentation_source_path: 'ref/bytepack.html'
language: en
---

# Byte Pack

## Ports

### Input

### **Port\_1** — First of *N* input ports scalar | vector | matrix

The number of input ports and their types specified as a cell array in
the **Input port data types (cell array)** parameter.
The block can have from `1` to *N*
input ports. *N* is the number of incoming data types
specified in the cell array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — Vector containing packed data vector

Transmits a vector of packed data.

**Data Types:** `uint8` | `uint16` | `uint32`

## Parameters

### **Output port (packed) data type** — Data type of packed output signal `uint8` (default) | `uint16` | `uint32`

The data type of the packed output signal at the output port.

### **Input port data types (cell array)** — Data types of unpacked input signals `{'double'}` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Data types of input signals (unpacked), specified as a cell array. The
block creates input ports in the order of the incoming data types specified
in the cell array. For example, the first data type in the cell array
corresponds to the top port and the last data type corresponds to the bottom
port.

For example, if the data types are `single`,
`uint8`, and `uint8`, the block
creates three input ports. The order of the input port data types is same as
the data types specified in the cell array.

### **Byte alignment** — Alignment of input signal data types after packing `1` (default) | `2` | `4` | `8`

Each element in the input signal list starts at a multiple of the byte
alignment value, specified from the start of the vector. If the byte
alignment value is larger than the size of the data type in bytes, the input
values are padded with zeros to fill the space allotted.

For example, if the byte alignment value is 4, a `uint32`
receives no padding, a `uint16` receives 2 bytes of
padding, and a `uint8` receives 3 bytes of padding.

**Tip**

If the model accesses the data items frequently, consider selecting a
byte alignment value equal to the largest data type that you want to
access. If the model transfers the data items frequently as a group,
consider selecting a byte alignment value of
`1`, which packs the data into the smallest
space possible.

### Example

Suppose that you are packing four signals into a vector of data type
`uint8` or `uint16`, and the signals have
these attributes.

| Dimension | Size | Type |
| --- | --- | --- |
| Vector | `3` | `int8` |
| Vector | `2` | `int16` |
| Scalar | `1` | `uint8` |
| Scalar | `1` | `uint32` |

To pack the signals:

1. Set **Output port (packed) data type**. This
   example compares `uint8` and
   `uint16`.
2. Set **Input port data types (cell array)**
   to:

   ```
   {'int8’, ‘int16’, ‘uint8’, ‘uint32’}
   ```

   The block creates four input ports that match the order of the incoming
   signal data types specified in the cell array.
3. Set the required byte alignment value. The byte alignment value specifies
   the number of bytes after which a new byte starts from the previous
   boundary.

   The size of the output is based on the packed vector size, the byte
   alignment value, and the smallest memory cell size of the processor.
   Depending on the byte alignment value, input values are padded with zeros
   before the next signal is packed. The smallest addressable memory cell
   indicates the number of bits occupied by the `char` or
   `uint8` data type for a processor and determines the
   structure of packets.
4. Connect incoming signals to the input port of the Byte Pack
   block.

For processors with a smallest addressable memory cell of 8 bits per char,
consider these values for input signals.

| **Unpacked Signals** | | | | |
| --- | --- | --- | --- | --- |
| **Dimension** | **Size** | **Data Type** | **Dec Value** | **Hex Value** |
| Vector | 3 | `int8` | 35 | 23 |
| 4 | 04 |
| –3 | FD |
| Vector | 2 | `int16` | 218 | 00DA |
| –12 | FFF4 |
| Scalar | 1 | `uint8` | 112 | 70 |
| Scalar | 1 | `uint32` | 5000 | 00001388 |

The packed output vector data type `uint8` is:

Red zeros represent padded empty memory cells.

For a packed output vector of data type `uint8` and byte
alignment value 2, the `int8` data value (23 04 FD) occupies the
first three memory cells, with each cell occupying 8 bits. Because three is not a
multiple of the byte alignment value 2, the next input signal of
`int16` data value (00DA FFF4) is allocated the next four cells
(fifth through eighth), leaving the fourth cell empty. The block fills the empty
cell with zero. The rest of the input signals are packed in a similar way.

After packing all input signals, the Byte Pack block calculates the
total packets allocated and outputs a `uint8` vector of size 4 + 4
+ 2 + 4 = 14. Here, the `int8` signal occupies the first 4 cells,
the `int16` signal occupies the second 4 cells, the
`uint16` signal occupies the third 2 cells, and the
`uint32` signal occupies the fourth 4 cells.

The packed output vector of data type `uint16` is:

For processors such as Texas Instruments®
C2000™, with the smallest addressable memory cell of 16 bits per char,
consider these values for input signals. The `int8` and
`uint8` data values occupy 16 bits, as indicated by the hex value.

| **Unpacked Signals** | | | | |
| --- | --- | --- | --- | --- |
| **Dimension** | **Size** | **Data Type** | **Dec Value** | **Hex Value** |
| Vector | 3 | `int8` | 35 | 0023 |
| 4 | 0004 |
| –3 | FFFD |
| Vector | 2 | `int16` | 218 | 00DA |
| –12 | FFF4 |
| Scalar | 1 | `uint8` | 112 | 0070 |
| Scalar | 1 | `uint32` | 5000 | 00001388 |

For the packed output vector of data type `uint8`, the output
packet occupies 16 bits, although the data value the packet represents is 8 bits.
The byte alignment values are calculated with respect to the16-bit addressable
memory.

For a packed output vector of data type `uint8` and byte
alignment value 2, the `int8` data value (0023 0004 00FD) occupies
the first three memory cells, with each cell occupying 16 bits. Because three is not
a multiple of byte alignment value 2, the next signal of data type
`int16` (00DA 0000 00F4 00FF) is allocated the next four cells
(fifth through eighth), leaving the fourth cell empty. The block fills the empty
cell with zero. The rest of the input signals are packed in a similar way. After
packing all input signals, the Byte Pack block calculates total
packets allocated and outputs a `uint8` vector of size 4 + 4 + 2 +
4 = 14.

For the packed output vector of data type `uint16`, the output
packet occupies 16 bits, and the data value the packet represents is also 16 bits.
For a packet size of 16 and larger, the byte alignment is calculated with respect to
the number of bytes the data values are packed into. Therefore, in this case, 1-byte
alignment is not allowed.

For a packed output of data type `uint16` and byte alignment
value 2, the three `int8` data values (0423 FD) are packed together
as two words in the first two memory cells. The fourth byte in the second memory
cell is empty and filled with zero. The `int16` data value (00DA
FFF4) is allocated the next two memory cells (third and fourth). The rest of the
input signals are packed in a similar way. After packing all signals, the
Byte Pack block calculates total packets allocated and outputs a
`uint16` vector of size 2 + 2 + 1 + 2 = 7.

## Libraries

C2000 Microcontroller Blockset / Target Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Convert input signals to 8-, 16-, or 32-bit vector

The Byte Pack block converts one or more signals of user-selectable
data types to a single `uint8`, `uint16`, or
`uint32` vector output. Using the parameters of this block, you
specify the input data types and the alignment of the data in the output vector. The
output of this block connects to an input port of a send block, such as SPI
Transmit, SCI Transmit, or UDP Send. The send
block then transmits signals across various communication networks, such as SPI, SCI,
UDP, or I2C.

**Note**

The Byte pack block requires the input signal dimensions to be calculated
accurately so that the block can set the output port signal dimensions
appropriately. In certain modeling scenarios, you may have to manually specify
the dimensions if Simulink cannot calculate the dimensions accurately. For example,

- When you are providing an input port directly to the Byte Pack
  block, you need the dimensions accurately for the input port.
- When the input to the Byte Pack is coming through a feedback loop
  involving a delay block then the dimensions will not be
  automatically calculated by Simulink. In this scenario, you can use
  signal specification block with the correct dimension before the
  signal is passed as input to the Byte Pack.
