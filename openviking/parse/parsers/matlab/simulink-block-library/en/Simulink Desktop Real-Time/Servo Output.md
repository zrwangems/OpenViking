---
type: simulink-block
title: 'Servo Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'servooutput'
documentation_source_path: 'ref/servooutput.html'
language: en
---

# Servo Output

## Ports
```yaml
ports:
- name: Servo Data
  summary: Servo data to write to output channels double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean
  direction: input
  data_types: double | single | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Missed Ticks
  summary: Missed tick count (optional) double
  direction: output
  data_types: double
```

### Input

### **Servo Data** — Servo data to write to output channels double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean

Servo position (angle). The minimum and maximum values for shaft position vary
with the **Block input signal** (units) argument value:

| Block input signal | Minimum Servo Data | Maximum Servo Data |
| --- | --- | --- |
| Degrees (default) | `0` | `180` |
| Radians | `0` | `pi` |
| Normalized bipolar | `-1` | `1` |
| Normalized unipolar | `0` | `1` |

**Example:**  90

**Data Types:** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
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
- name: Output channels
  summary: Channel vector that selects other output channels 1 (default) | vector
  group: ''
  block_parameter: Channels
- name: Block input signal
  summary: Units of the block input signal Degrees (default) | Radians | Normalized bipolar | Normalized unipolar
  group: ''
  block_parameter: RangeMode
- name: Minimum pulse duration
  summary: Duration of the control pulse 500e-6 (default)
  group: ''
  block_parameter: MinPulseDuration
- name: Maximum pulse duration
  summary: Duration of the control pulse 2500e-6 (default)
  group: ''
  block_parameter: MaxPulseDuration
- name: Initial value
  summary: Specify the value that the channel generates before execution starts vector
  group: ''
  block_parameter: InitialValue
- name: Final value
  summary: Specify the value that the channel generates after execution ends vector
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

Enter a value, in seconds, that represents how frequently you want the block to
execute and interact with the I/O hardware. The block synchronizes your model with the
real-time clock at this sample rate.

If you are using a fixed-step solver, enter the value that you entered as the
**Fixed step size** configuration parameter or an integer multiple of
that value.

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

### **Output channels** — Channel vector that selects other output channels `1` (default) | vector

Enter a channel vector that selects the other output channels that you are using on
this board. The vector can be any valid
MATLAB® vector form. For example, to select the first two other output channels,
enter:

```
[1,2]
```

or

```
[1:2]
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Channels` |

### **Block input signal** — Units of the block input signal `Degrees` (default) | `Radians` | `Normalized bipolar` | `Normalized unipolar`

Select the units of the block input signal that specifies servo position.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RangeMode` |

### **Minimum pulse duration** — Duration of the control pulse 500e-6 (default)

Select the duration of the control pulse that corresponds to the minimum servo
angle. Because not all servos are the same, this parameter lets you calibrate the input
signal to the actual servo angle.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MinPulseDuration` |

### **Maximum pulse duration** — Duration of the control pulse 2500e-6 (default)

Select the duration of the control pulse that corresponds to the maximum servo
angle. Because not all servos are the same, this parameter lets you calibrate the input
signal to the actual servo angle.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxPulseDuration` |

### **Initial value** — Specify the value that the channel generates before execution starts vector

Enter the initial value for each output channel that you entered in the
**Output channels** box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialValue` |

### **Final value** — Specify the value that the channel generates after execution ends vector

Enter the final value for each output channel that you entered in the
**Output channels** box.

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

**Introduced in R2018b**

### R2024b: Update to blocks with port names

In R2024b, when you enable optional ports, such as **Show "Missed Ticks"
port**, these Simulink®
Desktop Real-Time™ block ports appear with labels.

## Description

Write to standard servo output channels

The Servo Output block sets the shaft position of a standard servo
motor.

To rotate the servo shaft, send values to the block input.

Sending out-of-range values to the block input has the same effect as sending the minimum
or maximum input values.

The block input inherits the data type of the upstream block.
