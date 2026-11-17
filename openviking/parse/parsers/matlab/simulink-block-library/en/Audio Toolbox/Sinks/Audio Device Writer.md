---
type: simulink-block
title: 'Audio Device Writer'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'audiodevicewriter'
documentation_source_path: 'ref/audiodevicewriter.html'
language: en
---

# Audio Device Writer

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double | int16 | int32 | uint8
- name: Port_1
  summary: Number of samples underrun scalar
  direction: output
  data_types: uint32
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix

If input to the Audio Device Writer block is of data
type `double` or `single`, the block
clips values outside the range [–1, 1]. For other data types, the
allowed input range is [min, max] of the specified data type.

**Data Types:** `single` | `double` | `int16` | `int32` | `uint8`
### Output

### **Port\_1** — Number of samples underrun scalar

This port outputs the number of samples underrun while writing a frame
of data (one input matrix).

#### Dependencies

To enable this port, select the **Output number of samples
underrun** parameter.

**Data Types:** `uint32`
## Parameters
```yaml
parameters:
- name: Driver
  summary: Driver used to access your audio device DirectSound (default) | ASIO | WASAPI
  group: ''
- name: Device
  summary: Device used to play audio samples default audio device (default)
  group: ''
- name: Info
  summary: View information about your audio output configuration button
  group: ''
- name: Inherit sample rate from input
  summary: Specify source of input sample rate on (default) | off
  group: ''
- name: Sample rate (Hz)
  summary: Sample rate used by device to play audio data 44100 (default) | positive scalar
  group: ''
- name: Device bit depth
  summary: Data type used by device to perform digital-to-analog conversion 16-bit integer (default) | 8-bit integer | 24-bit
    integer | 32-bit float
  group: ''
- name: Use default channel mapping
  summary: Toggle channel mapping source on (default) | off
  group: ''
- name: Device output channels
  summary: Specify nondefault channel mapping [1:MaximumOutputChannels] (default) | scalar | vector
  group: ''
- name: Output number of samples underrun
  summary: Specify output port for number of samples underrun off (default) | on
  group: ''
```

#### Main Tab

### **Driver** — Driver used to access your audio device `DirectSound` (default) | `ASIO` | `WASAPI`

- ASIO drivers do not come pre-installed on Windows machines. To use
  the `ASIO` driver option, install an ASIO
  driver outside of MATLAB®.

  **Note**

  If **Driver** is set to
  `ASIO`, open the ASIO UI
  outside of MATLAB to set the sound card buffer size to the frame
  size (number of rows) input to the Audio Device
  Writer block. See the documentation of your ASIO
  driver for more information.
- WASAPI drivers are supported for exclusive-mode only.

ASIO and WASAPI drivers do not provide sample rate conversion. For ASIO
and WASAPI drivers, supply an audio stream with a sample rate supported by
your audio device.

This parameter applies only on Windows machines. Linux machines always use
the ALSA driver. Mac machines always use the CoreAudio driver.

To specify nondefault **Driver** values, you must have an
Audio Toolbox™ license.

### **Device** — Device used to play audio samples default audio device (default)

The device list is populated with devices available on your
computer.

### **Info** — View information about your audio output configuration button

This button opens a dialog box that lists your selected audio driver, the
full name of your audio device, and the maximum output channels for your
configuration. For example:

### **Inherit sample rate from input** — Specify source of input sample rate on (default) | off

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in **Sample rate (Hz)**.

### **Sample rate (Hz)** — Sample rate used by device to play audio data `44100` (default) | positive scalar

The possible range of **Sample rate (Hz)** depends on
your audio hardware.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

#### Advanced Tab

### **Device bit depth** — Data type used by device to perform digital-to-analog conversion `16-bit integer` (default) | `8-bit integer` | `24-bit integer` | `32-bit float`

Before performing digital-to-analog conversion, the input data is cast to
a data type specified by this parameter.

**Note**

To specify a nondefault **Device bit depth**, you
must have an Audio Toolbox license.

### **Use default channel mapping** — Toggle channel mapping source on (default) | off

When you select this parameter, the block uses the default mapping between
columns of the matrix input to this block and the channels of your device.
When you clear this parameter, you specify the mapping in **Device
output channels**.

### **Device output channels** — Specify nondefault channel mapping `[1:MaximumOutputChannels]` (default) | scalar | vector

Nondefault mapping between columns of matrix input to the Audio
Device Writer block and channels of output device, specified as
a scalar or vector. For example:

If **Device output channels** is specified as
`1:3`, then:

- The first column of the input matrix maps to channel 1.
- The second column of the input matrix maps to channel
  2.
- The third column of the input matrix maps to channel 3.

If **Device output channels** is specified as
`[3,1,2]`, then:

- The first column of the input matrix maps to channel 3.
- The second column of the input matrix maps to channel
  1.
- The third column of the input matrix maps to channel 2.

**Note**

To selectively map between columns of the input matrix and your sound
card's output channels, you must have an Audio Toolbox license.

#### Dependencies

To enable this parameter, clear the **Use default mapping
between columns of input of this block and sound card’s output
channels** parameter.

### **Output number of samples underrun** — Specify output port for number of samples underrun off (default) | on

When you select this parameter, an output port is added to the block. The
port outputs the number of samples underrun while writing a frame of data
(one input matrix).
## Libraries

Audio Toolbox / Sinks DSP System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Supports 16- and 32-bit signed and 8-bit unsigned integers. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The following code generation limitations apply:

- Host computer only. Excludes Simulink®
  Desktop Real-Time™ code generation.
- The executable generated from this block relies on prebuilt dynamic
  library files (`.dll` files) included with MATLAB. Use the `packNGo` function to package the
  code generated from this block and all the relevant files in a compressed
  zip file. Using this zip file, you can relocate, unpack, and rebuild your
  project in another development environment where MATLAB is not installed. For more details, see Run Audio I/O Features Outside MATLAB and Simulink.

## Version History

**Introduced in R2016a**

## Description

Play to sound card

The Audio Device Writer block writes audio samples to an audio output
device.

Parameters of the Audio Device Writer block specify the driver, the
device, and device attributes such as sample rate and bit depth.
