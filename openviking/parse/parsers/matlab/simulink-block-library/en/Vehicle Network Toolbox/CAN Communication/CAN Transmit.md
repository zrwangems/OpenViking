---
type: simulink-block
title: 'CAN Transmit'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'cantransmit'
documentation_source_path: 'ug/cantransmit.html'
language: en
---

# CAN Transmit

## Ports
```yaml
ports:
- name: CAN Msg
  summary: CAN message to transmit packed CAN message
  direction: input
  data_types: CAN_MESSAGE | bus
```

### Input

### **CAN Msg** — CAN message to transmit packed CAN message

CAN message as packed by the CAN Pack block, input as a CAN\_MESSAGE or a
Simulink signal bus.

**Data Types:** `CAN_MESSAGE` | `bus`
## Parameters
```yaml
parameters:
- name: Device
  summary: CAN device and channel list option
  group: ''
  block_parameter: Device
  type: character vector, string
- name: 'Transmit Options: On data change'
  summary: Enable event-based transmission when data changes 'off' (default) | 'on'
  group: ''
  block_parameter: EnableEventTransmit
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: 'Transmit Options: Periodic'
  summary: Enable periodic transmission 'off' (default) | 'on'
  group: ''
  block_parameter: EnablePerioicTransmit
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: 'Transmit Options: Message period'
  summary: Period of message transmission rate 1.000 (default) | positive numeric scalar
  group: ''
  block_parameter: MessagePeriod
  type: character vector, string
  values: double
  default: '''1.000'''
```

### **Device** — CAN device and channel list option

Select the CAN device and channel for transmitting CAN messages to the network. The
list of options shows all the devices installed on the system. It displays the vendor
name, the device name, and the channel ID. The default is the first available device on
your system.

Note: When using PEAK-System devices, CAN Transmit blocks in multiple enabled
subsystems might skip some messages. If possible, replace the enabled subsystems with a
different type of conditional subsystem, such as an if-action, switch-case-action, or
triggered subsystem; or redesign your model so that all the CAN Transmit blocks are
contained within a single enabled subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Device` |
| **Type:** character vector, string |

### **Transmit Options: On data change** — Enable event-based transmission when data changes `'off'` (default) | `'on'`

When event-based transmission is enabled, messages are transmitted only at those
time steps when a change in message data is detected. When the input data matches the
most recent transmission for a given message ID, the message is not
re-transmitted.

Event and periodic transmission can both be enabled to work together simultaneously.
If neither is selected, the default behavior is to transmit the current input at each
time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableEventTransmit` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Transmit Options: Periodic** — Enable periodic transmission `'off'` (default) | `'on'`

Select this option to enable periodic transmission of the message on the configured
channel at the specified message period. The period references real time, regardless of
the Simulink model time step size (fundamental sample time) or block execution sample
time. This is equivalent to the MATLAB function `transmitPeriodic`.

The periodic transmission is a nonbuffered operation. Only the last CAN message or
set of muxed messages present at the input of the CAN Transmit block is sent when the
time period occurs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnablePerioicTransmit` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Transmit Options: Message period** — Period of message transmission rate `1.000` (default) | positive numeric scalar

Specify a message transmission period in seconds. This value is used to transmit the
message in the specified period. By default this value is `1.000`
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MessagePeriod` |
| **Type:** character vector, string |
| **Values:** double |
| **Default:** `'1.000'` |
## Libraries

Vehicle Network Toolbox / CAN Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block generates code with limited portability that runs only on the host computer. See
Code Generation.

## Version History

**Introduced in R2009a**

## Description

Transmit CAN message to selected CAN device

The CAN Transmit block transmits messages to the CAN network using the specified CAN
device. The CAN Transmit block can transmit a single message or an array of
messages during a given timestep. To transmit an array of messages, use a mux (Simulink) (multiplex) block from the Simulink® block library.

**Note**

You need a license for both Vehicle Network Toolbox™ and Simulink software to use this block.

The CAN Transmit block has one input port. This port accepts a CAN message that was packed
using the CAN Pack block. It has no output ports.

CAN is a peer-to-peer network, so when transmitting messages on a physical bus at least
one other node must be present to properly acknowledge the message. Without another node, the
transmission will fail as an error frame, and the device will continually retry to
transmit.

### Other Supported Features

The CAN Transmit block supports the use of Simulink accelerator mode. Using this feature, you can speed up the execution of
Simulink models. For more information on this feature, see Acceleration (Simulink).

The CAN Transmit block supports the use of code generation along with the
packNGo function to group required source code and dependent shared libraries.

### Code Generation

Vehicle Network Toolbox
Simulink blocks allow you to generate code, enabling models containing these
blocks to run in accelerator, rapid accelerator, external, and deployed
modes.

**Code Generation with Simulink
Coder**

You can use Vehicle Network Toolbox, Simulink
Coder™, and Embedded Coder® software together to generate code on the host end that you
can use to implement your model. For more information on code generation,
see Generated Code Compilation (Simulink Coder).

**Shared Library Dependencies**

The block generates code with limited portability. The block uses
precompiled shared libraries, such as DLLs, to support I/O for
specific types of devices. With this block, you can use the
`packNGo` function supported by Simulink
Coder to set up and manage the build information for your
models. The `packNGo` (Simulink Coder) function
allows you to package model code and dependent shared libraries into
a zip file for deployment. You do not need MATLAB® installed on the target system, but the target system
needs to be supported by MATLAB.

To set up `packNGo`:

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

In this example, `gcs` is the current model that you
want to build. Building the model creates a zip file with the same name as
model name. You can move this zip file to another machine and there build
the source code in the zip file to create an executable which can run
independent of MATLAB and Simulink. The generated code compiles with both C and C++ compilers.
For more information, see Code Compilation Customization (Simulink Coder).

**Note**

On Linux® platforms, you need to add the folder where
you unzip the libraries to the environment variable
`LD_LIBRARY_PATH`.
