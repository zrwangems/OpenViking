---
type: simulink-block
title: 'LSTM Projected Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Sequence Layers'
documentation_page: 'lstmprojectedlayer'
documentation_source_path: 'ref/lstmprojectedlayer.html'
language: en
---

# LSTM Projected Layer

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data 2-dimensional array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Output data 2-dimensional array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input data 2-dimensional array

Input data. The data must have two dimensions corresponding to channels and time
steps, in that order.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output data 2-dimensional array

The result of the projected LSTM operation. The output data has two dimensions
corresponding to channels and time steps, in that order.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Layer
  summary: Corresponding layer object layerObject (default) | lstmProjectedLayer object
  group: Main
  block_parameter: Layer
  type: workspace variable
  values: lstmProjectedLayer object
  default: '''layerObject'''
- name: Data format
  summary: Format of input data CT (default)
  group: Main
  block_parameter: DataFormat
  type: character vector
  values: '''CT'''
  default: '''CT'''
- name: Stateful prediction
  summary: Whether to use stateful prediction on (default) | off
  group: Main
  block_parameter: StatefulPrediction
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Activation approximation method
  summary: Approximation method for computing activation function output None (default) | CORDIC | Lookup
  group: Data Types
  block_parameter: ApproximationMethod
  type: character vector
  values: '''None'' | ''CORDIC'' | ''Lookup'''
  default: '''None'''
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
- name: Input weights
  summary: 'Data type of input weights Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: InputWeightsDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Recurrent weights
  summary: 'Data type of recurrent weights Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: RecurrentWeightsDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Bias
  summary: 'Data type of bias Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant value'' |
    <data type expression>'
  group: Data Types
  block_parameter: BiasDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Input projector weights
  summary: 'Data type of input projector weights Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: InputProjectorWeightsDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Output projector weights
  summary: 'Data type of output projector weights Inherit: Inherit via back propagation (default) | Inherit: Inherit from
    ''Constant value'' | <data type expression>'
  group: Data Types
  block_parameter: OutputProjectorWeightsDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Initial cell state
  summary: 'Data type of initial cell state Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: TODODataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Cell state
  summary: 'Data type of cell state Inherit: Inherit via internal rule (default) | Inherit: Keep MSB | Inherit: Keep LSB |
    Inherit: Inherit via back propagation | Inherit: Same as first input | Inherit: Same as accumulator | <data type expression>'
  group: Data Types
  block_parameter: CellStateDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Keep LSB'' | ''Inherit: Inherit
    via back propagation'' | ''Inherit: Same as first input'' | ''Inherit: Same as accumulator'' | <data type expression>'
- name: Initial hidden state
  summary: 'Data type of initial hidden state Inherit: Inherit via back propagation (default) | Inherit: Inherit from ''Constant
    value'' | <data type expression>'
  group: Data Types
  block_parameter: InitialHiddenStateDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''Inherit: Inherit from ''Constant value'''' | <data type
    expression>'
- name: Hidden state
  summary: 'Data type of hidden state Inherit: Inherit via internal rule (default) | Inherit: Keep MSB | Inherit: Match scaling
    | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type expression>'
  group: Data Types
  block_parameter: HiddenStateDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Keep LSB'' | ''Inherit: Inherit
    via back propagation'' | ''Inherit: Same as first input'' | ''Inherit: Same as accumulator'' | <data type expression>'
- name: Input weights matrix multiply output
  summary: 'Data type of input weights matrix multiply output Inherit: Inherit via internal rule (default) | Inherit: Keep
    MSB | Inherit: Match scaling | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type expression>'
  group: Data Types
  block_parameter: InputWeightsMatrixMulitplyOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
- name: Recurrent weights matrix multiply output
  summary: 'Data type of recurrent weights matrix multiply output Inherit: Inherit via internal rule (default) | Inherit:
    Keep MSB | Inherit: Match scaling | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type
    expression>'
  group: Data Types
  block_parameter: RecurrentWeightsMatrixMulitplyOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
- name: Input projector weights matrix multiply output
  summary: 'Data type of input projector weights matrix multiply output Inherit: Inherit via internal rule (default) | Inherit:
    Keep MSB | Inherit: Match scaling | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type
    expression>'
  group: Data Types
  block_parameter: InputProjectorWeightsMatrixMultiplyOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
- name: Output projector weights matrix multiply output
  summary: 'Data type of output projector weights matrix multiply output Inherit: Inherit via internal rule (default) | Inherit:
    Keep MSB | Inherit: Match scaling | Inherit: Inherit via back propagation | Inherit: Same as first input | <data type
    expression>'
  group: Data Types
  block_parameter: OutputProjectorWeightsMatrixMultiplyOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
- name: Linear gate accumulator
  summary: 'Data type of linear gate accumulator Inherit: Inherit via internal rule (default) | Inherit: Same as first input
    | <data type expression>'
  group: Data Types
  block_parameter: LinearGateAccumDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Same as first input'' | <data type expression>'
- name: Linear gate add output
  summary: 'Data type of linear gate sum Inherit: Same as first input (default) | Inherit: Keep MSB | Inherit: Keep LSB |
    Inherit: Inherit via back propagation | Inherit: Inherit via internal rule | Inherit: Same as accumulator | <data type
    expression>'
  group: Data Types
  block_parameter: LinearGateAddOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Keep LSB'' | ''Inherit: Inherit
    via back propagation'' | ''Inherit: Same as first input'' | ''Inherit: Same as accumulator'' | <data type expression>'
- name: Gate activation output
  summary: 'Data type of gate activation output Inherit: Inherit via internal rule (default) | Inherit: Same as first input
    | <data type expression>'
  group: Data Types
  block_parameter: GateActivationoutDataTypeStr
  values: 'Inherit: Inherit via internal rule (default) | Inherit: Same as first input | <data type expression>'
- name: State activation output
  summary: 'Data type of state activation output ''Inherit: Inherit via internal rule'' (default) | ''Inherit: Same as first
    input'' | <data type expression>'
  group: Data Types
  block_parameter: StateActivationOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Same as first input'' | <data type expression>'
- name: Cell state product output
  summary: 'Data type of cell state product Inherit: Inherit via internal rule (default) | Inherit: Keep MSB | Inherit: Inherit
    via back propagation | Inherit: Same as first input | <data type expression>'
  group: Data Types
  block_parameter: CellStateProductOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Inherit via back propagation''
    | ''Inherit: Same as first input'' | <data type expression>'
- name: Cell state accumulator
  summary: 'Data type of cell state accumulator Inherit: Inherit via internal rule (default) | Inherit: Same as first input
    | <data type expression>'
  group: Data Types
  block_parameter: CellStateProductOutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Same as first input'' | <data type expression>'
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

### **Layer** — Corresponding layer object `layerObject` (default) | `lstmProjectedLayer` object

Specify the name of a workspace variable that contains an
`lstmProjectedLayer` object from a trained network. The LSTM
Projected Layer block configures itself by using the properties of the
object and calculates the block output by using the learnable parameters of the
object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layer` |
| **Type:** workspace variable |
| **Values:** `lstmProjectedLayer` object |
| **Default:** `'layerObject'` |

### **Data format** — Format of input data `CT` (default)

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
| **Values:** `'CT'` |
| **Default:** `'CT'` |

### **Stateful prediction** — Whether to use stateful prediction on (default) | off

Whether to use stateful prediction, specified as a boolean. If
`true`, the block maintains the cell state and hidden state between
time steps. If `false`, the block performs stateless prediction by
resetting cell states and hidden states to their initial values at the beginning of each
time step. Use stateless prediction for frame-based processing where Simulink step time represents frame period and the network processes multiple
samples at each time step. For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StatefulPrediction` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Data Types

### **Activation approximation method** — Approximation method for computing activation function output `None` (default) | `CORDIC` | `Lookup`

If the object that you pass as the value of the **Layer** parameter
uses the `tanh` state activation function or the
`sigmoid` gate activation function, then the block uses the
approximation method that you specify to compute the layer output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating-point | You are processing only floating-point data. |
| `CORDIC` | Floating-point (double and single) and fixed-point with a **Bias** value of `0` and a **Slope** value of a power of 2 | You are processing fixed-point data and want to deploy to FPGA hardware. |
| `Lookup` | Floating-point and fixed-point | You are processing fixed-point data and want to generate C/C++ code. |

For more information about the CORDIC approximation method, see `cordictanh` (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'None'` | `'CORDIC'` | `'Lookup'` |
| **Default:** `'None'` |

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

#### Dependencies

To enable this parameter, set **Output data type** to a value
other than `Inherit: Inherit via internal rule`.

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

#### Dependencies

To enable this parameter, set **Output data type** to a value
other than `Inherit: Inherit via internal rule`.

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

### **Input weights** — Data type of input weights `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `InputWeights` property of the
object that you specify with the **Layer** parameter to this data
type. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputWeightsDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Recurrent weights** — Data type of recurrent weights `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `RecurrentWeights` property of the
object that you specify with the **Layer** parameter to this data
type. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RecurrentWeightsDataTypeStr` |
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

### **Input projector weights** — Data type of input projector weights `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `InputProjector` property of
the object that you specify with the **Layer** parameter to this
data type. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

For more information, see LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputProjectorWeightsDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Output projector weights** — Data type of output projector weights `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `OutputProjector` property of
the object that you specify with the **Layer** parameter to this
data type. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

For more information, see LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputProjectorWeightsDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Initial cell state** — Data type of initial cell state `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `CellState` property of the
object that you specify with the **Layer** parameter to this data
type. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

This parameter affects only the initial cell state, *c*0. To cast later cell state values, use the **Cell
state** parameter. For more information, see Long Short-Term Memory Layer

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `TODODataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Cell state** — Data type of cell state `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

Choose the data type for the output of the Sum block
`ForIteratorSubsystem/LSTMProjectedCore/CellAdd` inside the
LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Sum block computes the
cell state *c**t* as *c**t*=*f**t*⊙*c**t*-1+*i**t*⊙*g**t*, where *i*, *f*, and
*g* denote the input gate, forget gate, and cell candidate gate,
respectively, and ⊙ denotes the Hadamard product (element-wise multiplication of
vectors). For more information, see Long Short-Term Memory Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CellStateDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Initial hidden state** — Data type of initial hidden state `Inherit: Inherit via back propagation` (default) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

The block casts the value of the `HiddenState` property of the
object that you specify with the **Layer** parameter to this data
type. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

This parameter affects only the initial hidden state, *h*0. To cast later hidden state values, use the **Hidden
state** parameter. For more information, see Long Short-Term Memory Layer

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialHiddenStateDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Hidden state** — Data type of hidden state `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Product block
`ForIteratorSubsystem/LSTMProjectedCore/HiddenStateProduct` inside
the LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Product block computes
the hidden state *h**t* as *h**t*=*o**t*⊙*σ**c*(*c**t*),where *o* denotes the output gate, *σ**c* denotes the
state activation function, and ⊙ denotes the Hadamard product (element-wise
multiplication of vectors). For more information, see Long Short-Term Memory Layer and LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `HiddenStateDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Input weights matrix multiply output** — Data type of input weights matrix multiply output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Product block
`InputWeightsMatrixMultiply/W*x` inside the LSTM Projected
Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Product block computes
the product of the input weights (*W*) and the projected input at the
time step (*x**t*). For more
information, see Long Short-Term Memory Layer and LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputWeightsMatrixMulitplyOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Recurrent weights matrix multiply output** — Data type of recurrent weights matrix multiply output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Product block
`ForIteratorSubsystem/LSTMProjectedCore/RecurrentWeightsMatrixMultiply/R*h_t-1`
inside the LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Product block computes
the product of the recurrent weights (*R*) and the projected hidden
state at the previous time step
(*h**t*-1). For more
information, see Long Short-Term Memory Layer and LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RecurrentWeightsMatrixMulitplyOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Input projector weights matrix multiply output** — Data type of input projector weights matrix multiply output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Product block
`InputWeightsMatrixMultiply/x'*Q_in` inside the LSTM
Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

The Product block computes the product of the transposed input
(*x*T) and the input projector weights
(*Q*in). For more information, see LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputProjectorWeightsMatrixMultiplyOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Output projector weights matrix multiply output** — Data type of output projector weights matrix multiply output `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Product block
`ForIteratorSubsystem/LSTMProjectedCore/RecurrentWeightsMatrixMultiply/h_t-1'*Q_out`
inside the LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Product block computes
the product of the transposed previous hidden state
(*h**t*-1T)
and the output projector weights (*Q*out). For
more information, see LSTM Projected Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputProjectorWeightsMatrixMultiplyOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Linear gate accumulator** — Data type of linear gate accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the accumulator of the Sum block
`ForIteratorSubsystem/LSTMProjectedCore/LinearGateAdd/Wx+Rh+b`
inside the LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

The Sum block computes the sum *W**QinT**x*+*R**QoutT**h*t+*b*, where *W* denotes the input weights,
*Qin* denotes the input projector matrix,
*x* denotes the input, *R* denotes the recurrent
weights, *Qout* denotes the output projector
matrix, *h**t* denotes the
hidden state at time step *t*, and *b* denotes the
bias. For more information, see Long Short-Term Memory Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `LinearGateAccumDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as first input'` | `<data type expression>` |

### **Linear gate add output** — Data type of linear gate sum `Inherit: Same as first input` (default) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Inherit via internal rule` | `Inherit: Same as accumulator` | `<data type expression>`

Choose the data type for the output of the Sum block
`ForIteratorSubsystem/LSTMProjectedCore/LinearGateAdd/Wx+Rh+b`
inside the LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

The Sum block computes the sum *W**QinT**x*+*R**QoutT**h*t+*b*, where *W* denotes the input weights,
*Qin* denotes the input projector matrix,
*x* denotes the input, *R* denotes the recurrent
weights, *Qout* denotes the output projector
matrix, *h**t* denotes the
hidden state at time step *t*, and *b* denotes the
bias. For more information, see Long Short-Term Memory Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `LinearGateAddOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Gate activation output** — Data type of gate activation output `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the gate activation function. For more information about gate activation functions, see **GateActivationFunction**. For more information on how an LSTM layer uses activation functions, see Long Short-Term Memory Layer.

The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `GateActivationoutDataTypeStr` |
| **Values:** | `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>` |

### **State activation output** — Data type of state activation output `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as first input'` | `<data type expression>`

Choose the data type for the output of the state activation function. For more information about state activation functions, see **StateActivationFunction**. For more information on how an LSTM layer uses activation functions, see Long Short-Term Memory Layer.

The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `StateActivationOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as first input'` | `<data type expression>` |

### **Cell state product output** — Data type of cell state product `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the output of the Product blocks
`ForIteratorSubsystem/LSTMProjectedCore/f*c_t-1` and
`ForIteratorSubsystem/LSTMProjectedCore/i*g` inside the LSTM
Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Product blocks compute
the Hadamard products (element-wise multiplication of vectors, denoted as ⊙) *f*t⊙*c**t*-1 and *i**t*⊙*g**t*, where *f* denotes the forget gate,
*c* denotes the cell state, *i* denotes the input
gate, and *g* denotes the cell candidate. For more information, see
Long Short-Term Memory Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CellStateProductOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Cell state accumulator** — Data type of cell state accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

Choose the data type for the accumulator of the Sum block
`ForIteratorSubsystem/LSTMProjectedCore/CellAdd` inside the
LSTM Projected Layer block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`. When you select `Inherit: Inherit via internal rule`,
Simulink chooses a data type to balance numerical accuracy, performance, and generated code
size, while taking into account the properties of the embedded target hardware.

For a time step *t*, the Sum block computes the
cell state *c**t* as

|  |  |
| --- | --- |
| *c**t*=*f**t*⊙*c**t*-1+*i**t*⊙*g**t* | **(1)** |

,

where *i*, *f*, and *g* denote
the input gate, forget gate, and cell candidate gate, respectively, and ⊙ denotes the
Hadamard product (element-wise multiplication of vectors). For more information, see
Long Short-Term Memory Layer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CellStateProductOutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as first input'` | `<data type expression>` |

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

Deep Learning Toolbox / Deep Learning Layers / Sequence Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: **Layer** parameter default value is `'layerObject'`

Starting in R2025a, the default value for the **Layer** parameter is `'layerObject'`. In previous versions, the default value is `'layer'`. If you have code that programmatically creates Simulink and relies on variables with the name `'layer'`, update your code so that the variable has the name `'layerObject'`.

### R2025a: **Gate activation output** and **State activation output** parameters

New **Gate activation output** and **State activation
output** parameters control the data types of the gate and state activation
outputs.

### R2025a: **Linear gate add output** parameter default value is `Inherit: Same as first input`

The default value of **Linear gate add output** is now
`Inherit: Same as first input`.

## Description

Long short-term memory (LSTM) projected layer for recurrent neural network (RNN)

The LSTM Projected Layer block represents a recurrent neural network (RNN)
layer that learns long-term dependencies between time steps in time-series and sequence data
in the `CT` format (two dimensions corresponding to channels and time steps,
in that order) by using projected learnable weights.

To compress a deep learning network, you can use *projected layers*. A
projected layer is a type of deep learning layer that enables compression by reducing the
number of stored learnable parameters. The layer introduces learnable projector matrices
*Q*, replaces multiplications of the form Wx, where *W* is a learnable matrix, with the multiplication WQQ⊤x, and stores *Q* and W′=WQ instead of storing *W*. Projecting *x*
into a lower dimensional space using *Q* typically requires less memory to
store the learnable parameters and can have similarly strong prediction accuracy.

Reducing the number of learnable parameters by projecting an LSTM layer rather than
reducing the number of hidden units of the LSTM layer maintains the output size of the layer
and, in turn, the sizes of the downstream layers, which can result in better prediction
accuracy.

The `exportNetworkToSimulink` function generates this block to represent an `lstmProjectedLayer`
object.
