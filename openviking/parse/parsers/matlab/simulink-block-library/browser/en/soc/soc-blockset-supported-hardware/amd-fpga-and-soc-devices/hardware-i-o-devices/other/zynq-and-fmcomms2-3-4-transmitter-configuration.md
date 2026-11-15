---
type: simulink-block
title: 'Zynq and FMCOMMS2/3/4 Transmitter Configuration'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices / Other'
documentation_page: 'zynqandfmcomms234transmitterconfiguration'
documentation_source_path: 'ref/zynqandfmcomms234transmitterconfiguration.html'
language: en
---

# Zynq and FMCOMMS2/3/4 Transmitter Configuration

## Ports

### Input

### **center frequency** — External RF center frequency nonnegative finite scalar

External RF center frequency, specified as a nonnegative finite scalar. The valid
center frequency range is from 70 MHz to 6 GHz.

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

The Zynq and FMCOMMS2/3/4 Transmitter Configuration block supports up to two channels to send data. Use the **Channel
mapping**  parameter to indicate whether to use a single channel or dual channels.
For each channel, you can set the **Gain (dB)** parameter independently, or
you can apply the same setting to all channels. If you select direct digital synthesis (DDS)
transmission for the **Data source select** parameter, you can also set all
DDS-based parameters independently. All other parameter values are applied to each channel in
use.

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

### **Source of gain** — Source of gain `Dialog` (default) | `Input Port`

Source of gain, specified as one of these options:

- `Dialog` — Specify the gain by using the
  **Gain (dB)** parameter.
- `Input Port` — Specify the gain by using the
  **gain** input port.

### **Gain (dB)** — Gain `-10` (default) | numeric scalar | 1-by-2 numeric vector

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

### **Channel mapping** — Channel input mapping `1` (default) | `2` | `[1 2]`

Channel input mapping, specified as one of these values:

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

### **Data source select** — Source of data `Input Port` (default) | `DDS`

Source of data, specified as one of these options:

- `Input Port` — Enable the **data**
  input port.
- `DDS` — Enable the DDS on the radio hardware to
  generate transmission data. The block uses two additive tones for each channel.
  To set the frequency and scale of the tones, use the **Tone 1 Frequency
  (Hz)**, **Tone 2 Frequency (Hz)**, **Tone 1
  Scale [0-1]**, and **Tone 2 Scale [0-1]**
  parameters. The DDS signals are generated on the FPGA.

### **Tone 1 Frequency (Hz)** — First DDS tone frequency `5000` (default) | numeric scalar | 1-by-2 numeric vector

First DDS tone frequency, in Hz, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  frequency for all channels in use. The block applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 numeric vector — Use this option to specify different frequencies for
  two channels. The `i`th element of the vector is applied to the
  `i`th channel specified by the **Channel
  mapping** parameter.

The valid range of **Tone 1 Frequency (Hz)** is from 0
to **Baseband sample rate (Hz)** / 2.

#### Dependencies

To enable this parameter, set **Data source select** to
`DDS`.

**Data Types:** `double`

### **Tone 2 Frequency (Hz)** — Second DDS tone frequency `10000` (default) | numeric scalar | 1-by-2 numeric vector

Second DDS tone frequency, in Hz, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  frequency for all channels in use. The block applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 numeric vector — Use this option to specify different frequencies for
  two channels. The `i`th element of the vector is applied to the
  `i`th channel specified by the **Channel
  mapping** parameter.

The valid range of **Tone 2 Frequency (Hz)** is from 0
to **Baseband sample rate (Hz)** / 2.

#### Dependencies

To enable this parameter, set **Data source select** to
`DDS`.

**Data Types:** `double`

### **Tone 1 Scale [0-1]** — First DDS tone scale `0.5` (default) | numeric scalar | 1-by-2 numeric vector

First DDS tone scale in millionths of full scale, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  scale for all channels in use. The block applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 numeric vector — Use this option to specify different scales for two
  channels. The `i`th element of the vector is applied to the
  `i`th channel specified by the **Channel
  mapping** parameter.

The valid range of **Tone 1 Scale [0-1]** is from 0 to
1.

#### Dependencies

To enable this parameter, set **Data source select** to
`DDS`.

**Data Types:** `double`

### **Tone 2 Scale [0-1]** — Second DDS tone scale `0.25` (default) | numeric scalar | 1-by-2 numeric vector

Second DDS tone scale in millionths of full scale, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  scale for all channels in use. The block applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 numeric vector — Use this option to specify different scales for two
  channels. The `i`th element of the vector is applied to the
  `i`th channel specified by the **Channel
  mapping** parameter.

The valid range of **Tone 2 Scale [0-1]** is from 0 to
1.

#### Dependencies

To enable this parameter, set **Data source select** to
`DDS`.

**Data Types:** `double`

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

Use of this block is not recommended. Use AD936x Data Write
instead. The new AD936x Data Write
block includes the functionality from this block, but supports both SoC builder workflow and
IP core generation workflow. For more information about SoC workflows, see SoC Generation Workflows.

### R2024a: Dual channels support

The block now supports two transmit channels. Use the **Channel mapping** parameter to indicate whether to use a single channel or dual channels.

## Description

Connect hardware logic to FMCOMMS Zynq radio transmitter hardware

The Zynq and FMCOMMS2/3/4 Transmitter Configuration block connects your
hardware logic to the FMCOMMS2/3/4 radio transmitter hardware. In simulation, this block
provides optional ports for center frequency and gain, which the SoC Builder tool
maps to hardware pins. The block does not connect to the radio hardware from
simulation.
