---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/parrot_ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Output UDP message received from sending UDP host [Nx1] array

At each sample time, the port outputs the data bytes of a message
received as a data vector of the size specified by the **Data
size (N)** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Size** — Number of data bytes in UDP message received scalar

At each sample time, the port outputs the number of data bytes in the
received message.

**Data Types:** `uint16`

## Parameters

### **Local IP port** — IP port on the receiving UDP host `25000` (default) | `[1, 65535]`

Specify the port number of the application on which you want to receive
messages. Match the local port number with the remote port number of the
sending host.

**Note**

Do not use ports `24099` and `26061`
for UDP communication with Parrot minidrone as these ports are
reserved.

### **Data type** — Data type of the data bytes in UDP message `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type of the bytes to be received from the sending
host.

### **Data size (N)** — Number of data bytes in each UDP message `4` (default)

Specify the number of data bytes that you want to receive in each
message.

### **Sample time** — Interval to read messages from sending UDP host `0.005` (default) | any non-negative value that is a multiple of 0.005 (5 ms) | -1

Enter the time interval at which to receive data.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Receive UDP message from UDP host

The UDP Receive block receives UDP message from a UDP host.

The block output, **Data**, emits UDP packet data as a
one-dimensional vector of a specified data type. The block output,
**Size**, emits the size of the data in the UDP buffer. With each
sample, the block outputs the bytes of a UDP message as a data vector of the size
specified by the **Data size (N)** parameter.

The data type of the block output, `Data`, depends on the
**Data type** parameter. The data type of the block output,
`Size`, is `uint16`. `Size`
represents the total bytes. For example, if the `Data Type` is double
and the number of elements (mentioned using the `Data size (N)`
parameter) is 5, then the value of `Size` is 40, that is, 8\*5
bytes.

The block receives the message on the port number specified in the **Local IP
port** parameter. Match the port number specified in the **Local IP
port** parameter with the remote port number of the sending host.

Parrot® minidrone is a little-endian device. The UDP Receive block
expects the byte order of the received UDP data to be little-endian.

**Note**

If you are having trouble using UDP to communicate with a computer, the antivirus
or firewall software might be blocking UDP traffic. If so, configure the software to
allow the traffic for a specific IP port number.
