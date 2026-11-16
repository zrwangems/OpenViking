---
type: simulink-block
title: 'Aurora 64B66B'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'aurora64b66b'
documentation_source_path: 'ref/aurora64b66b.html'
language: en
---

# Aurora 64B66B

## Ports

### Input

### **M\_AXIS\_wrReady** — Ready signal from downstream interface `0` | `1`

Control signal that indicates if the block can send stream data to the downstream
interface. When this value is `1` (`true`), the
downstream block is ready to receive data.

**Data Types:** `Boolean`

### **S\_AXIS\_rdData** — Input stream data scalar

Input stream data from the data source. Specify this value as a scalar.

**Data Types:** `uint64`

### **S\_AXIS\_rdValid** — Indication of valid input stream data `0` | `1`

Control signal that indicates if the input data from the data source is valid.
When this value is `1` (`true`), the block accepts
the values on the **S\_AXIS\_rdData** input port. When this value is
`0` (`false`), the block ignores the value on the
**S\_AXIS\_rdData** input port.

**Data Types:** `Boolean`

### **S\_AXIS\_rdLast** — Indication of last beat in burst `0` | `1`

Control signal that indicates the last beat of data from the upstream IP.

**Data Types:** `Boolean`

### **loopback** — Loopback mode selection scalar

Select loopback mode.

- `0` — The block does not loop back the transmitted
  data.
- `2` — The block loops back the transmitted data into
  the transceiver.

For more information about loopback modes, see UltraScale Architecture GTY Transceivers from the
Xilinx website.

**Data Types:** `fixdt(0,3,0)`
### Output

### **M\_AXIS\_wrData** — Output stream data scalar

Output stream data to the downstream destination IP.

**Data Types:** `uint64`

### **M\_AXIS\_wrValid** — Indication of valid output stream data `0` | `1`

Control signal that indicates if the output stream data is valid. When this value
is `1` (`true`), the block returns valid data on the
**M\_AXIS\_wrData** output port. When this value is `0`
(`false`), the values on the **M\_AXIS\_wrData** output port
are not valid.

**Data Types:** `Boolean`

### **M\_AXIS\_wrLast** — Indication of last beat in burst `0` | `1`

Control signal that indicates that the output stream data now has last beat of
burst data.

**Data Types:** `Boolean`

### **S\_AXIS\_rdReady** — Ready signal to upstream interface `0` | `1`

Control signal that indicates if the block can receive stream data from the
upstream interface.

**Data Types:** `Boolean`

## Parameters

### **Simulate using** — Simulation mode selection `Code generation` (default) | `Interpreted execution`

Select the simulation mode.

- `Code generation` — On the first model run,
  simulate and generate code for the block. If the structure of the block does not
  change, subsequent model runs do not regenerate the code.
- `Interpreted execution` — Simulate the block
  using the MATLAB® execution engine. Choosing this option can slow simulation
  performance.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design and
execute on an SoC device, use the SoC Builder
tool.

## Version History

**Introduced in R2023a**

## Description

Provide high-speed serial communication using Xilinx Aurora interface

The Aurora 64B66B block provides high-speed serial communication using the
Xilinx® Aurora 64B/66B cores.

For more information about Aurora 64B/66B cores, see Aurora 64B/66B from the Xilinx website.
