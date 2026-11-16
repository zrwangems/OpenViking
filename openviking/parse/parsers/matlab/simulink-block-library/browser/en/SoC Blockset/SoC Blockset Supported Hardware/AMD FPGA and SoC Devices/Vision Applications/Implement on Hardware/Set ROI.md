---
type: simulink-block
title: 'Set ROI'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Implement on Hardware'
documentation_page: 'setroi'
documentation_source_path: 'ref/setroi.html'
language: en
---

# Set ROI

## Ports

### Input

### **StartPos** — Coordinates of top-left corner of ROI N-by-2-matrix

Specify the coordinates of the ROIs as an *N*-by-2 matrix of the
form `[x
y]`, where *N* is the number of ROIs,
and *x*
*y* are coordinates of the top-left corner of each rectangle.

**Data Types:** `single` | `double` | `uint32`

### **ROI** — Replacement pixel values for the region of interest matrix

Specify the replacement pixel values as a matrix of
*N*-by-*width*-by-*height*. All
the ROIs must be the same size.

**Data Types:** `single` | `double` | `uint32`

### **valid** — Enable frame annotation `Boolean`

When this input is `true` (`1`), the block
modifies all frames found in memory. Your design should provide the
**StartPos** and **ROI** values and set
**valid** to `true` once video frames are
available in memory.

**Data Types:** `Boolean`

## Parameters

### **Use row-major format** — Read and modify frame buffer in row-major order on (default) | off

This block assumes the frame is stored in memory in row-major order. If your design
stores the frame in column-major order, clear this checkbox.

## Libraries

Find this block in the YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware example

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Draw over specified region of video frame stored in external memory

The Set ROI block overwrites one or more rectangular regions of a video
frame stored in external memory. For instance, you can use this block to display score labels
on identified objects. The block uses the processor-FPGA interface and the memory map of this
reference design to read and modify the specified pixels in the frame.

You can use this block only once per model. Your design should provide the ROI coordinates
and replacement values and set **valid** to `true` once
video frames are available in memory. The YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware (Vision HDL Toolbox) example shows how to use
this block in the postprocessing model that is targeted to the ARM® processor.
