---
type: simulink-block
title: 'Pulse Waveform Library'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'pulsewaveformlibrary'
documentation_source_path: 'ref/pulsewaveformlibrary.html'
language: en
---

# Pulse Waveform Library

## Ports

### Input

### **Idx** — Waveform index positive integer

Index to select the waveform, specified as a positive integer. The
index selects the waveform from the set of waveforms defined by the
**Specification of each waveform in the library**
parameter.

**Data Types:** `double`
### Output

### **Y** — Pulse waveform samples complex-valued column vector | complex-valued matrix

Pulse waveform samples, returned as a complex-valued vector or
complex-valued matrix.

**Data Types:** `double`
**Complex Number Support:** Yes

## Parameters

### **Sample rate (Hz)** — Sample rate of the output waveform `1e6` (default) | positive scalar

Sample rate of the output waveform, specified as a positive scalar. The ratio of
**Sample rate (Hz)** to each element in the **Pulse
repetition frequency (Hz)** vector must be an integer. This restriction is
equivalent to requiring that the pulse repetition interval is an integral multiple of
the sample interval.

### **Specification of each waveform in the library** — Pulse waveforms in the library `{{'Rectangular','PRF',1e4,'PulseWidth',50e-6},{'LinearFM','PRF',1e4,'PulseWidth',50e-6,'SweepBandwidth',1e5,'SweepDirection','Up','SweepInterval','Positive'}}` (default) | cell array

Pulse waveforms, specified as a cell array. Each cell of the array
contains the specification of one waveform. Each waveform is also a cell
array containing the parameters of the
waveform.

```
{{Waveform 1 Specification},{Waveform 2 Specification},{Waveform 3 Specification}, ...}
```

This
block supports four built-in waveforms and also lets you specify custom
waveforms. Each built-in waveform specifier consists of a waveform
identifier followed by several name-value pairs that set the properties of
the waveform.

**Built-in Waveforms**

|  |  |  |
| --- | --- | --- |
| Waveform type | Waveform identifier | Waveform name-value pair arguments |
| Linear FM | `'LinearFM'` | See Linear FM Waveform Arguments |
| Phase coded | `'PhaseCoded'` | See Phase-Coded Waveform Arguments |
| Rectangular | `'Rectangular'` | See Rectangular Waveform Arguments |
| Stepped FM | `'SteppedFM'` | See Stepped FM Waveform Arguments |

You can create a custom waveform with a user-defined function. The first
input argument of the function must be the sample rate. Use a function
handle instead of the waveform identifier in the first cell of a waveform
specification. The remaining cells contain all function input arguments
except the sample rate. Specify all input arguments in the order they are
passed into the function. The function must have at least one output
argument to return the samples of each pulse in a column vector. You can
only create custom waveforms when you set **Simulate
using** to `Interpreted
Execution`.

### **Source of simulation sample time** — Source of simulation sample time `Derive from waveform parameters` (default) | `Inherit from Simulink engine`

Source of simulation sample time, specified as `Derive from waveform
parameters` or `Inherit from Simulink engine`.
When set to `Derive from waveform parameters`, the block runs
at a variable rate determined by the PRF of the selected waveform. The elapsed time is
variable. When set to `Inherit from Simulink engine`, the
block runs at a fixed rate so the elapsed time is a constant.

#### Dependencies

To enable this parameter, select the **Enable PRF selection
input** parameter.

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or `Code
Generation`. If you want your block to use the MATLAB® interpreter,
choose `Interpreted Execution`. If you want
your block to run as compiled code, choose `Code Generation`.
Compiled code requires time to compile but usually runs faster.

Interpreted execution is useful when you are developing and tuning a model. The block runs the
underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the overall
simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

## Libraries

Radar Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Library of pulse waveforms

The Pulse Waveform Library generates different types of pulse waveforms from a library
of waveforms.
