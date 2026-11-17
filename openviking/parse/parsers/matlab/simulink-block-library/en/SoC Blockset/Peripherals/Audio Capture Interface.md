---
type: simulink-block
title: 'Audio Capture Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'audiocaptureinterface'
documentation_source_path: 'ref/audiocaptureinterface.html'
language: en
---

# Audio Capture Interface

## Ports
```yaml
ports:
- name: data
  summary: Data frame from captured audio *M*-element vector | *M*-by-*C* matrix
  direction: input
  data_types: int8 | int16 | int32
- name: event
  summary: Task event signal scalar
  direction: output
  data_types: rteEvent
- name: msg
  summary: SoC message data scalar
  direction: output
  data_types: SoCData
```

### Input

### **data** — Data frame from captured audio *M*-element vector | *M*-by-*C* matrix

To provide a single audio channel, specify this data as an
*M*-element audio data frame, where *M* defines the
number of samples of audio data per frame. To provide multiple audio channels
provided, specify data as an *M*-by-*C* matrix,
where *C* defines the number of channels.

#### Dependencies

To enable this port, set the **Input** parameter to
`From input port`.

**Data Types:** `int8` | `int16` | `int32`
### Output

### **event** — Task event signal scalar

This port sends a message after a frame of audio samples is captured for all
channels. This output connects to the input of the Task Manager
block to execute the associated event-driven task.

#### Dependencies

To enable this port, select the **Show event port**
parameter.

**Data Types:** `rteEvent`

### **msg** — SoC message data scalar

This port outputs data messages containing audio data to a connected Audio Capture
block.

**Data Types:** `SoCData`
## Parameters
```yaml
parameters:
- name: Input
  summary: Source of simulated audio data From dialog (default) | From input port | From timeseries object
  group: ''
- name: Value
  summary: Audio data to be output int16([1 2 3 4 5 6 7 8]) (default) | *CN*-length vector
  group: ''
- name: Object name
  summary: Timeseries object [ ] (default) | MATLAB workspace variable
  group: ''
- name: Sample time
  summary: Sample time in seconds -1 (default) | positive scalar
  group: ''
- name: Show event port
  summary: Option to enable task event ports off (default) | on
  group: ''
```

### **Input** — Source of simulated audio data `From dialog` (default) | `From input port` | `From timeseries object`

Specify the source of the simulated audio data.

### **Value** — Audio data to be output `int16([1 2 3 4 5 6 7 8])` (default) | *C**N*-length vector

Specify the audio data as a *C**N*-length vector
representing the audio frames for all channels, where *N* is the number
of samples per frame and *C* is the number of audio channels. The
samples for each channel are contiguous.

### **Object name** — Timeseries object [ ] (default) | `MATLAB workspace variable`

Specify the audio data as a timeseries object defined in the MATLAB® workspace.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

Enter the sample time defining the rate at which to output the message containing
audio data.

### **Show event port** — Option to enable task event ports `off` (default) | `on`

Select this parameter to enable an event port that, when connected to the Task Manager
block, can execute event-driven tasks.
## Libraries

SoC Blockset / Peripherals

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

Embedded Coder does not generate code for this block. In the
generated code, the advanced Linux sound architecture (ALSA) driver framework performs audio
capture on the device. The related Audio Capture block
represents the ALSA driver. For more information on the ALSA driver framework, see the Advanced
Linux Sound Architecture website.

## Version History

**Introduced in R2021a**

## Description

Simulate capture of sample from audio stream on hardware

The Audio Capture Interface block simulates the behavior of an audio input
device. The block outputs audio samples as a message to a connected Audio Capture block
that simulates audio driver code and connects to your algorithm. The block can also emit an
event that, when connected to a Task Manager block, can
trigger a task containing the Audio Capture block.
