---
type: simulink-block
title: 'Encoder Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'encoderinput'
documentation_source_path: 'ref/encoderinput.html'
language: en
---

# Encoder Input

## Ports
```yaml
ports:
- name: Encoder Data
  summary: Encoder data read from input channels vector
  direction: output
  data_types: single | double | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Missed Ticks
  summary: Missed tick count (optional) double
  direction: output
  data_types: double
```

### Output

### **Encoder Data** — Encoder data read from input channels vector

Data representing the state of an encoder. The data type and
range of the output values depend upon the capabilities of the board.

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
- name: Input channels
  summary: Select encoder input channels 1 (default) | vector
  group: ''
  block_parameter: Channels
- name: Quadrature mode
  summary: To detect optically the amplitude and direction of movement, select encoder stripe edges quadruple (default) |
    double | single | two-pulse
  group: ''
  block_parameter: QuadMode
- name: Reset input function
  summary: Select mode of reset pin reset (default) | gate | rising edge index | falling edge index
  group: ''
  block_parameter: IndexPulse
- name: Input filter clock frequency
  summary: Cutoff frequency (Hz) of low-pass filter Inf (default) | scalar
  group: ''
  block_parameter: InputFilter
- name: Output data type
  summary: Data type of block output double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32
  group: ''
  block_parameter: DataType
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

### **Input channels** — Select encoder input channels `1` (default) | vector

Enter a channel vector that selects the encoder input channels that you are
using on this board. The vector can be any valid MATLAB® vector form. Each vector element corresponds to a channel on
the selected hardware board in the same order as channels are numbered on
the board. For example, to select the first four encoder input channels,
enter:

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

### **Quadrature mode** — To detect optically the amplitude and direction of movement, select encoder stripe edges `quadruple` (default) | `double` | `single` | `two-pulse`

Encoders use two sets of stripes, shifted in
phase, to detect optically the amplitude and direction of movement.
This parameter specifies which encoder stripe edges the encoder counts.
From the list, select:

- `quadruple` (default) —
  Counts rising and falling edges from both stripe sets.
- `double` — Counts
  the rising edges from both stripe sets.
- `single` — Counts
  the rising edges from one stripe set.
- `two-pulse` — Counts the rising
  edges from two pulse encoder input with channel A input incrementing
  the count and input from channel B decrementing the count. This
  option is available when an NI-62xx or NI-63xx board is
  selected.

Quadruple mode yields four times more pulses per revolution
than the single mode. Therefore, quadruple is more accurate.
Use quadruple mode unless other parameters dictate otherwise.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `QuadMode` |

### **Reset input function** — Select mode of reset pin `reset` (default) | `gate` | `rising edge index` | `falling edge index`

The encoder interface chip has a reset pin in
addition to encoder inputs. Usually, you connect this pin to the index
output of the encoder. However, you can connect it to any
signal or not at all.
This parameter specifies the function of this pin. From the list,
select:

- `reset` (default) —
  Level reset of the encoder count.
- `gate` — Enables encoder
  counting.
- `rising edge index` —
  Resets the encoder count on the rising edge.
- `falling edge index` —
  Resets the encoder count on the falling edge.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexPulse` |

### **Input filter clock frequency** — Cutoff frequency (Hz) of low-pass filter `Inf` (default) | scalar

The encoder interface chip includes a low-pass
filter that filters out high frequencies, which the chip interprets
as noise. This parameter is the cutoff frequency (Hz) of this filter.
The cutoff frequency that you specify is rounded to the nearest frequency
supported by the chip.

If the encoder is moving slowly and high-frequency noise is
present, use the filter to eliminate the noise. With the filter in
operation, the chip does not count the noise as encoder pulses. If
the encoder is moving quickly, the filter can filter out the high-frequency
pulses, including pulses that you want to count. In this case, consider
disabling the filter by setting the cutoff frequency to `Inf`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputFilter` |

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

### R2024a: Encoder Input Block two-pulse input support

The Encoder Input block Quadrature mode
parameter supports selecting two-pulse mode when using a National Instruments™ 62xx or 63xx I/O board.

### R2018a: Encoder Input Block Reset for NI PCIe-6351

The Encoder Input block has an added option to select encoder phase
for index pulse to the National Instruments PCI-62xx and PCI-63xx board drivers

## Description

Read from one or multiple incremental encoder input channels

The Encoder Input block connects to and reads from specific encoder input
channels into your Simulink® model. After you have added an Encoder Input block to your
model, you can enter the parameters for its I/O driver.
