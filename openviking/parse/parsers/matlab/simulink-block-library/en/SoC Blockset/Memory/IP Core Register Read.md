---
type: simulink-block
title: 'IP Core Register Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'ipcoreregisterread'
documentation_source_path: 'ref/ipcoreregisterread.html'
language: en
---

# IP Core Register Read

## Ports
```yaml
ports:
- name: data
  summary: Data output vector
  direction: output
  data_types: single | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Output

### **data** — Data output vector

This port outputs the data vector received from the processor, starting at the
offset address from the base address of the IP core. Set the offset address in the
Hardware Mapping
tool.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Register name
  summary: Name of register RegA (default) | character vector
  group: ''
- name: Output data type
  summary: Data type of output data uint16 (default) | single | int8 | uint8 | int16 | int32 | uint32 | boolean | fixed point
    data type
  group: ''
- name: Output vector size
  summary: Vector size of output data 1 (default) | positive integer
  group: ''
- name: Sample time
  summary: Simulation interval of sampling -1 (default) | nonnegative scalar
  group: ''
```

### **Register name** — Name of register `RegA` (default) | character vector

Match this name to the **Register name** parameter specified in the
Register Write
block.

**Example:** `AddressReg1`

### **Output data type** — Data type of output data `uint16` (default) | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32` | `boolean` | `fixed point data type`

Select the data type for the output data. This value must match the value selected
for the Register Write
block.

### **Output vector size** — Vector size of output data `1` (default) | positive integer

Specify the vector size of the output data as a positive integer. This value must
match the value selected for the Register Write
block.

### **Sample time** — Simulation interval of sampling `-1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block outputs data. If
this value is `-1` (default), the sample time is inherited from the
model.
## Libraries

SoC Blockset / Memory

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Model register writes from software to hardware

The IP Core Register Read block models a write operation from a processor
to hardware logic. The block receives data sent with a Register Write block
from the processor. You can define the register offset in the Hardware Mapping
tool.
