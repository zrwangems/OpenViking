---
type: simulink-block
title: 'TCP/IP Send'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'tcpipsend'
documentation_source_path: 'tcpipsend.html'
language: en
---

# TCP/IP Send

## Ports

### Input

### **Data** — Data values to send vector | matrix | array

Data values to send from the block to your remote host, specified as a vector,
matrix, or array. The array size of this data must not change during simulation. Set
the parameters for this block before you send data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## Parameters

### **Remote address** — Remote host name or address remote host name or IP address

IP address or name of the TCP/IP server that you want to send data to.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Host` |
| **Type:** character vector, string |

### **Port** — Remote host port `80` (default) | remote host port

Remote port on the TCP/IP server that you want to connect to, specified as a number
from 1 to 65535.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Port` |
| **Type:** character vector, string |
| **Values:** 1 to 65,535 |
| **Default:** `'80'` |

### **Verify address and port connectivity** — Remote machine connection verification button

Click this button to check if a connection to the specified remote address and port
is valid.

### **Byte order** — Sequential order of bytes `big-endian` (default) | `little-endian`

Sequential order in which bytes are arranged into larger numerical values. If the
byte order is `little-endian`, then the remote machine stores
the first byte in the first memory address. If the byte order is
`big-endian`, then the remote machine stores the last byte in
the first memory address.

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

This parameter has the simulation wait while the block sends data. Clear the check
box if you do not want the write operation to cause the simulation to wait.

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

### **Timeout** — Allowed time to complete operations 10 (default) | positive scalar

Amount of time in seconds that the model waits for data to be sent during each
simulation time step. This value is relative to real-world or "wall clock" time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Timeout` |
| **Type:** character vector, string |
| **Values:** positive scalar |
| **Default:** `'10'` |

#### Dependencies

To enable this parameter, set **Enable blocking mode** to
`on`.

### **Transfer Delay** — Enables delayed acknowledgment `on` (default) | `off`

If you enable this parameter, the block collects small segments of outstanding data
and sends them in a single packet when acknowledgment (ACK) arrives from the server.
Clear this check box if you want to immediately send data to the network.

If a network is slow, you can improve its performance by enabling the transfer
delay. However, on a fast network acknowledgements arrive quickly and the difference
between enabling or disabling the transfer delay is negligible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TransferDelay` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

## Libraries

Instrument Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block generates platform-specific code for the host machine's platform only
(Windows®, macOS, Linux®). Set the **Device vendor** and **Device
type** in **Model Settings** > **Hardware
Implementation**. You must also select **Support long long**
under **Device details**.

## Version History

**Introduced in R2007b**

## Description

Send data over TCP/IP network to specified remote machine

The TCP/IP Send block configures and opens an interface to the specified
remote address using the TCP/IP protocol. The configuration and initialization occur once at
the start of the model's execution. The block sends data either in blocking mode or
nonblocking mode during the model's run time. Use the TCP/IP Send block to
write streaming data over a TCP/IP network. This block works only as a TCP/IP client and
cannot be used as a TCP/IP server.

The TCP/IP Send block has one input port that accepts both 1-D vector and
matrix data. The array size of this data must not change during simulation. This block has no
output ports. The block inherits the data type from the signal at the input port. Valid data
types are `single`, `double`, `int8`,
`uint8`, `int16`, `uint16`,
`int32`, `uint32`, `int64`, and
`uint64`.

### Other Supported Features

- The TCP/IP Send block supports the use of Simulink® Accelerator mode and Rapid Accelerator. This
  feature speeds up the execution of Simulink
  models.
- The TCP/IP Send block supports the use of model referencing. This
  feature lets your model include other Simulink
  models as modular components.
- The TCP/IP Send block supports C/C++ code generation. This feature
  allows you to generate C and C++ code using Simulink
  Coder™.

For more information on these features, see the Simulink
documentation.
