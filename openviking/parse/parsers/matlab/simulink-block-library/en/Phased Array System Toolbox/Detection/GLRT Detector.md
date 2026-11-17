---
type: simulink-block
title: 'GLRT Detector'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'glrtdetector'
documentation_source_path: 'ref/glrtdetector.html'
language: en
---

# GLRT Detector

## Ports
```yaml
ports:
- name: X
  summary: Input data real-valued *N*-by-*1* vector | complex-valued *N*-by-*1* vector | real-valued *N*-by-*M* matrix | complex-valued
    *N*-by-*M* matrix
  direction: input
  data_types: single | double
- name: Hyp
  summary: Augmented linear equality constraint matrix real-valued *R*-by-(*P* + 1) matrix | complex-valued *R*-by-(*P* +
    1) matrix
  direction: input
  data_types: single | double
- name: Obs
  summary: Observation matrix *N*-by-*P*-by-*D* array
  direction: input
  data_types: single | double
- name: Ncov
  summary: Known noise power positive scalar
  direction: input
  data_types: single | double
- name: Y
  summary: Detection results *D*-by-*M* logical-valued vector | 1-by-*L* integer-valued vector | 2-by-*L* integer-valued matrix
  direction: output
- name: Stat
  summary: detection statistic *N*-by-*M* (default) | 1-by-*L*
  direction: output
- name: Th
  summary: Detection threshold scalar
  direction: output
- name: Param
  summary: Maximum likelihood estimates of signal parameters *P*-by-*M*-by-*D* array
  direction: output
- name: N
  summary: Estimated noise power positive scalar
  direction: output
```

### Input

### **X** — Input data real-valued *N*-by-*1* vector | complex-valued *N*-by-*1* vector | real-valued *N*-by-*M* matrix | complex-valued *N*-by-*M* matrix

Input data, specified as a real-valued or complex-valued
*N*-by-*1* vector, or an
*N*-by-*M* real-valued or complex-valued matrix.
*N* is the signal length and *M* is the number of
data channels. Detection is performed along the columns of `X`. The
size of each row *M* cannot change during simulation. When *M
= 1*, `X` represents a single channel of data. When
*M > 1*, `X` can represent *N*
samples from *M* data channels. Data streams can later be combined,
for example, by the beamforming.

The input data has a general interpretation. For example, the data can be
interpreted as:

- Time series – *N* samples of a time series
- Sensor - *N* represents a snapshot of data samples from a
  set of sensors

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Hyp** — Augmented linear equality constraint matrix real-valued *R*-by-(*P* + 1) matrix | complex-valued *R*-by-(*P* + 1) matrix

Augmented linear equality constraint matrix, specified as a real-valued or
complex-valued *R*-by-(*P* + 1) matrix. The matrix
takes the form **[A,b]** and represents the equation:

AΘ=b

where the unknown parameters are represented byϴ. **A** has the rank *R ≥ 1*. The augmented linear
equality constraint matrix expresses the null hypothesis
*H*0.

For this signal model, the GLRT detector determines whether to reject the null
hypothesis which is expressed in the form **A\*ϴ = b**
where **A** is an
*R*-by-*P* matrix with *R ≤ P*
and rank *R ≥ 1*, and **b** is an
*R*-by-1 vector. **A** and **b** are carried in the augmented linear equality constraint
matrix **hyp = [A,b]**. Because there are
*D* signal models, the GLRT detector outputs *D*
detection results for each column of `X`

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Obs** — Observation matrix *N*-by-*P*-by-*D* array

Observation matrix for the linear deterministic signal model, specified as an
*N*-by-*P*-by-*D* array
*N > p* and rank *P*, *D* is the
number of signal models, and the white Gaussian `noise` is a
*N*-by-1 vector determined by the covariance
`ncov` argument. The observation matrix is defined by
`X` = `obs`\*`param` +
`noise`,

**Example:** 20.0

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Ncov** — Known noise power positive scalar

Known noise power, specified as a scalar or a row vector of length
*D*. When `ncov` is a scalar, it represents
equal known noise power for *D* models. When
`ncov` is a row vector of length *D*, it
represents the known noise power for the *D* models,
respectively.

**Example:** `20.0`

#### Dependencies

To enable this argument, set the `NoiseInputPort` property to
`true`.

**Data Types:** `single` | `double`
### Output

### **Y** — Detection results *D*-by-*M* logical-valued vector | 1-by-*L* integer-valued vector | 2-by-*L* integer-valued matrix

Detection results of *D* models for *M*
independent data samples returned as a *D*-by-*M*
logical-valued vector pr. The format of `Y` depends on how the
`OutputFormat` property is specified. By default, the
`OutputFormat` property is set to `'Detection
result'`.

When `OutputFormat` is `'Detection result'`,
`Y` is a *D*-by-*M* matrix
containing logical detection results, where *D* is the number of
signal models and *M* is the number of columns of
`X`. For each row, *Y* is
`true` in a column if there is a detection in the corresponding
column of `arg`. Otherwise, `Y` is
`false`.

When `OutputFormat` is `'Detection index'`,
`Y` is a 1-by-`L` vector or a
2-by-*L* matrix containing detection indices, where
*L* is the number of detection found in the *M*
data samples and *D* models. When `X` is a column
vector, *Y* is a 1-by-*L* vector and contains the
index of the detections found in the *D* models. When
`X` is a matrix, `Y` is a
2-by-*L* matrix, and each column of *Y* has the
form `[detrow;detcol]`, where `detrow` is the index
of the model, and `detcol` is the column index of
*X*.

### **Stat** — detection statistic *N*-by-*M* (default) | 1-by-*L*

Detection statistics, returned as a *N*-by-*M*
matrix or 1-by-*L* vector. The format of `stat`
depends on the `OutputFormat` property.

- When `OutputFormat` is `'Detection
  result'`, `stat` has the same size as
  *Y*.
- When `OutputFormat` is `'Detection
  index'`, `stat` is a 1-by-*L*
  vector containing detection statistics for each corresponding detection in
  *Y*.

#### Dependencies

To enable this port, select the **Output detection statistics and
threshold** check box.

### **Th** — Detection threshold scalar

Detection threshold, returned as a scalar.

#### Dependencies

To enable this port, select the **Output detection statistics and
threshold** check box.

### **Param** — Maximum likelihood estimates of signal parameters *P*-by-*M*-by-*D* array

Maximum likelihood estimates (MLE) of unknown signal parameters, returned as a
*P*-by-*M*-by-*D* array.

#### Dependencies

To enable this port, select the **Output MLEs of unknown signal
parameters** check box.

### **N** — Estimated noise power positive scalar

Estimated noise power, returned as a positive scalar. When the
`OutputFormat` property is `'Detection result'`,
`estnoise` has the same size as `Y`. When
`OutputFormat` property is `'Detection index'`,
`estnoise` returns a noise power estimate of size
1-by-*L* for each corresponding detection in
`Y`.

#### Dependencies

To enable this port, select the **Output estimated noise
power** check box.
## Parameters
```yaml
parameters:
- name: Probability of false alarm
  summary: Probability of false alarm 0.1 (default) | nonnegative scalar
  group: ''
  block_parameter: ProbabilityFalseAlarm
  type: double, single
  values: scalar |
  default: '0.1'
- name: Output format
  summary: Format of output data Detection result (default) | Detection index
  group: ''
  block_parameter: OutputFormat
  type: char, string
  values: Detection result | Detection index
  default: Detection result
- name: Output detection statistics and threshold
  summary: Output detection statistics and threshold 0 (default) | 1
  group: ''
  block_parameter: ThresholdOutputPort
  type: check box
  values: 0 | 1
  default: '0'
- name: Enable known noise power input
  summary: Enable known noise power input 1 (default) | 1
  group: ''
  block_parameter: NoiseInputPort
  type: check box
  values: 0 | 1
  default: '0'
- name: Output MLEs of unknown signal parameters
  summary: Output MLEs of unknown signal parameters 0 (default) | 1
  group: ''
  block_parameter: SignalParamterOutputPort
  type: check box
  values: 0 | 1
  default: '0'
- name: Output estimated noise power
  summary: Output estimated noise power 0 (default) | 1
  group: ''
  block_parameter: NoisePowerOutputPort
  type: check box
  values: 0 | 1
  default: '0'
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Probability of false alarm** — Probability of false alarm `0.1` (default) | nonnegative scalar

Probability of false alarm, specified as positive scalar between 0 and 1,
inclusive.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ProbabilityFalseAlarm` |
| **Type:**double, single |
| **Values:**`scalar` | |
| **Default:**0.1 |

**Data Types:** `single` | `double`

### **Output format** — Format of output data `Detection result` (default) | `Detection index`

Format of output data, specified as `Detection result` or
`Detection index`. Output data is returned in the
`Y` port.

**Example:** `Detection index`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputFormat` |
| **Type:**char, string |
| **Values:**`Detection result` | `Detection index` |
| **Default:**`Detection result` |

**Data Types:** `char` | `string`

### **Output detection statistics and threshold** — Output detection statistics and threshold `0` (default) | `1`

Select this checkbox to output detection statistics and detection threshold using
the **Stat** and **Th** ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ThresholdOutputPort` |
| **Type:**check box |
| **Values:**0 | 1 |
| **Default:**`0` |

### **Enable known noise power input** — Enable known noise power input `1` (default) | `1`

Select this checkbox to allow input of noise power using the
**NCov** port.

#### Dependencies

To select this check box, deselect the **Output estimated noise
power** checkbox.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NoiseInputPort` |
| **Type:**check box |
| **Values:**0 | 1 |
| **Default:**`0` |

### **Output MLEs of unknown signal parameters** — Output MLEs of unknown signal parameters 0 (default) | 1

Select this check box to output maximum likelihood estimate of signal parameters
using the `Param` port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SignalParamterOutputPort` |
| **Type:**check box |
| **Values:**0 | 1 |
| **Default:**`0` |

### **Output estimated noise power** — Output estimated noise power 0 (default) | 1

Select this check box to output estimated noise power using the `N`
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NoisePowerOutputPort` |
| **Type:**check box |
| **Values:**0 | 1 |
| **Default:**`0` |

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

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Perform generalized likelihood ratio test detection

The generalized likelihood ratio test detector (GLRT) performs detection of signals with
unknown parameters in the presence of noise. Unknown parameters include signal amplitude,
phase, frequency, and arrival times. The detector replaces unknown parameters by their maximum
likelihood estimates under the signal absent and *H*0
and the alternative signal present *H*1  hypotheses.
Then, the binary detector chooses between the null hypothesis *H*0 and the alternative hypothesis *H*1 based
on the measurements. If the *H*0  hypothesis best
accounts for the data, the detector declares that a target is not present. If the
*H*1  hypothesis best accounts for the data, the
detector declares that a target is present.
