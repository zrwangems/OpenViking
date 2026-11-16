---
type: simulink-block
title: 'CAN Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'canconfiguration'
documentation_source_path: 'ug/canconfiguration.html'
language: en
---

# CAN Configuration

## Ports

Not documented in R2025b.

## Parameters

### **Device** — CAN device and channel list option

Select the CAN device and a channel on the device that you want to use from the
list. Use this device to transmit and receive messages. The device driver determines the
default bus speed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Device` |
| **Type:** character vector, string |

### **Bus speed** — CAN bus bit rate integer

Set the `BusSpeed` property for the selected device, in bits per
second. The default bus speed is the default assigned by the selected device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BusSpeed` |
| **Type:** character vector, string |
| **Values:** integer |

### **Manually configure bit parameters** — Allow specifying individual bit parameters off (default) | on

**Note**

This option is available only for supporting vendors.

Select this check box to allow manual specifying of bit parameters. The bit
parameter settings include: **Synchronization jump width**,
**Time segment 1**, **Time segment 2**, and
**Number of samples**. For more information on these parameters, see
Bit Timing.
If you do not select this option, the device automatically assigns the bit parameters
depending on the bus speed setting.

**Tip**

Use the default bit parameter settings unless you have specific timing
requirements for your CAN connection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableBitParameters` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |
|  |

### **Synchronization jump width** — Maximum allowed time adjustment integer

Specify the maximum limit of bit time adjustment in the case of resynchronization.
The specified value must be a positive integer indicating a number of bit time quanta
segments. If you do not specify a value, the selected bus speed setting determine the
default value. To change this value, select the **Enable bit parameters
manually** check box first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SJW` |
| **Type:** character vector, string |
| **Values:** integer |

### **Time segment 1** — Number of time quanta before sample integer

Specify the number of bit time quanta before the sampling point. The specified value
must be a positive integer. Typically, an adjustment of this value is made with a
corresponding inverse adjustment to **Time segment 2** so that their
sum remains constant. If you do not specify a value, the selected bus speed setting
determines the default value. To change this value, select the **Enable bit
parameters manually** check box first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TSEG1` |
| **Type:** character vector, string |
| **Values:** integer |

### **Time segment 2** — Number of time quanta after sample integer

Specify the number of bit time quanta after the sampling point. The specified value
must be a positive integer. Typically, an adjustment of this value is made with a
corresponding inverse adjustment to **Time segment 1** so that their
sum remains constant. If you do not specify a value, the selected bus speed setting
determines the default value. To change this value, select the **Enable bit
parameters manually** check box first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TSEG2` |
| **Type:** character vector, string |
| **Values:** integer |

### **Number of samples** — Samples per bit integer

Specify the number of samples per bit. The specified value must be a positive
integer. If you do not specify a value, the selected bus speed setting determines the
default value. To change this value, select the **Enable bit parameters
manually** check box first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NSamples` |
| **Type:** character vector, string |
| **Values:** integer |

### **Verify bit parameter settings validity** — Check validity of settings

If you have set the bit parameter settings manually, click this button to see if
your settings are valid. The block runs a check to see if the combination of your bus
speed and bit parameter values form a valid combination for the CAN device. If the
current combination is not valid, the verification fails and displays an error message.
This button is active only when the **Enable bit parameters manually**
check box is selected.

#### Programmatic Use

None

### **Acknowledge mode** — Control channel activity on CAN bus `Normal` (default) | `Silent`

Specify whether the channel is in `Normal` or
`Silent` mode. By default **Acknowledge mode** is
`Normal`. In this mode, the channel can receive and transmit messages
normally, and perform other tasks on the network such as acknowledging messages and
creating error frames. To observe all message activity on the network and perform
analysis, without affecting the network state or behavior, select
`Silent`. In `Silent` mode, the channel can only
receive messages and not transmit.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AckMode` |
| **Type:** character vector, string |
| **Values:** `'Normal'` | `'Silent'` |
| **Default:** `'Normal'` |

## Libraries

Vehicle Network Toolbox / CAN Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When used with the CAN Receive and CAN
Transmit blocks, the CAN Configuration block supports code
generation, but with limited portability that runs only on the host computer.

## Version History

**Introduced in R2009a**

## Description

Configure parameters for specified CAN device

The CAN Configuration block configures parameters for a CAN device that you can use to
transmit and receive messages.

Specify the configuration of your CAN device before you configure other CAN blocks.

Use one CAN Configuration block to configure each device that sends and
receives messages in your model. If you use a CAN
Receive or a CAN Transmit block to receive and send messages on a
device, your model requires a corresponding CAN Configuration block for the
specified device.

**Note**

You need a license for both Vehicle Network Toolbox™ and Simulink® software to use this block.

### Other Supported Features

The CAN Configuration block supports the use of Simulink accelerator and rapid accelerator modes. Using this feature, you can speed up
the execution of Simulink models. For more information on this feature, see Acceleration (Simulink).
