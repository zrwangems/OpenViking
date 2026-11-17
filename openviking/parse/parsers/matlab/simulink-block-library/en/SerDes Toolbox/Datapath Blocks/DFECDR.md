---
type: simulink-block
title: 'DFECDR'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'dfecdr'
documentation_source_path: 'ref/dfecdr.html'
language: en
---

# DFECDR

## Ports
```yaml
ports:
- name: WaveIn
  summary: Input baseband signal scalar | vector
  direction: input
  data_types: double
- name: WaveOut
  summary: Estimated channel output scalar | vector
  direction: output
  data_types: double
```

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal. The input signal can be a sample-by-sample signal specified
as a scalar, or an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Estimated channel output scalar | vector

Estimated channel output. If the input signal is a sample-by-sample signal
specified as a scalar, the output is also scalar. If the input signal is an impulse
response vector signal, the output is also a vector.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Mode
  summary: DFE operating mode Adapt (default) | Off | Fixed
  group: DFE
- name: Initial tap weights (V)
  summary: Initial DFE tap weights [0 0 0 0] (default) | row vector
  group: DFE
- name: Adaptive gain
  summary: Controls DFE tap weight update rate 9.6e-5 (default) | positive real scalar
  group: DFE
- name: Adaptive step size (V)
  summary: DFE adaptive step resolution 1e-06 (default) | nonnegative real scalar | nonnegative real-valued row vector
  group: DFE
- name: Minimum DFE tap value (V)
  summary: Minimum value of adapted taps -1 (default) | real scalar | real-valued row vector
  group: DFE
- name: Maximum DFE tap value (V)
  summary: Maximum value of adapted taps 1 (default) | nonnegative real scalar | nonnegative real-valued row vector
  group: DFE
- name: 2x tap weights
  summary: Multiply DFE tap weights by a factor of two off (default) | on
  group: DFE
- name: CDR Mode
  summary: Determine CDR order 1st order (default) | 2nd order
  group: CDR
  block_parameter: CDRMode
  type: character vector
  values: 1st order | 2nd order
  default: 1st order
- name: Phase Detector
  summary: Clock phase detector option BangBang (default) | BaudRateTypeA
  group: CDR
  block_parameter: PhaseDetector
  type: character vector
  values: BangBang | BaudRateTypeA
  default: BangBang
- name: Phase Offset (symbol time)
  summary: Clock phase offset 0 (default) | real scalar in the range [-0.5,0.5]
  group: CDR
  block_parameter: PhaseOffset
  type: character vector
  values: real scalar in the range [-0.5,0.5]
  default: '0'
- name: Reference offset (ppm)
  summary: Reference clock offset impairment 0 (default) | real scalar in the range [0, 300]
  group: CDR
  block_parameter: ReferenceOffset
  type: character vector
  values: real scalar in the range [0, 300]
  default: '0'
- name: Early/late count threshold
  summary: Early or late CDR count threshold to trigger phase update 16 (default) | real positive integer ≥5
  group: CDR
  block_parameter: Count
  type: character vector
  values: real positive integer ≥5
  default: '16'
- name: Step (symbol time)
  summary: Clock phase resolution 0.0078 (default) | real scalar
  group: CDR
  block_parameter: Step
  type: character vector
  values: real scalar
  default: '0.0078'
- name: Frequency tracking gain
  summary: Internal gain for frequency tracking 0.00048828125 (default) | nonnegative real scalar
  group: CDR
  block_parameter: FrequencyStep
  type: character vector
  values: nonnegative real scalar
  default: '0.00048828125'
- name: Frequency tracking update
  summary: Frequency tracking update 16 (default) | nonnegative integer scalar
  group: CDR
  block_parameter: FrequencyCount
  type: character vector
  values: nonnegative real scalar
  default: '16'
- name: Frequency step ramp
  summary: Number of symbol times required for initial internal frequency tracking gain to reach specified value 3000 (default)
    | nonnegative integer scalar
  group: CDR
  block_parameter: FrequencyStepRamp
  type: character vector
  values: nonnegative real scalar
  default: '3000'
- name: Sensitivity (V)
  summary: Sampling latch metastability voltage 0 (default) | real scalar
  group: CDR
  block_parameter: Sensitivity
  type: character vector
  values: real scalar
  default: '0'
- name: Mode
  summary: Include Mode parameter in IBIS-AMI model on (default) | off
  group: CDR
- name: Tap weights
  summary: Include Tap weights parameter in IBIS-AMI model on (default) | off
  group: CDR
- name: Phase Offset
  summary: Include Phase Offset parameter in IBIS-AMI model on (default) | off
  group: CDR
- name: Reference offset
  summary: Include Reference offset parameter in IBIS-AMI model on (default) | off
  group: CDR
```

### DFE

### **Mode** — DFE operating mode `Adapt` (default) | `Off` | `Fixed`

DFE operating mode:

- `Off` — DFECDR is bypassed and the input
  waveform remains unchanged.
- `Fixed` — DFECDR applies the input DFE tap
  weights specified in **Initial tap weights (V)** to the input
  waveform.
- `Adapt` — The Init subsystem calls to the DFECDR
  System object™. The DFECDR System object finds the optimum DFE tap values for the best eye height opening
  for statistical analysis. During time domain simulation, DFECDR uses the adapted
  values as the starting point and applies them to the input waveform. For more
  information about the Init subsystem, see Statistical Analysis in SerDes Systems.

#### Programmatic Use

- Use `get_param(gcb,'Mode')` to view the current DFECDR
  **Mode**.
- Use `set_param(gcb,'Mode',value)` to set DFECDR to a
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
  value of DFECDR **Initial tap weights (V)**.
- Use `set_param(gcb,'TapWeights',value)` to set DFECDR to
  a specific **Initial tap weights (V)** vector value.

**Data Types:** `double`

### **Adaptive gain** — Controls DFE tap weight update rate `9.6e-5` (default) | positive real scalar

Controls DFE tap weight update rate, specified as a unitless positive real scalar.
Increasing the value of **Adaptive gain** leads to a faster
convergence of DFE adaptation at the expense of more noise in DFE tap values.

#### Programmatic Use

- Use `get_param(gcb,'EqualizationGain')` to view the
  current DFECDR **Adaptive gain** value.
- Use `set_param(gcb,'EqualizationGain',value)` to set
  DFECDR to a specific value of **Adaptive gain**.

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
  current DFECDR **Adaptive step size (V)** value.
- Use `set_param(gcb,'EqualizationStep',value)` to set
  DFECDR to a specific value of **Adaptive step size
  (V)**.

**Data Types:** `double`

### **Minimum DFE tap value (V)** — Minimum value of adapted taps `-1` (default) | real scalar | real-valued row vector

Minimum value of the adapted taps, specified as a real scalar or a real-valued row
vector in volts. Specify as a scalar to apply to all the DFE taps or as a vector that
has the same length as the **Initial tap weights (V)**.

#### Programmatic Use

- Use `get_param(gcb,'MinimumTap')` to view the current
  DFECDR **Minimum DFE tap value (V)** value.
- Use `set_param(gcb,'MinimumTap',value)` to set DFECDR to
  a specific value of **Minimum DFE tap value (V)**.

**Data Types:** `double`

### **Maximum DFE tap value (V)** — Maximum value of adapted taps `1` (default) | nonnegative real scalar | nonnegative real-valued row vector

Maximum value of the adapted taps, specified as a nonnegative real scalar or a
nonnegative real-valued row vector in volts. Specify as a scalar to apply to all the
DFE taps or as a vector that has the same length as the **Initial tap weights
(V)**.

#### Programmatic Use

- Use `get_param(gcb,'MaximumTap')` to view the current
  DFECDR **Maximum DFE tap value (V)** value.
- Use `set_param(gcb,'MaximumTap',value)` to set DFECDR to
  a specific value of **Maximum DFE tap value (V)**.

**Data Types:** `double`

### **2x tap weights** — Multiply DFE tap weights by a factor of two off (default) | on

Select to multiply the DFE tap weights by a factor of two.

The output of the slicer in the DFECDR block from the SerDes Toolbox™ is [-0.5 0.5]. But some industry applications require the slicer output
to be [-1 1]. **2x tap weights** allows you to quickly double the DFE
tap weights to change the slicer reference.

### CDR

### **CDR Mode** — Determine CDR order `1st order` (default) | `2nd order`

Determine the CDR order to enable phase and frequency tracking.

- `1st order` — Only tracks the phase.
- `2nd order` — Tracks both the phase and
  frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CDRMode` |
| **Type:** character vector |
| **Values:** `1st order` | `2nd order` |
| **Default:** `1st order` |

### **Phase Detector** — Clock phase detector option `BangBang` (default) | `BaudRateTypeA`

Clock phase detector option used in the clock data recovery. You can choose
between bang-bang (Alexander) or baud-rate type-A (Mueller-Muller).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseDetector` |
| **Type:** character vector |
| **Values:** `BangBang` | `BaudRateTypeA` |
| **Default:** `BangBang` |

### **Phase Offset (symbol time)** — Clock phase offset `0` (default) | real scalar in the range [-0.5,0.5]

Clock phase offset, specified as a real scalar in the range [-0.5,0.5] in fraction
of symbol time. **Phase Offset** is used to manually shift clock
probability distribution function (PDF) for better bit error rate (BER).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseOffset` |
| **Type:** character vector |
| **Values:** real scalar in the range [-0.5,0.5] |
| **Default:** `0` |

**Data Types:** `double`

### **Reference offset (ppm)** — Reference clock offset impairment `0` (default) | real scalar in the range [0, 300]

Reference clock offset impairment, specified as a real scalar in the range [0,
300] in parts per million (ppm). **Reference offset (ppm)** is the
deviation between transmitter oscillator frequency and receiver oscillator
frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ReferenceOffset` |
| **Type:** character vector |
| **Values:** real scalar in the range [0, 300] |
| **Default:** `0` |

**Data Types:** `double`

### **Early/late count threshold** — Early or late CDR count threshold to trigger phase update `16` (default) | real positive integer ≥5

Early or late CDR count threshold to trigger a phase update, specified as a
unitless real positive integer ≥5. Increasing the value of **Early/late count
threshold** provides a more stable output clock phase at the expense of
convergence speed. Because the bit decisions are made at the clock phase output, a
more stable clock phase has a better bit error rate (BER).

**Early/late count threshold** also controls the bandwidth of the
CDR.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Count` |
| **Type:** character vector |
| **Values:** real positive integer ≥5 |
| **Default:** `16` |

**Data Types:** `double`

### **Step (symbol time)** — Clock phase resolution `0.0078` (default) | real scalar

Clock phase resolution, specified as a real scalar in fraction of symbol time.
**Step (symbol time)** is the inverse of the number of phase
adjustments in CDR.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Step` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0.0078` |

**Data Types:** `double`

### **Frequency tracking gain** — Internal gain for frequency tracking `0.00048828125` (default) | nonnegative real scalar

Internal gain for the frequency tracking loop, specified as a nonnegative real
scalar.

#### Dependencies

To enable this parameter, set the **CDR Mode** to
`2nd order`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyStep` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0.00048828125` |

**Data Types:** `double`

### **Frequency tracking update** — Frequency tracking update `16` (default) | nonnegative integer scalar

Once every **Frequency tracking update** symbols, update the
system phase rotator clock with the frequency estimate.

#### Dependencies

To enable this parameter, set the **CDR Mode** to
`2nd order`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyCount` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `16` |

**Data Types:** `double`

### **Frequency step ramp** — Number of symbol times required for initial internal frequency tracking gain to reach specified value `3000` (default) | nonnegative integer scalar

To help frequency tracking loop lock early in a simulation, the initial
**Frequency tracking gain** starts at a high value of 1/(2\***Frequency tracking update)**. Then the **Frequency tracking gain** gradually
reduces to the specified value by roughly **Frequency step ramp**
symbol times.

#### Dependencies

To enable this parameter, set the **CDR Mode** to
`2nd order`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyStepRamp` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `3000` |

**Data Types:** `double`

### **Sensitivity (V)** — Sampling latch metastability voltage `0` (default) | real scalar

Sampling latch metastability voltage, specified as a real scalar in volts. If the
data sample voltage lies within the region (±**Sensitivity (V)**),
there is a 50% probability of bit error.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Sensitivity` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

**Data Types:** `double`

#### IBIS-AMI parameters

### **Mode** — Include Mode parameter in IBIS-AMI model on (default) | off

Select to include **Mode** as a parameter in the IBIS-AMI file.
If you deselect **Mode**, it is removed from the AMI files,
effectively hard-coding **Mode** to its current value.

### **Tap weights** — Include Tap weights parameter in IBIS-AMI model on (default) | off

Select to include **Tap weights** as a parameter in the IBIS-AMI
file. If you deselect **Tap weights**, it is removed from the AMI
files, effectively hard-coding **Tap weights** to its current
value.

### **Phase Offset** — Include Phase Offset parameter in IBIS-AMI model on (default) | off

Select to include **Phase Offset** as a parameter in the IBIS-AMI
file. If you deselect **Phase Offset**, it is removed from the AMI
files, effectively hard-coding **Phase Offset** to its current
value.

### **Reference offset** — Include Reference offset parameter in IBIS-AMI model on (default) | off

Select to include **Reference offset** as a parameter in the
IBIS-AMI file. If you deselect **Reference offset**, it is removed
from the AMI files, effectively hard-coding **Reference offset** to
its current value.
## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Decision feedback equalizer (DFE) with clock and data recovery (CDR)

The DFECDR block adaptively processes a sample-by-sample input signal or
analytically processes an impulse response vector input signal to remove distortions at post
cursor taps.

The DFE modifies baseband signals to minimize the intersymbol
interference (ISI) at the clock sampling times. The DFE samples data at each clock sample time
and adjusts the amplitude of the waveform by a correction voltage.

For impulse response processing, the hula-hoop algorithm is used to find the clock
sampling locations. The zero-forcing algorithm is then used to determine the
*N* correction factors necessary to have no ISI at the *N*
subsequent sampling locations, where *N* is the number of DFE taps.

For sample-by-sample processing, the clock recovery is accomplished by a first order phase
tracking and optionally second order frequency tracking model. The bang-bang phase detector
utilizes the unequalized edge samples and equalized data samples to determine the optimum
sampling location. The DFE correction voltage for the *N*-th tap is
adaptively found by finding a voltage that compensates for any correlation between two data
samples spaced by *N* symbol times. This requires a data pattern that is
uncorrelated with the channel ISI for correct adaptive behavior.
