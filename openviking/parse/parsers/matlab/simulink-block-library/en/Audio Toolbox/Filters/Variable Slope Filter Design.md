---
type: simulink-block
title: 'Variable Slope Filter Design'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'variableslopefilterdesign'
documentation_source_path: 'ref/variableslopefilterdesign.html'
language: en
---

# Variable Slope Filter Design

## Ports
```yaml
ports:
- name: S
  summary: Filter slope scalar in range [0,48]
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Fc
  summary: Normalized cutoff frequency scalar in range [0,1]
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: T
  summary: Filter type 0 (lowpass) | 1 (highpass)
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated
- name: Num
  summary: Numerator filter coefficients *N*-by-3 matrix
  direction: output
  data_types: single | double
- name: Den
  summary: Denominator filter coefficients *N*-by-3 matrix
  direction: output
  data_types: single | double
```

### Input

### **S** — Filter slope scalar in range [0,48]

Use this port to specify the value of the **Filter
slope** parameter.

#### Dependencies

To enable this port, select the **Specify slope from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — Normalized cutoff frequency scalar in range [0,1]

Use this port to specify the value of the **Normalized cutoff
frequency** parameter.

#### Dependencies

To enable this port, select the **Specify normalized cutoff frequency
from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **T** — Filter type `0` (lowpass) | `1` (highpass)

Use this port to specify the value of the **Filter
type** parameter; `0` corresponds to a lowpass filter and
`1` corresponds to a highpass filter.

#### Dependencies

To enable this port, select the **Specify filter type from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
### Output

### **Num** — Numerator filter coefficients *N*-by-3 matrix

Numerator filter coefficients, returned as an *N*-by-3 matrix.
*N* is the number of filter sections and depends on the **Maximum filter
slope** parameter. If **Filter
slope** is less than **Maximum filter slope**, then the
block sets the unused sections to pass-through sections.

#### Dependencies

- The data type of the output depends on the **Output data
  type** parameter.
- The output dimensions depend on the **Maximum filter
  slope** parameter.

**Data Types:** `single` | `double`

### **Den** — Denominator filter coefficients *N*-by-3 matrix

Denominator filter coefficients, returned as an *N*-by-3 matrix.
*N* is the number of filter sections and depends on the **Maximum filter
slope** parameter. A steeper slope requires more filter sections. If
**Filter
slope** is less than **Maximum filter slope**, then the
block sets the unused sections to pass-through sections.

#### Dependencies

- The data type of the output depends on the **Output data
  type** parameter.
- The output dimensions depend on the **Maximum filter
  slope** parameter.

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
- name: Maximum filter slope
  summary: Maximum filter slope (dB/octave) 12 (default) | scalar in range [0,48]
  group: ''
- name: Specify slope from input port
  summary: Use additional input port to specify slope off (default) | on
  group: ''
- name: Filter slope
  summary: Filter slope (dB/octave) 12 (default) | scalar in range [0,48]
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
  summary: Type of filter lowpass (default) | highpass
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

### **Maximum filter slope** — Maximum filter slope (dB/octave) `12` (default) | scalar in range [0,48]

Maximum filter slope in dB/octave, specified as a scalar in the range [0,48]. The
**Filter
slope** parameter cannot exceed this value.

### **Specify slope from input port** — Use additional input port to specify slope `off` (default) | `on`

When you select this parameter, an additional input port, **S**, is added
to the block.

### **Filter slope** — Filter slope (dB/octave) `12` (default) | scalar in range [0,48]

Filter slope in dB/octave, specified as a scalar in the range [0,48]. The block
rounds the slope value to the nearest multiple of 6.

**Tunable:** Yes

#### Dependencies

- To enable this parameter, clear the **Specify slope from input
  port** parameter.
- The value of this parameter cannot exceed the value of the **Maximum filter
  slope** parameter.

### **Specify normalized cutoff frequency from input port** — Use additional input port to specify normalized cutoff frequency `off` (default) | `on`

When you select this parameter, an additional input port, **Fc**, is added
to the block.

### **Normalized cutoff frequency** — Normalized cutoff frequency `0.1` (default) | scalar in range [0,1]

Normalized cutoff frequency of the filter, specified as a scalar in the range [0,1]
where 1 corresponds to the Nyquist frequency.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify normalized cutoff frequency
from input port** parameter.

### **Specify filter type from input port** — Use additional input port to specify filter type `off` (default) | `on`

When you select this parameter, an additional input port, **T**, is added
to the block.

### **Filter type** — Type of filter `lowpass` (default) | `highpass`

Type of filter, specified as `lowpass` for a lowpass filter
or `highpass` for a highpass filter.

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

Design tunable lowpass or highpass filter coefficients

The Variable Slope Filter Design block designs a lowpass or highpass filter
with the specified slope and cutoff frequency. The block outputs filter coefficients of
cascaded second-order section (SOS) filters, which you can use with the Second-Order Section
Filter block to filter audio signals. You can tune the filter parameters during
simulation.
