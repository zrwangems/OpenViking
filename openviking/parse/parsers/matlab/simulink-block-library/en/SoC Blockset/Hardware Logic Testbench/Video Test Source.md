---
type: simulink-block
title: 'Video Test Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'videotestsource'
documentation_source_path: 'ref/videotestsource.html'
language: en
---

# Video Test Source

## Ports
```yaml
ports:
- name: wrCtrlIn
  summary: Input control bus bus
  direction: input
  data_types: StreamVideoS2MBusObj
- name: wrData
  summary: Output video stream data vector
  direction: output
  data_types: uint8
- name: wrCtrlOut
  summary: Output control bus bus
  direction: output
  data_types: pixelcontrol
```

### Input

### **wrCtrlIn** — Input control bus bus

Control bus from the data consumer signaling that data consumer is ready to accept
video stream data. This control bus comprises a ready signal.

**Data Types:** `StreamVideoS2MBusObj`
### Output

### **wrData** — Output video stream data vector

Output video stream data to the data consumer. This value is returned as a
vector.

**Data Types:** `uint8`

### **wrCtrlOut** — Output control bus bus

Control bus to the data consumer, returned as a bus. This control bus comprises
these control signals:

- `hStart` — First pixel in a horizontal line of a
  frame
- `hEnd` — Last pixel in a horizontal line of a
  frame
- `vStart` — First pixel in the first (top) line of a
  frame
- `vEnd` — Last pixel in the last (bottom) line of a
  frame
- `valid` — Indicates the output pixel data on the
  **wrData** output port is valid

**Data Types:** `pixelcontrol`
## Parameters
```yaml
parameters:
- name: Frame size
  summary: Frame dimensions 160x120p (default) | ...
  group: ''
- name: Video source
  summary: Select video source type Video file (default) | Color bar | Ramp
  group: ''
- name: Input file name
  summary: Select input video file handshake_left.avi (default) | any supported video file format
  group: ''
- name: Color space
  summary: Color space YCbCr422 (default) | RGB | YOnly
  group: ''
- name: Reorder output frame
  summary: Output frame reordering off (default) | on
  group: ''
- name: Frame sample time
  summary: Frame sample time 1/60 (default) | positive scalar
  group: ''
```

### **Frame size** — Frame dimensions `160x120p` (default) | ...

Select the frame dimensions as one of these values:

- `480p SDTV (720x480p)`
- `576p SDTV (720x576p)`
- `720p HDTV (1280x720p)`
- `1080p HDTV (1920x1080p)`
- `160x120p`
- `320x240p`
- `640x480p`
- `800x600p`
- `1024x768p`
- `1280x768p`
- `1280x1024p`
- `1360x768p`
- `1366x768p`
- `1400x1050p`
- `1600x1200p`
- `1680x1050p`
- `1920x1200p`

### **Video source** — Select video source type `Video file` (default) | `Color bar` | `Ramp`

Select the type of video source as `Video file`, `Color
bar`, or `Ramp`.

### **Input file name** — Select input video file `handshake_left.avi` (default) | any supported video file format

Select the input video file by clicking the **Browse** button and
navigating to the video file location.

#### Dependencies

To enable this parameter, set the **Video source** parameter to
`Video file`.

### **Color space** — Color space `YCbCr422` (default) | `RGB` | `YOnly`

Select the type of color space as `YCbCr422`,
`RGB`, or `YOnly`.

### **Reorder output frame** — Output frame reordering `off` (default) | `on`

Select this option to reorder output pixels to *column-major*
order. Streaming pixel format order is from left to right across each line, then down to
the next line, or *row-major*. However, some matrix operations use
*column-major* order, that is, from top to bottom and then right to
the next column.

### **Frame sample time** — Frame sample time `1/60` (default) | positive scalar

Specify the frame sample time as a positive scalar. The denominator in default value
`1/60` denotes the number of frames per second.
## Libraries

SoC Blockset / Hardware Logic Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Generate continuous video stream data

The Video Test Source block generates continuous video stream data to
advanced extensible interface AXI4-based video stream data interface blocks. You can use this
block as a test source block for simulating AXI4-based video stream data applications.

The block accepts a control bus and outputs video stream data along with a control
bus.
