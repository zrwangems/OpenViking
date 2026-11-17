---
type: simulink-block
title: 'Video Test Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'videotestsink'
documentation_source_path: 'ref/videotestsink.html'
language: en
---

# Video Test Sink

## Ports
```yaml
ports:
- name: rdData
  summary: Input video stream data vector
  direction: input
  data_types: uint8
- name: rdCtrlIn
  summary: Input control bus bus
  direction: input
  data_types: pixelcontrol
- name: rdCtrlOut
  summary: Output control bus bus
  direction: output
  data_types: StreamVideoS2MBusObj
```

### Input

### **rdData** — Input video stream data vector

Input video stream data from the data source. This value must be a vector.

**Data Types:** `uint8`

### **rdCtrlIn** — Input control bus bus

Input control bus from the data source, specified as a bus. This control bus
comprises these signals:

- `hStart` — First pixel in a horizontal line of a
  frame
- `hEnd` — Last pixel in a horizontal line of a
  frame
- `vStart` — First pixel in the first (top) line of a
  frame
- `vEnd` — Last pixel in the last (bottom) line of a
  frame
- `valid` — Indicates the input pixel data on
  **rdData** input port is valid

**Data Types:** `pixelcontrol`
### Output

### **rdCtrlOut** — Output control bus bus

Output control bus to the data source signaling that the block is ready to accept
video stream data. This control bus comprises a ready signal.

**Data Types:** `StreamVideoS2MBusObj`
## Parameters
```yaml
parameters:
- name: Frame size
  summary: Frame dimensions 160x120p (default) | ...
  group: ''
- name: Color space
  summary: Color space YCbCr422 (default) | RGB | YOnly
  group: ''
- name: Reorder input frame
  summary: Input frame reorder off (default) | on
  group: ''
- name: Save data in workspace
  summary: Save data in workspace off (default) | on
  group: ''
- name: Variable name
  summary: Workspace variable name simOut (default) | any MATLAB-supported variable name
  group: ''
- name: View input
  summary: Display input in MATLAB off (default) | on
  group: ''
```

### **Frame size** — Frame dimensions `160x120p` (default) | ...

Select the frame dimensions as one of these values:

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

The **Frame size** value must be same as that of the data
source.

### **Color space** — Color space `YCbCr422` (default) | `RGB` | `YOnly`

Select the type of color space as `YCbCr422`,
`RGB`, or `YOnly`. The **Color
space** value must be same as that of the data source.

### **Reorder input frame** — Input frame reorder `off` (default) | `on`

Select this option to reorder input pixels. Streaming pixel format order is from
left to right across each line, then down to the next line, or
*row-major*. However, some matrix operations use
*column-major* order, that is, from top to bottom and then right to
the next column. Depending on how your design has manipulated the pixels, you may need
to reorder them for correct display.

### **Save data in workspace** — Save data in workspace `off` (default) | `on`

Select this parameter to save the input video stream data to the MATLAB® workspace.

### **Variable name** — Workspace variable name `simOut` (default) | any MATLAB-supported variable name

Specify the workspace to which input video stream data is saved. This parameter can
be any MATLAB-supported variable name.

#### Dependencies

To enable this parameter, select the **Save data in workspace**
parameter.

### **View input** — Display input in MATLAB `off` (default) | `on`

Select this parameter to view the input video stream data in the MATLAB viewer.
## Libraries

SoC Blockset / Hardware Logic Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Receive continuous video stream data

The Video Test Sink block receives continuous video stream data from
advanced extensible interface AXI4-based video stream data interface blocks. You can use this
block as a test sink block for simulating AXI4-based video stream data applications.

The block accepts video stream data along with a control bus and outputs a control
bus.
