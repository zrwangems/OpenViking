---
type: simulink-block
title: 'Audio Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audiocapture'
documentation_source_path: 'supportpkg/android_ref/audiocapture.html'
language: en
---

# Audio Capture

## Ports

### Output

### **Port\_1** — Audio sample captured from device microphone numeric matrix

The block outputs the audio samples captured from the device microphone, returned
as an *N*–by–2 numeric matrix. Here, *N* is the
number of audio samples per frame. The columns of the matrix represent the left and
right audio channels, respectively.

**Data Types:** `int16`

## Parameters

### **Audio sampling frequency (Hz)** — Sample rate of device microphone `44100` (default) | `8000` | `11025` | `16000` | `22050` | `24000` | `32000` | `48000`

Specify the sample rate of the device microphone.

### **Frame size (N)** — Number of audio samples per frame `4410` (default) | nonnegative scalar

Specify the number of audio samples per frame.

## Libraries

Simulink Support Package for Android Devices / Audio & Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Capture audio stream from device microphone

Use the Audio Capture block to capture an audio sample from the device
microphone. The block outputs the left and right audio channels as an
*N*–by–2 `int16` matrix. *N* is the
number of audio samples per frame, and the columns of the matrix represent the left and right
audio channels, respectively. The **Frame size (N)** parameter sets the value
of *N*.

The sample time of the block is derived from **Frame size (N)** and
**Audio sampling frequency (Hz)** parameter values. For example, if
**Audio sampling frequency (Hz)** is 44100 Hz and the **Frame size
(N)** is 4410, then the sample time is 4410/44100 = 0.1s.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
