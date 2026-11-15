---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/arduino_ref/udpreceive.html'
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

## Parameters

### **Local IP port** — IP port number of local device `56789` (default) | integer from 1 to 65,535

Specify the IP port number on which to receive UDP packets. The local device is the
iOS device that is running the model.

### **Sample time** — Sample time `1` (default) | nonnegative scalar

Specify how often this block reads the UDP messages, in seconds. Enter a value
greater than zero. This value defaults to a sample time of one second.

Smaller values require the processor to complete the same number of instructions in
less time, which can cause task overruns.

## Libraries

Simulink Support Package for Arduino Hardware / Ethernet Shield

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013b**

## Description

Receive data over UDP network from remote host

Use the UDP Receive  block to receive user datagram protocol (UDP) data
from a remote host. The block reads available UDP data from the socket buffer and outputs the
data as a vector.
