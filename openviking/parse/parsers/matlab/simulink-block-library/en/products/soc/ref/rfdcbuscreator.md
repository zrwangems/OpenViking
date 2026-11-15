---
type: simulink-block
title: 'RFDC Bus Creator'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'rfdcbuscreator'
documentation_source_path: 'ref/rfdcbuscreator.html'
language: en
---

# RFDC Bus Creator

## Ports

### Input

### **NCOFrequency** — Frequency for NCO mixer scalar

Frequency for the numerically controlled oscillator (NCO) mixer, specified as a
scalar. The NCO frequency value ranges from
–*F*s/2 to
*F*s/2, where
*F*s is the sample rate in Hz.

The block calculates the RF Data Converter real-time
interface-compatible NCO frequency as `NCOFrequency` x
(2*48* /
*F*s).

#### Dependencies

To enable this port, set **Control type** to
`NCO` or `NCO and
threshold`.

**Data Types:** `fixdt(1,48,0)`

### **NCOPhase** — Phase value for output of NCO mixer scalar

Phase value for the output of the NCO mixer, specified as a scalar. The NCO phase
value ranges from –180 to 180 degrees.

The block calculates the RF Data Converter real-time
interface-compatible NCO phase as `NCOPhase` x
(2*18* / 360).

#### Dependencies

To enable this port, set **Control type** to
`NCO` or `NCO and
threshold`.

**Data Types:** `fixdt(1,18,0)`

### **NCOPhaseReset** — Control signal that resets NCO phase offset `Boolean` scalar

Control signal that resets the NCO phase offset, specified as a Boolean
scalar.

#### Dependencies

To enable this port, set **Control type** to
`NCO` or `NCO and
threshold`.

**Data Types:** `Boolean`

### **NCOUpdateEnable** — Control signal that determines which NCO frequency and phase bits to update scalar

Control signal that determines which NCO frequency and phase bits to update,
specified as a scalar. Set the bits in this signal to `High` to
update the following bits of the frequency and phase value of the NCO.

- Bit 5 — Reset the phase offset to `0`
- Bit 4 — `NCOPhase[17:16]`
- Bit 3 — `NCOPhase[15:0]`
- Bit 2 — `NCOFrequency[47:32]`
- Bit 1 — `NCOFrequency[31:16]`
- Bit 0 — `NCOFrequency[15:0]`

For example, if you set only the bit 1 and bit 0 of
**NCOUpdateEnable** to `High`, only the NCO
frequency gets an update in its value on an update event.

#### Dependencies

To enable this port, set **Control type** to
`NCO` or `NCO and
threshold`.

**Data Types:** `fixdt(0,6,0)`

### **PLEvent** — Control signal that clears threshold status signal `Boolean` scalar

Control signal that clears the threshold status signal, specified as a Boolean
scalar.

#### Dependencies

To enable this port, set **Control type** to
`Threshold` or `NCO and
threshold`.

**Data Types:** `Boolean`

### **clearOverRange** — Control signal that clears over range signal `Boolean` scalar

Control signal that clears the over range signal, specified as a Boolean
scalar.

#### Dependencies

To enable this port, set **Control type** to
`Threshold` or `NCO and
threshold`.

**Data Types:** `Boolean`

### **clearOverVoltage** — Control signal that clears over voltage signal `Boolean` scalar

Control signal that clears the over voltage signal, specified as a Boolean
scalar.

#### Dependencies

To enable this port, set **Control type** to
`Threshold` or `NCO and
threshold` and select **Gen 3**.

**Data Types:** `Boolean`
### Output

### **ctrlBus** — Output control bus bus

Output control bus, returned as a bus.

**Data Types:** `DUT2RFDCRealTimeCtrlBusObj`

## Parameters

### **Control type** — Control type selection `NCO` (default) | `Threshold` | `NCO and threshold`

Specify the type of control.

- `NCO` — Connect DUT NCO control signals to the
  RF Data
  Converter block.
- `Threshold` — Connect DUT threshold control
  signals to the RF Data Converter block.
- `NCO and threshold` — Connect DUT NCO and
  threshold control signals to the RF Data Converter block.

The input ports of the block vary based on the type of **Control
type** that you select. For more details, see Description.

### **Gen 3** — Option to add ports for Gen 3 devices `off` (default) | `on`

Select this parameter to add ports for Gen 3 Zynq®
UltraScale+™ RFSoC devices.

#### Dependencies

To enable this parameter, set **Control type** to
`Threshold` or `NCO and
threshold`.

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

Convert control signals into RF Data Converter real-time interface-compatible bus

The RFDC Bus Creator block combines a set of control signals into an
RF Data Converter real-time interface-compatible bus. The block accepts
control signals and outputs a bus.

Port configurations for this block vary based on your control type selection.

| Parameter Configuration | Enabled Input Ports |
| --- | --- |
| Set **Control type** to `NCO`. | **NCOFrequency** |
| **NCOPhase** |
| **NCOPhaseReset** |
| **NCOUpdateEnable** |
| Set **Control type** to `Threshold`. | **PLEvent** |
| **clearOverRange** |
| Set **Control type** to `Threshold` and select **Gen 3**. | **PLEvent** |
| **clearOverRange** |
| **clearOverVoltage** |
| Set **Control type** to `NCO and threshold`. | **NCOFrequency** |
| **NCOPhase** |
| **NCOPhaseReset** |
| **NCOUpdateEnable** |
| **PLEvent** |
| **clearOverRange** |
| Set **Control type** to `NCO and threshold` and select **Gen 3**. | **NCOFrequency** |
| **NCOPhase** |
| **NCOPhaseReset** |
| **NCOUpdateEnable** |
| **PLEvent** |
| **clearOverRange** |
| **clearOverVoltage** |
