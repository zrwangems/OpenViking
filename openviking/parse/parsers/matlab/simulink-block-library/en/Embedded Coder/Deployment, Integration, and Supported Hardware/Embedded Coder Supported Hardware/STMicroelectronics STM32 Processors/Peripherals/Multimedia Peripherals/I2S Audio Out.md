---
type: simulink-block
title: 'I2S Audio Out'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Multimedia Peripherals'
documentation_page: 'i2saudioout'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2saudioout.html'
language: en
---

# I2S Audio Out

## Ports

### Input

### **Port\_1** — Port containing the processed audio sample `Scalar`

Input port containing the processed audio
samples to the audio devices.

**Data Types:** `int16` | `int32`

## Parameters

### **I2S Module** — Select I2S audio out module `I2S2` (default) | `I2S1` | `I2S1`

Select the I2S audio out module.

### **Signal format** — Select audio out signal format `16 bits` (default) | `24 bits` | `32 bits`

Select the I2S audio out signal format in bits.

### **Audio sample frequency (in kHz)** — `16` (default) | `8` | `22.5` | `32` | `44.1` | `48` | `96`

Select an audio sample rate. The
sample rate at which the processed audio
samples are sent out to the audio
device.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Send processed audio samples to audio devices

The I2S Audio Out block sends a stream of data to the audio
output connector. The block writes the processed audio data to the audio
device connected to the processor on the STM32F4xx based board. You can send
the audio samples at different rates such as 16kHz, 32kHz etc. with
different frame sizes.

The input port accepts either `int16` or
`int32` audio frames in [Nx2] format for
**Stereo**.

You can play only stereo [Nx2] audio frames on this block.

**Note**

You cannot play [1x1] audio samples on this block as the frame
requires at least two samples.

### Send Processed Audio Samples Using Double Buffering

The Audio Out block uses a double buffering mechanism to send data to
the audio device.

With double buffering, one buffer is used by the DMA to transfer audio
frame from the processor to the audio device while the other buffer
is used to receive the processed audio frame from your audio
algorithm. Doing so helps to prevent overwriting the buffer while
sending the data to the audio device.

When you send an audio frame of length `N samples`,
the block creates two buffers of length `N`
samples.

The following describes the double buffering mechanism in the Audio
Out block.

- In the first iteration, when the processed
  audio signal is sent to the audio device from
  ‘Audio out buffer1’, the ‘Audio out buffer0’ is
  filled with audio signal from the audio processing
  algorithm.

  In the first iteration, the ‘Audio out
  buffer1’ does not contain the audio samples.
  Therefore, the audio samples from the Audio Out
  block are delayed by one audio frame. If your
  model has Mic In and the Audio Out blocks, then
  there is a time delay of two audio frames as the
  Mic In block also uses the same double buffering
  technique.
- After the DMA completes sending out the
  processed data from ‘Audio out buffer1’, an
  interrupt is generated.
- In the second iteration, when the processed
  audio signal is sent out to the audio device from
  Audio out buffer0, the ‘Audio out buffer1’ is
  filled with the audio data from the audio
  processing algorithm.
