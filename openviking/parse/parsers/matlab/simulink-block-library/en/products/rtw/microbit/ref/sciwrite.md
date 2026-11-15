---
type: simulink-block
title: 'SCI Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Basic'
documentation_page: 'sciwrite'
documentation_source_path: 'microbit/ref/sciwrite.html'
language: en
---

# SCI Write

## Ports

### Input

### **Tx** — Data sent to UART vector

The data from your model sent to the UART port.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### Output

### **Status** — Status of write operation scalar

When the length of data received is greater than or equal to the
length specified in the **Data length (N)** parameter,
the output is `0`. Otherwise, the output is a nonzero
value, indicating that the length of data available is less than the
length specified in the **Data length (N)**
parameter.

`0` indicates a successful write operation.

For example, when the length of data received is 9 and
*N* = 8, the **Status** port
outputs `0` indicating a successful write operation.
When the length of data received is 9 and *N* = 10, the
**Status** port outputs `32`
indicating that data is not available.

| Length of Data Received = 9 | | | | |
| --- | --- | --- | --- | --- |
| **Port** | **Data Type** | **Data Length** | | |
| *N* = 8 | *N* = 9 | *N* = 10 |
| **Rx** | `uint8` | `8` | `9` | `9` |
| **Status** | `uint8` | `0` | `0` | `32` |

#### Dependencies

To enable the port, select the **Output status**
parameter.

**Data Types:** `uint8`

## Parameters

### **SCI module** — SCI module used for communications `0` (default) | Any integer value

SCI module that corresponds to the group of SCI pins that communicate with
the SCI device.

**Note**

In external mode, the SCI0 module is reserved for external mode
communication and cannot be used by the SCI Write
block.

### **Output status** — Option to display the status of write operation off (default) | on

Select this parameter to enable the **Status**
port.

The port outputs `0` for a successful write
operation.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Send N -by- 1 array of data to UART

The SCI Write block sends an
*N*-by-*1* array of data to the selected Universal
Asynchronous Receiver Transmitter (UART), where *N* is the length of
data to be read. The block inherits the data type from the signal at the input port. You
can change the **Baudrate** and select the **Transmit
pin** for the UART Serial Communication Interface (SCI) from **Configuration Parameters**  > **Hardware Implementation pane** > **SCI**.

During external mode simulation, the block outputs the simulation results returned
from the executable running on the target hardware. During simulation in all other
modes, the block outputs zeroes.
