---
type: simulink-block
title: 'DFEClkFwd'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'dfeclkfwd'
documentation_source_path: 'ref/dfeclkfwd.html'
language: en
---

# DFEClkFwd

## Ports

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal, can be a sample-by-sample signal specified as a scalar, or
an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Estimated channel output scalar | vector

Estimated channel output. If the input signal is a sample-by-sample signal
specified as a scalar, the output is also scalar. If the input signal is an impulse
response vector signal, the output is also a vector.

**Data Types:** `double`

## Parameters

### DFE

### **Mode** — DFE operating mode `Fixed` (default) | `Off` | `Adapt`

DFE operating mode:

- `Off` — DFE is bypassed and the input
  waveform remains unchanged.
- `Fixed` — DFE applies the input DFE tap
  weights specified in **Initial tap weights (V)** to the input
  waveform.
- `Adapt` — The DFE block finds the optimum
  DFE tap values for the best eye height opening for statistical analysis. During
  time domain simulation, the block uses the adapted values as the starting point
  and applies them to the input waveform. For more information, see Statistical Analysis in SerDes Systems.

#### Programmatic Use

- Use `get_param(gcb,'Mode')` to view the current DFEClkFwd
  **Mode**.
- Use `set_param(gcb,'Mode',value)` to set DFEClkFwd to a
  specific **Mode**.

### **Initial tap weights (V)** — Initial DFE tap weights `[0 0 0 0]` (default) | row vector

Initial DFE tap weights, specified as a row vector in volts. The length of the
vector specifies the number of DFE taps. The vector element value specifies the
strength of the tap at that element position. Setting a vector element value to zero
only initializes the tap.

You can use a valid MATLAB expression to evaluate the **Initial tap
weights (V)** row vector.

**Example:** `set_param(gcb,'TapWeights',"zeros(1,100)")` creates a
DFE with 100 taps.

#### Programmatic Use

- Use `get_param(gcb,'TapWeights')` to view the current
  value of DFEClkFwd **Initial tap weights (V)**.
- Use `set_param(gcb,'TapWeights',value)` to set DFEClkFwd
  to a specific **Initial tap weights (V)** vector value.

**Data Types:** `double`

### **Adaptive gain** — Controls DFE tap weight update rate `9.6e-5` (default) | positive real scalar

Controls DFE tap weight update rate, specified as a unitless positive real scalar.
Increasing the value of **Adaptive gain** leads to a faster
convergence of DFE adaptation at the expense of more noise in DFE tap values.

#### Programmatic Use

- Use `get_param(gcb,'EqualizationGain')` to view the
  current DFEClkFwd **Adaptive gain** value.
- Use `set_param(gcb,'EqualizationGain',value)` to set
  DFEClkFwd to a specific value of **Adaptive gain**.

**Data Types:** `double`

### **Adaptive step size (V)** — DFE adaptive step resolution `1e-06` (default) | nonnegative real scalar | nonnegative real-valued row vector

DFE adaptive step resolution, specified as a nonnegative real scalar or a
nonnegative real-valued row vector in volts. Specify as a scalar to apply to all the
DFE taps or as a vector that has the same length as the **Initial tap weights
(V)**.

**Adaptive step size (V)** specifies the minimum DFE tap change
from one time step to the next to mimic hardware limitations. Setting
**Adaptive step size (V)** to `0` yields DFE tap
values without any resolution limitation.

#### Programmatic Use

- Use `get_param(gcb,'EqualizationStep')` to view the
  current DFEClkFwd **Adaptive step size (V)** value.
- Use `set_param(gcb,'EqualizationStep',value)` to set
  DFEClkFwd to a specific value of **Adaptive step size
  (V)**.

**Data Types:** `double`

### **Minimum DFE tap value (V)** — Minimum value of adapted taps `-1` (default) | real scalar | real-valued row vector

Minimum value of the adapted taps, specified as a real scalar or a real-valued row
vector in volts. Specify as a scalar to apply to all the DFE taps or as a vector that
has the same length as the **Initial tap weights (V)**.

#### Programmatic Use

- Use `get_param(gcb,'MinimumTap')` to view the current
  DFEClkFwd **Minimum DFE tap value (V)** value.
- Use `set_param(gcb,'MinimumTap',value)` to set DFEClkFwd
  to a specific value of **Minimum DFE tap value (V)**.

**Data Types:** `double`

### **Maximum DFE tap value (V)** — Maximum value of adapted taps `1` (default) | nonnegative real scalar | nonnegative real-valued row vector

Maximum value of the adapted taps, specified as a nonnegative real scalar or a
nonnegative real-valued row vector in volts. Specify as a scalar to apply to all the
DFE taps or as a vector that has the same length as the **Initial tap weights
(V)**.

#### Programmatic Use

- Use `get_param(gcb,'MaximumTap')` to view the current
  DFEClkFwd **Maximum DFE tap value (V)** value.
- Use `set_param(gcb,'MaximumTap',value)` to set DFEClkFwd
  to a specific value of **Maximum DFE tap value (V)**.

**Data Types:** `double`

### **2x tap weights** — Multiply DFE tap weights by a factor of two on (default) | off

Select to multiply the DFE tap weights by a factor of two.

The output of the slicer in the DFEClkFwd block from the
SerDes Toolbox™ is `[-0.5 0.5]`. But some industry applications require
the slicer output to be `[-1 1]`. **2x tap weights**
allows you to quickly double the DFE tap weights to change the slicer
reference.

### CDR

### **Phase offset (symbol time)** — Manual clock phase offset `0` (default) | real scalar in the range [−0.5, 0.5]

Manual clock phase offset to move the recovered clock phase, specified as a real
scalar in the range [-0.5, 0.5] in the fraction of symbol time. **Phase offset
(symbol time)** is used to manually shift the clock probability
distribution function (PDF) for a better bit error rate (BER).

#### Programmatic Use

- Use `get_param(gcb,'PhaseOffset')` to view the current
  DFEClkFwd **Phase offset (symbol time)** value.
- Use `set_param(gcb,'PhaseOffset',value)` to set DFEClkFwd
  to a specific value of **Phase offset (symbol time)**.

**Data Types:** `double`

### **Reference offset (ppm)** — Reference clock offset impairment `0` (default) | real scalar in the range [−300, 300]

Reference clock offset impairment, specified as a real scalar in the range [−300,
300] in parts per million (ppm). **Reference offset (ppm)** is the
deviation between transmitter oscillator frequency and receiver oscillator
frequency.

#### Programmatic Use

- Use `get_param(gcb,'ReferenceOffset')` to view the
  current DFEClkFwd **Reference offset (ppm)** value.
- Use `set_param(gcb,'ReferenceOffset',value)` to set
  DFEClkFwd to a specific value of **Reference offset
  (ppm)**.

**Data Types:** `double`

### **Early/late count threshold** — Early or late CDR count threshold to trigger phase update `5` (default) | positive real integer ≥5

Early or late CDR count threshold to trigger a phase update, specified as a
unitless positive real integer ≥5. Increasing the value of **Early/late count
threshold** provides a more stable output clock phase at the expense of
convergence speed. Because the bit decisions are made at the clock phase output, a
more stable clock phase has a better bit error rate (BER).

**Early/late count threshold** also controls the bandwidth of the
CDR.

#### Programmatic Use

- Use `get_param(gcb,'Count')` to view the current
  DFEClkFwd
  **Early/late count threshold** value.
- Use `set_param(gcb,'Count',value)` to set
  DFEClkFwd to a specific value of **Early/late count
  threshold**.

**Data Types:** `double`

### **Step (symbol time)** — Clock phase resolution `0.005` (default) | real scalar

Clock phase resolution of the recovered clock, specified as a real scalar in
fraction of symbol time. **Step (symbol time)** is the inverse of the
number of phase adjustments in the CDR. If the CDR has 128 steps of phase adjustment,
the **Step (symbol time)** value is 1/128.

#### Programmatic Use

- Use `get_param(gcb,'ClockStep')` to view the current
  DFEClkFwd **Step (symbol time)** value.
- Use `set_param(gcb,'ClockStep',value)` to set DFEClkFwd
  to a specific value of **Step (symbol time)**.

**Data Types:** `double`

### **Sensitivity (V)** — Sampling latch metastability voltage `0` (default) | real scalar

Sampling latch metastability voltage, specified as a real scalar in volts. If the
data sample voltage lies within the region of (±**Sensitivity (V)**),
there is a 50% probability of bit error.

#### Programmatic Use

- Use `get_param(gcb,'Sensitivity')` to view the current
  DFEClkFwd **Sensitivity (V)** value.
- Use `set_param(gcb,'Sensitivity',value)` to set DFEClkFwd
  to a specific value of **Sensitivity (V)**.

**Data Types:** `double`

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

DFE with Clock Forwarding in the receiver AMI model

In a parallel link channel, a separate clock (or strobe) signal is sent along with the
data signals, which is used to latch each individual data bit. This is known as
clock-forwarding. The IBIS-AMI Specification describes a mechanism by which the clock
waveform, or recovered clock times, can be passed to the data AMI receiver model to allow the
model maker access to the clock. This enables the receiver model to include clock phase noise,
clock tree delays, phase interpolators, and so on.

You can use the DFEClkFwd block to simulate and generate the clock
forwarding DLLs according to the IBIS-AMI Specification.
