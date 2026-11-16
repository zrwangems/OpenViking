---
type: simulink-block
title: 'Stretch Processor'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'stretchprocessor'
documentation_source_path: 'ref/stretchprocessor.html'
language: en
---

# Stretch Processor

## Ports

### Input

### **X** — Input signal *M*-by-*P* complex-valued matrix

Input signal, specified as an
*M*-by-*P* complex-valued array.
*M* is the number of samples and
*P* is the number of pulses.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **PRF** — Pulse repetition frequency positive scalar

Pulse repetition frequency of current pulse, specified as a positive
scalar.

#### Dependencies

To enable this port, set the **Specify PRF as**
parameter to `Input port`.

**Data Types:** `double`
### Output

### **Y** — Stretch processed signal *M*-by-*P* complex-valued matrix

Stretch processed signal, returned as an
*M*-by-*P* complex-valued array.
*M* is the number of samples and
*P* is the number of pulses.

**Data Types:** `double`
**Complex Number Support:** Yes

## Parameters

### **Pulse width (s)** — Time duration of pulse `50e-6` (default) | positive scalar

The duration of each pulse, specified as a positive scalar. Set the product of
**Pulse width (s)** and **Pulse repetition
frequency** to be less than or equal to one. This restriction ensures that
the pulse width is smaller than the pulse repetition interval. Units are in
seconds.

**Example:** `300e-6`

### **Specify PRF as** — Source of PRF value `Property` (default) | `Auto` | `Input port`

Source of PRF value for the stretch processor, specified as
`Property`, `Auto`, or
`Input port`. When set to
`Property`, the **Pulse repetition frequency
(Hz)** parameter sets the PRF. When set to `Input
port`, pass in the PRF using the `PRF` input port.
When set to `Auto`, PRF is computed from the number of rows in
the input signal.

.

### **Pulse repetition frequency (Hz)** — Pulse repetition frequency `1e4` (default) | positive scalar

Pulse repetition frequency, PRF, specified as a positive scalar. Units are in Hertz.
Set this parameter to the same value set in any `Waveform` library
block used in the simulation.

#### Dependencies

To enable this parameter, set the **Specify PRF as** parameter to
`Property`.

### **FM sweep slope (Hz/s)** — Slope of linear FM sweep `2e9` (default) | scalar

Slope of the linear FM sweeping as a scalar, specified as a scalar. Units
are in Hertz per second.

**Example:** `1e3`

### **FM sweep interval** — Direction of FM sweep `Positive` (default) | `Symmetric`

FM sweep interval, specified as `Positive` or
`Symmetric`. If you set this parameter value to
`Positive`, the waveform sweeps the frequency
bandwidth between *0* and *B*, where
*B* is the frequency bandwidth. If you set this
parameter value to `Symmetric`, the waveform sweeps
in the interval between *–B/2* and
*B/2*.

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`. Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Reference range (m)** — Center of ranges of interest `5000` (default) | positive scalar

Center of ranges of interest, specified as a positive scalar. The
reference range must be within the unambiguous range of one pulse. Units are
in meters.

**Example:** `10e3`

### **Reference span (m)** — Span of ranges of interest `500` (default) | positive scalar

Span of ranges of interest, specified as a positive scalar. The span of
ranges is centered on the range specified by the **Reference range
(m)** parameter. Units are in meters.

**Example:** `1e3`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

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

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |

## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Stretch processor for linear FM waveforms

The Stretch Processor block applies stretch processing on a linear FM
waveform. Also known as dechirping, stretch processing is an alternative to matched
filtering for linear FM waveforms.
