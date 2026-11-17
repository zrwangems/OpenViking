---
type: simulink-block
title: 'Interleaved ADC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Architectures'
documentation_page: 'interleavedadc'
documentation_source_path: 'ref/interleavedadc.html'
language: en
---

# Interleaved ADC

## Ports
```yaml
ports:
- name: analog
  summary: Analog input signal scalar
  direction: input
  data_types: double
- name: start
  summary: External clock to start conversion scalar | vector
  direction: input
  data_types: double | Boolean
- name: Offset calibration
  summary: Offset error calibration at analog input scalar | vector
  direction: input
  data_types: double
- name: Gain calibration
  summary: Gain error calibration at analog input scalar | vector
  direction: input
  data_types: double
- name: digital
  summary: Converted digital output signal scalar | vector
  direction: output
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: ready
  summary: Determines whether analog to digital conversion is complete scalar | vector
  direction: output
  data_types: double | Boolean
```

### Input

### **analog** — Analog input signal scalar

Analog input signal, specified as a scalar.

**Data Types:** `double`

### **start** — External clock to start conversion scalar | vector

External clock to start conversion, specified as a scalar or a vector. If
specified as a vector, the number of elements in the vector must be equal to the
number of ADC cores.

The analog to digital conversion process starts at the rising edge of the signal
at the **start** port.

**Data Types:** `double` | `Boolean`

### **Offset calibration** — Offset error calibration at analog input scalar | vector

Add to the ADC input to calibrate the offset error, specified as a scalar or a
vector. If specified as a scalar, it is demultiplexed over analog inputs of the ADC
cores. If specified as a vector, the number of elements in the vector must be equal to
the number of ADC cores. The vector elements are applied per ADC core.

You can also use the port to dynamically calibrate the offset error to each ADC
core.

**Data Types:** `double`

### **Gain calibration** — Gain error calibration at analog input scalar | vector

Multiply the analog input to calibrate the gain error, specified as a scalar or a
vector. If specified as a scalar, it is demultiplexed over analog inputs of the ADC
cores. If specified as a vector, the number of elements in the vector must be equal to
the number of ADC cores. The vector elements are applied per ADC core.

You can also use the port to dynamically calibrate the gain error to each ADC
core.

**Data Types:** `double`
### Output

### **digital** — Converted digital output signal scalar | vector

Converted digital output signal, returned as a scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ready** — Determines whether analog to digital conversion is complete scalar | vector

Determines whether the analog to digital conversion is complete, returned as a
scalar.

Usually, the data type of the **ready** signal is the same as the
data type of the **start** signal. But if the start signal is a
fixed-point type or a 64-bit integer type, the data type of the
**ready** signal defaults to Boolean.

**Data Types:** `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Number of bits
  summary: Number of physical output bits for all ADC cores 8 (default) | scalar | vector
  group: Configuration
  block_parameter: NBits
  type: character vector
  values: scalar | vector
  default: '8'
- name: Input range
  summary: ADC dynamic range [-1 1] (default) | 2-element row vector | [NADCs x 2] matrix
  group: Configuration
  block_parameter: InputRange
  type: character vector
  values: 2-element row vector | [NADCs x 2] matrix
  default: '[-1 1]'
- name: Linearly interpolate analog input to find sampled value
  summary: Sub-sample interpolation with sinusoidal conversion start signal off (default) | on
  group: Configuration
- name: Number of ADCs (N)
  summary: Number of ADC cores to interleave 4 (default) | positive real integer
  group: Configuration
  block_parameter: NADCs
  type: character vector
  values: positive real integer
  default: '4'
- name: Match output to input scale
  summary: Inherit output polarity and data type from input off (default) | on
  group: Configuration
- name: Output polarity
  summary: Defines ADC output polarity Auto (default) | Bipolar | Unipolar
  group: Configuration
  block_parameter: OutputPolarity
  type: character vector
  values: Auto | Bipolar | Unipolar
  default: Auto
- name: Output data type
  summary: Defines ADC output data type double (default) | single | (u)int8 | (u)int16 | (u)int32 | fixdt(OutputPolarity,NBits)
  group: Configuration
  block_parameter: OutDataType
  type: character vector
  values: double | single | (u)int8 | (u)int16 | (u)int32 | fixdt(OutputPolarity,NBits)
  default: double
- name: Convert the output to scalar
  summary: Convert output to scalar on (default) | off
  group: Configuration
- name: Sample time
  summary: Fixed-step sample rate 6.25e-12 (default) | positive real scalar
  group: Configuration
  block_parameter: SampleTime
  type: character vector
  values: positive real scalar
  default: '6.25e-12'
- name: Simulate using
  summary: Define how to simulate ADC Code generation (default) | Interpreted execution
  group: Configuration
- name: Enable linearity impairments
  summary: Enable linearity impairments in ADC simulation off (default) | on
  group: Impairments
- name: Offset error
  summary: Shifts quantization steps by specific value 0 LSB (default) | real scalar
  group: Impairments
  block_parameter: OffsetError
  type: character vector
  values: real scalar
  default: 0 LSB
- name: Gain error
  summary: Error on slope of ADC transfer curve 0 LSB (default) | real scalar
  group: Impairments
  block_parameter: GainError
  type: character vector
  values: real scalar
  default: 0 LSB
- name: Enable timing impairments
  summary: Enable timing impairments in ADC simulation off (default) | on
  group: Impairments
- name: Conversion delay (seconds)
  summary: Latency of ADC 0 (default) | nonnegative real scalar
  group: Impairments
  block_parameter: ConversionDelay
  type: character vector
  values: real scalar
  default: '0'
- name: Enable offset calibration port
  summary: Enable offset calibration port off (default) | on
  group: Impairments
- name: Enable gain calibration port
  summary: Enable gain calibration port off (default) | on
  group: Impairments
```

### Configuration

### **Number of bits** — Number of physical output bits for all ADC cores `8` (default) | scalar | vector

Number of physical output bits for all ADC cores, specified as a unitless positive
real integer scalar or vector with length **NADCs**. **Number
of bits** determines the resolution of the ADC.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NBits` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `8` |

**Data Types:** `double`

### **Input range** — ADC dynamic range `[-1 1]` (default) | 2-element row vector | [**NADCs** x 2] matrix

ADC dynamic range, specified as a 2-element row vector in volts.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputRange` |
| **Type:** character vector |
| **Values:** 2-element row vector | [**NADCs** x 2] matrix |
| **Default:** `[-1 1]` |

**Data Types:** `double`

### **Linearly interpolate analog input to find sampled value** — Sub-sample interpolation with sinusoidal conversion start signal off (default) | on

Select to enable sub-sample interpolation with sinusoidal conversion start signal.
This approximates the input value at the zero-crossing of the input clock.

For square conversion start signals, disable this parameter.

### **Number of ADCs (N)** — Number of ADC cores to interleave `4` (default) | positive real integer

Number of ADC cores to interleave, specified as a positive real integer.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NADCs` |
| **Type:** character vector |
| **Values:** positive real integer |
| **Default:** `4` |

**Data Types:** `double`

### **Match output to input scale** — Inherit output polarity and data type from input off (default) | on

Inherit the output polarity and data type from the analog input signal to the ADC.
If you select this option, the ADC ignores the **Output polarity**
and **Output data type** parameters. The ADC output has the same
polarity as the input and the data type is double.

### **Output polarity** — Defines ADC output polarity `Auto` (default) | `Bipolar` | `Unipolar`

Defines the ADC output data polarity.

If **Output polarity** is set to `Auto`,
the minimum and maximum values of the output are determined by the polarity of the
**Input range**.

If **Output polarity** is set to
`Bipolar`, the outputs are between
`-2NBits-1` and
`2NBits-1-1`.

If **Output polarity** is set to
`Unipolar`, the outputs are between `0`
and `2NBits-1`.

#### Dependencies

To enable this parameter, deselect the **Match output to input
scale** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputPolarity` |
| **Type:** character vector |
| **Values:** `Auto` | `Bipolar` | `Unipolar` |
| **Default:** `Auto` |

### **Output data type** — Defines ADC output data type `double` (default) | `single` | `(u)int8` | `(u)int16` | `(u)int32` | `fixdt(OutputPolarity,NBits)`

Defines ADC output data type.

#### Dependencies

To enable this parameter, deselect the **Match output to input
scale** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutDataType` |
| **Type:** character vector |
| **Values:** `double` | `single` | `(u)int8` | `(u)int16` | `(u)int32` | `fixdt(OutputPolarity,NBits)` |
| **Default:** `double` |

### **Convert the output to scalar** — Convert output to scalar on (default) | off

Convert the output of the ADC to scalar. The block selects the most recent
conversion result using an internal counter to produce the scalar output.

### **Sample time** — Fixed-step sample rate `6.25e-12` (default) | positive real scalar

Fixed-step sample rate, specified as a positive real scalar. When using in SerDes
systems, **Sample time** represents the IBIS-AMI sample
interval.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `6.25e-12` |

### **Simulate using** — Define how to simulate ADC `Code generation` (default) | `Interpreted execution`

Define how the Interleaved ADC block is used in the simulation. You
can use the block as a Simulink® block, or use the System object™ implementation (either interpreted or code generation) for more
control.

### Impairments

### **Enable linearity impairments** — Enable linearity impairments in ADC simulation off (default) | on

Select to enable linearity impairments such as offset error and gain error in ADC
simulation. By default, this option is deselected.

### **Offset error** — Shifts quantization steps by specific value `0 LSB` (default) | real scalar

Shifts quantization steps by specific value, specified as a scalar in %FS, FS, or
LSB.

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

### **Gain error** — Error on slope of ADC transfer curve `0 LSB` (default) | real scalar

Error on the slope of the straight line that interpolates the ADC transfer curve,
specified as a real scalar in %FS, FS, or LSB.

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

### **Enable timing impairments** — Enable timing impairments in ADC simulation off (default) | on

Select to enable timing impairments such as conversion delay in ADC simulation. By
default, this option is deselected.

### **Conversion delay (seconds)** — Latency of ADC `0` (default) | nonnegative real scalar

Latency of the analog to digital converter, specified as a nonnegative real
scalar. If specified as a fraction, the Interleaved ADC block rounds it
to the closest integer multiple of the sample time.

#### Dependencies

This parameter is only available when **Enable timing
impairments** is selected. If you are using the Flash ADC
in the System object mode, this value is rounded to the nearest multiple of the sample
interval.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ConversionDelay` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

**Data Types:** `double`

### **Enable offset calibration port** — Enable offset calibration port off (default) | on

Select to enable the **offset calibration** port. The value at
this port is added to the analog input to calibrate the offset error after gain error
calibration is complete.

### **Enable gain calibration port** — Enable gain calibration port off (default) | on

Select to enable the **gain calibration** port. The value at this
port is multiplied by the analog input to calibrate the gain error.
## Libraries

Mixed-Signal Blockset / ADC / Architectures

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Time-interleaved ADC model

Use the Interleaved ADC to support the time-interleaved ADC models in your
design. This block is compatible with the SerDes Toolbox™ IBIS-AMI models. You can use the block to model over an infinite input range and
number of bits. This block uses Flash ADC as its
core.

An interleaved ADC consists of a set of ADC cores wired in parallel.

Interleaved ADC model

At the rising edge of a signal at the **start** port, the ADC starts a
conversion on the current core and indexes the input switch to the next core. When the
conversion is complete, the output switch changes to the core in question. The conversion
result is available at the **digital** port. The block also sends the rising
edge of a signal on the **ready** port. This result is held until the next
conversion is complete.

While a conversion is ongoing in one ADC core, the block can start new conversions in the
other cores, increasing the throughput compared to a single core ADC.
