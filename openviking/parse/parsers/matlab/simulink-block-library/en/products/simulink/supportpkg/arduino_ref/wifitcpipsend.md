---
type: simulink-block
title: 'WiFi TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifitcpipsend'
documentation_source_path: 'supportpkg/arduino_ref/wifitcpipsend.html'
language: en
---

# WiFi TCP/IP Send

## Ports

### Input

### **Port\_1** — Input data vector

The block accepts data as an *N*-by-1 array. The
block sends this data over a TCP/IP network to the receiving host. The
data is sent in little-endian format. To convert it to a big-endian
format, do any of the following:

- Place a Byte Reversal block just before the
  WiFi TCP/IP Send block.
- Apply the `swapbytes` function in a
  MATLAB
  Function block, and place the block just before
  the WiFi TCP/IP Send block.

The maximum number of bytes that can be sent by this block at each
time step is shown in the table.

| Target Hardware | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| Maximum Number of Sent Bytes | 2048 | 64 | 1400 |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Connection mode** — Set the block as server or client `Server` (default) | `Client`

Set the block as a TCP/IP server or client.

When you set this parameter to `Server`, you
must provide a **Local IP Port**. The local port
acts as the listening port on the TCP/IP server.

When you set this parameter to `Client`, you must provide a **Remote
IP address** and the **Remote IP port** on the
TCP/IP server to which you want to send the data. Before you deploy a model
that includes a client WiFi TCP/IP Send block, ensure that
the server is up and running.

### **Local IP port** — IP port on sending host from which data is sent `25000` (default) | [1 to 65,535]

Specify the port number of the application from which data is sent. This local port acts as
the listening port on the TCP/IP server.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to `Server`.

### **Remote IP address** — Remote IP address of server to which data is sent `192.168.1.2` (default) | any valid IP address

Specify the remote IP address of the server to which the data is
sent.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Remote IP port** — Remote IP port on server to which data is sent `25000` (default) | [1 to 65,535]

Specify the port number on the receiving server to which data
is sent.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to `Client`.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Send data over TCP/IP network to remote host over wireless network

The WiFi TCP/IP Send block sends data to a remote host or other hardware board
over a wireless network. You can set **Connection mode** of the block
to `Server` or `Client`. When you set
**Connection mode** to `Client`, you must provide
the **Server IP Address** and the **Server IP Port**
of the server to which you want to send data. When you set **Connection
mode** to `Server`, you must provide the **Local
IP Port**. This **Local IP Port** acts as a listening port
on the TCP/IP server.

You can run a Simulink® model containing WiFi TCP/IP Send block in Connected IO
mode on Arduino® boards.

**Note**

ESP32 and ESP8266 boards are not supported in Connected IO mode.

For more information about the fixed ports and the allocated pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

**Note**

If you are having trouble using TCP to communicate with a computer, antivirus or
firewall software might be blocking TCP traffic. If so, configure the software to
allow the traffic for a specific IP port number.

### Supported Hardware

You can use the WiFi TCP/IP Send block only with the following hardware:

- ESP8266
- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
