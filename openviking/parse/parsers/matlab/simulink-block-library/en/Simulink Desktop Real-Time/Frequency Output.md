---
type: simulink-block
title: 'Frequency Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'frequencyoutput'
documentation_source_path: 'ref/frequencyoutput.html'
language: en
---

# Frequency Output

## Ports

### Input

### **Frequency** — Frequency of output waveform (optional) vector

Frequency setting of waveform generator. The data type and range
of the input values depend upon the capabilities of the board.

#### Dependency

When you set **Output signal frequency source** to `external`,
this port is visible.

**Data Types:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Duty Cycle** — Duty cycle of output waveform (optional) vector

Duty cycle setting of waveform generator. The data type and
range of the input values depend upon the capabilities of the board.

#### Dependency

When you set **Output signal duty source** to `external`,
this port is visible.

**Data Types:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### Output

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

### **Output channels** — Select frequency output channels vector

Enter a channel vector that selects the frequency
output channels you are using on this board. The vector can be any
valid MATLAB® vector form. For example, to select the first eight
digital output channels, enter:

```
[1,2,3,4,5,6,7,8]
```

or

```
[1:8]
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Channels` |

### **Output signal frequency source** — Specify source of output frequency (Hz) `external` (default) | `internal`

Select the source that specifies the frequency to output, in
Hz. The **Output signal frequency source** can be
either of the following:

- `internal` — A tunable
  parameter named **Frequency** specifies the frequency.
- `external` (default) —
  A signal specifies the frequency. Input port `Frequency` appears
  on the block to accept the signal.

  You can specify additional settings for **Frequency
  initial value** and **Frequency final value**.

#### Dependency

If you specify `external` (the default),
port `Frequency` and the parameters **Frequency
initial value** and **Frequency final value** are
visible.

If you specify `internal`, **Frequency** replaces **Frequency
initial value** and **Frequency final value** is
disabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencySource` |

### **Frequency** — Specify the output frequency (Hz) scalar

This parameter replaces **Frequency initial value**.

#### Dependency

To make this parameter visible, set **Output signal
frequency source** to `internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Frequency` |

### **Frequency initial value** — Specify the frequency that the board generates before execution starts scalar

Optionally specify an initial frequency in hertz. When you connect
to the target, the specified frequency takes effect.
It persists until simulation starts, when the value of the frequency
signal takes effect. You
can use this parameter to specify initial conditions and give them
time to stabilize. If no
value appears, connecting to the target has no
effect on the frequency.

#### Dependency

To make this parameter visible, set **Output signal
frequency source** to `external`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Frequency` |

### **Frequency final value** — Specify the frequency that the board generates after execution ends scalar

Optionally specify a final frequency in hertz. When simulation
is complete, the specified frequency takes effect
and persists indefinitely. Disconnecting from the target does not
change the frequency. You can use this parameter to put a connected
device into a neutral state after simulation. If no
value appears, the frequency in effect
at the end of simulation persists afterward.

#### Dependency

To make this parameter visible, set **Output signal
frequency source** to `external`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencyFinalValue` |

### **Output signal duty source** — Specify source of output signal duty cycle `internal` (default) | `external`

Specify the source that determines the duty cycle. The **Output
signal duty source** can be either of the following:

- `internal` (default) —
  A tunable parameter named **Duty** specifies the
  duty cycle.
- `external` — A signal
  specifies the duty cycle. Input port `Duty Cycle` appears
  on the block to accept the signal.

#### Dependency

If you specify `internal` (the default), **Duty** is
visible. **Duty final value** is not visible.

If you specify `external`, port `Duty
Cycle` appears, parameter **Duty initial value** replaces **Duty**,
and parameter **Duty final value** is visible.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DutySource` |

### **Duty** — Specify the time during which the output signal is high `0.5` (default) | `0–1`

Specify the duty cycle as a decimal fraction from `0` through `1` inclusive.
It determines the amount of time that the output signal value is high
(`1`). For example, a duty cycle of `0.7` specifies
that the output is high 70% of the time and low 30% of the time.

Two duty cycle values have special significance:

- `0` — The output signal is
  continuously low (`0`) regardless of the frequency
  specification currently in effect.
- `1` — The output signal is
  continuously high (`1`) regardless of the frequency
  specification currently in effect.

#### Dependency

To make this parameter visible, set **Output signal
duty source** to `internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Duty` |

### **Duty initial value** — Specify the duty cycle of the board before execution starts `0–1`

Optionally specify an initial duty cycle. When you connect to
the target, the specified duty cycle takes effect.
It persists until simulation starts. If no
value appears, connecting to the target has no
effect on the duty cycle.
You can specify any duty
cycle. Often the **Duty initial value** is `0` or `1`,
enforcing a continuously low or high initial output signal. Specifying `0` or `1` overrides
any **Frequency
initial value** setting.

#### Dependency

To make this parameter visible, set **Output signal
duty source** to `external`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Duty` |

### **Duty final value** — Specify the duty cycle of the board after execution ends `0–1`

Optionally specify a final duty cycle. When simulation is complete,
the specified duty cycle takes effect
and persists indefinitely. Disconnecting from the target does not
change the duty cycle. If no
value appears, the duty cycle in effect
at the end of simulation persists indefinitely afterward. You can
specify any duty cycle.
Often the **Duty final value** is `0` or `1`,
enforcing a continuously low or high initial output signal. Specifying `0` or `1` overrides
any **Frequency
final value** setting.

#### Dependency

To make this parameter visible, set **Output signal
duty source** to `external`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DutyFinalValue` |

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

## Description

Write to one or multiple frequency or PWM output channels

The Frequency Output block generates and outputs a pulse-width-modulated square
wave to an analog output.

The square wave alternates between low (`0`)
and high (`1`) with a specified frequency and duty
cycle.

You specify the frequency in hertz (Hz).

You specify the duty cycle as a decimal fraction from `0` through `1` inclusive.
The duty cycle determines the amount of time that the output signal
value is high (`1`).

After you have added a Frequency Output block
to your model, double-click the Frequency Output block
to open the Block Parameters: Frequency Output dialog box.
