---
type: simulink-block
title: 'Frequency-Domain Adaptive Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'frequencydomainadaptivefilter'
documentation_source_path: 'ref/frequencydomainadaptivefilter.html'
language: en
---

# Frequency-Domain Adaptive Filter

## Ports
```yaml
ports:
- name: Input
  summary: Data input column vector
  direction: input
  data_types: single | double
- name: Desired
  summary: Desired signal column vector
  direction: input
  data_types: single | double
- name: Mu
  summary: Step size input real scalar in the range (0,1]
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Leak
  summary: Leakage factor input real scalar in the range (0,1]
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Avrg
  summary: Averaging factor input real scalar in the range (0,1]
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Offset
  summary: Offset for normalization terms nonnegative real scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Adapt
  summary: Enable filter coefficient updates nonnegative real scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Reset
  summary: Enable filter states reset nonnegative real scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Output
  summary: Filtered output column vector
  direction: output
  data_types: single | double
- name: Error
  summary: Difference between output and desired signal column vector
  direction: output
  data_types: single | double
- name: FFTCoeffs
  summary: Current FFT coefficients of filter row vector
  direction: output
  data_types: single | double
```

### Input

### **Input** — Data input column vector

The signal to be filtered by the frequency-domain FIR adaptive filter.
The data input and the desired signal input must have the same size and
data type. The length of the input vector must be divisible by the
**Block length** parameter value.

The data input can be a variable-size signal as long as the frame
length is a multiple of the **Block length**. You can
change the number of elements in the column vector during the model
simulation.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Desired** — Desired signal column vector

The frequency-domain adaptive filter adapts its filter weights to
minimize the error, **Error**, and converge the input
signal to match the desired signal as closely as possible.

The data input and the desired signal must have the same size and data
type. The length of the desired signal vector must be divisible by the
**Block length** parameter value.

The desired signal can be a variable-size signal as long as the frame
length is a multiple of the **Block length**. You can
change the number of elements in the column vector during the model
simulation.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Mu** — Step size input real scalar in the range (0,1]

Adaptation step size factor, specified as a real scalar in the range
(0,1]. Using a small step size ensures a small steady-state error.
However, a small step size decreases the resulting convergence speed of
the adaptive filter. Increasing the step size improves the convergence
speed, at the cost of increased steady-state mean squared error. When
the step size value is `1`, the algorithm provides the
optimal tradeoff between the convergence speed and the steady-state mean
squared error.

#### Dependencies

This port appears when you select the **Specify step size
from port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Leak** — Leakage factor input real scalar in the range (0,1]

Leakage factor used in leaky adaptive filter, specified as a real
scalar in the range (0,1]. When the value is less than 1, the block
implements a leaky adaptive algorithm. When the value is
`1`, the block provides no leakage in the adapting
method.

#### Dependencies

This port appears when you select the **Specify leakage
factor from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Avrg** — Averaging factor input real scalar in the range (0,1]

Averaging factor used to compute the exponentially windowed fast
Fourier transform (FFT) input signal powers for the coefficient updates,
specified as a real scalar in the range (0,1].

#### Dependencies

This port appears when you select the **Specify averaging
factor from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Offset** — Offset for normalization terms nonnegative real scalar

Offset for the normalization terms in the coefficient updates,
specified as a nonnegative real scalar value. Use this value to avoid
division by zero or division by very small numbers if any of the FFT
input signal powers become very small.

#### Dependencies

This port appears when you select the **Specify offset
from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Adapt** — Enable filter coefficient updates nonnegative real scalar

If you input a nonzero scalar value through this port, the block
continuously updates its filter coefficients. If you input a zero
through this port, the filter coefficients do not update, and their
values remain at the current value.

#### Dependencies

This port appears when you select the **Enable adapt
port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Reset** — Enable filter states reset nonnegative real scalar

If you input a nonzero scalar value through this port, the block
resets all internal states. If you input a zero through this port, the
internal states are not reset.

#### Dependencies

This port appears when you select the **Enable reset
port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Output** — Filtered output column vector

Filtered output, returned as a column vector. The block adapts its
filter weights to converge the input signal to match the desired signal
as closely as possible. The filter outputs the converged signal.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Error** — Difference between output and desired signal column vector

Difference between the output signal and the desired signal, returned
as a column vector. The objective of the adaptive filter is to minimize
this error. The block adapts its weights to converge towards optimal
filter weights which produce an output signal that matches the desired
signal as closely as possible. For more details on how
**Error** is computed, see References.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **FFTCoeffs** — Current FFT coefficients of filter row vector

Current discrete Fourier transform of the filter coefficients,
returned as a row vector. For `Constrained
FDAF` and `Unconstrained FDAF`
algorithms, the length of this vector is equal to the sum of the
**Filter length** value and the **Block
length** value. This port initially outputs the FFT values
of the **Initial time-domain coefficients** parameter.
During the model simulation, this port outputs the FFT values of the
current filter coefficients.

#### Dependencies

This port appears when you select the **Output filter FFT
coefficients** check box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Method
  summary: Method to calculate filter coefficients Constrained FDAF (default) | Partitioned constrained FDAF | Unconstrained
    FDAF | Partitioned unconstrained FDAF
  group: ''
- name: Filter length
  summary: Length of filter coefficients vector 32 (default) | positive, integer-valued scalar
  group: ''
- name: Block length
  summary: Block length for coefficient updates 32 (default) | positive, integer-valued scalar
  group: ''
- name: Specify step size from port
  summary: Flag to specify step size off (default) | on
  group: ''
- name: Step size
  summary: Adaptation step size 1 (default) | real scalar in the range (0,1]
  group: ''
- name: Specify leakage factor from port
  summary: Flag to specify leakage factor off (default) | on
  group: ''
- name: LeakageFactor
  summary: Adaptation leakage factor 1 (default) | real scalar in the range (0,1]
  group: ''
- name: Specify averaging factor from port
  summary: Flag to specify averaging factor off (default) | on
  group: ''
- name: Averaging factor
  summary: Averaging factor for signal power 0.9 (default) | real scalar in the range (0,1]
  group: ''
- name: Specify offset from port
  summary: Flag to specify offset off (default) | on
  group: ''
- name: Offset
  summary: Offset for normalization terms 0 (default) | nonnegative real scalar
  group: ''
- name: Initial FFT input signal power
  summary: Initial FFT input signal power 1 (default) | positive numeric scalar
  group: ''
- name: Initial time-domain coefficients
  summary: Initial time-domain coefficients of filter 0 (default) | scalar | vector
  group: ''
- name: Enable adapt port
  summary: Flag to enable coefficient update off (default) | on
  group: ''
- name: Enable reset port
  summary: Flag to reset internal states off (default) | on
  group: ''
- name: Output filter FFT coefficients
  summary: Flag to output the DFT of the filter coefficients off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Method** — Method to calculate filter coefficients `Constrained FDAF` (default) | `Partitioned constrained FDAF` | `Unconstrained FDAF` | `Partitioned unconstrained FDAF`

Method used to calculate the filter coefficients, specified as::

- `Constrained FDAF` –– Imposes a
  gradient constraint on the filter tap weights.
- `Partitioned constrained FDAF` ––
  Partitions the impulse response of the filter to reduce
  latency.
- `Unconstrained FDAF` –– No gradient
  constraint is imposed on the filter tap weights.
- `Partitioned unconstrained FDAF` ––
  Partitions the impulse response of the filter to reduce latency.
  No gradient constraint is imposed on the filter tap
  weights.

For more details, see Algorithms.

### **Filter length** — Length of filter coefficients vector `32` (default) | positive, integer-valued scalar

Length of the FIR filter coefficients vector, specified as a positive,
integer-valued scalar.

### **Block length** — Block length for coefficient updates `32` (default) | positive, integer-valued scalar

Block length for the coefficients update, specified as a positive,
integer-valued scalar. The adaptive filter processes the input data and the
desired signal as a block of samples of length set by this parameter. For
details on how this data is processed by the filter, see Algorithms. The length of the input vector must be divisible by the **Block
length** parameter value. The default value of the
**Block length** parameter is set to the value of the
**Filter length** parameter.

### **Specify step size from port** — Flag to specify step size off (default) | on

When you select this check box, the adaptation step size is input through
the **Mu** port. When you clear this check box, the step
size is specified on the block dialog through the **Step
size** parameter.

### **Step size** — Adaptation step size `1` (default) | real scalar in the range (0,1]

Adaptation step size factor, specified as a real scalar in the range
(0,1]. Setting the **Step size** parameter to
`1` provides the fastest convergence during
adaptation.

**Tunable:** Yes

#### Dependencies

This parameter appears when you clear the **Specify step size
from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Specify leakage factor from port** — Flag to specify leakage factor off (default) | on

When you select this check box, the leakage factor is input through the
**Leak** port. When you clear this check box, the
leakage factor is specified on the block dialog through the
**Leakage factor** parameter.

### **LeakageFactor** — Adaptation leakage factor `1` (default) | real scalar in the range (0,1]

Leakage factor used in leaky adaptive filter, specified as a real scalar
in the range (0,1]. When the value is less than `1`, the
block implements a leaky adaptive algorithm. When the value is
`1`, the block provides no leakage in the adapting
method.

**Tunable:** Yes

#### Dependencies

This parameter appears when you clear the **Specify leakage
factor from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Specify averaging factor from port** — Flag to specify averaging factor off (default) | on

When you select this check box, the averaging factor for signal power is
input through the **Avrg** port. When you clear this check
box, the averaging factor is specified on the block dialog through the
**Averaging factor** parameter.

### **Averaging factor** — Averaging factor for signal power `0.9` (default) | real scalar in the range (0,1]

Averaging factor used to compute the exponentially windowed FFT input
signal powers for the coefficient updates, specified as a real scalar in the
range (0,1].

**Tunable:** Yes

#### Dependencies

This parameter appears when you clear the **Specify averaging
factor from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Specify offset from port** — Flag to specify offset off (default) | on

When you select this check box, the offset for the normalization terms in
the coefficient updates is input through the **Offset**
port. When you clear this check box, the offset is specified on the block
dialog through the **Offset** parameter.

### **Offset** — Offset for normalization terms `0` (default) | nonnegative real scalar

Offset for the normalization terms in the coefficient updates, specified
as a nonnegative real scalar value. Use this value to avoid division by zero
or division by very small numbers if any of the FFT input signal powers
become very small.

**Tunable:** Yes

#### Dependencies

This parameter appears when you clear the **Specify offset
from port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Initial FFT input signal power** — Initial FFT input signal power `1` (default) | positive numeric scalar

Initial common value of all of the FFT input signal powers, specified as a
positive numeric scalar value.

If you change this value during the simulation, the change takes effect
only after a reset event occurs.

**Tunable:** Yes

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Initial time-domain coefficients** — Initial time-domain coefficients of filter `0` (default) | scalar | vector

Initial time-domain coefficients of the adaptive filter, specified as a
scalar or a vector of length equal to the value you specify in the
**Filter length** parameter. The adaptive filter block
uses these coefficients to compute the initial frequency-domain filter
coefficients.

If you change this value during the simulation, the change takes effect
only after a reset event occurs.

**Tunable:** Yes

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Enable adapt port** — Flag to enable coefficient update off (default) | on

When you select this check box, the **Adapt** input port
is enabled. If you input a nonzero scalar value through this port, the block
continuously updates its filter coefficients. If you input a zero through
this port, the filter coefficients do not update and their values remain at
the current value.

### **Enable reset port** — Flag to reset internal states off (default) | on

When you select this check box, the **Reset** input port
is enabled. If you input a nonzero scalar value through this port, the block
resets all internal states. If you input a zero through this port, the
internal states are not reset.

### **Output filter FFT coefficients** — Flag to output the DFT of the filter coefficients off (default) | on

When you select this check box, the **FFTCoeffs** output
port is enabled. Through this port, the block outputs the discrete Fourier
transform of the current filter coefficients.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.
## Libraries

DSP System Toolbox / Filtering / Adaptive Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Compute output, error, and coefficients using frequency domain FIR adaptive filter

The Frequency-Domain Adaptive Filter block implements an adaptive
finite impulse response (FIR) filter in the frequency domain using the fast block least
mean squares (LMS) algorithm. The **Filter length** and the
**Block length** parameters specify the filter length and the block
length values the algorithm uses. When you select the **Output filter FFT
coefficients** check box, the block outputs the discrete Fourier transform
of the current filter coefficients. The block offers the constrained and unconstrained
versions of the algorithm with partitioned and nonpartitioned modes. For details, see
Algorithms.
