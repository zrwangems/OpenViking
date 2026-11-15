---
type: simulink-block
title: 'Pulse Generator'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'pulsegenerator'
---

# Pulse Generator

Generate square wave pulses at regular intervals

## Libraries

Simulink / Sources

## Description

The Pulse Generator block generates square wave pulses at regular intervals.
The block waveform parameters, **Amplitude**, **Pulse
Width**, **Period**, and **Phase delay**,
determine the shape of the output waveform. The following diagram shows how each
parameter affects the waveform.

The Pulse Generator block can emit scalar, vector, or
matrix signals of any real data type. To emit a scalar signal, use scalars to specify
the waveform parameters. To emit a vector or matrix signal, use vectors or matrices,
respectively, to specify the waveform parameters. Each element of the waveform
parameters affects the corresponding element of the output signal. For example, the
first element of a vector amplitude parameter determines the amplitude of the first
element of a vector output pulse. All the waveform parameters must have the same
dimensions after scalar expansion. The data type of the output is the same as the data
type of the **Amplitude** parameter.

The block output can be generated in time-based or sample-based modes, determined by the
**Pulse type** parameter.

### Time-Based Mode

In time-based mode, Simulink® computes the block output only at times when the output actually
changes. This approach results in fewer computations for the block output over the
simulation time period. Activate this mode by setting the **Pulse
type** parameter to `Time based`.

The block does not support a time-based configuration that results in a constant
output signal. Simulink returns an error if the parameters **Pulse Width**
and **Period** satisfy either of these conditions:

Period​\*PulseWidth100=0Period​\*PulseWidth100=Period

Depending on the pulse waveform characteristics, the intervals between changes in
the block output can vary. For this reason, a time-based Pulse Generator block has a
variable sample time. The sample time color of such blocks is brown (see View Sample Time Information
for more information).

Simulink cannot use a fixed-step solver to compute the output of a time-based
pulse generator. If you specify a fixed-step solver for models that contain
time-based pulse generators, Simulink computes a fixed sample time for the time-based pulse generators. Then
the time-based pulse generators simulate as sample based.

If you use a fixed-step solver and the **Pulse type** is `Time based`, choose the step size such that the
period, phase delay, and pulse width (in seconds) are integer multiples of the
solver step size. For example, suppose that the period is `4`
seconds, the pulse width is `75%` (that is, `3`
s), and the phase delay is `1` s. In this case, the computed sample
time is `1` s. Therefore, choose a fixed-step size of
`1` or a number that divides `1` exactly (for
example, `0.25`). To ensure this setting, select
`auto` on the **Solver** pane of the
Configuration Parameters dialog box.

### Sample-Based Mode

In sample-based mode, the block computes its outputs at fixed intervals that you
specify. Activate this mode by setting the **Pulse type** parameter
to `Sample based`.

An important difference between the time-based and sample-based modes is that in time-based
mode, the block output is based on simulation time, and in sample-based mode, the
block output depends only on the simulation start, regardless of elapsed simulation
time.

This block supports reset semantics in sample-based mode. For example, if a Pulse
Generator block is in a resettable subsystem that hits a reset trigger,
the block output resets to its initial condition.

## Ports

### Output

### **Port\_1** — Output signal scalar | vector | matrix

Generated square wave pulse signal specified by the parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Pulse type** — Computational technique `Time based` (default) | `Sample based`

Computational technique to generate the type of square wave that this
block generates, either time- or sample-based. Some parameters in the dialog
box appear depending on whether you select time-based or
sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PulseType` |
| **Type**: character vector |
| **Values**: `'Time based'` | `'Sample based'` |
| **Default**: `'Time based'` |

### **Time (t)** — Source of time variable `Use simulation time` (default) | `Use external signal`

Specifies whether to use simulation time or an external signal as the
source of values for the output pulse's time variable. If you specify an
external source, the block displays an input port for connecting the source.
The output pulse differs as follows:

- `Use simulation time`: The block
  generates an output pulse where the time variable equals the
  simulation time.
- `Use external signal`: The block
  generates an output pulse where the time variable equals the value
  from the input port, which can differ from the simulation
  time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeSource` |
| **Type**: character vector |
| **Values**: `'Use simulation time'` | `'Use external signal'` |
| **Default**: `'Use simulation time'` |

### **Amplitude** — Signal amplitude `1` (default) | `scalar`

Specify the amplitude of the signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Amplitude` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Period (secs)** — Pulse period `10` (default) | `scalar`

Pulse period specified in seconds if the pulse type is time-based. If the pulse type is
sample-based, then the period is specified as the number of sample
times.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Period` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'10'` |

### **Pulse width** — Duty cycle `5` (default) | `scalar in the range [0,100]`

Duty cycle specified as the percentage of the pulse period that the signal is on if
time-based or as number of sample times if sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PulseWidth` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'5'` |

### **Phase delay (secs)** — Delay before pulse `0` (default) | `scalar`

Delay before the pulse is generated, specified in seconds, if the pulse type is
time-based or as number of sample times if the pulse type is
sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PhaseDelay` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Sample time** — Length of sample time `0` (default) | `scalar` | vector

Length of the sample time for this block in seconds. This parameter appears only if the
block's pulse type is sample-based. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if
the **Amplitude**, **Period**,
**Pulse width**, or **Phase delay**
parameter evaluates to an `N`-element row or column
vector.

- When you select this check box, the block outputs a vector of
  length `N` if any of the value parameters evaluate
  to an `N`-element row or column vector. For
  example, the block outputs a matrix of dimension
  `1-by-N` or `N-by-1`.
- When you clear this check box, the block does not output a vector
  of length `N` if any of the value parameters
  evaluate to an `N`-element row or column
  vector.

For more information on how this parameter is used, see Determine the Output Dimensions of Source Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Cannot be used inside a triggered subsystem hierarchy.

These blocks do not reference absolute time when configured for sample-based operation. In
time-based operation, they depend on absolute time.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL code generation is supported for this block with the **Pulse
type** parameter set to `Sample based` and the
**Time (t)** parameter set to `Use simulation
time`.

**Restrictions**

Connect the Pulse Generator block to the DUT ports to use it as
a source block in your model, but ensure it is not placed inside the DUT
subsystem.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
