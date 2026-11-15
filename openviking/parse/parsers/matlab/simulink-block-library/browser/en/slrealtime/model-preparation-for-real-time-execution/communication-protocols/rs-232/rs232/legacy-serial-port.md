---
type: simulink-block
title: 'Legacy Serial Port'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'legacyserialport'
documentation_source_path: 'io_ref/legacyserialport.html'
language: en
---

# Legacy Serial Port

## Ports

### Input

### **XMT** — Vector of data to transmit vector

Vector of the data used to transmit over the port.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **RCV** — Vector of data received over serial port vector

Vector containing data that has been received from serial port.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Serial port** — Port that is being accessed `Legacy Serial Port 1` (default) | .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

Specify the serial port for communications.

If using USB-to-serial adapters, the target computer
detects these adapters as `serusb1`, `serusb2`, and so
on in the order that the adapters are connected to the serial devices.

The order of port assignment is retained through the power cycle of the target
computer or serial device if there is no change in the connections to the ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `port` |

### **Baud rate** — Baud for transferring data `115200` (default) | `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

Select a baud for transmitting and receiving data through the modem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `baud` |

### **Data bits** — Number of bits per character `8` (default) | `7` | `6` | `5`

Select the number of bits that encode a character.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `width` |

### **Stop bits** — Number of stop bits for port `1` (default) | `2`

Select the number of stop bits for the character stream.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nstop` |

### **Parity** — Parity for checking data transfer `None` (default) | `Even` | `Odd` | `Mark` | `Space`

Select a parity for checking data integrity.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `parity` |

### **Enable auto RTS/CTS** — Enable RTS/CTS handshake `off` (default) | `on`

To enable the Request To Send/Clear To Send (RTS/CTS) handshake of the Universal
Asynchronous Receiver-Transmitter (UART) for flow control, select this check box. Serial
controllers use the RTS/CTS handshake to prevent data loss due to hardware FIFO overflow on
the device that you are sending
to.

Usually, the interrupt service routine executes quickly enough to empty the FIFO. If your
model gets FIFO overruns, select this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ctsmode` |

### **Max Output count** — Maximum number of elements for block to return `1024` (default) | integer

Enter the maximum number of elements that you want returned by a single
call to this block. The block uses this parameter to set the output vector
width.

If you select the **Read to delimiter** check box and if
the block does not find the delimiter before it reads **Receive
maximum read** characters, the output vector is empty.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxread` |

### **Min Output count** — Minimum number of elements for block to return `1` (default) | integer

Enter the minimum number of characters to read. If the FIFO does not
contain at least this number of characters, the output vector is
empty.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `minread` |

### **Read to delimiter** — Return characters including message delimiter `on` (default) | `off`

For the block to return all
characters in the FIFO, up to and including the specified delimiter, select
this check box.

If the buffer has errors, such as framing errors, the modem returns
characters regardless of the presence of the delimiter. These returned
characters help diagnose errors such as mismatched baud rates.

If the block does not find the delimiter before it reads **Receive
maximum read** characters, the output vector is empty.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `usedelimiter` |

### **Delimiter** — Numeric value of message delimiter `13` (default) | integer

Enter the numeric value of the character that is the message delimiter.
Any value from `0` to
`255` is valid. The common case looks for
`10` (line feed) or `13` (carriage
return).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `delimiter` |

### **Receive data type** — Data type of receiver `8 bit int null terminated` (default) | `8 bit uint null terminated` | `count+16 bit int` | `count+16 bit uint` | `count+32 bit int` | `count+32 bit uint`

This parameter specifies the data type of the receiver. The 8-bit data
types produce a NULL-terminated character vector in the output
vector.

For 16-bit and 32-bit data types, the first element contains the number of
valid elements in the rest of the output vector.

For 8-bit data types, only the character data is in the output vector, and
a NULL terminator is appended. The 16-bit or 32-bit wide data types cause
the error status from the UART to be placed in the second byte of each data
element. (The error status contains the parity, overrun, framing, and break
bits.) The character data is in the bottom 8 bits of each element. The first
element of the vector contains the number of data elements that
follow.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `odtype` |

### **Receive FIFO size** — FIFO size in bytes `1024` (default)

This parameter specifies the receive FIFO size in bytes.

**Example:** `1024`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fifosize` |

**Data Types:** `int32`

### **Transmit data type** — Data type of transmitter `count+32 bit int` (default) | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated` | `8 bit uint null terminated`

This parameter specifies the data type of the transmitter. The 8-bit data types require a
NULL-terminated character vector in the input vector.

The 16-bit and 32-bit data types reserve the first full element to contain the number of
elements to expect in the rest of the input vector. Only the low-order byte of each data
element is sent. Setting this data type enables a wider data type to hold the bytes.

If the data stream requires a NULL byte, select one of the 16-bit or 32-bit data types.
Because the 8-bit data types are NULL-terminated character vectors, the NULL byte terminates
the character vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `idtype` |

### **Sample Time** — Sample time `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time.
`-1` means that sample time is inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampletime` |

## Libraries

Simulink Real-Time / RS232 / Mainboard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2008a**

### R2021b: USB to Serial for RS232 Blocks

The RS232 mainboard blocks support connecting USB serial adapter ports. The
`Serial port` parameter of the Legacy Serial
Read block, Legacy Serial Write block, Legacy
Serial Setup block, Legacy Serial Port block, and
Legacy Serial Port F block means that you can select a
`USB Serial Port` or a `Legacy Serial
Port`.

## Description

Send and receive data over mainboard baseboard serial port

The Send/Receive block sets up the serial interface to send and
receive basic character streams. This block has basic First In, First Out (FIFO)
Read blocks inside the subsystem. It generates output as an array of packed
integers (settable at 8 bits, 16 bits, or 32 bits). Characters appear in the lower byte
and received status information appears in the upper byte.

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
