---
type: simulink-block
title: 'ALSA Audio Playback'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'alsaaudioplayback'
documentation_source_path: 'nvidia/ref/alsaaudioplayback.html'
language: en
---

# ALSA Audio Playback

## Ports

### Input

### **Port\_1** — Audio data *N*-by-*C* matrix

The block accepts an *N*-by-*C* matrix, where
*N* is the samples per channel, and *C* is the
number of channels supported by the audio. The block determines these values from the
input signal.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Device name** — ALSA audio output device `'hw:0,0'` (default) | valid ALSA audio output device

Specify the ALSA audio output device connected to the hardware to which the block
sends data. The default value, `'hw:0,0'`, specifies that the block
sends audio to the default audio jack of the hardware.

You can send audio to an ALSA audio output device connected to the hardware. To get
the list of audio output devices connected to the hardware, use the `listAudioDevices` function as described in List Available ALSA Audio Output Devices.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `deviceStr` |
| **Type:** character vector |
| **Values:** `valid name`| |
| **Default:**  `'hw:0,0'` |

### **Audio sampling frequency (Hz)** — Audio sample rate `44100` (default) | positive integer

Specify the sample rate used by the audio device to play audio, in Hz. The range of
**Audio sampling frequency (Hz)** depends on the connected ALSA audio
output device. To find the range of sample rates supported by the audio output device,
use the `listAudioDevices` function as described in List Available ALSA Audio Output Devices. However, if you
specify a sampling frequency that is not supported by the device, set the ALSA audio
output device as `'plughw:0,0'` in **Device
name**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleRateEnum` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:**  `'44100'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Send audio to sound card for playback using ALSA

The ALSA Audio Playback block sends audio data to the audio output devices,
such as speakers or headphones, connected to the NVIDIA® hardware. The block uses an Advanced Linux Sound Architecture (ALSA) driver
framework to send audio data.

The block accepts an *N*-by-*C* matrix, where
*N* is the samples per channel, and *C* is the number of
channels supported by the audio. The block determines these values from the input
signal.

**Note**

To use the ALSA Audio Playback block with audio devices that support more
than two channels, you must have an Audio Toolbox™ license.
