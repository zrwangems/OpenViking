---
type: simulink-block
title: 'Byte Unpack'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Utilities'
documentation_page: 'byteunpack'
documentation_source_path: 'nucleo/ref/byteunpack.html'
language: en
---

# Byte Unpack

## Ports

### Input

### **Port\_1** — Packed data scalar | vector | matrix

Receives a vector of packed data.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — First of *N* output ports scalar | vector | matrix

The block can have from `1` to *N* output
ports, as specified by elements of the cell array in the parameter **Output
port data types (cell array)**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Output port dimensions (cell array)** — Dimensions of each output port (unpacked) `{[1]}` (default) | `{[N], [M], ...}`

Output port dimensions specified as a cell array of vectors.

Specify the same dimensions that you set for the corresponding Byte Pack block in the model.

### **Output port data types (cell array)** — Data types for unpacked output signals `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Data types of the output ports (unpacked) specified for different output
signals as a cell array. The number of elements in the cell array determines
the number of output ports shown by this block instance.

Specify the same data types that you set in the **Input port data types (cell array)** parameter for the
corresponding Byte Pack block in the model.

### **Byte alignment** — Alignment of output signal data types before unpacking `1` (default) | `2` | `4` | `8`

Each element in the input signals list starts at a multiple of the byte
alignment value, specified from the start of the vector. If the byte
alignment value is larger than the size of the data type in bytes, the
output values are padded with zeros to fill the space allotted.

For example, if the byte alignment value is 4, a `uint32`
receives no padding, a `uint16` receives 2 bytes of
padding, and a `uint8` receives 3 bytes of padding.

Choose the same byte alignment value that you set in the **Byte alignment** parameter for the corresponding
Byte Pack block in the model.

### Example

Suppose that you are unpacking a vector of data type `uint8` or
`uint16`, and the unpacked signals have these
attributes.

| Dimension | Size | Type |
| --- | --- | --- |
| Vector | `3` | `int8` |
| Vector | `2` | `int16` |
| Scalar | `1` | `uint8` |
| Scalar | `1` | `uint32` |

To unpack the signals:

1. Set **Output port dimensions (cell array)**
   to:

   ```
   {'3’, ‘2’, ‘1’, ‘1’}
   ```
2. Set **Output port data types (cell array)**
   to:

   ```
   {'int8’, ‘int16’, ‘uint8’, ‘uint32’}
   ```

   The block creates four output ports that match the order of the signal
   data types specified in the cell array.
3. Set the required byte alignment value. The byte alignment value specifies
   the number of bytes after which a new byte starts from the previous
   boundary.

   The size of the output is based on the packed vector size, the byte
   alignment value, and the smallest memory cell size of the processor.
   Depending on the byte alignment value, output values padded with zeros are
   discarded before the next signal is unpacked. The smallest addressable
   memory cell indicates the number of bits occupied by `char`
   or `uint8` data type for a processor, and determines the
   structure of packets.
4. Connect incoming signals to the input port of the Byte
   Unpack block.

For processors with a smallest addressable memory cell of 8 bits per char,
consider the packed input vector data type `uint8`.

Red zeros represent padded empty memory cells.

For a packed input vector of data type `uint8` and byte alignment
value 2, the `int8` data value (23 04 FD) occupies three memory
cells, with each cell occupying 8 bits. The next input signal of
`int16` data value (00DA FFF4) occupies the next four cells
(fifth through eighth), and the fourth cell is empty (padded). The Byte
Unpack block considers the alignment and padding of cells while
unpacking.

The packed input vector of data type `uint16` is:

The unpacked output signals are:

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

For processors such as Texas Instruments®
C2000™, with a smallest addressable memory cell of 16 bits per char, consider
a packed input vector data type `uint8`. The output packet occupies
16 bits although the data value that the packet represents is 8 bits. The byte
alignment values are calculated with respect to the 16-bit addressable
memory.

For a packed input vector of data type `uint8` and byte alignment
value 2, the `int8` data value (0023 0004 00FD) occupies three
memory cells, with each cell occupying 16 bits. The next signal of data type
`int16` (00DA 0000 00F4 00FF) occupies the next four cells
(fifth through eighth), and the fourth cell is empty (padded). The Byte
Unpack block considers the alignment and padding of cells while
unpacking.

For the packed input vector of data type `uint16`, the output
packet occupies 16 bits, and the data value the packet represents is also 16 bits.
For a packet size of 16 and larger, the byte alignment is calculated with respect to
the number of bytes the data values have to be packed. Therefore, in this case,
1-byte alignment is not allowed.

For a packed input of data type `uint16` and byte alignment value
2, the three `int8` data values (0423 FD) occupy the first two
memory cells. The fourth byte in the second memory cell is empty and padded with
zero. The `int16` data value (00DA FFF4) occupies the next two
memory cells (third and fourth). The Byte Unpack block considers the
alignment and padding of cells while unpacking.

The table lists the unpacked output signals. The `int8` and
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

## Libraries

Simulink Support Package for Arduino Hardware / Utilities Embedded Coder / Embedded Targets / Host Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Utilities Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities SoC Blockset Support Package for Infineon AURIX Microcontrollers / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Unpack 8-, 16-, or 32-bit input vector to multiple output vectors

The Byte Unpack block converts a vector of `uint8`,
`uint16`, or `uint32` data type to one or more
signals of user-selectable data types. This block is the inverse of the Byte Pack block. The input of this block connects to an output port of a
receive block, such as SPI Receive, SCI Receive, or
UDP Receive. The Receive block then transmits signals
across various communication networks, such as SPI, SCI, UDP, or I2C.
