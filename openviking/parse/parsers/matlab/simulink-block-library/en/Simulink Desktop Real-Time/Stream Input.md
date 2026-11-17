---
type: simulink-block
title: 'Stream Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'streaminput'
documentation_source_path: 'ref/streaminput.html'
language: en
---

# Stream Input

## Ports
```yaml
ports:
- name: Output Data
  summary: Data received from communication channel numeric vector | string
  direction: output
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

### Output

### **Output Data** — Data received from communication channel numeric vector | string

Data values that were received from the communication channel
as formatted ASCII data and decoded according to **Format
string**.

### **Data Ready** — Data ready port (optional) `1` | `0`

This port signals `1` if the block has new
data available and `0` otherwise.

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
- name: Block output data types
  summary: Output type and grouping of data sent to the block outputs 'double' (default) | character vector | cell array of
    character vector
  group: ''
  block_parameter: DataTypes
- name: Format string
  summary: Format of data items being read from the stream '%f' (default) | character vector
  group: ''
  block_parameter: FormatString
- name: Message termination
  summary: Specify end of message {'\r', '\n'} (default) | character vector | cell array of character vector | integer
  group: ''
  block_parameter: Terminator
- name: Show “Data Ready” port
  summary: Add port Data Ready that signals 1 when data is available 'off' (default) | 'on'
  group: ''
  block_parameter: ShowReady
- name: Show “Data Error” port
  summary: Add port Data Error that signals 1 if error occurs 'off' (default) | 'on'
  group: ''
  block_parameter: ShowError
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

### **Block output data types** — Output type and grouping of data sent to the block outputs `'double'` (default) | character vector | cell array of character vector

A character vector or a cell array of character vectors. The
block has as many output ports as the number of character vectors.
Each vector specifies a data type by name, and optionally the number
of items of that data type in an output vector. For example, `'double'` means
one `double` value, and `'4*int8'` means
four `int8` values.

The values made available on output ports are grouped and typed
according to the **Block output data types** character
vectors. For example, if **Block output data types** is `{'2*int8','3*double'}`,
the block outputs:

- On output port `1` — an `int8` vector
  of width `2`
- On output port `2` — a `double` vector
  of width `3`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataTypes` |

### **Format string** — Format of data items being read from the stream `'%f'` (default) | character vector

A specification in the same format used by C library I/O routines like
`scanf`. The format string describes the data to be
received. The number of elements in the format string must equal the number
of data items specified in **Block output data types**. If
the specifier is `%s` or `%c` for string,
the created output port of type string only produces string signals. The
`Block output data types` parameter value for this
output port must be `"1"`, because strings can only be
scalars.

For example, assume that **Block output data types** is `{'2*int8','3*double'}` and **Format
string** is `'%d %d %f %f %f'`. The block
reads an ASCII representation of two integers and three doubles. The
block makes the resulting values available to the application on:

- Output port `1` — an `int8` vector
  of width `2`
- Output port `2` — a `double` vector
  of width `3`

If the data type specified for a value in **Block output
data types** differs from the type of the corresponding element
in **Format string**, type conversion occurs. The
block reads data as specified by **Format string**,
converts the data to match the **Block output data types**,
and provides the data to the application on the block output ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FormatString` |

### **Message termination** — Specify end of message `{'\r', '\n'}` (default) | character vector | cell array of character vector | integer

A character vector, cell array of character vectors, or a number.
If the value is a character vector, receiving this sequence of characters
terminates data input. If the value is a cell array, any
character vector in the cell array terminates data input. If the value
is a number, data input terminates after reading the specified number
of characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Terminator` |

### **Show “Data Ready” port** — Add port `Data Ready` that signals `1` when data is available `'off'` (default) | `'on'`

When you select this check box, the block makes visible the
output port `Data Ready`. This port signals `1` when
the block has new data available and `0` otherwise.

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

Read formatted ASCII data from communication channel

The Stream Input block reads formatted ASCII data from a port or file. After
you have added a Stream Input block to your model, double-click the
Stream Input block to open the Block Parameters: Stream Input dialog
box.

The driver must be one of:

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**

Specify parameter values as required, then click **OK** or **Apply**.
When you install a UDP device, enter port addresses in decimal format
in the Standard Devices UDP Protocol dialog box.
