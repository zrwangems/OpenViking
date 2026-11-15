---
type: simulink-block
title: 'Audio File Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audiofileread'
documentation_source_path: 'supportpkg/android_ref/audiofileread.html'
language: en
---

# Audio File Read

## Ports

### Output

### **Port1** — Audio data *M*-by-*N* matrix

The block emits data an *M*-by-*N* matrix,
where *M* is the number of channels and *N* is
the frame size. To specify *N*, use the **Frame
size** parameter.

**Data Types:** `int16`

## Parameters

### **File name** — Name of audio file on your development computer `guitartune.wav` (default)

If the location of the file does not appear on your MATLAB® path,
click **Browse** to specify the full path. If the
location of this file does appear on your MATLAB path, enter
only the file name.

### **Frame size** — Number of samples per frame of audio data `1024` (default) | positive integer

The frame size must be a positive integer value. Larger frame
sizes can result in a delay in your audio output.

## Libraries

Simulink Support Package for Android Devices / Audio & Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Add audio file from computer into mobile application

The Audio File Read block copies an audio source file into your model
and outputs the audio data into the model. The block outputs audio data as an
*M*-by-*N* matrix, where *M* is
the number of channels and *N* is the frame size of audio data.

Audio data consists of one or more channels. A `mono` audio source
file only has one channel and a `stereo` audio source file has two
channels. The audio data is output from the block as frames consisting of
`M` consecutive samples of audio data.

### Algorithm

The sample time of the Audio File Read block is determined
automatically by the data frame size and audio frequency of the selected audio
file.

*Sample time* = *frame
size* / *audio
frequency*

For example, if the *audio frequency* is 44,100 Hz and the
*frame size* is 4410 samples, then the block sample time is 4410 / 44,100 = 0.1 seconds.

To select an audio source file, use the **File name** parameter.
The audio frequency of the selected file displays on the block.

**Note**

To maintain audio quality, in blocks connected to the Audio File
Read block, set the sample time to inherited.
