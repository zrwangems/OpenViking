---
type: simulink-block
title: 'FIFO Read HDRS'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'fiforeadhdrs'
documentation_source_path: 'io_ref/fiforeadhdrs.html'
language: en
---

# FIFO Read HDRS

## Ports

### Input

### **F** — FIFO from which to read data serialfifoptr

Connects to the software FIFO containing data read from the serial port.

### **E** — Enable read from FIFO `true` | `false`

If `true`, read from FIFO.

#### Dependency

To make this port visible, set parameter **Enable input**.
### Output

### **1** — Numbered output streams, one per header vector

Vectors containing the parsed data read from the FIFO. Each output corresponds to one of the headers.

#### Dependency

To determine the data type of this vector, set the parameter **Output vector type**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## Parameters

### **Header** — Search targets in ASCII data stream cell array of character vector

Enter the headers that you want the block to look for in a block of data
from the FIFO. Enter each header in single quotes as an element in a cell
array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `hdr` |

### **Terminating string** — Characters that end data stream `[13 10]` (default) | [integer]

Enter the terminating character vector for the data. Enter the characters
defining the end of character vector, typically one or two
characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nterm` |

### **Output behavior** — Behavior when no new data `Zero output if no new data` (default) | `Hold last output if no new data`

From the list, select the behavior of the block if the FIFO has not received new data:

- `Hold last output if no new
  data` — Block keeps the output from the last FIFO
  message.
- `Zero output if no new data` —
  Block overwrites the first element of the output with
  `0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `hold` |

### **Enable input** — Enable read from FIFO `off` (default) | `on`

To create an input port that enables or disables the read operation, select this check box.
The input port takes a Boolean signal.

#### Dependency

Causes input port `E` to become visible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `enable` |

### **Maximum read size** — Maximum number of characters returned by block `1024` (default) | integer

Specify the maximum number of characters for this block to return. The resulting vector size
is one more than this maximum number of characters. This block indicates the number of
characters being returned by using the extra element as:

- A NULL terminator for the 8-bit data types
- The character count for the 16-bit and 32-bit data types

Enter a large enough number. If this number is too small, the block cannot return anything.
For example, if you enter the value `10`, but on execution the FIFO
contains `11` characters plus the null terminator, the block does not
return any characters. If it contains
`5`, the block returns `5` characters plus the NULL
terminator.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxsize` |

### **Output vector type** — Specify output data type `8 bit uint null terminated` (default) | `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

The 8-bit data types produce a NULL-terminated character vector in the output vector. For
16-bit and 32-bit data types, the first element contains the number of elements to expect
in the rest of the output vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outputtype` |

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time. `-1` means
that sample time is inherited.

#### Programmatic Use

```
sampletime
```

## Libraries

Simulink Real-Time / RS232

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Read multiple ASCII data streams according to header information

The FIFO Read HDRS block identifies and separates ASCII data streams
that have embedded identifiers.

The data following a particular header can have varying lengths, but has a common
termination marker such as `<CR><LF>`. Although you can
attain this same functionality with the FIFO Read block, it requires a
complicated state machine with this behavior:

- If the same header arrives in the FIFO more than once after the block was
  last executed, the block returns the latest instance of the header. The
  block catches up with data that arrives faster than the block
  executes.
- If a header arrives in the FIFO that does not match an item in the headers
  list, the block discards the message.
- If bytes arrive in the FIFO that do not match a header, the block
  interprets the message as having an unspecified header. The block skips
  these bytes.

Example models `slrt_ex_serialbaseboardasciitest` and
`slrt_ex_serialbaseboardasciisplit` show how to use the FIFO
Read HDRS block. To find and open these models, in the MATLAB® Command Window, type:

```
modelfinder('slrealtime')
```

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
