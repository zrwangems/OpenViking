---
type: simulink-block
title: 'Stream Data Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'streamdatasink'
documentation_source_path: 'ref/streamdatasink.html'
language: en
---

# Stream Data Sink

## Ports

### Input

### **rdData** — Input stream data scalar | vector

Input stream data from the data source. This value must be a scalar or
vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdCtrlIn** — Input control bus bus

Input control bus from the data source. This control bus comprises the following
control signals:

- `valid` — Indicates the input stream data on the
  **rdData** input port is valid
- `tlast` — Indicates the end of the data transaction

**Data Types:** `StreamM2SBusObj`
### Output

### **rdCtrlOut** — Output control bus bus

Output control bus to the data source, indicating that the block is ready to
accept stream data. This control bus comprises a ready signal.

**Data Types:** `StreamS2MBusObj`

## Parameters

### **Save data in workspace** — Save data in workspace `off` (default) | `on`

Select this parameter to save the input stream data to the MATLAB® workspace.

### **Variable name** — Workspace variable name `simOut` (default) | any MATLAB-supported variable name

Specify the workspace variable to which input stream data is saved. This parameter
can be any MATLAB-supported variable name.

#### Dependencies

To enable this parameter, select the **Save data in workspace**
parameter.

## Libraries

SoC Blockset / Hardware Logic Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Receive continuous stream data

The Stream Data Sink block receives continuous stream data from advanced
extensible interface AXI4-based stream data interface blocks. You can use this block as a test
sink block for simulating AXI4-based stream data applications.

The block accepts stream data along with a control bus and outputs a control bus.
