---
type: simulink-block
title: 'SCI Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'sciread'
documentation_source_path: 'beagleboneblue/ref/sciread.html'
language: en
---

# SCI Read

## Ports

### Output

### **Data** — Data read from UART vector

The **Data** port outputs the data read from the
selected UART.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — Status of read operation scalar

When the length of data received is greater than or equal to the
length specified in the **Data length (N)** parameter,
the block outputs `0`. The value `0`
indicates a successful read operation. When the length of data received
is less than the length specified in the **Data length
(N)** parameter, the block outputs a nonzero value.

For example, when the length of data received is 9 and
*N* = 8, the **Status** port
outputs `0`, indicating a successful read operation.
When the length of data received is 9 and *N* = 10, the
**Status** port outputs `32`,
indicating that data is not available.

| Length of Data Received = 9 | | | | |
| --- | --- | --- | --- | --- |
| **Port** | **Data Type** | **Data Length** | | |
| *N* = 8 | *N* = 9 | *N* = 10 |
| **Data** | `uint8` | `8` | `9` | `9` |
| **Status** | `uint8` | `0` | `0` | `32` |

**Data Types:** `uint8`

## Parameters

### **Port** — Serial port to which hardware is connected `/dev/ttyO1` (default) | valid path and file name

Specify the serial port on the hardware that is connected to the serial
device. For example, if the port UT0 is connected to a serial device,
specify this parameter as `/dev/ttyO0`. To view the
BeagleBone® Blue pinout, click the **View pin map**
button.

### **Baudrate (in bits/s)** — Serial baud rate `9600` (default) | `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

Select the number of bits to receive per second. The received bits include
the start bit, the data bits, the parity bit (if defined), and the stop
bits.

### **Parity** — Type of error checking for received data `None` (default) | `Even` | `Odd`

Select a parity to provide simple error checking for the received data.
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

Select the number of stop bits used to indicate the end of a byte.

- `1` — One stop bit is transmitted to
  indicate the end of a byte.
- `2` — Two stop bits are transmitted
  to indicate the end of a byte.

### **Data type** — Data type of data from UART port `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Select the type of data to be read from the UART port.

### **Data length (N)** — Number of data values to read from UART port `1` (default) | nonnegative integer

Specify the number of values to be read from the UART port for the
selected data type.

### **Sample time** — How often to read data from UART port `0.1` (default) | `-1` | nonnegative integer

Specify the time interval to read data from the UART port, specified in
seconds. When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Read serial data from UART port

The SCI Read block reads an *N*-by-1 array of data
from the Universal Asynchronous Receiver Transmitter (UART) on the hardware, where
*N* is the length of data to be read.

If you simulate a model that contains the SCI Read block without
connecting the hardware, the block outputs zeroes. See Block Produces Zeros or Does Nothing in Simulation.

This block operates in nonblocking mode.
