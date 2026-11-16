---
type: simulink-block
title: 'C29x UART Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F29H85x'
documentation_page: 'c29xuarttransmitblock'
documentation_source_path: 'ref/c29xuarttransmitblock.html'
language: en
---

# C29x UART Transmit

## Ports

### Input

### **Data** — UART send data vector | scalar

The port sends the data to the UART port.

## Parameters

### **UART module** — UART module `A` (default) | `B`

Select the UART module from which you want to transmit the data.

### **Additional package header** — Prefix header `S` (default)

Specify the additional package header to use as the prefix before the data
packet to synchronize the data packets.

### **Additional package terminator** — Suffix terminator `E` (default)

Specify the additional package terminator to use as the suffix after the data
packet to synchronize the data packets.

### **Enable blocking mode** — Enable blocking mode for data transmission `off` (default) | on

Enabling this option ensures that the FIFO buffer is checked for data
availability before sending the data.

## Libraries

C2000 Microcontroller Blockset / F29H85x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Send serial data to the Universal Asynchronous Receiver Transmitter (UART) port

Send serial data through the Universal asynchronous Receiver/ Transmitter (UART) port.
You can specify ASCII characters for packaging your data with the additional package header
and terminator.

DMA will be used internally to copy data in FIFO.
