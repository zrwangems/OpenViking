---
type: simulink-block
title: 'Audio File Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'audiofileread'
documentation_source_path: 'supportpkg/raspberrypi_ref/audiofileread.html'
language: en
---

# Audio File Read

## Ports

### Output

### **Port\_1** — Audio data *N*-by-*C* matrix

The block outputs the audio data as *N*-by-*C* matrix,
where *N* is the samples per channel, and *C* is
the number of channels supported by the audio.

For example, for a stereo audio source file with the **Samples
per audio channel (N)** parameter set to `3`,
the block organizes the audio data into a 3-by-2 matrix, which represents
a 2-channel signal containing three samples per channel.

Specify *N* with the **Samples per
audio channel (N)** parameter. The number of channels, *C*,
supported by the selected audio file is displayed in the block when
you browse for the audio file using the **File name** parameter.

When the number of times the audio is played exceeds the value specified in the
**Number of times to play file** parameter, the
**Port\_1** port outputs `0` every
sample time. For example, if you set the **Number of times to
play file** parameter to `3`, the
**Port\_1** port outputs zeros after the audio file
is played three times.

**Data Types:** `int16`

### **EOF** — End of audio file indicator `0` | `1`

The port outputs `1` when the last audio sample
is output from the block. Otherwise, the port outputs `0`.

#### Dependencies

To enable the port, select the **Output end of audio
indicator** parameter.

**Data Types:** `Boolean`

## Parameters

### **File name** — Name of audio file `guitartune.wav` (default)

If the location of the file does not appear on your MATLAB® path, click **Browse** to specify the full
path. If the location of this file does appear on your MATLAB path, enter only the file name.

### **Number of times to play file** — Number of times to play the audio file `inf` (default) | any integer value greater than 0

Enter `inf` to play the file until you stop the
simulation.

### **Output end of audio indicator** — Determine whether the output is the last audio sample in the audio file `off` (default) | `on`

The `EOF` port outputs `1` when the last
audio sample is output from the block. Otherwise, the port outputs
`0`.

### **Samples per audio channel(N)** — Number of samples per audio channel `4410` (default) | any integer value greater than 0

This parameter specifies the number of rows of the output matrix that the
block outputs. The output matrix has dimensions
*N*-by-*C*, where *N*
is the number of samples per channel, and *C* is the number
of channels.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Read audio frames from an audio file

The Audio File Read block copies an audio source
file and outputs the audio data into your model. The audio data can
be played on a loop multiple times, as specified by the **Number
of times to play file** parameter. The audio data can consist
of one or more channels, *C*. A mono audio source
file has only one channel, and a stereo audio source file has two
channels. The audio data is output from the block as *N* consecutive
samples of audio data.

### Algorithm

The Audio File Read block determines the sample
time (*T*s) from the samples
per audio channel (*N*) and sampling frequency (*F*s)
of the selected audio file.

*T*s = *N* / *F*s

For example, if *N* is 4410 samples and *F*s
is 44,100 Hz, the block sample time is 4410/44,100 = 0.1 seconds.

*N* is the value that you specify in the **Samples
per audio channel (N)** parameter. *F*s
of the selected audio file is automatically displayed on the block
when you browse the file using the **File name** parameter.
