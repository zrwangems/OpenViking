---
type: simulink-block
title: 'C28x SCI Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xscireceive'
documentation_source_path: 'ref/c28xscireceive.html'
language: en
---

# C28x SCI Receive

## Ports

### Input

### **Length** — Data length received from input port scalar

The block accepts the length of the data to be received.

#### Dependencies

To enable this port, set the **Data length
option** parameter to `Length via input
port`.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Data** — Data received from serial bus scalar | vector

The data received from the serial communication bus.

- The data port is configured as **fixed size
  signal** when data length is set to `Length
  via dialog`. It outputs only received data.
- The data port is configured as **variable size
  signal** when data length is set to `Length
  via Input port` or `Variable
  Length`. In this case the port outputs received
  data along with the length of the received data.

  When **Data length** is set as
  `Variable Length` or `Length via
  input port` the output data width is
  `0` if the data is not received. This is
  independent of connection output type set for **Action
  taken when connection times out** parameter.

  In order to generate code for variable size signals, go to **Configuration Parameters** > **Code Generation** > **Interface** and select **Variable-size
  signals**. For more information, see

  - Variable-Size Signal Basics
  - Variable-Size Signal Length Adaptation

**Note**

Currently, Monitor & Tune (External mode) is not supported to
output the variable size signal.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single`

### **status** — Status of serial communication scalar

Indicates the status of the received serial data:

- `0` - No errors.
- `1` - A time-out occurred while the block
  was waiting to receive data. This is the default status if
  expected header is not received.
- `2` - The received data contains an error
  (checksum error) or if the required tail is not
  received.
- `3` - SCI parity error flag: occurs when
  a character is received with a mismatch.
- `4` - SCI framing error flag: occurs when
  an expected stop bit is not found.
- `5` - SCI overrun error flag: occurs when
  a character is transferred to the receive registers before
  reading the previous character.
- `6` - SCI break-detect flag: occurs when
  SCI receiver data line (SCIRXD) remains continuously low for
  at least ten bits.
- `7` - Data not available flag: occurs in
  non-blocking mode when data is not available in the FIFO.
  The status is Data not available when the data length is set
  to **Variable length** after receiving the
  header, and if data is not available in the FIFO to read as
  a data or terminator.
- `8` - Partial Data available: Partial
  data status represents the data received partially excluding
  header. The status is set to **Partial
  Data** when the data length is set to
  `Variable length`, and if the
  terminator is expected to be received and when not received
  up to the `Max data length`.

#### Dependencies

This port appears only when you select **Output receiving
status**.

**Data Types:** `uint16`

## Parameters

### **SCI module** — SCI module for communication `A` (default) | `B` | `C` | `D`

The SCI module used for communication. The number of SCI modules supported
varies across different C2000™ processors.

### **Additional package header** — Indicates start of data `'S'` (default) | string | char | number from 0 to 255

The data located at the front of the received data package, which is not
part of the data being received, and indicates the start of data. The
additional package header must be represented using ASCII characters. You
can use a string or a number (0–255). You must add single quotes around
strings entered for this parameter, but the quotes are not received or
included in the total byte count. To specify a null value (no package
header), enter two single quotes only.

The data type of header is not related to the data type mentioned on the
block.

**Note**

- Match additional package headers or terminators with those
  specified in the host SCI Transmit
  block.
- If header is empty then whatever present in the receive
  buffer will be considered as starting point to receive. In
  case of data length option as Variable length, the tail will
  be calculated from this starting point itself if header is
  empty.
- If the expected header is not provided on the block then
  the data present in the FIFO is considered as a starting
  point of reception and from that point onwards required
  length of the data and terminal will be expected to
  retrieve.

### **Additional package terminator** — Indicates end of data `'E'` (default) | string | char | number from 0 to 255

The data located at the end of the received data package, which is not
part of the data being received, and indicates the end of data. The
additional package terminator must be represented using ASCII characters.
Use a string or a number (0–255). You must add single quotes around strings
entered for this parameter, but the quotes are not received or included in
the total byte count. To specify a null value (no package terminator), enter
two single quotes only.

The data type of terminator is not related to the data type mentioned on
the block.

### **Number of retries for header receive check** — Custom retrial count for header receive check `16` (default) | `positive integer, finite` | `scalar`

This parameter ensures to check the expected header as part of receive
data.

When the data is received in the FIFO, the block verifies for the header
in the received data one by one. If the data does not match with the header,
the block will discard the data and continue looking for the header in the
next data until the retry count expires.

If the header matches within the retry count, then it is considered as
start of the packet and the further received data is considered as valid
data.

### **Data type** — Data type of output data `uint8` (default) | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32`

The data type of the output data.

If data is transmitted as `uint8` but SCI receive block
output is expected to be `int16/int32` then it is assumed
that even number of bytes are present and that the output is formatted in
different data type. In case if there are odd number of data bytes are
present then last byte will be missed in the formatting even if the status
is showing **No Error**.

### **Data length option** — Data length the block receives `Length via dialog` (default) | `Length via input port` | `Variable length`

Select the data length option for the block.

- `Length via dialog` - Length of the data to
  be received is provided via `Data length`
  parameter.
- `Length via input port` - the block receives
  variable size data depending on the length received at the input
  port. If the length received at the input port is greater than
  the length provided in the maximum data length parameter, then
  maximum data length is considered.
- `Variable length` - The data is received
  until the tail matches in non-blocking mode. Ensure that the
  tail is not present as a part of data. When only header and
  terminator is available and data is not available then the
  status is set to **No Error** with variable
  data length set to zero.

  - If terminator value does not match till maximum length
    or if the data is not available in between then the
    block will output the received data along with its
    length and status will be set to `Partial data
    available`.
  - If terminator value is not provided the block tries to
    receive data of **max data length**. If
    length of the data read is less than max length or if
    the data is not available in between then the block will
    output received data with its length and status will be
    set to `Partial data available`.
  - If data is not read then status is set to
    **Data not available**.
  - The status is read as data not available when Header
    and terminator received with no data.
  - Tail to be avoided as part of SCI Data when using in
    variable length as presence of Tail is treated as end of
    Data Packet.
  - Output data port length is 0 if no data is received in
    variable length mode.

To enable input port **length**, select data length
option as `Length via input port`.

### **Data length** — Number of data types the block receives `1` (default) | `positive integer, finite` | `scalar`

The number of **Data type** the block receives (not
bytes). If this parameter is set to more than `1`, the
output will be a vector. Ensure that the data length specified is same as
that of the SCI Transmit block from which data is
received.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to `Length via
dialog`.

### **Max data length** — Maximum number of data types the block receives `1` (default) | positive integer, finite | `positive integer, finite`

The maximum number of **Data type** the block can receive
(not bytes).

If the data size to be received (based on data length or max data length,
header, terminator and data type) is greater than FIFO size bytes then it
will result in loss of data.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via input
port` or `Variable length`.

### **Initial output** — Default value output from block `0` (default) | scalar | vector

The default value output from the SCI Receive block. This
value is output, for example,when the **Action taken when connection
timeout** parameter is set to `Output the last
received value` and a connection time-out occurs before
data is received.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via input
port` or `Length via dialog`.

### **Action taken when connection times out** — Select type of output when connection times out `Output the last received value` (default) | `Output custom value`

Specifies what to output when a connection time out occurs. If
`Output the last received value` is selected,
the block outputs the last received value. If a value has not been received,
the block outputs the **Initial output** value.

If you select `Output custom value`, use the
**Output value when connection times out** parameter to
set the custom value.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via input
port` or `Length via dialog`.

### **Output value when connection times out** — Custom output value from block when connection times out `0` (default) | scalar | vector

Set the custom time out value.

**Output value when connection times out** parameter is
available only when **Action taken when connection times
out** parameter is set to `Output custom
value`.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via input
port` or `Length via dialog`.

### **Sample time** — Frequency at which data is read from SCI device `0.1` (default) | `-1` | scalar

Sample time for the block in seconds. To execute this block
asynchronously, set this parameter to `-1`.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via
dialog` or `Variable length`.

The sample time will inherit properties from input port when data
length option is set to `Length via input port`.

### **Wait until data received** — Wait until requested data is available `off` (default) | `on`

- `on` — If this option is enabled, the
  system waits until data is available to read (when data length is
  reached). The read operation runs in the blocking mode. The read
  operation is blocked when the block is waiting for the requested
  data. If data is available, the block outputs the data. If data is
  not available, the block waits for the data.

  A task overrun occurs if the target hardware is still waiting for
  the data when the next read operation begins.

  To fix overruns, increase the time step by using the
  **Sample time** parameter.
- `off` — If this option is disabled, the
  system checks FIFO at each time step (in polling mode) for data to
  read. If data is present, the block reads and outputs the contents.
  If data is not present, the block outputs the last value and
  continues. When you clear this parameter, the read operation runs in
  the nonblocking mode.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via input
port` or `Length via dialog`.

**Note**

When data length option is selected as **Variable
length**, the block execution will always occurs in
non-blocking mode.

### **Timeout** — Amount of time in seconds the block waits until data is received `inf` (default) | `positive value greater than 0`

Specify the amount of time that the block should wait during each time
step if the data is not available in the receive FIFO to read. If timeout
occurs, the read operation is aborted.

If the value is set to `inf` the block waits infinitely
for data to be available in FIFO.

**Note**

3 types of mode can be achieved with parameters **Wait
until data received** and **Timeout**.

- **Blocking mode** - In blocking mode,
  parameters **Wait until data received**
  is enabled and **Timeout** set to
  `inf`.

  In this mode, if data is not available in FIFO to
  read, it will wait for infinite time until the data is
  available to read.
- **Blocking mode with Timeout** - In
  blocking mode with timeout, parameters **Wait
  until data received** is enabled and
  **Timeout** set to `any
  finite value > 0`.

  In this mode if data is not available in FIFO to read,
  it will wait checking the FIFO status until the timeout
  value mentioned. If data is not available in FIFO to
  read within that time then the SCI Receive block will
  output status as `timeout`.
- **Non-Blocking mode** - In
  Non-Blocking mode, parameter **Wait until data
  received** is disabled.

  In this mode the SCI Receive block will read the data
  if the data is available in FIFO else the SCI Receive
  block will output status as `Data not
  available`.
- In order to receive data of length more than FIFO
  length use either blocking mode or blocking mode with
  timeout. This ensures of extra time to get remaining
  data in FIFO after reading entire FIFO. You might
  encounter data loss, if you try to receive data greater
  than the FIFO length in Non-Blocking mode.

  In blocking mode with and without timeout enabled, you
  might encounter task overrun as it waits for the data to
  read.

#### Dependencies

To enable this parameter, set the **Data length
option** parameter to either `Length via input
port` or `Length via dialog` and enable
the parameter `Wait until data received`.

### **Output receiving status** — Status of serial communication `off` (default) | `on`

Creates a **Status** block output that provides the
status of serial communication.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Receive data on target via serial communication interface (SCI) from host

The SCI Receive block supports asynchronous serial digital
communication between the processor and other asynchronous peripherals. This block
receives scalar or vector data using the specified SCI hardware module.

A model can only contain one SCI Receive block for each module. The
C28x processor has four SCI modules — A, B, C, and D. The number of SCI modules
available varies depending on the processor selected. You can configure the SCI modules
by navigating to **Hardware Implementation** > **Target hardware resources**. Verify that these settings meet the requirements of your
application.

**Note**

Serial External mode with similar SCI module blocks results in conflict check
error.

The block outputs data either in blocking mode or in non-blocking mode. In blocking
mode, the model blocks the execution while it waits for the requested data to be
available. In non-blocking mode, the model runs continuously. To set the block in
blocking mode, select the **Wait until data received** option.
