---
type: simulink-block
title: 'WiFi UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifiudpsend'
documentation_source_path: 'supportpkg/arduino_ref/wifiudpsend.html'
language: en
---

# WiFi UDP Send

## Ports

### Input

### **Port\_1** — Input data vector

The block accepts data as an *N*-by-1 array. The block sends this data over
a wireless network to the receiving host. The data is sent in
little-endian format. To convert it to a big-endian format, do any of
the following:

- Place a Byte Reversal block just before the
  WiFi UDP Send block.
- Apply the `swapbytes` function in a
  MATLAB
  Function block, and place the block just before
  the WiFi UDP Send block.

The maximum number of bytes that can be sent by this block at each
time step is shown in the table.

| Target Hardware | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| Maximum Number of Sent Bytes | 2048 | 64 | 1400 |

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **Remote IP address** — Remote IP address of host to which data is sent `192.168.1.2` (default) | any valid IP address

Specify the remote IP address of the host to which the data is sent. To
broadcast data to all the receiving hosts, specify
`255.255.255.255`.

### **Remote IP Port** — Remote IP port on host to which data is sent `50002` (default) | [1 to 65,535]

Specify the port number of the application on the host to which data is sent. Match the remote
port number with the local port number on the receiving host.

### **Local IP Port** — IP port on sending host from which data is sent `50001` (default) | [1 to 65,535]

Specify the port number of the application on the target from which data is sent.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Send data to UDP host on wireless network

The WiFi UDP Send block sends data to a UDP host over a wireless network. The
block sends data from the port number specified in the **Local IP
Port** parameter. Specify the IP address and the port number of the
receiving host in the **Remote IP address** and the **Remote IP
Port** parameters.

You can run a Simulink® model containing WiFi UDP Send block in Connected IO mode
on Arduino® boards.

For more information about the fixed ports and the allocated pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

**Note**

If you are having trouble using UDP to communicate with a computer, antivirus or
firewall software might be blocking UDP traffic. If so, configure the software to
allow the traffic for a specific IP port number.

### Supported Hardware

You can use the WiFi UDP Send block only with the following hardware:

- ESP8266
- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
