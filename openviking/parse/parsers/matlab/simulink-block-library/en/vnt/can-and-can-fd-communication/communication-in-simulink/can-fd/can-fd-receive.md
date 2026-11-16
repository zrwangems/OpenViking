---
type: simulink-block
title: 'CAN FD Receive'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN and CAN FD Communication / Communication in Simulink / CAN FD'
documentation_page: 'canfdreceive'
documentation_source_path: 'ug/canfdreceive.html'
language: en
---

# CAN FD Receive

## Ports

### Output

### **CAN Msg** — Received CAN messages `CAN_FD_MESSAGE_BUS`

The `CAN Msg` output port contains one or more packed
CAN messages received at that particular timestep, output as a
`CAN_FD_MESSAGE_BUS`. The output includes either
one or all messages for that timestep, depending on the setting of
**Number of messages received at each
timestep**.

**Data Types:** `CAN_FD_MESSAGE_BUS`

### **f()** — Function-call event output function-call event

The `f()` output port is a trigger to a Function-Call
subsystem. If the block receives a new message, it triggers a
Function-Call from this port. You can then connect to a Function-Call Subsystem (Simulink)
to unpack and process a message.

**Data Types:** `function-call event`

## Parameters

**Tip**

Configure your CAN FD Configuration block before you configure the
CAN FD Receive block parameters.

### **Device** — CAN device and channel list option

Select from the list the CAN device and a channel on the device you want
to receive CAN messages from. This field lists all the devices installed on
the system. It displays the vendor name, the device name, and the channel
ID. The default is the first available device on your system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Device` |
| **Type:** character vector, string |

### **Standard IDs Filter** — Limit or allow messages based on standard ID `Allow all` (default) | `Allow only` | `Block all`

Select the filter for standard IDs. Choices are:

- `Allow all` (default): Allows all standard IDs to
  pass the filter.
- `Allow only`: Allows only the ID or range of IDs
  specified in the text field, specified as a single ID or an array of
  IDs. You can also specify disjointed IDs or arrays separated by a
  comma. For example, to allow IDs 400 through 500, and 600 through
  650, enter `[[400:500],[600:650]]`. Standard IDs
  must be positive integers from 0 to 2047. You can also specify
  hexadecimal values with the `hex2dec`
  function.
- `Block all`: Blocks all standard IDs from passing
  the filter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StdIDsCombo` |
| **Type:** character vector, string |
| **Values:** `'Allow all'` | `'Allow only'` | `'Block all'` |
| **Default:** `'Allow all'` |

If using `'Allow only'`, set the filter values with
the following:

|  |
| --- |
| **Block Parameter:** `StandardIDs` |
| **Type:** character vector, string |
| **Values:** integer scalar or row vector |

### **Extended IDs Filter** — Limit or allow messages based on extended ID `Allow all` (default) | `Allow only` | `Block all`

Select the filter on this block for extended IDs. Choices are:

- `Allow all` (default): Allows all extended IDs to
  pass the filter.
- `Allow only`: Allows only those IDs specified in
  the text field. Allows only the ID or range of IDs specified in the
  text field, specified as a single ID or an array of IDs. You can
  also specify disjointed IDs or arrays separated by a comma. For
  example, to accept IDs 3000 through 3500, and 3600 through 3620,
  enter `[[3000:3500],[3600:3620]]`. Extended IDs
  must be positive integers from 0 to 536870911. You can also specify
  hexadecimal values using the `hex2dec`
  function.
- `Block all`: Blocks all extended IDs from passing
  the filter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtIDsCombo` |
| **Type:** character vector, string |
| **Values:** `'Allow all'` | `'Allow only'` | `'Block all'` |
| **Default:** `'Allow all'` |

|  |
| --- |
| **Block Parameter:** `ExtendedIDs` |
| **Type:** character vector, string |
| **Values:** integer scalar or row vector |

### **Sample time** — Block execution rate `0.01` (default)

Specify the sampling time of the block, which defines the rate at which
the block is executed during simulation. The default value is 0.01
simulation seconds. If the block is inside a triggered subsystem or to
inherit sample time, you can specify `-1` as your sample
time. You can also specify a MATLAB variable for sample time. For more information, see Timing in Hardware Interface Models.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector, string |
| **Values:** double |
| **Default:** `'0.01'` |

### **Number of messages received at each timestep** — Receive one or all messages `all` (default) | `1`

Select how many messages the block receives at each specified timestep.
Valid choices are:

- `all` (default): The CAN FD
  Receive block delivers all available messages in the
  FIFO buffer to the model during a specific timestep. The block
  generates one function call for each delivered message. The output
  port always contains one CAN message at a time.
- `1`: The CAN FD Receive block
  delivers one message per timestep from the FIFO buffer to the
  model.

If the block does not receive any messages before the next timestep, it
outputs the last received message.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgsPerTimestep` |
| **Type:** character vector, string |
| **Values:** `'all'` | `'1'` |
| **Default:** `'all'` |

## Libraries

Vehicle Network Toolbox / CAN FD Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block generates code with limited portability that runs only on the host computer. See
Code Generation.

## Version History

**Introduced in R2018a**

## Description

Receive CAN FD messages from specified CAN FD device

The CAN FD Receive block receives messages from the CAN network and delivers them to
the Simulink® model. It outputs one message or all messages at each timestep, depending
on the block parameters.

**Note**

You need a license for both Vehicle Network Toolbox™ and Simulink software to use this block.

The CAN FD Receive block has two output ports:

- The `f()` output port is a trigger to a Function-Call
  subsystem. If the block receives a new message, it triggers a Function-Call from
  this port. You can then connect to a Function-Call Subsystem (Simulink) to
  unpack and process a message.
- The `Msg` output port contains the CAN messages received at
  that particular timestep. The block outputs messages as a Simulink bus signal. For more information on Simulink bus objects, see Composite Interfaces (Simulink).

The CAN FD Receive block stores CAN messages in a first-in, first-out
(FIFO) buffer. The FIFO buffer delivers the messages to your model in the queued order
at every timestep.

**Note**

You cannot have more than one CAN FD Receive block in a model using the same
PEAK-System device channel.

### Other Supported Features

The CAN FD Receive block supports the use of Simulink accelerator mode. Using this feature, you can speed up the execution
of Simulink models. For more information, see Acceleration (Simulink).

The CAN FD Receive block supports the use of code generation along
with the packNGo function to group required source code and dependent shared
libraries.

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
