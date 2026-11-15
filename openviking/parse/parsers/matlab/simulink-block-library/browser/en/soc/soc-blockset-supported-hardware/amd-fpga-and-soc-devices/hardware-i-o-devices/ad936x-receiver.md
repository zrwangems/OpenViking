---
type: simulink-block
title: 'AD936x Receiver'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'ad936xreceiver'
documentation_source_path: 'ref/ad936xreceiver.html'
language: en
---

# AD936x Receiver

## Ports

### Input

### **data** — Simulation input data complex matrix

Input signal simulating the radio hardware, specified as a complex matrix. The
number of columns in the matrix depends on the number of channels in use, as specified
by the radio channel properties. Each column corresponds to a channel of complex data
received on one channel.

When you select the **Concatenated complex signal** parameter,
the datatype is represented as `uint32`, rather than
`int16` complex.

#### Dependencies

- To enable this simulation port, you must set **Simulation
  input** to `From input port`.

**Data Types:** `int16`
**Complex Number Support:** Yes

### **center frequency** — External RF center frequency nonnegative finite scalar

External RF center frequency, specified as a nonnegative finite scalar. The valid
center frequency range is from 70 MHz to 6 GHz.

#### Dependencies

To enable this port, set the **Simulation input** parameter to
`From connected IO`, and set the **Source of
gain** parameter to `Input port`.

**Data Types:** `double`

### **gain** — External gain numeric scalar | 1-by-2 numeric vector

External gain, specified as a numeric scalar or a 1-by-2 numeric vector. The valid
gain range is from –10 dB to 73 dB and depends on the center frequency. An
incompatible gain and center frequency combination returns an error from the radio
hardware. For the acceptable minimum and maximum gain values per center frequency,
check the manufacturer's specification.

Set the gain based on the radio channel configuration.

- For a single channel, specify the gain as a scalar.
- For two channels that use the same gain value, specify the gain as a scalar.
  The block applies the gain by scalar expansion.
- For two channels that use different gain values, specify the gain as a
  1-by-2 vector. The `i`th element of the vector is applied to
  the `i`th channel specified by the radio channel
  parameters.

#### Dependencies

To enable this port, set the **Simulation input** parameter to
`From connected IO`, and set the **Source of
gain** parameter to `Input port`.

**Data Types:** `double`
### Output

### **data** — Output signal complex matrix

Output signal received from the radio hardware, returned as a complex matrix. The
number of columns in the matrix depends on the number of channels in use, as specified
by the by radio channel properties. Each column corresponds to a channel of complex
data received on one channel.

This port supports complex values with these data types:

- 16-bit signed integers — Complex values are the raw 16-bit I and Q samples
  from the board. The 12-bit value from the ADC of the
  AD9361/AD9364
  RF chip is sign-extended to 16 bits.
- Single-precision floating point — Complex values are scaled to the range of
  [–1,
  1]. The block derives this value from the sign-extended 16
  bits received from the board.
- Double-precision floating point — Complex values are scaled to the range of
  [–1,
  1]. The block derives this value from the sign-extended 16
  bits received from the board.

To specify the data type, use the **Output data type**
parameter.

When you select the **Concatenated complex signal** parameter,
the data type is represented as `uint32`, rather than
`int16` complex

To qualify data reception, use the **data valid** port. The first
valid data frame can contain transient values, resulting in packets containing
undefined data.

**Data Types:** `int16` | `single` | `double`
**Complex Number Support:** Yes

### **valid** — Valid data indicator `1` | `0`

Valid data indicator, returned as one of these values:

- `1` indicates that the block has received data from the
  radio hardware.
- `0` indicates that the block has not received data from the
  radio hardware.

**Data Types:** `Boolean`

### **overflow** — Data discontinuity flag `1` | `0`

Data discontinuity flag, returned as one of these values:

- `1` indicates the presence of overflow resulting in
  noncontiguous data.
- `0` indicates no overflow.

You can use this port as a diagnostic tool to determine real-time
operation of the AD936x Receiver block. If your model is not running in real time,
increase the frame size to approach or achieve real-time performance. Alternatively,
you can decrease the baseband sampling rate.

#### Dependencies

To enable this port, on the **Main** tab, set
**Simulation input** to **From connected
IO**, and select the **Enable output port for overflow
indicator** parameter.

**Data Types:** `Boolean`

## Parameters

The AD936x Receiver block supports up to
two
channels to receive data from the AD936x-based Zynq radio hardware. Use the radio channel parameters to indicate whether to use a
single channel or
two
channels. For each channel in the output signal, **data**, you can set the
**Gain (dB)** parameter independently, or you can apply the same setting to
all channels. All other parameter values are applied to each channel in use.

### **Simulation input** — Simulation input source `Zeros` (default) | `From input port` | `From connected IO`

Select source for simulation input:

- `Zeros` — the output data from the block is a vector of zeros,
  type `int16` complex.
- `From input port` — this option adds an input port
  **data** to the block. Connect the port to a data source. The
  input data is passed-through to the output. The 12-bit value from the ADC of the
  AD9361 RF chip is sign-extended to 16 bits.
- `From connected IO` — Use this option to receive live input
  data from the board.

### Main

### **Enable Channel 1** — Use Channel 1 on (default) | off

Select this option to enable data reception on channel 1.

### **Enable Channel 2** — Use Channel 2 off (default) | on

Select this option to enable data reception on channel 2.

The RF chip of the radio hardware determines the number of channels you can use
for receiving data.

| Supported Radio Hardware | RF Chip | Number of Channels | Supported RF Ports |
| --- | --- | --- | --- |
| ADI RF SOM  ZC706 and FMCOMMS2 or FMCOMMS3  ZedBoard and FMCOMMS2 or FMCOMMS3  ZCU102 and FMCOMMS2 or FMCOMMS3 | AD9361 | 2 | TX1A, RX1A, TX2A, RX2A |
| ZC706 and FMCOMMS4  ZedBoard and FMCOMMS4  ZCU102 and FMCOMMS4 | AD9364 | 1 | TXA, RXA |

### **Radio IP address** — IP address of radio hardware `192.168.3.2` (default) | dotted-quad expression

IP address of the radio hardware, specified as a dotted-quad expression.

This parameter must match the physical IP address of the radio hardware assigned
during hardware setup. For more information, see Set Up AMD FPGA and SoC Devices. If you configure the
radio hardware with an IP address other than the default, update **Radio IP
address** accordingly.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

### **Info** — SDR Radio information button

Click this button to check connectivity between the block and the radio hardware,
and to synchronize radio settings between them.

When you set block parameter values, the AD936x Receiver block first checks that
the values have the correct data types. If the values pass those checks, the values
can still be out of range for the radio hardware. In that case, the radio hardware
sets the actual value as close to the specified value as possible. When you next
synchronize the block with the radio hardware by clicking **Info**, a dialog box displays the actual values.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

### **Source of center frequency** — Source of center frequency `Dialog` (default) | `Input port`

Source of center frequency, specified as one of these options:

- `Dialog` — Set the center frequency by using the
  **Center frequency (Hz)** parameter.
- `Input port` — Set the center frequency by using
  the **center frequency** input port.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

### **Center frequency (Hz)** — RF center frequency in Hz `2.4e9` (default) | nonnegative scalar

RF center frequency in Hz, specified as a nonnegative scalar. The valid range for
center frequency is 70 MHz to 6 GHz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`, and set the **Source of
center frequency** parameter to `Dialog`.

**Data Types:** `double`

### **Source of gain** — Source of gain `AGC Slow Attack` (default) | `AGC Fast Attack` | `Dialog` | `Input port`

Source of gain, specified as one of these values:

- `AGC Slow Attack` — For signals with slowly
  changing power levels.
- `AGC Fast Attack` — For signals with rapidly
  changing power levels.
- `Dialog` — Specify the gain by using the
  **Gain (dB)** parameter.
- `Input port` — Specify the gain by using the
  **gain** input port.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

### **Gain (dB)** — Gain `10` (default) | numeric scalar | 1-by-2 numeric vector

Gain in dB, specified as a numeric scalar or a 1-by-2 numeric vector. The valid
gain range is from –10 dB to 73 dB and depends on the center frequency. An
incompatible gain and center frequency combination returns an error from the radio
hardware. For the acceptable minimum and maximum gain values per center frequency,
check the manufacturer's specification.

Set the gain value based on the radio properties configuration.

- For a single channel, specify the gain as a scalar.
- For two channels that use the same gain value, specify the gain as a scalar.
  The block applies the gain by scalar expansion.
- For two channels that use different gain values, specify the gain as a 1-by-2
  vector. The *i*th element of the vector is applied to the
  *i*th channel specified by the radio properties.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`, and set the **Source of
gain** parameter to `Dialog`.

**Data Types:** `double`

### **Baseband sample rate (Hz)** — Baseband sampling rate in Hz `1e6` (default) | positive scalar

Baseband sampling rate in Hz, specified as a positive scalar. The valid range of
this parameter is 520.834 kHz to 61.44 MHz.

**Note**

To synchronize the block with the radio hardware, on the
**Menu** tab, click **Info**. If the specified
and actual rates have a small mismatch, verify that the computed rate is close to
the value you actually want.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

**Data Types:** `double`

### **Output data type** — Complex data type on data port `int16` (default) | `single` | `double`

Select output data type, as one of these options:

- `int16` — Integer values are the raw
  16-bit I and Q samples from the board. The 12-bit value from the ADC of the
  AD9361/AD9364
  RF chip is sign-extended to 16 bits.
- `single` — Single-precision floating point
  values are scaled to the range of
  [–1,
  1]. The block derives this value from the sign-extended 16
  bits received from the board.
- `double` — Double-precision floating point
  values are scaled to the range of
  [–1,
  1]. The block derives this value from the sign-extended 16
  bits received from the board.

### **Samples per frame** — Number of samples per frame `2000` (default) | positive integer

Number of samples per frame, specified as a positive integer. In single-channel
mode, the number of samples per frame must be even. When streaming to the host, using
large frame sizes can give more efficient performance. To determine real-time
operation of the object, use the **overflow** output port.

To capture an even number of samples per frame with an odd number of samples per
frame, enable burst mode .

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO` or
`Zeros`.

### **Enable output port for overflow indicator** — Enable overflow control signal `on` (default) | `off`

Select this parameter to enable the **overflow** output port
during host-radio hardware data transfers.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

### **Enable burst mode** — Enable burst mode `off` (default) | `on`

When you select this parameter, the block produces a set of contiguous frames.
This setting can help simulate models that cannot run in real time. When you enable
burst mode, specify the amount of contiguous data by using the **Frames in
burst** parameter. For more information on how to use this parameter, see
Burst Mode.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO`.

### **Frames in burst** — Number of frames in a contiguous burst `1` (default) | positive integer

Number of frames in a contiguous burst, specified as a positive integer.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `From connected IO` and select the **Enable
burst mode** parameter.

**Data Types:** `double`

### **Concatenated complex signal** — Concatenate complex signal off (default) | on

Select this option when the input and output signal are represented as
`unit32` instead of a complex number with `int16`
for real and `int16` for imaginary.

#### Dependencies

To enable this parameter, set the **Output data type**
parameter to `int16` complex. It is grayed out for other
options.

### **Sample time** — Sample time of the block `0.02` (default) | positive scalar

Sample time of the block, specified as a positive scalar. The default value
corresponds to **Samples per frame** divided by **Baseband
sample rate (Hz)**.

#### Dependencies

To enable this parameter, set the **Simulation input**
parameter to `Zeros`.

When the **Simulation input** parameter to `From
connected IO`, this parameter is visible in the
**Advanced** tab.

**Data Types:** `double`

### Filter

The parameters in this tab are only visible when **Simulation input**
is set to `From connected IO`.

### **Use custom filter** — Enable custom filter `off` (default) | `on`

When you select this parameter, the filter chain uses a custom filter design instead
of the default filter design. For example, if the gain or bandwidth characteristics of
the default filter does not satisfy the requirements for your application, you can
design a custom filter that meets your specific requirements. If the AD936x Receiver block
does not have a custom filter design applied yet, click on **Launch filter
wizard** to open the ADI filter wizard. The wizard enables you to design a
custom filter for the Analog Devices
AD9361/AD9364
RF chip based on the **Baseband sample rate (Hz)** parameter. You can
adjust and optimize the settings for calculating the analog filters, interpolation and
decimation filters, and FIR coefficients. When you finish with the wizard, to apply the
custom filter design to the block, click **Apply** on the block mask.

**Note**

When applying a custom filter to the AD936x Receiver block by using the ADI filter
wizard, **Use custom filter** is automatically selected. To
switch between the default and your custom filter design, clear or select
**Use custom filter**, respectively. Then click
**Apply** on the block mask.

For more information, see Baseband Sampling Rate and Filter Chains.

### Advanced

The parameters in this tab are only visible when **Simulation input**
is set to `From connected IO`.

### **Bypass user logic** — Enable bypassing user logic `off` (default) | `on`

Select this parameter to enable the radio hardware data path to bypass the algorithm generated
and programmed during FPGA targeting or hardware-software co-design. For more
information, see FPGA Targeting Workflow and Hardware-Software Co-Design Workflow.

### **Enable quadrature correction** — Quadrature correction `on` (default) | `off`

When you select this parameter, the block applies in-phase and quadrature (IQ) imbalance compensation.

### **Enable RF DC correction** — RF DC correction `on` (default) | `off`

When you select this parameter, the block applies an RF direct current (DC) blocking filter.

### **Enable baseband DC correction** — Baseband DC correction `on` (default) | `off`

When you select this parameter, the block applies a baseband DC blocking filter.

### **Override automatic sample time** — Change sample time of the block `off` (default) | `on`

When you select this parameter, you can change the sample time of the block, by using the
**Sample time** parameter. For more information, see SDR Receiver Sample Times.

### **Sample time** — Sample time of the block `0.02` (default) | positive scalar

Sample time of the block, specified as a positive scalar. The default value corresponds to
**Samples per frame** divided by **Baseband sample rate
(Hz)**. Consider changing the default value only when deploying a
hardware-software co-design implementation.

#### Dependencies

To enable this parameter, select the **Override automatic sample
time** parameter.

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

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ADI RF SOM SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute on an SoC device, use
the SoC Builder tool or
IP Core Generation (HDL Coder) workflow.

## Version History

**Introduced in R2024b**

## Description

Receive data from AD936x-based Zynq radio hardware

The AD936x Receiver block receives data from an AD936x-based Zynq® radio hardware.

You can use the AD936x Receiver block to simulate and develop various software-defined radio
(SDR) applications. This diagram shows the conceptual overview of receiving radio signals in
Simulink® using the SoC Blockset™ Support Package for AMD FPGA and SoC Devices. Simulink interacts with the AD936x Receiver block to receive signals from the radio
hardware.

Block diagram showing the flow from an antenna, to a Zynq board, to an AD936c Receiver block, and then to an FPGA design block
