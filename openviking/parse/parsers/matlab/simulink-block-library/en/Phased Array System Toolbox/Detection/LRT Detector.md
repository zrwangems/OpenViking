---
type: simulink-block
title: 'LRT Detector'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'lrtdetector'
documentation_source_path: 'ref/lrtdetector.html'
language: en
---

# LRT Detector

## Ports
```yaml
ports:
- name: X
  summary: Input data real-valued *N*-by-*1* vector | complex-valued *N*-by-*1* vector | real-valued *N*-by-*M* matrix | complex-valued
    *N*-by-*M* matrix
  direction: input
  data_types: single | double
- name: XK
  summary: Known signal real-valued *N*-by-1 vector | complex-valued *N*-by-1 vector
  direction: input
  data_types: single | double
- name: NCov
  summary: Noise power positive scalar
  direction: input
  data_types: single | double
- name: Y
  summary: Detection results 1-by-*M* logical-valued vector | 1-by-*L* integer-valued vector
  direction: output
  data_types: single | double | Boolean
- name: Stat
  summary: Detection statistics *D*-by-*M* (default) | matrix | 1-by-*L* vector
  direction: output
  data_types: single | double
- name: Th
  summary: Detection threshold scalar
  direction: output
  data_types: single | double
```

### Input

### **X** — Input data real-valued *N*-by-*1* vector | complex-valued *N*-by-*1* vector | real-valued *N*-by-*M* matrix | complex-valued *N*-by-*M* matrix

Input data, specified as a real-valued or complex-valued
*N*-by-*1* vector, or an
*N*-by-*M* real-valued or complex-valued matrix.
*N* is the signal length and *M* is the number of
data channels. Each data channel has *N* samples to yield an
*N*-by-*M* matrix. Each row represents the
components of a length-*M* data vector. When *M =
1*, `X` represents a single channel of data. When
*M > 1*, `X` can represent *N*
samples from *M* data channels. Detection is performed along the
columns of `X`. The size of each row *M* cannot
change during the simulation.

The LRT detector assumes the same signal model in each column of
`X`. The noise-free signal is contained in the
*N*-dimensional data vector `Xknown`. Gaussian
noise, defined by the noise power `NCov`, is added to each column.
For this signal model, the LRT detector determines whether or not to reject the null
hypothesis `Xknown` `= 0`. Because there is only
one known signal model, the LRT detector outputs one detection result for each column
of `X`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **XK** — Known signal real-valued *N*-by-1 vector | complex-valued *N*-by-1 vector

Known noise-free signal, specified as a real-valued or complex-valued
*N*-by-1 vector.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **NCov** — Noise power positive scalar

Noise power or covariance, specified as a positive scalar.

**Example:** `2.0`

**Data Types:** `single` | `double`
### Output

### **Y** — Detection results 1-by-*M* logical-valued vector | 1-by-*L* integer-valued vector

Detection results, returned as a 1-by-*M* logical-valued vector
or a 1-by-*L* integer-valued vector. The format of
`Y` depends on the value of the **Output
format** parameter. By default, the **Output format**
parameter is set to `'Detection result'`.

- When the **Output format** parameter is set to
  `'Detection result'`, `Y` is a
  1-by-*M* vector containing logical detection results, where
  *M* is the number of columns of `X`.
  `Y` is `true` if there is a detection in the
  corresponding column of `X`. Otherwise, `Y`
  is `false`.
- When the **Output format** parameter is set to
  `'Detection index'`, `Y` is a
  1-by-*L* integer-valued vector containing detection indices,
  where *L* is the number of detections found over all
  *M* channels.

**Data Types:** `single` | `double` | `Boolean`
**Complex Number Support:** Yes

### **Stat** — Detection statistics *D*-by-*M* (default) | matrix | 1-by-*L* vector

Detection statistics, returned as a *D*-by-*M*
matrix or as a 1-by-*L* vector. The format of
`stat` depends on the setting of the **Output
format** parameter.

- When **Output format** parameter is `'Detection
  result'`, `stat` is a
  *D*-by-*M* matrix.
- When **Output format** parameter is `'Detection
  index'`, `stat` is a 1-by-*L*
  vector containing detection statistics for each corresponding detection in
  *Y*.

#### Dependencies

To enable this port, select the **Output detection statistics and
threshold** check box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Th** — Detection threshold scalar

Detection threshold, returned as a scalar.

#### Dependencies

To enable this port, select the **Output detection statistics and
threshold** check box.

**Data Types:** `single` | `double`
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
  summary: Output detection statistics and threshold false (default) | true
  group: ''
  block_parameter: ThresholdOutputPort
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

### **Output detection statistics and threshold** — Output detection statistics and threshold `false` (default) | `true`

Select this checkbox to output detection statistics and detection threshold using
the **Stat** and **Th** ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ThresholdOutputPort` |
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

Likelihood ratio test detector

The likelihood ratio test (LRT) detector performs binary signal detection in the presence
of noise. The binary detector chooses between the null hypothesis
*H*0  and the alternative hypothesis
*H*1 based on data measurements. The null hypothesis
denotes the absence of any signal while the alternative hypothesis denotes the presence of
some signal.
