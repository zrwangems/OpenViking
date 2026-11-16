---
type: simulink-block
title: 'Deinterleave'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'deinterleave'
documentation_source_path: 'ref/deinterleave.html'
language: en
---

# Deinterleave

## Ports

### Input

### **CbCr** — Interleaved video frame matrix

Interleaved video frame, specified as a matrix. The matrix represents
the chrominance component of an image in YCbCr 4:2:2 format. It contains
interleaved Cb and Cr pixel values.
### Output

### **Cb** — Blue chrominance frame matrix

Blue chrominance frame, returned as a matrix. The matrix is half the
size of the input matrix.

### **Cr** — Red chrominance frame matrix

Red chrominance frame, returned as a matrix. The matrix is half the
size of the input matrix.

## Parameters

Not documented in R2025b.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / PicoZed SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC702 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Convert interleaved CbCr frame to separate components

The Deinterleave block accepts an input video frame consisting of
interleaved Cb and Cr values. The output is separate Cb and Cr frames. Use this block to
convert an interleaved frame from the HDMI FMC card to separate Cb and Cr frame
components for connecting to Computer Vision Toolbox™ blocks. The frame size of the Cb and Cr output components is half the size
of the associated Y component.

**Note**

This block does not support HDL code generation, and you cannot use this block
inside the FPGA user logic.

The FPGA data path for YCbCr 4:2:2 format consists of a Y component and a
time-interleaved CbCr component. The pixel-streaming subsystem targeted for the user
logic on the FPGA must have these two input and output ports. When you convert the pixel
stream to frames, use dummy data (duplicate the CbCr component) for the third component.
The resulting frame has 3 full-sized components. To connect to Computer Vision Toolbox blocks, drop the duplicate component and separate the interleaved frame
into the half-size Cb and Cr component frames. See the Pixels to Frame for YCbCr
4:2:2 block in the YCbCr 4:2:2 HDL Pixel-Streaming Algorithm template, and
the example models.
