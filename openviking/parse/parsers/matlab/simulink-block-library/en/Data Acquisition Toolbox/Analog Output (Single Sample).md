---
type: simulink-block
title: 'Analog Output (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'analogoutputsinglesample'
documentation_source_path: 'analogoutputsinglesample.html'
language: en
---

# Analog Output (Single Sample)

## Ports
```yaml
ports:
- name: Data
  summary: Analog output to generate double
  direction: input
  data_types: double
```

### Input

### **Data** — Analog output to generate double

Analog output to generate, specified as doubles. If using only one input port for
all channels, provide a 1-by-N vector for a single scan on all N channels.

If using a port for each channel, provide a double value to each port. Multiple
ports are named by channel names or device specified channel IDs.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Device
  summary: Device through which you want to output data select available device
  group: ''
- name: Channels
  summary: Device channel selection and configuration options depend on device
  group: ''
- name: Number of ports
  summary: Number of input data ports 1 for all channels | 1 per channel
  group: ''
- name: Sample time
  summary: Block sample time numeric value
  group: ''
```

### **Device** — Device through which you want to output data select available device

The device from which you want to generate data. The items in the list vary,
depending on which devices you have connected to your system. Devices in the list are
specified by adaptor/vendor name and unique device ID, followed by the model name of the
device, for example, `ni Dev1 (USB-6255)`. The first available device
is selected by default. A CompactDAQ chassis is shown as a single device; vendor name,
chassis ID, and chassis model would be shown in the list, for example, `ni cDAQ2
(cDAQ-9172)`.

### **Channels** — Device channel selection and configuration options depend on device

Device channel selection and configuration table. The channel configuration table
lists the hardware channels of your device, and lets you select and configure them.
Specify which channels to acquire data from (by default all the channels are selected).
The following parameters are specified for each selected channel:

**Channel ID** — Hardware channel ID specified by the
device. The Channel ID column is read-only, and the parameters are defined when the
device is selected.

**Name** — Channel name. By default the table displays any
names provided by the hardware, but you can edit the names. For example, if the device
is a sound card with two channels, you can name them `Left` and
`Right`.

**Module** — Device ID the channel belongs to. The Module
column is read-only. If a CompactDAQ chassis is selected, it shows the ID of the
CompactDAQ module which the channel belongs to; otherwise the ID of the device.

**Measurement Type** — Measurement type of the channel. This
block supports only voltage measurement types. (For other measurement types, use a
DataAcquisition object in MATLAB®.)

**Output Range** — Output ranges available for each channel
supported by the hardware, defined when a device is selected.

### **Number of ports** — Number of input data ports **1 for all channels** | **1 per channel**

Number of input data ports, specified as:

**1 for all channels** (default) — One input port on the
block provides data for all channels. Provide data as a 1-by-N vector for N
channels.

**1 per channel** — N input ports on the block, where N is
equal to the number of selected channels. Provide data as a double value to each port.
For naming, each output port uses the channel name if one was specified, otherwise the
channel ID, for example, `ao1`.

### **Sample time** — Block sample time numeric value

Block sample time, specifies the sample time of the block during the simulation.
This is the rate at which the block is executed during simulation. The default value is
1 (simulation seconds). For more information, see Timing in Hardware Interface Models and What Is Sample Time? (Simulink).
## Libraries

Data Acquisition Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Output single sample to multiple analog channels of data acquisition device

The Analog Output (Single Sample) block opens, initializes, configures, and
controls an analog data acquisition device. The opening, initialization, and configuration of
the device occur once at the start of the model execution. The block outputs a single sample
every time step, synchronously to the hardware, during the model run time.

The block has one or more input ports, depending on the option you choose in its dialog
box. It has no output ports. The valid data type of the signal at the input port is
double.

The Analog Output (Single Sample) block inherits the sample time from the
driving block connected to the input port. Analog output is done synchronously, according to
the following diagram.

Timing of synchronous analog output

At the first time step (T1), data is output to the selected hardware channels. The
simulation does not continue until data is output to all channels.

**Notes**

To use this block, you need both Data Acquisition Toolbox™ and Simulink® software.

You can use the Analog Output (Single Sample) block only with devices
that support single sample output. To send data using devices that do not support
acquisition of a single sample (such as devices designed for sound and vibration), use the
Analog Output block.

Some devices are not supported by the Simulink blocks in Data Acquisition Toolbox. To see if your device supports Simulink, refer to Supported Hardware.

### Other Supported Features

- This block supports the use of text accelerator mode, but not Rapid Accelerator or code generation.
- The block supports the use of model referencing, so that your model can include
  other Simulink models as modular components.

For more information on these features, see the Simulink
documentation.
