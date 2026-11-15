---
type: simulink-block
title: 'Serial Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'serialwrite'
documentation_source_path: 'nvidia/ref/serialwrite.html'
language: en
---

# Serial Write

## Ports

### Input

### **Port\_1** — Input port that accepts data [Nx1] or [1xN] array

The input port through which the block accepts data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Port** — Port at which you connect board to serial device `/dev/ttyTHS1` (default)

The port at which you connect the NVIDIA
Jetson board to the serial device.

### **Baudrate (in bits/s)** — Bits per second `9600` (default) | `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

Select the rate at which the data is read over the serial line. The baud
rate is measured as the number of bits read per second.

### **Parity** — Parity added to data to detect error `None` (default) | `Even` | `Odd`

Select the parity you want to add to the transmitted data. A parity bit is
used to detect error in the data transmission.

- **None** – This value means that no parity is
  used for error detection in the data transmission.
- **Even** – The parity bit value is 1 if the
  number of bits with value 1 is odd. The parity bit value is 0 if the
  number of bits with value 1 is even.
- **Odd** – The parity bit value is 1 if the number
  of bits with value 1 is even. The parity bit value is 0 if the
  number of bits with value 1 is odd.

### **Stop bits** — Bits used to signal stop of data transmission 1 (default) | 2

Select the number of bits used to signal the stop of data
transmission.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Write data to serial port

Use the Serial Write block to write data to a serial device connected to a NVIDIA®
Jetson™ hardware. To open the serial pin map of the NVIDIA
Jetson board, click the **View pin map** button. For more
information, see Serial Port Mapping for NVIDIA Jetson Boards.
