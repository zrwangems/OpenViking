---
type: simulink-block
title: 'UDP Send'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Interface-Based Instrument Communication / UDP Interface'
documentation_page: 'udpsend'
documentation_source_path: 'udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Data** — Data values to send vector | matrix | array

Data values to send from the block to your remote host, specified as a vector,
matrix, or array. Set the parameters for this block before you send data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## Parameters

### **Remote address** — Remote host name or address remote host name or IP address

IP address or name of the remote machine or server that you want to send data
to.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Host` |
| **Type:** character vector, string |

### **Remote port** — Remote host port `9090` (default) | remote host port

Remote port on the remote machine or server that you want to connect to, specified
as a number from 1 to 65,535.

You can also specify the value of this parameter as an existing workspace
variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Port` |
| **Type:** character vector, string |
| **Values:** 1 to 65,535 |
| **Default:** `'80'` |

### **Local address** — Local host name or IP address 0.0.0.0 (default) | local host name or IP address

Host name, dotted-decimal IP address, or web server of the local host. This block
supports both IPV4 and IPV6 address formats.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LocalAddress` |
| **Type:** character vector, string |

### **Local port** — Port of local host for binding -1 (default) | local host port

Port of local host for binding for UDP, specified as a number from 1 to 65,535. If
you do not specify a value, a value is automatically assigned.

You can also specify the value of this parameter as an existing workspace
variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LocalPort` |
| **Type:** character vector, string |

### **Enable local port sharing** — Allow other UDP sockets to bind to same local port `off` (default) | `on`

Parameter that enables local port sharing. Select this parameter if you want to
allow other UDP sockets to bind to the same local port.

UDP ports can be shared by other applications to allow for multiple applications to
listen to the UDP datagrams on that port. You can bind this block to a specific
**Local port**, and in another application bind a UDP socket to that
same local port number so both can receive UDP broadcast data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnablePortSharing` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Verify address and port connectivity** — Remote machine connection verification button

Click this button to check if a connection to the specified remote address and port
is valid.

### **UDP packet size** — Maximum number of bytes written in datagram packet 512 (default) | numeric

Maximum number of bytes of data to be written in a datagram packet. You can increase
or decrease the packet size if necessary.

You can also specify the value of this parameter as an existing workspace
variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputDatagramPacketSize` |
| **Type:** character vector, string |
| **Values:** 1 to 65,535 |
| **Default:** `'512'` |

### **Byte order** — Sequential order of bytes `big-endian` (default) | `little-endian`

Sequential order in which bytes are arranged into larger numerical values. If the
byte order is `little-endian`, the remote machine stores the
first byte in the first memory address. If the byte order is
`big-endian`, the remote machine stores the last byte in the
first memory address.

Configure the byte order to match the appropriate value for your remote machine
before sending data. Refer to your instrument documentation for information about the
order in which it stores bytes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ByteOrder` |
| **Type:** character vector, string |
| **Values:** `'little-endian'` | `'big-endian'` |
| **Default:** `'big-endian'` |

### **Enable blocking mode** — Simulation waits while sending data `on` (default) | `off`

This parameter has the simulation wait while the block sends data. Unselect this
parameter if you do not want the write operation to cause the simulation to wait.

If you enable blocking mode, the simulation waits for the data to be sent. If you do
not enable blocking mode, the simulation runs continuously.

For more information, see Enable Blocking Mode in Receive and Send Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableBlockingMode` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

## Libraries

Instrument Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007b**

## Description

Send data over UDP network to specified remote machine

The UDP Send block configures and opens an interface to the specified
remote machine using the UDP protocol. The configuration and initialization occur once at the
start of the model's execution. The block sends data either in blocking mode or nonblocking
mode during the model's run time. You can use multiple UDP Send blocks at a
time to send data to a specific
port.

The UDP Send block has one input port that accepts both 1-D vector and
matrix data. This block has no output ports. The block inherits the data type from the signal
at the input port. Valid data types are `single`, `double`,
`int8`, `uint8`, `int16`,
`uint16`, `int32`, `uint32`,
`int64`, and `uint64`.

**Note**

You must have a license for both Instrument Control Toolbox™ and Simulink® to use this block.

### Other Supported Features

- The UDP Send block supports the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution
  of Simulink models by using these modes. For more information on these simulation
  modes, see Acceleration (Simulink).
- The UDP Send block supports the use of model referencing. This
  feature lets your model include other Simulink
  models as modular components.

For more information on these features, see the Simulink
documentation.
