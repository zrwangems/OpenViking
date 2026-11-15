---
type: simulink-block
title: 'Sine Wave'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinewave'
language: en
---

# Sine Wave

Generate sine wave, using simulation time as time source

## Libraries

Simulink / Sources

## Description

The Sine Wave block outputs a sinusoidal waveform. The block can operate in time-based
or sample-based mode.

**Note**

This block is the same as the Sine Wave Function block that
appears in the Math Operations library. If you select `Use external
signal` for the **Time** parameter in the block
dialog box, you get the Sine Wave Function block.

### Time-Based Mode

The block calculates the output waveform.

y=amplitude×sin(frequency×time+phase)+bias.

In time-based mode, the value of the **Sample time** parameter determines
whether the block operates in continuous mode or discrete mode.

- `0` (the default) causes the block to operate in
  continuous mode.
- `>0` causes the block to operate in discrete
  mode.

For more information, see Specify Sample Time.

**Block Behavior in Continuous Mode**

When operating in continuous mode, the Sine Wave block can become
inaccurate due to loss of precision as time becomes very large.

**Block Behavior in Discrete Mode**

A **Sample time** parameter value greater than zero causes the block to
behave as if it were driving a Zero-Order Hold block whose sample
time is set to that value.

This way, you can build models with sine wave sources that are purely discrete, rather
than models that are hybrid continuous/discrete systems. Hybrid systems are
inherently more complex and as a result take more time to simulate.

In discrete mode, this block uses a differential incremental algorithm instead
of one based on absolute time. As a result, the block can be useful in models
intended to run for an indefinite length of time, such as in vibration or
fatigue testing.

The differential incremental algorithm computes the sine based on the value
computed at the previous sample time. This method uses the following
trigonometric identities:

sin(t+Δt)=sin(t)cos(Δt)+sin(Δt)cos(t)cos(t+Δt)=cos(t)cos(Δt)−sin(t)sin(Δt)

In matrix form, these identities are:

[sin(t+Δt)cos(t+Δt)]=[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)][sin(t)cos(t)]

Because Δ*t* is constant, the following expression is a constant:

[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)]

Therefore, the problem becomes one of a matrix multiplication of the value of sin(t) by a constant matrix to obtain sin(t+Δt).

Discrete mode reduces but does not eliminate the accumulation of round-off errors. This
accumulation can happen because computation of the block output at each time
step depends on the value of the output at the previous time step.

**Methods to Handle Round-Off Errors in Discrete Mode**

To handle round-off errors when the Sine Wave block operates in time-based
discrete mode, use one of these methods.

| Method | Rationale |
| --- | --- |
| Insert a Saturation block directly downstream of the Sine Wave block. | By setting saturation limits on the Sine Wave block output, you can remove overshoot due to accumulation of round-off errors. |
| Set up the Sine Wave block to use the `sin()` math library function to calculate block output.  1. On the Sine Wave block dialog box, set    **Time** to `Use    external signal` so that an input    port appears on the block icon. 2. Connect a clock signal to this input port using a    Digital    Clock block. 3. Set the sample time of the clock signal to the    sample time of the Sine Wave block. | The `sin()` math library function computes block output at each time step *independently* of output values from other time steps, preventing the accumulation of round-off errors. |

### Sample-Based Mode

Sample-based mode uses this formula to compute the output of the Sine Wave
block.

y=Asin(2π(k+o)/p)+b

- *A* is the amplitude of the sine wave.
- *p* is the number of time samples per sine wave
  period.
- *k* is a repeating integer value that ranges from 0 to
  *p*–1.
- *o* is the offset (phase shift) of the signal.
- *b* is the signal bias.

In this mode, Simulink® sets *k* equal to `0` at the first
time step and computes the block output, using the formula. At the next time step,
Simulink increments *k* and recomputes the output of the
block. When *k* reaches *p*, Simulink resets *k* to `0` before computing
the block output. This process continues until the end of the simulation.

The sample-based method of computing block output at a given time step does not depend on
the output of the previous time steps. Therefore, this mode avoids the accumulation
of round-off errors. Sample-based mode supports reset semantics in subsystems that
offer it. For example, if a Sine Wave block is in a resettable
subsystem that receives a reset trigger, the repeating integer `k`
resets and the block output resets to its initial condition.

## Ports

### Output

### **Port\_1** — Sine wave output signal scalar | vector

Output sine wave signal created based on the block parameter
values.

**Data Types:** `double`

## Parameters

### **Sine type** — Type of sine wave `Time based` (default) | `Sample based`

Specify the type of sine wave that this block generates. Some parameters in the dialog
box appear depending on whether you select time-based or
sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SineType` |
| **Type**: character vector |
| **Values**: `'Time based'` | `'Sample based'` |
| **Default**: `'Time based'` |

### **Time (t)** — Source of time variable `Use simulation time` (default) | `Use external signal`

Specify whether to use simulation time as the source of values for the
time variable, or an external source. If you specify an external time
source, the block creates an input port for the time source. When you select
an external time source, the block is the same as the Sine Wave
Function block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeSource` |
| **Type**: character vector |
| **Values**: `'Use simulation time'` | `'Use external signal'` |
| **Default**: `'Use simulation time'` |

### **Amplitude** — Amplitude of the sine wave `1` (default) | scalar | vector

Specify the amplitude of the output sine wave signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Amplitude` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Bias** — Constant added to sine wave `0` (default) | scalar | vector

Specify the constant value added to the sine to produce the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Bias` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Frequency (rad/sec)** — Frequency of sine wave `1` (default) | scalar | vector

Specify the frequency, in rad/sec.

#### Dependencies

To enable this parameter, set **Sine type** to
`Time based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Frequency` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Phase (rad)** — Phase shift of sine wave `0` (default) | scalar | vector

Specify the phase shift of the sine wave.

You cannot configure this parameter to appear in the generated code as a
tunable global variable if you set **Time (t)** to
`Use simulation time`. For example, if you set
**Default parameter behavior** to
`Tunable` or apply a storage class to a
`Simulink.Parameter` object, the
**Phase** parameter does not appear in the generated
code as a tunable global variable.

To generate code so that you can tune the phase during execution, set
**Time (t)** to `Use external
signal`. You can provide your own time input signal or use
a Digital Clock block to generate the time signal. For an
example, see Tune Phase Parameter of Sine Wave Block During Code Execution (Simulink Coder).

#### Dependencies

To enable this parameter, set **Sine type** to
`Time based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Phase` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Samples per period** — Samples per period `0` (default) | `integer scalar` | `integer vector`

Specify the number of samples per period.

#### Dependencies

To enable this parameter, set **Sine type** to
`Sample based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Samples` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'10'` |

### **Number of offset samples** — Offset in number of sample times `0` (default) | `integer scalar` | `integer vector`

Specify the offset (discrete phase shift) in number of sample times.

#### Dependencies

To enable this parameter, set **Sine type** to
`Sample based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Offset` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Sample time** — Sample period `0` (default) | scalar | vector

Specify the sample period in seconds. The default is `0`. If the sine
type is sample-based, the sample time must be greater than 0. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Interpret vector parameters as 1-D** — Output dimensions for one-row or one-column matrices `off` (default) | `on`

Specify the output dimensions to be a 1-D vector signal when other parameters are one-row
and one-column matrices. If you do not select this box, the block outputs a
signal of the same dimensionality as the numeric parameters. See Determine the Output Dimensions of Source Blocks. This
parameter is not available when an external signal specifies time. In this
case, if numeric parameters are column or row matrix values, the output is a
1-D vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VectorParams1D` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Depends on absolute time when placed inside a triggered subsystem hierarchy. These blocks
do not reference absolute time when configured for sample-based operation. In
time-based operation, they depend on absolute time.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL code generation from this block supports:

- Sample-based sine waves.
- `Use simulation time` as the source of values
  for the time variable.
- Scalar values for parameters **Amplitude**,
  **Bias**, **Samples per period**,
  **Number of offset samples**, and **Sample
  time**.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| General | |
| --- | --- |
| **MapToRAM** | Map lookup tables to RAM. The default is `inherit`. See MapToRAM (HDL Coder). |

## Version History

**Introduced before R2006a**
