---
type: simulink-block
title: 'TCP/IP Send'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'tcpipsend'
documentation_source_path: 'nvidia/ref/tcpipsend.html'
language: en
---

# TCP/IP Send

## Ports

### Input

### **Port1** — Input port to accept data [Nx1] array

The block accepts data as an [Nx1] array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

#### Main Tab

### **Connection mode** — Option to set the block as client or server `Server` (default) | `Client`

Select this option to set the block as TCP/IP client or TCP/IP server.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Mode_` |
| **Type:** character vector |
| **Values:** `'Server'`|`'Client'` |
| **Default:**  `'Server'` |

### **Local IP port** — Local port acting as the listening port of the server 25000 (default) | scalar

Enter the local port number which acts as the listening port of the TCP/IP server.
This parameter appears only when you set the **Connection mode** to
`Server`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LocalServerPort_` |
| **Type:** character vector |
| **Values:** `'25000'`|`scalar` |
| **Default:**  `'25000'` |

### **Remote IP address** — Remote address of the server to which to send the data 127.0.0.1 (default) | scalar

Enter the remote server address to which to send the data. This parameter appears
only when you set the **Connection mode** to
`Client`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoteAddr_` |
| **Type:** character vector |
| **Values:** `'127.0.0.1'`|`scalar` |
| **Default:**  `'127.0.0.1'` |

### **Remote IP port** — Remote port of the server to which to send data 25000 (default) | scalar

Enter the remote server port. This parameter appears only when you set the
**Connection mode** to `Client`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoteServerPort_` |
| **Type:** character vector |
| **Values:** `'25000'`|`scalar` |
| **Default:**  `'25000'` |

#### Advanced Tab

### **Manually specify local IP port** — Manually specify the number of the local IP port off (default) | on

Allow manual specification of local IP port from which to send data. This parameter
appears only when you set the **Connection mode** to
`Client`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ClientPortBindingSelection_` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Local IP port** — Local port from which to send the data 25000 (default) | scalar

Enter the local port of the client to send data. This parameter appears only when
you set the **Connection mode** to `Client`
and select the check box **Manually specify local IP port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ClientPortToBind_` |
| **Type:** character vector |
| **Values:** `'35000'`|`scalar` |
| **Default:**  `'35000'` |

### **Wait until previous packet transmitted** — Option to set for the block to wait for the data to be sent off (default) | on

Select this option to specify for block to wait for the current data to be sent.
Selecting this check box enables the ‘blocking mode’.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BlockingMode_` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Timeout in seconds** — Time to wait until the data is sent 0.1 (default) | scalar

Specify the time the block waits for the data to be sent during each simulation time
step. This field is unavailable, if you have not selected **Wait until previous
packet transmitted** parameter. Enter `inf` value in this
parameter, if you want the block to wait indefinitely until it sends the data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BlockTimeout_` |
| **Type:** character vector |
| **Values:** `'0.1'`|`scalar` |
| **Default:**  `'0.1'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Send data over TCP/IP network to another remote host

Send data to a remote host/another hardware board over the network. You can set the
connection mode of the block as a server or a client. When you set connection mode as TCP/IP
client, you must provide the remote address and the remote IP port of the TCP/IP server to
which you have to send the data. When you set the block as a TCP/IP server, you must provide
the local IP port of the TCP/IP server. This IP port acts as the listening port of the TCP/IP
server.
