---
type: simulink-block
title: 'Host Serial Receive'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'hostserialreceive'
documentation_source_path: 'ref/hostserialreceive.html'
language: en
---

# Host Serial Receive

## Ports

### Output

### **data** — Port to output received data scalar

A first in, first out (FIFO) buffer receives the data. At every time step, the
`data` port outputs the requested values from the buffer.

**Data Types:** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **status** — Transaction status scalar

The status of the transaction. The status can be one of the following
values:

- 0 — No errors
- 1 — A timeout occurred when the block was waiting to receive data
- 2 — There is an error in the received data (checksum error)
- 3 — SCI parity error flag — Occurs when a character is received with a
  mismatch
- 4 — SCI framing error flag — Occurs when an expected stop bit is not
  found

#### Dependencies

To enable this port, select the **Output receiving status**
parameter.

**Data Types:** `uint16`

## Parameters

### **Serial Connection** — Serial port used for receiving data `Serial 1` (default) | `Serial 2` | `Serial 3` | `Serial 4`

Specify a serial port to receive communication from the target hardware. Select an
available serial port from the list. You can configure the selected port using the
Host Serial Setup block. If you do not configure a serial port, the
block prompts you to do so. Each Host Serial Receive block must have a
configured serial port. If you use multiple ports in your simulation, you must configure
each port separately.

### **Additional package header** — Package header data `'S'` (default) | scalar

Specifies the data located at the front of the received data package, which is not
part of the data being received, and generally indicates start of data. The additional
package header must be an ASCII value. You can use a text value or a numeric value in
the range (0–255). You must put single quotes around the text that you enter in this
field, but the quotes are not received and they are not included in the total byte
count.

### **Additional package terminator** — Package terminator data `'E'` (default) | scalar

Specifies the data located at the end of the received data package, which is not
part of the data being received, and generally indicates end of data. The additional
package terminator must be an ASCII value. You can use a text value or a numeric value
in the range (0–255). You must put single quotes around text entered in this field, but
the quotes are not received and they are not included in the total byte count.

### **Data type** — Output data type `single` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

Specifies the data type of the block output.

### **Data size** — Output data size `1` (default) | scalar | matrix

Specifies the output data size or the number of values that should be read at every
simulation time step.

### **Initial output** — Default block output value `0` (default) | scalar

Specifies the initial or default output value of the block. This value is used, for
example, if a connection timeout occurs and the **Action taken when connection
times out** parameter is set to `Output the last received
value`, but the block has not received any value yet.

### **Action taken when connection times out** — Action taken by block when connection times out `Output the last received value` (default) | `Output custom value` | `Error`

Specifies what to output if a connection timeout occurs.

- `Output the last received value` — The block outputs
  the value received at the preceding time step. If the block did not receive a value
  previously, it outputs the value of the **Initial output**
  parameter.
- `Output custom value` — The block outputs a
  user-defined value. Use the **Output value when connection times
  out** parameter to define this custom value.
- `Error` — The block outputs an error.

### **Output value when connection times out** — Output custom value when the connection times out `0` (default) | scalar

Specifies a custom value that the block outputs when a connection timeout
occurs.

#### Dependencies

To enable this parameter, set **Action taken when connection times
out** to either `Output custom value` or
`Error`.

### **Sample time** — Sample time for block execution `-1` (default) | scalar

Determines how often the Host Serial Receive block is called (in
seconds). When you set this value to `-1`, the model inherits the
sample time of the model. To execute this block asynchronously, set **Sample
time** to `-1`.

### **Output receiving status** — Enable status output port `off` (default) | `on`

Select this parameter to enable the **status** output port that
provides the status of the transaction. If you clear this parameter, the block hides the
**status** port.

### **Enable blocking mode** — Block simulation while receiving data `on` (default) | `off`

Select this parameter to block the simulation while receiving data. Clear this
parameter if you do not want the read operation to block the simulation.

If you enable the blocking mode, the model blocks the simulation while it is waiting
to receive the requested data. When you do not enable the blocking mode, the simulation
runs continuously.

## Libraries

Motor Control Blockset / Protection and Diagnostics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Configure host-side serial communications interface to receive data from serial port

The Host Serial Receive block specifies the configuration of the data that
it receives from the target hardware.

The data package that the block receives is limited to 16 bytes of ASCII characters,
including package headers and terminators. Calculate the size of a package by including the
package header, or terminator, or both, and the data size. This table shows the number of
bytes in each data type.

| Data Type | Byte Count |
| --- | --- |
| `single` | 4 bytes |
| `int8` and `uint8` | 1 byte |
| `int16` and `uint16` | 2 bytes |
| `int32` and `uint32` | 4 bytes |

For example, if your data package has a package header 'S' (1 byte) and package terminator
'E' (1 byte), that leaves 14 bytes for the actual data. If your data is of type
`int8`, there is space in the data package for 14
`int8`s. If your data is of type `uint16`, there is
space in the data package for 7 `uint16`s. If your data is of type
`int32`, there is space in the data package for only 3
`int32`s, with 2 bytes left over. Even though you could fit two
`int8`s or one `uint16` in the remaining space, you
should not, because you cannot mix data types in the same package.

The number of data types that can fit into a data package determine the data size. In the
preceding example, the data size is 14 for `int8` and 7 for
`uint16`. When the data size exceeds 16 bytes, unexpected behavior,
including run-time errors, are likely to occur.
