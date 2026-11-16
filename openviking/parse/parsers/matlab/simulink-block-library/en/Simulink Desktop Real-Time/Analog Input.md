---
type: simulink-block
title: 'Analog Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'analoginput'
documentation_source_path: 'ref/analoginput.html'
language: en
---

# Analog Input

## Ports

### Output

### **Analog Data** — Analog-to-digital converter data read from input channels vector

Result of A/D conversion of an analog signal. The data type
and range of the output value depend on the capabilities of the board.

**Data Types:** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

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

### **Input channels** — Select analog input channels `1` (default) | vector

Enter a channel vector that selects the analog
input channels that you are using on this board. The vector can be
any valid MATLAB® vector
form. For example, to select eight contiguous analog input channels,
enter:

```
[1,2,3,4,5,6,7,8]
```

or

```
[1:8]
```

To select the first three analog input channels, enter:

```
[1,2,3]
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Channels` |

### **Input range** — Input range of analog inputs board dependent

From the list, select the input range for the analog input channels that you entered for the
**Input channels** parameter. For example, if the board
has an input range of `±5 V`, select `-5
to 5 V`.

If you want a different input range for different analog channels, add an I/O block for each
different input range. The valid values depend upon the capabilities of the
board.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VoltRange` |

### **Block output signal** — Value type returned from block `Volts` (default) | `Normalized bipolar` | `Normalized unipolar` | `Raw`

From the list, select from the following options:

- `Volts` — Returns
  a value equal to the analog voltage.
- `Normalized bipolar` —
  Returns a full range value of -`1` to `+1` regardless
  of the input voltage range.
- `Normalized unipolar` —
  Returns a full range value of `0` to `+1` regardless
  of the input voltage range. For example, analog input ranges of `0` volts
  to `+5` volts and of `−5` volts
  to `+5` volts are converted to `0` to `+1`.
- `Raw` — Returns a
  value from `0` through `2n -1`.
  For example, a 12-bit A/D converter returns values from `0` through `212 -1` (`0` to `4095`).
  The advantage of this method is that the returned value is an integer
  with no round-off errors.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RangeMode` |

### **Output data type** — Data type of block output `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

From the list, select the type of data that the block outputs to the model. The valid values
depend on the capabilities of the board.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |

## Libraries

Simulink Desktop Real-Time

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2024b: Update to blocks with port names

In R2024b, when you enable optional ports, such as **Show "Missed Ticks"
port**, these Simulink
Desktop Real-Time™ block ports appear with labels.

## Description

Read from one or multiple analog input channels

The Analog Input block connects to and reads from specific analog input
channels from your Simulink® model. After you add an Analog Input block to your model,
you can enter the parameters for its I/O driver.
