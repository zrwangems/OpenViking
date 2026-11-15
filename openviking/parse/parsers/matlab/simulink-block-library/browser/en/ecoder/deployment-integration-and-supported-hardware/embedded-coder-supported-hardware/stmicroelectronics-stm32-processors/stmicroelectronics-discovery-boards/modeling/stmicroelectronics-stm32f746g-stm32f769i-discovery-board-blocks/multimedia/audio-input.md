---
type: simulink-block
title: 'Audio Input'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'audioinput'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/audioinput.html'
language: en
---

# Audio Input

## Ports

### Output

### **Port\_1** — Output port containing PCM audio samples in frames matrix

The block emits PCM audio frames. For STM32F746G, the output frames
are `[Nx2]`
`int16` matrix. For STM32F769I, the output frames are
`[Nx2]` or `[Nx4]`
`int16` matrix. `N` is the number of
samples per frame specified in the **Samples per frame
(N)** parameter, and `2` is the number of
audio channels per frame.

The block interprets
an `N`-by-`2` matrix as
a multichannel signal with `2` independent
channels and `N` samples per channel. For example,
if you specify **Samples per frame (N)** as
`5`, the block interprets the following sequence of
`5`-by-`2` matrices as a
two-channel signal with a frame size of 5.

**Data Types:** `int16`

## Parameters

### **Device** — Device from which to acquire audio `Microphone` (default) | `LineIn`

Select the device from which the block reads audio data.

### **Audio sampling frequency (Hz)** — Sampling frequency to read audio signal from the audio device `8000` | `11025` | `16000` | `22050` | `32000` | `44100 (default for STM32F769I)` | `48000 (default for STM32F746G)` | `96000` | `192000(STM32F746G only)`

Specify the number of samples per second to read from the audio device
that you specify in the **Device** parameter.

### **Number of Channels** — Number of audio channels (STM32F769I only) `2` (default) | `4`

If the **Device** is Microphone, you can select 2 or 4
audio channels. This parameter is not available for Line In.

**Note**

To use four microphones in the Audio Input block, you must have an
Audio Toolbox™ license.

### **Samples per frame (N)** — Number of samples per frame at the output `48(default for STM32F746G)` | `1024(default for STM32F769I)` | `integer between 1 and 65535`

Specify the number of samples per frame that the block emits.

### **Volume** — Loudness of the audio signal at the output (STM32F746G only) `90` (default) | `integer between 0 and 100`

The block applies gain to the value that you specify in this parameter.
The gain is calculated as:

(Volume\*240)/100

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Read audio sample from audio devices on STMicroelectronics STM32F746G/STM32F769I– Discovery board

The Audio Input block reads audio samples from the audio
device (Microphone, Line In) connected to the processor on the
STM32F746G/STM32F769I–Discovery™ boards. The audio samples are either in Pulse Density Modulation (PDM)
format or Pulse Code Modulated (PCM) format. The format of the audio samples depends on
the device from which the block acquires audio.

The block emits PCM audio frames. For STM32F746G, these frames are
`[Nx2]`
`int16` matrix. For STM32F769I, these frames are
`[Nx2]` for Line In input, and `[Nx2]` or
`[Nx4]` for Microphone input, depending on the number of channels
selected. `N` is the number of samples per frame, and
`2` and `4` are the number of audio channels per
frame.

You can read audio samples at different rates, such as 8 kHz, 11 kHz, 16 kHz, 22 kHz,
32 kHz, 44 kHz, 48 kHz, 96 kHz, and 192 kHz (STM32F746G only), with different frame
sizes.

Using the parameters of this block, you specify the device from which you acquire
audio. For STM32F746G, you can also specify the volume level at which the block emits
audio frames.

The output of this block connects to audio devices such as headphones or
speakers.

### Read Audio from Microphone or LineIn

The STM32F746G/STM32F769I–Discovery board acquires audio from either of the two audio devices, Dual MEMS
Microphones (MP34DT01), or Line In that connect to the board.

The dual MEMS microphones (MP34DT01) on the STM32F746G–Discovery board outputs a PDM signal, which is then sent to the WM8994 codec.
The WM8994 codec converts the PDM signal to 16-bit PCM format and sends it to the
ARM®
Cortex® M7 processor.

The two dual MEMS microphones on the STM32F769I–Discovery board outputs PDM signals, which are then sent to the digital filter
for sigma delta modulation (DFSDM) peripheral. The DFSDM peripheral converts the PDM
signals to 16-bit PCM format and sends it to the ARM
Cortex M7 processor.

LineIn outputs a PCM signal. The output signal is sent to the WM8994 codec, which
is then sent to the ARM
Cortex M7 processor. These frames are then sent to the connected audio
devices.

Audio data between audio devices, WM8994 codec, and the ARM
Cortex M7 processor are transferred by using I2S line.

**Note**

The 16-bit PCM audio frames from LineIn, which are streamed through the
WM8994 codec and ARM
Cortex M7 processor, do not undergo any conversion.

### Read Audio Data with Double Buffering

The Audio Input block uses a double buffering mechanism to read the
audio data from the audio device.

With double buffering, the DMA uses one buffer to read an audio PCM signal from
the audio device while the other buffer sends audio frames to the audio processing
algorithm. When the audio algorithm uses the buffer, this mechanism helps to prevent
overwriting of the buffer.

With the double buffering mechanism in the Audio Input block:

- In the first iteration, when the Audio In buffer1 sends the data for
  audio processing, the DMA fills Audio In buffer0.

  In the first iteration, the Audio In buffer1 does not contain the
  audio samples. Therefore, the audio samples from the Audio
  Input block are delayed by one audio frame.
- After the DMA completes filling Audio In buffer0, an interrupt is
  triggered.
- In the second iteration, when the Audio In buffer0 sends the data for
  audio processing, the DMA fills Audio In buffer1.
