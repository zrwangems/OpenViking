---
type: simulink-block
title: 'F28M35x/F28M36x UART Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28M35x / M3'
documentation_page: 'f28m35xf28m36xuarttransmit'
documentation_source_path: 'ref/f28m35xf28m36xuarttransmit.html'
language: en
---

# F28M35x/F28M36x UART Transmit

## Ports

### Input

### **Data** — UART send data vector | scalar

The port sends the data to the UART port.

DMA will be used internally to copy data in FIFO.

## Parameters

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

### **Enable blocking mode** — Enable blocking mode for data transmission `off` (default) | on

Enabling this option ensures that the FIFO buffer is checked for data availability
before sending the data.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Transmit serial data to the Universal Asynchronous Receiver Transmitter (UART) port

Transmit serial data through the Universal asynchronous Receiver/ Transmitter (UART)
port. You can specify ASCII characters for packaging your data with the additional package
header and terminator.
