---
type: simulink-block
title: 'F28M35x/F28M36x UART Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28M35x / M3'
documentation_page: 'f28m35xf28m36xuartreceive'
documentation_source_path: 'ref/f28m35xf28m36xuartreceive.html'
language: en
---

# F28M35x/F28M36x UART Receive

## Ports
```yaml
ports:
- name: Data
  summary: UART receive data vector | scalar
  direction: output
- name: Status
  summary: UART receive status 0 | 1 | 2 | 3 | 4 | 8
  direction: output
```

### Output

### **Data** — UART receive data vector | scalar

Outputs the data read from the UART port.

### **Status** — UART receive status 0 | 1 | 2 | 3 | 4 | 8

The status port outputs one of these values:

- 0 — represents no error in data reception
- 1 — represents frame error
- 2 — represents parity error
- 3 — represents data synchronization error
- 4 — represents a break in the data reception
- 8 — represents an overrun error.
## Parameters
```yaml
parameters:
- name: UART Port
  summary: Select UART port for data transmission UART0 (default) | UART1 | UART2 | UART3 | UART4
  group: ''
- name: Additional package header
  summary: Prefix header S (default)
  group: ''
- name: Additional package terminator
  summary: Suffix terminator E (default)
  group: ''
- name: Data type
  summary: Type of data to be received uint8 (default) | double | single | int8 | int8 | int16 | int32 | uint32 | boolean
  group: ''
- name: Data length
  summary: Size of data to be received 1 (default) | positive integer
  group: ''
- name: Enable blocking mode
  summary: Enable blocking mode for data transmission off (default) | on
  group: ''
- name: Sample time
  summary: Interval at which block reads data 0.1 (default)
  group: ''
```

### **UART Port** — Select UART port for data transmission `UART0` (default) | `UART1` | `UART2` | `UART3` | `UART4`

Select a port number from UART0 to UART4 for data transmission.

The UART Port selection allows access to the different UART modules present on the
processor.

### **Additional package header** — Prefix header `S` (default)

Specify the additional package header to use as the prefix before the data packet
to synchronize the data packets.

### **Additional package terminator** — Suffix terminator `E` (default)

Specify the additional package terminator to use as the suffix after the data
packet to synchronize the data packets.

### **Data type** — Type of data to be received `uint8` (default) | `double` | `single` | `int8` | `int8` | `int16` | `int32` | `uint32` | `boolean`

Select the output data type.

### **Data length** — Size of data to be received `1` (default) | positive integer

Specify the data length to receive.

### **Enable blocking mode** — Enable blocking mode for data transmission `off` (default) | on

Enabling this option ensures that the FIFO buffer is checked for data availability
before receiving the data.

### **Sample time** — Interval at which block reads data `0.1` (default)

Specify the sample time for receiving data. To execute this block asynchronously,
set Sample Time to -1.
## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Receive data from the Universal Asynchronous Receiver Transmitter (UART) port

Receive serial data from the Universal Asynchronous Receiver/ Transmitter (UART)
port.

You can specify the ASCII characters for packaging your data with the additional package
header and terminator. You can specify the data type and the data length that you want to
receive using the block.

DMA interrupt will be used in the background for Data transfer from Receive FIFO to
buffer. `UART_DMARx interrupt` will be triggered when any data will be
received in the FIFO.
