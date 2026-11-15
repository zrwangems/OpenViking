---
type: simulink-block
title: 'NR Polar Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'nrpolardecoder'
documentation_source_path: 'ref/nrpolardecoder.html'
language: en
---

# NR Polar Decoder

## Ports

### Input

### **data** — Input sample scalar

Input sample, specified as a scalar log-likelihood ratio (LLR). The block supports
builtin types, and signed fixed-point values with a wordlength of 4 to 16 bits.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `fixed point` | `int8` | `int16` | `double` | `single`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate the
boundaries of the frame and the validity of the samples.

- `start` — Indicates the start of the input frame
- `end` — Indicates the end of the input frame
- `valid` — Indicates that the data on the input
  **data** port is valid

For more details, see Sample Control Bus.

**Data Types:** `bus`

### **K** — Length of information block in bits positive integer

Length of information block in bits, specified as a positive integer. For downlink
messages, **K** must be in the range 36 to 164. For uplink messages,
**K** must be in the range 18 to 25 or 31 to 1023.

#### Dependencies

To enable this port, set the **Configuration source** parameter
to `Input port`.

**Data Types:** `fixdt(0,10,0)`

### **E** — Rate-matched output length in bits scalar positive integer

Rate-matched output length in bits, specified as a scalar positive integer.
Specify a value for **E** that is greater than **K**
and less than or equal to 8192.

#### Dependencies

To enable this port, set the **Configuration source** parameter
to `Input port`.

**Data Types:** `fixdt(0,14,0)`

### **RNTI** — Target RNTI 16-bit unsigned integer

Target RNTI, specified as a 16-bit unsigned integer. This value increases decoding
accuracy for DCI messages. For example, when decoding SIB1 DCI messages, enable this
port and set the target RNTI to 65,535. For MIB decoding, you can disable this port or
set the target RNTI to 0.

#### Dependencies

To enable this port, set **Link direction** to
`Downlink` and select the **Enable target RNTI
port** parameter.

**Data Types:** `uint16`
### Output

### **data** — Decoded data bit scalar

Decoded data bit, returned as a scalar. The output message length is
*A* bits, where `A =
K – CRCLen`. For downlink messages,
*CRCLen* is 24. For uplink messages, *CRCLen* is
11 or 6, as defined by the 5G NR standard.

**Data Types:** `fixdt(0,1,0)` | `Boolean` | `double` | `single`
**Complex Number Support:** Yes

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, returned as a `samplecontrol`
bus. The bus includes the `start`, `end`, and
`valid` control signals, which indicate the boundaries of the frame
and the validity of the samples.

- `start` — Indicates the start of the output
  frame
- `end` — Indicates the end of the output frame
- `valid` — Indicates that the data on the output
  **data** port is valid

For more details, see Sample Control Bus.

**Data Types:** `bus`

### **err** — CRC result scalar

CRC result, returned as a scalar. If you clear the **Full checksum
mismatch** parameter, this value is a Boolean. When you select the
**Full checksum mismatch** parameter, this value is a
`ufix24` scalar for downlink messages and a
`ufix11` or `ufix6` scalar for uplink messages.

If you enable the **RNTI** port, the block compares the internal
CRC checksum against the target RNTI value. Otherwise, the block compares the CRC
checksum against a value of 0.

**Data Types:** `Boolean` | `ufix11` | `ufix24`

### **nextFrame** — Ready for new inputs scalar

The block sets this signal to `1` when the block is ready to accept the start
of the next frame. If the block receives an input **start** signal
while **nextFrame** is `0`, the block discards the
frame in progress and begins processing the new data.

For more information, see Using the nextFrame Output Signal.

**Data Types:** `Boolean`

## Parameters

### **Link direction** — Direction of 5G NR link `Downlink` (default) | `Uplink`

Direction of 5G NR link, specified as `Downlink` or
`Uplink`. When you choose
`Downlink`, the block performs deinterleaving, as specified in
the 5G NR standard. When you select `Uplink`, the block omits
the deinterleaving logic.

Downlink decoding uses a CRC length of 24 bits. Uplink decoding uses a CRC length of
6 bits (**K** in the range 18 to 25) or 11 bits (**K**
in the range 31 to 1023).

### **List length** — Number of decoding paths `2` (default) | `4` | `8`

This parameter is the maximum number of parallel paths maintained in the decoding
tree. Increasing the list length increases the error correction performance but uses
more hardware resources and increases the decoding latency. When you use list lengths of
`4` and `8`, the latency can vary
depending on the SNR of the input signal, and is not constant for given values of
**K** and **E**. Use the
**nextFrame**  output signal to determine when the block
is available for a new message.

### **Configuration source** — Source for K and E `Property` (default) | `Input port`

Select `Input port` to enable the **K**
and **E** ports. Select `Property` to use the
**Message length (K)** and **Rate-matched length
(E)** parameters.

### **Message length (K)** — Length of information block in bits `56` (default) | positive integer

For downlink messages, **K** must be in the range 36 to 164. For
uplink messages, **K** must be in the range 18 to 25 or 31 to
1023.

#### Dependencies

To enable this parameter, set the **Configuration source**
parameter to `Property`.

### **Rate-matched length (E)** — Rate-matched output length in bits `864` (default) | positive integer

Specify a value for **E** that is greater than
**K** and less than or equal to 8192.

#### Dependencies

To enable this parameter, set the **Configuration source**
parameter to `Property`.

### **Full checksum mismatch** — Return checksum from final decoding stage `off` (default) | `on`

When you clear this parameter, the block returns a Boolean scalar on the
**err** port that indicates whether the CRC was successful. When you
select this parameter, the block returns the full CRC checksum on the
**err** port. If your design decodes DCI messages and makes use of
the RNTI remainder, select this parameter.

If you enable the **RNTI** port, the block compares the internal
CRC checksum with the target RNTI value. Otherwise, the block compares the CRC checksum
against a value of 0.

The `nrPolarDecode` (5G Toolbox) function
returns a decoded message that includes the CRC bits. This block returns the decoded
message without the CRC bits, and returns the CRC status separately on the
**err** port. This behavior is equivalent to calling the `nrCRCDecode` (5G Toolbox) function after
using the `nrPolarDecode` function. Not recomputing the CRC bits
saves hardware latency and resources.

### **Enable target RNTI port** — Optional port to specify target RNTI value `off` (default) | `on`

Select this parameter to enable the **RNTI** input port. Providing
a target RNTI value increases decoding accuracy for DCI messages. For example, when
decoding SIB1 DCI messages, enable this port and set the target RNTI to 65535. For MIB
decoding, you can disable this port or set the target RNTI to 0.

Enabling this port also changes how the block computes the **err**
output port value. If you enable the **RNTI** port, the block compares
the internal CRC checksum with the target RNTI value. Otherwise, the block compares the
CRC checksum against a value of 0.

#### Dependencies

To enable this parameter, set the **Link direction** parameter to
`Downlink`.

## Libraries

Wireless HDL Toolbox / Error Detection and Correction

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2020a**

## Description

Perform polar decoding according to 5G NR standard

The NR Polar Decoder block implements a streaming polar decoder with
hardware-friendly control signals.
The 5G NR standard uses polar codes for channel coding of the DCI, UCI, and BCH transmit
channels.

You must specify the link direction because the coding scheme defined by the 5G NR
standard is different for downlink and uplink messages. Downlink messages are encoded with
interleaving and use a CRC length of 24 bits. Uplink messages do not use interleaving, and use
a CRC length of 6 or 11.

This block implements a CRC-aided successive-cancellation list decoder. This
implementation matches the performance of the `nrPolarDecode` (5G Toolbox) function. You can
choose a list length of 2, 4, or 8. Increasing the list length increases the error correction
performance but uses more hardware resources and increases the decoding latency. You can
improve decoding performance for DCI messages by using the optional **RNTI**
port to specify an expected RNTI value.

This block also performs CRC decoding of the message, equivalent to the `nrCRCDecode` (5G Toolbox) function. The block selects the CRC length based on your
specification of the link direction and the **K** value you provide. The
block detects DCI messages from the values of **K** and
**E**, and automatically prepends 1s to the message, equivalent to the
`padCRC` input argument of the `nrPolarDecode` (5G Toolbox) function.

Because the latency of the polar decoding operation can vary, the block provides an output
signal, **nextFrame**, that indicates when the block is ready to accept new
inputs. For more details, see the Latency section of this page.
