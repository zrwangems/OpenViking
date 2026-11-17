---
type: simulink-block
title: 'FIFO Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'fifowrite'
documentation_source_path: 'io_ref/fifowrite.html'
language: en
---

# FIFO Write

## Ports
```yaml
ports:
- name: D
  summary: Data to write to FIFO vector
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
- name: F
  summary: FIFO vector serialfifoptr
  direction: output
- name: DP
  summary: True if new data is present in the FIFO true | false
  direction: output
```

### Input

### **D** — Data to write to FIFO vector

Vector containing the data to write to the FIFO.

#### Dependency

To determine the data type of this vector, set the parameter
**Input vector type**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### Output

### **F** — FIFO vector serialfifoptr

Connects to the FIFO that writes data to the serial port.

### **DP** — `True` if new data is present in the FIFO `true` | `false`

If data is present in the FIFO, returns
`true`.

#### Dependency

To make this port visible, set parameters **Max and Min
read size ports** and **Enable
passthrough**.
## Parameters
```yaml
parameters:
- name: Size
  summary: Size of FIFO, in bytes 1024 (default) | integer
  group: ''
  block_parameter: size
- name: Input vector type
  summary: Specify input data type 8 bit uint null terminated (default) | count+32 bit int | count+32 bit uint | count+16
    bit int | count+16 bit uint | 8 bit int null terminated
  group: ''
  block_parameter: inputtype
- name: Data present output
  summary: Enables output DP off (default) | on
  group: ''
  block_parameter: present
- name: Sample time
  summary: Sample time of block -1 (default) | numeric
  group: ''
- name: ID
  summary: Identifier for overflow messages character vector
  group: ''
  block_parameter: id
```

### **Size** — Size of FIFO, in bytes `1024` (default) | integer

Enter the number of elements that can be held in the FIFO at one time. If
a write operation to the FIFO causes the number of elements to exceed
**Size**, an error occurs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `size` |

### **Input vector type** — Specify input data type `8 bit uint null terminated` (default) | `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

For the 16-bit and 32-bit data types, include as first element the number
of elements to expect in the rest of the input vector. The count controls
how many bytes that the block copies into the FIFO. The block does not copy
the count itself into the FIFO.

For the 8-bit data types, provide a NULL-terminated character vector in
the output vector. The block copies data into the FIFO up to, but not
including, the NULL terminator.

For more information, see RS-232 Legacy Drivers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inputtype` |

### **Data present output** — Enables output `DP` `off` (default) | `on`

Select this check box to create the Boolean output `DP`.
If data is present in the FIFO, `DP` becomes
`true`. The transmit side of the send/receive subsystem
uses this output. This output is given to the Enable TX block, which enables
the transmitter buffer empty interrupt.

This setting makes the output port `DP` visible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `present` |

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time. `-1` means
that sample time is inherited.

#### Programmatic Use

```
sampletime
```

### **ID** — Identifier for overflow messages character vector

Enter a user-defined identifier for FIFO overflow messages.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `id` |
## Libraries

Simulink Real-Time / RS232

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Write simple data streams

The FIFO Write block is the write side of a FIFO read/write pair. Use
this block to generate simple data streams.

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
