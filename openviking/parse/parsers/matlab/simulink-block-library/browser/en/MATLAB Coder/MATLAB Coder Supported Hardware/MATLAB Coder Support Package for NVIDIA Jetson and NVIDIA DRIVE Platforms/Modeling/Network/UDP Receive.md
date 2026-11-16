---
type: simulink-block
title: 'UDP Receive'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'udpreceive'
documentation_source_path: 'nvidia/ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — UDP packets received from sending UDP host `vector` (default)

At each sample time, the port outputs the contents of a packet
received as a data vector of the size that you specify in the
**Data size (N)** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Size** — Determine if requested data is received at given time step `scalar` (default)

The port outputs 0 if the data is received at a given time step.
Otherwise, it outputs a nonzero value indicating that no new data is
available.

**Data Types:** `uint8`

## Parameters

### **Local IP port** — IP port on NVIDIA® Jetson™ board to receive data `25000` | positive integer in the range `[1,65535]`

Specify the port number of the application from which you want to receive
the packets. Match the local port number with the remote port number of the
sending host.

### **Data type** — Data type of elements in UDP packets `uint8` (default) | `boolean` | `uint16` | `uint32` | `int8` | `int16` | `int32` | `single` | `double`

Select the data type of the elements in the UDP packets received by the
block. The size of each element depends on its data type.

### **Data size** — Number of data elements in each UDP packet `255` (default)

Specify the number of elements that you want to receive in each
packet.

### **Sample time (seconds)** — Time frequency at which block receives data `0.1` (default) | `scalar`

Specify how often the block should read the port buffer. Enter a value
greater than `0` or `-1` (for inherited
sample time).

When you specify this parameter as-1, Simulink® determines the best sample time for the block based on the
block context within the model.

This value defaults to a sample time of `0.1` seconds.
Smaller values require the processor to complete the same number of
instructions in less time and this can cause task overruns.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Receive UDP packets from UDP host

The UDP Receive block receives UDP packets from a UDP host. Use the block for
stateless and connectionless data exchange.

With each sample, the block outputs the contents of a UDP packet as a data vector of
the size specified in the **Data size (N)** parameter.

The data type of the block output, `Data`, depends on the
**Data type** parameter. The data type of the block output,
`Size`, is `uint16`.

**Note**

Your antivirus software or firewall might block UDP traffic. Configure the
software to allow traffic from a specific IP port number.
