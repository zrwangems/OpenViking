---
type: simulink-block
title: 'TCP/IP Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'tcpreceive'
documentation_source_path: 'nucleo/ref/tcpreceive.html'
language: en
---

# TCP/IP Receive

## Ports

### Output

### **Data** — Output data vector

At each time step, the port outputs data as a vector of the size that
you specify in the **Data size (N)** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Requested data received at given time step scalar

At each time step, when the length of data received is greater than or
equal to the length specified in the **Data size (N)**
parameter, the port outputs `0`. A value of
`0` indicates that the requested data is received
at the given time step. Otherwise, it outputs a nonzero value,
indicating that no new data is received.

**Data Types:** `uint16`

## Parameters

### **Connection mode** — Set the block as server or client `Server` (default) | `Client`

Set the block as TCP/IP server or client.

When you set this parameter to `Server`, you must provide
a **Local IP Port**. The local port acts as the listening
port on the TCP/IP server.

When you set this parameter to `Client`, you must provide
the **Server IP Address** and the **Server IP
Port** on the TCP/IP server from which you want to receive the
data.

### **Local IP Port** — IP port on receiving host from which data is received `25001` (default) | any integer from 1 to 65,535

This local port number acts as a listening port on the TCP/IP server.
Match the local port number with the remote port number of the sending
host.

### **Server IP Address** — Remote IP address of server from which data is received `192.168.1.2` (default) | any valid IP address

Specify the IP address of the sending server from which the data is
received.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Server IP Port** — Remote IP port on server from which data is received `25000` (default) | any integer from 1 to 65,535

Specify port number on the sending server from which data is
received.

#### Dependencies

This parameter appears only when you set the **Connection
mode** to `Client`.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the type of the data the block receives from the sending host. The
size of each element depends on its data type.

### **Data size (N)** — Number of data bytes in received data `1` (default) | any positive integer

Specify number of data bytes to receive at each time step.

### **Wait until data received** — Wait until requested data is available `off` (default) | `on`

- When you select this parameter, the read operation runs in
  blocking mode. The read operation is blocked while waiting for the
  requested data to be available. If data is available, the
  **Data** port outputs data. If data is not
  available, the **Data** port waits for data.

  A task overrun occurs if the target hardware is still waiting for
  the data to be available when the next read operation is scheduled
  to begin.

  To fix overruns:

  - Increase the time step by using the **Sample
    time** parameter.
  - Reduce the length of data requested by using the
    **Data size (N)** parameter.
- When you clear this parameter, the read operation runs in
  non-blocking mode. When reading data, if data is not available, the
  **Data** port contains the data received in the
  previous time step. The **Status** port outputs
  `0`. In this mode, the block does not wait for
  the requested data to be available.

### **Output error status** — Option to display the error status during data transmission `on` (default) | `off`

Select this option to display the error status during data
transmission.

When you select the Output error status parameter, the block configures
an output port. The port on the block is labeled as Status, indicating that
the block outputs the status of the read operation at the output
port.

### **Sample time** — Interval at which block reads data from sending host `-1` (default) | nonnegative value

When you set this parameter to `-1`, Simulink®
determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Receive data over TCP/IP network from remote host

The TCP Receive block receives data from a remote host or other target
hardware over a network. When you set **Connection mode** to
`Server`, you must provide the **Local IP Port**.
The **Local IP Port** acts as the listening port of the TCP/IP server.
When you set **Connection mode** to `Client`, you must
provide the **Server IP Address** and the **Server IP
Port** on the server from which to receive the data. The server must be up
and running before deploying the model that contains the TCP Receive
block to the target.

The block accepts data either in blocking mode or in non-blocking mode. In blocking
mode, the model blocks the execution while it waits for the requested data to be
available. In non-blocking mode, the model runs continuously. To set the block in
blocking mode, select the **Wait until data received** option.

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

At each time step, the **Data** port outputs data as a vector of the
size that you specify in the **Data size (N)** parameter. The
**Status** port outputs 0 or a nonzero value indicating whether new
data is received. 0 at the **Status** port indicates that a valid data
is received.

**Note**

In some cases, the antivirus or firewall may block the TCP traffic. If so,
configure the antivirus or firewall to allow the traffic for a specific IP port
number.
