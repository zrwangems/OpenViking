---
type: simulink-block
title: 'FMCOMMS5 Transmitter'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Radio Applications / Radio Configuration'
documentation_page: 'fmcomms5transmitter'
documentation_source_path: 'ref/fmcomms5transmitter.html'
language: en
---

# FMCOMMS5 Transmitter

## Ports

### Input

### **data** — Input signal complex matrix

Input signal sent to the radio hardware, specified as a complex matrix. The number
of columns in the matrix depends on the number of channels in use, as specified by the
**Channel mapping**  parameter. Each column corresponds to a
channel of complex data sent via one channel. In single-channel mode, the number of
elements in a column must be even.

This port supports complex values with these data types:

- 16-bit signed integers — Since the
  AD9361
  RF chip has a 12-bit DAC, only the 12 most significant bits of the I and Q
  samples are used.
- Single-precision floating point — Complex values in the range of [–1, 1].
  Since the AD9361 RF chip has a 12-bit DAC, numbers of magnitude less than 0.0625
  are lost.
- Double-precision floating point — Complex values in the range of [–1, 1].
  Since the AD9361 RF chip has a 12-bit DAC, numbers of magnitude less than 0.0625
  are lost.

To determine whether data has been transmitted successfully, enable the
**underflow** port.

#### Dependencies

To enable this port, set the **Data source select** parameter
to `Input port`.

**Data Types:** `int16` | `single` | `double`
**Complex Number Support:** Yes

### **center frequency** — External RF center frequency nonnegative finite scalar

External RF center frequency, specified as a nonnegative finite scalar. The valid
center frequency range is from 70 MHz to 6 GHz.

#### Dependencies

To enable this port, set the **Source of center frequency**
parameter to `Input port`.

**Data Types:** `double`

### **gain** — External gain source numeric scalar | 1-by-2 or 1-by-4 numeric vector

External gain source, specified as a numeric scalar, or a 1-by-2 or 1-by-4 numeric
vector. The valid gain range is –89.75 dB to 0 dB. The resolution is 0.25 dB.

Set the gain based on the **Channel mapping** parameter configuration.

- For a single channel, specify the gain as a scalar.
- For two or four channels that use the same gain value, specify the gain as a
  scalar. The block applies the gain by scalar expansion.
- For two or four channels that use different gain values, specify the gain as
  a 1-by-2 or
  1-by-4
  vector, respectively. The `i`th element of
  the vector is applied to the `i`th channel specified by the
  **Channel mapping** parameter.

#### Dependencies

To enable this port, set the **Source of gain** parameter to
`Input port`.

**Data Types:** `double`
### Output

### **underflow** — Data discontinuity flag `1` | `0`

Data discontinuity flag, returned as one of these values:

- `1` indicates the presence of underflow resulting in
  noncontiguous data.
- `0` indicates no underflow.

You can use this value as a diagnostic tool to determine real-time
operation of the FMCOMMS5 Transmitter block. If your model is not running in real time,
increase the frame size to approach or achieve real-time performance. Alternatively,
you can decrease the baseband sampling rate.

**Note**

Running the block for the first time initializes the radio. Because this initialization can result in an underflow, ignore the **underflow** output port value of the first run.

#### Dependencies

To enable this port, on the **Main** tab, select the
**Enable output port for underflow indicator** parameter.

**Data Types:** `Boolean`

## Parameters

The
FMCOMMS5 Transmitter block supports up to
four
channels to send data to the FMCOMMS5 Zynq radio hardware. Use the **Channel mapping**  parameter to
indicate whether to use a single channel or
multiple
channels. For each channel in the input signal, **data**, you can set the
**Gain (dB)** parameter independently, or you can apply the same setting to
all channels. If you select direct digital synthesis (DDS) transmission for the **Data
source select** parameter, you can also set all DDS-based parameters independently.
All other parameter values are applied to each channel in use.

To check connectivity between the block and the radio hardware, and to
synchronize radio settings between them, on the
**Main** tab, click
**Info**.

When you set block parameter values, the FMCOMMS5 Transmitter block first checks that
the values have the correct data types. If the values pass those
checks, the values can still be out of range for the radio hardware.
In that case, the radio hardware sets the actual value as close to
the specified value as possible. When you next synchronize the block
with the radio hardware by clicking **Info**, a
dialog box displays the actual values.

If a parameter is listed as tunable, then you can change its value during
simulation.

#### Main Tab

### **Radio IP address** — IP address of radio hardware `192.168.3.2` (default) | dotted-quad expression

IP address of the radio hardware, specified as a dotted-quad expression.

This parameter must match the physical IP address of the radio hardware assigned
during hardware setup. For more information, see Set Up AMD FPGA and SoC Devices. If you configure the radio hardware with an IP address
other than the default, update **Radio IP address** accordingly.

### **Source of center frequency** — Source of center frequency `Dialog` (default) | `Input port`

Source of center frequency, specified as one of these options:

- `Dialog` — Set the center frequency by using the
  **Center frequency (Hz)** parameter.
- `Input port` — Set the center frequency by using
  the **center frequency** input port.

### **Center frequency (Hz)** — RF center frequency in Hz `2.4e9` (default) | nonnegative scalar

RF center frequency in Hz, specified as a nonnegative scalar. The valid range for
center frequency is 70 MHz to 6 GHz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Source of center frequency**
parameter to `Dialog`.

**Data Types:** `double`

### **Source of gain** — Choose source of gain `Dialog` (default) | `Input port`

- `Dialog` —
  Specify the gain by using the **Gain
  (dB)** parameter.
- `Input port`
  — Specify the gain by using the
  **gain** input port.

### **Gain (dB)** — Gain `-10` (default) | numeric scalar | 1-by-2 or 1-by-4 numeric vector

Gain in dB, specified as a numeric scalar, or a 1-by-2 or
1-by-4
numeric vector. The valid gain range is –89.75 dB to 0 dB. The
resolution is 0.25 dB.

Set the gain based on the **Channel mapping** parameter
configuration.

- For a single channel, specify the gain as a scalar.
- For two or four channels that use the same gain value, specify the gain as a
  scalar. The block applies the gain by scalar expansion.
- For two or four channels that use different gain values, specify the gain as a
  1-by-2 or 1-by-4
  vector, respectively. The `i`th element of the
  vector is applied to the `i`th channel specified by the
  **Channel mapping** parameter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Source of gain** parameter to
`Dialog`.

**Data Types:** `double`

### **Channel mapping** — Channel input mapping `1` (default) | integer | `[N M]` | `[1 2 3 4]`

Channel input mapping, specified as one of these values:

- Integer from 1 to 4 — The integer value indicates which single channel
  is in use.
- `[N
  M]`, where *N* and
  *M* are distinct integers from 1 to 4 — Channels
  *N* and *M* are in use.
- `[1 2 3 4]` — All four channels are in use.

The RF chip of the radio hardware determines the number of channels you can use for
sending data. For the FMCOMMS5, two AD9361 RF chips are used to provide support for four
channels. The channels specified by 1 and 2 are situated on the first AD9361 chip. The
channels specified by 3 and 4 are situated on the second AD9361 chip. Using multiple
channels across the two chips has certain limitations. For more information, see Multiple Channel Synchronization for FMCOMMS5.

| Supported Radio Hardware | RF Chip | Number of Channels | Supported RF Ports |
| --- | --- | --- | --- |
| ZC706 and FMCOMMS5 | 2 x AD9361 | 4 | - For AD9361 Chip A: TX1A\_A, RX1A\_A, TX2A\_A, RX2A\_A - For AD9361 Chip B: TX1A\_B, RX1A\_B, TX2A\_B, RX2A\_B |

### **Baseband sample rate (Hz)** — Baseband sampling rate in Hz `1e6` (default) | positive scalar

Baseband sampling rate in Hz, specified as a positive scalar. The valid range of this
parameter is 520.834 kHz to 61.44 MHz.

**Note**

To synchronize the block with the radio hardware, on the **Menu** tab,
click **Info**. If the specified and actual rates have a small mismatch,
verify that the computed rate is close to the value you actually want.

**Data Types:** `double`

### **Enable output port for underflow indicator** — Enable underflow control signal `on` (default) | `off`

Select this parameter to enable the **underflow** output port during
host-radio hardware data transfers.

#### Filter Tab

### **Use custom filter** — Enable custom filter `off` (default) | `on`

When you select this parameter, the filter chain uses a custom filter design instead of the
default filter design. For example, if the gain or bandwidth characteristics of the
default filter does not satisfy the requirements for your application, you can design a
custom filter that meets your specific requirements. If the FMCOMMS5 Transmitter block does not
have a custom filter design applied yet, click on **Launch filter
wizard** to open the ADI filter wizard. The wizard enables you to design a
custom filter for the Analog Devices
AD9361
RF chips based on the **Baseband sample rate (Hz)** parameter. You can
adjust and optimize the settings for calculating the analog filters, interpolation and
decimation filters, and FIR coefficients. When you finish with the wizard, to apply the
custom filter design to the block, click **Apply** on the block mask.
The setting is applied to each channel in use across both AD9361 chips.

**Note**

When applying a custom filter to the FMCOMMS5 Transmitter block by using the ADI filter
wizard, **Use custom filter** is automatically selected. To
switch between the default and your custom filter design, clear or select
**Use custom filter**, respectively. Then click
**Apply** on the block mask.

For more information, see Baseband Sampling Rate and Filter Chains.

#### Advanced Tab

### **Bypass user logic** — Enable bypassing user logic `off` (default) | `on`

Select this parameter to enable the radio hardware data path to bypass the algorithm generated
and programmed during FPGA targeting or hardware-software co-design. For more
information, see FPGA Targeting Workflow and Hardware-Software Co-Design Workflow.

### **Data source select** — Source of data `Input Port` (default) | `DDS`

Source of data, specified as one of these values:

- `Input Port` — This selection enables the
  **data** input port.
- `DDS` — This selection enables DDS transmission.
  The block uses two additive tones for each channel. To set the tone
  frequency and tone scale of these tones, use the **Tone 1 Frequency
  (Hz)**, **Tone 2 Frequency (Hz)**,
  **Tone 1 Scale [0-1]**, and **Tone 2 Scale
  [0-1]** parameters. The DDS signals are generated on the
  FPGA.

### **Tone 1 Frequency (Hz)** — First DDS tone frequency in Hz `5000` (default) | numeric scalar | 1-by-2 or 1-by-4 numeric vector

First DDS tone frequency in Hz, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  frequency for all channels in use. The object applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 or 1-by-4 numeric vector — Use this option to specify different
  frequencies for two or four channels, respectively. The `i`th
  element of the vector is applied to the `i`th channel specified
  by the **Channel mapping** parameter.

The valid range of **Tone 1 Frequency (Hz)** is from 0
to **Baseband sample rate (Hz)** / 2.

#### Dependencies

To enable this parameter, set the **Data source select**
parameter to `DDS`.

**Data Types:** `double`

### **Tone 2 Frequency (Hz)** — Second DDS tone frequency in Hz `10000` (default) | numeric scalar | 1-by-2 or 1-by-4 numeric vector

Second DDS tone frequency in Hz, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  frequency for
  all
  channels in use. The object applies scalar expansion for each channel specified by
  the **Channel mapping** parameter.
- 1-by-2 or
  1-by-4 numeric vector — Use this option to specify different
  frequencies for two
  or four
  channels, respectively. The `i`th element of
  the vector is applied to the `i`th channel specified by the
  **Channel mapping** parameter.

The valid range of **Tone 2 Frequency (Hz)** is from 0
to **Baseband sample rate (Hz)** / 2.

#### Dependencies

To enable this parameter, set the **Data source select**
parameter to `DDS`.

**Data Types:** `double`

### **Tone 1 Scale [0-1]** — First DDS tone scale `0.5` (default) | numeric scalar | 1-by-2 or 1-by-4 numeric vector

First DDS tone scale in millionths of full scale, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  scale for all channels in use. The object applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 or 1-by-4 numeric vector — Use this option to specify different scales
  for two or four channels, respectively. The `i`th element of the
  vector is applied to the `i`th channel specified by the
  **Channel mapping** parameter.

The valid range of **Tone 1 Scale [0-1]** is from 0 to
1.

#### Dependencies

To enable this parameter, set the **Data source select**
parameter to `DDS`.

**Data Types:** `double`

### **Tone 2 Scale [0-1]** — Second DDS tone scale `0.25` (default) | numeric scalar | 1-by-2 or 1-by-4 numeric vector

Second DDS tone scale in millionths of full scale, specified as one of these options:

- Numeric scalar — Use this option for a single channel or to specify the same
  scale for all channels in use. The object applies scalar expansion for each
  channel specified by the **Channel mapping** parameter.
- 1-by-2 or 1-by-4 numeric vector — Use this option to specify different scales
  for two or four channels, respectively. The `i`th element of the
  vector is applied to the `i`th channel specified by the
  **Channel mapping** parameter.

The valid range of **Tone 2 Scale [0-1]** is from 0 to
1.

#### Dependencies

To enable this parameter, set the **Data source select**
parameter to `DDS`.

**Data Types:** `double`

### **Data timeout (sec)** — Timeout for I/O operations in seconds `Inf` (default) | nonnegative scalar

Timeout for I/O operations in seconds, specified as one of these options:

- `Inf` — The block waits indefinitely to complete I/O
  operations.
- Nonnegative scalar, *N* — The block waits
  *N* seconds to complete I/O operations. Zero seconds
  corresponds to a non-blocking setup.

**Data Types:** `double`

### **Loopback** — Built-in self-test (BIST) loopback mode `Disabled` (default) | `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

Built-in self-test loopback mode, specified as one of these options:

- `Disabled` — Disable BIST loopback.
- `Digital Tx -> Digital Rx` — Enable digital
  signals to loop back within the device. The signals bypass the RF
  stage.
- `RF Rx -> RF Tx` — Enable incoming receiver RF
  signals to loop back to the RF transmitter port. The signals bypass the
  FPGA.

### **Test signal injection** — BIST signal injection mode `Disabled` (default) | `Tone Inject Tx` | `Tone Inject Rx`

BIST signal injection mode, specified as one of these values:

- `Disabled` — Disable BIST signal
  injection.
- `Tone Inject Tx` — Enable BIST signal injection
  to transmit path.
- `Tone Inject Rx` — Enable BIST signal injection
  to receive path.

When you enable BIST signal injection, you can set the source of BIST
signal generation with the **Signal generator mode** parameter.

### **Signal generator mode** — Source of BIST signal generation `PRBS` (default) | `Tone`

Source of BIST signal generation, specified as one of these options:

- `PRBS` — Use the pseudo random binary sequence
  (PRBS) generator of the board.
- `Tone` — Use the tone generator of the board. To
  set the tone frequency and tone level, use the **Tone frequency
  (Hz)** and **Tone level (dB)** parameters,
  respectively.

#### Dependencies

To enable this parameter, set the **Test signal injection**
parameter to `Tone Inject Tx` or `Tone Inject
Rx`.

### **Tone frequency (Hz)** — BIST tone frequency `Fs/32` (default) | `Fs/16` | `Fs*3/32` | `Fs/8`

BIST tone frequency, specified as
`Fs/32`, `Fs/16`,
`Fs*3/32`, or `Fs/8`.

#### Dependencies

To enable this parameter, set the
**Signal generator mode** parameter to
`Tone`.

### **Tone level (dB)** — BIST tone level `0` (default) | `-6` | `-12` | `-18`

BIST tone level, specified as `0`,
`-6`, `-12`, or
`-18`.

#### Dependencies

To enable this parameter, set the
**Signal generator mode** parameter to
`Tone`.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Send data to FMCOMMS5 Zynq radio hardware

The FMCOMMS5 Transmitter block sends data to an FMCOMMS5 Zynq® radio hardware. The block supports the Xilinx® ZC706 radio hardware with Analog Devices® FMCOMMS5 RF card.

You can use the FMCOMMS5 Transmitter block to simulate and develop various software-defined radio
(SDR) applications. This diagram shows the conceptual overview of transmitting and receiving
radio signals in Simulink® using the SoC Blockset™ Support Package for AMD FPGA and SoC Devices. Simulink interacts with the FMCOMMS5 Transmitter block to send data to the radio hardware.

For transmitting a radio signal over the air, pass the signal generated in Simulink to a transmitter block. The transmitter block forwards the signal to the radio hardware. For receiving a radio signal over the air, use a receiver block. The receiver block forwards the signal received from the radio hardware for post processing in Simulink.
