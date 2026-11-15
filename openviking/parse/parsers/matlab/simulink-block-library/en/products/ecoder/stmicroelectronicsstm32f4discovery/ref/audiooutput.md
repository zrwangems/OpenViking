---
type: simulink-block
title: 'Audio Output'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Multimedia'
documentation_page: 'audiooutput'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/audiooutput.html'
language: en
---

# Audio Output

## Ports

### Input

### **Port\_1** — Input port containing PCM audio samples in frames matrix

The block accepts `[NxM]` or `[MxN]``int16` PCM
audio frames. `N` is the number of samples per frame. `M` is
the number of audio channels in the signal.

The maximum number of audio channels supported is 2 for STM32F746G and 4 for STM32F769I. For
STM32F746G, the block supports audio frames in mono:
(`[Nx1]` or `[1xN]`) format and
stereo: (`[Nx2]` or `[2xN]`) format.
For STM32F769I, the block supports audio frames in quad:
`[4xN]` or `[Nx4]`. The values of
`M` and `N` are determined from
the incoming audio frames at the input port.

The block interprets an `N`-by-`2` matrix as a
multichannel signal with `2` independent
channels and `N` samples per channel. For example,
the block interprets a sequence of
`5`-by-`2` matrices as a
two-channel signal with a frame size of 5.

**Data Types:** `int16`

## Parameters

### **Device** — Device to send the audio data to `Headphone` (default) | `Speaker` | `Both`

Select the audio device to which the block sends audio data.

### **Sampling frequency (Hz)** — Sampling frequency to write audio signal to the audio device `8000` | `11025` | `16000` | `22050` | `32000` | `44100 (default for STM32F769I)` | `48000 (default for STM32F746G)` | `96000` | `192000(STM32F746G only)`

Specify the number of samples per second to write to the audio
device that you specify in the **Device** parameter.

### **Volume** — Loudness of the audio signal at the output `90 (default for STM32F746G)` | `80 (default for STM32F769I)` | `integer between 0 and 100`

The block applies gain to the value that you specify in this
parameter. The gain is calculated as:

(Volume\*63) /100

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Send processed audio samples to audio devices on STMicroelectronics STM32F746G/STM32F769I– Discovery board

The Audio Output block writes the processed audio data to
the audio device (headphones or speakers) that are connected to the processor on the
STM32F746G/STM32F769I–Discovery™ board.

The block accepts `int16` Pulse Code Modulated (PCM) audio frames. For
STM32F746G, these frames are either mono: (`[1xN]` or
`[Nx1]`) or stereo: (`[2xN]` or
`[Nx2]`) `int16` matrix. For STM32F769I, these
frames are quad: `[4xN]` or `[Nx4]`.
`N` is the number of samples per frame from the input signal, and
`2` and `4` are the number of audio channels per
frame.

You can send audio samples at different rates, such as 8 kHz, 11 kHz, 16 kHz, 22 kHz, 32 kHz,
44 kHz, 48 kHz, 96 kHz, and 192 kHz (STM32F746G only), with different sampling
frequencies.

Using the parameters of this block, you specify the device to
which you want to send the audio. You also specify the volume level
at which the block emits audio frames.

### Write Audio to Headphone or Speaker

The STM32F746G–Discovery board sends audio to audio devices, headphones or speakers, or both,
that are connected to it.

The `int16` PCM audio frames from the input port of the Audio
Output block instance are streamed through the ARM®
Cortex® M7 processor and WM8994 codec. These frames are then sent to the
connected audio devices.

The audio data between the ARM
Cortex M7 processor, WM8994 codec, and the audio devices are transferred by
using I2S line.

**Note**

The audio frames streamed through the ARM
Cortex M7 processor and WM8994 codec do not undergo any
conversion.

### Send Processed Audio Samples with Double Buffering

The Audio Output block uses a double buffering
mechanism to send data to the audio device.

With double buffering, the DMA uses one buffer to transfer an
audio frame from the processor to the audio device while the other
buffer receives the processed audio frame from your audio algorithm.
When sending the data to the audio device, doing so helps to prevent
overwriting the buffer.

When you send an audio frame of length `N` samples, the block creates two
buffers of length `N` samples.

With the double buffering mechanism in theAudio Output block:

- In the first iteration, when the processed audio signal is sent out to
  the audio device from Audio out buffer1, the Audio out buffer0 is filled
  with audio signal from the audio processing algorithm.

  In the first iteration, the Audio out buffer1 does not contain the
  audio samples. Therefore, the audio samples from the Audio
  Output block are delayed by one audio frame. If your model
  has Audio Input and Audio Output blocks,
  there is a time delay of two audio frames. This delay occurs because the
  Audio Input block also uses the same double buffering
  technique.
- After the DMA completes sending out the processed data from Audio out
  buffer1, an interrupt is generated.
- In the second iteration, when the processed audio signal is sent out
  to the audio device from Audio out buffer0, the Audio out buffer1 is
  filled with the audio data from the audio processing algorithm.
