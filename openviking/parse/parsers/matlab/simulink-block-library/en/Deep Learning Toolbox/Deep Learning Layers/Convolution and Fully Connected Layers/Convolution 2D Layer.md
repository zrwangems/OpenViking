---
type: simulink-block
title: 'Convolution 2D Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Convolution and Fully Connected Layers'
documentation_page: 'convolution2dlayer'
documentation_source_path: 'ref/convolution2dlayer.html'
language: en
---

# Convolution 2D Layer

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data 3-dimensional array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Convolved output data 3-dimensional array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input data 3-dimensional array

Input data on which to perform the convolution operation. The data must have three
dimensions corresponding to two spatial dimensions and one channel dimension, in that
order.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Convolved output data 3-dimensional array

The result of convolving the input data over the first two (spatial) dimensions.
The output data has three dimensions corresponding to two spatial dimensions and one
channel dimension, in that order.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Layer
  summary: Corresponding layer object layerObject (default) | convolution2dLayer object
  group: Main
  block_parameter: Layer
  type: workspace variable
  values: convolution2dLayer object
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
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Option to prevent fixed-point tools from overriding Output data type off (default) | on
  group: Data Types
  block_parameter: LockScale
  values: '''off'' (default) | ''on'''
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
- name: Weights
  summary: 'Data type of weights Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant value''
    | <data type expression>'
  group: Data Types
  block_parameter: WeightsDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Bias
  summary: 'Data type of bias Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant value'' |
    <data type expression>'
  group: Data Types
  block_parameter: BiasDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Accumulator
  summary: 'Data type of accumulator Inherit: Inherit via internal rule (default) | Inherit: Same as first input | <data type
    expression>'
  group: Data Types
  block_parameter: AccumDataTypeStr
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

### **Layer** — Corresponding layer object `layerObject` (default) | `convolution2dLayer` object

Specify the name of a workspace variable that contains a
`convolution2dLayer` object from a trained network. The
Convolution 2D Layer block configures itself by using the properties
of the object and calculates the block output by using the learnable parameters of the
object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layer` |
| **Type:** workspace variable |
| **Values:** `convolution2dLayer` object |
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

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the **Output** data type you specify on the block. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

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

### **Weights** — Data type of weights `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `Weights` property of the object
that you specify with the **Layer** parameter to this data type.
The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `WeightsDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Bias** — Data type of bias `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `Bias` property of the object that
you specify with the **Layer** parameter to this data type.
The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `BiasDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Accumulator** — Data type of accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

Choose the data type of the accumulator for each Convolution block
inside the Convolution 2D Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `AccumDataTypeStr` |
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

Deep Learning Toolbox / Deep Learning Layers / Convolution and Fully Connected Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: **Layer** parameter default value is `'layerObject'`

Starting in R2025a, the default value for the **Layer** parameter is `'layerObject'`. In previous versions, the default value is `'layer'`. If you have code that programmatically creates Simulink and relies on variables with the name `'layer'`, update your code so that the variable has the name `'layerObject'`.

### R2025a: Updated integer rounding mode and saturate on integer overflow parameters

The **Integer rounding mode** and **Saturate integer overflow** parameters are now split into output and internal versions of the parameters. **Output integer rounding mode** and **Output saturate on integer overflow** control the behavior of the final cast operation of the output of the block. **Internal integer rounding mode** and **Internal saturate on integer overflow** control the internal block operations.

## Description

2-D convolutional layer

The Convolution 2D Layer block applies sliding convolutional filters to 2-D
input. The layer convolves the input by moving the filters along the input vertically and
horizontally and computing the dot product of the weights and the input, and then adding a
bias term. This block accepts 2-D image data in the `SSC` format (three
dimensions corresponding to two spatial dimensions and one channel dimension, in that order)
and convolves over the spatial dimensions.

The `exportNetworkToSimulink` function generates this block to represent a `convolution2dLayer`
object.
