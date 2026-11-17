---
type: simulink-block
title: 'Stream Connector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'streamconnector'
documentation_source_path: 'ref/streamconnector.html'
language: en
---

# Stream Connector

## Ports
```yaml
ports:
- name: wrData
  summary: Input stream data scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: wrValid
  summary: Indication of valid input stream data boolean scalar
  direction: input
  data_types: Boolean
- name: wrLast
  summary: Indication of last beat in burst boolean scalar
  direction: input
  data_types: Boolean
- name: rdReady
  summary: Ready signal from downstream interface boolean scalar
  direction: input
  data_types: Boolean
- name: rdData
  summary: Output stream data scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: rdValid
  summary: Indication of valid output stream data boolean scalar
  direction: output
  data_types: Boolean
- name: rdLast
  summary: Indicates last beat in burst boolean scalar
  direction: output
  data_types: Boolean
- name: wrReady
  summary: Ready signal to upstream interface boolean scalar
  direction: output
  data_types: Boolean
```

### Input

### **wrData** — Input stream data scalar

Input stream data from the data source. Specify this value as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrValid** — Indication of valid input stream data boolean scalar

Control signal that indicates if the input data from the data source is valid.
When this value is (true), the block accepts the values on the **wrData**
port. When this value is (false), the block ignores the value on the
**wrData** port.

**Data Types:** `Boolean`

### **wrLast** — Indication of last beat in burst boolean scalar

Control signal that indicates the last beat of data from the upstream IP.

**Data Types:** `Boolean`

### **rdReady** — Ready signal from downstream interface boolean scalar

Control signal that indicates if the block can send stream data to the downstream
interface. When this value is (true), the downstream block is ready to receive
data.

**Data Types:** `Boolean`
### Output

### **rdData** — Output stream data scalar

Output stream data to the downstream destination IP.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdValid** — Indication of valid output stream data boolean scalar

Control signal that indicates if the output stream data is valid.

**Data Types:** `Boolean`

### **rdLast** — Indicates last beat in burst boolean scalar

Control signal that indicates that the output stream data now has last beat of
burst data.

**Data Types:** `Boolean`

### **wrReady** — Ready signal to upstream interface boolean scalar

Control signal that indicates if the block can receive stream data from the
upstream interface.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

SoC Blockset / Hardware Logic Connectivity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

Using SoC Blockset™, you can model a simplified streaming protocol in your model. Use HDL Coder™ to generate AXI4-Stream interfaces in the IP core. For more information about
the AXI4-stream protocol, see AXI4-Stream Interface.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Connect two IPs with data streaming interfaces

The Stream Connector block connects two IPs with data streaming interfaces.
Use this block in the FPGA model of an SoC application to connect two IPs.
