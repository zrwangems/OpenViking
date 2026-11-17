---
type: simulink-block
title: 'LMS Update'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'lmsupdate'
documentation_source_path: 'ref/lmsupdate.html'
language: en
---

# LMS Update

## Ports
```yaml
ports:
- name: Input
  summary: Data input scalar | column vector
  direction: input
  data_types: single | double
- name: Error
  summary: Error scalar | column vector
  direction: input
  data_types: single | double
- name: Mu
  summary: Filter adaptation step size 0.1 (default) | scalar in the range [0,1]
  direction: input
  data_types: single | double
- name: Adapt
  summary: Update filter weights real scalar | vector
  direction: input
  data_types: single | double | Boolean | int16 | int32 | int64 | int8 | uint16 | uint32 | uint64 | uint8
- name: Reset
  summary: Reset filter weights real scalar
  direction: input
  data_types: single | double | Boolean | int16 | int32 | int64 | int8 | uint16 | uint32 | uint64 | uint8
- name: Wts
  summary: Filter weights row vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **Input** — Data input scalar | column vector

Data input to the adaptive filter, specified as one of these:

- Scalar –– When you set the **Adaptive filter
  mode** parameter to `Tapped
  delay-line FIR filter`, the input to the
  block should be a scalar.

  The block algorithm buffers the input samples to generate
  the vector u(n)=[u(n),u(n−1),...,u(n−L+1)], where *L* is the length
  of the adaptive filter and *n* is the time
  index. The block algorithm then passes the vector through
  the filter.
- Column vector of length *L* –– When you
  set the **Adaptive filter mode** parameter
  to `Adaptive linear combiner`, the
  block does not buffer the input samples, and the input to
  the block should be in the form of a column vector. The
  block multiplies the vector with the filter weights to
  generate the filter output. In this case, there is no
  relationship between the input samples.

When you set the **Number of adaptive filters**
parameter to a value greater than 1, the block assumes that all filters
run on the same input.

When you set the **Algorithm** parameter to
`Sign—Error LMS`,
`Sign—Data LMS`, or
`Sign—Sign LMS`, the data input
through the **Input** port must be real.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Error** — Error scalar | column vector

Specify the error between the output signal and the desired signal as a:

- Scalar when the number of adaptive filters
  *N* = 1.
- Column vector of length *N* when
  *N* > 1.

When you set the **Algorithm** parameter to
`Sign—Error LMS`,
`Sign—Data LMS`, or
`Sign—Sign LMS`, the error input
through the **Error** port must be real.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Mu** — Filter adaptation step size 0.1 (default) | scalar in the range [0,1]

Specify the filter adaptation step size as a scalar in the range
[0,1].

#### Dependency

To enable this port, set **Step size source** to
`Input port`.

**Data Types:** `single` | `double`

### **Adapt** — Update filter weights real scalar | vector

The input to this port can be one of these:

- Scalar –– If the number of adaptive filters
  (*N*) is greater than 1, then the block
  updates the filter weights for all filters if the value at
  the port is nonzero and does not update if the value at the
  port is 0.
- Vector of length *N* –– If the number of
  adaptive filters (*N*) is greater than 1,
  then the block determines whether to update each filter
  during run time depending on the value of the corresponding
  element in the **Adapt** vector input. When
  the **Adapt** port input element is not 0,
  the block updates the filter weights. When the input is 0,
  the filter weights do not change.

For an example, see Adapt Multiple Filters Using LMS Update Block.

#### Dependency

To enable this port, select the **Enable adapt
input** parameter on the block dialog.

**Data Types:** `single` | `double` | `Boolean` | `int16` | `int32` | `int64` | `int8` | `uint16` | `uint32` | `uint64` | `uint8`

### **Reset** — Reset filter weights real scalar

When the input to this port is not 0, the block resets the filter
weights to their initial values. When the input to this port is 0, the
filter weights do not change.

#### Dependency

To enable this port, select the **Enable reset
input** parameter on the block dialog.

**Data Types:** `single` | `double` | `Boolean` | `int16` | `int32` | `int64` | `int8` | `uint16` | `uint32` | `uint64` | `uint8`
### Output

### **Wts** — Filter weights row vector | matrix

The block outputs the filter weights as a 1-by-*L*
row vector or a *N*-by-*L* matrix,
where *N* is the number of adaptive filters, and
*L* is the length of each filter.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Algorithm
  summary: LMS adaptive algorithm LMS (default) | Normalized LMS | Sign—Error LMS | Sign—Data LMS | Sign—Sign LMS
  group: ''
- name: Filter length
  summary: Length of the filter 32 (default) | positive integer
  group: ''
- name: Number of adaptive filters
  summary: Number of adaptive filters 1 (default) | positive integer
  group: ''
- name: Step size source
  summary: Method to specify the step size Property (default) | Input port
  group: ''
- name: Step size (mu)
  summary: Size of the adaptation step 0.1 (default) | nonnegative scalar
  group: ''
- name: Leakage factor (0 to 1)
  summary: Leakage factor 1.0 (default) | real scalar in the range [0,1]
  group: ''
- name: Initial value of filter weights
  summary: Initial value of filter weights 0 (default) | real scalar | vector | matrix
  group: ''
- name: Adaptive filter mode
  summary: Adaptive filter mode Tapped delay-line FIR filter (default) | Adaptive linear combiner
  group: ''
- name: Enable adapt input
  summary: Update the filter weights off (default) | on
  group: ''
- name: Enable reset input
  summary: Reset the filter weights off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Algorithm** — LMS adaptive algorithm `LMS` (default) | `Normalized LMS` | `Sign—Error LMS` | `Sign—Data LMS` | `Sign—Sign LMS`

The block uses one of the listed algorithms to compute the filter weights.
For more details on the algorithms, see Algorithms.

### **Filter length** — Length of the filter 32 (default) | positive integer

Specify the length of each adaptive filter *L* as a
positive integer.

When there are *N* adaptive filters, the weights vector
the block generates through the **Wts** output port is an
*N*-by-*L* matrix.

### **Number of adaptive filters** — Number of adaptive filters 1 (default) | positive integer

Specify the number of adaptive filters *N* the block
supports as a positive integer.

When you specify this value to be an integer greater than 1, each filter
can be chosen to adapt independently during run time by providing the
**Adapt** input as a logical vector of
length *N*. All filters are assumed to run on the same
input and have a common step size, leakage factor, and reset input.

The weights the block generates through the **Wts**
output port is an *N*-by-*L* matrix, where
*L* is the length of each filter.

For an example that shows how to adapt multiple filters, see Adapt Multiple Filters Using LMS Update Block.

### **Step size source** — Method to specify the step size `Property` (default) | `Input port`

- `Property` — Specify the filter
  adaptation size using the **Step size (mu)**
  parameter.
- `Input port` — Pass filter
  adaptation size using the **Mu** input port.

### **Step size (mu)** — Size of the adaptation step 0.1 (default) | nonnegative scalar

**Step size (mu)** indicates the amount by which the
filter weights are updated in each iteration. Choose an optimal step size so
that the filter is stable and the convergence speed is optimal.

This parameter is tunable. You can change its value even during the
simulation.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Step size source** to
`Property`.

### **Leakage factor (0 to 1)** — Leakage factor 1.0 (default) | real scalar in the range [0,1]

**Leakage factor (0 to 1)** prevents unbounded growth of
the filter coefficients by reducing the drift of the coefficients from their
optimum values. A leakage factor of `1.0` indicates no
leakage. If you encounter coefficient drift, that is, large fluctuation
about the optimum solution, decrease the leakage factor until the
coefficient fluctuation becomes small.

This parameter is tunable. You can change its value even during the
simulation.

**Tunable:** Yes

### **Initial value of filter weights** — Initial value of filter weights 0 (default) | real scalar | vector | matrix

Specify the initial value of filter weights as one of the following:

- Scalar
- Vector of size 1-by-*L* ––
  *N* is set to 1
- Matrix of size *N*-by-*L* ––
  *N* > 1 and *L* > 1

where *N* is the number of adaptive filters
specified in **Number of adaptive filters** and
*L* is the length of each filter specified in
**Filter length**.

This parameter specifies the initial value of the filter weights **w**(*n*−1). The block uses this
value to compute the weights **w**(*n*), when *n* = 1. For
more information, see Algorithms.

### **Adaptive filter mode** — Adaptive filter mode `Tapped delay-line FIR filter` (default) | `Adaptive linear combiner`

Specify the adaptive filter mode as one of the following:

- `Tapped delay-line FIR filter` –– The
  block assumes the variable portion of the adaptive filter to be
  a tapped delay-line FIR filter. In this mode, the input samples
  are related using this equation:

  u(n)=[u(n),u(n−1),...,u(n−L+1)]

  where *n* is the current time index and
  *L* is the length of the adaptive filter
  specified in the **Filter length**
  parameter.

  The block accepts scalar input samples in this mode. The block
  algorithm buffers the samples to form the **u**(*n*) vector.
- `Adaptive linear combiner` –– The
  block does not buffer the input samples, and the input you
  provide to the block must be a column vector equal in length to
  the **Filter length** parameter. In this case,
  there is no relationship between the input samples.

For more details, see Algorithms.

### **Enable adapt input** — Update the filter weights off (default) | on

When you select this check box, the **Adapt** input port
appears on the block. When the input to this port is greater than 0, the
block updates the filter weights. When the input to this port is less than
or equal to 0, the filter weights do not change.

### **Enable reset input** — Reset the filter weights off (default) | on

When you select this check box, the **Reset** input port
appears on the block. When the input to this port is greater than 0, the
block resets the filter weights to their initial values. When the input to
this port is less than or equal to 0, the filter weights do not
change.

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
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Estimate weights of least mean squares (LMS) adaptive filter

The LMS Update block estimates the weights of an least mean squares
(LMS) adaptive filter. Specify data and error as inputs and the block computes the
filter weights based on the algorithm specified in the **Algorithm**
parameter. For more details on the algorithms, see Algorithms.

You can configure the block to operate as a tapped-delay line FIR filter or as an
adaptive linear combiner using the **Adaptive filter mode** parameter.
The block can also adapt multiple filters independently when you specify the
**Number of adaptive filters** parameter to a value greater than 1.

You can use this block to compute the adaptive filter weights in applications such as
system identification, inverse modeling, and filtered-x LMS algorithms, which are used
in acoustic noise cancellation. For more details, see References.
