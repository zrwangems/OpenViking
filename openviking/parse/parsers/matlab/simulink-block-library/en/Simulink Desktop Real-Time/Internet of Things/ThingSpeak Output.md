---
type: simulink-block
title: 'ThingSpeak Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Internet of Things'
documentation_page: 'thingspeakoutput'
documentation_source_path: 'ref/thingspeakoutput.html'
language: en
---

# ThingSpeak Output

## Ports

### Input

### **Data** — Data to write to channel numeric

Scalar numeric data to write to the ThingSpeak channel.

**Example:** `3.14159`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Channel number** — ThingSpeak channel being accessed Read-only: `0` (default) | numeric

This parameter is read-only.

To select a channel, click the **Configure channel parameters**
button. In the Network Services ThingSpeak dialog box, set the **Channel
ID** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvAddress` |

### **Configure channel parameters** — Select and configure channel to access (button)

To configure the channel, click this button. A dialog box displays the
channel parameter settings.

To accept your changes, click **OK**. To test your
changes, click **Test**. To revert your settings to their
previous values, click **Revert**. To exit the dialog box
without changing the settings, click **Cancel**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvName` |
| **Block Parameter:** `DrvOptions` |

### **ThingSpeak server** — Server for data transfer `api.thingspeak.com` (default) | character vector

The default value is the standard address of the public
ThingSpeak server.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvName` |
| **Block Parameter:** `DrvOptions` |

### **Channel ID** — Unique channel `0` (default) | numeric

Select a unique channel among the available channels.

You cannot read and write over the same ThingSpeak channel in the same model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvOptions` |

### **Write API key** — Access key for writing to channel character vector

By default, this key is the API key for the channel on the
public server, api.thingspeak.com.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvOptions` |

### **Update period (secs)** — Write update period, in seconds `20` (default) | numeric

Time between successive writes to the channel.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DrvOptions` |

### **View channel web page** — Access web page for channel (button)

To access the web page
for **Channel number**, click **View channel web page**.

#### Programmatic Use

|  |
| --- |
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

### **Output fields** — Define which parts of data to write `1` (default) | `[1–8]`

You can write `1–8` fields to each channel. Use this
parameter to ignore implementation-specific information and transmit only
the fields that your application requires.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ChannelFields` |

### **Initial value** — First value transmitted [] (default) | `[integer]`

Transmit an initial value, for example an initial state value or an
initialization command.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialValue` |

### **Final value** — Last value transmitted [] (default) | `[integer]`

Transmit a final value, for example a final state value or a wrap-up
command.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FinalValue` |

## Libraries

Simulink Desktop Real-Time / Internet of Things

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

### R2024b: Update to blocks with port names

In R2024b, when you enable optional ports, such as **Show "Missed Ticks"
port**, these Simulink®
Desktop Real-Time™ block ports appear with labels.

## Description

Write output fields to ThingSpeak channel

The ThingSpeak Output block writes numeric data to
`1−8`
ThingSpeak™ channels.

By default, this block uses the public ThingSpeak server, `api.thingspeak.com`. To configure the ThingSpeak channel, click **Configure channel parameters**.

To access the web page
for **Channel number**, click **View channel web page**.

This block does not synchronize the ThingSpeak timestamp with the simulation time. For example, assume that the block is
set to a sample time of `0.1` s and that the channel update period is
`20` s. The block transmits the data at a particular simulation
time, *T*, but ThingSpeak writes the data and gives it a timestamp only at the `20`
update period.
