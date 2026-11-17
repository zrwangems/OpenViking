---
type: simulink-block
title: 'Range Response'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'rangeresponse'
documentation_source_path: 'ref/rangeresponse.html'
language: en
---

# Range Response

## Ports
```yaml
ports:
- name: X
  summary: Input data cube complex-valued *K*-by-1 column vector | complex-valued *K*-by-*L* matrix | complex-valued *K*-by-*N*-by-*L*
    array
  direction: input
  data_types: double
- name: Coeff
  summary: Matched filter coefficients complex-valued column vector
  direction: input
  data_types: double
- name: XRef
  summary: Reference signal complex-valued *K*-by-1 column vector
  direction: input
  data_types: double
- name: Resp
  summary: Range response data cube complex-valued *M*-element column vector | complex-valued *M*-by-*L* matrix | complex-valued
    *M*-by-*N* by-*L* array
  direction: output
  data_types: double
- name: Range
  summary: Range values along range dimension real-valued *M*-by-1 column vector
  direction: output
  data_types: double
```

### Input

### **X** — Input data cube complex-valued *K*-by-1 column vector | complex-valued *K*-by-*L* matrix | complex-valued *K*-by-*N*-by-*L* array

Input data cube, specified as a complex-valued *K*-by-1
column vector, a complex-valued *K*-by-*L* matrix,
or a complex-valued *K*-by-*N*-by-*L* array.

- *K* is the number of range or time
  samples.
- *N* is the number of independent
  channels such as sensors or directions.
- *L* is the number of pulses or sweeps
  in the input signal.

See Radar Data Cube Concept.

Each *K*-element column vector is processed
independently.

For an FMCW waveform, with a triangle sweep, the sweeps alternate
between positive and negative slopes. However, Range Response is
designed to process consecutive sweeps of the same slope. To apply
the Range Response block for a triangle-sweep system,
use one of the following approaches:

- Specify a positive **Sweep slope** parameter
  value, with `X` corresponding to upsweeps only.
  After obtaining the Doppler or speed values, divide them by 2.
- Specify a negative **Sweep slope** parameter
  value, with `X` corresponding to downsweeps only.
  After obtaining the Doppler or speed values, divide them by 2.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Coeff** — Matched filter coefficients complex-valued column vector

Matched filter coefficients, specified as a complex-valued column
vector. The length of the vector must be less than or equal to the
number of rows in the input data, *K*.

#### Dependencies

To enable this port, set **Range processing method** to `Matched
filter`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **XRef** — Reference signal complex-valued *K*-by-1 column vector

Reference signal used for dechirping the input signal, specified
as a complex-valued *K*-by-1 column vector. The
number of rows must equal the length of the first dimension of `X`.

#### Dependencies

To enable this port, set **Range processing method** to `FFT` and
select the **Dechirp input signal** parameter.

**Data Types:** `double`
**Complex Number Support:** Yes
### Output

### **Resp** — Range response data cube complex-valued *M*-element column vector | complex-valued *M*-by-*L* matrix | complex-valued *M*-by-*N* by-*L* array

Range response data cube, returned as a

- Complex-valued *M*-element column
  vector
- Complex-valued *M*-by-*L* matrix
- Complex-valued *M*-by-*N* by-*L* array

See Radar Data Cube Concept. The value of *M* depends
on the type of processing

| Range processing method | Dechirp input signal | Value of *M* |
| --- | --- | --- |
| `FFT` | `off` | If you set the **Source of FFT length in range processing** to `Auto`,*M = K*, the length of the first dimension of `x`. Otherwise, *M* equals the value of the **FFT length in range processing** parameter. |
| `on` | *M* equals the number of rows, *K*, of the input signal. |
| `Matched filter` | N/A | *M* equals the number of rows, *K*, of the input signal. |

**Data Types:** `double`
**Complex Number Support:** Yes

### **Range** — Range values along range dimension real-valued *M*-by-1 column vector

Range values along the first dimension of the **Resp** output
data port, specified as a real-valued *M*-by-1 column
vector. This quantity defines the range values along the first dimension
of the `Resp` output port data. Units are in meters.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Measurement mode
  summary: Measurement mode Monostatic (default) | Bistatic
  group: ''
- name: Range processing method
  summary: Range processing method Matched filter (default) | FFT
  group: ''
- name: Propagation speed (m/s)
  summary: Signal propagation speed physconst('LightSpeed') (default) | positive scalar
  group: ''
- name: Inherit sample rate
  summary: Inherit sample rate from upstream blocks on (default) | off
  group: ''
- name: Sample rate (Hz)
  summary: Sampling rate of signal 1e6 (default) | positive real-valued scalar
  group: ''
- name: FM sweep slope (Hz/s)
  summary: FM sweep slope 1e9 (default) | scalar
  group: ''
- name: Dechirp input signal
  summary: Enable dechirping of input signal on (default) | off
  group: ''
- name: Source of FFT length in range processing
  summary: Source of FFT length for range processing Auto (default) | Property
  group: ''
- name: FFT length in range processing
  summary: Range processing FFT length 1024 (default) | positive integer
  group: ''
- name: Range processing window
  summary: Range FFT weighting window None (default) | Hamming | Chebyshev | Hann | Kaiser | Taylor
  group: ''
- name: Range sidelobe attenuation level
  summary: Sidelobe attenuation for range processing 30 (default) | positive scalar
  group: ''
- name: Set reference range at center
  summary: Set reference range at center of range grid on (default) | off
  group: ''
- name: Reference range (m)
  summary: Reference range of range grid 0.0 (default) | nonnegative scalar
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Measurement mode** — Measurement mode `Monostatic` (default) | `Bistatic`

Measurement mode, specified as `Monostatic` or `Bistatic`. When set to `Monostatic`, the range measurement is the monostatic range. When set to `Bistatic`, the range measurement is the bistatic range.

**Example:** `Bistatic`

**Data Types:** `char` | `string`

### **Range processing method** — Range processing method `Matched filter` (default) | `FFT`

Range processing method, specified as `Matched filter` or `FFT`.

|  |  |
| --- | --- |
| `Matched filter` | The block applies a matched filter to the incoming signal. This approach is commonly used for pulsed signals, where the matched filter is the time reverse of the transmitted signal. |
| `FFT` | The block applies an FFT to the input signal. This approach is commonly used for FMCW and linear FM pulsed signals. |

**Data Types:** `char`

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream blocks. Otherwise,
specify the sample rate using the **Sample rate (Hz)**
parameter.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sampling rate of signal `1e6` (default) | positive real-valued scalar

Specify the signal sampling rate as a positive scalar. Units are in Hz.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate** check
box.

**Data Types:** `double`

### **FM sweep slope (Hz/s)** — FM sweep slope `1e9` (default) | scalar

Specify the slope of the linear FM sweep as a scalar. This parameter
must match the actual sweep of the input data in port `X`.

#### Dependencies

To enable this parameter, set **Range processing method** to `FFT`.

**Data Types:** `double`

### **Dechirp input signal** — Enable dechirping of input signal `on` (default) | `off`

Select this parameter to enable dechirping of input signal.

#### Dependencies

To enable this parameter, set **Range processing method** to `FFT`.

**Data Types:** `Boolean`

### **Source of FFT length in range processing** — Source of FFT length for range processing `Auto` (default) | `Property`

Source of FFT length for range processing, specified as `Auto` or `Property`

|  |  |
| --- | --- |
| `Auto` | The FFT length equals the number of rows of the input data cube. |
| `Property` | Specify FFT length in the **FFT length in range processing** parameter. |

#### Dependencies

To enable this parameter, set **Range processing method** to
`FFT`.

**Data Types:** `char`

### **FFT length in range processing** — Range processing FFT length `1024` (default) | positive integer

FFT length for range processing, specified as a positive integer.

#### Dependencies

To enable this parameter, set **Range processing method** to `FFT` and **Source
of FFT length in range processing** to `Property`.

**Data Types:** `double`

### **Range processing window** — Range FFT weighting window `None` (default) | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

Range FFT weighting window, specified as `None`, `Hamming`, `Chebyshev`, `Hann`, `Kaiser`,
or `Taylor`.

If you set this property to `Taylor`, the generated
Taylor window has four nearly constant sidelobes next to the mainlobe.

#### Dependencies

To enable this parameter, set **Range processing method** to `FFT`.

**Data Types:** `char`

### **Range sidelobe attenuation level** — Sidelobe attenuation for range processing `30` (default) | positive scalar

Sidelobe attenuation for range processing, specified as a positive
scalar. Units are in dB.

#### Dependencies

To enable this parameter, set **Range processing method** to `FFT` and **Range
processing window** to `Kaiser`, `Chebyshev`,
or `Taylor`.

**Data Types:** `double`

### **Set reference range at center** — Set reference range at center of range grid `on` (default) | `off`

Set reference range at the center of range grid, specified as
`on` or `off`. Selecting this check
box, enables you to set the reference range at the center of the range grid.
Otherwise, the reference range is set to the beginning of the range
grid.

#### Dependencies

To enable this property, set the **Range processing
method** to `FFT`.

### **Reference range (m)** — Reference range of range grid `0.0` (default) | nonnegative scalar

Reference range of the range grid, specified as a nonnegative scalar.

- If you set the **Range processing method**
  parameter to `Matched filter`, the
  reference range is set to the start of the range grid.
- If you set the **Range processing method**
  property to `FFT`, the reference range
  depends on the **Set reference range at
  center** check box.

  - When you select the **Set reference range
    at center** check box, the reference
    range is set to the center of the range grid.
  - If you do not select the **Set reference
    range at center** check box, the
    reference range is set to the start of the range
    grid.

  Units are in meters.

**Example:** `1000.0`

**Data Types:** `double`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |
## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Range response

The Range Response block performs range filtering
on fast-time (range) data, using either a matched filter or an FFT-based
algorithm. The output is typically used as input to a detector. Matched
filtering improves the SNR of pulsed waveforms. For continuous FM
signals, FFT processing extracts the beat frequency of FMCW waveforms.
Beat frequency is directly related to range.

The input to the block is a radar data cube. The organization
of the data cube follows the Phased Array System Toolbox™ convention.
The first dimension of the cube represents the fast time samples or
ranges of the received signals. The second dimension represents multiple
spatial channels such as different sensors or beams. The third dimension,
slow time, represent pulses. Range filtering operates along the fast-time
dimension of the cube. Processing along the other dimensions is not
performed. If the data contains only one channel or pulse, the data
cube can contain fewer than three dimensions. Because this object
performs no Doppler processing, you can use it to process noncoherent
radar pulses.

The output of the block is also a data cube with the same number
of dimensions as the input. Its first dimension contains range-processed
data but its length can differ from the first dimension of the input
data cube.
