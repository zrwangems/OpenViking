---
type: simulink-block
title: 'TCP Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'tcpreceive'
documentation_source_path: 'io_ref/tcpreceive.html'
language: en
---

# TCP Receive

## Ports

### Input

### **Enable** — Allow data reception integer

When `Enable` > `0`, the block
attempts to receive data sent to the remote
device.

As a best practice, connect the `Status` output
of a TCP configure block to the `Enable` input of
the associated TCP Send and TCP Receive blocks.
### Output

### **Data** — Data that is received from the remote client vector

The parameter **Receive width** determines the
maximum size of the data vector.

**Data Types:** `uint8`

### **Length** — Actual size of data vector double

To test whether the number of data items exceeds the width of the data
output port, use this value.

## Parameters

### **Receive using** — List of IP address and port pairs Read-only: `x.x.x.x:y`

This parameter is read-only.

The block receives the list of IP address and port pairs from the TCP
configuration blocks in the model.

Ports `1` through `1023` and
`5500` through `5560` are reserved for Simulink Real-Time
communications.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `socketAddPort` |

### **Receive width** — Maximum expected length of data vector `1–65504`

Maximum number of `uint8` values that the block expects
to receive from the client
device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rcvWidth` |

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time. `-1` means
that the sample time is inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleTime` |

## Libraries

Simulink Real-Time / IP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Receive data over TCP network from a remote device

The TCP Receive block receives data sent from a remote client
device to a server application on
a Speedgoat® target
computer.
