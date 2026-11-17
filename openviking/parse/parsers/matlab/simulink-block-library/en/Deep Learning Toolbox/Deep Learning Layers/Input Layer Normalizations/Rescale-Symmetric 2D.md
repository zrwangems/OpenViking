---
type: simulink-block
title: 'Rescale-Symmetric 2D'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Input Layer Normalizations'
documentation_page: 'rescalesymmetric2d'
documentation_source_path: 'ref/rescalesymmetric2d.html'
language: en
---

# Rescale-Symmetric 2D

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data 3-dimensional array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Normalized output data 3-dimensional array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input data 3-dimensional array

Input data to normalize. The data must have three dimensions corresponding to two
spatial dimensions and one channel dimension, in that order.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Normalized output data 3-dimensional array

Normalized output data. The output data has three dimensions corresponding to two
spatial dimensions and one channel dimension, in that order.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Layer
  summary: Corresponding layer object layerObject (default) | imageInputLayer object
  group: Main
  block_parameter: Layer
  type: workspace variable
  values: imageInputLayer object
  default: '''layerObject'''
- name: Data format
  summary: Format of input data SSC (default)
  group: Main
  block_parameter: DataFormat
  type: character vector
  values: '''SSC'''
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
  summary: 'Data type of output Inherit: Inherit via internal rule (default) | Inherit: Keep MSB | Inherit: Keep LSB | Inherit:
    Inherit via back propagation | Inherit: Same as first input | Inherit: Same as accumulator | <data type expression>'
  group: Data Types
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Keep LSB'' | ''Inherit: Inherit
    via back propagation'' | ''Inherit: Same as first input'' | ''Inherit: Same as accumulator'' | <data type expression>'
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types
  block_parameter: LockScale
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output integer rounding mode
  summary: Rounding mode for fixed-point output cast operation Floor (default) | Ceiling | Convergent | Nearest | Round |
    Simplest | Zero
  group: Data Types
  block_parameter: RndMeth
  values: '''Floor'' (default) | ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Output saturate on integer overflow
  summary: Method of overflow action for output cast operation off (default) | on
  group: Data Types
  block_parameter: SaturateOnIntegerOverflow
  values: '''off'' (default) | ''on'''
- name: Min
  summary: 'Data type of minimum value Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: MinDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Max
  summary: 'Data type of maximum value Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: MaxDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Divide output
  summary: 'Data type of division output Inherit: Inherit via internal rule (default) | Inherit: Keep MSB | Inherit: Match
    scaling | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type expression>'
  group: Data Types
  block_parameter: DivideOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
- name: Subtract Min Accumulator
  summary: 'Data type of accumulator for SubtractMin block Inherit: Inherit via internal rule (default) | Inherit: Same as
    first input | <data type expression>'
  group: Data Types
  block_parameter: SubtractMinAccumDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Same as first input'' | <data type expression>'
- name: Subtract one Accumulator
  summary: 'Data type of accumulator for SubtractOne block Inherit: Inherit via internal rule (default) | Inherit: Same as
    first input | <data type expression>'
  group: Data Types
  block_parameter: SubtractOneAccumDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Same as first input'' | <data type expression>'
- name: Internal integer rounding mode
  summary: Rounding mode for internal fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest
    | Zero
  group: Data Types
  block_parameter: InternalRndMeth
  values: '''Floor'' (default) | ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Internal saturate on integer overflow
  summary: Method of overflow action for internal block operations off (default) | on
  group: Data Types
  block_parameter: InternalSaturateOnIntegerOverflow
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

### **Layer** — Corresponding layer object `layerObject` (default) | `imageInputLayer` object

Specify the name of a workspace variable that contains an
`imageInputLayer` object that comes from a trained network and has
the `Normalization` property set to
`"rescale-symmetric"`. The Rescale-Symmetric 2D
block configures itself by using the properties of the object and calculates the block
output by using the `Min` and `Max` properties
of the object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layer` |
| **Type:** workspace variable |
| **Values:** `imageInputLayer` object |
| **Default:** `'layerObject'` |

### **Data format** — Format of input data `SSC` (default)

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
| **Values:** `'SSC'` |
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

### **Output data type** — Data type of output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Output integer rounding mode** — Rounding mode for fixed-point output cast operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for the output value of the block, generated by the final
fixed-point cast operation. For the rounding mode for the other internal block
operations, see **Internal integer rounding mode**. For more
information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function in the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Output saturate on integer overflow** — Method of overflow action for output cast operation `off` (default) | `on`

Specify whether integer overflows saturate or wrap for the output value of the block,
generated by the final fixed-point cast operation. For the method of overflow action of
the internal block operations, see **Internal saturate on integer
overflow**.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than the maximum value causes
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
- When you select this parameter, saturation applies to only the output or
  the result.
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

### **Min** — Data type of minimum value `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `Min` property of the object that
you specify with the **Layer** parameter to this data type.
The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `MinDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Max** — Data type of maximum value `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `Max` property of the object that
you specify with the **Layer** parameter to this data type.
The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Divide output** — Data type of division output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Divide (Simulink) block inside each Neighborhood
Processing Subsystem (Simulink) block inside the Rescale-Symmetric 2D
block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DivideOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Subtract Min Accumulator** — Data type of accumulator for SubtractMin block `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

Choose the data type of the SubtractMin block within the layer block.
This block subtracts the trained minimum from the input. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SubtractMinAccumDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as first input'` | `<data type expression>` |

### **Subtract one Accumulator** — Data type of accumulator for SubtractOne block `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

Choose the data type of the SubtractOne block within the layer block.
This block subtracts the constant 1 in internal operations. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SubtractOneAccumDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as first input'` | `<data type expression>` |

### **Internal integer rounding mode** — Rounding mode for internal fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for internal fixed-point computations except for the output
operation. For the rounding mode of the output operation, see **Output integer
rounding mode**. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB rounding function in the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InternalRndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Internal saturate on integer overflow** — Method of overflow action for internal block operations `off` (default) | `on`

Specify whether integer overflows saturate or wrap for the internal operations of the
block. For the method of overflow action of the block output, see **Output
saturate on integer overflow**.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than the maximum value causes
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
- When you select this parameter, saturation applies just to internal
  operations of the block.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InternalSaturateOnIntegerOverflow` |
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

Deep Learning Toolbox / Deep Learning Layers / Input Layer Normalizations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: **Layer** parameter default value is `'layerObject'`

Starting in R2025a, the default value for the **Layer** parameter is `'layerObject'`. In previous versions, the default value is `'layer'`. If you have code that programmatically creates Simulink and relies on variables with the name `'layer'`, update your code so that the variable has the name `'layerObject'`.

### R2025a: Updated integer rounding mode, saturate on integer overflow, and accumulator parameters

The **Integer rounding mode** and **Saturate integer overflow** parameters are now split into output and internal versions of the parameters. **Output integer rounding mode** and **Output saturate on integer overflow** control the behavior of the final cast operation of the output of the block. **Internal integer rounding mode** and **Internal saturate on integer overflow** control the internal block operations.

New **Subtract Min Accumulator** and **Subtract one
Accumulator** parameters control the data types of accumulators within the layer
block.

## Description

2-D input layer with rescale-symmetric normalization

The Rescale-Symmetric 2D block inputs 2-dimensional image data (data with
three dimensions corresponding to two spatial dimensions and one channel dimension, in that
order) to a neural network and rescales the input to be in the range [-1, 1].

The `exportNetworkToSimulink` function generates this block to represent an `imageInputLayer`
object that has the `Normalization` property set to
`"rescale-symmetric"`.
