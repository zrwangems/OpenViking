---
type: simulink-block
title: 'RFDC Bus Selector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'rfdcbusselector'
documentation_source_path: 'ref/rfdcbusselector.html'
language: en
---

# RFDC Bus Selector

## Ports

### Input

### **ctrlBus** — Input control bus bus

Input control bus, specified as a bus.

**Data Types:** `RFDC2DUTRealTimeCtrlBusObj`
### Output

### **overRange** — Over range output `Boolean` scalar

Over range output, returned as a Boolean scalar. A `High` on this
output indicates that the signal exceeds the full-scale input of the digital-to-analog
converter (DAC) or analog-to-digital converter (ADC).

**Data Types:** `Boolean`

### **overThreshold1** — Over threshold 1 output `Boolean` scalar

Over threshold 1 output, returned as a Boolean scalar. A `High`
on this output indicates that the signal amplitude level exceeds the threshold value
specified by the **Threshold1** parameter in the RF Data
Converter block.

**Data Types:** `Boolean`

### **overThreshold2** — Over threshold 2 output `Boolean` scalar

Over threshold 2 output, returned as a Boolean scalar. A `High`
on this output indicates that the signal amplitude level exceeds the threshold value
specified by the **Threshold2** parameter in the RF Data
Converter block.

**Data Types:** `Boolean`

### **overVoltage** — Over voltage output `Boolean` scalar

Over voltage output, returned as a Boolean scalar. An `Over
Voltage` condition occurs when a signal far exceeds the normal operating
input-range. For more information, see Zynq UltraScale+ RFSoC RF Data Converter v2.6 Gen 1/2/3 in the Xilinx® documentation.

**Data Types:** `Boolean`

### **commonmodeOverVoltage** — Common mode over voltage output `Boolean` scalar

Common mode over voltage output, returned as a Boolean scalar. A
`High` on this output indicates that the input signal common mode
exceeds the safe operating conditions. For more information, see Zynq UltraScale+ RFSoC RF Data Converter v2.6 Gen 1/2/3 in the Xilinx documentation.

#### Dependencies

To enable this port, select **Gen 3**.

**Data Types:** `Boolean`

### **commonmodeUnderVoltage** — Common mode under voltage output `Boolean` scalar

Common mode under voltage output, returned as a Boolean scalar. A
`High` on this output indicates that the input signal common mode
is too low for safe operation. For more information, see Zynq UltraScale+ RFSoC RF Data Converter v2.6 Gen 1/2/3 in the Xilinx documentation.

#### Dependencies

To enable this port, select **Gen 3**.

**Data Types:** `Boolean`

## Parameters

### **Gen 3** — Option to add ports for Gen 3 devices `off` (default) | `on`

Select this parameter to add ports for Gen 3 Zynq®
UltraScale+™ RFSoC devices.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute on an SoC device, use
the SoC Builder
tool.

## Version History

**Introduced in R2022a**

## Description

Convert RF Data Converter real-time interface-compatible bus into control signals

The RFDC Bus Selector block separates an RF Data Converter
real-time interface-compatible bus into a set of control signals. The block accepts a bus and
outputs control signals.
