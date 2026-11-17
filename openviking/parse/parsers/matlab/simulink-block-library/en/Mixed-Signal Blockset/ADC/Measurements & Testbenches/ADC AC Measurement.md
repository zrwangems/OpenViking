---
type: simulink-block
title: 'ADC AC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'adcacmeasurement'
documentation_source_path: 'ref/adcacmeasurement.html'
language: en
---

# ADC AC Measurement

## Ports
```yaml
ports:
- name: digital
  summary: Converted digital signal from ADC scalar
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: ready
  summary: Indicates whether analog to digital conversion is complete scalar
  direction: input
  data_types: double
- name: start
  summary: External conversion start clock scalar
  direction: input
  data_types: double
```

### Input

### **digital** — Converted digital signal from ADC scalar

Converted digital signal from an ADC, specified as a scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ready** — Indicates whether analog to digital conversion is complete scalar

Indicates whether the analog to digital conversion is complete, specified as a
scalar.

**Data Types:** `double`

### **start** — External conversion start clock scalar

External conversion start clock, specified as a scalar. The analog to digital
conversion process starts at the rising edge of the signal at the
**start** port.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Distortion measurement type
  summary: Type of distortion to measure Harmonic (default) | Intermodulation
  group: ''
  block_parameter: DistortionMeasurement
  type: character vector
  values: Harmonic | Intermodulation
  default: Harmonic
- name: Analog stimulus frequency (Hz)
  summary: Frequency of the analog input signal to ADC positive real scalar | positive real valued vector
  group: ''
  block_parameter: InputFrequency
  type: character vector
  values: positive real scalar | positive real valued vector
  default: '10000'
- name: Spectrum estimation method
  summary: Spectrum estimation method Welch (default) | Filter bank
  group: ''
  block_parameter: Method
  type: character vector
  values: Filter bank | Welch
  default: Filter bank
- name: Resolution bandwidth (Hz)
  summary: Resolution bandwidth positive real scalar
  group: ''
  block_parameter: RBW
  type: character vector
  values: positive real scalar
  default: '976.5625'
- name: Start conversion frequency (Hz)
  summary: Frequency of the start conversion clock of the ADC 1e6 (default) | positive real scalar
  group: ''
  block_parameter: Frequency
  type: character vector
  values: positive real scalar
  default: 1e6
- name: Hold off time (s)
  summary: Delays measurement analysis to avoid corruption by transients 0 (default) | nonnegative real scalar
  group: ''
  block_parameter: HoldOffTime
  type: character vector
  values: nonnegative real scalar
  default: '0'
- name: Recommended min. simulation stop time (s)
  summary: Minimum time simulation must run for meaningful result positive real scalar
  group: ''
- name: Set as model stop time
  summary: Automatically set recommended min. simulation stop time as model stop time button
  group: ''
- name: Output result to base workspace
  summary: Store detailed test results to base workspace off (default) | on
  group: ''
- name: Workspace variable name
  summary: Name of the variable that stores detailed test results adc_ac_out (default) | character string
  group: ''
  block_parameter: VariableName
  type: character vector
  values: character string
  default: adc_ac_out
- name: Show spectrum analyzer during simulation
  summary: Displays spectrum analyzer during simulation off (default) | on
  group: ''
```

### **Distortion measurement type** — Type of distortion to measure `Harmonic` (default) | `Intermodulation`

Type of distortion the ADC AC Measurement block is set to measure,
specified as `Harmonic` or
`Intermodulation`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `DistortionMeasurement` |
| **Type:** character vector |
| **Values:** `Harmonic` | `Intermodulation` |
| **Default:** `Harmonic` |

### **Analog stimulus frequency (Hz)** — Frequency of the analog input signal to ADC positive real scalar | positive real valued vector

Frequency of the analog input signal to an ADC block, specified as a
positive real scalar or positive real valued vector in hertz. **Analog stimulus
frequency** must match the input frequency to the ADC device
under test.

- When the ADC AC Measurement is set to measure the
  `Harmonic` distortion, the default value of
  **Analog stimulus frequency** is `10000`.
- When the ADC AC Measurement is set to measure the
  `Intermodulation` distortion, the default value of
  **Analog stimulus frequency** is
  `[9000,11000]`.

**Analog stimulus frequency** must not share any common multiples
other than 1 with the **Start conversion frequency**.

To satisfy this condition, use the equation fanalog=JMfstart,

where:

*f*analog is the analog signal
frequency,

*f*start is the start conversion
frequency,

*J* is the number of cycles of the stimulus per FFT window,

and *M* is the number of FFT points.

**Note**

*J* is selected as the largest prime number less than one tenth
of the number of FFT points. The minimum value of *M* is allowed to
be 16.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputFrequency` |
| **Type:** character vector |
| **Values:** positive real scalar | positive real valued vector |
| **Default:** `10000` |

### **Spectrum estimation method** — Spectrum estimation method **Welch** (default) | **Filter bank**

Select the spectrum estimation method as one of the following:

- **Filter bank** — Use an analysis filter bank to estimate the
  power spectrum. Compared to Welch's method, this method has a lower noise floor,
  better frequency resolution, lower spectral leakage, and requires fewer samples per
  update. For more information, see Spectrum Estimation — Filter Bank
- **Welch** — Use Welch's method of averaged modified
  periodograms. For more information, see Spectrum Estimation — Welch's Method

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Method` |
| **Type:** character vector |
| **Values:** **Filter bank** | **Welch** |
| **Default:** **Filter bank** |

### **Resolution bandwidth (Hz)** — Resolution bandwidth positive real scalar

Resolution bandwidth, specified as a positive real scalar in hertz. This parameter
defines the smallest positive frequency that can be resolved. By default, this parameter
is calculated automatically. You can deselect **Set automatically** to
customize the value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `RBW` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `976.5625` |

### **Start conversion frequency (Hz)** — Frequency of the start conversion clock of the ADC `1e6` (default) | positive real scalar

Frequency of the start conversion clock of the ADC, specified as a positive real
scalar in hertz. **Start conversion frequency** must match the
frequency of the start conversion clock of the ADC block.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Frequency` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e6` |

### **Hold off time (s)** — Delays measurement analysis to avoid corruption by transients `0` (default) | nonnegative real scalar

Delays measurement analysis to avoid corruption by transients, specified as a
nonnegative real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `HoldOffTime` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### **Recommended min. simulation stop time (s)** — Minimum time simulation must run for meaningful result positive real scalar

Minimum time the simulation must run to obtain meaningful results, specified as a
positive real scalar in seconds.

For AC measurement, the simulation must run so that the ADC can generate 6 spectral
updates of the ADC output. The time to generate one spectral output based on Welch's
method is given by:

t=1.5·SamplingFrequencyRBW

where *SamplingFrequency* and *RBW* are the
sampling frequency and resolution bandwidth of the spectrum estimator inside the ADC
Testbench block.

This parameter is only reported by the testbench and is not editable.

**Data Types:** `double`

### **Set as model stop time** — Automatically set recommended min. simulation stop time as model stop time button

Click to automatically set the **Recommended min. simulation stop time
(s)** as the stop time of the Simulink® model.

### **Output result to base workspace** — Store detailed test results to base workspace off (default) | on

Store detailed test results in the base workspace for further processing at the end
of simulation. By default, this option is not selected.

### **Workspace variable name** — Name of the variable that stores detailed test results `adc_ac_out` (default) | character string

Name of the variable that stores detailed test results, specified as a character
string.

#### Dependencies

This parameter is only available when **Output result to base
workspace** is selected.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `VariableName` |
| **Type:** character vector |
| **Values:** character string |
| **Default:** `adc_ac_out` |

### **Show spectrum analyzer during simulation** — Displays spectrum analyzer during simulation off (default) | on

Displays spectrum analyzer during simulation. By default, this option is not
selected.
## Libraries

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Measure AC performance metrics of ADC output

The ADC AC Measurement block measures ADC AC performance metrics such as
signal to noise ratio (SNR), signal to noise and distortion radio (SINAD), spurious free
dynamic range (SFDR), effective number of bits (ENOB), noise floor, and conversion delay. You
can use ADC AC Measurement block to validate the ADC architectural models
provided in Mixed-Signal Blockset™, or you can use an ADC of your own implementation
