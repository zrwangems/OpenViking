---
type: simulink-block
title: 'Viterbi Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Convolutional'
documentation_page: 'viterbidecoder'
documentation_source_path: 'ref/viterbidecoder.html'
language: en
---

# Viterbi Decoder

## Ports
```yaml
ports:
- name: In
  summary: Convolutionally encoded codeword column vector
  direction: input
  data_types: double | single | Boolean | int8 | int16 | int32 | uint8 | uint16 | uint32 | ufixn
- name: Era
  summary: Erasure bits in codeword binary-valued vector
  direction: input
  data_types: double | Boolean
- name: Rst
  summary: Option to reset state of decoder registers scalar
  direction: input
  data_types: double | Boolean
- name: Out
  summary: Output message binary column vector
  direction: output
  data_types: double | single | Boolean | int8 | int16 | int32 | uint8 | uint16 | uint32 | ufix1
```

### Input

### **In** — Convolutionally encoded codeword column vector

Convolutionally encoded codeword, specified as a column vector. If the
decoder takes *N* input bit streams (that
is, it can receive 2*N* possible input symbols), the block input
vector length is *L*×*N* for some positive integer *L*. For more information, see Input and Output Sizes, Input Values and Decision Types, and the `Operation mode` parameter.

This port is unnamed until a second input port is enabled.

**Data Types:** `double` | `single` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `ufixn`

### **Era** — Erasure bits in codeword binary-valued vector

Erasure bits in the codeword, specified as a binary-valued vector.
Values of `1` in the vector correspond to erased bits,
and values of `0` correspond to nonerased bits.

For these erasures in the incoming data stream, the decoder does not
update the branch metric. The widths and the sample times of the erasure
and the input data ports must be the same.

#### Dependencies

To enable this port, select **Enable erasures
input port**.

**Data Types:** `double` | `Boolean`

### **Rst** — Option to reset state of decoder registers `scalar`

Option to reset the state of decoder registers, specified as scalar
value. When this port receives a nonzero input value, the block sets its
internal memory to the initial state before processing the input data.
Resetting the decoder registers to the initial state sets:

- The all-zeros state metric to zero
- All other state metrics to the maximum value
- The traceback memory to zero

Using the reset port on this block is analogous to setting
**Operation mode** for the Convolutional Encoder block
to `Reset on nonzero input via port`.

#### Dependencies

To enable this port, set the **Operation
mode** parameter to
`Continuous` and select
**Enable reset input port**.

**Data Types:** `double` | `Boolean`
### Output

### **Out** — Output message binary column vector

Output message, returned as a binary column vector. If the decoder
produces *K* output bit streams (that is,
it can produce 2*K* possible output symbols), the block
output vector length is *L*×*K* for some positive integer *L*. For more information, see Input and Output Sizes.

This port is unnamed on the block icon.

**Data Types:** `double` | `single` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `ufix1`
## Parameters
```yaml
parameters:
- name: Trellis structure
  summary: Trellis description of convolutional code poly2trellis(7,[171 133]) (default)
  group: ''
- name: numInputSymbols
  summary: Number of symbols input to encoder 2*K*
  group: ''
- name: numOutputSymbols
  summary: Number of symbols output from encoder 2*N*
  group: ''
- name: numStates
  summary: Number of states in encoder power of 2
  group: ''
- name: nextStates
  summary: Next states matrix of integers
  group: ''
- name: outputs
  summary: Outputs matrix of octal numbers
  group: ''
- name: Punctured code
  summary: Option to enable specification of code puncturing off (default) | on
  group: ''
- name: Puncture vector
  summary: Puncture pattern vector [1; 1; 0; 1; 0; 1] (default) | vector
  group: ''
- name: Enable erasures input port
  summary: Option to enable erasures input port off (default) | on
  group: ''
- name: Decision type
  summary: Decoder decision type Unquantized (default) | Hard decision | Soft decision
  group: ''
- name: Number of soft decision bits
  summary: Soft input word length 4 (default) | positive integer
  group: ''
- name: Error if quantized input values are out of range
  summary: Option to error if quantized input values are out of range off (default) | on
  group: ''
- name: Traceback depth
  summary: Traceback depth 34 (default) | positive integer
  group: ''
- name: Operation mode
  summary: Termination method of encoded frame Continuous (default) | Truncated | Terminated
  group: ''
- name: Enable reset input port
  summary: Option to add reset input port off (default) | on
  group: ''
- name: Delay reset action to next time step
  summary: Option to delay reset action until next time step off (default) | on
  group: ''
- name: State metric word length
  summary: State metric word length 16 (default) | positive integer
  group: ''
- name: Output data type
  summary: Output data type Inherit via internal rule (default) | Smallest unsigned integer | double | single | int8 | uint8
    | int16 | uint16 | int32 | uint32 | boolean
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main

### **Trellis structure** — Trellis description of convolutional code `poly2trellis(7,[171 133])` (default)

Trellis description of the convolutional code, specified as a structure
that contains the trellis description for a rate *K* ∕
*N* code. *K* is the number of input
bit streams, and *N* is the number of output bit
streams.

You can either use the `poly2trellis` function to
create the trellis structure or create it manually. For more about this
structure, see Trellis Description of a Convolutional Code and the
`istrellis` function.

The trellis structure contains these fields.

### **numInputSymbols** — Number of symbols input to encoder 2*K*

Number of symbols input to the encoder, specified as an integer equal to
2*K*, where *K*
is the number of input bit streams.

### **numOutputSymbols** — Number of symbols output from encoder 2*N*

Number of symbols output from the encoder, specified as an integer equal to
2*N*, where *N*
is the number of output bit streams.

### **numStates** — Number of states in encoder power of 2

Number of states in the encoder, specified as a power of 2.

### **nextStates** — Next states matrix of integers

Next states for all combinations of current states and current inputs, specified
as a matrix of integers. The matrix size must be `numStates` by
2*K*.

### **outputs** — Outputs matrix of octal numbers

Outputs for all combinations of current states and current inputs, specified as a matrix of
octal numbers. The matrix size must be `numStates` by
2*K*.

### **Punctured code** — Option to enable specification of code puncturing `off` (default) | `on`

Select this parameter to view and enable the **Puncture
vector** parameter.

### **Puncture vector** — Puncture pattern vector `[1; 1; 0; 1; 0; 1]` (default) | vector

Puncture pattern vector to puncture the decoded data, specified as a vector. The vector
must contain `1`s and `0`s, where
`0` indicates the position of the punctured bits. This
puncture pattern must match the puncture pattern used by the convolutional
encoder.

For some commonly used puncture patterns for specific rates and
polynomials, see the Yasuda [4], Haccoun [5], and Begin [6] references.

#### Dependencies

This parameter appears only when you select the **Punctured code** parameter.

### **Enable erasures input port** — Option to enable erasures input port `off` (default) | `on`

Select this parameter to add the `Era` input port to
the block.

### **Decision type** — Decoder decision type `Unquantized` (default) | `Hard decision` | `Soft decision`

Decoder decision type, specified as
`Unquantized`, `Hard
decision`, or `Soft Decision`.

- `Unquantized` — The decoder uses the
  Euclidean distance to calculate the branch metrics. The input
  data must be a real-valued vector of double- or single-precision
  soft values that are unquantized. The object maps positive
  values to logical `1`s and negative values to
  logical `0`s
- `Hard decision` — The decoder uses
  Hamming distance to calculate the branch metrics. The input must
  be a vector of hard decision values, which are
  `0`s or `1`s. The data
  type of the inputs must be double precision, single precision,
  logical, or numeric.
- `Soft Decision` — The decoder uses
  Hamming distance to calculate the branch metrics. The input
  requires a vector of quantized soft values that are represented
  as integers between 0 and 2*SoftInputWordLength*
  – 1. The data type of the inputs must be double
  precision, single precision, logical, or numeric. Alternatively,
  you can specify the data type as an unsigned and unscaled
  fixed-point object using the `fi` (Fixed-Point Designer) object with
  a word length (*SoftInputWordLength*) equal
  to the word length that you specify for the **Number of
  soft decision bits** parameter.
  `0` is considered as most confident
  `0` and 2*SoftInputWordLength*
  – 1 as the most confident
  `1`.

### **Number of soft decision bits** — Soft input word length `4` (default) | positive integer

Soft input word length that represents the number of bits for each
quantized soft input value, specified as an integer.

#### Dependencies

This parameter appears only when you set the **Decision type** parameter to `Soft
decision`.

### **Error if quantized input values are out of range** — Option to error if quantized input values are out of range `off` (default) | `on`

Select this parameter to error if the quantized input values are out of
range. If you do not select this parameter, out of range input values are
ignored.

#### Dependencies

This parameter appears only when you set the **Decision type** parameter to `Hard
decision` or `Soft
decision`.

### **Traceback depth** — Traceback depth `34` (default) | positive integer

Traceback depth, specified as an integer that indicates the number of
trellis branches used to construct each traceback path.

The traceback depth influences the decoding delay. The decoding delay is the number of zero symbols that precede the first decoded symbol in the output.

- For the continuous operating mode, the decoding delay is equal to the number of
  traceback depth symbols.
- For the truncated or terminated operating mode, the decoding delay is zero. In
  this case, the traceback depth must be less than or equal to the number of symbols
  in each input.

As a general estimate, a typical traceback depth value is approximately two
to three times (*ConstraintLength* – 1) / (1 –
*coderate*). The constraint length of the code, *ConstraintLength*,
is equal to (log2(`trellis`.`numStates`) +
1). The *coderate* is equal to (*K* / *N*) ×
(length(*PuncturePattern*) /
sum(*PuncturePattern*).

*K* is the number of input symbols, *N*
is the number of output symbols, and *PuncturePattern* is the puncture
pattern vector.

For example, applying this general estimate, results in these approximate
traceback depths.

- A rate 1/2 code has a traceback depth of 5(*ConstraintLength* – 1).
- A rate 2/3 code has a traceback depth of 7.5(*ConstraintLength* – 1).
- A rate 3/4 code has a traceback depth of 10(*ConstraintLength* – 1).
- A rate 5/6 code has a traceback depth of 15(*ConstraintLength* – 1).

For more information, see [7].

### **Operation mode** — Termination method of encoded frame `Continuous` (default) | `Truncated` | `Terminated`

Method for transitioning between successive input frames, specified as one
of these mode values.

- `Continuous` — The block saves its
  internal state metric at the end of each input, for use with the
  next frame. Each traceback path is treated independently. This
  mode results in a decoding delay of **Traceback depth**×*K* zero bits
  for a rate *K*/*N*
  convolutional code. *K* is the number of
  message symbols, and *N* is the number of coded
  symbols. If the **Enable reset input port** is
  selected, the decoder states are reset if the
  `Rst` port receives a nonzero value.
- `Truncated` — The block treats each
  input independently. The traceback path starts at the state with
  the best metric and always ends in all-zeros state. This mode is
  appropriate when the corresponding Convolutional Encoder
  block has its **Operation mode**
  set to `Truncated (reset every frame)`. There
  is no output delay for this mode.
- `Terminated` — The block treats each
  input independently, and the traceback path always starts and
  ends in all-zeros state. This mode is appropriate when the
  uncoded message signal (that is, the input to the corresponding
  Convolutional Encoder
  block) has enough zeros at the end of each input to fill all
  memory registers of the feed-forward encoder. Specifically,
  there are at least `k*max(constr-1)` zeros at
  the end of the input, for an encoder that has
  `k` input streams and constraint length
  vector `constr` (using the polynomial
  description). For feedback encoders, this mode is appropriate if
  the corresponding Convolutional Encoder
  block has **Operation mode** set to
  `Terminate trellis by appending
  bits`.

**Note**

The decoder states reset at every input time step when the block
outputs sequences that vary in length during simulation and you set the
**Operation mode** to
`Truncated` or
`Terminated`.

When the input signal contains only one symbol, use the
`Continuous` operation mode.

### **Enable reset input port** — Option to add reset input port `off` (default) | `on`

Select this parameter to add the `Rst` input
port.

#### Dependencies

This parameter appears only when you set the **Operation mode** parameter to
`Continuous`.

### **Delay reset action to next time step** — Option to delay reset action until next time step `off` (default) | `on`

Select this parameter to delay reset of the decoder until after computing
the encoded data received in the current time step. You must enable this
option for HDL support. Generating HDL code requires HDL Coder™ software.

#### Dependencies

This parameter appears only when you set the **Operation mode** parameter to
`Continuous` and select **Enable
reset input port**.

#### Data Types

### **State metric word length** — State metric word length `16` (default) | positive integer

State metric word length, specified as a positive integer.

### **Output data type** — Output data type `Inherit via internal rule` (default) | `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Output data type, specified as `double`,
`single`, `boolean`,
`int8`, `uint8`,
`int16`, `uint16`,
`int32`, or `uint32`, or set to
`'Inherit via internal rule'` or `'Smallest
unsigned integer'`.

- When set to `'Smallest unsigned integer'`, the
  output data type is selected based on the settings used in the
  **Hardware Implementation** pane of the
  Configuration Parameters dialog box of the model. If
  `ASIC/FPGA` is selected in the
  **Hardware Implementation** pane, the output
  data type is `ufix(1)`. For all other selections,
  it is an unsigned integer with the smallest specified word length
  corresponding to the char value (for example,
  `uint8`).
- When set to `'Inherit via internal rule'`, the block:

  - Outputs data type double for double inputs
  - Outputs data type single for single inputs
  - Behaves similar to the `'Smallest unsigned
    integer'` option for all other data type
    inputs
## Libraries

Communications Toolbox / Error Detection and Correction / Convolutional Communications Toolbox HDL Support / Error Detection and Correction / Convolutional

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Input can be ufix(1) for hard decision, and ufix(N) for soft decision; output can be ufix(1) only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**Note**

For decoding data encoded with truncated or terminated modes, or punctured
codes, use the Viterbi
Decoder (Wireless HDL Toolbox)
block. The Wireless HDL Toolbox™ block provides an HDL-optimized algorithm with hardware-friendly
control signals and simulates the latency of the HDL algorithm in Simulink.

HDL Coder provides additional configuration options that affect HDL
implementation and synthesized logic.

HDL Coder supports the following features of the Viterbi Decoder
block:

- Non-recursive encoder/decoder with feed-forward trellis and simple shift
  register generation configuration
- Continuous mode
- Sample-based input
- Decoder rates from 1/2 to 1/7
- Constraint length from 3 to 9

When you set **Decision type** to `Soft
decision`, HDL code generation is supported for fixed-point input
and output data types. The input fixed-point data type must be
`ufixN`. `N` is the number of soft-decision
bits. HDL code generation is not supported for signed built-in data types
(`int8`, `int16`, `int32`).

When you set **Decision type** to `Hard
decision`, HDL code generation is supported for input with data
types `ufix1` and `Boolean`. HDL code generation
is not supported for double and single input data types.

The Viterbi Decoder block decodes every bit by tracing back through
a traceback depth that you define for the block. The block implements a complete
traceback for each decision bit, using registers to store the minimum state index
and branch decision in the traceback decoding unit. There are two methods to
optimize the traceback logic: a pipelined register-based implementation or a
RAM-based architecture. See the Generate HDL Code for Viterbi Decoder example.

**Register-Based Traceback**

You can specify that the traceback decoding unit be pipelined to improve the
speed of the generated circuit. You can add pipeline registers to the traceback
unit by specifying the number of traceback stages per pipeline register.

Using the `TracebackStagesPerPipeline` implementation
parameter, you can balance the circuit performance
based on system requirements. A smaller parameter value indicates the
requirement to add more registers to increase the speed of the traceback
circuit. Increasing the parameter value results in fewer registers along with a
decrease in the circuit speed.

**RAM-Based Traceback**

Instead of using registers, you can choose to use RAMs to save the survivor
branch information. The coder does not support **Enable reset input
port** when using RAM-based traceback.

1. Right-click the block and open **HDL Code** > **HDL Block Properties**. Set the **Architecture** property to
   `RAM-based Traceback`.
2. Double-click the block and set the **Traceback
   depth** on the Viterbi Decoder block
   mask.

RAM-based traceback and register-based traceback differ in the following
ways:

- The RAM-based implementation traces back through one set of data to
  find the initial state to decode the previous set of data. The
  register-based implementation combines the traceback and decode
  operations into one step. It uses the best state found from the minimum
  operation as the decoding initial state.
- RAM-based implementation traces back through M samples, decodes the
  previous M bits in reverse order, and releases one bit in order at each
  clock cycle. The register-based implementation decodes one bit after a
  complete traceback.

Because of the differences in the two traceback algorithms, the RAM-based
implementation produces different numerical results than the register-based
traceback. A longer traceback depth, for example, 10 times the constraint
length, is recommended in the RAM-based traceback. This depth achieves a similar
bit error rate (BER) as the register-based implementation. The size of RAM
required for the implementation depends on the trellis and the traceback depth.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **TracebackStagesPerPipeline** | See Register-Based Traceback. |

**Restrictions**

- **Punctured code**: Do not select this option.
  Punctured code requires frame-based input, which HDL Coder does not support.
- **Decision type**: The coder does not support the
  `Unquantized` decision type.
- **Error if quantized input values are out of range**:
  The coder does not support this option.
- **Operation mode**: The coder supports only the
  `Continuous` mode.
- **Enable reset input port**: When you enable both
  **Enable reset input port** and **Delay
  reset action to next time step**, HDL support is provided.
  You must select `Continuous` operation mode,
  and use register-based traceback.
- You cannot use the Viterbi Decoder block inside a Resettable Synchronous
  Subsystem (HDL Coder).

## Version History

**Introduced before R2006a**

### R2022b: Version History

Unquantized input values outside of the range [–1012,
1012] are clipped to –1012
and 1012, respectively.

## Description

Decode convolutionally encoded data using Viterbi algorithm

The Viterbi Decoder block decodes convolutionally encoded input symbols to produce binary
output symbols by using the Viterbi algorithm. A trellis structure specifies the
convolutional encoding scheme. For more information, see Trellis Description of a Convolutional Code.

This block can process several symbols at a time for faster performance and can accept
inputs that vary in length during simulation. For more information about variable-size
signals, see Variable-Size Signal Basics (Simulink).

This icon shows all the optional block ports enabled.

Viterbi Decoder block with optional erasure and reset ports enabled
