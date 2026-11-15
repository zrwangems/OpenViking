---
type: simulink-block
title: 'Vector To DAC'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'vectortodac'
documentation_source_path: 'ref/vectortodac.html'
language: en
---

# Vector To DAC

## Ports

### Input

### **vectorData** — DAC data samples in vector form vector

DAC data samples, specified as a column vector. This input must be an
*N*-element column vector of *N* samples, where
the first sample is the lower significant bit (LSB), and the last sample is the most
significant bit (MSB). *N* is the length of the input word set by the
**Shortened input word length** parameter.

**Data Types:** `int16` | `uint16`
### Output

### **dacData** — DAC data samples scalar

DAC data samples, returned as a scalar. The block returns *N* x
16 bit output samples, where *N* is the length of the input word set
by the **Shortened input word length** parameter.

**Data Types:** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Shortened input word length** — Length of input word `16` (default) | integer from 1 to 16

Specify the input word length as an integer from 1 to 16. This parameter sets the
required input vector size and the bit width of the output samples.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design and
execute on an SoC device, use the SoC Builder
tool.

## Version History

**Introduced in R2020b**

## Description

Convert vector inputs to concatenated 16-bit DAC output samples

The Vector To DAC block converts the vector input to concatenated 16-bit
digital-to-analog converter (DAC) output samples.

The block accepts a vector of *N* samples through the
**vectorData** input port and outputs 16-bit samples packed into
*N* x 16 bits through the **dacData** output port based on the
*N* value. *N* is the length of the input word.
