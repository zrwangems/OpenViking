---
type: simulink-block
title: 'Serial Transmit'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'serialtransmit'
documentation_source_path: 'px4/ref/serialtransmit.html'
language: en
---

# Serial Transmit

## Ports

### Input

### **Data** — Data to be sent to the UART or USART port vector

The port accepts values as an N-by-1 or 1-by-N array.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **Port** — UART or USART port for serial communication `/dev/ttyACM0` (default) | `/dev/ttyS1` | `/dev/ttyS2` | `/dev/ttyS3` | `/dev/ttyS5` | `/dev/ttyS6`

Enter the name of the UART or USART port on the PX4 flight controller through which the block transmits the accepted data. To
view the mapping between UART/USART ports and the labels on the Pixhawk flight
controller, see Serial Port Names and Corresponding Labels on PX4 Flight Controller Boards.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Send serial data to UART or USART port

The Serial Transmit block sends serial data to the Universal Asynchronous
Receiver Transmitter (UART) port or the Universal Synchronous and Asynchronous Receiver
Transmitter (USART) port on the PX4® flight controller.

The block accepts data as an N-by-1 or 1-by-N array and sends the same to the specified
UART or USART port. The properties for each port for serial communication are mentioned in the
Configuration Parameters dialog box in Simulink® (go to **Configuration Parameters**  > **Hardware Implementation** > **/dev/tty**\* pane).

During Connected I/O simulation, this block writes data to the specified serial port of
the hardware.

The block inherits the data type from the signal at the input port.

**Note**

If you are using Cube Orange autopilot, then use `GPS2` for serial data
communication, as there might be issues using `TELEM1` or
`TELEM2` ports.
