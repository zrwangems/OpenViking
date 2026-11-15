---
type: simulink-block
title: 'WiFi UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifiudpreceive'
documentation_source_path: 'supportpkg/arduino_ref/wifiudpreceive.html'
language: en
---

# WiFi UDP Receive

## Ports

### Output

### **Data** — Output data vector

At each sample time, the port outputs data as a vector of the size specified in the
**Data size (N)** parameter. The data is received
in little-endian format. To convert it to a big-endian format, do any of
the following:

- Place a Byte Reversal block immediately
  after the WiFi UDP Receive block.
- Apply the `swapbytes` function in a
  MATLAB
  Function block and place the block immediately
  after the WiFi UDP Receive block.

For more information, see Outputs for Received Data.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Size** — Number of data bytes received scalar

At each sample time, the port outputs the number of bytes in the
received data. For more information, see Outputs for Received Data.

**Data Types:** `uint16`

## Parameters

### **Local IP Port** — IP port on receiving host from which data is received `50001` (default) | [1 to 65,535]

Specify the port number of the application on which you want to receive data. Match the local
port number with the remote port number on the sending host.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the type of the data the block receives from the sending
host. The size of each element depends on its data type.

### **Data size (N)** — Number of bytes in received data `1` (default) | any positive integer

The number of bytes received at each sample time.

The maximum number of bytes that can be received by this block at each
sample time is shown in the table.

| Target Hardware | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| Maximum Number of Received Bytes | 40 | 64 | 1400 |

### **Sample time** — Interval at which block reads data from sending host `0.1` (default) | `-1` | any nonnegative value

When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the
block context within the model. When the hardware is ESP8266, the minimum
sample time allowed is `0.01` seconds. Otherwise, it is
`0.000001` seconds (1 microsecond).

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Receive data from UDP host on wireless network

The WiFi UDP Receive block receives data from a UDP host on a wireless network.
At each sample time, the block outputs data as a vector of the size specified in the
**Data size (N)** parameter. The block receives data on the port
number specified in the **Local IP Port** parameter. Match the port
number specified in the **Local IP Port** parameter with the remote
port number on the sending host.

**Note**

If you are having trouble using UDP to communicate with a computer, antivirus or
firewall software might be blocking UDP traffic. If so, configure the software to
allow the traffic for a specific IP port number.

You can run a Simulink® model containing WiFi UDP Receive block in Connected IO
mode on Arduino® boards.

For more information about the fixed ports and the allocated pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

### Supported Hardware

You can use the WiFi UDP Receive block only with the following hardware:

- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
