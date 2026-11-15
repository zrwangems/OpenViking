---
type: simulink-block
title: 'Audio File Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audiofilewrite'
documentation_source_path: 'supportpkg/android_ref/audiofilewrite.html'
language: en
---

# Audio File Write

## Ports

### Input

### **Port1** — Audio data *M*-by-*N* matrix

The block emits data an *M*-by-*N*
matrix, where *M* is the number of samples per frame
and *N* is the number of channels.

**Data Types:** `int16`

### **Port2** — control `Input port` (default) | `Block dialog`

Recording the audio data can be controlled by either input port or can
be specified via dialog.

**Data Types:** `int16`

## Parameters

### **File name** — Name of audio file on your development computer `audiowrite` (default)

If the location of the file does not appear on your MATLAB® path, click **Browse** to specify the full
path. If the location of this file does appear on your MATLAB path, enter only the file name.

### **File type** — Type of audio data `wav` (default) | `m4a`

Audio File Write block writes mono or stereo audio data to a
`wav` or `m4a`. Inputs for the audio
file can be `0` or `1`.

### **Audio Sampling frequency(Hz)** — Number of samples per frame of audio data `44100` (default) | positive integer

The audio sampling frequency must be a positive integer value. Larger
frame sizes can result in a delay in your audio input. Ensure that the audio
sampling frequency matches the input sampling frequency to avoid any issues
in the output.

### **Record control** — Control recording of audio data `Input control` (default) | `Block dialog`

Recording the audio data can be controlled by either Input port or can be
specified via dialog. In `Input control` mode, control
input can accept only `0`, `1` and
`2` as input. `0` is stop recording,
`1` is start recording and `2` is
pause recording.

### **Max record time** — Set record time for audio data `60` (default) | positive integer

The record time must be a positive integer value. This parameter is
enabled when **Record control** is set to `Block
dialog`.

### **Bit rate(kpbs)** — Number of kilobits per second `128` (default) | positive integer

The bit rate must be a positive integer value. This parameter is enabled
when **File type** is set to `m4a`.

## Libraries

Simulink Support Package for Android Devices / Audio & Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Write audio frames to an audio file

The Audio File Write block writes mono or stereo audio data to a
`wav` or `m4a` file. The block accepts audio data
as an *M*-by-*N* matrix, where *M* is
the number of samples per frame and *N* is the number of
channels.

Audio data consists of one or more channels. A `mono` audio source
file only has one channel and a `stereo` audio source file has two
channels.
