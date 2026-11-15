---
type: simulink-block
title: 'TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'tcpipreceive'
documentation_source_path: 'supportpkg/parrot_ref/tcpipreceive.html'
language: en
---

# TCP/IP Receive

## Ports

### Output

### **Data** — Output data [Nx1] array

At each time step, the port outputs data as a vector of the size
specified in the **Data size (N)** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Status of the data received `1` | `0`

At each time step, when the length of data received is greater than or
equal to the length specified in the **Data size (N)**
parameter, the port outputs `1`. Otherwise, it outputs
`0`, indicating that no new data is
received.

**Data Types:** `uint16`

## Parameters

#### Main Tab

### **Connection mode** — Set block as server or client `Server` (default) | `Client`

Set the block as TCP/IP server or client.

When you set this parameter to `Server`, you must provide
a **Local IP port**. The local port acts as the listening
port of the TCP/IP server.

When you set this parameter to `Client`, you must provide
the **Remote IP port** of the TCP/IP server from which you
want to receive the data.

### **Local IP port** — IP port of receiving host from which data is received `25000` (default) | [1, 65535]

This local port number acts as a listening port of the receiving host.
Match the local port number with the remote port number of the sending
host.

### **Remote IP address** — Remote IP address of server from which data is received `192.168.3.2` (default)

The IP address of the server from which the data is received. The
**Remote IP address** is set at 192.168.3.2; do not
change this IP address.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Remote IP port** — Remote IP port of server from which data is received `25000` (default) | [1, 65535]

Specify port number of the server from which data is received.

**Note**

Do not use ports `24099` and `26061`
for TCP/IP communication with Parrot minidrone as these ports are
reserved.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the type of data the block receives from the sending host. The
size of each element depends on its data type.

### **Data size (N)** — Number of bytes in received data `1` (default) | any positive integer

The number of bytes to receive at each time step.

### **Sample time** — Interval at which block reads data from sending host `0.005` (default) | any non-negative value that is a multiple of 0.005 (5 ms) | -1

Enter the time interval at which to receive data.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

#### Advanced Tab

### **Manually specify local IP port** — Manually specify the number of the local IP port off (default) | logical

Allow manual specification of local IP port at which to receive data. This
parameter appears only when you set the **Connection mode**
to `Client`.

### **Local IP port** — Local port at which to receive data 25000 (default) | scalar

Enter the local port of the client to receive data. This parameter appears
only when you set the **Connection mode** to
`Client` and select the check box
**Manually specify local IP port**.

### Receive TCP Data

This section explains the values at the output ports in non-blocking mode, with
the following block parameters specified as:

| Block Parameter | Value |
| --- | --- |
| **Data type** | `uint8` |
| **Data size (N)** | `4` |

The values at the output ports vary depending on whether the length of data
received is less than, greater than, or equal to the length of requested data.

- Length of data received = Data size (N): The **Data**
  port outputs data as a vector of the size specified in the
  **Data size (N)** parameter. The
  **Status** port outputs `1`,
  indicating that the requested data is received.

  Suppose that the length of the data received is 4. In this case, the
  **Data** port outputs a data vector of size 4
  filled with the received data bytes. The **Status**
  port outputs `1`.
- Length of data received < Data size (N): In non-blocking mode, the
  block does not wait for the requested data to be available. The
  **Data** port outputs data as a vector of the size
  specified in the **Data size (N)** parameter filled
  with zeros. The **Status** port outputs
  `0`, indicating that no new data is
  received.
- Length of data received > Data size (N): The
  **Data** port outputs a data vector of the size
  specified in the **Data size (N)** parameter. The
  vector contains only the first *N* bytes from the
  data. The remaining bytes are emitted along with the data bytes in the
  next time step. The **Status** port outputs
  `1`, indicating that the requested data is
  received.

  Suppose that the length of data received is 5 bytes. In this case, the
  **Data** port outputs a data vector of size 4. The
  vector contains only the first 4 bytes from the received data. The fifth
  byte is emitted along with the data bytes in the next time step. The
  **Status** port outputs
  `1`.

| Data Length | Mode of Read Operation | | Output Port | |
| --- | --- | --- | --- | --- |
| Data | Status |
| Length of data received = Data size (N) | Non-blocking | |  | `1` |
| Length of data received < Data size (N) | Non-blocking | |  | `0` |
| Length of data received > Data size (N) | Non-blocking | |  | `1` |

## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Receive data over TCP/IP network from remote host

The TCP/IP Receive block receives data from a remote host over a
Bluetooth® network. When you set **Connection mode** to
`Server`, you must provide the **Local IP port**.
The **Local IP port** acts as the listening port of the TCP/IP server.
When you set **Connection mode** to `Client`, you must
provide the **Remote IP port** of the server from which to receive the
data.

The block has two output ports, **Data** and
**Status**. At each sample time, the **Data** port
outputs data as a vector of the size specified in the **Data size (N)**
parameter. The **Status** port contains 0 or 1 to indicate whether the
new data at the specified time step is received. The **Status** port
value 1 indicates that the data from **Data** port is valid.

Parrot® minidrone is a little-endian device. The TCP/IP Receive
block expects the byte order of the received TCP/IP data to be big-endian, and it
converts the data to little-endian.

**Note**

In some cases, the antivirus or firewall software might block the TCP traffic. If
so, configure the antivirus or firewall software to allow the traffic for a specific
IP port number.
