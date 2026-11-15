---
type: simulink-block
title: 'Array Processing'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'arrayprocessing'
documentation_source_path: 'slref/arrayprocessing.html'
language: en
---

# Array Processing

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**Limitations**

- The Array Processing Subsystem block does not support HDL code
  generation if it is at the top level of the model.
- The Array Processing Subsystem block does not support HDL code
  generation if the model does not have the **Enable frame to
  sample conversion (HDL Coder)** model configuration parameter selected.

## Version History

**Introduced in R2024a**

## Description

Control block for Array Processing Subsystem

The Array Processing block serves as a control block for the Array Processing
Subsystem block. The Array Processing Subsystem block applies an
algorithm to each element of an input matrix and returns an output matrix that contains the
output of that algorithm for each element of the input matrix, similarly to the `arrayfun` function
and the For Each Subsystem block.

The Array Processing Subsystem block is optimized for large input matrices
such as image data. Use the Array Processing Subsystem block for
high-performance element-wise operations such as image processing tasks.
