---
type: simulink-block
title: 'ALSA Audio Capture'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'alsaaudiocapture'
documentation_source_path: 'nvidia/ref/alsaaudiocapture.html'
language: en
---

# ALSA Audio Capture

## Ports

### Output

### **Port\_1** — Audio data *N*-by-*C* matrix

The block outputs the audio data as an
*N*-by-*C* matrix, where *N* is
the samples per channel, and *C* is the number of channels supported
by the audio. Specify the values of *N* and *C* in
the **Samples per frame (N)** and **Number of channels
(C)** parameters, respectively.

For example, for a stereo audio source file with three samples per channel, the
block organizes the audio data into a 3-by-2 matrix.

Block diagram show data layout from ALSA audio capture block

The data type of the output matrix is of the type specified in the
**Device Bit depth** parameter.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Device name** — ALSA audio input device `'hw:1,0'` (default) | valid ALSA audio input device

Specify the ALSA audio input device connected to the hardware from which the block
reads audio data.

You can receive audio from an ALSA audio input device connected to the hardware. To
get the list of audio input devices connected to the hardware, use the `listAudioDevices` function as described in List Available ALSA Audio Input Devices.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `deviceStr` |
| **Type:** character vector |
| **Values:** `valid name`| |
| **Default:**  `'hw:1,0'` |

### **Device Bit depth** — Audio data type `16-bit integer` (default) | `8-bit integer` | `32-bit integer`

Before performing analog-to-digital conversion, the audio data is cast to the data
type specified in this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataBitDepth` |
| **Type:** character vector |
| **Values:** `'16-bit integer'`|`'8-bit integer'``'32-bit integer'` |
| **Default:**  `'16-bit integer'` |

### **Number of channels (C)** — Number of channels supported `2` (default) | positive integer

To find the number of channels supported by the audio input device, use the
`listAudioDevices` function as described in List Available ALSA Audio Input Devices.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numberofChannels` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:**  `'2'` |

### **Audio sampling frequency (Hz)** — Audio sample rate `44100` (default) | positive integer

Specify the sample rate used by the audio input device to read audio data, in Hz.
The sample rates listed in the **Audio sampling frequency (Hz)**
parameter depends on the audio input device. To find the sample rates supported by the
audio input device, use the `listAudioDevices` function as described in List Available ALSA Audio Input Devices.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleRateEnum` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:**  `'44100'` |

### **Samples per frame (N)** — Number of samples per audio channel `4410` (default) | positive integer

This parameter specifies the number of rows of the output matrix that the block
outputs. The output matrix has dimensions *N*-by-*C*,
where *N* is the number of samples per channel, and
*C* is the number of channels.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `frameSize` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:**  `'4410'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Capture audio from sound card using ALSA

The ALSA Audio Capture block reads audio data from the audio input device
connected to the NVIDIA® hardware. The block uses the Advanced Linux Sound Architecture (ALSA) driver
framework to read audio data.

The block outputs the audio data as an *N*-by-*C*
matrix, where *N* is the samples per audio channel, and *C*
is the number of channels supported by the audio device. Specify the values for
*N* and *C* in the **Samples per frame
(N)** and **Number of channels (C)** parameters,
respectively.

**Note**

To use the ALSA Audio Capture block with audio devices that support more
than two channels, you must have an Audio Toolbox™ license.

### Algorithm

Consider a Simulink® model that includes an ALSA Audio Capture block and an ALSA Audio
Playback block. At each sample time, the ALSA Audio Capture reads
stereo audio data from the microphone connected to the audio input connector of the
hardware. The block outputs data as a 3-by-2 matrix. The ALSA Audio Playback
block accepts the audio matrix and sends audio to the headphones connected to the audio
output jack of the hardware.

Sample workflow diagram for the audio blocks

The ALSA Audio Capture block determines the sample time
(*T*s) from the samples per audio channel
(*N*) and sampling frequency (*F*s).

*T*s = *N* /
*F*s

For example, if *N* is 4410 samples and *F*s is 44,100
Hz, the block sample time is 4410/44,100 = 0.1 seconds.

*N* is the number of samples per audio channel specified in the
**Number of channels (C)** parameter. *F*s is the
sampling frequency of audio data specified in the **Audio sampling frequency
(Hz)** parameter.
