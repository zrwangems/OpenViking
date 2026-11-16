---
type: simulink-block
title: 'TCP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28M36x / M3'
documentation_page: 'tcpreceive'
documentation_source_path: '../rtw/freescalefrdmk64fboard/ref/tcpreceive.html'
language: en
---

# TCP Receive

## Ports

### Output

### **Data** — Output data vector

At each time step, the port outputs data as a vector of the size that
you specify in the **Data size (N)** parameter. For
more information, see Receive TCP Data.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Requested data received at given time step `0` | `1`

At each time step, when the length of data received is greater than or
equal to the length specified in the **Data size (N)**
parameter, the port outputs `0`. Otherwise, it outputs
`1`, indicating that no new data is
received.

For more information, see Receive TCP Data.

**Data Types:** `uint16`

## Parameters

#### Main

### **Connection mode** — Set block as server or client `Server` (default) | `Client`

Set the block as TCP/IP server or client.

When you set this parameter to `Server`, you must provide
a **Local IP Port**. The local port acts as the listening
port of the TCP/IP server.

When you set this parameter to `Client`, you must provide
the **Remote IP Address** and the **Remote IP
Port** of the TCP/IP server from which you want to receive the
data.

### **Local IP Port** — IP port of receiving host from which data is received `25001` (default) | [1 to 65,535]

This local port number acts as a listening port of the receiving host.
Match the local port number with the remote port number of the sending
host.

### **Remote IP Address** — Remote IP address of server from which data is received `192.168.1.2` (default) | any valid IP address

Specify the IP address of the server from which the data is
received.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Remote IP Port** — Remote IP port of server from which data is received `25000` (default) | [1 to 65,535]

Specify port number of the server from which data is received.

#### Dependencies

This parameter appears only when you set the **Connection
mode** to `Client`.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the type of the data the block receives from the sending host. The
size of each element depends on its data type.

### **Data size (N)** — Number of bytes in received data `1` (default) | any positive integer

The number of bytes to receive at each time step.

### **Sample time** — Interval at which block reads data from sending host `0.1` (default) | any nonnegative value

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

#### Advanced

### **Wait until data received** — Wait until requested data is available on (default) | off

- When you select this option, the read operation runs in blocking
  mode. The read operation is blocked while waiting for the requested
  data to be available. When reading, if data is not available, the
  block waits for the time specified in the **Timeout in
  seconds** parameter. For more information on the values
  at the output port in blocking mode, see Receive TCP Data.

  A task overrun occurs if the target hardware is still waiting for
  the data to be available when the next read operation is scheduled
  to begin.

  To fix overruns:

  - Increase the time step by using the **Sample
    time** parameter.
  - Reduce the length of the data requested by using the
    **Data size (N)** parameter.
- When you clear this option, the read operation runs in
  non-blocking mode. In this mode, the block does not wait for the
  requested data to be available. For more information on the values
  at the output port in non-blocking mode, see Receive TCP Data.

### **Timeout in seconds** — Time to wait until data is received `0.1` (default) | `Inf` | any nonnegative value

Specify the amount of time that the block waits for the data to be
available during each time step. If timeout occurs, the read operation is
aborted.

#### Dependencies

The parameter is available only when you select the **Wait
until data received** parameter.

### Receive TCP Data

This section explains the values at the output ports in blocking and non-blocking
mode, with the following block parameters specified as:

| Block Parameter | Value |
| --- | --- |
| **Data type** | `uint8` |
| **Data size (N)** | `4` |

The values at the output ports vary depending on whether the length of data
received is less than, greater than, or equal to the length of requested data.

- Length of data received = Data size (N): The **Data**
  port outputs data as a vector of the size specified in the
  **Data size (N)** parameter. The
  **Status** port outputs `0`,
  indicating that the requested data is received.

  Suppose that the length of the data received is 4. In this case, the
  **Data** port outputs a data vector of size 4
  filled with the received data bytes. The **Status**
  port outputs `0`.
- Length of data received < Data size (N): In blocking mode, the
  block waits for the data to be available for **Timeout in
  seconds** seconds. If the data becomes available within
  **Timeout in seconds** seconds, the
  **Data** port outputs data as a vector of the size
  specified in the **Data size (N)** parameter. The
  **Status** port outputs `0`,
  indicating that new data is received. If the wait time exceeds
  **Timeout in seconds**, the
  **Data** port outputs data as a vector of the size
  specified in the **Data size (N)** parameter filled
  with zeros. The **Status** port outputs
  `1`, indicating that no new data is
  received.

  In non-blocking mode, the block does not wait for the requested data
  to be available. The **Data** port outputs data as a
  vector of the size specified in the **Data size (N)**
  parameter filled with zeros. The **Status** port
  outputs `1`, indicating that no new data is
  received.
- Length of data received > Data size (N): The
  **Data** port outputs a data vector of the size
  specified in the **Data size (N)** parameter. The
  vector contains only the first *N* bytes from the
  data. The remaining bytes are emitted along with the data bytes in the
  next time step. The **Status** port outputs
  `0`, indicating that the requested data is
  received.

  Suppose that the length of data received is 5 bytes. In this case, the
  **Data** port outputs a data vector of size 4. The
  vector contains only the first 4 bytes from the received data. The fifth
  byte is emitted along with the data bytes in the next time step. The
  **Status** port outputs
  `0`.

| Data Length | Mode of Read Operation | | Output Port | |
| --- | --- | --- | --- | --- |
| Data | Status |
| Length of data received = Data size (N) | Blocking | |  | `0` |
| Non-blocking | |
| Length of data received < Data size (N) | Blocking | Data received before timeout occurred |  | `0` |
| Wait time exceeded the specified timeout |  | `1` |
| Non-blocking | |  | `1` |
| Length of data received > Data size (N) | Blocking | |  | `0` |
| Non-blocking | |

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Receive data over TCP/IP network from remote host

The TCP Receive block receives data from a remote host or other target
hardware over a wired network. When you set **Connection mode** to
`Server`, you must provide the **Local IP Port**.
The **Local IP Port** acts as the listening port of the TCP/IP server.
When you set **Connection mode** to `Client`, you must
provide the **Remote IP Address** and the **remote IP
Port** of the server from which to receive the data.

The block has two output ports, **Data** and **Status**. At
each sample time, the **Data** port outputs data as a vector of the
size specified in the **Data size (N)** parameter.

The **Status** port outputs `0`, when the length of the data
received is greater than or equal to the length specified in the **Data size (N)** parameter. Otherwise, it outputs `1`,
indicating that no new data is available.

During simulations without the hardware, the block emits zeros.

**Note**

In some cases, the antivirus or firewall may block the TCP traffic. If so,
configure the antivirus or firewall to allow the traffic for a specific IP port
number.

The block accepts data either in blocking mode or in non-blocking mode.

In blocking mode, the model blocks the execution while it waits for the requested data to
be available.

blocking mode

At time step 1, the block requests four data values, and the TCP/IP receive buffer gets
four data values. The execution runs.

At time step 2, the block requests for data again, but the TCP/IP receive buffer gets
only three data values. The execution pauses until the buffer receives the fourth data
value or the time-out value elapses. Then, the execution resumes.

At time step 3, the block requests for data, and the buffer receives five data values.
The block returns the first four data values, and the remaining data value is used in the
next receipt cycle.

In non-blocking mode, the model runs continuously.

non blocking mode

At time step 1, the block requests data, and the buffer gets four data values. The block
changes the **Status** port value to 0, indicating that new
requested data is available. The **Data** port, at this
point, contains the newly received data values. The block resets the **Data** port value to 0.

At time step 2, the block requests data again, but the buffer gets only three values. The
block cannot return a value of 3 because the data size is specified as 4. Therefore, the
block sets the **Status** port value to 1, indicating that
there is no new data. All values on the **Data** port become
0. The buffer, at this point, has three data values. However, during this phase, the
execution does not stop unlike in the blocking mode.

At time step 3, the buffer has five data values, and the block returns the first four
data values in the order received and changes the **Status**
port value to 0. The remaining data value is used in the next receipt cycle.
