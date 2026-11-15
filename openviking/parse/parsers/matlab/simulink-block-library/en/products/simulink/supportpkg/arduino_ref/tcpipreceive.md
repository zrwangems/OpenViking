---
type: simulink-block
title: 'TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'tcpipreceive'
documentation_source_path: 'supportpkg/arduino_ref/tcpipreceive.html'
language: en
---

# TCP/IP Receive

## Ports

### Output

### **Data** — Output port to emit the data received [Nx1] array

The block outputs data as an [Nx1] array.

**Data Types:** `uint8`

### **Status** — Output port to emit the data received status 1 | 0

This port shows the data received status. The status value 1 means successful
receipt of data.

**Data Types:** `int32`

## Parameters

### **Server port** — Server port at which to receive data `5896` (default) | scalar

Enter the port number through which you want the TCP/IP server to initiate the
message reception. The server port numbers range from 0 to 65535.

### **Sample time** — Time frequency at which block receives data 1 (default) | scalar

Specify how often this block reads the TCP/IP messages, in seconds. Enter a value
greater than zero. This value defaults to a sample time of `1`
second.

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

Receive data over TCP/IP network from remote host

Use the TCP/IP Receive block to receive data from a remote host or another
target hardware over a network.
