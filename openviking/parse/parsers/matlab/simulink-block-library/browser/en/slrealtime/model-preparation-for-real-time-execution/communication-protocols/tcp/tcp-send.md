---
type: simulink-block
title: 'TCP Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / TCP'
documentation_page: 'tcpsend'
documentation_source_path: 'io_ref/tcpsend.html'
language: en
---

# TCP Send

## Ports

### Input

### **Enable** — Allow data transmission integer

When `Enable` > `0`, the block
attempts to transmit data to the remote
device.

As a best practice, connect the `Status` output
of a TCP configure block to the `Enable` input of
the associated TCP Send and TCP Receive blocks.

### **Data** — Data to transmit over the TCP network vector

Vector of `Length` to transmit to the client
device.

**Data Types:** `uint8`

### **Length** — Length of data vector double

Number of `uint8` values to transmit to the client
device.
### Output

### **Status** — Number of bytes sent double

Returns the number of `uint8` values transmitted to
the client
device.

## Parameters

### **Send using** — List of IP address and port pairs Read-only: `x.x.x.x:y`

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

Send data over TCP network to a remote device

The TCP Send block sends data from a server application on a
Speedgoat® target computer to a
remote client device.
