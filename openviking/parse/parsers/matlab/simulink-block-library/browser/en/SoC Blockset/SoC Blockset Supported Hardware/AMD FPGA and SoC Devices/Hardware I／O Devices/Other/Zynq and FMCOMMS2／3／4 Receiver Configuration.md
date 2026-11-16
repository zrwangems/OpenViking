---
type: simulink-block
title: 'Zynq and FMCOMMS2/3/4 Receiver Configuration'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices / Other'
documentation_page: 'zynqandfmcomms234receiverconfiguration'
documentation_source_path: 'ref/zynqandfmcomms234receiverconfiguration.html'
language: en
---

# Zynq and FMCOMMS2/3/4 Receiver Configuration

## Ports

### Input

### **center frequency** — External RF center frequency nonnegative finite scalar

External RF center frequency, specified as a nonnegative finite scalar on the
port. The valid center frequency range is from 70 MHz to 6 GHz.

#### Dependencies

To enable this port, set the **Source of center frequency**
parameter to `Input Port`.

**Data Types:** `double`

### **gain** — External gain numeric scalar | 1-by-2 numeric vector

External gain, specified as a numeric scalar or a 1-by-2 numeric vector. The valid
gain range is –10 dB to 77 dB. The resolution is 0.25 dB.

Set the gain based on the **Channel mapping** parameter configuration.

- For a single channel, specify the gain as a scalar.
- For two channels that use the same gain value, specify the gain as a scalar.
  The block applies the gain by scalar expansion.
- For two channels that use different gain values, specify the gain as a
  1-by-2 vector. The `i`th element of the vector is applied to
  the `i`th channel specified by the **Channel
  mapping** parameter.

#### Dependencies

To enable this port, set the **Source of gain** parameter to
`Input Port`.

**Data Types:** `double`

## Parameters

The Zynq and FMCOMMS2/3/4 Receiver Configuration block supports up to two channels to receive data. Use the
**Channel mapping**  parameter to indicate whether to use a single channel
or dual channels. For each channel, you can set the **Gain (dB)** parameter
independently, or you can apply the same setting to all channels. All other parameter values
are applied to each channel in use.

### Main

### **Source of center frequency** — Source of center frequency `Dialog` (default) | `Input Port`

Source of center frequency, specified as one of these options:

- `Dialog` — Set the center frequency by using the
  **Center frequency (Hz)** parameter.
- `Input Port` — Set the center frequency by using
  the **center frequency** input port.

### **Center frequency (Hz)** — RF center frequency `2400000000` (default) | nonnegative scalar

RF center frequency, in Hz, specified as a nonnegative scalar. The valid range for
center frequency is 70 MHz to 6 GHz.

#### Dependencies

To enable this parameter, set **Source of center frequency** to
`Dialog`.

**Data Types:** `double`

### **Source of gain** — Source of gain `AGC Slow Attack` (default) | `AGC Fast Attack` | `Dialog` | `Input Port`

Source of gain, specified as one of these options:

- `AGC Slow Attack` –– Use this mode for signals with
  a slowly changing power level.
- `AGC Fast Attack` –– Use this mode for signals with
  a rapidly changing power level.
- `Dialog` — Specify the gain by using the
  **Gain (dB)** parameter.
- `Input Port` — Specify the gain by using the
  **gain** input port.

### **Gain (dB)** — Gain `10` (default) | numeric scalar

Gain, in dB, specified as a numeric scalar or a 1-by-2 numeric vector. The valid
gain range is –10 dB to 77 dB. The resolution is 0.25 dB.

Set the gain based on the **Channel mapping** parameter configuration.

- For a single channel, specify the gain as a scalar.
- For two channels that use the same gain value, specify the gain as a scalar.
  The block applies the gain by scalar expansion.
- For two channels that use different gain values, specify the gain as a
  1-by-2 vector. The `i`th element of the vector is applied to
  the `i`th channel specified by the **Channel
  mapping** parameter.

#### Dependencies

To enable this parameter, set **Source of gain** to
`Dialog`.

**Data Types:** `double`

### **Channel mapping** — Channel output mapping `1` (default) | `2` | `[1 2]`

Channel output mapping, specified as one of these values:

- `1` — Specify this option to use channel 1.
- `2` — Specify this option to use channel 2.
- `[1 2]` — Specify this option to use both the
  channels.

### **Baseband sample rate (Hz)** — Baseband sampling rate `4e6` (default) | positive scalar

Baseband sampling rate, in Hz, specified as a positive scalar. The valid range of
this parameter is 520.834 kHz to 61.44
MHz.

**Data Types:** `double`

### Advanced

### **Enable quadrature tracking** — Quadrature tracking `on` (default) | `off`

When you select this parameter, the block applies in-phase and quadrature (IQ)
imbalance compensation.

### **Enable RF DC tracking** — RF DC tracking `on` (default) | `off`

When you select this parameter, the block applies an RF direct current (DC)
blocking filter.

### **Enable baseband DC tracking** — Baseband DC tracking `on` (default) | `off`

When you select this parameter, the block applies a baseband DC blocking
filter.

## Libraries

SoC Blockset Support Package for Xilinx Devices / MPSoC / ZCU102 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZedBoard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate processor code for your design, and execute on an SoC device,
use the SoC Builder tool.

## Version History

**Introduced in R2019a**

### R2024b: Not recommended

Use of this block is not recommended. Use AD936x Data Read
instead. The new AD936x Data Read
block includes the functionality from this block, but supports both SoC builder workflow and
IP core generation workflow. For more information about SoC workflows, see SoC Generation Workflows.

### R2024a: Dual channels support

The block now supports two receive channels. Use the **Channel mapping** parameter to indicate whether to use a single channel or dual channels.

## Description

Connect hardware logic to FMCOMMS Zynq radio receiver hardware

The Zynq and FMCOMMS2/3/4 Receiver Configuration block connects to the
FMCOMMS2/3/4 radio receiver hardware in your hardware logic. In simulation, this block
provides optional ports for center frequency and gain, which the SoC Builder tool
maps to hardware pins. The block does not connect to the radio hardware from
simulation.
