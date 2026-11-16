---
type: simulink-block
title: 'Audio Capture'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Audio'
documentation_page: 'audiocapture'
documentation_source_path: 'ref/audiocapture.html'
language: en
---

# Audio Capture

## Ports

### Input

### **msg** — Data message from audio capture interface scalar

This message port receives data messages from a connected Audio Capture
Interface block. The messages process when the Task Manager
block triggers the task containing the Audio Capture block. For more
information on messages, see Messages.

**Data Types:** `SoCData`
### Output

### **data** — Data frame from captured audio *M*-element vector | *M*-by-*C* matrix

When block receives a single audio channel, data is an
*M*-element audio data frame received from a simulated hardware audio
source. The **Samples per frame** parameter defines the number
of samples, *M*, of audio data. When the block receives multiple
audio channels, the audio data is an *M*-by-*C*
matrix, where *C* is specified by the **Number of
channels** parameter.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Data type** — Data type of audio device `int16` (default) | `int8` | `int32`

Specify the data type for the audio capture device.

### **Number of channels** — Number of data channels `2` (default) | positive integer

Specify the number of audio channels, *C*, received from the audio
device. This number should match the **Number of channels** parameter
in the Audio Capture
Interface block.

### **Samples per frame** — Size of data vector read from audio device `4410` (default) | positive scalar integer

Specify the number samples per frame, *M*, of audio data
received.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

If used in a timer-driven task, enter the sample time of the task defined in the
Task Manager
block. If used in the event-driven task, enter `-1`.

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

Capture audio samples from an input audio device and send to an algorithm

The Audio Capture block simulates behavior of the driver code that captures
samples of an audio stream on an hardware board. The input of this block must be connected to
an Audio Capture Interface
block that simulates the physical audio device on a hardware board. Place this block inside a
task and connect to an algorithm to process a frame of audio samples each time the task
executes. For more information on tasks, see Timer-Driven Task and Event-Driven Tasks.
