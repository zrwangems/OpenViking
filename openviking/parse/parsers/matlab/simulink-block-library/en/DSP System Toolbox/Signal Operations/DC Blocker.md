---
type: simulink-block
title: 'DC Blocker'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'dcblocker'
documentation_source_path: 'ref/dcblocker.html'
language: en
---

# DC Blocker

## Ports

### Input

### **Input** — Input signal scalar | vector | matrix

Specify the input signal that contains the DC component as a scalar, vector, or a
matrix.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Output signal with no DC component scalar | vector | matrix

Output signal with the DC component removed. When the output is fixed-point, it is
signed only.

The size, data type, and complexity of the output signal are the same as that of the
input signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Algorithm for estimating DC offset** — Algorithm for estimating DC offset `IIR` (default) | `FIR` | `CIC` | `Subtract mean`

Specify the algorithm used for estimating the DC offset. Select from the
following:

- `IIR` uses a recursive estimate based on
  a narrow, lowpass elliptic filter. This algorithm typically uses
  less memory than FIR and is more efficient.
- `FIR` uses a nonrecursive, moving-average
  estimate. This algorithm typically uses more memory than IIR and is
  less efficient.
- `CIC` uses a lowpass filter that does not
  employ any multipliers. If the algorithm is
  `CIC`, then fixed-point data must be
  input to the DC Blocker.
- `Subtract mean` computes the means of the
  columns of the input matrix and subtracts the means from the input.
  This method does not retain state between inputs. For example, if
  the input is `[1 2 3 4; 3 4 5 6]`, then the
  DC Blocker block in `Subtract
  mean` mode outputs `[-1 -1 -1 -1; 1 1 1
  1]`.

### **Normalized bandwidth of lowpass IIR or CIC filter** — Normalized bandwidth `0.001` (default) | real scalar in the range (0 1)

Specify the normalized filter bandwidth as a real scalar greater than 0
and less than 1.

#### Dependencies

The DC Blocker uses this parameter only when the
estimation algorithm is set to `IIR` or
`CIC`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Order of lowpass IIR elliptic filter** — Order of lowpass IIR elliptic filter `6` (default) | integer greater than 3

Specify the filter order of the lowpass IIR elliptic filter as an integer
greater than 3.

#### Dependencies

The DC Blocker uses this parameter only when the
estimation algorithm is set to `IIR`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Number of past input samples for FIR algorithm** — Number of past input samples for FIR algorithm `50` (default) | positive integer

Specify, as a positive integer, the number of samples to use when the
estimation algorithm is set to `FIR`.

#### Dependencies

The DC Blocker uses this parameter only when the
estimation algorithm is set to `FIR`.

**Data Types:** `single` | `double`

### **View Filter Response** — Visualize frequency response button

Opens the `fvtool` and displays the magnitude response
of the DC Blocker. The response is based on the block
parameters. Changes made to these parameters update
`fvtool`.

To update the magnitude response while `fvtool` is
running, modify the block parameters and click
**Apply**.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Signal Operations Communications Toolbox / Comm Filters Communications Toolbox / RF Impairments Correction DSP System Toolbox HDL Support / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Excludes CIC algorithm for estimating DC offset. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The DC Blocker block supports SIMD code generation using Intel AVX2 code
replacement library when the input signal has a data type of
`single` or `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**Note**

For a DC Blocker optimized for HDL code generation, see High Performance DC Blocker for FPGA (DSP HDL Toolbox). The DSP HDL Toolbox™ block provides an HDL-optimized algorithm with hardware-friendly
control signals and simulates the latency of the HDL algorithm in Simulink.

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

**Complex Data Support**

This block supports code generation for complex signals.

## Version History

**Introduced in R2014a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Block DC component

The DC Blocker block removes the DC component of the input signal.

This block supports C/C++ code generation and SIMD code generation. For details, see
Code Generation.
