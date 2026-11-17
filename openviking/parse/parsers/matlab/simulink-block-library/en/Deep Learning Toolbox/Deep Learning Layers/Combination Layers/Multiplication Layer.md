---
type: simulink-block
title: 'Multiplication Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Combination Layers'
documentation_page: 'multiplicationlayer'
documentation_source_path: 'ref/multiplicationlayer.html'
language: en
---

# Multiplication Layer

## Ports
```yaml
ports:
- name: Port_1
  summary: First input data scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_2
  summary: Second input data scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_N
  summary: '*N*th input data scalar | vector | matrix'
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Output data scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — First input data scalar | vector | matrix

First input to multiply, provided as an array that follows the format that you
specify with the **Data format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — Second input data scalar | vector | matrix

Second input to multiply, provided as an array that follows the format that you
specify with the **Data format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — *N*th input data scalar | vector | matrix

*N*th input to multiply, provided as an array that follows the
format that you specify with the **Data format** parameter. The
block has a number of input ports equal to the value that you specify with the
**Number of inputs** block parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output data scalar | vector | matrix

The element-wise product of the input data. The output data uses the format that
you specify with the **Data format** block parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of inputs
  summary: Number of values to layer block 2 (default) | 3 | 4 | 5
  group: Main
  block_parameter: NumInputs
  type: character vector
  values: '''2'' | ''3'' | ''4'' | ''5'''
  default: '''2'''
- name: Data format
  summary: Format of input data SSC (default) | C | CT | SC | SSSC
  group: Main
  block_parameter: DataFormat
  type: character vector
  values: '''SSC'' | ''C'' | ''CT'' | ''SC'' | ''SSSC'''
  default: '''SSC'''
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
  summary: 'Data type of output Inherit: Inherit via internal rule (default) | Inherit: Keep MSB | Inherit: Match scaling
    | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type expression>'
  group: Data Types
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
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

### Main

### **Number of inputs** — Number of values to layer block `2` (default) | `3` | `4` | `5`

Specify the number of inputs to the block. The block computes the product of the
inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumInputs` |
| **Type**: character vector |
| **Values**: `'2'` | `'3'` | `'4'` | `'5'` |
| **Default**: `'2'` |

### **Data format** — Format of input data `SSC` (default) | `C` | `CT` | `SC` | `SSSC`

Data format for the input data. The options use the same
notation as the `fmt` argument of the
`dlarray` object, except layer blocks do not support the Batch
(`B`) dimension and instead assume an observation number of
`1`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataFormat` |
| **Type:** character vector |
| **Values:** `'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **Default:** `'SSC'` |

### Data Types

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Minimum value of the output range that the software checks.

The software uses the minimum value to perform:

- Parameter range checking for some blocks. For more information, see Specify Minimum and Maximum Values for Block Parameters (Simulink).
- Simulation range checking. For more information, see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output signal. Use the Saturation (Simulink) block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Maximum value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking for some blocks. For more information, see Specify Minimum and Maximum Values for Block Parameters (Simulink).
- Simulation range checking. For more information, see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output signal. Use the Saturation (Simulink) block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Data type of output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the **Output** data type you specify on the block. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the rounding of a
block parameter, enter an expression using a MATLAB® rounding function in the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether integer overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data type can represent.

For example, the maximum value that the signed 8-bit integer `int8` can
represent is 127. Any block operation result greater than the maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  –128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is –126.

#### Tips

- Set this parameter to `on` when your model has a possible
  overflow and you want explicit saturation protection in the generated
  code.
- To optimize the efficiency of your generated code, keep the default
  `off` setting for this parameter. Using the default
  setting also helps you avoid overspecifying how the block handles
  out-of-range signals. For more information, see Troubleshoot Signal Range Errors (Simulink).
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or the result.
- In general, the code generation process can detect when overflow is not possible. In this case, the code generator does not produce saturation code.

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

Deep Learning Toolbox / Deep Learning Layers / Combination Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Multiplication layer

The Multiplication Layer block multiplies inputs from multiple neural
network layers element-wise. Each nonscalar input to a Multiplication Layer
block must have the same dimensions and must follow the data format that you specify with the
**Data format** block parameter. The block expands scalar inputs to have
the same dimensions as the other inputs.

The `exportNetworkToSimulink` function generates this block to represent a `multiplicationLayer`
object.
