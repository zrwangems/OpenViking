---
type: simulink-block
title: 'Analog Input'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'analog_input'
documentation_source_path: 'analog_input.html'
language: en
---

# Analog Input

## Ports
```yaml
ports:
- name: Data
  summary: Acquired analog input double
  direction: output
  data_types: double
- name: Relative timestamp
  summary: Relative timestamps of scans
  direction: output
  data_types: double
```

### Output

### **Data** — Acquired analog input double

Acquired analog input data, returned as doubles. If using only one
output port for all channels, each scan is available as a matrix of scan
blocksize by number of channels, M-by-N. If using a port for each
channel, each scan results in a blocksize-by-1 column vector on each
port. Multiple ports are named by channel names or device specified
channel IDs.

**Data Types:** `double`

### **Relative timestamp** — Relative timestamps of scans

Relative timestamp of each scan, returned as a double. This port is
available when you check the Output
relative timestamps parameter.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Device
  summary: Device from which you want to acquire data
  group: ''
- name: Acquisition Mode
  summary: Synchronous setting Asynchronous | Synchronous
  group: ''
- name: Channels
  summary: Device channel selection and configuration options depend on device
  group: ''
- name: Number of ports
  summary: Number of output data ports 1 for all channels | 1 per channel
  group: ''
- name: Input sample rate
  summary: Device sampling rate numeric value
  group: ''
- name: Block size
  summary: Number of scans per time step integer value
  group: ''
- name: Output relative timestamps
  summary: Add timestamp output port
  group: ''
```

Use the Block Parameters dialog box to select your acquisition mode and to set other
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

### **Acquisition Mode** — Synchronous setting **Asynchronous** | **Synchronous**

Synchronous setting, specified as one of the following options.

**Asynchronous** — In asynchronous mode, the data
acquisition from the device and the simulation happen in parallel. The model
initiates the acquisition from the device when the simulation starts. Data
from the device is continuously acquired into a FIFO (first in, first out)
buffer in parallel as the simulation runs. At each time step, the model
fetches data from the FIFO buffer and outputs a block of data. The data in
the FIFO buffer is contiguous according to the hardware acquisition
clock.

**Synchronous** — In synchronous mode, the
simulation is blocked while acquiring data from the device. The model
initiates the acquisition from the device at each time step and immediately
enters a wait state until the acquisition request has completed. This is
unbuffered input; the block outputs the latest block of data at each time
step.

The following diagrams show the difference between synchronous and
asynchronous modes for the Analog Input block.

**Synchronous Analog Input**

Timing of synchronous analog input

At the first time step (T1), the acquisition is initiated for the required
block of data (B1). The simulation does not continue until B1 is completely
acquired.

**Asynchronous Analog Input – Scenario
1**

Timing of asynchronous analog input when faster simulation must be blocked

Scenario 1 shows the case when simulation speed outpaces data acquisition
speed. At the first time step (T1), the required block of data (B1) is still
being acquired. Therefore, the simulation does not continue until B1 is
completely acquired.

**Asynchronous Analog Input – Scenario
2**

Timing of asynchronous analog input without blocking simulation

Scenario 2 shows the case when data acquisition speed outpaces simulation
speed. At the first time step (T1), the required block of data (B1) has been
completely acquired. Therefore, the simulation runs continuously.

**Note**

Several factors, including device hardware and model complexity, can
affect the simulation speed, causing both scenarios 1 and 2 to occur
within the same simulation.

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
such as AC or DC. The coupling type is defined when a device is
selected.

### **Number of ports** — Number of output data ports **1 for all channels** | **1 per channel**

Number of output data ports, specified as:

**1 for all channels** — Output data from a single
port as a matrix, with a size of blocksize by number of channels
selected.

**1 per channel** — Output data from N ports,
where N is equal to the number of selected channels. Each output port is a
column vector with a size of blocksize-by-1. For naming, each output port
uses the channel name if one was specified, otherwise the channel ID, for
example, `ai0`.

### **Input sample rate** — Device sampling rate numeric value

The rate at which samples are acquired from the device, in samples per
second. This is the sampling rate for the hardware. The sample rate must be
a positive real number within the range supported by the selected
hardware.

### **Block size** — Number of scans per time step integer value

The number of data samples to read from the block output at each time step
for each channel. It must be a positive integer greater than or equal to 2,
within the range supported by the selected hardware.

### **Output relative timestamps** — Add timestamp output port

Select this option to output the relative data timestamps, one for each
sample. This option adds a new output port to the block. The data type of
this port is double, and corresponds to the time offset in seconds of the
sample related to the start of acquisition. For asynchronous acquisition,
the acquisition is initiated once at the start of model execution, the
relative timestamp is a monotonically-increasing number relative to the
start of simulation. For synchronous acquisition, an acquisition is
initiated at every time step; as a result, the relative timestamp is reset
to zero every time an acquisition is initiated.
## Libraries

Data Acquisition Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Acquire data from multiple analog channels of data acquisition device

The Analog Input block opens, initializes, configures, and controls an
analog data acquisition device. The opening, initialization, and configuration of the
device occur once at the start of the model execution. During the model run time, the
block acquires data either synchronously (deliver the current block of data the device
is providing) or asynchronously (stream buffered incoming data).

The block has no input ports. It has one or more output ports, depending on the
configuration you choose in its dialog box.

Use the Analog Input block to incorporate live measured data into
Simulink® for:

- System characterization
- Algorithm verification
- System and algorithm modeling
- Model and design validation
- Controller design

The following diagram shows the basic analog input usage configuration, with which you
can:

- Read acquired data at each time step or once per model execution.
- Analyze the data, or use it as input to a system in the model.
- Optionally display results.

Analog Input block connected in a model

**Notes**

To use this block, you need both Data Acquisition Toolbox™ and Simulink software.

Some devices are not supported by the Simulink blocks in Data Acquisition Toolbox. To see if your device supports Simulink, refer to Supported Hardware.

You can use the Analog Input block only with devices that support
clocked acquisition. To acquire data using devices that do not support clocking, use
the Analog Input (Single Sample) block.

### Other Supported Features

- If you have DSP System Toolbox™, you can use this block for signal applications.
- This block supports the use of text accelerator mode, but not Rapid Accelerator or code generation.
- The block supports the use of model referencing, so that your model can
  include other Simulink models as modular components.

For more information on these features, see the Simulink documentation.
