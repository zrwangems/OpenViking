---
type: simulink-block
title: 'Complex to Magnitude-Angle'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complextomagnitudeangle'
documentation_source_path: 'slref/complextomagnitudeangle.html'
language: en
---

# Complex to Magnitude-Angle

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: Magnitude scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_2
  summary: Radian phase angle scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Complex input signal that the block computes and outputs the magnitude
and/or the phase angle.

#### Limitations

Fixed-point data types are supported only when you set the
**Approximation method** to
`CORDIC`.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Magnitude scalar | vector | matrix

Output signal that is the magnitude and/or phase angle of the input
signal. To choose the output, set the **Output**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — Radian phase angle scalar | vector | matrix

Radian phase angle, returned as a real-valued scalar, vector, or
matrix.

#### Dependencies

- To enable this port, set **Output** to
  `Magnitude and angle` or
  `Angle`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Output
  summary: Magnitude and/or phase angle output specification Magnitude and angle (default) | Magnitude | Angle
  group: ''
  block_parameter: Output
  type: character vector
  values: '''Magnitude and angle'' | ''Magnitude'' | ''Angle'''
  default: '''Magnitude and angle'''
- name: Approximation method
  summary: Approximation method None (default) | CORDIC
  group: ''
  block_parameter: ApproximationMethod
  type: character vector
  values: '''None'' | ''CORDIC'''
  default: '''None'''
- name: Number of iterations
  summary: Number of iterations for CORDIC algorithm 11 (default) | positive integer, less than or equal to word length of
    fixed-point input
  group: ''
  block_parameter: NumberOfIterations
  type: character vector
  values: positive integer, less than or equal to word length of fixed-point input
  default: '''11'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: ''
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
```

### **Output** — Magnitude and/or phase angle output specification `Magnitude and angle` (default) | `Magnitude` | `Angle`

Specify if the output is the magnitude and/or the phase angle in radians
of the input signal.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `Output` |
| **Type:** character vector |
| **Values:** `'Magnitude and angle'` | `'Magnitude'` | `'Angle'` |
| **Default:** `'Magnitude and angle'` |

### **Approximation method** — Approximation method `None` (default) | `CORDIC`

Specify the type of approximation for computing output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating-point | You want to use the default Taylor series algorithm. |
| `CORDIC` | Floating-point and fixed-point | You want a fast, approximate calculation. |

The block uses these data type propagation rules.

| Data Type of Complex Input | Approximation Method | Data Type of Magnitude Output | Data Type of Angle Output |
| --- | --- | --- | --- |
| Floating point | `None` or `CORDIC` | Same as input | Same as input |
| Signed, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*)  where:  - *`WL`* = input word   length of the magnitude + 2 + 1 - *`FL`* = input fraction   length of the magnitude | `fixdt`(1, *`WL`* + 2, *`FL`*)  where:  - *`WL`* = input word   length of the magnitude -3, for best precision for   [`-pi, pi`) - *`FL`* = input fraction   length of the angle |
| Unsigned, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*)  where:  - *`WL`* = input word   length of the magnitude + 2 - *`FL`* = input fraction   length of the magnitude | `fixdt`(1, *`WL`* + 3, *`FL`*)  where:  - *`WL`* = input word   length of the angle - 2, for best precision   fraction length for range [0, pi/2] - *`FL`* = input fraction   length of the angle |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'None' | 'CORDIC'` |
| **Default:** `'None'` |

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | positive integer, less than or equal to word length of fixed-point input

Number of iterations the CORDIC algorithm performs, specified as a
positive integer-valued scalar. Increasing the number of iterations can
produce more accurate results but also increases the expense of the
computation and adds latency.

| Data Type of Block Inputs | Value You Can Specify |
| --- | --- |
| Floating-point | A positive integer. The maximum value is 52 for double or 23 for single. |
| Fixed-point | A positive integer that does not exceed the word length of the magnitude input or the word length of the phase angle input, whichever value is smaller. |

#### Dependencies

To enable this parameter, set **Approximation
method** to `CORDIC`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfIterations` |
| **Type:** character vector |
| **Values:** positive integer, less than or equal to word length of fixed-point input |
| **Default:** `'11'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |
## Libraries

Simulink / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024b: Complex to Magnitude-Angle block supports fixed-point inputs

Complex to Magnitude-Angle block now
supports the CORDIC approximation method. This method allows fixed-point inputs at
input **Port\_1**. To select the CORDIC method, set the new
**Approximation method** parameter to
`CORDIC`.

When you select the CORDIC method, the block icon updates. The new parameter,
Number of iterations, lets you define the number of iterations for the CORDIC
algorithm.

Complex to Magnitude-Angle block icon with CORDIC approximation method input

## Description

Compute magnitude and/or phase angle of complex signal

The Complex to Magnitude-Angle block outputs the magnitude and/or phase angle of the
input signal, depending on the setting of the **Output** parameter. The
outputs are real values of the same data type as the block input. The input can be an
array of complex signals, in which case the output signals are also arrays. The
magnitude signal array contains the magnitudes of the corresponding complex input
elements. The angle output similarly contains the angles of the input elements.
