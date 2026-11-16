---
type: simulink-block
title: 'ADC To Vector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'adctovector'
documentation_source_path: 'ref/adctovector.html'
language: en
---

# ADC To Vector

## Ports

### Input

### **adcData** — ADC data samples scalar

ADC data samples, specified as a scalar. The size of this input must be
*N* x 16 bits, where *N* is the number of samples
per clock cycle set by the **Samples per clock** parameter.

**Data Types:** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **vectorData** — ADC data samples in vector form vector

ADC data samples, returned as a vector. The block returns the data as an
*N*-element column vector, where *N* is the number
of samples per clock cycle set by the **Samples per clock**
parameter.

For example, consider the case where *N* = 2 and the input to the
**adcData** port is of size 32 bits. In this case, the block returns vector
[*S*0,
*S*1], where
*S*0 is a 16-bit value sliced from 0 to 15
bits of input data from the **adcData** port, and
*S*1 is a 16-bit value sliced from 16 to 31
bits of input data from the **adcData** port.

**Data Types:** `int16` | `uint16`

## Parameters

### **Samples per clock** — Number of samples per clock cycle `4` (default) | integer from 1 to 16

Specify the number of samples per clock cycle as an integer from 1 to 16. This
parameter sets the required bit width of the input samples and sets the output vector
size.

### **Output data type** — Output data type `fixdt(1,16,0)` (default) | `int16` | `uint16`

Specify the output data type as a signed or unsigned fixed point or an integer data
type. For more information on how to specify output data type, see Specify Data Types Using Data Type Assistant.

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

Convert concatenated 16-bit ADC input samples to vector outputs

The ADC To Vector block converts the concatenated 16-bit analog-to-digital
converter (ADC) input samples to vector outputs.

The block accepts 16-bit samples packed into *N* x 16 bits through the
**adcData** input port and outputs a vector of *N* samples through
the **vectorData** output port. *N* is the number of samples per
clock cycle.
