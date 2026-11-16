---
type: simulink-block
title: 'FIFO Read'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'fiforead'
documentation_source_path: 'io_ref/fiforead.html'
language: en
---

# FIFO Read

## Ports

### Input

### **F** — FIFO from which to read data serialfifoptr

Connects to the software FIFO containing data read from the serial
port.

### **MAX** — Maximum number of bytes to read from FIFO integer

The maximum number of bytes to return from the block.

#### Dependency

To make this port visible, set parameter **Max and Min
read size ports**.

### **MIN** — Minimum number of bytes to read from FIFO integer

The minimum number of bytes to return from the block.

#### Dependency

To make this port visible, set parameter **Max and Min
read size ports**.
### Output

### **D** — Parsed data read from FIFO vector

Vector containing the parsed data read from the FIFO.

#### Dependency

To determine the data type of this vector, set the parameter
**Output vector type**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **ENA** — Pass value of `MAX` through integer

Passes the value of port `MAX` through to the block
that reads the `ENA` port.

#### Dependency

To make this port visible, set parameters **Max and Min
read size ports** and **Enable
passthrough**.

## Parameters

### **Maximum read size** — Maximum number of characters returned by block `1024` (default) | integer

Specify the maximum number of characters for this block to return. The
resulting vector size is one more than this maximum number of characters.
This block indicates the number of characters being returned by using the
extra element as:

- A null terminator for the 8-bit data types
- The character count for the 16-bit and 32-bit data types

Enter a large enough number. If this number is too small, the block cannot
return anything. For example, if you enter the value `10`,
but on execution the FIFO contains `11` characters plus the
null terminator, the block does not return
any characters. If the FIFO contains
`5`, the block returns `5` characters
plus the null terminator.

If you select the parameter **Max and Min read size
ports**, the block interprets the value input on port
`MAX` as the maximum number of characters to return.
The actual maximum number of characters to return is the smaller of the
value on port `MAX` and the maximum read size in the block
parameters. Use this value in binary mode when you have not selected the
**Read to delimiter** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxsize` |

### **Minimum read size** — Minimum number of characters returned by block `1` (default) | integer

Enter the smallest read size in bytes. The FIFO must contain at least this
number of elements before elements are returned.

If you select the parameter **Max and Min read size
ports**, the value of port `MIN` supersedes
this value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `minsize` |

### **Read to delimiter** — Return delimited element sets `on` (default) | `off`

Select this check box to enable the return of element sets that terminate
with the **Delimiter** value. Use this parameter when
working with character-based elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `usedelimiter` |

### **Delimiter** — Terminator value for delimited element sets `13` (default) | `uint`

Enter the decimal value for an 8-bit input terminator. This parameter
specifies the value on which a FIFO read operation terminates. This value
works with the **Read to delimiter** parameter. By default,
this block looks for a carriage return. It returns characters only when one
is found. For reference, the decimal value of a carriage return is
`13` and a line feed is `10`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `delimiter` |

### **Output vector type** — Specify output data type `8 bit uint null terminated` (default) | `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

The 8-bit data types produce a NULL-terminated character vector in the output vector. For
16-bit and 32-bit data types, the first element contains the number of elements to expect
in the rest of the output vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outputtype` |

### **Max and Min read size ports** — Enable maximum and minimum input ports `off` (default) | `on`

When you select this check box:

- The value from input port `MAX` is the maximum
  number of characters to be removed from the FIFO. If this number
  exceeds the value of **Maximum read size**, the
  block disregards the value from the maximum input port. It takes the
  value of **Maximum read size** as the maximum
  number of characters to be removed from the FIFO.
- The value from the input port `MIN` is the
  minimum number of characters that the FIFO must contain before
  elements can be returned. This value supersedes the value set with
  the **Minimum read size** parameter.

This setting makes the input ports `MAX` and
`MIN` visible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `enable` |

### **Enable passthrough** — Enable passthrough of `MAX` value `off` (default) | `on`

Select this check box to pass the value of input port
`MAX` through to output port
`ENA`.

#### Dependency

Causes output port `ENA` to become visible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `enableout` |

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

Read simple data streams

The FIFO Read block is the read side of a FIFO read/write pair. You use
this block to parse simple data streams. The block functions in two modes that you set
by using the **Read to delimiter** check box.

- If you select the **Read to delimiter** check box, the block
  reads only elements if the specified delimiter has been written to the
  FIFO Write block. If the delimiter is found, the block
  returns elements up to and including the delimiter in the output vector. If the
  delimiter is not found, the block returns a zero-length vector, as determined by
  the data type. (If you have a zero-length vector, you can have your model
  perform a particular operation or ignore the case.)
- If you clear the **Read to delimiter** check box, the block
  returns elements between **Minimum read size** and the smaller
  of the number of elements currently in the FIFO and **Maximum read
  size**.

  When performing ASCII reads, select the **Read to delimiter**
  check box. When performing binary reads, clear this check box.

Here are some examples of how you can set up the FIFO Read block:

- **Transmit side of the interrupt service
  routine** — If the interrupt reason is not an empty hardware
  FIFO on the UART, the maximum input port receives a value of
  `0`. If the hardware FIFO is empty, it receives the size of
  the hardware FIFO. The minimum input port receives the constant value of
  `1`.
- **Receive side of the interrupt service routine**
  — The typical case with ASCII data has the minimum and maximum input
  ports disabled. The **Read to delimiter parameter** check box
  is selected and the **Delimiter** parameter has the value of
  carriage return or line feed. The value of the **Maximum read
  size** parameter is large (along the order of the FIFO size) and
  the value of **Minimum read size** parameter is 1. In this
  form, the driver acts like a nonblocking read line.

  An alternate receive-side configuration for fixed-length binary blocks of data
  has the value of the **Maximum read size** and
  **Minimum read size** parameters set to the fixed length of
  the block. The **Read to delimiter** parameter is not
  selected.

For complex data streams, consider using the FIFO Read HDRS and
FIFO Read Binary blocks. For guidelines on when to use these blocks,
see RS-232 FIFO Read Blocks.

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
