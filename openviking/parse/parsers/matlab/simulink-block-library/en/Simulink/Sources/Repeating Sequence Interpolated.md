---
type: simulink-block
title: 'Repeating Sequence Interpolated'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequenceinterpolated'
documentation_source_path: 'slref/repeatingsequenceinterpolated.html'
language: en
---

# Repeating Sequence Interpolated

## Ports
```yaml
ports:
- name: Port_1
  summary: Periodic output signal scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Output

### **Port\_1** — Periodic output signal scalar

Output signal generated based on the values in the **Vector of time
values** and **Vector of output values**
parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Vector of output values
  summary: Vector of output values [3 1 4 2 1].' (default) | vector
  group: Main
  block_parameter: OutValues
  type: character vector
  values: vector
  default: '''[3 1 4 2 1].'''''
- name: Vector of time values
  summary: Vector of time values [0 0.1 0.5 0.6 1].' (default) | vector
  group: Main
  block_parameter: TimeValues
  type: character vector
  values: vector
  default: '''[0 0.1 0.5 0.6 1].'''''
- name: Lookup Method
  summary: Lookup method for output Interpolation-Use End Values (default) | Use Input Nearest | Use Input Below | Use Input
    Above
  group: Main
  block_parameter: LookUpMeth
  type: character vector
  values: '''Interpolation-Use End Values'' | ''Use Input Nearest'' | ''Use Input Below'' | ''Use Input Above'''
  default: '''Interpolation-Use End Values'''
- name: Sample time
  summary: Time interval between samples 0.01 (default) | scalar
  group: Main
  block_parameter: tsamp
  type: character vector
  values: scalar
  default: '''0.01'''
- name: Output minimum
  summary: Minimum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMin
  values: '''[]'' (default) | scalar in quotes'
- name: Output maximum
  summary: Maximum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMax
  values: '''[]'' (default) | scalar in quotes'
- name: Output data type
  summary: 'Specify the output data type double (default) | Inherit: Inherit via back propagation | single | int8 | int32
    | uint32 | int64 | uint64 | fixdt(1,16,2^0,0) | <data type expression> | ...'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via back propagation'' | ''double'' | ''single'' | ''int8'' | ''uint8'' | int16 | ''uint16''
    | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | fixdt(1,16,0) | fixdt(1,16,2^0,0) | fixdt(1,16,2^0,0). ''<data type
    expression>'''
  default: '''double'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Signal Attributes
  block_parameter: LockScale
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### Main

### **Vector of output values** — Vector of output values `[3 1 4 2 1].'` (default) | vector

Vector of output values that specify the output waveform. Each element corresponds to
the time value in the **Vector of time values**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutValues` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'[3 1 4 2 1].''` |

### **Vector of time values** — Vector of time values `[0 0.1 0.5 0.6 1].'` (default) | vector

Specify the column vector containing time values. The time values must
be strictly increasing, and the vector must have the same size as the
vector of output values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeValues` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'[0 0.1 0.5 0.6 1].''` |

### **Lookup Method** — Lookup method for output `Interpolation-Use End Values` (default) | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

Specify the lookup method to determine the output between data
points.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LookUpMeth` |
| **Type**: character vector |
| **Values**: `'Interpolation-Use End Values'` | `'Use Input Nearest'` | `'Use Input Below'` | `'Use Input Above'` |
| **Default**: `'Interpolation-Use End Values'` |

### **Sample time** — Time interval between samples `0.01` (default) | scalar

Specify the time interval between samples. To inherit the sample time,
set this parameter to `-1`. See Specify Sample Time
for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `tsamp` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.01'` |

### Signal Attributes

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Specify the output data type `double` (default) | `Inherit: Inherit via back propagation` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
| **Default**: `'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |
## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Cannot be used inside a triggered subsystem hierarchy.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Output discrete-time sequence and repeat, interpolating between data points

The Repeating Sequence Interpolated block outputs a periodic discrete-time
sequence based on the values in **Vector of time values** and
**Vector of output values** parameters. Between data points, the
block uses the method you specify for the **Lookup Method** parameter
to determine the output.
