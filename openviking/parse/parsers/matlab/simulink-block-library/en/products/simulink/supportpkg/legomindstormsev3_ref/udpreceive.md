---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Communication Protocol Blocks'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Output port for data [Nx1] array

The output port that emits the UDP packet data as a one dimensional
vector of a specified data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Size** — Size of the data in UDP buffer scalar

The output port that emits the size of the data in the UDP buffer.

**Data Types:** `uint16`

## Parameters

### **Local IP port** — Local IP port number used by the sending UDP host 25000 (default) | scalar

The number of the IP port on the local device, which can range
from 1 to 65535. This value defaults to `25000`.
The local device is the board running the model.

### **Data type** — Data type of the vector elements in the message output uint8 (default) | scalar

This is the data type of the vector elements in the message
output. Match the data type with the data input used to create the
UDP packets.

### **Data size (N)** — Number of data elements in each UDP packet 255 (default) | scalar

Set the number of data elements in each UDP packet. Match the
data size used to create the UDP packets.

### **Sample time** — Time frequency at which the block reads the port buffer 0.1 (default) | scalar

Specify how often this block reads the port buffer. Enter a
value greater than zero.

Smaller values require the processor to complete the same number
of instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Receive UDP packets from another UDP host on an Internet network

Receive UDP packets from the local network. The block output, **data**,
emits UDP packet data as a one-dimensional vector of a specified data
type. The block output, **size**, emits the size
the data in the UDP buffer.

The data type of the block output, `Data`,
depends on the **Data type** parameter. The data
type of the block output, `Size`, is `uint16`.

While UDP Receive waits for new data to arrive, **size** emits
a stream of zeros. When new data arrives, **size** changes
to a non-zero value.

If you simulate a model that contains the UDP Receive block on your host computer (e.g.,
Simulation > Normal), and send UDP packets to that model from a board, the
**data** output emits a disproportionately large number of zeros.
This is because Simulink® software simulates the model as a free-running application with a shorter
period than the real-time application running on the board. In other words, the
free-running simulation outputs zeros because it is waiting for the
“slower” real-time application on the board to send data. If both
applications were running on boards, this mismatch would not occur.

**Note**

If you are having trouble using UDP to communicate with a computer,
investigate whether antivirus or firewall software might be blocking
UDP traffic. If so, try configuring the software to allow UDP traffic
for a specific IP port number.
