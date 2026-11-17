---
type: simulink-block
title: 'Limiter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Dynamic Range Control'
documentation_page: 'limiter'
documentation_source_path: 'ref/limiter.html'
language: en
---

# Limiter

## Ports
```yaml
ports:
- name: x
  summary: Input signal 1-D vector | matrix
  direction: input
  data_types: single | double
- name: T
  summary: Threshold (dB) scalar
  direction: input
  data_types: single | double
- name: K
  summary: Knee width (dB) scalar
  direction: input
  data_types: single | double
- name: AT
  summary: Attack time (s) scalar
  direction: input
  data_types: single | double
- name: RT
  summary: Release time (s) scalar
  direction: input
  data_types: single | double
- name: Y
  summary: Output signal matrix
  direction: output
  data_types: single | double
- name: G
  summary: Gain applied to each input sample matrix
  direction: output
  data_types: single | double
```

### Input

### **x** — Input signal 1-D vector | matrix

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a single
  channel.

This port is unnamed unless you specify additional input ports.

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
### Output

### **Y** — Output signal matrix

The Limiter block outputs a signal with the same
data type as the input signal. The size of the output depends on the
size of the input:

- Matrix input –– The block outputs a matrix the same size and data type as the input
  signal.
- 1-D vector input –– The block outputs an *N*-by-1 matrix (column vector),
  where *N* is the number of elements in the 1-D
  vector.

This port is unnamed until you select the **Output gain
(dB)** parameter.

**Data Types:** `single` | `double`

### **G** — Gain applied to each input sample matrix

#### Dependencies

To enable this port, select the **Output gain (dB)** parameter.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Threshold (dB)
  summary: Operation threshold –10 (default) | scalar in the range –50 to 0 inclusive
  group: ''
- name: Knee width (dB)
  summary: Transition area in the limiter characteristic 0 (default) | scalar in the range 0 to 20 inclusive
  group: ''
- name: View static characteristic
  summary: Open static characteristic plot of dynamic range limiter button
  group: ''
- name: Attack time (s)
  summary: Time for applied gain to ramp up 0 (default) | scalar in the range 0 to 4 inclusive
  group: ''
- name: Release time (s)
  summary: Time for applied gain to ramp down 0.2 (default) | scalar in the range 0 to 4 inclusive
  group: ''
- name: Make-up gain mode
  summary: Make-up gain mode Property (default) | Auto
  group: ''
- name: Make-up gain (dB)
  summary: Applied make-up gain 0 (default) | scalar in the range –10 to 24 inclusive
  group: ''
- name: Inherit sample rate from input
  summary: Specify source of input sample rate on (default) | off
  group: ''
- name: Input sample rate (Hz)
  summary: Specify input sample rate 44100 (default) | positive scalar
  group: ''
- name: Output gain (dB)
  summary: Gain applied on each input sample off (default) | on
  group: ''
- name: Sidechain
  summary: Enable sidechain input off (default) | on
  group: ''
- name: Simulate using
  summary: Specify type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

If a parameter is listed as tunable, then you can change its value during
simulation.

#### Main Tab

### **Threshold (dB)** — Operation threshold `–10` (default) | scalar in the range –50 to 0 inclusive

*Operation threshold* is the level above which gain
is applied to the input signal.

To specify **Threshold (dB)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Knee width (dB)** — Transition area in the limiter characteristic `0` (default) | scalar in the range 0 to 20 inclusive

For soft knee characteristics, the transition area is defined by the
relation

y=x−(x−T+W2)2(2×W)

for the range (2×|x−T|)≤W, where

- *y* is the output level in dB.
- *x* is the input level in dB.
- *T* is the threshold in dB.
- *W* is the knee width in dB.

To specify **Knee width (dB)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **View static characteristic** — Open static characteristic plot of dynamic range limiter button

The plot is updated automatically when parameters of the
Limiter block change.

**Tunable:** Yes

### **Attack time (s)** — Time for applied gain to ramp up `0` (default) | scalar in the range 0 to 4 inclusive

*Attack time* is the time the limiter gain takes to
rise from 10% to 90% of its final value when the input goes above the
threshold. The **Attack time (s)** parameter smooths the
applied gain curve.

To specify **Attack time (s)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Release time (s)** — Time for applied gain to ramp down `0.2` (default) | scalar in the range 0 to 4 inclusive

*Release time* is the time the limiter gain takes to
drop from 90% to 10% of its final value when the input goes below the
threshold. The **Release time (s)** parameter smooths the
applied gain curve.

To specify **Release time (s)** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

### **Make-up gain mode** — Make-up gain mode `Property` (default) | `Auto`

- `Property` –– Make-up gain is set to the
  value specified by the **Make-up gain (dB)**
  parameter.

- `Auto` –– Make-up gain is applied at the
  output of the Limiter block such that a steady-state
  0 dB input has a 0 dB output.

**Tunable:** No

### **Make-up gain (dB)** — Applied make-up gain `0` (default) | scalar in the range –10 to 24 inclusive

*Make-up gain* compensates for gain lost during
limiting. It is applied at the output of the Limiter
block.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Make-up gain
mode** parameter to
`Property`.

### **Inherit sample rate from input** — Specify source of input sample rate `on` (default) | `off`

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, specify the sample rate in
the **Input sample rate (Hz)** parameter.

**Tunable:** No

### **Input sample rate (Hz)** — Specify input sample rate `44100` (default) | positive scalar

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
**SC** port enables dynamic range limiting of the input
signal **x** using a separate sidechain signal.

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

Dynamic range limiter

The Limiter block performs dynamic range limiting independently across each
input channel. Dynamic range limiting suppresses the volume of loud sounds that cross a
given threshold. The block uses specified attack and release times to achieve a smooth
applied gain curve.
