---
type: simulink-block
title: 'RLS Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'rlsfilter'
documentation_source_path: 'ref/rlsfilter.html'
language: en
---

# RLS Filter

## Ports
```yaml
ports:
- name: Input
  summary: Input signal scalar | column vector
  direction: input
  data_types: single | double
- name: Desired
  summary: Desired signal scalar | column vector
  direction: input
  data_types: single | double
- name: Lambda
  summary: Forgetting factor scalar in the range [0,1]
  direction: input
  data_types: single | double
- name: Adapt
  summary: Option to update filter weights scalar | column vector
  direction: input
  data_types: single | double
- name: Reset
  summary: Reset signal scalar
  direction: input
  data_types: single | double
- name: Output
  summary: Filtered signal scalar | column vector
  direction: output
  data_types: single | double
- name: Error
  summary: Difference between output and desired signal scalar | column vector
  direction: output
  data_types: single | double
- name: Wts
  summary: Adaptive filter weights scalar | column vector
  direction: output
  data_types: single | double
```

### Input

### **Input** — Input signal scalar | column vector

Specify the input signal you want to filter as a scalar or a column
vector.

The input signal and the desired signal must have the same size, data
type, and complexity.

The input signal can be a variable-size signal, that is, the frame
length of the signal can change during simulation as long as the signal
dimensions match with the input signal.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Desired** — Desired signal scalar | column vector

Specify the signal you want to model as a scalar or a column vector.
The RLS filter adapts its coefficients to minimize the error and
converge the input signal to the desired signal as closely as
possible.

The input signal and the desired signal must have the same size, data
type, and complexity.

The desired signal can be a variable-size signal, that is, the frame
length of the signal can change during simulation as long as the signal
dimensions match with the input signal.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Lambda** — Forgetting factor scalar in the range [0,1]

Specify the RLS forgetting factor *λ* as a scalar in
the range `0` ≤ *λ* ≤
`1` through this input port. For more information
on this parameter, see the **Forgetting factor (0 to
1)** parameter description.

#### Dependencies

To enable this port, set the **Specify forgetting factor
via** parameter as `Input
port`.

**Data Types:** `single` | `double`

### **Adapt** — Option to update filter weights scalar | column vector

If the input is a nonzero value, the block continuously updates the
filter weights. If the value of this input is zero, the filter weights
remain at their current values.

#### Dependencies

To enable this port, select the **Adapt port**
parameter.

**Data Types:** `single` | `double`

### **Reset** — Reset signal scalar

Specify the reset signal as a scalar signal. When you want to reset
the value of the filter weights to their initial values, use the
**Reset port** parameter. The block resets the
filter weights whenever a reset event is detected at the
**Reset** port. The reset signal rate must be the
same rate as the data signal input.

To enable the **Reset** port, select one of these options from the
**Reset port** list:

- `Rising edge` — Triggers a
  reset operation when the **Reset** input does
  one of the following:

  - Rises from a negative value to a positive value or
    zero
  - Rises from zero to a positive value, where the rise is
    not a continuation of a rise from a negative value to
    zero

- `Falling edge` — Triggers a
  reset operation when the **Reset** input does
  one of the following:

  - Falls from a positive value to a negative value or
    zero
  - Falls from zero to a negative value, where the fall is
    not a continuation of a fall from a positive value to
    zero

- `Either edge` — Triggers a
  reset operation when the **Reset** input is a
  `Rising edge` or
  `Falling edge`
- `Non-zero sample` — Triggers a
  reset operation at each sample time that the
  **Reset** input is not zero

To disable the reset port, set **Reset port** to
`None`.

#### Dependencies

To enable this port, set **Reset port** to any
option other than `None`.

**Data Types:** `single` | `double`
### Output

### **Output** — Filtered signal scalar | column vector

Filtered signal, returned as a scalar or a column vector. The block
adapts its filter coefficients to converge the input signal to match the
desired signal. The filter outputs the converged signal. For more
details on how the block computes the output, see Algorithms.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Error** — Difference between output and desired signal scalar | column vector

Difference between the filtered signal and the desired signal,
returned as a scalar or a column vector. The objective of the RLS filter
is to minimize this error. The block adapts its coefficients to converge
towards optimal filter coefficients that produce an output signal that
matches closely with the desired signal. For more details on how the
block computes the error, see Algorithms.

The block outputs the RLS filter coefficients through the
**Wts** port.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Wts** — Adaptive filter weights scalar | column vector

Weights of the RLS filter, returned as a column vector of length equal
to the value you specify in the **Filter length**
parameter. For each iteration, the block outputs the current updated
filter weights from this port. For more information on how the block
updates the filter weights, see Algorithms.

The data type of the filter weights matches the data type of the
filtered signal.

#### Dependencies

To enable this port, select the **Output filter weights**
parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Filter length
  summary: Length of FIR filter coefficients vector 32 (default) | positive integer
  group: ''
- name: Specify forgetting factor via
  summary: Specify forgetting factor Dialog (default) | Input port
  group: ''
- name: Forgetting factor (0 to 1)
  summary: RLS forgetting factor 1.0 (default) | scalar in the range [0,1]
  group: ''
- name: Initial value of filter weights
  summary: Initial value of FIR filter weights 0 (default) | vector
  group: ''
- name: Initial input variance estimate
  summary: Initial input covariance estimate 0.1 (default) | scalar | square matrix
  group: ''
- name: Adapt port
  summary: Enable Adapt port off (default) | on
  group: ''
- name: Reset port
  summary: Enable Reset port None (default) | Rising edge | Falling edge | Either edge | Non-zero sample
  group: ''
- name: Output filter weights
  summary: Output filter weights on (default) | off
  group: ''
```

### **Filter length** — Length of FIR filter coefficients vector `32` (default) | positive integer

Specify the length of the FIR filter coefficients vector
*L* as a positive integer.

### **Specify forgetting factor via** — Specify forgetting factor `Dialog` (default) | `Input port`

Specify the forgetting factor through:

- `Dialog` –– Use the
  **Forgetting factor (0 to 1)** parameter to
  specify the forgetting factor in the block dialog box.
- `Input port` –– Use the
  **Lambda** input port to specify the
  forgetting factor.

### **Forgetting factor (0 to 1)** — RLS forgetting factor `1.0` (default) | scalar in the range [0,1]

Specify the RLS forgetting factor *λ* as a scalar in the
range `0` ≤ *λ* ≤ `1`.
This parameter specifies how quickly the filter forgets past sample
information. Setting *λ* = `1` denotes
infinite memory, while adapting to find the new filter. Typically, 1−12L<λ<1, where *L* is the filter length. You can
specify a forgetting factor using the input port,
**Lambda**, or enter a value in the
**Forgetting factor (0 to 1)** parameter in the block
dialog box.

#### Dependencies

To enable this parameter, set the **Specify forgetting factor
via** parameter to
`Dialog`.

**Tunable:** Yes

### **Initial value of filter weights** — Initial value of FIR filter weights `0` (default) | vector

Specify initial values of the FIR filter weights w^(0) as a scalar or a vector of length equal to the filter
length. When you specify a scalar, the block uses the scalar value to create
a vector of filter weights. This vector has length equal to the filter
length and all of its values are equal to the scalar value.

### **Initial input variance estimate** — Initial input covariance estimate `0.1` (default) | scalar | square matrix

Specify the initial values of the input covariance estimate, 1/**P**(*n*) as a:

- Scalar –– **P**(*n*) is a diagonal matrix
  with diagonal elements equal to the scalar value.
- Square matrix –– Each dimension of the matrix equals the value
  you specify in the **Filter length**
  parameter.

The initial value of **P**(*n*) is 1σ2I where you specify σ2 in the **Initial input variance
estimate** parameter.

### **Adapt port** — Enable Adapt port `off` (default) | `on`

Select this parameter to enable the **Adapt** input port. Use this port
to specify if the block must update its filter weights or to keep them at
the current level. For more information, see the description of the
**Adapt** input port.

### **Reset port** — Enable Reset port `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

Select this parameter to enable the **Reset** input port. For more
information on each of the reset options, see the description for the
**Reset** input port.

### **Output filter weights** — Output filter weights `on` (default) | `off`

Select this parameter to export the filter weights from the **Wts**
port.
## Libraries

DSP System Toolbox / Filtering / Adaptive Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Compute filtered output, filter error, and filter weights for given input and desired signal using RLS adaptive filter algorithm

The RLS Filter block recursively computes the least squares estimate
(RLS) of the FIR filter weights. The block estimates the filter weights (also known as
the coefficients) needed to minimize the error
*e*(*n*) between the output signal
*y*(*n*) and the desired signal
*d*(*n*). For more information, see Algorithms. For more information
on adaptive filters, see Overview of Adaptive Filters and Applications.
