---
type: simulink-block
title: 'Discrete Zero-Pole'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'discretezeropole'
documentation_source_path: 'slref/discretezeropole.html'
language: en
---

# Discrete Zero-Pole

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar
  direction: input
  data_types: single | double
- name: Port_1
  summary: Model of discrete system scalar | vector
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — Input signal scalar

Input signal specified as a real-valued scalar.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Model of discrete system scalar | vector

Model of system as defined by zeros, poles, and gain of discrete
transfer function. The width of the output is equal to the number of
columns in the **Zeros** matrix, or one if
**Zeros** is a vector.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Zeros
  summary: Matrix of zeros [1] (default) | vector | matrix
  group: Main
  block_parameter: Zeros
  type: character vector
  values: vector
  default: '''[1]'''
- name: Poles
  summary: Vector of poles [0 0.5] (default) | vector
  group: Main
  block_parameter: Poles
  type: character vector
  values: vector
  default: '''[0 0.5]'''
- name: Gain
  summary: Gain value 1 (default) | scalar | vector
  group: Main
  block_parameter: Gain
  type: character vector
  values: scalar | vector
  default: '''1'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 | scalar | vector
  group: Main
  block_parameter: SampleTime
  type: character vector
  values: scalar | vector
  default: '''-1'''
- name: State name
  summary: Unique name for block state '' (default) | alphanumeric string
  group: State Attributes
  block_parameter: StateName
  type: character vector
  values: unique name
  default: ''''''
- name: State name must resolve to Simulink signal object
  summary: Require state name resolve to a signal object off (default) | on
  group: State Attributes
  block_parameter: StateMustResolveToSignalObject
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### Main

### **Zeros** — Matrix of zeros `[1]` (default) | vector | matrix

Specify the vector or matrix of zeros. The number of zeros must be
less than or equal to the number of poles. If the poles and zeros are
complex, they must be complex conjugate pairs.

- For a single-output system, enter a vector for the zeros of
  the transfer function.
- For a multiple-output system, enter a matrix. Each column of
  the matrix contains the zeros of a transfer function that
  relates the system input to one of the outputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Zeros` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[1]'` |

### **Poles** — Vector of poles `[0 0.5]` (default) | vector

Specify the vector of poles. The number of poles must be greater than or equal to the
number of zeros. If the poles and zeros are complex, they must be
complex conjugate pairs.

- For a single-output system, enter a vector for the poles of
  the transfer function.
- For a multiple-output system, enter a vector for the poles
  common to all transfer functions of the system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Poles` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0 0.5]'` |

### **Gain** — Gain value `1` (default) | scalar | vector

Specify vector of gain values.

- For a single-output system, enter a scalar or 1-by-1 vector
  for the gain of the transfer function.
- For a multiple-output system, enter a vector of gains. Each
  element is the gain of the corresponding transfer function in
  **Zeros**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Gain` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` | scalar | vector

Specify the time interval between samples. For more information, see
Specifying Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink® signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |
## Libraries

Simulink / Discrete

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset` functions
(`string.h`) under certain conditions.

## Version History

**Introduced before R2006a**

## Description

Model system defined by zeros and poles of discrete transfer function

The Discrete Zero-Pole block models a discrete system defined by the zeros,
poles, and gain of a *z*-domain transfer function. This block assumes
that the transfer function has the following form:

H(z)=KZ(z)P(z)=K(z−Z1)(z−Z2)...(z−Zm)(z−P1)(z−P2)...(z−Pn),

where *Z* represents the zeros vector, *P* the poles
vector, and *K* the gain. The number of poles must be greater than or
equal to the number of zeros (*n* ≥ *m*). If
the poles and zeros are complex, they must be complex conjugate pairs.

The block displays the transfer function depending on how the
parameters are specified. See Zero-Pole for more information.

### Modeling a Single-Output System

For a single-output system, the input and the output of the block are scalar
time-domain signals. To model this system:

1. Enter a vector for the zeros of the transfer function in the
   **Zeros** field.
2. Enter a vector for the poles of the transfer function in the
   **Poles** field.
3. Enter a 1-by-1 vector for the gain of the transfer function in the
   **Gain** field.

### Modeling a Multiple-Output System

For a multiple-output system, the block input is a scalar and the output is a
vector, where each element is an output of the system. To model this system:

1. Enter a matrix of zeros in the **Zeros** field.

   Each *column* of this matrix contains the zeros of a
   transfer function that relates the system input to one of the
   outputs.
2. Enter a vector for the poles common to all transfer functions of the
   system in the **Poles** field.
3. Enter a vector of gains in the **Gain** field.

   Each element is the gain of the corresponding transfer function in
   **Zeros**.

Each element of the output vector corresponds to a column in
**Zeros**.
