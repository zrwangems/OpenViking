---
type: simulink-block
title: 'Interleave'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'interleave'
documentation_source_path: 'ref/interleave.html'
language: en
---

# Interleave

## Ports

### Input

### **Cb** — Blue chrominance frame matrix

Blue chrominance frame, specified as a matrix. The matrix represents
the blue chrominance component of an image in YCbCr 4:2:2 format. The
matrix contains half the values of the corresponding Y frame.

### **Cr** — Red chrominance frame matrix

Red chrominance frame, specified as a matrix. The matrix represents
the red chrominance component of an image in YCbCr 4:2:2 format. The
matrix contains half the values of the corresponding Y frame.
### Output

### **CbCr** — Interleaved video frame matrix

Interleaved video frame, returned as a matrix. It is twice the size of
the input matrices, and contains interleaved Cb and Cr pixel
values.

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

Convert separate Cb and Cr components into interleaved CbCr frame

The Interleave block accepts separate Cb and Cr frame components. The
output is a frame consisting of interleaved Cb and Cr data. Use this block to prepare
for conversion from frames to pixel-streaming when targeting YCbCr 4:2:2 format on the
FPGA with an HDMI FMC card.

**Note**

This block does not support HDL code generation, and you cannot use this block
inside the FPGA user logic.

The FPGA data path for YCbCr 4:2:2 format consists of a Y component and a
time-interleaved CbCr component. The pixel-streaming subsystem targeted for the user
logic on the FPGA must have these two input and output ports. Captured YCbCr video data
from board comes into Simulink® as three component frames. The horizontal size of the Cb and Cr frames is
half the size of the Y component. For pixel-streaming design, recreate an interleaved
CbCr component by combining the Cb and Cr frames before converting to a pixel stream.
When you convert the frame to pixel streams, use dummy data (duplicate the interleaved
CbCr frame) for the third component. See the Frame to Pixels for YCbCr
4:2:2 block in the YCbCr 4:2:2 HDL Pixel-Streaming Algorithm template, and
the example models.
