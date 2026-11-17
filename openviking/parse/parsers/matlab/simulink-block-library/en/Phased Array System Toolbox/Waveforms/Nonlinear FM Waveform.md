---
type: simulink-block
title: 'Nonlinear FM Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'nonlinearfmwaveform'
documentation_source_path: 'ref/nonlinearfmwaveform.html'
language: en
---

# Nonlinear FM Waveform

## Ports
```yaml
ports:
- name: PRFIdx
  summary: PRF Index positive integer
  direction: input
  data_types: double
- name: FreqOffset
  summary: Frequency offset scalar
  direction: input
  data_types: double
- name: Y
  summary: Pulse waveform complex-valued vector
  direction: output
  data_types: double
- name: PRF
  summary: Pulse repetition frequency positive scalar
  direction: output
  data_types: double
- name: Coeff
  summary: Matched filter coefficients vector | matrix
  direction: output
  data_types: double
```

### Input

### **PRFIdx** — PRF Index positive integer

Index to select the pulse repetition frequency (PRF), specified as a positive
integer. The index selects the PRF from the predefined vector of values specified by
the **Pulse repetition frequency (Hz)** parameter.

**Example:**
`4`

#### Dependencies

To enable this port, select **Enable PRF selection
input**.

**Data Types:** `double`

### **FreqOffset** — Frequency offset scalar

Frequency offset in Hz, specified as a scalar.

**Example:**
`2e3`

#### Dependencies

To enable this port, set **Source of Frequency Offset** to
`Input port`.

**Data Types:** `double`
### Output

### **Y** — Pulse waveform complex-valued vector

Pulse waveform samples, returned as a complex-valued vector.

**Data Types:** `double`

### **PRF** — Pulse repetition frequency positive scalar

Pulse repetition frequency of current pulse, returned as a positive scalar.

#### Dependencies

To enable this port, set the **Output signal format** parameter
to `Pulses` and then select the **Enable PRF
output** parameter.

**Data Types:** `double`

### **Coeff** — Matched filter coefficients vector | matrix

Matched filter coefficients, returned as a vector or matrix.

#### Dependencies

To enable this port, select **Enable Matched Filter Coefficients
Output**.

**Data Types:** `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Sample rate (Hz)
  summary: Sample rate of the output waveform 1e6 (default) | positive scalar
  group: ''
  block_parameter: SampleRate
  type: double
  values: positive scalar
  default: 1e6
- name: Method to specify pulse duration
  summary: Pulse duration as time or duty cycle Pulse width (default) | Duty cycle
  group: ''
  block_parameter: DurationSpecification
  type: string
  values: string
  default: '''Pulse width'''
- name: Pulse width (s)
  summary: Time duration of pulse 50e-6 (default) | positive scalar
  group: ''
  block_parameter: PulseWidth
  type: double
  values: string
  default: 50e-6
- name: Duty cycle
  summary: Waveform duty cycle 0.5 (default) | scalar in the range *[0,1]*
  group: ''
  block_parameter: DutyCycle
  type: double
  values: positive scalar
  default: 1e6
- name: Pulse repetition frequency (Hz)
  summary: Pulse repetition frequency 1e4 (default) | positive scalar
  group: ''
  block_parameter: PRF
  type: double
  values: positive scalar
  default: 1e6
- name: Enable PRF selection input
  summary: Select predefined PRF off (default) | on
  group: ''
  block_parameter: PRFSelectionInputPort
  type: logical
  values: positive scalar
  default: 'off'
- name: Frequency modulation
  summary: Frequency modulation Polynomial (default) | Hyperbolic | Hybrid Linear-Tangent | Stepped Price
  group: ''
  block_parameter: FrequencyModulation
  type: char, string
  values: char. string
  default: Hyperbolic
- name: Coefficients of a polynomial FM
  summary: Coefficients of polynomial frequency function [1 0 0] (default) | (*N*+1)-length real-valued vector
  group: ''
  block_parameter: PolynomialCoefficients
  type: double
  values: vector
  default: '[1 0 0]'
- name: Sweep bandwidth (Hz)
  summary: Bandwidth of nonlinear FM sweep 100e3 (default) | positive scalar
  group: ''
  block_parameter: SweepBandwidth
  type: double
  values: positive scalar
  default: 100e3
- name: Sweep direction
  summary: Direction of nonlinear FM sweep Up (default) | Down
  group: ''
  block_parameter: SweepDirection
  type: enum
  values: Up, Down
  default: Up
- name: Sweep interval
  summary: FM frequency sweep interval Positive (default) | Symmetric
  group: ''
  block_parameter: SweepInterval
  type: enum
  values: Symmetric, Positive
  default: Positive
- name: Envelope function
  summary: FM signal amplitude envelope Rectangular (default) | Gaussian | Hamming | Chebyshev | Hann | Kaiser | Taylor
  group: ''
  block_parameter: Envelope
  type: enum
  values: Rectangular, Gaussian, Hamming, Chebyshev, Hann, Kaiser, or Taylor
  default: Rectangular
- name: Source of Frequency Offset
  summary: Source of frequency offset Property (default) | Input port
  group: ''
  block_parameter: FrequencyOffsetSource
  type: enum
  values: Property, Input Port
  default: Property
- name: Frequency Offset (Hz)
  summary: Frequency offset 0 (default) | scalar
  group: ''
  block_parameter: FrequencyOffset
  type: double
  values: scalar
  default: '0'
- name: Output signal format
  summary: Format of the output signal Pulses (default) | Samples
  group: ''
  block_parameter: OutputFormat
  type: enum
  values: Pulses Samples
  default: Pulses
- name: Number of samples in output
  summary: Number of samples in output 100 (default) | positive integer
  group: ''
  block_parameter: NumSamples
  type: double
  values: positive scalar
  default: '100'
- name: Number of pulses in output
  summary: Number of pulses in output 1 (default) | positive integer
  group: ''
  block_parameter: NumPulses
  type: double
  values: positive scalar
  default: '1'
- name: Enable PRF Output
  summary: Enable output of PRF off (default) | on
  group: ''
  block_parameter: PRFOutputPort
  type: enum
  values: off on
  default: 'off'
- name: Enable Matched Filter Coefficients Output
  summary: Enable output of matched filter coefficients off (default) | on
  group: ''
  block_parameter: CoefficientOutputPort
  type: enum
  values: off on
  default: 'off'
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample rate (Hz)** — Sample rate of the output waveform `1e6` (default) | positive scalar

Sample rate of the output waveform, specified as a positive scalar. The ratio of
**Sample rate (Hz)** to each element in the **Pulse
repetition frequency (Hz)** vector must be an integer. This restriction is
equivalent to requiring that the pulse repetition interval is an integral multiple of
the sample interval.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SampleRate` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`1e6` |

### **Method to specify pulse duration** — Pulse duration as time or duty cycle `Pulse width` (default) | `Duty cycle`

Method to set the pulse duration, specified as `Pulse width`
or `Duty cycle`. When you set this parameter to
`Pulse width`, the pulse duration is set using the
**Pulse width (s)** parameter. When you set this parameter to
`Duty cycle`, the pulse duration is computed from the
values of the **Pulse repetition frequency (Hz)** and **Duty
Cycle** parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`DurationSpecification` |
| **Type:**string |
| **Values:**string |
| **Default:**`'Pulse width'` |

### **Pulse width (s)** — Time duration of pulse `50e-6` (default) | positive scalar

The duration of each pulse, specified as a positive scalar. Set the product of
**Pulse width (s)** and **Pulse repetition
frequency** to be less than or equal to one. This restriction ensures that
the pulse width is smaller than the pulse repetition interval. Units are in
seconds.

**Example:** `300e-6`

#### Dependencies

To enable this parameter, set the **Method to specify pulse
duration** parameter to `Pulse width`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PulseWidth` |
| **Type:**double |
| **Values:**string |
| **Default:**`50e-6` |

### **Duty cycle** — Waveform duty cycle `0.5` (default) | scalar in the range *[0,1]*

Waveform duty cycle, specified as a scalar in the range *[0,1]*.

**Example:** `0.7`

#### Dependencies

To enable this parameter, set the **Method to specify pulse duration**
parameter to `Duty cycle`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`DutyCycle` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`1e6` |

### **Pulse repetition frequency (Hz)** — Pulse repetition frequency `1e4` (default) | positive scalar

Pulse repetition frequency, *PRF*, specified as a scalar or a row vector.
Units are in Hz. The pulse repetition interval, *PRI*, is the inverse of the
pulse repetition frequency, *PRF*. The value of **Pulse repetition
frequency (Hz)** must satisfy these constraints:

- The product of **Pulse width** and **Pulse repetition
  frequency (Hz)** must be less than or equal to one. This condition expresses
  the requirement that the pulse width is less than one pulse repetition interval. For the
  phase-coded waveform, the pulse width is the product of the chip width and number of
  chips.
- The ratio of sample rate to any element of **Pulse repetition
  frequency** must be an integer. This condition expresses the requirement that
  the number of samples in one pulse repetition interval is an integer.

You can select the value of *PRF* by using block parameter settings alone or
in conjunction with the input port, `PRFIdx`.

- When the **Enable PRF selection input** parameter is not selected,
  set the *PRF* using block parameters.

  - To implement a constant *PRF*, specify **Pulse
    repetition frequency (Hz)** as a positive scalar.
  - To implement a staggered *PRF*, specify **Pulse
    repetition frequency (Hz)** as a row vector with positive values. After
    the waveform reaches the last element of the vector, the process continues
    cyclically with the first element of the vector. When *PRF* is
    staggered, the time between successive output pulses cycles through the successive
    values of the *PRF* vector.
- When the **Enable PRF selection input** parameter is selected, you
  can implement a selectable *PRF* by specifying **Pulse
  repetition frequency (Hz)** as a row vector with positive real-valued
  entries. But this time, when you execute the block, select a *PRF* by
  passing an index into the *PRF* vector into the
  `PRFIdx` port.

In all cases, the number of output samples is fixed when you set the
**Output signal format** to `Samples`. When you
use a varying *PRF* and set **Output signal format** to
`Pulses`, the number of output samples can vary.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PRF` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`1e6` |

### **Enable PRF selection input** — Select predefined PRF off (default) | on

Select this parameter to enable the `PRFIdx` port.

- When enabled, pass in an index into a vector of predefined PRFs. Set
  predefined PRFs using the **Pulse repetition frequency
  (Hz)** parameter.
- When not enabled, the block cycles through the vector of PRFs specified by
  the **Pulse repetition frequency (Hz)** parameter. If
  **Pulse repetition frequency (Hz)** is a scalar, the
  PRF is constant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PRFSelectionInputPort` |
| **Type:**logical |
| **Values:**positive scalar |
| **Default:**`off` |

### **Frequency modulation** — Frequency modulation `Polynomial` (default) | `Hyperbolic` | `Hybrid Linear-Tangent` | `Stepped Price`

Frequency modulation of the nonlinear FM waveform, specified as
`Polynomial`, `Hyperbolic`,
`Hybrid Linear-Tangent`, or `Stepped
Price`.

- When set to `Polynomial` the block generates a waveform
  with an instantaneous frequency that follows a polynomial function. The coefficients
  of the polynomial are specified by the **Coefficients of a Polynomial
  FM** parameter. The resulting frequency function is normalized such
  that each pulse sweeps the bandwidth specified in **Sweep bandwidth
  (Hz)**. The **Sweep interval** parameter is
  inactive when **Frequency modulation** is set to
  `Polynomial`.
- When set to `Hyperbolic` the block generates a
  hyperbolic frequency modulated (HFM) waveform. Use the **Start frequency
  of a hyperbolic FM** parameter to set the start frequency of the
  hyperbolic sweep. The **Sweep interval** parameter is
  inactive in this case.
- When set to `Hybrid Linear-Tangent` the block generates
  a hybrid NLFM waveform that combines an LFM with a tan-FM as described by Collins
  and Atkins [1]. The balance
  between LFM and tan-FM is specified by the **Balance between linear FM
  and tan-FM** parameter, and the portion of the
  *tan(x)* curve used for tan-FM is specified by the
  **Tangent curve portion** parameter.
- When set to `Stepped Price` the block generates a
  stepped version of the Price's NLFM waveform as given by Levanon and Mozeson [2]. The
  **Sweep interval** parameter is inactive when
  **Frequency modulation** parameter is set to
  `Stepped Price`. In this case the sweep bandwidth is
  determined by the bandwidth factors specified in the **Bandwidth
  factors** parameter and the number of frequency steps specified in
  **Number of frequency steps** parameter.

**Example:** `Stepped Price`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`FrequencyModulation` |
| **Type:**char, string |
| **Values:**char. string |
| **Default:**`Hyperbolic` |

**Data Types:** `char` | `string`

### **Coefficients of a polynomial FM** — Coefficients of polynomial frequency function `[1 0 0]` (default) | (*N*+1)-length real-valued vector

Coefficients of the polynomial frequency function, specified as a
length-(*N*+1) real-valued vector. The vector represents the
coefficients of an *N*-th degree polynomial. The first entry in the
vector is the coefficient of the highest power *N* of the polynomial.
The last entry is the coefficient of the power zero term of the polynomial.

**Example:** `[0.5,1,1,0.5]`

#### Dependencies

To enable this property, set the **Frequency modulation**
parameter to `Polynomial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PolynomialCoefficients` |
| **Type:**double |
| **Values:**vector |
| **Default:**`[1 0 0]` |

**Data Types:** `double`

### **Sweep bandwidth (Hz)** — Bandwidth of nonlinear FM sweep `100e3` (default) | positive scalar

Bandwidth of the linear FM sweep, specified as a positive scalar. Units are in
Hz.

**Example:** `50e3`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SweepBandwidth` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`100e3` |

### **Sweep direction** — Direction of nonlinear FM sweep `Up` (default) | `Down`

Direction of nonlinear FM sweep as `Up` (increasing frequency) or
`Down` (decreasing frequency).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SweepDirection` |
| **Type:**enum |
| **Values:**Up, Down |
| **Default:**`Up` |

### **Sweep interval** — FM frequency sweep interval `Positive` (default) | `Symmetric`

FM frequency sweep interval, specified as `Positive` or
`Symmetric`. If you set this parameter to
`Positive`, the waveform sweeps the frequency interval
between *0* and *B*, where *B* is the
value of the **Sweep bandwidth** parameter. If you set this parameter
value to `Symmetric`, the waveform sweeps the interval between
*–B/2* and *B/2*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SweepInterval` |
| **Type:**enum |
| **Values:**Symmetric, Positive |
| **Default:**`Positive` |

### **Envelope function** — FM signal amplitude envelope `Rectangular` (default) | `Gaussian` | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

FM signal amplitude envelope function, specified as
`Rectangular`, `Gaussian`,
`Hamming`, `Chebyshev`,
`Hann`, `Kaiser`, or
`Taylor`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`Envelope` |
| **Type:**enum |
| **Values:**`Rectangular`, `Gaussian`, `Hamming`, `Chebyshev`, `Hann`, `Kaiser`, or `Taylor` |
| **Default:**`Rectangular` |

### **Source of Frequency Offset** — Source of frequency offset `Property` (default) | `Input port`

Source of frequency offset, specified as `Property` or
`Input port`.

- When set to
  `Property`, the offset is
  determined by the value of the **Frequency
  Offset** parameter.
- When set to `Input
  port`, the offset is determined by
  the value of the **FreqOffset**
  port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`FrequencyOffsetSource` |
| **Type:**enum |
| **Values:**`Property`, `Input Port` |
| **Default:**`Property` |

### **Frequency Offset (Hz)** — Frequency offset `0` (default) | scalar

Frequency offset, specified as a scalar. Units are in Hz.

**Example:** `2e3`

#### Dependencies

To enable this parameter set the **Source of Frequency Offset**
parameter to `Input port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`FrequencyOffset` |
| **Type:**double |
| **Values:**`scalar` |
| **Default:**`0` |

### **Output signal format** — Format of the output signal `Pulses` (default) | `Samples`

The format of the output signal, specified as `Pulses` or `Samples`.

If you set this parameter to `Samples`, the output of the block consists of multiple samples. The number of samples is the value of the **Number of samples in output** parameter.

If you set this parameter to `Pulses`, the output of the block consists of multiple pulses. The number of pulses is the value of the **Number of pulses in output** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputFormat` |
| **Type:**enum |
| **Values:**`Pulses` `Samples` |
| **Default:**`Pulses` |

### **Number of samples in output** — Number of samples in output `100` (default) | positive integer

Number of samples in the block output, specified as a positive integer.

**Example:** `1000`

#### Dependencies

To enable this parameter, set the **Output signal format**
parameter to `Samples`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NumSamples` |
| **Type:**double |
| **Values:**`positive scalar` |
| **Default:**`100` |

**Data Types:** `double`

### **Number of pulses in output** — Number of pulses in output `1` (default) | positive integer

Number of pulses in the block output, specified as a positive integer.

**Example:** `2`

#### Dependencies

To enable this parameter, set the **Output signal
format** parameter to
`Pulses`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NumPulses` |
| **Type:**double |
| **Values:**`positive scalar` |
| **Default:**`1` |

**Data Types:** `double`

### **Enable PRF Output** — Enable output of PRF `off` (default) | `on`

Select this parameter to enable the `PRF` output port.

#### Dependencies

To enable this parameter, set **Output signal format** to
`Pulses`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PRFOutputPort` |
| **Type:**enum |
| **Values:**`off` `on` |
| **Default:**`off` |

### **Enable Matched Filter Coefficients Output** — Enable output of matched filter coefficients `off` (default) | `on`

Select this parameter to enable the `Coeff` output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CoefficientOutputPort` |
| **Type:**enum |
| **Values:**`off` `on` |
| **Default:**`off` |

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

When the Simulink model is in `Accelerator` mode, the block mode specified
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

Phased Array System Toolbox / Waveforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Nonlinear FM pulse waveform

The Nonlinear FM Waveform block generates a nonlinear FM pulse waveform
with specified pulse width, pulse repetition frequency (PRF), and sweep bandwidth. The block
outputs an integer number of pulses or an integral number of samples.
