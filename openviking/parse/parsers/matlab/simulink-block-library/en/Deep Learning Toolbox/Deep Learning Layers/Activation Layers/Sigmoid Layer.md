---
type: simulink-block
title: 'Sigmoid Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Activation Layers'
documentation_page: 'sigmoidlayer'
documentation_source_path: 'ref/sigmoidlayer.html'
language: en
---

# Sigmoid Layer

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Output data scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input data scalar | vector | matrix

The matrix to which to apply the sigmoid function.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output data scalar | vector | matrix

The result of applying the sigmoid function on the input matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Approximation method
  summary: Approximation method for computing layer output None (default) | CORDIC | Lookup
  group: Data Types
  block_parameter: ApproximationMethod
  type: character vector
  values: '''none'' | ''CORDIC'' | ''Lookup'''
  default: '''none'''
- name: Output minimum
  summary: Minimum output value for range checking [] (default) | scalar
  group: Data Types
  block_parameter: OutMin
  values: '''[]'' (default) | scalar in quotes'
- name: Output maximum
  summary: Maximum output value for range checking [] (default) | scalar
  group: Data Types
  block_parameter: OutMax
  values: '''[]'' (default) | scalar in quotes'
- name: Output data type
  summary: 'Data type of output Inherit: Inherit via internal rule (default) | <data type expression>'
  group: Data Types
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | <data type expression>'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Option to prevent fixed-point tools from overriding Output data type off (default) | on
  group: Data Types
  block_parameter: LockScale
  values: '''off'' (default) | ''on'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: Data Types
  block_parameter: RndMeth
  values: '''Floor'' (default) | ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types
  block_parameter: SaturateOnIntegerOverflow
  values: '''off'' (default) | ''on'''
- name: Sample time
  summary: Option to specify sample time -1 (default) | scalar
  group: Execution
  block_parameter: SampleTime
  values: '''-1'' (default) | scalar'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Data Types

### **Approximation method** — Approximation method for computing layer output `None` (default) | `CORDIC` | `Lookup`

Specify the type of approximation for computing the output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating point | You are processing only floating point data. |
| `CORDIC` | Floating point (double and single) and fixed point with a **Bias** value of `0` and a **Slope** value of a power of 2 | You are processing fixed point data and want to deploy to FPGA hardware. |
| `Lookup` | Floating point and fixed point | You are processing fixed point data and want to generate C/C++ code. |

For more information about the CORDIC approximation method, see `cordictanh` (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'none'` | `'CORDIC'` | `'Lookup'` |
| **Default:** `'none'` |

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink)) for
  some blocks.
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes such
  as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual
output signal. Use the Saturation (Simulink) block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink)) for
  some blocks.
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes such
  as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual
output signal. Use the Saturation (Simulink) block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Data type of output `Inherit: Inherit via internal rule` (default) | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see
Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer
`int8` can represent is 127. Any block operation result greater
than this maximum value causes overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127. Similarly,
  the block output saturates at a minimum output value of -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result. For
  example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more information,
  see Troubleshoot Signal Range Errors (Simulink).
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### Execution

### **Sample time** — Option to specify sample time `-1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample time, such as continuous (`0`) or inherited (`-1`). For more options, see Types of Sample Time (Simulink).

By default, the block inherits its sample time based on the context of the block within the
model.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Data Types:** `char` |
| **Values:** `'-1'` (default) | scalar |
## Libraries

Deep Learning Toolbox / Deep Learning Layers / Activation Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: Updated **Output data type** value options

The **Output data type** value options are `'Inherit:
Inherit via internal rule'` and `<data type
expression>`. Previously, the **Output data type**
value options were `'Inherit: Inherit via internal rule'`,
`'Inherit: Keep MSB'`, `'Inherit: Keep
LSB'`, `'Inherit: Inherit via back propagation'`,
`'Inherit: Same as first input'`, and `<data type
expression>`.

### R2025a: **Approximation method** dependencies removed

Block parameters do not depend on the value of **Approximation
method**. Previously, the value of **Approximation method**
had to be `'None'` to enable the other block parameters.

## Description

Sigmoid layer

The Sigmoid Layer block applies a sigmoid function to layer input such that
the output is bounded in the interval (0,1).

The `exportNetworkToSimulink` function generates this block to represent a `sigmoidLayer` object.
Because it applies an element-wise operation, this block supports input data of any format and
outputs data that has the same dimensions and format as the input.
