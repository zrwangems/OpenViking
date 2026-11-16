---
type: simulink-block
title: 'Audio Device Reader'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'audiodevicereader'
documentation_source_path: 'ref/audiodevicereader.html'
language: en
---

# Audio Device Reader

## Ports

### Output

### **A** — Output signal scalar | vector | matrix

The output of the Audio Device
Reader block is determined by the block’s
parameters. If the block output is a matrix, the
columns correspond to independent channels.

**Data Types:** `single` | `double` | `int16` | `int32` | `uint8`

### **O** — Number of samples overrun scalar

This port outputs the number of samples
overrun while acquiring a frame of data (one
output matrix).

#### Dependencies

To enable this port, select the
**Output number of samples
overrun** parameter.

**Data Types:** `uint32`

## Parameters

#### Main Tab

### **Driver** — Driver used to access your audio device `DirectSound` (default) | `ASIO` | `WASAPI`

- ASIO drivers do not come pre-installed on
  Windows machines. To use the
  `ASIO` driver option,
  install an ASIO driver outside of MATLAB®.

  **Note**

  If **Driver** is set to
  `ASIO`, open the ASIO UI
  outside of MATLAB to set the sound card buffer size to
  the value specified by the **Samples per
  frame** parameter. See the documentation
  of your ASIO driver for more information.
- WASAPI drivers are supported for
  exclusive-mode only.

ASIO and WASAPI drivers do not provide
sample rate conversion. For ASIO and WASAPI
drivers, set **Sample rate (Hz)**
to a sample rate supported by your audio
device.

This parameter applies only on Windows
machines. Linux machines always use the ALSA
driver. Mac machines always use the CoreAudio
driver.

### **Device** — Device used to acquire audio samples default audio device (default)

The device list is populated with devices
available on your computer.

### **Info** — View information about your audio input configuration button

This button opens a dialog box that lists
your selected audio driver, the full name of your
audio device, and the maximum input channels for
your configuration. For example:

### **Sample rate (Hz)** — Sample rate your device uses to acquire audio data `44100` (default) | integer

The possible range of **Sample rate
(Hz)** depends on your audio
hardware.

### **Number of channels** — Number of channels acquired by your audio device `1` (default) | integer

The number of input channels is also the
number of channels (matrix columns) output by the
Audio Device Reader block.

#### Dependencies

To specify which input channels your audio
device acquires, on the
**Advanced** tab, select the
**Use default channel mapping**
parameter.

### **Samples per frame** — Frame size read from audio device `1024` (default) | integer

**Samples per frame** is
also the device buffer size, and the frame size
(number of matrix rows) output by the Audio
Device Reader block.

#### Advanced Tab

### **Device bit depth** — Data type used by device to acquire audio data `16-bit integer` (default) | `8-bit integer` | `16-bit integer` | `24-bit integer` | `32-bit integer`

Data type used by device to acquire audio
data, specified as a character vector or
string.

### **Use default channel mapping** — Toggle channel mapping source on (default) | off

When you select this parameter, the block
uses the default mapping between the sound card’s
input channels and the matrix columns output by
this block. When you clear this parameter, you
specify the mapping in **Device input
channels**.

### **Device input channels** — Specify nondefault channel mapping `[1:MaximumInputChannels]` (default) | scalar | vector

Nondefault map of device channels and matrix
output by the Audio Device Reader
block, specified as a scalar or vector. For
example:

If **Device input
channels** is specified as
`1:3`, then:

- Channel 1 maps to the first column of the
  output matrix.
- Channel 2 maps to the second column of the
  output matrix.
- Channel 3 maps to the third column of the
  output matrix.

If **Device input
channels** is specified as
`[3,1,2]`, then:

- Channel 3 maps to the first column of the
  output matrix.
- Channel 1 maps to the second column of the
  output matrix.
- Channel 2 maps to the third column of the
  output matrix.

#### Dependencies

To specify a nondefault mapping, clear the
**Use default channel mapping**
parameter.

### **Output number of samples overrun** — Specify additional output port for number of samples overrun off (default) | on

When you select this parameter, an
additional output port, **O**, is
added to the block. The **O**
port outputs the number of samples overrun while
acquiring a frame of data (one output
matrix).

### **Output data type** — Data type output from block `double` (default) | `single` | `int32` | `int16` | `uint8`

Data type of the output.

**Note**

If this parameter is specified as
`double` or
`single`, the block outputs data
in the range [–1, 1]. For other data types, the
range is [min, max] of the specified data
type.

## Libraries

Audio Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Supports 16- and 32-bit signed and 8-bit unsigned integers. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The executable generated from this block relies on prebuilt
dynamic library files (.dll files) included with MATLAB. Use the `packNGo` function
to package the code generated from this object and all the
relevant files in a compressed zip file. Using this zip
file, you can relocate, unpack, and rebuild your project in
another development environment where MATLAB is not installed. For more details, see Run Audio I/O Features Outside MATLAB and Simulink.

## Version History

**Introduced in R2016a**

## Description

Record from sound card

The Audio Device Reader block reads audio samples using
your computer's audio device. The Audio Device Reader
block specifies the driver, the device and its attributes, and the
data type and size output from your Audio Device Reader block.
