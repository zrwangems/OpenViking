---
type: simulink-block
title: 'WiFi TCP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'wifitcpreceive'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/wifitcpreceive.html'
language: en
---

# WiFi TCP Receive

## Ports

### Output

### **Data** — Output data vector

At each time step, the port outputs data as a vector of the size
specified in the **Data size (N)** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — Requested data received at given time step `scalar`

The port outputs `0` if the data is received at given
time step. At other times the port outputs a nonzero value, indicating
that no new data is available.

#### Dependencies

To enable this port, select the **Output
Status** parameter.

**Data Types:** `uint8`

## Parameters

### **Connection mode** — Set block as server or client `Server` (default) | `Client`

Set the block as a TCP server or client.

When you set this parameter to `Server`, you must provide
a **Local IP port**. The local port acts as the listening
port on the TCP server.

When you set this parameter to `Client`, you must provide
a **Remote IP address** and the **Remote IP
port** on the TCP server from which you want to receive the
data. Before you deploy a model that includes a client WiFi TCP
Receive block, ensure that the server is up and running.

### **Local IP port** — IP port on receiving host from which data is received `25000` (default) | `positive integer in the range [1 to 65,535]`

This local port number acts as a listening port on the TCP server. Match
the local port number with the remote port number of the sending
host.

#### Dependencies

To enable this parameter, set **Connection mode**
parameter to `Server`.

### **Remote IP address** — Remote IP address of server from which data is received `192.168.1.2` (default) | `any valid IP address`

Specify the IP address of the sending server from which the data is
received.

#### Dependencies

To enable this parameter, set **Connection mode**
parameter to `Server`.

### **Remote IP port** — Remote IP port on server from which data is received `25000` (default) | `positive integer in the range [1 to 65,535]`

Specify the port number of the sending server from which data is
received.

#### Dependencies

To enable this parameter, set **Connection mode**
parameter to `Server`.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type of the elements in the TCP data received by the
block. The size of each element depends on its data type.

### **Data size (N)** — Number of data bytes in received data `1` (default) | any positive integer

Specify the number of data bytes to receive at each time step.

### **Sample time** — Interval at which block reads data from sending host `0.5` (default) | nonnegative value

Specify how often the block should read the port buffer. Enter a value
greater than `0` or `-1` (for inherited
sample time).

This value defaults to a sample time of `0.5` seconds.
Smaller values require the processor to complete the same number of
instructions in less time and this can cause task overruns.

### **Timeout in seconds** — Time to wait until the data is received `0.001` (default) | (0.0005s to 30s)

Specify the maximum amount of time that the block should wait for the data
during each time step. If a timeout occurs, the read operation is aborted.

**Note**

When simulating a model in external mode, specify a value less
than `3` seconds.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Receive TCP/IP packets from another TCP/IP host on internet network

The WiFi TCP Receive block receives data from a remote host or other
hardware over a wireless network.

At each time step, the **Data** port outputs data as a
vector of the size specified in the **Data size (N)**
parameter. The **Status** port outputs 0 or a nonzero value
indicating whether new data is received. 0 at the **Status** port indicates that a valid data is received.

**Note**

Your antivirus software or firewall might block TCP traffic. Configure the
software to allow traffic from a specific IP port number.
