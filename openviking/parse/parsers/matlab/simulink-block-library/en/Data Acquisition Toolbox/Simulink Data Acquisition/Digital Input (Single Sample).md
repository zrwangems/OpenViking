---
type: simulink-block
title: 'Digital Input (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: 'Simulink Data Acquisition'
documentation_page: 'digitalinputsinglesample'
documentation_source_path: 'digitalinputsinglesample.html'
language: en
---

# Digital Input (Single Sample)

## Ports

### Output

### **Data** — Acquired digital input boolean

Acquired digital input data, returned as booleans. If using only one output port
for all lines, the output is a 1-by-N vector for N channels. If using a port for each
line, each scan results in a single boolean on each port. Multiple ports are named by
line names or device specified line IDs.

**Data Types:** `Boolean`

### **Timestamp** — Timestamp of scan double

Timestamp of scan, returned as a double. This port is available when you check the
Output timestamp
parameter.

**Data Types:** `double`

## Parameters

### **Device** — Device from which you want to acquire data

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

### **Number of ports** — Number of output data ports **1 for all lines** | **1 per line**

Number of output data ports, specified as:

**1 for all lines** — The block has only one output port for
all of the lines that are selected in the table. Acquired data is returned as a 1-by-N
vector of boolean values, whose size is the number of lines.

**1 per line** — The block has one output port per selected
line. Data is returned as a 1-by-1 boolean value on each port. The name of each output
port is the name specified in the table for each line. If no name is provided, the name
is the Line ID. For example, if line 2 of hardware port 3 is selected, and you did not
specify a name in the line table, `port3/line2` appears in the block.
Data size for each line is 1-by-1.

### **Sample time** — Block execution rate 1 (default)

Specifies the sample time of the block during the simulation. This is the rate at
which the block is executed during simulation. The default value is 1 (simulation
seconds). For more information, see Timing in Hardware Interface Models and What Is Sample Time? (Simulink).

### **Output timestamp** — Add timestamp output port

Select this option to output the absolute timestamp of the scan. This option adds a
new output port to the block. The data type of this port is double (datenum), which
corresponds to a serial date number. You can convert the datenum into a datetime value
with the `datetime` function.

## Libraries

Data Acquisition Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Acquire single sample from multiple digital lines of data acquisition device

The Digital Input (Single Sample) block synchronously outputs the latest
scan of data available from the digital lines selected at each simulation time step. It
acquires unbuffered digital data, and delivers this as a vector of boolean values.

The block has no input ports. It has one or more output ports, depending on the option you
choose in its dialog box.

The block inherits the sample time of the model. Digital input acquisition is done
synchronously, according to the following diagram.

Timing of synchronous digital input

At the first time step (T1), data is acquired from the selected hardware lines. The
simulation does not continue until data is read from all lines.

**Note**

To use this block, you need both Data Acquisition Toolbox™ and Simulink® software.

Some devices are not supported by the Simulink blocks in Data Acquisition Toolbox. To see if your device supports Simulink, refer to Supported Hardware.

### Other Supported Features

- This block supports the use of text accelerator mode, but not Rapid Accelerator or code generation.
- The block supports the use of model referencing, so that your model can include
  other Simulink models as modular components.

For more information on these features, see the Simulink
documentation.
