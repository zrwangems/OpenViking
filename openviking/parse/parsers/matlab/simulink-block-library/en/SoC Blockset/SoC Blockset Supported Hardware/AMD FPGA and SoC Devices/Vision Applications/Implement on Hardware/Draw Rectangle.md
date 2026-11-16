---
type: simulink-block
title: 'Draw Rectangle'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Implement on Hardware'
documentation_page: 'drawrectangle'
documentation_source_path: 'ref/drawrectangle.html'
language: en
---

# Draw Rectangle

## Ports

### Input

### **points** — Rectangle coordinates and dimensions N-by-4 matrix

Specify the rectangle coordinates as an *N*-by-4 matrix of the
form `[x
y
width
height]`, where *N* is the number of
rectangles to draw, *x*
*y* are coordinates of the top-left corner of each rectangle, and
*width*
*height* are the horizontal and vertical dimensions of each
rectangle.

**Data Types:** `uint32`

### **valid** — Enable frame annotation `Boolean`

When this input is `true` (`1`), the block
modifies all frames found in memory. Your design should provide the
**points** values and set **valid** to
`true` once video frames are available in memory.

**Data Types:** `Boolean`

## Parameters

### **Color** — Color of rectangle bounding line `Green` (default) | `Red` | `Blue` | `Black` | `White`

Color of the rectangle bounding line, specified as `Green`,
`Red`, `Blue`,
`Black`, or `White`.

### **Thickness** — Thickness of rectangle bounding line 3 (default) | scalar

Thickness of rectangle bounding line, specified as a number of pixels.

## Libraries

Find this block in the YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware example

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Draw rectangles onto video frame stored in external memory

The Draw Rectangle block overlays a rectangle onto a video frame stored in
external memory. For instance, you can use this block to display bounding boxes around
identified objects. The block uses the processor-FPGA interface and the memory map for this
reference design to read and modify the specified pixels in the frame.

You can use this block only once per model. Your design should provide the
**points** values and set **valid** to
`true` once video frames are available in memory. The YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware (Vision HDL Toolbox) example shows how to use
this block in the postprocessing model that is targeted to the ARM® processor.
