---
type: simulink-block
title: 'Counter Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'counterinput'
documentation_source_path: 'ref/counterinput.html'
language: en
---

# Counter Input

## Ports

### Output

### **Counter Data** — Counter data read from input channels vector

Data representing the state of a counter. The data type of the
output values depends upon the capabilities of the board.

**Data Types:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

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

### **Input channels** — Select counter-input channels `1` (default) | vector

Enter a channel vector that selects the counter
input channels you are using on this board. The vector can be any
valid MATLAB® vector form.

For example, to select the first four counter-input channels
on the board, enter:

```
[1,2,3,4]
```

or

```
[1:4]
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Channels` |

### **Reset after read** — Counter-reset policy `never` (default) | `always` | `level` | `rising edge` | `falling edge` | `either edge`

Determines whether the software resets the counter to zero after reading
its value. From the list, select one of the following options:

- `never` —
  Do not reset after reading.
- `always` —
  Always reset after reading.
- `level` — Reset after
  reading if the block input is nonzero. Adds an input to the Counter
  Input block.
- `rising edge` — Reset
  after reading if the block input changes from zero to nonzero between
  the last two successive readings. Adds an input to the Counter
  Input block.
- `falling edge` — Reset
  after reading if the block input changes from nonzero to zero between
  last two successive readings. Adds an input to the Counter
  Input block.
- `either edge` — Reset
  after reading if the block input changes either from zero to nonzero
  or from nonzero to zero between the last two successive readings.
  Adds an input to the Counter Input block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ResetMode` |

### **Clock input source** — Clock input that increments counter `input pin rising edge` (default) | `input pin falling edge` | `internal clock`

Determines the clock input source to increment
the counter. From the list, select:

- `input pin rising edge` —
  Clock edge low-to-high transitions
- `input pin falling edge` —
  Clock edge high-to-low transitions
- `internal clock` —
  Internal time base

  If you set the **Gate input functionality** parameter
  to `enable when high, latch & reset on edge`,
  or `enable when low, latch & reset on edge`,
  you can measure positive or negative pulse lengths in units of the
  internal time base. You can use this combination with National Instruments™ drivers
  for pulse width measurement.

Not all counter chips
support selecting the input edge. In this case, only supported options
appear in the list.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CounterEdge` |

### **Gate input functionality** — Action of counter-gate input pin `none` (default) | `enable when high` | `enable when low` | `start on rising edge` | `start on falling edge` | `reset on rising edge` | `reset on falling edge` | `latch on rising edge` | `latch on falling edge` | `latch & reset on rising edge` | `latch & reset on falling edge` | `enable when high, latch & reset on edge` | `enable when low, latch & reset on edge`

Defines the action of the counter gate input
pin. From the list, select:

- `none` —
  Enable counting unconditionally, ignoring gate input.
- `enable when high` —
  Disable counting when gate input is low and enable counting when gate
  input is high.
- `enable when low`  —
  Disable counting when gate input is high and enable counting when
  gate input is low.
- `start on rising edge` —
  Disable counting until low-to-high gate transition occurs.
- `start on falling edge` —
  Disable counting until high-to-low gate transition occurs.
- `reset on rising edge` —
  Reset counter to zero when low-to-high gate transition occurs.
- `reset on falling edge` —
  Reset counter to zero when high-to-low gate transition occurs.
- `latch on rising edge` —
  Store count in register when low-to-high gate transition occurs. Return
  contents of register.
- `latch on falling edge` —
  Store count in register when high-to-low gate transition occurs. Return
  contents of register.
- `latch & reset on rising edge` —
  Store count in register, and then reset counter to zero when low-to-high
  gate transition occurs. Return contents of register.
- `latch & reset on falling edge` —
  Store count in register, and then reset counter to zero when high-to-low
  gate transition occurs. Return contents of register.
- `enable when high, latch & reset on
  edge` — Disable counting while gate input is low.
  Start counting when low-to-high gate transition occurs. Count while
  gate input is high. Store count in register, and then reset counter
  to zero when high-to-low gate transition occurs. Return contents of
  register.

  If you set the **Clock input source** parameter
  to `internal clock`, you can measure positive
  pulse lengths in units of the internal time base. You can use this
  combination with most National Instruments drivers for pulse width
  measurement.
- `enable when low, latch & reset on
  edge` — Disable counting while gate input is high.
  Start counting when high-to-low gate transition occurs. Count while
  gate input is low. Store count in register, and then reset counter
  to zero when low-to-high gate transition occurs. Return contents of
  register.

  If you set the **Clock input source** parameter
  to `internal clock`, you can measure negative
  pulse lengths in units of the internal time base. You can use this
  combination with National Instruments drivers for pulse width
  measurement.

Not all counter chips
support all gate input modes.
Only supported modes appear in the list.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CounterGate` |

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

Read from one or multiple counter-input channels

The Counter Input block connects to and reads from specific counter-input
channels into your Simulink® model. After you have added a Counter Input block to your
model, you can enter the parameters for its I/O driver.
