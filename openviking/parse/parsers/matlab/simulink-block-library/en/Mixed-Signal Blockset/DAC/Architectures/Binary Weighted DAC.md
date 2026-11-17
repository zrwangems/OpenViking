---
type: simulink-block
title: 'Binary Weighted DAC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Architectures'
documentation_page: 'binaryweighteddac'
documentation_source_path: 'ref/binaryweighteddac.html'
language: en
---

# Binary Weighted DAC

## Ports
```yaml
ports:
- name: digital
  summary: Digital input signal to DAC integer
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: start
  summary: External clock to start conversion scalar
  direction: input
  data_types: double
- name: analog
  summary: Converted analog output signal scalar
  direction: output
  data_types: double
- name: ready
  summary: Indicates whether digital-to-analog conversion is complete scalar
  direction: output
  data_types: double
```

### Input

### **digital** — Digital input signal to DAC integer

Digital input signal to DAC, specified as an integer.

If the **Input polarity** parameter is set to
`Bipolar`, the allowed range of the signal is
[−2(*NBits*-1),
2(*NBits*-1)-1].

If the **Input polarity** parameter is set to
`Unipolar`, the allowed range of the signal is [0,
2*NBits*-1].

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **start** — External clock to start conversion scalar

External clock to start conversion, specified as a scalar. The digital-to-analog
conversion process starts at the rising edge of the signal at the
**start** port.

#### Dependencies

To enable this port, select **Use external start clock** in the
**General** tab.

**Data Types:** `double`
### Output

### **analog** — Converted analog output signal scalar

Converted analog output signal, returned as a scalar.

**Data Types:** `double`

### **ready** — Indicates whether digital-to-analog conversion is complete scalar

Indicates whether the digital-to-analog conversion is complete, returned as a
scalar.

#### Dependencies

To enable this port, select **Show ready port** in the
**General** tab.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Number of bits
  summary: Number of bits in input word 5 (default) | positive real integer
  group: General
  block_parameter: NBits
  type: character vector
  values: positive real integer
  default: '5'
- name: Input polarity
  summary: Polarity of input signal to DAC Bipolar (default) | Unipolar
  group: General
  block_parameter: Polarity
  type: character vector
  values: Bipolar|Unipolar
  default: Bipolar
- name: Use external start clock
  summary: Connect to external start conversion clock on (default) | off
  group: General
- name: Conversion start frequency (Hz)
  summary: Frequency of internal start conversion clock 1e6 (default) | positive real scalar
  group: General
  block_parameter: StartFreq
  type: character vector
  values: positive real scalar
  default: 1e6
- name: Reference (V)
  summary: Reference voltage 2 (default) | real scalar
  group: General
  block_parameter: Ref
  type: character vector
  values: real scalar
  default: '2'
- name: Bias (V)
  summary: Bias voltage added to output 0 (default) | real scalar
  group: General
  block_parameter: Bias
  type: character vector
  values: real scalar
  default: '0'
- name: Show ready port
  summary: Enable ready port on block off (default) | on
  group: General
- name: Enable linearity impairments
  summary: Enable offset and gain errors in DAC simulation on (default) | off
  group: Impairments
- name: Offset error
  summary: Shifts quantization steps by specific value 0 LSB (default) | real scalar
  group: Impairments
  block_parameter: OffsetError
  type: character vector
  values: real scalar
  default: 0 LSB
- name: Gain error
  summary: Error in slope of DAC transfer curve 0 LSB (default) | real scalar
  group: Impairments
  block_parameter: GainError
  type: character vector
  values: real scalar
  default: 0 LSB
- name: Enable timing impairments
  summary: Enable timing impairments in DAC simulation on (default) | off
  group: Impairments
- name: Specify switch timing using
  summary: Specify how DAC calculates switch timing Settling time (default) | Slew rate
  group: Impairments
- name: Settling time (s)
  summary: Time required for output to settle 2e-7 (default) | nonnegative real scalar
  group: Impairments
  block_parameter: SettlingTime
  type: character vector
  values: real scalar
  default: 2e-7
- name: Settling time tolerance (LSB)
  summary: Tolerance for calculating settling time 0.5 (default) | positive real scalar
  group: Impairments
  block_parameter: SettlingTimeTolerance
  type: character vector
  values: positive real scalar
  default: '0.5'
- name: Rising slew rate
  summary: Switch rising slew rate for DAC 5015625 (default) | positive real scalar | positive real vector
  group: Impairments
  block_parameter: RisingSlewRate
  type: character vector
  values: positive real scalar | positive real vector
  default: '5015625'
- name: Falling slew rate
  summary: Switch falling slew rate for DAC -5015625 (default) | negative real scalar | negative real vector
  group: Impairments
  block_parameter: FallingSlewRate
  type: character vector
  values: negative real scalar | negative real vector
  default: '-5015625'
```

### General

### **Number of bits** — Number of bits in input word `5` (default) | positive real integer

Number of bits in the input word, specified as a unitless positive real integer.
**Number of bits** determines the resolution of the DAC.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NBits` |
| **Type:** character vector |
| **Values:** positive real integer |
| **Default:** `5` |

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

### **Use external start clock** — Connect to external start conversion clock on (default) | off

Select to connect to an external start conversion clock. By default, this option
is selected. If you deselect this option, a Sampling Clock
Source block inside the Segmented DAC is used to generate the start
conversion clock

### **Conversion start frequency (Hz)** — Frequency of internal start conversion clock `1e6` (default) | positive real scalar

Frequency of the internal start conversion clock, specified as a real scalar in Hz.
The **Conversion start frequency** parameter determines the conversion
rate at the start of conversion.

#### Dependencies

To enable this parameter, deselect **Use external start
clock**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StartFreq` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e6` |

**Data Types:** `double`

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

### **Show ready port** — Enable ready port on block off (default) | on

Select to enable the **ready** port on the block. This option is
deselected by default.

### Impairments

### **Enable linearity impairments** — Enable offset and gain errors in DAC simulation on (default) | off

Select to enable impairments such as offset error and gain error in DAC
simulation. This parameter is selected. by default.

### **Offset error** — Shifts quantization steps by specific value `0 LSB` (default) | real scalar

Shifts quantization steps by a specific value, specified as a scalar in %FS
(percentage full scale), FS (full scale), or LSB (least significant bit).

**Offset error** is applied before **Reference
(V)** and **Bias (V)**.

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5
LSB wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

#### Dependencies

To enable this parameter, select **Enable linearity
impairments** in the **Impairments** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OffsetError` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0 LSB` |

**Data Types:** `double`

### **Gain error** — Error in slope of DAC transfer curve `0 LSB` (default) | real scalar

Error in the slope of the straight line interpolating the DAC transfer curve,
specified as a real scalar in %FS (percentage full scale), FS (full scale), or LSB
(least significant bit).

**Gain error** is applied before **Reference
(V)** and **Bias (V)**.

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5
LSB wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

#### Dependencies

To enable this parameter, select **Enable linearity
impairments** in the **Impairments** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `GainError` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0 LSB` |

**Data Types:** `double`

### **Enable timing impairments** — Enable timing impairments in DAC simulation on (default) | off

Select to enable timing impairments such as settling time or slew rate in DAC
simulation. This parameter is selected. by default.

### **Specify switch timing using** — Specify how DAC calculates switch timing `Settling time` (default) | `Slew rate`

Specify whether the Binary Weighted DAC calculates switch timing using the
settling time parameters or the slew rate parameters.

#### Dependencies

To enable this parameter, select **Enable timing impairments**
in the **Impairments** tab.

### **Settling time (s)** — Time required for output to settle `2e-7` (default) | nonnegative real scalar

The time required for the output of the DAC to settle to within some fraction of
its final value, specified as a nonnegative real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable timing impairments**
and set **Specify switch timing using** to
`Settling time` in the **Impairments**
tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTime` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `2e-7` |

**Data Types:** `double`

### **Settling time tolerance (LSB)** — Tolerance for calculating settling time `0.5` (default) | positive real scalar

The tolerance allowed for calculating settling time, specified as a positive real
scalar in LSB. The output of the DAC must settle within the **Settling time
tolerance (LSB)** by **Settling time (s)**.

#### Dependencies

To enable this parameter, select **Enable timing impairments**
and set **Specify switch timing using** to
`Settling time` in the **Impairments**
tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTimeTolerance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.5` |

**Data Types:** `double`

### **Rising slew rate** — Switch rising slew rate for DAC `5015625` (default) | positive real scalar | positive real vector

Switch the rising slew rate for the DAC, specified as a positive real scalar or
vector. If **Rising slew rate** is scalar, it specifies the
same slew rate for all the switches. If **Rising slew rate** is
a vector of length *Nbits*, it specifies the slew rate for each
individual switch.

#### Dependencies

To enable this parameter, select **Enable timing impairments**
and set **Specify switch timing using** to `Slew
rate` in the **Impairments** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `RisingSlewRate` |
| **Type:** character vector |
| **Values:** positive real scalar | positive real vector |
| **Default:** `5015625` |

### **Falling slew rate** — Switch falling slew rate for DAC `-5015625` (default) | negative real scalar | negative real vector

Switch the falling slew rate for the DAC, specified as a positive real scalar or
vector. If **Falling slew rate** is scalar, it specifies the
same slew rate for all the switches. If **Falling slew rate**
is a vector of length *Nbits*, it specifies the slew rate for each
individual switch.

#### Dependencies

To enable this parameter, select **Enable timing impairments**
and set **Specify switch timing using** to `Slew
rate` in the **Impairments** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FallingSlewRate` |
| **Type:** character vector |
| **Values:** negative real scalar | negative real vector |
| **Default:** `-5015625` |
## Libraries

Mixed-Signal Blockset / DAC / Architectures

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

N-bit DAC based on R-2R weighted resistor architecture

The R-2R DAC is one of the most common types of Binary-Weighted DACs. It consists of a
parallel binary-weighted resistor bank. Each digital level is converted to an equivalent
analog signal by the resistor bank.

The input/output transfer curve of the binary weighted DAC can be nonmonotonic, which
means that the transfer curve can reverse its direction.

The R-2R DAC architecture is low resolution and consumes more power due to the large
number of resistors required to implement the architecture.
