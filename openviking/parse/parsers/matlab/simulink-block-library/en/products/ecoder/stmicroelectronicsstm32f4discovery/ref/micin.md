---
type: simulink-block
title: 'Mic In'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'micin'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/micin.html'
language: en
---

# Mic In

## Ports

### Output

### **Port\_1** — Output port containing audio samples from MEMS microphone scalar

The output port containing audio samples from MEMS microphone
on the STMicroelectronics® STM32F4–Discovery board.

**Data Types:** `int16`

## Parameters

### **Sample rate (Hz)** — Sample frequency to read audio signal 48000 (default) | 8000 | 16000 | 22050 | 32000 | 44100 | 48000

Select a sample rate. It is the sampling frequency to read audio
signal from the MEMS microphone.

### **Frame size (samples)** — Audio signal frame size based on sample rate 48 (default) |

The audio signal frame size is based on the sample rate that
you select.

### **Sample time** — Sample time based on sample rate 48/48000 (default) |

The block sample time is calculated based on the sample rate
that you select.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Read audio sample from MEMS microphone available on the STMicroelectronics STM32F4– Discovery board

This block reads the audio samples collected from the MEMS microphone
(MP45DT02, ST MEMS audio sensor, omnidirectional digital microphone),
available on STM32F4–Discovery™ board. The MEMS microphone
produces a Pulse Density Modulated (PDM) signal.

The block output emits int16 Pulse Code Modulated audio frame
with the size specified in **Frame size (samples)**  field
from the block mask.

The block sample rate is calculated as: Sample frequency/ Frame
size.

For example, the Mic in block sample time with 48 kHz sampling
frequency and 96 samples frame size is equal to 2 ms (96/48000).
The minimum allowed sampling rate for the Mic in block is 1ms.

In the Configuration Parameters dialog, under Coder Target,
you can select `“Mic In” block DMA interrupt` as
the **Scheduler Interrupt Source**. This ensures
that the processing of your algorithm is synchronized with the Mic
In block interrupt.

When you select this option, make sure your model base rate
is the same as the Mic In block sample time.

**Note**

As the Mic In block always outputs 1ms of int16 PCM audio frame
data, the values in **Frame Size** and **Sample
Time** are calculated based on the **Sample Rate** that
you select. The values in these parameters are for display purposes
only. You cannot edit these values.

### PDM Processing

Pulse Density Modulation (PDM) uses the density of a pulse to
represent a signal. The relative density of the pulses in PDM corresponds
to the analog signal amplitude. In PDM bit stream, ‘1’
corresponds to a pulse of positive polarity and ‘0’
corresponds to a pulse of negative polarity. PDM uses a single bit
to convey the audio.

Some of the advantages of PDM processing are:

- Simple in concept and execution
- Low cost audio transmission in digital form
- Efficient systems with good design
- Low noise and less signal interference

### Read Audio Data Using Double Buffering

The Mic In block uses a double buffering to read the audio data
from the MEMS microphone.

With double buffering, one buffer is used by the DMA to read
audio PDM signal from the MEMS microphone while the other buffer is
used to send audio frames to the audio processing algorithm. This
helps to prevent overwriting of the buffer while being used by the
audio algorithm.

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
