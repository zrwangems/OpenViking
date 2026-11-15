---
type: simulink-block
title: 'Sine Wave'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'sinewave'
documentation_source_path: 'ref/sinewave.html'
language: en
---

# Sine Wave

## Ports

### Output

### **Port\_1** — Sinusoidal signal scalar | vector | matrix

Output a sinusoidal signal as a scalar or vector. For more information
about output complexity, see Description. For information about
multichannel support, see Generating Multichannel Outputs.

**Tip**

To output fixed-point data types, you must set **Sample
mode** to `Discrete` and
**Computation method** to `Table
lookup`.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main

### **Amplitude** — Amplitude of sine waves `1` (default) | scalar | vector

A length-*N* vector containing the amplitudes of
the sine waves in each of *N* output channels, or a
scalar to be applied to all *N* channels. The vector
length must be the same as that specified for the
**Frequency** and **Phase offset**
parameters.

**Tip**

This parameter is tunable (Simulink) only when the **Computation
method** is `Trigonometric
fcn` or
`Differential`.

**Tunable:** Yes

### **Frequency (Hz)** — Frequency of each sine wave `100` (default) | scalar | vector

A length-*N* vector containing frequencies, in
hertz, of the sine waves in each of *N* output
channels, or a scalar to be applied to all *N*
channels. The vector length must be the same as that specified for the
**Amplitude** and **Phase offset**
parameters. You can specify positive, zero, or negative frequencies.

**Tip**

This parameter is tunable (Simulink) when you set:

- Solver **Type** to
  `Fixed-step`.
- **Sample mode** to
  `Continuous`.
- **Sample mode** to
  `Discrete` and
  **Computation method** to
  `Trigonometric fcn`.

**Tunable:** Yes

### **Phase offset (rad)** — Phase offset `0` (default) | scalar | vector

A length-*N* vector containing the phase offsets,
in radians, of the sine waves in each of *N* output
channels, or a scalar to be applied to all *N*
channels. The vector length must be the same as that specified for the
**Amplitude** and **Frequency**
parameters.

**Tip**

This parameter is tunable (Simulink) when you set:

- Solver **Type** to
  `Fixed-step`.
- **Sample mode** to
  `Continuous`.
- **Sample mode** to
  `Discrete` and
  **Computation method** to
  `Trigonometric fcn`.

**Tunable:** Yes

### **Sample mode** — Continuous or discrete sampling mode `Discrete` (default) | `Continuous`

Specify the sampling mode as `Continuous` or
`Discrete`:

- `Continuous`

  In continuous mode, the sinusoid in the
  *i*th channel,
  *yi*, is
  computed as a continuous function,

  yi=Aisin(2πfit+ϕi)(real)oryi=Aiej(2πfit+ϕi)(complex)

  and the block's output is continuous. In this mode, the block
  operates the same as the Simulink® Sine Wave block with **Sample
  time** set to `0`. This mode
  offers high accuracy, but requires trigonometric function
  evaluations at each simulation step, which is computationally
  expensive. Also, because this method tracks absolute simulation
  time, a discontinuity will eventually occur when the time value
  reaches its maximum limit.

  Note also that many DSP System Toolbox™ blocks do not accept continuous-time
  inputs.
- `Discrete`

  In discrete mode, the block can generate discrete-time output
  by directly evaluating the trigonometric function, by table
  lookup, or by a differential method. For more information on
  these computation methods, see Algorithms.

### **Output complexity** — Real or complex waveform `Real` (default) | `Complex`

The type of waveform to generate: `Real`
specifies a real sine wave, `Complex` specifies
a complex exponential.

### **Computation method** — Method for computing discrete-time sinusoids `Trigonometric fcn` (default) | `Table lookup` | `Differential`

The method by which discrete-time sinusoids are generated:
`Trigonometric fcn`, `Table
lookup`, or `Differential`.
For more information on each of the available options, see Algorithms.

#### Dependencies

This parameter is only visible when you set the **Sample
mode** to `Discrete`.

**Note**

To generate fixed-point sinusoids, you must set the
**Computation method** to
`Table lookup`.

### **Optimize table for** — Optimize for speed or memory `Speed` (default) | `Memory`

Optimizes the table of sine values for
`Speed` or
`Memory`. When optimized for speed, the
table contains *k* elements, and when optimized for
memory, the table contains *k*/4 elements, where
*k* is the number of input samples in one full
period of the sine wave.

#### Dependencies

This parameter is only visible when you set the
**Computation method** parameter to
`Table lookup`.

### **Sample time** — Sample period `1/1000` (default) | scalar

The period with which the sine wave is sampled,
*Ts*, as a finite
scalar, greater than zero. The output frame period of the block is
*M**Ts*,
where you specify *M* in the **Samples per
frame** parameter.

#### Dependencies

To enable this parameter, set **Sample mode** to
`Discrete`.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

The number of consecutive samples from each sinusoid to buffer into
the output frame, *M*, specified as a positive scalar
integer. This parameter is not tunable.

The block output is an *M*-by-*N*
matrix with frame period
*M**T*s,
where you specify *T*s in the
**Sample time** parameter.

#### Dependencies

To enable this parameter, set **Sample mode** to
`Discrete`.

### **Resetting states when re-enabled** — State behavior inside enabled subsystems `Restart at time zero` (default) | `Catch up to simulation time`

This parameter determines the behavior of the Sine Wave
block when an enabled subsystem is reenabled. The block can either reset
itself to its starting state (`Restart at time
zero`), or resume generating the sinusoid based on the
current simulation time (`Catch up to simulation
time`).

#### Dependencies

This parameter only applies when the Sine Wave
block is located inside an enabled subsystem and the
**States when enabling** parameter of the
Enable (Simulink) block is set
to `reset`.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>` | `Inherit:Inherit via back propagation`

Select how you would like to specify the data type properties of the
**Output data type**. You can choose:

- `Inherit` — Lets you
  specify a rule for inheriting a data type, for example,
  `Inherit: Inherit via back
  propagation`
- `Built in`— Lets you
  specify a built in data type, for example,
  `double`
- `Fixed point` — Lets you
  specify the fixed-point attributes of the data type.
- `Expression` — Lets you
  specify an expression that evaluates to a valid data type,
  for example, `fixdt(1,16)`

### Data Type Assistant

### **Mode** — Data type mode `Built in` (default) | `Inherit` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output data type**. You can choose:

- `Inherit` — Lets you
  specify a rule for inheriting a data type, for example,
  `Inherit: Inherit via back
  propagation`
- `Built in`— Lets you
  specify a built-in data type, for example,
  `double`
- `Fixed point` — Lets you
  specify the fixed-point attributes of the data type.
- `Expression` — Lets you
  specify an expression that evaluates to a valid data type,
  for example, `fixdt(1,16)`

For more information, see Specify Data Types Using Data Type Assistant (Simulink).

### **Signedness** — Signedness of fixed-point data `Signed` (default)

Specify the signedness of the fixed-point output. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Limitations

The Sine Wave only supports
`Signed` data types.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 2 to 128

Specify the bit size of the word that holds the quantized integer as a
positive integer from 2 to 128. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`

### **Fraction length** — Fraction length for fixed-point data type `0` (default) | integer scalar

Specify the fraction length of the fixed-point data type as a positive
or negative integer scalar.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point` and
**Scaling** to `Binary
point`.

### **Data type override** — Data type override mode `Inherit` (default) | `Off`

Select the data type override mode for this signal. You can
select:

- `Inherit` — Inherits the data type
  override setting specified for the model.
- `Off` — Ignores the data type
  override setting specified for the model and uses the
  fixed-point data type you specify.

#### Dependencies

To enable this parameter, set **Mode** to
`Built in` or `Fixed
point`. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

## Libraries

DSP System Toolbox / Sources DSP System Toolbox HDL Support / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Sine Wave block references absolute simulation time when
configured in continuous sample mode.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**Note**

For a sine wave generator that is optimized for HDL code generation and has
hardware-friendly control signals, see NCO (DSP HDL Toolbox), and Generate Sine Wave (DSP HDL Toolbox). The DSP HDL Toolbox™ blocks provide HDL-optimized algorithms with hardware-friendly
control signals and simulate the latency of the HDL algorithm in Simulink.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**Restrictions**

For HDL code generation, you must select the following Sine
Wave block settings:

- **Computation method**: `Table
  lookup`
- **Sample mode**:
  `Discrete`

Output:

- The output port cannot have data types `single` or
  `double`.
- This block does not support frame-based vector output during HDL code
  generation. The vector outputs from amplitude and frequency array are
  supported.

**Complex Data Support**

This block supports code generation for complex signals.

## Version History

**Introduced before R2006a**

## Description

Generate continuous or discrete sine wave

The Sine Wave block generates a multichannel real or complex sinusoidal
signal, with independent amplitude, frequency, and phase in each output channel. The
block supports floating point and signed fixed-point data types.

The block generates a real sinusoidal signal when you set the **Output
complexity** parameter to `Real`. The real
sinusoidal output is defined by an expression of the type

y=Asin(2πft+ϕ)

where you specify *A* in the **Amplitude**
parameter, *f* in hertz in the **Frequency**
parameter, and *ϕ* in radians in the **Phase
offset** parameter.

The block generates a complex exponential signal when you set the **Output
complexity** parameter to `Complex`. This complex
exponential signal is defined by an expression of the type

y=Aej(2πft+ϕ)=A{cos(2πft+ϕ)+jsin(2πft+ϕ)}

### Generating Multichannel Outputs

For both real and complex sinusoids, the **Amplitude**,
**Frequency**, and **Phase offset** parameter
values (*A*, *f*, and *ϕ*)
can be scalars or length-*N* vectors, where
*N* is the desired number of channels in the output. When you
specify at least one of these parameters as a length-*N* vector,
scalar values specified for the other parameters are applied to every
channel.

For example, to generate the three-channel output containing the following real
sinusoids, set the block parameters as shown:

y={sin(2000πt)  (channel 1)2sin(1000πt)   (channel 2)3sin(500πt+π2)   (channel 3)

- **Output complexity** =
  `Real`
- **Amplitude** = `[1 2 3]`
- **Frequency** = `[1000 500 250]`
- **Phase offset** = `[0 0 pi/2]`
