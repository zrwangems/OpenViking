---
type: simulink-block
title: 'TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Communication Protocol Blocks'
documentation_page: 'tcpipreceive'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/tcpipreceive.html'
language: en
---

# TCP/IP Receive

## Ports

### Output

### **Data** — Output port to emit the data received [Nx1] array

The block outputs data as an [Nx1] array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — Output port to emit the data received status 1 | 0

This port shows the data received status. The status value 1
means successful receipt of data.

**Data Types:** `int8`

## Parameters

#### Main Tab

### **Connection mode** — The option to set the block as server or client `Server` (default) | `Client`

Select the option to connect the block as TCP/IP server or TCP/IP
client.

### **Local IP port** — Local port acting as the listening port of the server 25000 (default) | scalar

Enter the local port number which acts as the listening port
of the TCP/IP server. This parameter appears only when you set the **Connection
mode** to `Server`

### **Remote IP address** — Remote address of the server from which to receive data 127.0.0.1 (default) | scalar

Enter the remote server address from which to receive the data. This
parameter appears only when you set the **Connection mode**
to `Client`.

### **Remote IP port** — Remote port of the server from which to receive data 25000 (default) | scalar

Enter the remote server port. This parameter appears only when
you set the **Connection mode** to `Client`.

### **Data type** — Data type to receive uint8 (default) | double | single | int8 | uint16 | int16 | uint32 | int32 | boolean

Select the data type that is to be received from the remote
host.

### **Data size(N)** — Data size to receive 1 (default) | scalar

Enter the data size to be received from the remote host.

### **Sample time** — The time frequency at which to receive data 0.1 (default) | scalar

Enter the time frequency at which to receive data.

#### Advanced Tab

### **Manually specify local IP port** — Manually specify the number of the local IP port off (default) | on

Allow manual specification of local IP port at which to receive
data. This parameter appears only when you set the **Connection
mode** to `Client`.

### **Local IP port** — Local port at which to receive data 25000 (default) | scalar

Enter the local port of the client to receive data. This parameter
appears only when you set the **Connection mode** to `Client` and
select the check box **Manually specify local IP port**.

### **Wait until data received** — Option to set for the block to wait for the data to be received off (default) | on

Select this option to specify if the block waits for the data
to be received. Selecting this check box enables the blocking mode.

### **Timeout in seconds** — Time to wait until the data is received 0.1 (default) | scalar

Specify the time the block waits for the data to be received
during each simulation time step. This field is unavailable, if you
have not selected **Wait until data received** parameter.
Enter ‘inf’ value in this parameter, if you want the
block to wait indefinitely until it receives the data.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Receive data over TCP/IP network from remote host

Receive data from a remote host/another target hardware over
a network. When you set the connection mode as server, you must provide
the local port. The local port acts as the listening port of the TCP/IP
server. When you set the block as a client, you must provide the remote
address and the remote port of the TCP/IP server to receive data.
The block accepts data either in blocking mode or in non-blocking
mode. The **Data** port output contains
the requested data at each time step. The **Status** port
contains 0 or 1 to indicate whether the new data at the specified
time step is received. The Status port value 1 indicates that the
data from **Data** port is valid.

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
