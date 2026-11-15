---
type: simulink-block
title: 'WiFi TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifitcpipreceive'
documentation_source_path: 'supportpkg/arduino_ref/wifitcpipreceive.html'
language: en
---

# WiFi TCP/IP Receive

## Ports

### Output

### **Data** — Output data vector

At each time step, the port outputs data as a vector of the size specified in the
**Data size (N)** parameter. The data is received in little-endian format.
To convert it to a big-endian format, do any of the following:

- Place a Byte Reversal block immediately after the WiFi TCP/IP
  Receive block.
- Apply the `swapbytes` function in a MATLAB Function block, and place the block immediately after the WiFi
  TCP/IP Receive block.

For more information, see Blocking Mode and Non-Blocking Mode.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — Requested data received at given time step `1` | `0`

At each time step, when the length of data received is greater than or equal to the length
specified in the **Data size (N)** parameter, the port outputs
`1`. Otherwise, it outputs `0`, indicating that no new
data is received.

For more information, see Blocking Mode and Non-Blocking Mode.

**Data Types:** `int8`

## Parameters

#### Main Tab

### **Connection mode** — Set block as server or client `Server` (default) | `Client`

Set the block as a TCP/IP server or client.

When you set this parameter to `Server`, you must provide a
**Local IP port**. The local port acts as the listening port on the TCP/IP
server.

When you set this parameter to `Client`, you must provide a
**Remote IP address** and the **Remote IP port** on the
TCP/IP server from which you want to receive the data. Before you deploy a model that includes
a client WiFi TCP/IP Receive block, ensure that the server is up and
running.

### **Local IP port** — IP port on receiving host from which data is received `25000` (default) | [1 to 65,535]

This local port number acts as a listening port on the TCP/IP
server. Match the local port number with the remote port number of
the sending host.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to `Server`.

### **Remote IP address** — Remote IP address of server from which data is received `192.168.1.2` (default) | any valid IP address

Specify IP address of the server from which the data is received.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to `Client`.

### **Remote IP port** — Remote IP port on server from which data is received `25000` (default) | [1 to 65,535]

Specify port number on the server from which data is received.

#### Dependencies

This parameter appears only when you set the **Connection
mode** to `Client`.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the type of data the block receives from the sending host. The size of each element
depends on its data type.

### **Data size (N)** — Number of bytes in received data `1` (default) | any positive integer

The number of bytes to receive at each time step.

The maximum number of bytes that can be received by this block at each time step is shown
in the table.

| Target Hardware | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| Maximum Number of Received Bytes | 40 | 64 | 1400 |

### **Sample time** — Interval at which block reads data from sending host `0.1` (default) | `-1` | any nonnegative value

When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the block context within
the model. When the hardware is ESP8266, the minimum sample time allowed is
`0.01` seconds. Otherwise, it is `0.000001` seconds (1
microsecond).

#### Advanced Tab

### **Wait until data received** — Wait until requested data is available off (default) | on

- When you select this option, the read operation runs in Blocking Mode. The read operation is blocked while waiting for the requested data
  to be available. When waiting for the data, the **Status** port displays
  same values from the previous time step. When the data become available, the
  **Data** port outputs data bytes, and the **Status** port
  changes to `1`.

  A task overrun occurs if the target hardware is still waiting for the data to be
  available when the next read operation is scheduled to begin.

  To fix overruns:

  - Increase the time step by using the **Sample time**
    parameter.
  - Reduce the length of data requested by using the **Data size (N)**
    parameter.
- When you clear this option, the read operation runs in Non-Blocking Mode. When reading data, if data is not available, the
  **Data** port outputs data as a vector of the size specified in the
  **Data size (N)** parameter filled with zeros. The
  **Status** port outputs `0`. In this mode, the block does
  not wait for the requested data to be available.

### **Timeout in seconds** — Time to wait until the data is received `0.1` (default) | (0, 2^32/1000]

Specify the amount of time that the block waits for the data during each time step. If timeout
occurs, the read operation is aborted.

**Note**

When simulating a model in External mode, we recommend you to specify **Timeout
in seconds** less than `3` seconds.

#### Dependencies

This parameter appears only when you select the **Wait
until data received** parameter.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Receive data over TCP/IP network from remote host on wireless network

The WiFi TCP/IP Receive block receives data from a remote host or other
hardware over a wireless network. When you set **Connection mode** to
`Server`, you must provide the **Local IP port**. The
**Local IP port** acts as a listening port on the TCP/IP server. When you set
**Connection mode** to `Client`, you must provide the
**Remote IP address** and the **Remote IP port** of the TCP/IP
server to receive data.

The block accepts data either in Blocking Mode or in Non-Blocking Mode. The block has two output ports, **Data** and
**Status**. The **Data** port outputs requested
data at each time step. The **Status** port indicates whether the
new data at the specified time step is received.

You can run a Simulink® model containing WiFi TCP/IP Receive block in Connected IO mode on
Arduino® boards.

**Note**

ESP32 and ESP8266 boards are not supported in Connected IO mode.

For more information about the fixed ports and the allocated pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

**Note**

If you are having trouble using TCP to communicate with a computer, antivirus or firewall
software might be blocking TCP traffic. If so, configure the software to allow the traffic for a
specific IP port number.

### Supported Hardware

You can use the WiFi TCP/IP Receive block only with the following hardware:

- ESP8266
- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
