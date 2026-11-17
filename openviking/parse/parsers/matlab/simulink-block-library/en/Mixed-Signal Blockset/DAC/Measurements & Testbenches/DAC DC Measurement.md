---
type: simulink-block
title: 'DAC DC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Measurements & Testbenches'
documentation_page: 'dacdcmeasurement'
documentation_source_path: 'ref/dacdcmeasurement.html'
language: en
---

# DAC DC Measurement

## Ports
```yaml
ports:
- name: digital
  summary: Digital input signal from DAC scalar
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: analog
  summary: Converted analog signal from DAC scalar
  direction: input
  data_types: double
- name: start
  summary: External clock to start conversion scalar
  direction: input
  data_types: double
```

### Input

### **digital** — Digital input signal from DAC scalar

Digital signal from a DAC, specified as a scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **analog** — Converted analog signal from DAC scalar

Converted analog signal from a DAC, specified as a scalar.

**Data Types:** `double`

### **start** — External clock to start conversion scalar

External clock to start conversion, specified as a scalar. This port determines
when digital-to-analog conversion process starts.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Input polarity
  summary: Polarity of input signal to DAC Bipolar (default) | Unipolar
  group: ''
  block_parameter: Polarity
  type: character vector
  values: Bipolar|Unipolar
  default: Bipolar
- name: Reference (V)
  summary: Reference voltage 2 (default) | real scalar
  group: ''
  block_parameter: Ref
  type: character vector
  values: real scalar
  default: '2'
- name: Bias (V)
  summary: Bias voltage added to output 0 (default) | real scalar
  group: ''
  block_parameter: Bias
  type: character vector
  values: real scalar
  default: '0'
- name: Settling time (s)
  summary: Time required for output to settle 3e-7 (default) | nonnegative real scalar
  group: ''
  block_parameter: SettlingTime
  type: character vector
  values: real scalar
  default: 3e-7
- name: Hold off time (s)
  summary: Delay before measurement analysis 1e-3 (default) | nonnegative real scalar
  group: ''
  block_parameter: HoldOffTime
  type: character vector
  values: nonnegative real scalar
  default: 1e-3
- name: Number of bits
  summary: Number of bits in input word 10 (default) | positive real integer
  group: ''
  block_parameter: NBits
  type: character vector
  values: positive real integer
  default: '10'
- name: Start conversion frequency (Hz)
  summary: Frequency of internal start conversion clock 1e6 (default) | positive real scalar
  group: ''
  block_parameter: StartFreq
  type: character vector
  values: positive real scalar
  default: 1e6
- name: Recommended simulation stop time (s)
  summary: Minimum time simulation must run for meaningful result 0.02148 (default) | positive real scalar
  group: ''
- name: Endpoint
  summary: Measure DNL, INL using endpoint method on (default) | off
  group: ''
- name: Best fit
  summary: Measure DNL, INL using best fit method on (default) | off
  group: ''
- name: Output result to base workspace
  summary: Store detailed test results to base workspace off (default) | on
  group: ''
- name: Workspace variable name
  summary: Name of the variable that stores detailed test results dac_dc_out (default) | character string
  group: ''
  block_parameter: VariableName
  type: character vector
  values: character string
  default: dac_dc_out
- name: Plot
  summary: Plot measurement results button
  group: ''
```

### **Input polarity** — Polarity of input signal to DAC `Bipolar` (default) | `Unipolar`

Polarity of the input signal to the DAC.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Polarity` |
| **Type:** character vector |
| **Values:** `Bipolar`|`Unipolar` |
| **Default:** `Bipolar` |

### **Reference (V)** — Reference voltage `2` (default) | real scalar

Reference voltage of the DAC, specified as a real scalar in volts. **Reference
(V)** helps determine the output from the input digital code,
**Number of bits**, and **Bias (V)** using the
equation:

DAC output = ((Digital input code2Number of bits)Reference)+Bias.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Ref` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `2` |

**Data Types:** `double`

### **Bias (V)** — Bias voltage added to output `0` (default) | real scalar

Bias voltage added to the output of the DAC, specified as a real scalar in volts.
**Bias (V)** helps determine the output from the input digital
code, **Number of bits**, and **Reference (V)** using
the equation:

DAC output = ((Digital input code2Number of bits)Reference)+Bias.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Bias` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

**Data Types:** `double`

### **Settling time (s)** — Time required for output to settle `3e-7` (default) | nonnegative real scalar

The time required for the output of the DAC to settle to within some fraction of its
final value, specified as a nonnegative real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTime` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `3e-7` |

**Data Types:** `double`

### **Hold off time (s)** — Delay before measurement analysis `1e-3` (default) | nonnegative real scalar

Delay before measurement analysis to avoid corruption by transients, specified as a
nonnegative real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `HoldOffTime` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `1e-3` |

**Data Types:** `double`

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

### **Start conversion frequency (Hz)** — Frequency of internal start conversion clock `1e6` (default) | positive real scalar

Frequency of the internal start conversion clock, specified as a real scalar in Hz.
The **Start conversion frequency** parameter determines the conversion
rate at the start of conversion.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StartFreq` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e6` |

**Data Types:** `double`

### **Recommended simulation stop time (s)** — Minimum time simulation must run for meaningful result `0.02148` (default) | positive real scalar

Minimum time the simulation must run to obtain meaningful results, specified as a
positive real scalar in seconds.

To measure DC performance, the simulation must run so that the DAC can sample each
digital code 20 times. Based on this assumption, the **Recommended simulation
stop time (s)**
*T* is given by:

T=Samples per bit(StartFreq/2Nbits+1)+Hold off time,

where *StartFreq* is the frequency of the conversion start clock
and *Nbits* is the resolution of the DAC.

The number of samples per bit is calculated using the equation:

Samples per bit = max(1Error tolerance,10).

This parameter is only reported by the block and is not editable.

**Data Types:** `double`

### **Endpoint** — Measure DNL, INL using endpoint method on (default) | off

Measure the differential nonlinearity (DNL) error and integral nonlinearity (INL)
error using the endpoint method. This method uses the endpoints of the actual transfer
function to measure the DNL and INL errors.

### **Best fit** — Measure DNL, INL using best fit method on (default) | off

Measure the differential nonlinearity (DNL) error and integral nonlinearity (INL)
error using the best fit method. This method uses a standard curve-fitting technique to
find the best fit to measure the DNL and INL errors.

### **Output result to base workspace** — Store detailed test results to base workspace off (default) | on

Select to store detailed test results to a `struct` in the base
workspace for further processing at the end of simulation. By default, this parameter is
deselected.

### **Workspace variable name** — Name of the variable that stores detailed test results `dac_dc_out` (default) | character string

Name of the variable that stores detailed test results, specified as a character
string.

#### Dependencies

To enable this parameter, select **Output result to base
workspace** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `VariableName` |
| **Type:** character vector |
| **Values:** character string |
| **Default:** `dac_dc_out` |

### **Plot** — Plot measurement results button

Click to plot measurement result for further analysis.
## Libraries

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Measure DC performance metrics of DAC output

The DAC DC Measurement block measures DAC DC performance metrics such as
offset error, gain error, integral nonlinearity (INL), and differential nonlinearity (DNL)
errors. You can use the DAC DC Measurement block to validate the DAC
architecture models provided in Mixed-Signal Blockset™, or you can use a DAC of your own implementation.
