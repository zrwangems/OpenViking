---
type: simulink-block
title: 'ADC Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'adctestbench'
documentation_source_path: 'ref/adctestbench.html'
language: en
---

# ADC Testbench

## Ports

### Input

### **from adc digital** — Digital signal from ADC output scalar

Digital input signal from the ADC output, specified as a scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **from adc ready** — Conversion ready signal from ADC output scalar

Conversion ready signal from the ADC output, specified as a scalar. This signal
indicates when the ADC conversion process is complete.

**Data Types:** `double`
### Output

### **to adc analog** — Analog stimulus signal for ADC input scalar

Analog output stimulus signal for the ADC input, returned as a scalar.

**Data Types:** `double`

### **to adc start** — External start conversion clock for ADC scalar

External start conversion clock for ADC, returned as a scalar. The rising edge of
this signal starts the conversion process in ADC block.

**Data Types:** `double`

## Parameters

### **Measurement** — Select whether to measure DC or AC performance metrics `DC` (default) | `AC`

Select whether to measure static (DC) or dynamic (AC) performance metrics.

- Select `DC` to measure offset error and gain
  error.
- Select `AC` to measure SNR, SINAD, SFDR, ENOB, noise
  floor, and conversion delay.

### **Recommended min. simulation stop time (s)** — Minimum time simulation must run for meaningful result `2.048e-02` (default) | positive real scalar

Minimum time for which the simulation must run to obtain meaningful results,
specified as a positive real scalar in seconds.

- To measure DC performance, the simulation must run so that ADC can sample each
  digital code until the error tolerance is satisfied. When calculating stop time, the
  block assumes a minimum of 10 samples per code. You can calculate the expected
  number of samples (*Samples*) from error tolerance
  (*ErrorTolerance*):

  Samples=max(ceil(log2(1ErrorTolerance)),10)

  The recommended stop time in this case is:

  StopTime=(Samples·SampleInterval·2Nbits)+HoldOffTime

  where *SampleInterval* is the sample interval of the ADC
  Testbench and *Nbits* is the resolution of the ADC, and
  *Hold off time* is the defined by the **Hold off
  time** parameter.

  If there is jitter present in the signal, recommended stop time increases to
  account for the additional steps required to sample the jittery signal.

  **Note**

  If you manually set the sweep range using the **Sweep
  range** parameter, you may need to run the simulation longer than the
  recommended stop time.

  So, the **Recommended min. simulation stop time (s)**
  *T* is calculated by using the formula: T=1fanalog+HoldOffTime.
- To measure AC performance, the simulation must run so that the ADC can generate
  6 spectral updates of the ADC output. The time to generate one spectral output based
  on Welch's method is given by:

  t=1.5·SamplingFrequencyRBW

  where *SamplingFrequency* and *RBW* are the
  sampling frequency and resolution bandwidth of the spectrum estimator inside the ADC
  Testbench block.

This parameter is only reported by the testbench and is not editable.

**Data Types:** `double`

### **Set as model stop time** — Automatically set recommended min. simulation stop time as model stop time button

Click to automatically set the **Recommended min. simulation stop time
(s)** as the stop time of the Simulink® model.

### **Endpoint** — Measure DNL, INL using endpoint method on (default) | off

Measure the differential nonlinearity (DNL) error and integral nonlinearity (INL)
error using the endpoint method. This method uses the end points of the actual transfer
function to measure the DNL and INL error.

### **Best fit** — Measure DNL, INL using best fit method on (default) | off

Measure the differential nonlinearity (DNL) error and integral nonlinearity (INL)
error using the best fit method. This method uses a standard curve fitting technique to
find the best fit to measure the DNL and INL error.

### **Plot DC analysis result** — Plot DC analysis results button

Click to plot DC analysis result for further analysis. To perform a complete DC
analysis including integral nonlinearity (INL) and differential nonlinearity (DNL), use
the ADC DC
Measurement block.

#### Dependencies

This parameter is only available when **Measurement** option is
set to `DC`.

### **Export measurement result** — Store detailed test results to base workspace button

Click to store detailed test results to a spreadsheet (XLS file) or as
comma-separated values (CSV file) for further processing.

### Stimulus

### **Sample interval (s)** — Rate at which ADC Testbench polls input `1e-6` (default) | positive real scalar

Rate at which the ADC Testbench block polls its input, specified as
a positive real scalar in seconds. The testbench reads the input signal and updates
the value of its output to control the device under test.

#### Dependencies

To enable this parameter, set **Measurement** option as
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleInterval` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e-6` |

### **Distortion measurement type** — Type of distortion to measure `Harmonic` (default) | `Intermodulation`

Type of distortion the ADC Testbench block is set to measure,
specified as `Harmonic` or
`Intermodulation`.

If the block is calculating the **Analog stimulus frequency**
automatically,

- when measuring harmonic distortion, the calculated stimulus frequency is used
  directly.
- when measuring intermodulation distortion, the harmonics are chosen as one
  tenth above and below the calculated stimulus frequency.

#### Dependencies

To enable this parameter, set **Measurement** option as
`AC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `DistortionMeasurement` |
| **Type:** character vector |
| **Values:** `Harmonic` | `Intermodulation` |
| **Default:** `Harmonic` |

### **Analog stimulus frequency (Hz)** — Frequency of the analog input signal to ADC positive real scalar | positive real valued vector

Frequency of the analog input signal to an ADC block, specified as
a positive real scalar in hertz. **Analog stimulus frequency** must
match the input frequency to the ADC device under test. By default,
this parameter is calculated automatically. You can deselect **Set
automatically** to customize the value.

If the block is calculating the **Analog stimulus frequency**
automatically,

- when measuring harmonic distortion, the calculated stimulus frequency is used
  directly.
- when measuring intermodulation distortion, the harmonics are chosen as one
  tenth above and below the calculated stimulus frequency.

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

#### Dependencies

To enable this parameter, set **Measurement** option as
`AC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputFrequency` |
| **Type:** character vector |
| **Values:** positive real scalar | positive real valued vector |
| **Default:** `98632.8125` |

### **Resolution bandwidth (Hz)** — Resolution bandwidth positive real scalar

Resolution bandwidth, specified as a positive real scalar in hertz. This parameter
defines the smallest positive frequency that can be resolved. By default, this
parameter is calculated automatically. You can deselect **Set
automatically** to customize the value.

#### Dependencies

To enable this parameter, set **Measurement** option as
`AC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `RBW` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `976.5625` |

### **Start conversion frequency (Hz)** — Frequency of the start conversion clock of the ADC `1e6` (default) | positive real scalar

Frequency of the start conversion clock of the ADC, specified as a positive real
scalar in Hz. **Start conversion frequency (Hz)** must match the
frequency of the start conversion clock of the ADC block.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StartFreq` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e6` |

**Data Types:** `double`

### **RMS aperture jitter (s)** — RMS aperture jitter to be added by the start conversion clock `40e-12` (default) | positive real scalar

RMS aperture jitter to be added by the start conversion clock, specified as a
positive real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `RMSJitt` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `40e-12` |

**Data Types:** `double`

### **Error tolerance (LSB)** — Maximum difference between successive samples of analog signal `0.1` (default) | positive scalar in the range (`0, 1`]

Maximum allowed difference in the amplitude of the successive samples of the
analog input signal, specified as positive real scalar in least significant bit
(LSB).

#### Dependencies

To enable this parameter, set **Measurement** option as
`DC`.

**Data Types:** `double`

### **Automatically determine sweep range** — Automatically determine sweep range on (default) | off

Select to automatically determine the sweep range from the ADC dynamic input range
and target metrics. You can deselect this option to specify a custom sweep
range.

#### Dependencies

To enable this parameter, set **Measurement** option as
`DC`.

### **Sweep range** — Custom sweep range `[-1 1]` (default) | 2-element vector

Define a custom sweep range, specified as a 2-element vector.

#### Dependencies

To enable this parameter, set **Measurement** option as
`DC` and deselect the **Automatically determine
sweep range** parameter.

**Data Types:** `double`

### **Stop simulation on completion** — Stop simulation on completion on (default) | off

Select to stop the simulation on completion. You can deselect this option
terminate a simulation early.

#### Dependencies

To enable this parameter, set **Measurement** option as
`DC`.

### Setup

### **Autofill setup parameter** — Automatically propagate setup parameters from ADC button

Click to automatically propagate setup parameters from the ADC.

#### Dependencies

This parameter only works when the ADC is a Flash ADC
or a SAR ADC
from the Mixed-Signal Blockset.

### **Number of bits** — Number of physical output bits `10` (default) | positive real integer in the range `[1, 26]`

Number of physical output bits, specified as a unitless positive real integer in the
range `[1, 26]`. **Number of bits** determines the
resolution of the ADC.

#### Programmatic Use

- Use `get_param(gcb,'NBits')` to view the current
  **Number of bits**.
- Use `set_param(gcb,'NBits',value)` to set
  **Number of bits** to a specific value.

**Data Types:** `double`

### **Input range (V)** — ADC dynamic range `[-1 1]` (default) | 2-element row vector

ADC dynamic range, specified as a 2-element row vector in volts.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputRange` |
| **Type:** character vector |
| **Values:** 2-element row vector |
| **Default:** `[-1 1]` |

**Data Types:** `double`

### **Hold off time (s)** — Delay before measurement analysis `0` (default) | nonnegative real scalar

Delays measurement analysis to avoid corruption by transients, specified as a
nonnegative real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `HoldOffTime` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

**Data Types:** `double`

### **Show spectrum analyzer during simulation** — Displays spectrum analyzer during simulation off (default) | on

Displays spectrum analyzer during simulation. By default, this option is
deselected.

#### Dependencies

This parameter is only available when **Measurement** option is
set to `AC`.

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. By default, this option
is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `5` (default) | positive integer scalar

Number of samples of the input buffering available during simulation, specified as
a positive integer scalar.

Selecting different simulation solver or sampling strategies can change the number
of input samples needed to produce an accurate output sample. Set the **Buffer
size** to a large enough value that the input buffer contains all the input
samples required.

#### Dependencies

This parameter is only available when **Enable increased buffer
size** option is selected in the **Configuration**
tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NBuffer` |
| **Type:** character vector |
| **Values:** positive integer scalar |
| **Default:** `5` |

**Data Types:** `double`

### Target Metric

### **Autofill target metric** — Automatically propagate target metrics from ADC button

Click to automatically propagate target metrics from ADC.

#### Dependencies

- To enable this parameter, set **Measurement** option to
  `DC`.
- This parameter only works when the ADC is a Flash
  ADC or a SAR
  ADC from the Mixed-Signal Blockset.

### **Offset error** — Shifts quantization steps by specific value `1.5 LSB` (default) | real scalar

Shifts quantization steps by specific value, specified as a positive real scalar
in %FS, FS, or LSB.

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5
LSB wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

#### Dependencies

To enable this parameter, set **Measurement** option to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TargetOffsetError` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `1.5 LSB` |

**Data Types:** `double`

### **Gain error** — Error on the slope of ADC transfer curve `1 LSB` (default) | real scalar

Error on the slope of the straight line interpolating ADC transfer curve,
specified as a positive real scalar in least significant bit %FS, FS, or LSB.

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5
LSB wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

#### Dependencies

To enable this parameter, set **Measurement** option to
`DC`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TargetGainError` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `1 LSB` |

**Data Types:** `double`

## Libraries

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Measures DC and AC performance metrics of ADC output

The ADC Testbench block measures both DC and AC performance metrics. DC
performance metrics include offset error and gain error. AC performance metrics include signal
to noise ratio (SNR), signal to noise and distortion ratio (SINAD), spurious free dynamic
range (SFDR), effective number of bits (ENOB), noise floor, and conversion delay.

The ADC Testbench block generates the stimulus to drive the device under
test (DUT) from the **Stimulus** tab. The setup parameters for validating the
DUT are defined in the **Setup** tab and the target validation metrics are
defined in the **Target Metric** tab.

You can use the ADC Testbench block to validate the ADC architectural
models provided in Mixed-Signal Blockset™, or you can validate an ADC of your own implementation.
