---
type: simulink-block
title: 'DAC AC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Measurements and Testbenches / DAC'
documentation_page: 'dacacmeasurement'
documentation_source_path: 'ref/dacacmeasurement.html'
language: en
---

# DAC AC Measurement

## Ports

### Input

### **digital** — Digital input signal from DAC scalar

Digital input signal from a DAC, specified as a scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **analog** — Converted analog signal from DAC scalar

Converted analog signal from a DAC, specified as a scalar.

**Data Types:** `double`

### **start** — External clock to start conversion scalar

External clock to start conversion, specified as a scalar. This port determines
when digital-to-analog conversion process starts.

**Data Types:** `double`

## Parameters

### **Digital signal frequency (Hz)** — Frequency of digital input signal to DAC `1e3` (default) | positive real scalar

Frequency of the digital input signal to the DAC block, specified as
a positive real scalar in hertz. **Digital signal frequency (Hz)** must
match the input frequency of the DAC device under test.

**Digital input frequency (Hz)** needs to satisfy two
requirements:

- All the output codes of the DAC must be activated.
- The **Digital signal frequency (Hz)** must not share any common
  multiples other than 1 with the **Conversion start frequency
  (Hz)**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputFrequency` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e3` |

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

### **Settling time tolerance (LSB)** — Tolerance for calculating settling time `0.5` (default) | positive real scalar

The tolerance allowed for calculating settling time, specified as a positive real
scalar in LSB. The output of the DAC must settle within the **Settling time
tolerance (LSB)** by **Settling time (s)**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTimeTolerance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.5` |

**Data Types:** `double`

### **Hold off time (s)** — Delay before measurement analysis to avoid corruption by transients `0` (default) | nonnegative real scalar

Delay before measurement analysis to avoid corruption by transients, specified as a
nonnegative real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `HoldOffTime` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### **Recommended simulation stop time (s)** — Minimum time simulation must run for meaningful result `0.09` (default) | positive real scalar

Minimum time the simulation must run to obtain meaningful results, specified as a
positive real scalar in seconds.

To measure AC performance, the simulation must run so that the DAC can generate six
spectral updates of the DAC output. So, the **Recommended simulation stop time
(s)**
*T* is given by [1]:

T=6(1.5RBW+Hold off time),

where *RBW* is the resolution bandwidth of the spectrum estimator
inside the DAC Testbench block and is given by the equation: RBW=[min(Input frequency)0.1].

This parameter is only reported by the block and is not editable.

**Data Types:** `double`

### **Output result to base workspace** — Store detailed test results to base workspace off (default) | on

Store detailed test results to a struct in the base workspace for further processing
at the end of simulation. By default, this parameter is deselected.

### **Workspace variable name** — Name of the variable that stores detailed test results `dac_ac_out` (default) | character string

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
| **Default:** `dac_ac_out` |

### **Show spectrum analyzer during simulation** — Displays Spectrum Analyzer during simulation on (default) | off

Select this parameter to display the Spectrum Analyzer window during simulation. By
default, this parameter is selected.

## Libraries

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Measure AC performance metrics of DAC output

The DAC AC Measurement block measures DAC AC performance metrics such as
signal-to-noise ratio (SNR), signal to noise and distortion radio (SINAD), spurious-free
dynamic range (SFDR), effective number of bits (ENOB), and noise floor. You can use DAC
AC Measurement block to validate the DAC architecture models provided in Mixed-Signal Blockset™, or you can use a DAC of your own implementation
