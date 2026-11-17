---
type: simulink-block
title: 'CAN FD Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdconfiguration'
documentation_source_path: 'ug/canfdconfiguration.html'
language: en
---

# CAN FD Configuration

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Device
  summary: CAN device and channel list option
  group: ''
  block_parameter: Device
  type: character vector, string
- name: Arbitration Bus speed
  summary: Arbitration bit rate numeric
  group: ''
  block_parameter: ArbitrationBusSpeed
  type: character vector, string
  values: integer
- name: Data Bus speed
  summary: Data bit rate numeric
  group: ''
  block_parameter: DataBusSpeed
  type: character vector, string
  values: integer
- name: Bus frequency
  summary: PEAK-System bus rate numeric
  group: ''
  block_parameter: BusFrequency
  type: character vector, string
  values: numeric
- name: Arbitration/Data bit rate prescaler
  summary: Bit rate prescaler integer
  group: ''
  block_parameter: ArbitrationPrescaler, DataPrescaler
  type: character vector, string
  values: integer
- name: Synchronization jump width
  summary: Maximum allowed time adjustment integer
  group: ''
  block_parameter: ArbitrationSJW, DataSJW
  type: character vector, string
  values: integer
- name: Time segment 1
  summary: Number of time quanta before sample integer
  group: ''
  block_parameter: ArbitrationTSEG1, DataTSEG1
  type: character vector, string
  values: integer
- name: Time segment 2
  summary: Number of time quanta after sample integer
  group: ''
  block_parameter: ArbitrationTSEG2, DataTSEG2
  type: character vector, string
  values: integer
- name: Verify bit parameter settings validity
  summary: Check validity of settings
  group: ''
- name: Acknowledge mode
  summary: Control channel activity on CAN bus Normal (default) | Silent
  group: ''
  block_parameter: AckMode
  type: character vector, string
  values: '''Normal'' | ''Silent'''
  default: '''Normal'''
```

### **Device** — CAN device and channel list option

Select the CAN FD device and a channel on the device that you want to use
from the list. Use this device to transmit and/or receive messages. The
device driver determines the default bus speed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Device` |
| **Type:** character vector, string |

### **Arbitration Bus speed** — Arbitration bit rate numeric

Set arbitration bus speed for the selected device, in bits per second. The
default speed is assigned by the selected device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ArbitrationBusSpeed` |
| **Type:** character vector, string |
| **Values:** integer |

### **Data Bus speed** — Data bit rate numeric

Set data bus speed for the selected device, in bits per second. The
default speed is assigned by the selected device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataBusSpeed` |
| **Type:** character vector, string |
| **Values:** integer |

### **Bus frequency** — PEAK-System bus rate numeric

(PEAK-System only.) Set the bus frequency, in megahertz.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BusFrequency` |
| **Type:** character vector, string |
| **Values:** numeric |

### **Arbitration/Data bit rate prescaler** — Bit rate prescaler integer

(PEAK-System only.) Set separate bit rate prescaler values for arbitration
and data bit rates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ArbitrationPrescaler`, `DataPrescaler` |
| **Type:** character vector, string |
| **Values:** integer |

For Vector and PEAK-System devices, the next three parameters are available in two
sets for manually setting bit parameters for data and arbitration bus speeds. For more
information on these parameters, see Bit
Timing.

### **Synchronization jump width** — Maximum allowed time adjustment integer

Specify the maximum limit of bit time adjustment in the case of
resynchronization. The specified value must be a positive integer indicating
a number of bit time quanta segments. If you do not specify a value, the
selected bus speed setting determines the default value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ArbitrationSJW`, `DataSJW` |
| **Type:** character vector, string |
| **Values:** integer |

### **Time segment 1** — Number of time quanta before sample integer

Specify the number of bit time quanta before the sampling point. The
specified value must be a positive integer. Typically, an adjustment of this
value is made with a corresponding inverse adjustment to **Time
segment 2** so that their sum remains constant. If you do not
specify a value, the selected bus speed setting determines the default
value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ArbitrationTSEG1`, `DataTSEG1` |
| **Type:** character vector, string |
| **Values:** integer |

### **Time segment 2** — Number of time quanta after sample integer

Specify the number of bit time quanta after the sampling point. The
specified value must be a positive integer. Typically, an adjustment of this
value is made with a corresponding inverse adjustment to **Time
segment 1** so that their sum remains constant. If you do not
specify a value, the selected bus speed setting determines the default
value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ArbitrationTSEG2`, `DataTSEG2` |
| **Type:** character vector, string |
| **Values:** integer |

### **Verify bit parameter settings validity** — Check validity of settings

If you have altered the bit parameter settings, click this button to see
if your settings are valid. The block runs a check to see if the combination
of your bus speed settings and the bit parameter values form a valid value
for the device. If the new bit parameter values do not form a valid
combination, the verification fails and displays an error message.

#### Programmatic Use

None

### **Acknowledge mode** — Control channel activity on CAN bus `Normal` (default) | `Silent`

Specify whether the channel is in Normal or Silent mode. By default
**Acknowledge mode** is `Normal`. In
this mode, the channel both receives and transmits messages normally and
performs other tasks on the network such as acknowledging messages and
creating error frames. To observe all message activity on the network and
perform analysis, without affecting the network state or behavior, select
`Silent`. In Silent mode, you can only receive messages
and not transmit.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AckMode` |
| **Type:** character vector, string |
| **Values:** `'Normal'` | `'Silent'` |
| **Default:** `'Normal'` |
## Libraries

Vehicle Network Toolbox / CAN FD Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When used with the CAN FD
Receive and CAN FD
Transmit blocks, the CAN FD Configuration block supports
code generation, but with limited portability that runs only on the host
computer.

## Version History

**Introduced in R2018a**

## Description

Configure parameters for specified CAN FD device

The CAN FD Configuration block configures parameters for a CAN FD device that you can
use to transmit and receive messages.

Specify the configuration of your CAN FD device before you configure other CAN FD
blocks.

Use one CAN FD Configuration block to configure each device that sends
and receives messages in your model. If you use a CAN FD Receive
or a CAN FD Transmit
block to receive and send messages on a device, your model checks to see if there is a
corresponding CAN FD Configuration block for the specified device.

**Note**

You need a license for both Vehicle Network Toolbox™ and Simulink® software to use this block.

### Other Supported Features

The CAN FD Configuration block supports the use of Simulink accelerator mode. Using this feature, you can speed up the execution
of Simulink models. For more information, see Acceleration (Simulink).
