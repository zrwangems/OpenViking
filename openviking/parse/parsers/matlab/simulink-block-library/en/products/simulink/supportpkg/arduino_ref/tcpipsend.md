---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/arduino_ref/tcpipsend.html'
language: en
---

# TCP/IP Send

## Ports

### Input

### **Port\_1** — Input port to accept data [Nx1] array

The block inputs the data values to send from the block to your remote
host.

**Data Types:** `uint8`

## Parameters

### **Server port** — Server port number `50000` (default) | integer from 1 to 65,535

Enter the port number through which you want the TCP/IP server to send the messages.
The server port numbers range from 0 to 65535.

## Libraries

Simulink Support Package for Arduino Hardware / Ethernet Shield

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013b**

## Description

Send data over TCP/IP network to another remote host

Use the TCP/IP Send block to send data to a remote host or another hardware
board over the network.
