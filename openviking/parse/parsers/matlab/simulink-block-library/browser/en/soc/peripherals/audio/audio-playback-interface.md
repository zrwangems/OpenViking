---
type: simulink-block
title: 'Audio Playback Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Audio'
documentation_page: 'audioplaybackinterface'
documentation_source_path: 'ref/audioplaybackinterface.html'
language: en
---

# Audio Playback Interface

## Ports

### Input

### **msg** — SoC message data vector

This port receives data messages containing audio data from a connected Audio Playback
block.

**Data Types:** `SoCData`
### Output

### **data** — Audio data frame *M*-element vector | *M*-by-*C* matrix

When the block receives a single audio channel, the audio data frame is an
*M*-element vector from a simulated hardware audio output. The
**Samples per frame** parameter defines the number of
samples, *M*, of audio data. When the block receives multiple audio
channels, the audio data frame is an *M*-by-*C*
matrix, where *C* is specified by the **Number of
channels** parameter.

#### Dependencies

To enable this port, set the **Output** parameter to
`To output port`.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Output** — Output type `To terminator` (default) | `To output port`

Specify if the block acts as a terminator, similar to the Terminator block, or produces data to an output port.

### **Number of channels** — Number of data channels `2` (default) | positive integer

Specify the number of audio channels, *C*, sent to the audio
device. This number must match the **Number of channels** parameter in
the Audio Playback
block.

### **Samples per frame** — Size of data vector read from audio device `4410` (default) | positive scalar integer

Specify the number of samples per frame, *M*, of audio data.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

Enter the sample time to be used by the timer-driven task subsystem when you clear
the **Enable event-based execution** parameter.

## Libraries

SoC Blockset / Peripherals

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

Embedded Coder does not generate code for this block. In the
generated code, the advanced Linux sound architecture (ALSA) driver framework performs audio
output on the device. The related Audio Playback block
represents the ALSA driver. For more information on the ALSA driver framework, see the Advanced
Linux Sound Architecture website.

## Version History

**Introduced in R2021a**

## Description

Simulate audio output device on a hardware board

The Audio Playback Interface block simulates the behavior of an audio
output device. The block receives audio samples as messages from a connected Audio Playback block
that simulates audio driver code connected to your algorithm.
