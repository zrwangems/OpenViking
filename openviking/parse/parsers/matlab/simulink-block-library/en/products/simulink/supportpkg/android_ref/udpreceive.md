---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/android_ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — UDP data received numeric vector

UDP data received from a remote host, returned as a numeric vector. Set the data
type of this output by using the **Data type**
parameter.

If you simulate a model containing the UDP Receive block on your
host computer in normal mode, then the **Data** port outputs a zero
for each step of the simulation when no UDP packets are available. As a free-running
application with a shorter period than the real-time application running on the
Android® device, many zeros can be produced from the output port
`Data`. In other words, the free-running simulation outputs zeros
while waiting for the slower real-time application on the Android device to send data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Size** — Size of received UDP packet nonegative scalar

Size of received UDP packet, returned as a nonnegative scalar. While the block
waits for new data to arrive, this port outputs a `0`. When new data
arrives, this port value changes to the length of the received UDP packet.

**Data Types:** `uint16`

## Parameters

### **Local IP port** — IP port number of local device `25000` (default) | integer from 1 to 65,535

Specify the IP port number of the local device. The local device is the iOS device
that is running the model.

### **Data type** — Data type of output UDP packet `uint8` (default) | `uint16` | `unit32` | `int8` | `int16` | `int32` | `single` | `double`

Set the data type of the vector elements in the output. Match this data type with
the data input used to create the UDP packets.

### **Data size (N)** — Size of output UDP packet `255` (default) | positive integer

Specify the number of data elements in each UDP packet. Match the data size used to
create the UDP packets.

### **Sample time** — Sample time `0.01` (default) | nonnegative scalar

Specify how often this block reads the port buffer. Enter a value greater than zero.

**Note**

Smaller values for **Sample time** require the processor to
complete the same number of instructions in less time, which can cause task
overruns.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014a**

## Description

Receive data over UDP network from remote host

Use the UDP Receive  block to receive user datagram protocol (UDP) data
from a remote host. The block reads available UDP data from the socket buffer and outputs the
data as a vector.
