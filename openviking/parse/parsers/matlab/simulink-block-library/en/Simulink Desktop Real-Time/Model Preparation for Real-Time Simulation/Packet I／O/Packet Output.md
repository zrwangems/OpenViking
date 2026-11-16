---
type: simulink-block
title: 'Packet Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Simulation / Packet I/O'
documentation_page: 'packetoutput'
documentation_source_path: 'ref/packetoutput.html'
language: en
---

# Packet Output

## Ports

### Input

### **Input Data** — Data to write to communication channel vector

Data values that are sent to communication channel as unformatted binary data. For CAN or
Virtual CAN devices, this port supports:

- `CAN_MESSAGE` datatype
- `CAN_MESSAGE_BUS` datatype
- `CAN_FD_MESSAGE_BUS` datatype in CAN FD
  mode

**Data Types:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### Output

### **Data Ready** — Data ready port (optional) `1` | `0`

This port signals `1` if the block is ready
to accept new data and `0` otherwise.

#### Dependency

When you select **Show “Data Ready” port**,
this port is visible.

### **Data Error** — Data error port (optional) `1` | `0`

This port signals `1` if a data error occurs
and `0` otherwise.

#### Dependency

When you select **Show “Data Error” port**,
this port is visible.

### **Missed Ticks** — Missed tick count (optional) double

In **Connected IO** mode, returns the number of timer ticks that your model
lags behind the real-time kernel. When the model lags by more than **Maximum missed
ticks**, the software reports an error and simulation stops.

#### Dependency

When you select **Show “Missed Ticks”
port**, this port is visible.

**Data Types:** `double`

## Parameters

### **Install new board** — Register a board `< no board selected >` (default)

When you click **Install new board**, the software
displays a list of manufacturers of supported boards. When you select
a manufacturer, the software displays a list of boards available from
that manufacturer. When you select a board, the software adds the
board to the list of registered boards and makes that board the current
board.

By default, the initial selection in the list of registered boards is `<
no board selected >`.

For more information about driver support for I/O boards, see Hardware Support from Simulink Desktop Real-Time.

#### Dependency

When you select a board in the list of registered boards, the **Delete
current board** and **Board setup** buttons
are available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvName` |

### **Delete current board** — Delete the current board (button)

To delete the current board, click this button. The initial
selection of the list of registered boards changes to `<
no board selected >`.

#### Dependency

To activate this parameter, select a board in the list of registered
boards.

When you delete the current board, the **Delete current
board** and **Board setup** buttons are
no longer available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvName` |

### **Board setup** — Set up the board (button)

To set up the board, click this button.

A board-specific dialog box opens to set up the board. For more
information, see the board manufacturer documentation.

#### Dependency

To activate this parameter, select a board in the list of registered
boards.

To deactivate this parameter, click **Delete current
board**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvAddress` |
| **Block Parameter:** `DrvOptions` |

### **Sample time** — Sample time of block `0.1` (default) | double

Enter a value, in seconds, that represents how frequently you
want the block to execute and interact with the I/O hardware. The
block synchronizes your model with the real-time clock at this sample
rate.

If you are using a fixed-step solver, enter the value that you entered as the **Fixed
step size** configuration parameter or an integer multiple of that
value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |

### **Maximum missed ticks** — Number of timer ticks by which your model can trail the kernel `10` (default) | integer

In **Connected IO** mode, enter the number of timer ticks that your model can
lag behind the real-time kernel. When the model lags behind by this number or fewer timer
ticks, the software assumes that the lag is temporary. It allows the model to catch up, even
if the model misses some ticks. When the model lags by more than this number, the software
reports an error and simulation stops.

In **Run in Kernel** mode, the software ignores this value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — Send number of missed ticks to port `Missed Ticks` `'off'` (default) | `'on'`

In **Connected IO** mode, select this check box to send the number of missed
ticks to output port `Missed Ticks`.

In **Run in Kernel** mode, the `Missed Ticks` port is
zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowMissedTicks` |

### **Yield CPU when waiting** — Yield CPU while kernel waits for hardware `'off'` (default) | `'on'`

In **Connected IO** mode, select this check box to grant other programs more
CPU time while the kernel waits for a response from the hardware.

In **Run in Kernel** mode, the software ignores this value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `YieldWhenWaiting` |

### **Packet identifier** — Identifier of the packet `1` (default) | vector

Enter the ID of the packet to process. If your protocol does
not have packet IDs, this parameter is disabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PacketID` |

### **Extended identifier** — Extended identifier of the packet (CAN boards only) `'off'` (default) | `'on'`

Select this check box if **Packet identifier** is
an extended identifier.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PacketID` |

### **Output packet size** — Number of bytes that each input packet contains `32` (default) | integer

Enter the number of bytes expected in each input packet. This
number must match the number of bytes required by the type specifications
in **Output packet data types**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PacketSize` |

### **Output packet field data types** — Output type and grouping of data in the packet sent to the device `'4*double'` (default) | character vector | cell array of character vector

One or more character vectors that specify how data provided
by the application is formatted into a packet. The Packet Output block
has an input port corresponding to each character vector in **Output
packet field data types**. Changing the number of character
vectors changes the number of ports.

Each character vector has the format
[`n*`]`datatype`.
The data that the character vector describes has the type specified by
`datatype` and the width specified by
`n`. If `n` is not
specified, the width is `1`. For example, `'double'` means one
`double` value, and `'4*int8'` means a vector of four
`int8` values. You can also type `'CAN_MESSAGE'` to specify
a single `CAN_MESSAGE` value.

The signal input to each port of the Packet Output block
can be a scalar or vector of the data type. The character vector for
each port specifies the type to be used when its signal is output
to the device. If the character vector for a port matches the type
of the signal input to that port, the signal value appears verbatim
in the output packet.

You can also perform type conversion on output. For example,
assume that the input is a four-element `int16` vector
and the character vector is `'4*int8'`. The four
integers are converted to `int8` before being written
to the packet. The resulting data occupies 4 bytes in the output packet.

The block forces an out-of-range value to the maximum value
for that data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataTypes` |

### **Output packet field byte order** — Byte order of packet being sent to device `Little Endian` (default) | `Big Endian`

From the list, select:

- `Little Endian` (default)
  — Receive multibyte values in little-endian format.
- `Big Endian` — Receive
  multibyte values in big-endian format.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ByteOrder` |

### **Show “Data Ready” port** — Add port `Data Ready` that signals `1` when the block can accept new data `'off'` (default) | `'on'`

When you select this check box, the block makes visible the
output port `Data Ready`. This output port signals `1` when
the block is ready to accept new data and otherwise signals `0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowReady` |

### **Show “Data Error” port** — Add port `Data Error` that signals `1` if error occurs `'off'` (default) | `'on'`

When you select this check box, the block makes visible the
output port `Data Error`. This port signals `1` when
a data error occurs and `0` otherwise.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowError` |

### **Initial value** — Data to send when simulation begins vector

Optional. Enter a vector that has the same number of elements
as the sum of the widths of the input signals across all
ports. When simulation begins, send the specified data before the
other data that is sent during simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialValue` |

### **Final value** — Data to send when simulation ends vector

Optional. Enter a vector that has the same number of elements
as the sum of the widths of the input signals across all
ports. When simulation ends, after the other data that is sent during
simulation, send the specified data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FinalValue` |

## Libraries

Simulink Desktop Real-Time

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007b**

### R2024b: Update to blocks with port names

In R2024b, when you enable optional ports, such as **Show "Missed Ticks"
port**, these Simulink®
Desktop Real-Time™ block ports appear with labels.

### R2020b: CAN and CAN FD Message Bus Datatypes

For CAN or Virtual CAN devices, the Packet Input block and
Packet Output block provide support for the
`CAN_MESSAGE_BUS` datatype in CAN mode and support for the
`CAN_FD_MESSAGE_BUS` datatype in CAN FD mode.

### R2019b: Packet Input and Packet Output Blocks Support PEAK-System and Kvaser CAN Devices

The Packet Input block and Packet Output block
support PEAK-System and Kvaser CAN devices.

### R2019a: RS-232 Serial Port Drivers Support for macOS

The serial port drivers for the Packet Input block, Packet
Output block, Stream Input block, and Stream
Output block support macOS systems. In previous releases, the serial port drivers for these
blocks supported Windows® systems only.

## Description

Write binary data or a CAN message to a communication channel

The Packet Output block connects to and write unformatted binary data to a
port, file, or CAN device. After you add a Packet Output block to your
model, double-click the block to set its parameters.

The driver must be one of:

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**
- **Kvaser** > **CAN Device**
- **PEAK-System** > **CAN Device**
- **Vector** > **CAN Device**
- **MathWorks** > **virtual CAN** (requires Vehicle Network Toolbox™)

When you install a UDP device, enter port addresses in decimal
format in the Standard Devices UDP Protocol dialog box.

Any serial output port
can send data with sample rates up to 500 Hz. To enable a faster sample
rate of up to 10 kHz for some output serial ports, click **Install
new board**, select **Standard Devices** > **Serial Port**, and select **Direct
port access**.

The block does not support this option with all
types of serial output hardware.
