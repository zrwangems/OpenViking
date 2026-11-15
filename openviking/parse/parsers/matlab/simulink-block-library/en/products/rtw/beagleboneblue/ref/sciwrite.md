---
type: simulink-block
title: 'SCI Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'sciwrite'
documentation_source_path: 'beagleboneblue/ref/sciwrite.html'
language: en
---

# SCI Write

## Ports

### Input

### **Port\_1** — Data sent to UART vector

The data from your model sent to the UART port.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## Parameters

### **Port** — Serial port on hardware `/dev/ttyO1` (default) | valid path and file name

Specify the serial port on the hardware that is connected to the serial
device. For example, if the port UT0 is connected to a serial device,
specify this parameter as `/dev/ttyO0`. To view the
BeagleBone® pinout, click the **View pin map**
button.

### **Baudrate (in bits/s)** — Serial baud rate `9600` (default) | `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

Select the number of bits transferred per second. The transferred bits
include the start bit, the data bits, the parity bit (if defined), and the
stop bits.

### **Parity** — Type of error checking for transmitted data `None` (default) | `Even` | `Odd`

Select a parity to provide simple error checking for the transmitted data.
The table shows the types of parity checking.

| Parity Type | Description |
| --- | --- |
| `None` | No parity checking. |
| `Even` | The data bits plus the parity bit result in an even number of 1s. |
| `Odd` | The data bits plus the parity bit result in an odd number of 1s. |

The parity checking process follows these steps:

1. The transmitting device sets the parity bit to 0
   or 1, depending on the data bit values and the type of
   parity-checking selected.
2. The receiving device checks if the parity bit is
   consistent with the transmitted data. If it is, the data bits are
   accepted. If it is not, an error is returned.

For example, suppose the data bits 01110001 are transmitted to your
computer. If even parity is selected, the parity bit is set to 0 by the
transmitting device to produce an even number of 1s. If odd parity is
selected, the parity bit is set to 1 by the transmitting device to produce
an odd number of 1s.

**Note**

Parity checking can detect only 1-bit errors. Multiple-bit errors can
appear as valid data.

### **Stop bits** — Number of bits used to indicate end of byte `1` (default) | `2`

Select the number of stop bits used to indicate end of a byte.

- `1` — One stop bit is transmitted to
  indicate the end of a byte.
- `2` — Two stop bits are transmitted
  to indicate the end of a byte.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Send serial data to UART port

The SCI Write block sends data to the selected Universal Asynchronous
Receiver Transmitter (UART) port of the hardware. The data must be an
*N*-by-1 or 1-by-*N* array, where
*N* is the length of data to write. The block inherits the data
type from the signal at the input port.

If you simulate a model that contains the SCI Write block without
connecting the hardware, the block does nothing. For more information, see Block Produces Zeros or Does Nothing in Simulation.
