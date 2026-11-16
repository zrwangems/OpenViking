---
type: simulink-block
title: 'CAN Replay'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN and CAN FD Communication / Communication in Simulink / CAN'
documentation_page: 'canreplay'
documentation_source_path: 'ug/canreplay.html'
language: en
---

# CAN Replay

## Ports

### Output

### **CAN Msg** — Replayed CAN messages `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

This output port contains a packed CAN message logged at that particular timestep,
output as a `CAN_MESSAGE` or signal bus of type
`CAN_MESSAGE_BUS`.

**Data Types:** `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

### **f()** — Function-call event output function-call event

This port provides a trigger to a Function-Call subsystem when the block receives
a new message. You can connect it to a Function-Call Subsystem (Simulink) to unpack and process the message.

**Data Types:** `function-call event`

## Parameters

**Tip**

Configure your CAN Configuration block before you configure the
CAN Receive block parameters.

### **File name** — Path and name of MAT-file with messages `untitled.mat` (default) | file name

Specify the name and path of the file that contains logged CAN messages that you can
replay. You can click **Browse** to browse to a file location and
select the file.

### **Variable name** — Variable in MAT-file holding messages `ans` (default) | variable

Specify the variable saved in the MAT-file that holds the CAN message
information.

### **Number of times to replay messages** — Repeat value `Inf` (default) | integer

Specify the number of times you want the message replayed in your model. You can
specify any positive integer, including `Inf`. Specifying
`Inf` continuously replays messages until simulation stops.

### **Replay messages to** — Specify output location CAN Bus (default) | `Output port`

Specify if the model is replaying messages to the CAN network or an output port.
When replaying to the CAN network, you must also select a
**Device**.

### **Device** — CAN device and channel device list option

Select the device on the CAN network to replay messages to. This field is
unavailable if you select `Output port` for the **Replay
message to** parameter.

### **Sample time** — Block execution rate `0.01` (default) | numeric

Specify the sampling time of the block during simulation. This value defines the
frequency at which the CAN Replay block runs during simulation. If the
block is inside a triggered subsystem or to inherit sample time, you can specify
`–1` as the sample time. You can also specify a MATLAB variable for sample time. The default value is `0.01`
simulation seconds. For more information, see Timing in Hardware Interface Models.

### **Output as bus** — Enable signal bus output off (default) | on

Select this option for the block to output CAN messages as a Simulink bus signal. For more information on Simulink bus objects, see Composite Interfaces (Simulink).

## Libraries

Vehicle Network Toolbox / CAN Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block generates code with limited portability that runs only on the host computer. See
Code Generation.

## Version History

**Introduced in R2011b**

## Description

Replay logged CAN messages

The CAN Replay block replays logged messages from a `.mat` file to a CAN
network or to Simulink®. You need a CAN Configuration block to replay to the network.

To replay messages logged in the MATLAB® Command window in your Simulink model, convert them into a compatible format using `canMessageReplayBlockStruct` and save the result to a separate file. For more
information, see Log and Replay CAN Messages.

**Note**

You need a license for both Vehicle Network Toolbox™ and Simulink software to use this block.

### Replay Timing

The block replays messages using their original timestamps to synchronize with
simulation time (for regular simulations) or wall-clock time (for replay to a physical
network). Specifically, when the Simulink solver advances one time step, the block sends the messages whose timestamps
belong to that time step. Therefore, it is important that the timestamps are consistent with
the time range of the simulation. It is recommended to set the simulation start time to
`0`, and to shift the message timestamps so that the initial timestamp is
`0`.

For more information, see **Start time (Simulink)** and the example Log and Replay CAN Messages.

### Other Supported Features

The CAN Replay block supports the use of Simulink accelerator and rapid accelerator modes. Using this feature, you can speed up
the execution of Simulink models. For more information on this feature, see Acceleration (Simulink).

The CAN Replay block supports the use of code generation along with the
packNGo function to group required source code and dependent shared libraries. For more
information, see Code Generation.

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
a zip file for deployment. You do not need MATLAB installed on the target system, but the target system
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
