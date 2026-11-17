---
type: simulink-block
title: 'Decision Feedback Equalizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Equalizers'
documentation_page: 'decisionfeedbackequalizer'
documentation_source_path: 'ref/decisionfeedbackequalizer.html'
language: en
---

# Decision Feedback Equalizer

## Ports
```yaml
ports:
- name: in
  summary: Input signal column vector
  direction: input
  data_types: double
- name: Desired
  summary: Training symbols column vector
  direction: input
  data_types: double
- name: Train
  summary: Train equalizer flag boolean scalar
  direction: input
  data_types: Boolean
- name: Update
  summary: Update tap weights flag 1 | 0
  direction: input
  data_types: Boolean
- name: Reset
  summary: Reset equalizer flag 1 | 0
  direction: input
  data_types: Boolean
- name: Out
  summary: Equalized symbols column vector
  direction: output
- name: Err
  summary: Error signal column vector
  direction: output
- name: w
  summary: Tap weights column vector
  direction: output
```

### Input

### **in** — Input signal column vector

Input signal, specified as a column vector. The vector length of **in**
must be equal to an integer multiple of the **Number of input
samples per symbol** parameter. For more information, see Symbol Tap Spacing.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Desired** — Training symbols column vector

Training symbols, specified as a column vector. The vector length of
**Desired** must be less than or equal to the length of input
**in**. The
**Desired** input port is ignored when the **Train** input
port is `0`.

#### Dependencies

To enable this port, set the **Adaptive
algorithm** parameter to `LMS` or
`RLS`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Train** — Train equalizer flag boolean scalar

Train equalizer flag, specified as `1` or `0`.
The block starts training when this value changes from `0` to
`1` (at the rising edge). The block trains until all symbols in the
**Desired** input
port are processed.

#### Dependencies

To enable this port, set the **Adaptive
algorithm** parameter to `LMS` or
`RLS` and select the **Enable training
control input** parameter.

**Data Types:** `Boolean`

### **Update** — Update tap weights flag `1` | `0`

Update tap weights flag, specified as `1` or
`0`. The tap weights are updated when this value is
`1`.

#### Dependencies

To enable this port, set the **Adaptive
algorithm** parameter to `CMA` and the **Source of adapt
weights flag** parameter to `Input
port`.

**Data Types:** `Boolean`

### **Reset** — Reset equalizer flag `1` | `0`

Reset equalizer flag, specified as `1` or `0`.
If **Reset** is set to `1`, the block resets the tap weights
before processing the incoming signal. The block performs initial training until all
symbols in the **Desired** input
port are processed.

#### Dependencies

To enable this port, select the **Enable reset
input****Enable reset input** parameter.

**Data Types:** `Boolean`
### Output

### **Out** — Equalized symbols column vector

Equalized symbols, returned as a column vector that has the same length as input
signal **in**.

This port is unnamed until you select the **Output error
signal** or **Output taps
weights** parameter.

### **Err** — Error signal column vector

Error signal, returned as a column vector that has the same length as input signal
**in**.

#### Dependencies

To enable this port, select the **Output error
signal** parameter.

### **w** — Tap weights column vector

Tap weights, returned as an *N*Taps-by-1
vector, where *N*Taps is equal to the sum of
the **Number of forward
taps** and **Number of feedback
taps** parameter values. **w** contains the tap weights
from the last tap weight update.

#### Dependencies

To enable this port, select the **Output taps
weights** parameter.
## Parameters
```yaml
parameters:
- name: Number of forward taps
  summary: Number of forward equalizer taps 5 (default) | positive integer
  group: ''
- name: Number of feedback taps
  summary: Number of feedback equalizer taps 3 (default) | positive integer
  group: ''
- name: Signal constellation
  summary: Signal constellation pskmod(0:3,4,pi/4) (default) | vector
  group: ''
- name: Number of input samples per symbol
  summary: Number of input samples per symbol 1 (default) | positive integer
  group: ''
- name: Adaptive algorithm
  summary: Adaptive algorithm LMS (default) | RLS | CMA
  group: ''
- name: Step size
  summary: Step size 0.01 (default) | positive scalar
  group: ''
- name: Forgetting factor
  summary: Forgetting factor 0.99 (default) | scalar in the range (0, 1]
  group: ''
- name: Initial inverse correlation matrix
  summary: Initial inverse correlation matrix 0.1 (default) | scalar | matrix
  group: ''
- name: Reference tap
  summary: Reference tap 3 (default) | positive integer
  group: ''
- name: Input signal delay (samples)
  summary: Input signal delay 0 (default) | nonnegative integer
  group: ''
- name: Source of adapt weights flag
  summary: Source of adapt tap weights request Property (default) | Input port
  group: ''
- name: Adapt tap weights
  summary: Adapt tap weights on (default) | off
  group: ''
- name: Initial tap weights source
  summary: Source for initial tap weights Auto (default) | Property
  group: ''
- name: Initial weights
  summary: Initial tap weights 0 or [0;0;1;0;0] (default) | scalar | column vector
  group: ''
- name: Tap weight update period (symbols)
  summary: Tap weight update period 1 (default) | positive integer
  group: ''
- name: Enable training control input
  summary: Enable training control input off (default) | on
  group: ''
- name: Update tap weights when not training
  summary: Update tap weights when not training on (default) | off
  group: ''
- name: Enable reset input
  summary: Enable reset input off (default) | on
  group: ''
- name: Info
  summary: Decision feedback equalizer information button
  group: ''
- name: Output error signal
  summary: Enable error signal output off (default) | on
  group: ''
- name: Output taps weights
  summary: Enable tap weights output off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Structure parameters

### **Number of forward taps** — Number of forward equalizer taps `5` (default) | positive integer

Number of forward equalizer taps, specified as a positive integer. The number of
forward equalizer taps must be greater than or equal to the value of the **Number of input samples
per symbol** parameter.

### **Number of feedback taps** — Number of feedback equalizer taps `3` (default) | positive integer

Number of feedback equalizer taps, specified as a positive integer.

### **Signal constellation** — Signal constellation `pskmod(0:3,4,pi/4)` (default) | vector

Signal constellation, specified as a vector. The default value is a QPSK
constellation generated using this code: `pskmod(0:3,4,pi/4)`.

### **Number of input samples per symbol** — Number of input samples per symbol `1` (default) | positive integer

Number of input samples per symbol, specified as a positive integer. Setting this
parameter to any number greater than `1` effectively creates a
fractionally spaced equalizer. For more information, see Symbol Tap Spacing.

#### Algorithm parameters

### **Adaptive algorithm** — Adaptive algorithm `LMS` (default) | `RLS` | `CMA`

Adaptive algorithm used for equalization, specified as one of these values:

- `LMS` — Update the equalizer tap weights using the
  Least Mean Square (LMS) Algorithm.
- `RLS` — Update the equalizer tap weights using the
  Recursive Least Square (RLS) Algorithm.
- `CMA` — Update the equalizer tap weights using the
  Constant Modulus Algorithm (CMA).

### **Step size** — Step size `0.01` (default) | positive scalar

Step size used by the adaptive algorithm, specified as a positive scalar. Increasing
the step size reduces the equalizer convergence time but causes the equalizer output
estimates to be less stable.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `LMS` or `CMA`.

### **Forgetting factor** — Forgetting factor `0.99` (default) | scalar in the range (0, 1]

Forgetting factor used by the adaptive algorithm, specified as a scalar in the range
(0, 1]. Decreasing the forgetting factor reduces the equalizer convergence time but
causes the equalizer output estimates to be less stable.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `RLS`.

### **Initial inverse correlation matrix** — Initial inverse correlation matrix `0.1` (default) | scalar | matrix

Initial inverse correlation matrix, specified as a scalar or an
*N*Taps-by-*N*Taps
matrix. *N*Taps is equal to the sum of the
**Number of forward
taps** and **Number of feedback
taps** parameter values. If you specify this value as a scalar,
*a*, the equalizer sets the initial inverse correlation matrix to
*a* times the identity matrix:
*a*(`eye`(*N*Taps)).

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `RLS`.

#### Control parameters

### **Reference tap** — Reference tap `3` (default) | positive integer

Reference tap, specified as a positive integer less than or equal to the **Number of forward
taps** parameter value. The equalizer uses the reference tap location to
track the main energy of the channel.

### **Input signal delay (samples)** — Input signal delay `0` (default) | nonnegative integer

Input signal delay in samples relative to the reset time of the equalizer, specified
as a nonnegative integer. If the input signal is a vector of length greater than 1, then
the input delay is relative to the start of the input vector. If the input signal is a
scalar, then the input delay is relative to the first call of the block and to the first
call of the block after the **Reset** input port
toggles to `1`.

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `LMS` or `RLS`.

### **Source of adapt weights flag** — Source of adapt tap weights request `Property` (default) | `Input port`

Source of the adapt tap weights request, specified as one of these values:

- `Property` — Specify this value to use the **Adaptive
  algorithm** parameter to control when the block adapts tap
  weights.
- `Input port` — Specify this value to use the **Update**
  input port to control when the block adapts tap weights.

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `CMA`.

### **Adapt tap weights** — Adapt tap weights `on` (default) | `off`

Select this parameter to adaptively update the equalizer tap weights. If this
parameter is cleared, the block keeps the equalizer tap weights unchanged.

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `CMA` and **Source of adapt
weights flag** to `Property`.

### **Initial tap weights source** — Source for initial tap weights `Auto` (default) | `Property`

Source for initial tap weights, specified as one of these values:

- `Auto` — Initialize the tap weights to the
  algorithm-specific default values, as described in the **Initial
  weights** parameter.
- `Property` — Initialize the tap weights using the
  **Initial
  weights** parameter value.

### **Initial weights** — Initial tap weights `0` or `[0;0;1;0;0]` (default) | scalar | column vector

Initial tap weights used by the adaptive algorithm, specified as a scalar or an
*N*Taps-by-1 vector.
*N*Taps is equal to the sum of the **Number of forward
taps** and **Number of feedback
taps** parameter values. The default is `0` when the
**Adaptive
algorithm** parameter is set to `LMS` or
`RLS`. The default is `[0;0;1;0;0]` when the
**Adaptive
algorithm** parameter is set to `CMA`.

If you specify **Initial weights** as a vector, the vector length
must be *N*Taps. If you specify
**Initial weights** as a scalar, the equalizer uses scalar
expansion to create a vector of length *N*Taps
with all values set to **Initial weights**.

#### Dependencies

To enable this parameter, set **Initial tap weights
source** to `Property`.

### **Tap weight update period (symbols)** — Tap weight update period `1` (default) | positive integer

Tap weight update period in symbols, specified as a positive integer. The equalizer
updates the tap weights after processing this number of symbols.

### **Enable training control input** — Enable training control input `off` (default) | `on`

Select this parameter to enable input port **Train**. If this parameter is
cleared, the block does not reenter training mode after the initial tap training.

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `LMS` or `RLS`.

### **Update tap weights when not training** — Update tap weights when not training `on` (default) | `off`

Select this parameter to use decision directed mode to update equalizer tap weights.
If this parameter is cleared, the block keeps the equalizer tap weights unchanged after
training.

#### Dependencies

To enable this parameter, set **Adaptive
algorithm** to `LMS` or `RLS`.

### **Enable reset input** — Enable reset input `off` (default) | `on`

Select this parameter to enable input port **Reset**. If this
parameter is cleared, the block does not reset the tap weights before processing the
incoming signal.

### **Info** — Decision feedback equalizer information button

Select **Info** to display decision feedback equalizer
information for applied settings.

#### Diagnostic parameters

### **Output error signal** — Enable error signal output `off` (default) | `on`

Select this parameter to enable output port **Err** containing
the equalizer error signal.

### **Output taps weights** — Enable tap weights output `off` (default) | `on`

Select this parameter to enable output port **w** containing tap
weights from the last tap weight update.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).
## Libraries

Communications Toolbox / Equalizers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Equalize modulated signals using decision feedback filtering

The Decision Feedback Equalizer block uses a decision feedback filter tap delay line with a weighted sum
to equalize modulated signals transmitted through a dispersive channel. Using an estimate of
the channel modeled as a finite input response (FIR) filter, the block processes input frames
and outputs the estimated signal.

This icon shows the block with all ports enabled for configurations that use the LMS or
RLS adaptive algorithm.

This icon shows the block with all ports enabled for configurations that use the CMA
adaptive algorithm.
