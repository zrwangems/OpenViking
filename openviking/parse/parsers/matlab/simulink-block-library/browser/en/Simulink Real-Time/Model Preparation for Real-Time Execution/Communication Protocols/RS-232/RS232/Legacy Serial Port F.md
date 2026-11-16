---
type: simulink-block
title: 'Legacy Serial Port F'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'legacyserialportf'
documentation_source_path: 'io_ref/legacyserialportf.html'
language: en
---

# Legacy Serial Port F

## Ports

### Input

### **XMT** — Vector of data to transmit vector

Vector of the data used to transmit over the port.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **FIFO** — FIFO of data received over serial port serialfifoptr

First In, First Out (FIFO) containing data that has been received from
the serial port.

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

### **Port to modify** — Port that is being accessed `1` (default) | `2`

This parameter specifies the port for which you want to view or modify parameters. On
the Simulink® block, the upper port is port `1` and the lower port is
port `2`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `port` |

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
`-1` means that the sample time is inherited.

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

Send and receive data over mainboard baseboard serial port with FIFO

The Send/Receive FIFO block sets up the serial interface to send and
receive character and binary streams. It transmits input data as does the
Send/Receive block, but it propagates received data through First In,
First Out (FIFO) outputs.

A model that contains a Send/Receive FIFO block and the FIFO
Read block provides the same capability as the Send/Receive
block. A model that contains a Send/Receive FIFO block and a FIFO
Read HDRS or FIFO Read Binary block provides greater
capability than the Send/Receive block.

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
