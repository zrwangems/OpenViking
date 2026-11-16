---
type: simulink-block
title: 'UDP Receive'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'udpreceive'
documentation_source_path: 'udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Data received vector | matrix | array

Data received by the block from the remote address, returned as a vector, matrix,
or array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Status** — New data available `0` (default) | `1`

New data available status, returned as a logical `1`
(`true`) or `0` (`false`). If
this port returns `1`, new data is available to be read.

#### Dependencies

To enable this port, unselect the **Enable blocking mode** parameter.

**Data Types:** `Boolean`

## Parameters

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

### **Remote address** — Remote host name or address `localhost` (default) | remote host name or IP address

IP address or name of the remote machine or server that you want to receive data
from.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Host` |
| **Type:** character vector, string |

### **Remote port** — Remote host port `9090` (default) | remote host port

Remote port on the machine that you want to connect to, specified as a number from 1
to 65,535.

You can also specify the value of this parameter as an existing workspace
variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Port` |
| **Type:** character vector, string |
| **Values:** 1 to 65,535 |
| **Default:** `'9090'` |

### **Verify address and port connectivity** — Remote machine connection verification button

Click this button to check if a connection to the specified remote address and port
is valid.

### **Output latest data** — Receive latest data `off` (default) | `on`

This parameter allows you to receive the latest data. Select this parameter if you
want to receive the latest data.

Data is normally received in a FIFO manner. When enabled, the latest available
packets are received, instead of the block using the FIFO method.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GetLatestData` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

#### Dependencies

This parameter is not available if you set **Source Data type**
to `ASCII`.

### **Data size** — Number of values read `[1, 1]` (default) | numeric array

Output data size, or the number of values to be read at each simulation time step.
This parameter is specified as a scalar or vector.
The data does not include the terminator
values.

You can also specify the value of this parameter as an existing workspace
variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataSize` |
| **Type:** character vector, string |
| **Values:** vector |
| **Default:** `'[ 1, 1 ]'` |

### **Source Data type** — Output data type `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `ASCII`

Data type that the block receives from the remote address, specified as a
MATLAB® data type.

This data type must match the data type of the data at the remote address. You
cannot use this parameter to change the data type of the data at the remote
address.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Type:** character vector, string |
| **Values:** `'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'ASCII'` |
| **Default:** `'uint8'` |

### **ASCII format string** — Format of string data `%f` (default) | numeric conversion specifiers

Format of the received string data. You can use the following conversion specifiers
or a combination of them.

| Numeric Field Type | Conversion Specifier | Details |
| --- | --- | --- |
| Integer, signed | `%d` | Base 10 |
| `%i` | The values in the data determine the base:  - The default is base 10. - If the initial digits are `0x` or   `0X`, then the values are hexadecimal (base 16). - If the initial digit is `0`, then values are octal   (base 8). |
| `%ld` or `%li` | 64-bit values, base 10, 8, or 16 |
| Integer, unsigned | `%u` | Base 10 |
| `%o` | Base 8 (octal) |
| `%x` | Base 16 (hexadecimal) |
| `%lu`, `%lo`, `%lx` | 64-bit values, base 10, 8, or 16 |
| Floating-point number | `%f` | Floating-point fields can contain any of the following (not case sensitive): `Inf`, `-Inf`, `NaN`, or `-NaN`. |
| `%e` |
| `%g` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ASCIIFormatting` |
| **Type:** character vector, string |
| **Values:** `'%d'` | `'%i'` | `'%ld'` | `'%li'` | `'%u'` | `%o'` | `'%x'` | `'%lu'` | `'%lo'` | `'%lx'` | `'%f'` | `'%e'` | `'%g'` |
| **Default:** `'%f'` |

#### Dependencies

To enable this parameter, set **Source Data type** to
`ASCII`.

### **Terminator** — Terminator `LF` (default) | `CR` | `CR/LF` | `LF/CR` | `Custom terminator`

Terminator that indicates the end of your data block. The simulation considers any
data that occurs before the terminator as a new data block. The terminator data is not
sent to the output port. This terminator must match the terminator in the data you are
reading from your remote machine.

If you select `Custom Terminator`, you can specify your own
terminator value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Terminator` |
| **Type:** character vector, string |
| **Values:** `'CR'` | `'LF'` | `'CR/LF'` | `'LF/CR'` | `'Custom terminator'` |
| **Default:** `'LF'` |

#### Dependencies

To enable this parameter, set **Source Data type** to
`ASCII`.

### **Custom Terminator** — Custom terminator numeric array | integer from 0 to 255

Custom terminator that indicates the end of your data block. The simulation
considers any data that occurs before the terminator as a new data block. The terminator
data is not sent to the output port.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters. The exact form of this
parameter depends on the type of the ASCII character.

| Type of ASCII Character | Example ASCII Character | MATLAB Command | Parameter Value |
| --- | --- | --- | --- |
| Control character (escape sequence) | `"LF"` (`"\n"`) | `uint8(sprintf('\n'))` | `[10]` |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"End"` | `uint8('End')` | `[69 110 100]` |

You can also specify this parameter using the hexadecimal representation
of the ASCII characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomTerminator` |
| **Type:** character vector, string |
| **Values:** integer array |
| **Default:** `'10'` |

#### Dependencies

To enable this parameter, set **Terminator** to
`Custom terminator`.

### **Byte order** — Sequential order of bytes `big-endian` (default) | `little-endian`

Sequential order in which bytes are arranged into larger numerical values. If the
byte order is `little-endian`, the first byte is organized in
the first memory address in the received UDP packet. If the byte order is
`big-endian`, the last byte is organized in the first memory
address in the received UDP packet.

Configure the byte order to match the appropriate value for your remote machine
before receiving data. Refer to your instrument documentation for information about the
order in which it stores bytes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ByteOrder` |
| **Type:** character vector, string |
| **Values:** `'little-endian'` | `'big-endian'` |
| **Default:** `'big-endian'` |

### **Enable blocking mode** — Simulation waits while receiving data `on` (default) | `off`

This parameter has the simulation wait while the block receives data. When new data
becomes available, the simulation continues from the next time step. Unselect this
parameter if you do not want the read operation to cause the simulation to wait.

If you enable blocking mode, the simulation waits for the requested data to become
available. At each time step, the model waits for up to the amount of time specified by
the **Timeout** parameter. If data is not received within this time,
the block outputs a value of `0`.

If you do not enable blocking mode, the simulation runs continuously and the block
has two output ports, **Status** and **Data**. The
**Data** port contains the requested set of data at each time step.
The **Status** port contains 0 or 1 based on whether it received new
data at the given time step.

For more information, see Enable Blocking Mode in Receive and Send Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableBlockingMode` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Timeout** — Allowed time to complete operations 10 (default) | positive scalar

Amount of time in seconds that the model waits for data during each simulation time
step. This value is relative to real-world or "wall clock" time.

You can also specify the value of this parameter as an existing workspace
variable.

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

### **Block sample time** — Sampling time 0.01 (default) | positive numeric

Sampling time of the block during the simulation. This is the rate at which the
block is executed during simulation. For more information, see Timing in Hardware Interface Models.

You can also specify the value of this parameter as an existing workspace
variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector, string |
| **Values:** positive numeric |
| **Default:** `'0.01'` |

## Libraries

Instrument Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007b**

## Description

Receive data over UDP network from specified remote machine

The UDP Receive block configures and opens an interface to a specified
remote address using the UDP protocol. The configuration and initialization occur once at the
start of the model's execution. The block acquires data either in blocking mode or nonblocking
mode during the model's run time.

This block has no input ports. It has one or two output ports based on whether you select
blocking or nonblocking mode. If you select blocking mode, the block has one output port,
**Data**, corresponding to the data it receives. If you do not select
blocking mode, the block has two output ports, **Data** and
**Status**.

UDP Receive block nonblocking mode and blocking mode

This block uses a First In, First Out (FIFO) buffer to receive data. At each time step,
the **Data** port returns the requested values from the buffer. In
nonblocking mode, the **Status** port indicates if the block has received new
data. If the **Status** port displays `1`, new data is
available and if the **Status** port displays
`0`, no new data is available.

**Note**

You must have a license for both Instrument Control Toolbox™ and Simulink® to use this block.

### Other Supported Features

- The UDP Receive block supports the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution
  of Simulink models by using these modes. For more information on these simulation
  modes, see Acceleration (Simulink).
- The UDP Receive block supports the use of model referencing. This
  feature lets your model include other Simulink
  models as modular components.

For more information on these features, see the Simulink
documentation.
