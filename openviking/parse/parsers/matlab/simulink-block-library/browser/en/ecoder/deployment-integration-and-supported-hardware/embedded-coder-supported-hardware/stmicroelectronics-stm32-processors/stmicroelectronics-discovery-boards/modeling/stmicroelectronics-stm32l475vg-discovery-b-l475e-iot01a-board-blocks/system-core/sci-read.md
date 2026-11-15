---
type: simulink-block
title: 'SCI Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'sciread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/sciread.html'
language: en
---

# SCI Read

## Ports

### Output

### **Rx** — Data read from UART vector

The port outputs the data read from the selected UART.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — Status of read operation scalar

When you select the **Output error status**
parameter, an output port, labeled as `Status`, becomes
available.

The port outputs the status of each read request as mentioned in the
following table:

**Return status codes**

| **Status** | Description |
| --- | --- |
| `0` | SUCCESS |
| `1` | RX\_BUSY |
| `2` | TX\_BUSY |
| `4` | PARITY\_ERROR |
| `8` | FRAME\_ERROR |
| `16` | BUS\_ERROR |
| `32` | DATA\_NOT\_AVAILABLE |

When the length of data received is greater than or equal to the
length specified in the **Data length (N)** parameter,
the output is `0`. Otherwise, the output is a nonzero
value, indicating that the length of data available is less than the
length specified in the **Data length (N)**
parameter.

`0` indicates a successful read operation.

For example, when the length of data received is 9 and
*N* = 8, the **Status** port
outputs `0` indicating a successful read operation.
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

SCI module to which the SCI device is connected.

**Note**

In external mode, the SCI0 module is reserved for external mode
communication and cannot be used by the SCI Read
block.

### **Data type** — Data type of data from the UART port `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Data type of data to be read from the UART port.

### **Data length (N)** — Number of data points to be read from the UART port `1` (default) | Any integer greater than or equal to 0

Number of data points to be read from the UART port for the selected data
type.

### **Output status** — Status of read operation off (default) | on

Select this parameter to enable the **Status**
port.

### **Sample time** — Frequency at which to read data from the UART port `0.1` (default)

Frequency at which to read data from the UART port, specified in seconds.
When you set this parameter to `-1`, Simulink determines
the best sample time for the block based on the block context within the
model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Read N -by- 1 array of data on UART

The SCI Read block reads an
*N*-by-*1* array of data from the Universal
Asynchronous Receiver Transmitter (UART), where *N* is the length of
data to be read. You can change the **Baudrate** and select the
**Receive pin** for the UART Serial Communication Interface (SCI)
from **Configuration Parameters**  > **Hardware Implementation pane** > **SCI**.

During external mode simulation, the block outputs the simulation results returned
from the executable running on the target hardware. During simulation in all other
modes, the block outputs zeroes.

This block operates in nonblocking mode.
