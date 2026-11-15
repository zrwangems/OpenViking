---
type: simulink-block
title: 'Serial Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'serialwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/serialwrite.html'
language: en
---

# Serial Write

## Ports

### Input

### **Port\_1** — The input port to accept data [Nx1] or [1xN] array

The input port through which the block accepts data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

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

### **Parity** — Even parity or the odd parity added to the data `None` (default) | `Even` | `Odd`

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

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Write data to the serial device

Write data to a serial device connected to the Raspberry Pi® hardware.
To open the pin map of the Raspberry Pi board, click the **View
pin map**.

Refer to Asynchronous Serial Communication for information.
