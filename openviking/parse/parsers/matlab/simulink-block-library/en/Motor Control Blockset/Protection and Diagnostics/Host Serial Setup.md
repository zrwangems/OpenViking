---
type: simulink-block
title: 'Host Serial Setup'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'hostserialsetup'
documentation_source_path: 'ref/hostserialsetup.html'
language: en
---

# Host Serial Setup

## Ports

Not documented in R2025b.

## Parameters

### **Port name** — Port that you want to configure `'Please_select_a_port'` (default) | `'COM3'`

Select an available serial port that you want to configure. By default no port is
selected and this field displays `'Please_select_a_port'`. Use
a configured port in the Host Serial Transmit and Host Serial Receive blocks. Both
transmit and receive blocks must use a serial port that you configure using the
Host Serial Setup block.

### **Baud rate** — Baud rate for serial communication `115200` (default) | scalar

Enter the rate at which the model transmits the bits through the serial
interface.

### **Number of stop bits** — Number of stop bits `1` (default) | `2`

Enter the number of bits that the model uses to indicate the end of a byte.

### **Parity mode** — Method used to check parity bits `none` (default) | `odd` | `even`

Specify how you want to check parity bits in the data bits that the model transmits
through the serial port.

- `none` — Model does not perform parity check.
- `odd` — Model sets the parity bit to 0 if the number of
  ones in a given set of bits is even.
- `even` — Model sets the parity bit to 1 if the number
  of ones in a given set of bits is odd.

### **Timeout** — Time interval before a one-way communication times out `1.0` (default) | scalar

Enter values greater than or equal to zero (seconds). When the COM port involved is
using the protocol mode, this value indicates how long the transmitting side waits for
an acknowledgement from the receiving side or how long the receiving side waits for
data.

The system displays a warning message every *n* number of seconds,
when the transmit or receive block exceeds the **Timeout** value of
*n* seconds.

### **Byte order** — Byte order for serial communication `LittleEndian` (default) | `BigEndian`

Specify the byte order as either `LittleEndian` or
`BigEndian`. If byte order is
`LittleEndian`, the model stores the first byte in the first
memory address. If byte order is `BigEndian`, the model stores
the last byte in the first memory address. You should configure the byte order to an
appropriate value before performing a read or write operation.

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

Configure communication ports used by Host Serial Receive and Host Serial Transmit blocks

The Host Serial Setup block is a standalone block that standardizes the
serial communication (COM) port settings used by the Host Serial Receive and Host Serial
Transmit blocks.

Setting the COM port configurations globally by using the Host Serial Setup block avoids
conflicts. For example, the Host Serial Transmit block cannot use a COM1 port with settings
different than those on the COM1 port of the Host Serial Receive block. You need to set the
port configurations only once for each COM port.
