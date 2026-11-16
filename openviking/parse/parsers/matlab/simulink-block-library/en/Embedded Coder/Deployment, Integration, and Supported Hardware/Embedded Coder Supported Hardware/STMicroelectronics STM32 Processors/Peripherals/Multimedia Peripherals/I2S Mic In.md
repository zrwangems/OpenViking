---
type: simulink-block
title: 'I2S Mic In'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Multimedia Peripherals'
documentation_page: 'i2smicin'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2smicin.html'
language: en
---

# I2S Mic In

## Ports

### Output

### **Port\_1** — Output port containing audio samples from MEMS microphone `Scalar`

The output port containing audio samples from MEMS microphone on the
STM32F4xx based board.

**Data Types:** `int16` | `int32`

## Parameters

### **I2S Module** — Select I2S mic in module `I2S2` (default) | `I2S1` | `I2S1`

Select the I2S mic in module.

### **Enable PDM audio frame to PCM audio frame conversion** — Enable to convert PDM to PCM audio frame `off` (default) | `on`

Select to enable the conversion of PDM audio frame to PCM audio frame
conversion.

### **Signal format** — Select audio out signal format `16 bits` (default) | `24 bits` | `32 bits`

Select the I2S mic in signal format in bits.

### **Number of channels** — Select number of channel for audio out `Stereo` (default) | `Mono`

- `Stereo` - select stereo to record and play
  using 2 different audio channels.
- `Mono` - select mono to record and play using
  single audio channel.

#### Dependencies

To set the parameter **Number of channels** to
`Mono`, enable the **Enable PDM audio frame
to PCM audio frame conversion** parameter. Disable the
**Enable PDM audio frame to PCM audio frame
conversion** parameter, when `Stereo` is
selected.

### **Audio sample frequency (in kHz)** — `16` (default) | `8` | `22.5` | `32` | `44.1` | `48` | `96`

Select an audio sample rate. It is the sampling
frequency to read audio signal from the MEMS microphone.

### **Audio frame size** — Audio signal frame size based on sample rate `16` (default)

The audio signal frame size is based on the sample rate that you
select.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Read audio sample from MEMS microphone available on the STM32F4xx based board

The I2S Mic In block reads the audio samples collected from the MEMS
microphone (MP45DT02, ST MEMS audio sensor, omnidirectional digital microphone),
available on STM32F4xx based board. The MEMS microphone produces a Pulse Density
Modulated (PDM) signal.

The block outputs `int16` or `int32` Pulse Code
Modulated audio frame with the size specified in **Frame size (samples)** field from the block mask.

The block sample rate is calculated as: Sample frequency/ Frame size.

For example, the Mic in block sample time with 48 kHz sampling frequency and 96
samples frame size is equal to 2 ms (96/48000). The minimum allowed sampling rate for
the Mic in block is 1ms.

**Note**

- As the Mic In block always outputs 1ms of int16 PCM audio frame data,
  the values in **Frame Size** and **Sample
  Time** are calculated based on the **Sample
  Rate** that you select. The values in these parameters are
  for display purposes only. You cannot edit these values.
- The PDM filter option in STM32CubeMX project is available only for
  STM32F4xx and STM32F7xx based boards.

### PDM Processing

Pulse Density Modulation (PDM) uses the density of a pulse to represent a signal.
The relative density of the pulses in PDM corresponds to the analog signal
amplitude. In PDM bit stream, ‘1’ corresponds to a pulse of positive polarity and
‘0’ corresponds to a pulse of negative polarity. PDM uses a single bit to convey the
audio.

Some of the advantages of PDM processing are:

- Simple in concept and execution
- Low cost audio transmission in digital form
- Efficient systems with good design
- Low noise and less signal interference

### Read Audio Data Using Double Buffering

The Mic In block uses a double buffering to read the audio data from the MEMS
microphone.

With double buffering, one buffer is used by the DMA to read audio PDM signal from
the MEMS microphone while the other buffer is used to send audio frames to the audio
processing algorithm. This helps to prevent overwriting of the buffer while being
used by the audio algorithm.

The following describes the double buffering mechanism in the Mic In block.

- In the first iteration, when the ‘Mic in buffer1’ sends the data for
  audio processing, the DMA fills ‘Mic in buffer0’.

  In the first iteration, the ‘Mic in buffer1’ does not contain the
  audio samples. Therefore, the audio samples from the Mic In block are
  delayed by one audio frame.
- After the DMA completes filling Mic in buffer0, an interrupt is
  triggered.
- In the second iteration, when the ‘Mic in buffer0’ sends the data for
  audio processing and the DMA fills ‘Mic in buffer1’.
