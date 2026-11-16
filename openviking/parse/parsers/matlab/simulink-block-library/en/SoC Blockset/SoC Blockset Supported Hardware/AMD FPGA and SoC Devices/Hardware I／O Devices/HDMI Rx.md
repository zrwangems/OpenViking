---
type: simulink-block
title: 'HDMI Rx'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'hdmirx'
documentation_source_path: 'ref/hdmirx.html'
language: en
---

# HDMI Rx

## Ports

### Output

### **hdmiRxData** — Single YCbCr 4:2:2 pixel in pixel stream concatenated YCbCr value

Single YCbCr 4:2:2 pixel in pixel stream, specified as a scalar in
concatenated YCbCr 4:2:2 format, where

- bits [1:8] represent Y.
- bits [9:16] represent Cb or Cr, interleaved in
  time.

**Data Types:** `uint16`

### **ctrl** — Control signals accompanying output pixel stream `pixelcontrol` bus

Control signals accompanying output pixel stream, returned as a `pixelcontrol` (Vision HDL Toolbox) bus. The bus contains five
Boolean signals indicating the validity of a pixel and its location
within a frame.

When the **Output mode** parameter is
`Frame`, the block sets all five signals in
the `pixelcontrol` bus to `true` to
indicate when the output data is valid.

**Data Types:** `bus`

## Parameters

#### Main

### **Frame size** — Video frame size `160x120p` (default) | `Pixel` | ...

Select the video frame size as one of these values:

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

### **Output mode** — Output mode of the block `Frame` (default) | `Pixel`

Specify whether the output is streamed one pixel per clock cycle or one
frame per clock. `Pixel` mode better represents the
hardware algorithm and is recommended for FPGA deployment.
`Frame` mode enables faster simulation.

#### Simulation

### **Input file name** — Input video file character vector

Specify the full path to an input video file. For information on the
supported file types, see From Multimedia File (Computer Vision Toolbox).

**Example:** `'handshake_left.avi'`

### **Frame sample time** — Block sample time `1/60` (default) | positive scalar

Block sample time, in seconds, specified as a positive scalar. The default
value corresponds to a frame rate of 60 fps.

### **Visualize input frame** — Display input video `on` (default) | `off`

Selecting this option enables a To Video Display (Computer Vision Toolbox) block to display
the input frame during simulation.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your
design, and execute on an SoC device, use the SoC Builder
tool.

## Version History

**Introduced in R2019a**

## Description

Convert video stream to YCbCr 4:2:2 pixel stream

The HDMI Rx block converts raw video data to a YCbCr 4:2:2 pixel stream
format. It can return data in pixel stream mode for hardware algorithm design or in
frame mode for faster simulation. When you include this block in your design, the
SoC Builder tool generates all the IP blocks necessary to receive video
data from the FMC-HDMI-CAM card attached to your hardware board. None of the block
parameters affect hardware behavior. When simulating, specify a video file to
stream.

You must have Computer Vision Toolbox™ to use this block.
