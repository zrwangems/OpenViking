---
type: simulink-block
title: 'Audio Playback'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audioplayback'
documentation_source_path: 'supportpkg/android_ref/audioplayback.html'
language: en
---

# Audio Playback

## Ports

### Input

### **Port\_1** — Audio sample numeric matrix

The block inputs the audio sample, specified as an *N*–by–2
numeric matrix. Here, *N* is the number of audio samples per frame,
and the columns of the matrix represents the left and right audio channels,
respectively.

**Data Types:** `int16`

## Parameters

### **Audio sampling frequency (Hz)** — Sample rate of device speaker `44100` (default) | `8000` | `11025` | `16000` | `22050` | `24000` | `32000` | `48000`

Specify the audio sampling frequency of the device speaker.

## Libraries

Simulink Support Package for Android Devices / Audio & Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Play audio on device speaker

Use the Audio Playback block to play an audio sample on the device speaker.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
