---
type: simulink-block
title: 'Expander'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Dynamic Range Control'
documentation_page: 'expander'
documentation_source_path: 'ref/expander.html'
language: en
---

# Expander

## Ports

### Input

### **x** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a single
  channel.

This port is unnamed unless you specify additional input ports.

**Data Types:** `single` | `double`

### **R** — Ratio scalar

#### Dependencies

To enable this port, select **Specify from input
port** for the Ratio parameter.

**Data Types:** `single` | `double`

### **T** — Threshold (dB) scalar

#### Dependencies

To enable this port, select **Specify from input
port** for the Threshold (dB) parameter.

**Data Types:** `single` | `double`

### **K** — Knee width (dB) scalar

#### Dependencies

To enable this port, select **Specify from input
port** for the Knee width (dB) parameter.

**Data Types:** `single` | `double`

### **AT** — Attack time (s) scalar

#### Dependencies

To enable this port, select **Specify from input
port** for the Attack time (s) parameter.

**Data Types:** `single` | `double`

### **RT** — Release time (s) scalar

#### Dependencies

To enable this port, select **Specify from input
port** for the Release time (s)
parameter.

**Data Types:** `single` | `double`

### **HT** — Hold time (s) scalar

#### Dependencies

To enable this port, select **Specify from input
port** for the Hold time (s) parameter.

**Data Types:** `single` | `double`
### Output

### **Y** — Output signal matrix

The Expander block outputs a signal with the same data
type as the input signal. The size of the output depends on the size of
the input:

- Matrix input –– The block outputs a matrix the same size and
  data type as the input signal.
- 1-D vector input –– The block outputs an
  *N*-by-1 matrix (column vector), where
  *N* is the number of elements in the 1-D
  vector.

This port is unnamed until you select the **Output gain
(dB)** parameter.

**Data Types:** `single` | `double`

### **G** — Gain applied to each input sample matrix

#### Dependencies

To enable this port, select the **Output gain
(dB)** parameter.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

#### Main Tab

### **Ratio** — Expansion ratio `5` (default) | scalar in the range 1 to 50 inclusive

*Expansion ratio* is the input/output ratio for
signals that undershoot the operation threshold.

Assuming a hard knee characteristic and a steady-state input such that
*x*[*n*] dB < **Threshold
(dB)**, the expansion ratio is defined as R=(y[n]−T)(x[n]−T), where

- *R* is the expansion ratio.
- *y*[*n*] is the output
  signal in dB.
- *x*[*n*] is the input signal
  in dB.
- *T* is the threshold in dB.

To specify **Ratio** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Threshold (dB)** — Operation threshold `–10` (default) | scalar in the range –140 to 0 inclusive

*Operation threshold* is the level below which gain
is applied to the input signal.

To specify **Threshold (dB)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Knee width (dB)** — Transition area in the compression characteristic `0` (default) | scalar in the range 0 to 20

For soft knee characteristics, the transition area is defined by the relation

y=x+(1−R)×(x−T−W2)2(2×W)

for the range (2×|x−T|)≤W, where

- *y* is the output level in dB.
- *x* is the input level in dB.
- *R* is the expansion ratio.
- *T* is the threshold in dB.
- *W* is the knee width in dB.

To specify **Knee width (dB)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **View static characteristic** — Open static characteristic plot of dynamic range expander button

The plot is updated automatically when parameters of the
Expander block change.

**Tunable:** Yes

### **Attack time (s)** — Time for applied gain to ramp up `0.05` (default) | scalar in the range 0 to 4 inclusive

*Attack time* is the time the expander gain takes to
rise from 10% to 90% of its final value when the input goes below the
threshold. The **Attack time (s)** parameter smooths the
applied gain curve.

To specify **Attack time (s)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Release time (s)** — Time for applied gain to ramp down `0.2` (default) | scalar in the range 0 to 4 inclusive

*Release time* is the time the expander gain takes to
drop from 90% to 10% of its final value when the input goes above the
threshold. The **Release time (s)** parameter smooths the
applied gain curve.

To specify **Release time (s)** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

### **Hold time (s)** — Time during which applied gain holds steady `0.05` (default) | scalar in the range 0 to 4 inclusive

*Hold time* is the period for which the (negative)
gain is held before starting to decrease towards its steady state value when
the input level drops below the threshold.

To specify **Hold time (s)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Inherit sample rate from input** — Specify source of input sample rate `on` (default) | `off`

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, specify the sample rate in
the **Input sample rate (Hz)** parameter.

**Tunable:** No

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | positive scalar

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

#### Advanced Tab

### **Output gain (dB)** — Gain applied on each input sample `off` (default) | `on`

When you select this parameter, an additional output port,
**G**, is added to the block. The
**G** port outputs the gain applied on each input
channel in dB.

**Tunable:** No

### **Sidechain** — Enable sidechain input `off` (default) | `on`

When you select this parameter, an additional input port
**SC** is added to the block. The
**SC** port enables dynamic range expansion of the
input signal **x** using a separate sidechain
signal.

The datatype and (frame) length input to the **SC** port
must be the same as the input to the **x** port.

The number of channels of the sidechain input must be equal to the number
of channels of `x` or be equal to one.

- `Sidechain channel count is equal to one` ––
  The computed gain, `G`, based on
  this channel is applied to all channels of `x`.
- `Sidechain channel count is equal to channel count of``x` –– The
  computed gain, `G`, for each
  sidechain channel is applied to the corresponding channel of
  `x`.

**Tunable:** No

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` –– Simulate model
  using the MATLAB® interpreter. This option shortens startup time and has
  a simulation speed comparable to `Code
  generation`. In this mode, you can debug the source
  code of the block.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.

**Tunable:** No

## Libraries

Audio Toolbox / Dynamic Range Control

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Dynamic range expander

The Expander block performs dynamic range expansion independently
across each input channel. Dynamic range expansion attenuates the volume of quiet sounds
below a given threshold. The block uses specified attack, release, and hold times to
achieve a smooth applied gain curve.
