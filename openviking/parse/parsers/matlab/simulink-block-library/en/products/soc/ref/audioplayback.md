---
type: simulink-block
title: 'Audio Playback'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Audio'
documentation_page: 'audioplayback'
documentation_source_path: 'ref/audioplayback.html'
language: en
---

# Audio Playback

## Ports

### Input

### **data** — Audio data frame *M*-element vector | *M*-by-*C* matrix

Audio data frame to be sent to an audio playback device, specified as an
*M*-element for single channel audio or as an
*M*-by-*C* matrix for multi-channel audio.
*C* is specified by the **Number of
channels** parameter.

**Data Types:** `int8` | `int16` | `int32`
### Output

### **msg** — Data message from audio capture interface scalar

This port outputs data messages containing audio data to a connected Audio Playback
Interface block. For more information on messages, see Messages.

**Data Types:** `SoCData`

## Parameters

### **Number of channels** — Number of channels `2` (default) | positive scalar

Specify the number of audio channels, *C*, in each audio data
sample.

## Libraries

SoC Blockset / Processor I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- To automatically generate C code for your design,
  and execute on an SoC device, use the SoC Builder tool.
  For more information on generating code for SoC designs, see Use SoC Builder to Generate SoC Design.
- To generate and execute C code for your SoC models, this block requires Embedded Coder® and SoC Blockset™ Support Package for Embedded Linux® Devices.
- To use this block, you must set **Hardware Board** to
  `Embedded Linux Board`. You can then follow the instructions
  to configure the board. For more information, see Create an Embedded Linux Device Configuration.

When deployed to a supported hardware board, this block uses the V4L2 driver framework
to capture images from video capture devices, such as a camera. To specify the video capture
device and event triggers, use the Hardware Mapping tool. For more information
on the V4L2 driver framework, see Video4Linux.

## Version History

**Introduced in R2021a**

## Description

Playback audio samples from an algorithm to an output audio device

The Audio Playback block simulates behavior of the driver code that plays
audio to an audio output, such as a speaker, on a hardware board. The output of this block
must be connected to an Audio Playback
Interface block that simulates a physical audio device on the hardware board. Place
this block inside a task and connect to an algorithm to output a frame of audio samples each
time the task executes. For more information on tasks, see Timer-Driven Task and Event-Driven Tasks.
