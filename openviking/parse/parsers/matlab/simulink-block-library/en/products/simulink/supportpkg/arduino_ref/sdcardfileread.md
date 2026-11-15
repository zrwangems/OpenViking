---
type: simulink-block
title: 'SD Card File Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'sdcardfileread'
documentation_source_path: 'supportpkg/arduino_ref/sdcardfileread.html'
language: en
---

# SD Card File Read

## Ports

### Input

### **Port\_1** — Index to read data scalar

The port accepts the index to read data. For raw and ASCII files, the
block starts reading data from the specified index. For audio files, the
block starts reading data from the location that is calculated using the
specified index, excluding the Waveform Audio File Format (WAV)
header.

#### Dependencies

To enable this port, select the **Enable reading from
index** parameter.

**Data Types:** `uint8`
### Output

### **Data** — Audio data from SD card *M*-by-*N* matrix

The block outputs the data read from the SD card. The format of the
output depends on the **File type** parameter. If you
select the **File type** as:

- `Raw` –– The block outputs the
  data in `uint8` format.
- `ASCII` –– By default, the block
  outputs the data in `uint8` format. If you
  select the **Enable Delimiter** parameter,
  the block outputs the data in the **Data
  type** format.
- `Audio (wav)` –– The block
  outputs the audio data as an
  *M*-by-*N* matrix,
  where *M* is the **Frame
  size**, and *N* is the
  **Number of Channels** supported by the
  audio.

The block outputs zeroes when it encounters the end of the file
(EOF).

**Data Types:** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Boolean`

### **Status** — Status of the read operation scalar

The block outputs the status of read operation as a
`uint8` value. Each value corresponds to a data
transfer status.

| Status Value | Status Description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `FILE CANNOT BE OPENED` |
| `2` | `NOT A WAVE FILE` |
| `3` | `BLOCK MASK DATA MISMATCH FOR AUDIO` |
| `4` | `INDEX VALUE EXCEEDS FILE LENGTH` |
| `5` | `FILE HAS CHARACTERS OTHER THAN (0-9, Period, and Delimiter)` |
| `6` | `END OF FILE` |

**Data Types:** `uint8`

## Parameters

### **SPI module** — SPI communication module `0` (default) | scalar

Specify the SPI module on the Arduino hardware to communicate with SPI peripherals. For more
information on Arduino pin mapping and modules that hardware boards support, see
Pin Mapping for Arduino Timer-Independent Blocks.

### **File type** — Read format of data file `Raw` (default) | `ASCII` | `Audio(wav)`

Specify the format in which the block reads the
file.

### **File name** — Name of audio file `testaudio.wav` (default)

Specify the path and name of the file from which the block reads data. For
example, to read the `sample.wav` file that is located
inside the `TestAudio` folder of the SD card, specify the
**File name** as
`/TestAudio/sample.wav`

### **Number of times to read file** — Number of times to read the audio file `Inf` (default) | positive integer

Specify the number of times the block reads the file from beginning. To
read the file until you stop the simulation, specify the **Number of
times to read file** as `Inf`.

### **Enable reading from index** — Enable reading from given index off (default) | on

When you select the **Enable reading from index**
parameter, the block configures an input port. Specify an index at this
port.

For raw and ASCII files, the block starts reading data from the specified
index. For audio files, the block starts reading data from the location that
is calculated using the specified index, excluding the WAV header.

### **Enable Delimiter** — Option to read data using delimiters off (default) | on

- `off` –– The block reads data and outputs it in
  `uint8` format.
- `on` –– At each sample time, the block reads data
  until it encounters the next delimiter, specified in the
  **Delimitter** parameter. The block outputs the
  data in the **Data type** format, omitting the
  delimiter at the end. The block continues to read the data until the
  EOF is encountered.

#### Dependencies

To enable this parameter, set **File type** to
`ASCII`.

### **Delimitter** — Delimiter to read data , (default)

Specify the delimiter to read the data. At each sample time, the block
reads data until it encounters the next delimiter. The block outputs the
data in the **Data type** format, omitting the delimiter at
the end. The block continues to read the data until the EOF is
encountered.

#### Dependencies

To enable this parameter, select the **Enable
Delimiter** parameter.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

For raw and ASCII files, specify how often the block reads data from the
SD card. When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the
block context within the model.

For audio (wav) files, the block calculates the sample time
(*T*s) from the frame size (*N*) and
sampling rate (*F*s) of the selected audio file.

*T*s = *N* /
*F*s

For example, if *N* is 4410 samples and
*F*s is 44,100 Hz, the block sample time is 4410/44,100
= 0.1 seconds.

*N* is the value that you specify in the **Frame
size** parameter. *F*s is the value that you
specify in the **Sample rate (Hz)** parameter.

### **Sample rate (Hz)** — Number of samples per frame of audio data `44100` (default) | positive integer between `1` and `48000`

Specify the sample rate used by the audio input device to read audio
data, in Hz. Larger frame sizes may result in a delay in your audio input.
Ensure that the audio sampling frequency matches the input sampling
frequency to avoid any issues in the output.

**Tip**

To find the sample rate of the specified audio file, use the
`audioinfo` command in the MATLAB® Command Window. Copy the sample rate from the
`SampleRate` property of the
`audioinfo` command and paste the copied rate
to the **Sample rate (Hz)** parameter.

#### Dependencies

To enable this parameter, set **File type** to
`Audio (wav)`.

### **Number of Channels** — Number of channels supported `1` (default) | `2`

Specify if the audio file is mono or stereo. If the audio file is mono,
set this parameter value as `1`. If the audio file is
stereo, set this parameter value as `2`.

**Tip**

To find the number of channels that the specified audio file supports,
use the `audioinfo` command in the MATLAB Command Window. Set the **Number of
Channels** parameter to the value displayed in the
`NumChannels` property of the
`audioinfo` command.

#### Dependencies

To enable this parameter, set **File type** to
`Audio (wav)`.

### **Bits per sample** — Number of bits `8` (default) | `16`

Specify the number of bits in each sample of audio.

**Tip**

To find the bits per sample for the specified audio file, use the
`audioinfo` command in the MATLAB Command Window. Set the **Bits per
sample** parameter to the value displayed in the
`BitsPerSample` property of the
`audioinfo` command.

#### Dependencies

To enable this parameter, set **File type** to
`Audio (wav)`.

### **Frame Size** — Number of samples per frame of audio data `100` (default) | positive integer between `1` and `16384`

Specify the number of samples in a frame. Larger frame sizes may result in
a delay in your audio output.

#### Dependencies

To enable this parameter, set **File type** to
`Audio (wav)`.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Read data from an SD card

The SD Card File Read block reads data from files stored in an SD card
that is connected to the hardware. The hardware communicates with the SD card over Serial Peripheral Interface (SPI). Specify
the SD Card SPI CS Pin for communication
in the Configuration Parameters dialog box.

If you simulate a model that contains the SD Card Read block without
connecting the hardware, the block outputs zeros. For more information, see Block Produces Zeros or Does Nothing in Simulation.

Click **View pin map** to open the Arduino Pin Mapping
table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

**Note**

You can now deploy a Simulink® model containing the SD Card File Read block on your
Arduino® compatible ESP32 WROOM and ESP32 WROVER boards.
