---
type: simulink-block
title: 'Host Serial Transmit'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'hostserialtransmit'
documentation_source_path: 'ref/hostserialtransmit.html'
language: en
---

# Host Serial Transmit

## Ports
```yaml
ports:
- name: data
  summary: Port to receive data to be transmitted scalar
  direction: input
  data_types: single | int8 | uint8 | int16 | uint16 | int32 | uint32
```

### Input

### **data** — Port to receive data to be transmitted scalar

This port accepts both one-dimensional and matrix data for transmission to the
target hardware.

**Data Types:** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
## Parameters
```yaml
parameters:
- name: Serial Connection
  summary: Serial port used for transmitting data Serial 1 (default) | Serial 2 | Serial 3 | Serial 4
  group: ''
- name: Additional package header
  summary: Package header data 'S' (default) | scalar
  group: ''
- name: Additional package terminator
  summary: Package terminator data 'E' (default) | scalar
  group: ''
- name: Enable blocking mode
  summary: Block simulation while sending data off (default) | on
  group: ''
```

### **Serial Connection** — Serial port used for transmitting data `Serial 1` (default) | `Serial 2` | `Serial 3` | `Serial 4`

Specify a serial port to transmit to the target hardware. Select an available serial
port from the list. You can configure the selected port using the Host Serial
Setup block. If you do not configure a serial port, the block prompts you to
do so. Each Host Serial Transmit block must have a configured serial
port. If you use multiple ports in your simulation, you must configure each port
separately.

### **Additional package header** — Package header data `'S'` (default) | scalar

Specifies the data located at the front of the transmitted data package, which is
not part of the data being transmitted, and generally indicates start of data. The
additional package header must be an ASCII value. You can use a text value or a numeric
value in the range (0–255). You must put single quotes around the text that you enter in
this field, but the quotes are not transmitted and they are not included in the total
byte count.

### **Additional package terminator** — Package terminator data `'E'` (default) | scalar

Specifies the data located at the end of the transmitted data package, which is not
part of the data being transmitted, and generally indicates end of data. The additional
package terminator must be an ASCII value. You can use a text value or a numeric value
in the range (0–255). You must put single quotes around text entered in this field, but
the quotes are not transmitted and they are not included in the total byte count.

### **Enable blocking mode** — Block simulation while sending data `off` (default) | `on`

Select this parameter to block the simulation while transmitting data. Clear this
parameter if you do not want the write operation to block the simulation.
## Libraries

Motor Control Blockset / Protection and Diagnostics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Configure host-side serial communications interface to transmit data to serial port

The Host Serial Transmit block specifies the configuration of the data that
it transmits to the target hardware.

The data package that the block sends is limited to 16 bytes of ASCII characters,
including package headers and terminators. Calculate the size of a package by including the
package header, or terminator, or both, and the data size. This table shows the number of
bytes in each data type.

| Data Type | Byte Count |
| --- | --- |
| `single` | 4 bytes |
| `int8` and `uint8` | 1 byte |
| `int16` and `uint16` | 2 bytes |
| `int32` and `uint32` | 4 bytes |

For example, if your data package has a package header 'S' (1 byte) and package terminator
'E' (1 byte), that leaves 14 bytes for the actual data. If your data is of type
`int8`, there is space in the data package for 14
`int8`s. If your data is of type `uint16`, there is
space in the data package for 7 `uint16`s. If your data is of type
`int32`, there is space in the data package for only 3
`int32`s, with 2 bytes left over. Even though you could fit two
`int8`s or one `uint16` in the remaining space, you
should not, because you cannot mix data types in the same package.

The number of data types that can fit into a data package determine the data size. In the
preceding example, the data size is 14 for `int8` and 7 for
`uint16`. When the data size exceeds 16 bytes, unexpected behavior,
including run-time errors, are likely to occur.
