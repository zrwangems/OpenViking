---
type: simulink-block
title: 'Serial Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'serialread'
documentation_source_path: 'supportpkg/raspberrypi_ref/serialread.html'
language: en
---

# Serial Read

## Ports

### Output

### **Data** — Output port to read data [Nx1] array

The data port through which the block reads the data from the
serial device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — Output port to emit the status of the data read scalar

The output port that emits status of the data read. The following table lists the possible
status values and their description.

| Status Value | Status Description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `RX_BUSY` |
| `2` | `TX_BUSY` |
| `4` | `PARITY_ERROR` |
| `8` | `FRAME_ERROR` |
| `16` | `BUS_ERROR` |
| `32` | `DATA_NOT_AVAILABLE` |

**Data Types:** `uint8`

## Parameters

### **Board** — The specific board used for serial communication `Pi 3 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi 5 Model`

Select the specific board that you are using. Changing the board
updates the pin choices that you get.

### **Port** — The port at which you want to connect to the serial device /dev/ttyAMA0 (default)

The port to which to you want to connect from the selected Raspberry Pi board
to the serial device. For Pi 3 Model B board, the default serial port
is /dev/ttyS0.

### **Baudrate (in bits/s)** — Bits per second 9600 (default) | 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400

Select the rate at which the data is read over the serial line. The baud rate is measured as
the number of bits read per second.

### **Parity** — Even parity or the odd parity added to the data used for error detection `None` (default) | `Even` | `Odd`

Select the parity added to the data transmitted. A parity bit
is used to detect error in data transmission.

- None – None value in this parameter means that
  no parity is used for error detection in the data transmission.
- Even parity – The parity bit value is 1, if
  the number of bits with value as 1 is odd. The parity bit value is
  0, if the number of bits with value as 1 is even.
- Odd parity – The parity bit value is 1, if
  the number of bits with value as 1 is even. The parity bit value is
  0, if the number of bits with value as 1 is odd.

### **Stop bits** — The bit used as the stop bit 1 (default) | 2

Select the bit used as the stop bit in the data transmission.
A stop bit marks the end of a unit of transmission.

### **Data length (N)** — Data length for transmission 1 (default) | scalar

Enter the data size that you want to read from the serial device
for the selected data type.

### **Data type** — Data type for transmission uint8 (default) | uint8 | uint16 | uint32 | int8 | int16 | int32 | single | double

Select the data type you want to transmit.

### **Sample time** — Time frequency at which block reads data 0.1 (default) | scalar

Specify how often this block reads the serial data. Enter a
value greater than zero.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Read data from serial device

Read data from a serial device connected to the Raspberry Pi® hardware.

Refer to Asynchronous Serial Communication for information.
To open the pin map of the Raspberry Pi board, click the **View
pin map** button.
