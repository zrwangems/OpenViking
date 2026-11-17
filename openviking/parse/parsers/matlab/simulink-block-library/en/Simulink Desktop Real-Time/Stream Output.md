---
type: simulink-block
title: 'Stream Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'streamoutput'
documentation_source_path: 'ref/streamoutput.html'
language: en
---

# Stream Output

## Ports
```yaml
ports:
- name: Input Data
  summary: Data to write to communication channel numeric vector | string
  direction: input
- name: Data Ready
  summary: Data ready port (optional) 1 | 0
  direction: output
- name: Data Error
  summary: Data error port (optional) 1 | 0
  direction: output
- name: Missed Ticks
  summary: Missed tick count (optional) double
  direction: output
  data_types: double
```

### Input

### **Input Data** — Data to write to communication channel numeric vector | string

Data values that are sent to the communication channel as ASCII data,
encoded according to **Format string**.
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
```yaml
parameters:
- name: Install new board
  summary: Register a board < no board selected > (default)
  group: ''
  block_parameter: DrvName
- name: Delete current board
  summary: Delete the current board (button)
  group: ''
  block_parameter: DrvName
- name: Board setup
  summary: Set up the board (button)
  group: ''
  block_parameter: DrvOptions
- name: Sample time
  summary: Sample time of block 0.1 (default) | double
  group: ''
  block_parameter: SampleTime
- name: Maximum missed ticks
  summary: Number of timer ticks by which your model can trail the kernel 10 (default) | integer
  group: ''
  block_parameter: MaxMissedTicks
- name: Show “Missed Ticks” port
  summary: Send number of missed ticks to port Missed Ticks 'off' (default) | 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: Yield CPU when waiting
  summary: Yield CPU while kernel waits for hardware 'off' (default) | 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: Input port sizes
  summary: Specify number and width of ports 1 (default) | vector
  group: ''
  block_parameter: PortSizes
- name: Format string
  summary: Format of data items being written to the stream '%g' (default) | character vector
  group: ''
  block_parameter: FormatString
- name: Show “Data Ready” port
  summary: Add port Data Ready that signals 1 when the block can accept new data 'off' (default) | 'on'
  group: ''
  block_parameter: ShowReady
- name: Show “Data Error” port
  summary: Add port Data Error that signals 1 if error occurs 'off' (default) | 'on'
  group: ''
  block_parameter: ShowError
- name: Initial string
  summary: Data to send when simulation begins character vector
  group: ''
  block_parameter: InitialValue
- name: Final string
  summary: Data to send when simulation ends character vector
  group: ''
  block_parameter: FinalValue
```

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

### **Input port sizes** — Specify number and width of ports `1` (default) | vector

Enter a port width, or vector of port widths. The number of elements
determines the number of input ports. Each port has the width specified by
the corresponding element. For example, specifying
`[3,1,2]` indicates that the block has three input
ports: a vector of width `3`, a scalar, and a vector of
width `2`, for a total of six elements. You specify only
the widths.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortSizes` |

### **Format string** — Format of data items being written to the stream `'%g'` (default) | character vector

Enter a specification in the same format used by C library I/O routines
like `printf`. The format string describes the data to be
sent. The format string must have the same number of specifiers as the sum
of the elements of **Input port sizes**. If the
specifier is `%s` or `%c` for string, the
created input port of type string only accepts string signals. The
`Input port sizes` parameter value for this input port
must be `"1"`, because strings can only be scalars.

For example, assume that **Input port sizes** is
`[3,1,2]`. Then a **Format string** of
`'%d %d %d %f %d %d'` outputs ASCII
representing:

- Three integers from the vector on the first input port
- One double from the scalar on the input second port
- Two integers from the vector on the third input port

If the data type specified in the **Format string** for a
value differs from the type of the actual value, type conversion occurs.
Converted data that conforms to the **Format string** is
output as ASCII to the device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FormatString` |

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

### **Initial string** — Data to send when simulation begins character vector

Optional. Enter a character vector. When simulation begins, send the
specified data before the other data that is sent during simulation.

The character vector can contain anything. You can use it to initialize a
device. It is sent literally as specified, without reference to
**Format string**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialValue` |

### **Final string** — Data to send when simulation ends character vector

Optional. Enter a character vector. When simulation ends, after the other
data that is sent during simulation, send the specified data.

The character vector can contain anything. You can use it to shut down a
device. It is sent literally as specified, without reference to
**Format string**

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

### R2019b: Stream Input and Stream Output Blocks Support String Signals

The Stream Input block and Stream Output block
support Simulink string signals.

### R2019a: RS-232 Serial Port Drivers Support for macOS

The serial port drivers for the Packet Input block, Packet
Output block, Stream Input block, and Stream
Output block support macOS systems. In previous releases, the serial port drivers for these
blocks supported Windows® systems only.

### R2018a: TCP and UDP Protocol Support for Stream Input and Stream Output

The TCP protocol and UDP protocol drivers for the Stream Input
block and Stream Output block are available from the Standard Devices
list. From the Install new board button, select **Standard Devices** > **TCP Protocol** or select **Standard Devices** > **UDP Protocol**.

## Description

Write formatted ASCII data to communication channel

The Stream Output block writes formatted ASCII data to a port or file.
After you have added a Stream Output block to your model, double-click
the Stream Output block to open the Block Parameters: Stream Output
dialog box.

The driver must be one of:

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**

When you install a UDP device, enter port addresses in decimal format in the Standard
Devices UDP Protocol dialog box.

Any serial output port
can send data with sample rates up to 500 Hz. To enable a faster sample
rate of up to 10 kHz for some output serial ports, click **Install
new board**, select **Standard Devices** > **Serial Port**, and select **Direct
port access**.

The block does not support this option with all
types of serial output hardware.
