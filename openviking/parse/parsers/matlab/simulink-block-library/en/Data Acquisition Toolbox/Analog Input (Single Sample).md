---
type: simulink-block
title: 'Analog Input (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'analoginputsinglesample'
documentation_source_path: 'analoginputsinglesample.html'
language: en
---

# Analog Input (Single Sample)

## Ports
```yaml
ports:
- name: Data
  summary: Acquired analog input double
  direction: output
  data_types: double
- name: Timestamp
  summary: Timestamp of scan
  direction: output
  data_types: double
```

### Output

### **Data** — Acquired analog input double

Acquired analog input data, returned as doubles. If using only one
output port for all channels, the output is an array of data. If using a
port for each channel, each scan results in a single value on each port.
Multiple ports are named by channel names or device specified channel
IDs.

**Data Types:** `double`

### **Timestamp** — Timestamp of scan

Timestamp of scan, returned as a double. This port is available when
you check the Output
timestamp parameter.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Device
  summary: Device from which you want to acquire data
  group: ''
- name: Channels
  summary: Device channel selection and configuration options depend on device
  group: ''
- name: Number of ports
  summary: Number of output data ports 1 for all channels | 1 per channel
  group: ''
- name: Sample time
  summary: Block execution rate 1 (default)
  group: ''
- name: Output timestamp
  summary: Add timestamp output port
  group: ''
```

Use the Block Parameters dialog box to select your device and to set other
configuration options.

### **Device** — Device from which you want to acquire data

The device from which you want to acquire data. The items in the list
vary, depending on which devices you have connected to your system. Devices
in the list are specified by adaptor or vendor name and unique device ID,
followed by the model name of the device, for example, `ni Dev1
(USB-6255)`. The first available device is selected by default.
A CompactDAQ chassis would be shown as a single device identified by vendor
name, chassis ID, and chassis model; for example, `ni cDAQ2
(cDAQ-9172)`.

### **Channels** — Device channel selection and configuration options depend on device

Device channel selection and configuration table. The channel
configuration table lists the hardware channels of your device, and lets you
select and configure them. Specify which channels to acquire data from (by
default all the channels are selected). The following parameters are
specified for each selected channel:

**Channel ID** — Hardware channel ID specified by
the device. The Channel ID column is read-only, and the parameters are
defined when the device is selected.

**Name** — Channel name. By default the table
displays any names provided by the hardware, but you can edit the names. For
example, if the device is a sound card with two channels, you can name them
`Left` and `Right`.

**Module** — Device ID the channel belongs to. The
Module column is read-only. If a CompactDAQ chassis is selected, it shows
the ID of the CompactDAQ module which the channel belongs to; otherwise the
ID of the device.

**Measurement Type** — Measurement type of the
channel. This block supports only voltage measurement types. (For other
measurement types, use a DataAcquisition object in MATLAB®.)

**Input Range** — Input ranges available for each
channel supported by the hardware, defined when a device is selected.

**Terminal Configuration** — Specifies the
hardware terminal configuration, such as single-ended, differential, etc.
The terminal configuration options are defined by the capabilities of the
selected channel.

**Coupling** — Hardware coupling configuration,
such as AC or DC. The coupling type is defined when a device is selected.

### **Number of ports** — Number of output data ports **1 for all channels** | **1 per channel**

Number of output data ports, specified as:

**1 for all channels** — Outputs the acquired data
from a single port as a 1-by-N vector with a length equal to the number of
channels selected.

**1 per channel** — Outputs the acquired data from
N ports, where N is equal to the number of selected channels. Each port
output is a 1-by-1 double. For naming, each output port uses the channel
name if one was specified, otherwise the channel ID, for example,
`ai0`.

### **Sample time** — Block execution rate 1 (default)

Specifies the sample time of the block during the simulation. This is the
rate at which the block is executed during simulation. The default value is
1 (simulation seconds). For more information, see Timing in Hardware Interface Models and What Is Sample Time? (Simulink).

### **Output timestamp** — Add timestamp output port

Select this option to output the absolute timestamp of the scan. This
option adds a new output port to the block. The data type of this port is
double (datenum), which corresponds to a serial date number. You can convert
the datenum into a datetime value with the `datetime`
function.
## Libraries

Data Acquisition Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Acquire single sample from multiple analog channels of data acquisition device

The Analog Input (Single Sample) block opens, initializes, configures,
and controls an analog data acquisition device. The opening, initialization, and
configuration of the device occur once at the start of the model execution. The block
acquires a single sample every time step, synchronously from the device, during the
model run time.

The block has no input ports. It has one or more output ports, depending on the
configuration you choose in its dialog box.

Use the Analog Input (Single Sample) block to incorporate live measured
data into Simulink® for:

- System characterization
- Algorithm verification
- System and algorithm modeling
- Model and design validation
- Controller design

Analog input acquisition is done synchronously, according to the following
diagram.

Timing of synchronous analog input

At the first time step (T1), data is acquired from the selected hardware channels. The
simulation does not continue until data is read from all channels.

**Notes**

To use this block, you need both Data Acquisition Toolbox™ and Simulink software.

Some devices are not supported by the Simulink blocks in Data Acquisition Toolbox. To see if your device supports Simulink, refer to Supported Hardware.

You can use Analog Input (Single Sample) block only with devices
that support single sample acquisition. If the device does not support single sample
acquisition, the model generates an error. To acquire data from devices that do not
support acquisition of a single sample (such as devices designed for sound and
vibration), use the Analog Input block.

### Other Supported Features

- If you have DSP System Toolbox™, you can use this block for signal applications.
- This block supports the use of text accelerator mode, but not Rapid Accelerator or code generation.
- The block supports the use of model referencing, so that your model can
  include other Simulink models as modular components.

For more information on these features, see the Simulink documentation.
