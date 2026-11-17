---
type: simulink-block
title: 'Shelving Equalizer Design'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'shelvingequalizerdesign'
documentation_source_path: 'ref/shelvingequalizerdesign.html'
language: en
---

# Shelving Equalizer Design

## Ports
```yaml
ports:
- name: G
  summary: Peak gain (dB) real scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: S
  summary: Slope coefficient positive scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Fc
  summary: Normalized cutoff frequency scalar in range [0,1]
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: T
  summary: Filter type 0 (low-shelf) | 1 (high-shelf)
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated
- name: Num
  summary: Numerator filter coefficients three-element row vector
  direction: output
  data_types: single | double
- name: Den
  summary: Denominator filter coefficients three-element row vector
  direction: output
  data_types: single | double
```

### Input

### **G** — Peak gain (dB) real scalar

Use this port to specify the value of the **Peak gain
(dB)** parameter.

#### Dependencies

To enable this port, select the **Specify peak gain from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **S** — Slope coefficient positive scalar

Use this port to specify the value of the **Slope
coefficient** parameter.

#### Dependencies

To enable this port, select the **Specify slope coefficient from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — Normalized cutoff frequency scalar in range [0,1]

Use this port to specify the value of the **Normalized cutoff
frequency** parameter.

#### Dependencies

To enable this port, select the **Specify normalized cutoff frequency
from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **T** — Filter type `0` (low-shelf) | `1` (high-shelf)

Use this port to specify the value of the **Filter
type** parameter; `0` corresponds to a low-shelf
equalizer and `1` corresponds to a high-shelf equalizer.

#### Dependencies

To enable this port, select the **Specify filter type from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
### Output

### **Num** — Numerator filter coefficients three-element row vector

Numerator filter coefficients of the designed SOS filter, returned as a
three-element row vector.

#### Dependencies

The data type of the output depends on the **Output data
type** parameter.

**Data Types:** `single` | `double`

### **Den** — Denominator filter coefficients three-element row vector

Denominator filter coefficients of the designed SOS filter, returned as a
three-element row vector.

#### Dependencies

The data type of the output depends on the **Output data
type** parameter.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Smooth tuned filter parameters
  summary: Smooth filter parameters when tuning off (default) | on
  group: ''
- name: Smoothing factor
  summary: Smoothing factor for tuned parameters 0.6 (default) | scalar in range [0,1)
  group: ''
- name: Specify peak gain from input port
  summary: Use additional input port to specify gain off (default) | on
  group: ''
- name: Peak gain (dB)
  summary: Peak gain (dB) 0 (default) | real scalar
  group: ''
- name: Specify slope coefficient from input port
  summary: Use additional input port to specify slope coefficient off (default) | on
  group: ''
- name: Slope coefficient
  summary: Slope coefficient 1.5 (default) | positive scalar
  group: ''
- name: Specify normalized cutoff frequency from input port
  summary: Use additional input port to specify normalized cutoff frequency off (default) | on
  group: ''
- name: Normalized cutoff frequency
  summary: Normalized cutoff frequency 0.1 (default) | scalar in range [0,1]
  group: ''
- name: Specify filter type from input port
  summary: Use additional input port to specify filter type off (default) | on
  group: ''
- name: Filter type
  summary: Type of shelving equalizer low (default) | high
  group: ''
- name: Output data type
  summary: Data type of output coefficients double (default) | single
  group: ''
- name: Sample time
  summary: Sample time of block -1 (default) | positive scalar
  group: ''
- name: Simulate using
  summary: Specify type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Smooth tuned filter parameters** — Smooth filter parameters when tuning `off` (default) | `on`

Select this parameter to gradually change a filter parameter to the new value when
tuning it. If you clear this parameter, the tuned parameter immediately switches to the
new value. Specify the level of smoothing with the **Smoothing
factor** parameter.

### **Smoothing factor** — Smoothing factor for tuned parameters `0.6` (default) | scalar in range [0,1)

Smoothing factor for tuned parameters, specified as a scalar in the range [0,1). As
the smoothing factor approaches 1, a tuned parameter changes more gradually to the new
value. A smoothing factor of 0 is equivalent to no smoothing.

For more information about smoothing, see Smoothing.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Smooth tuned filter
parameters** parameter.

### **Specify peak gain from input port** — Use additional input port to specify gain `off` (default) | `on`

When you select this parameter, an additional input port, **G**, is added
to the block. Use this port to specify the gain of the filter.

### **Peak gain (dB)** — Peak gain (dB) `0` (default) | real scalar

Peak gain of the filter in dB, specified as a real scalar. The gain specifies how
much the filter boosts (if the gain is positive) or cuts (if the gain is negative) the
frequency spectrum of the input signal.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify peak gain from input
port** parameter.

### **Specify slope coefficient from input port** — Use additional input port to specify slope coefficient `off` (default) | `on`

When you select this parameter, an additional input port, **S**, is added
to the block. Use this port to specify the slope of the filter.

### **Slope coefficient** — Slope coefficient `1.5` (default) | positive scalar

Slope coefficient of the filter, specified as a positive scalar. The slope controls
the width of the transition band in the filter response.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify slope coefficient from
input port** parameter.

### **Specify normalized cutoff frequency from input port** — Use additional input port to specify normalized cutoff frequency `off` (default) | `on`

When you select this parameter, an additional input port, **Fc**, is added
to the block.

### **Normalized cutoff frequency** — Normalized cutoff frequency `0.1` (default) | scalar in range [0,1]

Normalized cutoff frequency of the filter, specified as a scalar in the range [0,1]
where 1 corresponds to the Nyquist frequency. The cutoff frequency specifies the
frequency at half of the peak gain of the filter, *G*/2 dB, where
*G* is the peak gain.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify normalized cutoff frequency
from input port** parameter.

### **Specify filter type from input port** — Use additional input port to specify filter type `off` (default) | `on`

When you select this parameter, an additional input port, **T**, is added
to the block.

### **Filter type** — Type of shelving equalizer `low` (default) | `high`

Type of shelving equalizer, specified as `low` for a
low-shelf equalizer or `high` for a high-shelf
equalizer.

- A low-shelf equalizer boosts or cuts the frequency spectrum below the cutoff
  frequency.
- A high-shelf equalizer boosts or cuts the frequency spectrum above the cutoff
  frequency.

### **Output data type** — Data type of output coefficients `double` (default) | `single`

Data type of output coefficients, specified as `double` or
`single`.

### **Sample time** — Sample time of block `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as `-1` or a
positive scalar. Setting this parameter to `-1` means Simulink determines the sample time automatically for you. You can set this
parameter to enable the design block to run at a slower rate than the filtering
block.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` –– Simulate model using the
  MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` –– Simulate model using generated C
  code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.
## Libraries

Audio Toolbox / Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Design tunable shelving equalizer coefficients

The Shelving Equalizer Design block designs a shelving equalizer with the
specified gain, slope, and cutoff frequency. You can choose to design a low-shelf or a
high-shelf equalizer. The block outputs the coefficients of a second-order section (SOS)
filter, which you can use with the Second-Order Section
Filter block to filter audio signals. You can tune the filter parameters during
simulation.
