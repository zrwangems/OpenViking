---
type: simulink-block
title: 'ALSA Audio Playback'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'alsaaudioplayback'
documentation_source_path: 'supportpkg/raspberrypi_ref/alsaaudioplayback.html'
language: en
---

# ALSA Audio Playback

## Ports

### Input

### **Port\_1** — Audio data *N*-by-*C* matrix

The block accepts an *N*-by-*C*
matrix, where *N* is the samples per channel, and
*C* is the number of channels supported by the
audio. The block determines these values from the input signal.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Device name** — ALSA audio output device `'hw:0,0'` (default) | any connected ALSA audio output device

Specify the ALSA audio output device connected to the hardware to which
the block sends data. The default value, `'hw:0,0'`,
specifies that the block sends audio to the default audio jack of the
hardware.

You can send audio to any ALSA audio output device connected to the
hardware. To get the list of audio output devices connected to the hardware,
use the `listAudioDevices`
function as described in List Available ALSA Audio Output Devices.

### **Audio sampling frequency (Hz)** — Audio sample rate `44100` (default) | any positive integer

Specify the sample rate used by the audio device to play audio, in Hz. The
range of **Audio sampling frequency (Hz)** depends on the
connected ALSA audio output device. To find the range of sample rates
supported by the audio output device, use the `listAudioDevices`
function as described in List Available ALSA Audio Output Devices.
However, if you specify a sampling frequency that is not supported by the
device, set the ALSA audio output device as `'plughw:0,0'`
in **Device name**.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Send audio to sound card for playback using ALSA

The ALSA Audio Playback block sends audio data to the audio output
devices, such as speakers or headphones, connected to the hardware. The block uses an
Advanced Linux Sound Architecture (ALSA) driver framework to send audio data.

The block accepts an *N*-by-*C* matrix, where
*N* is the samples per channel, and *C* is the
number of channels supported by the audio. The block determines these values from the
input signal.

**Note**

To use the ALSA Audio Playback block with audio devices that
support more than two channels, you must have an Audio Toolbox™ license.

In the Simulink® model, you can set the ALSA Audio Playback block as the
source of the scheduler interrupt for the Raspberry Pi® hardware. For more information, see Scheduler options.

### Algorithm

Consider a Simulink model that includes a ALSA Audio Capture block and
a ALSA Audio Playback block. The ALSA Audio Capture
reads stereo audio data from the microphone connected to the audio input connector
of the hardware. The block outputs data as a 3-by-2 matrix. At each sample time, the
ALSA Audio Playback block accepts the audio matrix and sends
audio to the headphones connected to the audio output jack of the hardware.

The ALSA Audio Playback block determines the sample time
(*T*s) from the samples per audio
channel (*N*) and sampling frequency
(*F*s).

*T*s = *N*
/ *F*s

For example, if *N* is 4410 samples and *F*s is
44,100 Hz, the block sample time is 4410/44,100 = 0.1 seconds.

*N* is the number of samples per audio channel. The block
determines the value of *N* from the input data.
*F*s is the sampling frequency of the input data specified in
the **Audio sampling frequency (Hz)** parameter.
