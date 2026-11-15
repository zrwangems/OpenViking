---
type: simulink-block
title: 'QPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Phase Modulation'
documentation_page: 'qpskdemodulatorbaseband'
documentation_source_path: 'ref/qpskdemodulatorbaseband.html'
language: en
---

# QPSK Demodulator Baseband

## Ports

### Input

### **In** — Input QPSK-modulated signal scalar | vector

Input QPSK-modulated signal, specified as a complex-valued scalar or
vector containing the baseband representation of a QPSK-modulated
signal. When the noise variance or signal power result in computations
involving extreme positive or negative magnitudes, see Soft-Decision QPSK Demodulation for demodulation decision type considerations.

This port in unnamed on the block until you enable the
**Var** port.

**Data Types:** `double` | `single` | `fixed point`
**Complex Number Support:** Yes

### **Var** — Noise variance estimate positive scalar

Noise variance estimate, specified as a positive scalar.

When the noise variance or signal power result in computations
involving extreme positive or negative magnitudes, see Soft-Decision QPSK Demodulation for demodulation decision type considerations.

#### Dependencies

This parameter applies when you set **Noise variance source** to
`Port`.

**Data Types:** `double` | `single`
### Output

### **Out** — Output signal scalar | column vector

Output signal, returned as a scalar or column vector. The output is a
demodulated version of the PSK-modulated input signal, **In**.

- When you set **Output type** to
  `Integer`, the returned output
  signal elements are integers in the range [0, 3].
- When you set **Output type** to
  `Bit`, the returned output
  signal contains a vector with an even number of elements
  because QPSK has 2 bits per symbol.

This port in unnamed on the block.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Output type** — Integer or bit pair output indicator `Integer` (default) | `Bit`

Integer or bit pair output indicator, specified as
`Integer` or `Bit`.

- When you set **Output type** to
  `Integer` and **Constellation ordering** to
  `Binary`, the block maps the
  point e(jϕ +
  jπm/2) to *m*, where ϕ is the
  phase offset in radians (**Phase offset (rad)**) and
  *m* is 0, 1, 2, or 3.
- When you set **Output type** to
  `Bit` and **Decision type** to `Hard
  decision`, the output contains pairs of binary
  values. The most significant bit (top-most bit in the
  vector) is the first bit the block outputs.
- When you set **Output type** to
  `Bit` and **Decision type** to `Log-likelihood
  ratio` or `Approximate log-likelihood
  ratio`, the output contains bitwise LLR or
  approximate LLR values, respectively.

### **Decision type** — Demodulator output `Hard decision` (default) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

Demodulator output, specified as `Hard
decision`, `Log-likelihood
ratio`, or `Approximate log-likelihood
ratio`. The LLR and approximate LLR outputs are used
with error decoders that support soft-decision inputs, such as a Viterbi Decoder, to achieve
superior performance. For more information, see Algorithms.

The output values for `Log-likelihood ratio`
and `Approximate log-likelihood ratio` decision
types are of the same data type as the input values.

#### Dependencies

This parameter applies when you set **Output type** to `Bit`.

### **Noise variance source** — Source of noise variance estimate `Dialog` (default) | `Port`

Source of noise variance estimate, specified as one of these options:

- To define the noise variance by using the **Noise variance** parameter, set this
  parameter to `Dialog`.
- To define the noise variance by using the **Var** port, set this parameter to
  `Port`.

#### Dependencies

This parameter applies when you set **Decision type** to `Log-likelihood
ratio` or `Approximate log-likelihood
ratio`.

### **Noise variance** — Noise variance estimate `1` (default) | positive scalar

Noise variance estimate, specified as a positive scalar.

When the noise variance or signal power result in computations
involving extreme positive or negative magnitudes, see Soft-Decision QPSK Demodulation for demodulation decision type considerations.

This parameter is tunable in normal mode, accelerator mode and rapid
accelerator mode. If you use the Simulink
Coder™ rapid simulation (RSIM) target to build an RSIM
executable, then you can tune the parameter without recompiling the
model. Avoiding recompilation is useful for Monte Carlo simulations in
which you run the simulation multiple times (perhaps on multiple
computers) with different amounts of noise.

**Tunable:** Yes

#### Dependencies

This parameter applies when you set **Noise variance source** to
`Dialog`.

### **Constellation ordering** — Symbol mapping `Gray` (default) | `Binary`

Symbol mapping of integer or bit pair outputs, specified as
`Gray` or
`Binary`.

- To map symbols using Gray-coded ordering, set this
  parameter to `Gray`.
- To map symbols using binary-coded ordering, set this
  parameter to `Binary`.

### **Phase offset (rad)** — Phase offset of zeroth point `pi/4` (default) | scalar

Phase of the zeroth point of the signal constellation in radians,
specified as a scalar.

### Data Types

### **Output** — Output data type `Same as input`

Output data type is the same as the input data type.

#### Dependencies

This setting applies when you set **Output type** to `Bit` and
**Decision type** to `Log-likelihood
ratio` or `Approximate log-likelihood
ratio`.

### **Output data type** — Output data type `Inherit via internal rule` (default) | `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Output data type of the demodulated signal, specified as one of these
options:

- For integer outputs, the output data type can be set to
  `'Inherit via internal rule'`,
  `'Smallest unsigned integer'`,
  `double`, `single`,
  `int8`, `uint8`,
  `int16`, `uint16`,
  `int32`, or
  `uint32`.
- For bit outputs, when you set **Decision type** to `Hard
  decision`, the output data type can be set to
  `'Inherit via internal rule'`,
  `'Smallest unsigned integer'`,
  `double`, `single`,
  `int8`, `uint8`,
  `int16`, `uint16`,
  `int32`, `uint32`, or
  `boolean`.

When you set this parameter to `'Inherit via internal
rule'`, the block inherits the output data type from the
input port.

- If the input is a floating-point type
  (`single` or
  `double`), the output data type is the same
  as the input data type.
- If the input data type is fixed-point, the output data
  type works as if this parameter is set to `'Smallest
  unsigned integer'`.

When you set this parameter to `'Smallest unsigned
integer'`, the output data type is based on the settings
that you use in the **Hardware Implementation** pane of
the Configuration Parameters dialog box of the model.

- If `ASIC/FPGA` is selected in the
  **Hardware Implementation** pane, and
  you set **Output type** to `Bit`, the
  output data type is the ideal minimum one-bit size
  (`ufix(1)`). For all other selections,
  it is an unsigned integer with the smallest available word
  length large enough to fit 1 bit, usually corresponding to
  the size of a char (for example,
  `uint8`).
- If `ASIC/FPGA` is selected in the
  **Hardware Implementation** pane, and
  you set **Output type** to `Integer`,
  the output data type is the ideal minimum two-bit size
  (`ufix(2)`). For all other selections,
  it is an unsigned integer with the smallest available word
  length large enough to fit 2 bits, usually corresponding to
  the size of a char (for example,
  `uint8`).

For information about specifying data types, see Data Type Assistant.

#### Dependencies

This parameter applies when you set **Output type** to `Integer`
or **Output type** to
`Bit` and **Decision type** to `Hard
decision`.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Fixed-point inputs must be signed.  b When ASIC/FPGA is selected in the Hardware Implementation Pane, output is ufix(1) for bit outputs, and ufix(ceil(log2(M))) for integer outputs. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced before R2006a**

## Description

Demodulate QPSK-modulated data

The QPSK Demodulator Baseband block demodulates a signal that was modulated using the
quadrature phase shift keying method (QPSK) method. The input is a baseband
representation of the modulated signal.

The input must be a complex signal. This block accepts a scalar or column vector input
signal. For information about the data types, see Supported Data Types.
