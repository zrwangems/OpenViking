---
type: simulink-block
title: 'OTAVA DTRX2'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'otavadtrx2'
documentation_source_path: 'ref/otavadtrx2.html'
language: en
---

# OTAVA DTRX2

## Ports

### Input

### **RFIn*`x`*** — RX input data scalar | column vector

RX input data, specified as a scalar or column vector with a length in the range
[1, *N*], where *N* is the number of samples per
clock cycle.

***`x`*** indicates the RX channel number.
The values of ***`x`*** range from 1 to 2. The
number of **RFIn** ports depends on the number of RX channels that you enable
in the block.

**Data Types:** `uint16` | `uint32` | `uint64` | `fixed point`

### **IFIn*`x`*** — TX input data column vector

TX input data, specified as a column vector.

***`x`*** indicates the TX channel number.
The values of ***`x`*** range from 1 to 2. The
number of **IFIn** ports depends on the number of TX channels that you enable
in the block.

**Data Types:** `int16`
### Output

### **IFOut*`x`*** — RX output data column vector

RX output data, returned as a column vector.

***`x`*** indicates the RX channel number.
The values of ***`x`*** range from 1 to 2. The
number of **IFOut** ports depends on the number of RX channels that you
enable in the block.

**Data Types:** `int16` | `uint16`

### **RFOut*`x`*** — TX output data scalar | column vector

TX output data, returned as a scalar or column vector with a length in the range
[1, *N*], where *N* is the number of samples per
clock cycle.

***`x`*** indicates the TX channel number.
The values of ***`x`*** range from 1 to 2. The
number of **RFOut** ports depends on the number of TX channels that you
enable in the block.

**Data Types:** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### RX Channel

### **Enable Channel 1** — Option to enable RX1 channel `on` (default) | `off`

Select this parameter to enable the RX1 channel.

### **Enable Channel 2** — Option to enable RX2 channel `on` (default) | `off`

Select this parameter to enable the RX2 channel.

### **Center frequency (GHz)** — Center frequency of RX channel `27.5` (default) | finite scalar in the range [19, 31]

Specify the center frequency of the RX channel as a finite scalar in the range
[19, 31].

### **Intermediate frequency (GHz)** — IF of RX channel `3.7` (default) | finite scalar in the range [3.4, 4.3]

Specify the intermediate frequency (IF) of the RX channel as a finite scalar in
the range [3.4, 4.3].

### **IF Signal band width (MHz)** — Bandwidth of IF signal `50` (default) | finite scalar up to 800

Specify the bandwidth of the IF signal in MHz as a finite scalar up to 800.

### **IF DSA attenuation (dB)** — Attenuation of IF DSA `31` (default) | finite scalar in the range [0, 31]

Specify the attenuation of the IF digital step attenuator (DSA) as a finite scalar
in the range [0, 31]. You can increase or decrease the value of this parameter by a
step size of 1.

### **RF DSA attenuation (dB)** — Attenuation of RF DSA `14` (default) | finite scalar in the range [0, 14]

Specify the attenuation of the radio frequency (RF) DSA as a finite scalar in the
range [0, 14]. You can increase or decrease the value of this parameter by a step size
of 2.

### **Enable IF LNA** — Option to enable IF LNA `on` (default) | `off`

Select this parameter to enable the IF low-noise amplifier (LNA).

### **Enable RF LNA** — Option to enable RF LNA `on` (default) | `off`

Select this parameter to enable the RF LNA.

### TX Channel

### **Enable Channel 1** — Option to enable TX1 channel `on` (default) | `off`

Select this parameter to enable the TX1 channel.

### **Enable Channel 2** — Option to enable TX2 channel `on` (default) | `off`

Select this parameter to enable the TX2 channel.

### **Center frequency (GHz)** — Center frequency of TX channel `27.5` (default) | finite scalar in the range [19, 31]

Specify the center frequency of the TX channel as a finite scalar in the range
[19, 31].

### **Intermediate frequency (GHz)** — IF of TX channel `4.3` (default) | finite scalar in the range [3.4, 4.3]

Specify the IF of the TX channel as a finite scalar in the range [3.4,
4.3].

### **IF Signal band width (MHz)** — Bandwidth of IF signal `50` (default) | finite scalar up to 800

Specify the bandwidth of the IF signal in MHz as a finite scalar up to 800.

### **DSA attenuation (dB)** — Attenuation of DSA `15` (default) | finite scalar in the range [0, 15]

Specify the attenuation of the DSA as a finite scalar in the range [0, 15]. You
can increase or decrease the value of this parameter by a step size of 1.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208

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

Integrate OTAVA DTRX2 mmWave radio card with ZCU208 board

The OTAVA DTRX2 block integrates the OTAVA DTRX2 mmWave radio card with the
Xilinx®
Zynq®
UltraScale+™ RFSoC ZCU208 Evaluation Kit. The block provides an RF front-end interface in the
millimeter-wave (mmWave) frequency band to implement your RF applications on the ZCU208
board.

The block supports the mmWave frequency band in the 19 to 31 GHz range. Use this block to
target applications in 5G, radar, and satellite communications in Ka or Ku band.

The block accepts a vector of *N* samples through the
**IFIn***`x`* ports and outputs 16-bit samples as a column
vector with a length in the range [1, *N*] through the
**RFOut***`x`* ports. *N* is the number of
samples per clock cycle and *`x`* is 1 or 2. The block accepts 16-bit
samples as a column vector with a length in the range [1, *N*] through the
**RFIn***`x`* ports and outputs a vector of
*N* samples through the **IFOut***`x`*
ports based on the value of *N*.

In generation, the SoC Builder tool maps
the control path interface for the configuration of the DTRX2 radio card on the
hardware.

The block supports a maximum of two transmit (TX) and two receive (RX) channels. These
channels correspond to the TX and RX channels of the DTRX2 radio card.

| Block Channel | DTRX2 Radio Card Channel |
| --- | --- |
| **IFIn1** - **RFOut1** | TX1 |
| **IFIn2** - **RFOut2** | TX2 |
| **RFIn1** - **IFOut1** | RX1 |
| **RFIn2** - **IFOut2** | RX2 |

To integrate the OTAVA DTRX2 block with the RF Data Converter
block, follow these instructions.

- Connect TX1 with **DAC 1** in **Tile 0**.
- Connect TX2 with **DAC 0** in **Tile 0**.
- Connect RX1 with **ADC 1** in **Tile 3**.
- Connect RX2 with **ADC 0** in **Tile 3**.

**Note**

- Do not target any signal to the DTRX2 radio card when the card power switch is off.
  Turn the power switch on before targeting the card.
- For reference clock spurious mitigation, use a 10 dB coaxial attenuator or a
  low-pass filter with a cutoff value greater than 122.88 MHz between the CLK104 output
  and the REF\_CLK\_IN input of the DTRX2 radio card.
- Terminate all unused RF channels input and output connectors of the DTRX2 radio card
  with 50 ohms 2.92 mm terminations.

For detailed instructions on setting up and using the mmWave radio card, see Wideband mmWave Radio Dev Kit for RFSoC
Gen-3 on the Avnet® website.
