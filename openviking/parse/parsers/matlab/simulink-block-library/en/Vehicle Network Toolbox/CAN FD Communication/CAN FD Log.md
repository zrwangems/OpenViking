---
type: simulink-block
title: 'CAN FD Log'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdlog'
documentation_source_path: 'ug/canfdlog.html'
language: en
---

# CAN FD Log

## Ports

### Input

### **CAN Msg** — CAN FD messages to log `CAN_FD_MESSAGE_BUS`

The **CAN Msg** input port is available when the **Log
messages from** parameter is set to `Input port`. Provide
an input from another block as a Simulink signal bus of type `CAN_FD_MESSAGE_BUS`.

**Data Types:** `CAN_FD_MESSAGE_BUS`

## Parameters

**Tip**

If you are logging from the network, you need to configure your CAN channel with a
CAN FD Configuration
block.

### **File name** — Log file location and name `untitled.mat` (default) | file name

Enter the path and name of the MAT-file to log CAN messages to, or click
**Browse** to browse to a file location.

The model appends the log file name with the current date and time in the format
`YYYY-MMM-DD_hhmmss`. Specify a unique name to differentiate between
your files for repeated logging.

### **Variable name** — Variable name for CAN FD messages in log file `ans` (default) | variable name

Specify the name for the variable saved in the MAT-file that holds the CAN message
information.

### **Maximum number of messages to log** — Limit quantity of messages `10000` (default) | numeric

Specify the maximum number of messages this block can log from the selected device
or port. The specified value must be a positive integer. The default value is
`10000` messages. The log file saves the most recent messages up to
the specified maximum number.

### **Log messages from** — Source of messages `CAN FD Bus` (default) | `Input port`

Select the source of the messages logged by the block. To log messages from the CAN
FD bus network, select `CAN FD Bus`, then specify a
**Device**. To log messages from another block in the model, select
`Input port`, which adds an inport port to the block.

### **Device** — CAN device and channel list option

Select the device on the CAN FD network that you want to log messages from. This
field is available only if you select `CAN FD Bus` for the
**Log messages from** parameter.

### **Sample time** — Block sampling time in simulation `0.01` (default) | numeric

Specify the sampling time of the block during simulation. This value defines the
frequency at which the CAN FD Log block runs during simulation. If the
block is inside a triggered subsystem or to inherit sample time, you can specify
`–1` as the sample time. You can also specify a MATLAB variable for sample time. The default value is `0.01`
simulation seconds. For more information, see Timing in Hardware Interface Models.

## Libraries

Vehicle Network Toolbox / CAN FD Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block generates code with limited portability that runs only on the host computer. See
Code Generation.

## Version History

**Introduced in R2018b**

## Description

Log received CAN FD messages

The CAN FD Log block logs CAN FD messages from the CAN network, or messages
sent to the block input port, to a `.mat` file. You can load the saved
messages into MATLAB® for further analysis or into another Simulink® model.

Configure your CAN FD Log block to log from the Simulink input port. For more information, see Log and Replay CAN Messages.

The CAN FD Log block appends the specified filename with the current date
and time, creating unique log files for repeated logging.

If you want to use messages logged using Simulink blocks in the MATLAB Command window, use `canFDMessage` to
convert messages to the correct format.

**Note**

You need a license for both Vehicle Network Toolbox™ and Simulink software to use this block.

**Note**

You cannot have more than one CAN FD Log block in a model using the same
PEAK-System device channel.

### Other Supported Features

- The CAN FD Log block supports the use of Simulink accelerator mode. Using this feature, you can speed up the execution of
  Simulink models. For more information on this feature, see Acceleration (Simulink).
- The CAN FD Log block supports the use of code generation along with
  the packNGo function to group required source code and dependent shared
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
