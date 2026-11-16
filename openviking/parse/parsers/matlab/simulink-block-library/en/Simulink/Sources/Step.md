---
type: simulink-block
title: 'Step'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'step'
documentation_source_path: 'slref/step.html'
language: en
---

# Step

## Ports

### Output

### **Port\_1** — Output step signal scalar | vector

Output step function signal defined by the parameters **Step time**,
**Initial value**, and **Final
value**.

**Data Types:** `double` | `single`

## Parameters

### **Step time** — Time when step occurs `1` (default) | scalar

Specify the time, in seconds, when the output jumps from the
**Initial value** parameter to the **Final
value** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Time` |
| **Type**: character vector |
| **Values:** `'1'` | real- or complex-valued scalar, vector, or matrix |
| **Default**: `'1'` |

### **Initial value** — Output value before step `0` (default) | scalar

Specify the block output until the simulation time reaches the
**Step time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Before` |
| **Type**: character vector |
| **Values:** `'1'` | real- or complex-valued scalar, vector, or matrix |
| **Default**: `'0'` |

### **Final value** — Output value after step `1` (default) | scalar

Specify the block output when the simulation time reaches and exceeds the
**Step time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `After` |
| **Type**: character vector |
| **Values:** `'1'` | real- or complex-valued scalar, vector, or matrix |
| **Default**: `'1'` |

### **Sample time** — Sample rate `0` (default) | scalar

Specify the sample rate of step. See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if the
**Constant value** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector. For example,
  the block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **Output data type** — Output data type `double` (default) | `Inherit: Inherit via back propagation` | `single` | `<data type expression>`

Output data type. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via back
propagation`, the block uses the data type of the driving
block.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | <data type expression> |
| **Default:** `'double'` |

### **Mode** — Category of data type `Inherit` (default) | `Built in` | `Expression`

Category of data type, specified as `Inherit`,
`Built in`, or `Expression`. For more
information on using this parameter, see Specify Data Types Using Data Type Assistant.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink® inherits the data type override setting from its
  context, that is, from the block, `Simulink.Signal`
  object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type override setting of its
  context.

For more information, see Specify Data Types Using Data Type Assistant
in the Simulink
documentation.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button, and set the **Mode**
to `Built in`.

#### Tips

The ability to turn off data type override for an individual data type
provides greater control over the data types in your model when you
apply data type override. For example, you can use this option to ensure
that data types meet the requirements of downstream blocks regardless of
the data type override setting.

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

## Version History

**Introduced before R2006a**

## Description

Generate step function

The Step block provides a step between two definable levels at a specified
time. If the simulation time is less than the **Step time** parameter
value, the block's output is the **Initial value** parameter value. For
simulation time greater than or equal to the **Step time**, the output
is the **Final value** parameter value.

The numeric block parameters must be of the same dimensions after scalar expansion. If the
**Interpret vector parameters as 1-D** option is off, the block
outputs a signal of the same dimensions and dimensionality as the parameters. If the
**Interpret vector parameters as 1-D** option is on and the numeric
parameters are row or column vectors (that is, single-row or column 2-D arrays), the
block outputs a vector (1-D array) signal. Otherwise, the block outputs a signal of the
same dimensionality and dimensions as the parameters.
