---
type: simulink-block
title: 'Digital Output (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'digitaloutputsinglesample'
documentation_source_path: 'digitaloutputsinglesample.html'
language: en
---

# Digital Output (Single Sample)

## Ports

### Input

### **Data** — Generated digital output data boolean

Generated digital output data, specified as booleans. If using only one input port
for all lines, provide a 1-by-N vector of data. If using a port for each line, provide
a single value on each port. Multiple ports are named by line names or device
specified line IDs.

**Data Types:** `Boolean`

## Parameters

### **Device** — Device with which you want to generate data

The device from which you want to acquire data. The items in the list vary,
depending on which devices you have connected to your system. Devices in the list are
specified by adaptor or vendor name and unique device ID, followed by the model name of
the device, for example, `ni Dev1 (USB-6255)`. The first available
device is selected by default. A CompactDAQ chassis would be shown as a single device
identified by vendor name, chassis ID, and chassis model; for example, `ni cDAQ2
(cDAQ-9172)`.

### **Lines** — Device line selection and configuration options depend on device

**Line ID** — ID of the hardware line (for example,
port0/line0). This is automatically detected and filled in by the selected device, and
is read-only.

**Name** — Hardware line name. This is automatically
detected and filled in from the hardware, though you can edit the name.

**Module** — Device ID that the line belongs to. The Module
column is read-only. If a CompactDAQ chassis is selected, it shows the ID of the
CompactDAQ module which the line belongs to; otherwise the ID of the device.

### **Number of ports** — Number of input data ports **1 for all lines** | **1 per line**

Number of input data ports, specified as:

**1 for all lines** — The block has only one input port for
all of the lines that are selected in the table. Generated data is defined as a 1-by-N
row vector of boolean values, whose size is the number of lines.

**1 per line** — The block has one input port per selected
line. The name of each input port is the name specified in the table for each line. If
no name is provided, the name is the Line ID. For example, if line 2 of hardware port 3
is selected, and you did not specify a name in the line table,
`port3/line2` appears in the block. Data size for each line is
1-by-1.

### **Sample time** — Block execution rate 1 (default)

Specifies the sample time of the block during the simulation. This is the rate at
which the block is executed during simulation. The default value is 1 (simulation
seconds). For more information, see Timing in Hardware Interface Models and What Is Sample Time? (Simulink).

## Libraries

Data Acquisition Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Output single sample to multiple digital lines of data acquisition device

The Digital Output (Single Sample) block synchronously outputs the latest set of data to
the hardware at each simulation time step. It outputs unbuffered digital data. Specify the
output data as a vector of boolean values.

The block has no output ports. It can have one or more input ports, depending on the
option you choose in its dialog box. The data type of the signal at the input port must be a
boolean data type.

The Digital Output (Single Sample) block inherits the sample time from the driving block
connected to the input port. Digital output is done synchronously, according to the following
diagram.

Timing of synchronous digital output

At the first time step (T1), data is output to the selected hardware lines. The simulation
does not continue until data is output to all lines.

**Note**

To use this block, you need both Data Acquisition Toolbox™ and Simulink® software.

Some devices are not supported by the Simulink blocks in Data Acquisition Toolbox. To see if your device supports Simulink, refer to Supported Hardware.

### Other Supported Features

- This block supports the use of text accelerator mode, but not Rapid Accelerator or code generation.
- The block supports the use of model referencing, so that your model can include
  other Simulink models as modular components.

For more information on these features, see the Simulink
documentation.
