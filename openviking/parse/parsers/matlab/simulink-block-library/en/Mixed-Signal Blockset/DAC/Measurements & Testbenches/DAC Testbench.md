---
type: simulink-block
title: 'DAC Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Measurements & Testbenches'
documentation_page: 'dactestbench'
documentation_source_path: 'ref/dactestbench.html'
language: en
---

# DAC Testbench

## Ports
```yaml
ports:
- name: from dac analog
  summary: Analog signal from DAC output scalar
  direction: input
  data_types: double
- name: to dac digital
  summary: Digital stimulus signal for DAC input scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: to dac start
  summary: External start conversion clock for DAC scalar
  direction: output
  data_types: double
```

### Input

### **from dac analog** — Analog signal from DAC output scalar

Analog input signal from the DAC output, specified as a scalar.

**Data Types:** `double`
### Output

### **to dac digital** — Digital stimulus signal for DAC input scalar

Digital output stimulus signal for the DAC input, returned as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **to dac start** — External start conversion clock for DAC scalar

External start conversion clock for DAC, returned as a scalar. The rising edge of
this signal starts the conversion process in the DAC block.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Measurement
  summary: Select whether to measure DC or AC performance metrics DC (default) | AC
  group: ''
- name: Recommended min. simulation stop time (s)
  summary: Minimum time simulation must run for meaningful result 2.048e-02 (default) | positive real scalar
  group: ''
- name: Set as model stop time
  summary: Automatically set recommended min. simulation stop time as model stop time button
  group: ''
- name: Endpoint
  summary: Measure DNL, INL using endpoint method on (default) | off
  group: ''
- name: Best fit
  summary: Measure DNL, INL using best fit method on (default) | off
  group: ''
- name: Plot DC analysis result
  summary: Plot DC analysis result button
  group: ''
- name: Export measurement result
  summary: Store detailed test results to base workspace button
  group: ''
- name: Digital input frequency (Hz)
  summary: Frequency of digital input signal to DAC 1e4 (default) | positive real scalar
  group: Stimulus
  block_parameter: InputFrequency
  type: character vector
  values: positive real scalar
  default: 1e3
- name: Start conversion frequency (Hz)
  summary: Frequency of internal start-conversion clock 1e6 (default) | positive real scalar
  group: Stimulus
  block_parameter: StartFreq
  type: character vector
  values: positive real scalar
  default: 1e6
- name: Error tolerance (LSB)
  summary: Maximum difference between successive samples of digital signal 0.1 (default) | positive scalar in the range (0,
    1]
  group: Stimulus
  block_parameter: ErrorTolerance
  type: character vector
  values: positive scalar in the range (0, 1]
  default: '0.1'
- name: Autofill setup parameters
  summary: Automatically propagate setup parameters from DAC button
  group: Setup
- name: Number of bits
  summary: Number of bits in input word 10 (default) | positive real integer
  group: Setup
  block_parameter: NBits
  type: character vector
  values: positive real integer
  default: '10'
- name: Input polarity
  summary: Polarity of input signal to DAC Bipolar (default) | Unipolar
  group: Setup
  block_parameter: Polarity
  type: character vector
  values: Bipolar|Unipolar
  default: Bipolar
- name: Reference (V)
  summary: Reference voltage 1 (default) | real scalar
  group: Setup
  block_parameter: Ref
  type: character vector
  values: real scalar
  default: '1'
- name: Bias (V)
  summary: Bias voltage added to output 0 (default) | real scalar
  group: Setup
  block_parameter: Bias
  type: character vector
  values: real scalar
  default: '0'
- name: Settling time (s)
  summary: Time required for output to settle 0.25/1e-6 (default) | nonnegative real scalar
  group: Setup
  block_parameter: SettlingTime
  type: character vector
  values: real scalar
  default: 0.25/1e-6
- name: Settling time tolerance (LSB)
  summary: Tolerance for calculating settling time 0.5 (default) | positive real scalar
  group: Setup
  block_parameter: SettlingTimeTolerance
  type: character vector
  values: positive real scalar
  default: '0.5'
- name: Hold off time (s)
  summary: Delay before measurement analysis 0 (default) | nonnegative real scalar
  group: Setup
- name: Show spectrum analyzer during simulation
  summary: Displays Spectrum Analyzer during simulation off (default) | on
  group: Setup
- name: Autofill target metric
  summary: Automatically propagate target metrics from DAC button
  group: Target Metric
- name: Offset error
  summary: Shifts quantization steps by specific value 0 LSB (default) | real scalar
  group: Target Metric
  block_parameter: TargetOffsetError
  type: character vector
  values: real scalar
  default: 0 LSB
- name: Gain error
  summary: Error in slope of DAC transfer curve 0 LSB (default) | real scalar
  group: Target Metric
  block_parameter: TargetGainError
  type: character vector
  values: real scalar
  default: 0 LSB
```

### **Measurement** — Select whether to measure DC or AC performance metrics `DC` (default) | `AC`

Select whether to measure static (DC) or dynamic (AC) performance metrics:

- Select `DC` to measure offset error and gain
  error.
- Select `AC` to measure SNR, SINAD, SFDR, ENOB, and
  noise floor.

### **Recommended min. simulation stop time (s)** — Minimum time simulation must run for meaningful result `2.048e-02` (default) | positive real scalar

Minimum time for which the simulation must run to obtain meaningful results,
specified as a positive real scalar in seconds.

- To measure DC performance, the simulation must run so that the DAC can sample
  each digital code 20 times. Based on this assumption, the **Recommended min.
  simulation stop time (s)**
  *T* is given by:

  T=Samples per bit(StartFreq/2Nbits+1)+Hold off time,

  where *StartFreq* is the frequency of the conversion-start
  clock and *Nbits* is the resolution of the DAC.

  The number of samples per bit is calculated using the equation:

  Samples per bit = max(1Error tolerance,10).
- To measure AC performance, the simulation must run so that the DAC can generate
  six spectral updates of the DAC output. So, the **Recommended min.
  simulation stop time (s)**
  *T* is given by [1]:

  T=6(1.5RBW+Hold off time),

  where *RBW* is the resolution bandwidth of the spectrum
  estimator inside the DAC Testbench block and is given by the
  equation: RBW=[min(Input frequency)0.1].

This parameter is only reported by the testbench and is not editable.

**Data Types:** `double`

### **Set as model stop time** — Automatically set recommended min. simulation stop time as model stop time button

Click to automatically set the **Recommended min. simulation stop time
(s)** as the stop time of the Simulink® model.

### **Endpoint** — Measure DNL, INL using endpoint method on (default) | off

Measure the differential nonlinearity (DNL) error and integral nonlinearity (INL)
error using the endpoint method. This method uses the endpoints of the actual transfer
function to measure the DNL and INL errors.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

### **Best fit** — Measure DNL, INL using best fit method on (default) | off

Measure the differential nonlinearity (DNL) error and integral nonlinearity (INL)
error using the best fit method. This method uses a standard curve-fitting technique to
find the best fit to measure the DNL and INL errors.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

### **Plot DC analysis result** — Plot DC analysis result button

Click to plot DC analysis result for further analysis. To perform a complete DC
analysis including integral nonlinearity (INL) and differential nonlinearity (DNL), use
the DAC DC
Measurement block.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

### **Export measurement result** — Store detailed test results to base workspace button

Click to store detailed test results to a spreadsheet (XLS file) or as
comma-separated values (CSV file) for further processing.

### Stimulus

### **Digital input frequency (Hz)** — Frequency of digital input signal to DAC `1e4` (default) | positive real scalar

Frequency of the digital input signal to the DAC block, specified
as a positive real scalar in hertz. **Digital input frequency (Hz)**
must match the input frequency of the DAC device under test.

**Digital input frequency (Hz)** needs to satisfy two
requirements:

- All the output codes of the DAC must be activated.
- The **Digital input frequency (Hz)** must not share any
  common multiples other than 1 with the **Start conversion frequency
  (Hz)**.

#### Dependencies

To enable this parameter, set **Measurement** to
`AC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputFrequency` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e3` |

**Data Types:** `double`

### **Start conversion frequency (Hz)** — Frequency of internal start-conversion clock `1e6` (default) | positive real scalar

Frequency of internal start-conversion clock, specified as a positive real scalar
in Hz. **Start conversion frequency (Hz)** determines the rate of the
DAC.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StartFreq` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e6` |

**Data Types:** `double`

### **Error tolerance (LSB)** — Maximum difference between successive samples of digital signal `0.1` (default) | positive scalar in the range (`0, 1`]

Maximum allowed difference in the amplitude of successive samples of the digital
input signal, specified as a positive real scalar in least significant bit
(LSB).

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ErrorTolerance` |
| **Type:** character vector |
| **Values:** positive scalar in the range (`0, 1`] |
| **Default:** `0.1` |

**Data Types:** `double`

### Setup

### **Autofill setup parameters** — Automatically propagate setup parameters from DAC button

Click to automatically propagate setup parameters from the DAC.

#### Dependencies

The DAC must be a Binary Weighted
DAC from the Mixed-Signal Blockset.

### **Number of bits** — Number of bits in input word `10` (default) | positive real integer

Number of bits in the input word, specified as a unitless positive real integer.
**Number of bits** determines the resolution of the DAC.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NBits` |
| **Type:** character vector |
| **Values:** positive real integer |
| **Default:** `10` |

**Data Types:** `double`

### **Input polarity** — Polarity of input signal to DAC `Bipolar` (default) | `Unipolar`

Polarity of the input signal to the DAC.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Polarity` |
| **Type:** character vector |
| **Values:** `Bipolar`|`Unipolar` |
| **Default:** `Bipolar` |

### **Reference (V)** — Reference voltage `1` (default) | real scalar

Reference voltage of the DAC, specified as a real scalar in volts.
**Reference (V)** helps determine the output from the input digital
code, **Number of bits**, and **Bias (V)** using the
equation:

DAC output = ((Digital input code2Number of bits)Reference)+Bias.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Ref` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `1` |

**Data Types:** `double`

### **Bias (V)** — Bias voltage added to output `0` (default) | real scalar

Bias voltage added to the output of the DAC, specified as a real scalar in volts.
**Bias (V)** helps determine the output from the input digital
code, **Number of bits**, and **Reference (V)**
using the equation:

DAC output = ((Digital input code2Number of bits)Reference)+Bias

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Bias` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

**Data Types:** `double`

### **Settling time (s)** — Time required for output to settle `0.25/1e-6` (default) | nonnegative real scalar

The time required for the output of the DAC to settle to within some fraction of
its final value, specified as a nonnegative real scalar in seconds.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTime` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0.25/1e-6` |

**Data Types:** `double`

### **Settling time tolerance (LSB)** — Tolerance for calculating settling time `0.5` (default) | positive real scalar

The tolerance allowed for calculating settling time, specified as a positive real
scalar in LSB. The output of the DAC must settle within the **Settling time
tolerance (LSB)** by **Settling time (s)**.

#### Dependencies

To enable this parameter, set **Measurement** to
`AC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTimeTolerance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.5` |

**Data Types:** `double`

### **Hold off time (s)** — Delay before measurement analysis `0` (default) | nonnegative real scalar

Delay before measurement analysis to avoid corruption by transients, specified as
a nonnegative real scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'HoldOffTime')` to view the current
  value of **Hold off time (s)**.
- Use `set_param(gcb,'HoldOffTime',value)` to set
  **Hold off time (s)** to a specific value.

**Data Types:** `double`

### **Show spectrum analyzer during simulation** — Displays Spectrum Analyzer during simulation off (default) | on

Select this parameter to display the Spectrum Analyzer window during simulation.
By default, this parameter is deselected.

#### Dependencies

To enable this parameter, set **Measurement** to
`AC`.

### Target Metric

### **Autofill target metric** — Automatically propagate target metrics from DAC button

Click to automatically propagate target metrics from the DAC.

#### Dependencies

- To enable this parameter, set **Measurement** to
  `DC`.
- The DAC must be a Binary
  Weighted DAC from the Mixed-Signal Blockset.

### **Offset error** — Shifts quantization steps by specific value `0 LSB` (default) | real scalar

Shifts quantization steps by a specific value, specified as a real scalar in %FS
(percentage of full scale), FS (full scale), or LSB (least significant bit).

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5
LSB wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TargetOffsetError` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0 LSB` |

**Data Types:** `double`

### **Gain error** — Error in slope of DAC transfer curve `0 LSB` (default) | real scalar

Error in the slope of the straight line interpolating the DAC transfer curve,
specified as a real scalar in %FS (percentage of full scale), FS (full scale), or LSB
(least significant bit).

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5
LSB wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

#### Dependencies

To enable this parameter, set **Measurement** to
`DC`.

#### Programmatic Use

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TargetGainError` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0 LSB` |

**Data Types:** `double`
## Libraries

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Measure DC and AC performance metrics of DAC output

The DAC Testbench block measures both DC and AC performance metrics of a
DAC (digital to analog converter). DC performance metrics include offset error and gain error.
AC performance metrics include signal-to-noise ratio (SNR), signal to noise and distortion
radio (SINAD), spurious-free dynamic range (SFDR), effective number of bits (ENOB), and noise
floor.

The DAC Testbench block generates the stimulus to drive the device under
test (DUT) from the **Stimulus** tab. The setup parameters for validating the
DUT are defined on the **Setup** tab. The target validation metrics are
defined on the **Target Metric** tab.

You can use the DAC Testbench block to validate the DAC architecture models
provided in Mixed-Signal Blockset™, or you can validate a DAC of your own implementation.
