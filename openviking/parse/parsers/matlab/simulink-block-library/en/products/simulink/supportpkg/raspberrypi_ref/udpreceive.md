---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — UDP packets received from sending UDP host vector

At each sample time, the block outputs the contents of a packet received as a data
vector of the size that you specify in the **Data size
(elements)** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Size** — Number of data bytes in UDP message received scalar

At each sample time, the block outputs the number of data bytes in the received
message.

**Data Types:** `uint8`

## Parameters

### **Local IP port** — IP port number on receiving UDP port `25000` (default) | positive integer in the range [`1`,`65535`]

Specify the port number of the application on which you want to receive the UDP
message. Match the local port number with the remote port number of the sending
host.

### **Data type** — Data type of elements in UDP packet `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type in which the block receives data bytes from the sending
host.

### **Data size (elements)** — Number of data elements in each UDP packet `255` (default) | scalar

Specify the number of elements that you want to receive in each UDP packet.

### **Sample time (seconds)** — Time intervals at which block receives data `0.01` (default) | scalar

Specify the frequency at which the scheduler calls the UDP Receive block, in
seconds. Enter a value greater than zero. In real-time operation, setting this parameter
to a smaller value reduces the likelihood of dropped UDP messages.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Receive UDP packets over IP network

The UDP Receive block receives UDP packets from a UDP host. Use the block
for stateless and connectionless data exchange.

**Note**

Your antivirus software or firewall might block UDP traffic. Configure the software to
allow traffic from a specific IP port number.
