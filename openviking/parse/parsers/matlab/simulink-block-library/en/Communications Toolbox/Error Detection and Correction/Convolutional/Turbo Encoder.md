---
type: simulink-block
title: 'Turbo Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Convolutional'
documentation_page: 'turboencoder'
documentation_source_path: 'ref/turboencoder.html'
language: en
---

# Turbo Encoder

## Ports

### Input

### **In** — Input message binary column vector

Input message, specified as a binary column vector of length
*L*, where *L* is the length of
the uncoded input message.

**Data Types:** `double` | `int8` | `fi(data,0,1)`

### **IntrInd** — Interleaver indices column vector of integers

Interleaver indices, specified as a column vector of integers. The
vector must be of length *L*, where
*L* is the length of the binary input message. Each
element of the vector must be an integer in the range [1,
*L*] and must be unique. The interleaver indices
define the mapping used to permute the input bits at the encoder.

#### Dependencies

To enable this port, set the **Source of interleaver
indices** property to `Input
port`.

**Data Types:** `double`

### **OutInd** — Output indices column vector of integers

Output indices for the bit ordering and puncturing used on the fully
encoded data, specified as a column vector of integers. Element values
in the vector must be relative to the fully encoded data for the coding
scheme, including the tail bits for all streams.

**Tunable:** Yes

#### Dependencies

To enable this port, set the **Source of output
indices** property to `Input
port`.

**Data Types:** `double`
### Output

### **Out** — Parallel concatenated codeword binary column vector

Parallel concatenated codeword, returned as a binary column vector of
length *M*, where *M* is the number of
bits in the parallel concatenated codeword. This output inherits its
data type from the `In` input.

**Data Types:** `double` | `int8` | `fi(data,0,1)`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Trellis structure** — Trellis description of constituent convolutional code `poly2trellis(4,[13 15],13)` (default) | structure

Specify the trellis as a MATLAB® structure that contains the trellis description for a rate
*K* ∕ *N* constituent convolutional
code. *K* is the number of input bit streams, and
*N* is the number of output bit streams.

**Note**

*K* must be 1 for the turbo coder. For more
information, see Coding Rate.

You can either use the `poly2trellis` function to
create the trellis structure or create it manually. For more about this
structure, see the Trellis Description of a Convolutional Code topic and the
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

### **Source of interleaver indices** — Source of interleaver indices `Property` (default) | `Input port`

Specify the source of the interleaver indices as
`Property` or `Input
port`.

- When you set this parameter to
  `Property`, the block uses the
  **Interleaver indices** parameter to specify
  the interleaver indices.
- When you set this parameter to `Input
  port`, the block uses the
  `IntrInd` input port to specify the
  interleaver indices.

### **Interleaver indices** — Interleaver indices `(64:-1:1).'` (default) | column vector of integers

Specify the interleaver indices as a column vector of integers. The vector
must be of length *L*, where *L* is the
length of the binary input message. Each element of the vector must be an
integer in the range [1, *L*] and must be unique. The
interleaver indices define the mapping used to permute the input bits at the
encoder.

#### Dependencies

To enable this parameter, set the **Source of interleaver
indices** parameter to
`Property`.

### **Source of output indices** — Source of output indices `Auto` | `Property` | `Input port`

Specify the source of the output indices as `Auto`, `Property`, or
`Input port`.

- When you set this parameter to `Auto`, the block computes output indices that
  puncture the second systematic stream and include all tail
  bits.
- When you set this parameter to
  `Property`, the block uses the
  output indices that you specify for the **Output
  indices** parameter.
- When you set this parameter to `Input
  port`, the block uses the
  **OutInd** input port to specify the output
  indices. The vector length and values for the output indices and
  coded output signal can change with each execution of the
  block.

### **Output indices** — Output indices `getTurboIOIndices(64,2,3)` (default) | column vector of integers

Specify the output indices for the bit ordering and puncturing used on the
fully encoded data as a column vector of integers. The number of bits output
from the encoder is equal to the length of this parameter. The maximum
length must not exceed the fully encoded length of
(*L*+*mLen*) × *N* ×
2), where *L* is the input vector length,
*mLen* is the memory length, and *N*
is the number of constituent coder encoded streams.

#### Dependencies

To enable this parameter, set the **Source of output
indices** parameter to
`Property`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as `Interpreted
execution` or `Code generation`.

- `Interpreted execution` — Simulate the model by
  using the MATLAB interpreter. This option requires less startup time, but the
  speed of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / Error Detection and Correction / Convolutional

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a ufix(1) only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

## Description

Encode binary data using parallel concatenated encoding scheme

The Turbo Encoder block encodes a binary input signal using a parallel concatenated
coding scheme. This coding scheme employs two identical convolutional encoders and one
internal interleaver. Each constituent encoder is independently terminated by tail bits.
For more information about the constituent encoders, see Parallel Concatenated Convolutional Encoding Scheme.

This icon shows the block with all ports enabled.

Turbo Encoder block with optional ports (IntrInd and OutInd) enabled
