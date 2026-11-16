---
type: simulink-block
title: 'HDMI Tx'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'hdmitx'
documentation_source_path: 'ref/hdmitx.html'
language: en
---

# HDMI Tx

## Ports

### Input

### **hdmiTxData** — Single YCbCr 4:2:2 pixel in pixel stream concatenated YCbCr value

Single YCbCr 4:2:2 pixel in pixel stream, specified as a scalar in
concatenated YCbCr 4:2:2 format, where

- bits [1:8] represent Y.
- bits [9:16] represent Cb or Cr, interleaved in
  time.

**Data Types:** `uint16`

### **ctrl** — Control signals accompanying input pixel stream `pixelcontrol` bus

Control signals accompanying input pixel stream, specified as a `pixelcontrol` (Vision HDL Toolbox) bus. The bus contains five
Boolean signals indicating the validity of a pixel and its location
within a frame.

When the **Input mode** parameter is
`Frame`, the block sets all five signals in
the `pixelcontrol` bus to `true` to
indicate when the output data is valid.

**Data Types:** `bus`
### Output

### **frame** — Output frame data vector

Output frame data, returned as a vector in the YCbCr 4:2:2
format.

#### Dependencies

To enable this port, select the **Frame output**
parameter.

**Data Types:** `uint8`

### **valid** — Control signal accompanying output frame data scalar

Control signal accompanying output frame data, returned as a
scalar.

This port is a control signal that indicates when the
**frame** output port is valid. The block sets this
value to `1` when the data is available on the
**frame** output port.

#### Dependencies

To enable this port, select the **Frame output**
parameter.

**Data Types:** `Boolean`

## Parameters

### **Frame size** — Video frame size `160x120p` (default) | ...

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

### **Input mode** — Video input format `Frame` (default) | `Pixel`

Specify whether the input is streamed one pixel per clock cycle or one
frame per clock. `Pixel` mode better represents the
hardware algorithm and is recommended for FPGA deployment.
`Frame` mode enables faster simulation.

### **Visualize output frame** — Display output video `on` (default) | `off`

Select this parameter to
enable a To Video Display (Computer Vision Toolbox) block to display
the output frame during simulation.

### **Frame output** — Frame output `off` (default) | `on`

Select this parameter to enable the output ports
**frame** and **valid**. Using these
ports, you can access video frame data from this block and export it to any
file or a workspace variable.

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

Convert YCbCr 4:2:2 pixel stream to video frame

The HDMI Tx block converts a pixel stream in YCbCr 4:2:2 format to raw
video data for display during simulation. It can return data in pixel stream mode for
hardware algorithm design or in frame mode for faster simulation. When you include this
block in your design, the SoC Builder tool generates all the IP blocks
necessary to transmit video data to the FMC-HDMI-CAM card attached to your hardware
board. None of the block parameters affect hardware behavior.

You must have Computer Vision Toolbox™ to use this block.
