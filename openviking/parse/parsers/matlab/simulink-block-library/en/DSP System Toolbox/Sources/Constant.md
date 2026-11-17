---
type: simulink-block
title: 'Constant'
family: 'libsb2sl'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'MAT'
documentation_page: 'constant'
documentation_source_path: 'ref/constant.html'
language: en
---

# Constant

## Ports
```yaml
ports:
- name: Port_1
  summary: Constant value scalar | vector | matrix | N-D array
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### Output

### **Port\_1** — Constant value scalar | vector | matrix | N-D array

Constant value, specified as a real or complex valued scalar, vector, matrix, or N-D
array. By default, the Constant block outputs a signal
whose dimensions, data type, and complexity are the same as those of the
**Constant value** parameter. However, you can
specify the output to be any data type that Simulink® supports, including fixed-point and enumerated data
types.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Constant value
  summary: Constant output value scalar | vector | matrix | N-D array
  group: Main
  block_parameter: Value
  values: scalar in quotes | vector in quotes | matrix in quotes | array in quotes
- name: Interpret vector parameters as 1-D
  summary: Treat vectors as 1-D on (default) | off
  group: Main
  block_parameter: VectorParams1D
  values: '''on'' (default) | ''off'''
- name: Sample time
  summary: Sampling interval inf (default) | scalar | vector
  group: Main
  block_parameter: SampleTime
  values: '''inf''  (default) | scalar in quotes | vector in quotes'
- name: Output minimum
  summary: Minimum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMin
  values: '''[ ]'' (default) | scalar in quotes'
- name: Output maximum
  summary: Maximum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMax
  values: '''[ ]'' (default) | scalar in quotes'
- name: Output data type
  summary: 'Output data type Inherit: Inherit from ''Constant value'' (default) | Inherit: Inherit via back propagation |
    double | single | half | int8 | int16 | ...'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit from ''Constant value'''' (default) | ''Inherit: Inherit via back propagation'' | ''double''
    | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64''
    | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''Enum: <class name>'' | ''Bus: <object
    name>'' | ''ValueType: <object name>'' | ''<data type expression>'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding Output data type off (default) | on
  group: Signal Attributes
  block_parameter: LockScale
  values: '''off'' (default) | ''on'''
- name: Mode
  summary: Category of data to specify Inherit (default) | Built in | Fixed point | Enumerated | Bus object | Value type |
    Expression
  group: Signal Attributes
- name: Data type override
  summary: Specify data type override mode for this signal Inherit | Off
  group: Signal Attributes
- name: Signedness
  summary: Specify signed or unsigned Signed (default) | Unsigned
  group: Signal Attributes
- name: Scaling
  summary: Method for scaling fixed-point data Best precision (default) | Binary point | Slope and bias
  group: Signal Attributes
- name: Word length
  summary: Bit size of the word that holds the quantized integer 16 (default) | integer from 0 to 32
  group: Signal Attributes
- name: Fraction length
  summary: Specify fraction length for fixed-point data type 0 (default) | scalar integer
  group: Signal Attributes
- name: Slope
  summary: Specify slope for the fixed-point data type 2^0 (default) | positive, real-valued scalar
  group: Signal Attributes
- name: Bias
  summary: Specify bias for the fixed-point data type 0 (default) | real-valued scalar
  group: Signal Attributes
```

### Main

### **Constant value** — Constant output value scalar | vector | matrix | N-D array

Specify the constant value output of the block.

The default value depends on the block you add.

- `1` — Constant or
  One block
- `0` — Zero block
- `inf` — Inf block
- `-inf` — Negative Inf
  block
- `exp(1)` — Eulers Number
  block
- `pi` — Pi block
- `NaN` — NaN block

You can enter any expression that MATLAB evaluates as a matrix, including the Boolean keywords
`true` and `false`.

If you set **Output data type** to a bus object,
you can specify one of these options:

- A full MATLAB structure corresponding to the bus
  object
- `0` to indicate a structure corresponding
  to the ground value of the bus object

For details, see Using Bus Objects as the Output Data Type.

For nonbus data types, Simulink converts this parameter from its value data type to the
specified output data type offline, using a rounding method of nearest
and overflow action of saturate.

#### Dependencies

The software ignores the data type of the constant value when **Output
data type** specifies a `Simulink.ValueType`
object.

When this parameter specifies a `Simulink.Parameter` object and
**Output data type** specifies a
`Simulink.ValueType` object:

- The block uses the minimum, maximum, and data type specified by the
  `Simulink.ValueType` object.
- The block uses the unit specified by the
  `Simulink.Parameter` object.
- The dimensions and complexity specified by the objects must match.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Value` |
| **Values:** | scalar in quotes | vector in quotes | matrix in quotes | array in quotes |
| **Data Types:** | `char` | `string` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length
`N` if the **Constant
value** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of
  length `N`, provided the **Constant
  value** parameter evaluates to an
  `N`-element row or column vector.
- When you clear this check box, the block outputs a matrix of
  dimension 1-by-`N` or
  `N`-by-1, provided the **Constant
  value** parameter evaluates to an
  `N`-element row or column vector. For
  example, the block outputs a matrix of dimension
  1-by-`N` or
  `N`-by-1.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `VectorParams1D` |
| **Values:** | `'on'` (default) | `'off'` |

### **Sample time** — Sampling interval `inf` (default) | scalar | vector

Specify the interval between times that the Constant block output can change during
simulation, for example, due to tuning the **Constant value**
parameter.

The default value of `inf` indicates that the block
output can never change. This setting speeds simulation and generated
code by avoiding the need to recompute the block output.

See Specify Sample Time (Simulink)
for more information.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'inf'`  (default) | scalar in quotes | vector in quotes |
| **Data Types:** | `char` | `string` |

### Signal Attributes

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Specify the lower value of the output range that the software checks as a finite, real,
double, scalar value.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink)) for
  some blocks.
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes such
  as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation (Simulink) block instead.

#### Dependencies

The software ignores the value of this parameter when **Output data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the minimum values
specified by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[ ]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Specify the upper value of the output range that the software checks as a finite, real,
double, scalar value.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink)) for
  some blocks.
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes such
  as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation (Simulink) block instead.

#### Dependencies

The software ignores the value of this parameter when **Output data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the maximum values
specified by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[ ]'` (default) | scalar in quotes |

### **Output data type** — Output data type `Inherit: Inherit from 'Constant value'` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `int16` | ...

Specify the output data type.

The **Data Type Assistant** helps you
set data attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

You can specify any of these options:

- Inherited data type
- Built-in Simulink data type — For example, specify `single`
  or `uint8`. See Data Types Supported by Simulink (Simulink).
- Fixed-point data type — Use the `fixdt` (Simulink) function. For example,
  specify `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded by
  `Enum:`. For example, specify `Enum:
  myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus` (Simulink) object preceded by
  `Bus:`. For example, specify `Bus:
  myBusObject`.
- Value type *(since R2023b)* — Use the name of the
  `Simulink.ValueType` (Simulink) object preceded by `ValueType:`.
  For example, specify `ValueType: windVelocity`. The
  value type you specify must have `DimensionsMode` set to
  `'Fixed'`.
- Custom data type — Use a MATLAB expression that specifies the type. For example, you can specify a
  `Simulink.NumericType` (Simulink) object whose
  `DataTypeMode` property is set to a value other than
  `'Fixed-point: unspecified scaling'`.

When you specify a
`Simulink.ValueType` or `Simulink.Bus` object as the
data type, the **Output minimum** and **Output
maximum** parameters of the Constant block are ignored.
The software uses the corresponding properties of the
`Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead. For example, suppose a block sets **Output minimum**
to `0`. When the **Output data type** of the block
specifies a `ValueType` object that has `1` as its
minimum, the block uses `1` instead of `0` as its
minimum.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit from 'Constant value''` (default) | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output data type** you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Mode** — Category of data to specify `Inherit` (default) | `Built in` | `Fixed point` | `Enumerated` | `Bus object` | `Value type` | `Expression`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu to the right.
  Select one of these choices:

  - `Inherit from 'Constant value'`
    (default)
  - `Inherit via back propagation`
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu to the right. Select
  one of these choices:

  - `double` (default)
  - `single`
  - `half`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `int64`
  - `uint64`
  - `boolean`
- `Fixed point` — Fixed-point data types.
- `Enumerated` — Enumerated data types. Selecting
  `Enumerated` enables a text box to the right, where you
  can enter a class name.
- `Bus object` — Bus object. Selecting `Bus
  object` enables a text box to the right, where you enter the name
  of a bus object that you want to use to define the structure of the bus. To create
  or change a bus object, click **Edit** to the right of the text
  box.
- `Value type` *(since R2023b)* —
  Value type. Selecting `Value type` enables a text box to
  the right, where you enter the name of a value type that you want to use to define
  the properties of the output signal. To create or change a value type, click
  **Edit** to the right of the text box.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a text box to the
  right, where you can enter the expression.

  Do not specify a bus object as the expression.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, the software inherits the
  data type override setting from its context, that is, from the block,
  `Simulink.Signal` object, or Stateflow® chart that is using the signal.
- When you select `Off`, the software ignores the data
  type override setting of its context and uses the fixed-point data type specified
  for the signal.

For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button, and set the
**Mode** to `Built in`
or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data
type provides greater control over the data types in your model when
you apply data type override. For example, you can use this option
to ensure that data types meet the requirements of downstream blocks
regardless of the data type override setting.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed
data can represent positive and negative values, but unsigned data
represents positive values only.

- `Signed`, specifies the fixed-point
  data as signed.
- `Unsigned`, specifies the fixed-point
  data as unsigned.

For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type (Simulink).

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type (Simulink).

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For
more information, see Specifying a Fixed-Point Data Type (Simulink).

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.
## Libraries

Simulink / Commonly Used Blocks Simulink / Sources DSP System Toolbox / Sources HDL Coder / Commonly Used Blocks HDL Coder / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Tunable Parameters**

You can use a tunable parameter in a Constant block intended
for HDL code generation. For details, see Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

| Architecture | Parameters | Description |
| --- | --- | --- |
| `default`  `Constant` | None | This implementation emits the value of the Constant block. |
| `Logic Value` | None | By default, this implementation emits the character `'Z'` for each bit in the signal. For example, for a 4-bit signal, the implementation would emit `'ZZZZ'`. |
| `{'Value', 'Z'}` | If the signal is in a high-impedance state, use this parameter value. This implementation emits the character `'Z'` for each bit in the signal. For example, for a 4-bit signal, the implementation would emit `'ZZZZ'`. |
| `{'Value', 'X'}` | If the signal is in an unknown state, use this parameter value. This implementation emits the character `'X'` for each bit in the signal. For example, for a 4-bit signal, the implementation would emit `'XXXX'`. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

- The `Logic Value` implementation does not
  support the `double` data type. If you specify this
  implementation for a constant value of type
  `double`, a code generation error
  occurs.
- Delay balancing does not support a Constant block
  that has **Sample time** set to
  `inf` when the infinite sample time propagates
  to the device under test (DUT) output. If there is an infinite
  sample rate error during HDL code generation, set **Sample
  time** to `-1`.

**`Simulink.ValueType` Object Support**

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type (Simulink).

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023b: Set **Output data type** to a `Simulink.ValueType` object

The **Output data type** parameter supports `Simulink.ValueType` (Simulink) objects that have fixed dimensions.

When you specify a value type as the data type of a Constant block, the
value type overrides the minimum and maximum specified by the block and the data type of the
constant value. The value type validates the dimensions, complexity, and unit of the
constant value. When these properties do not match, the software issues a warning or
error.

For example, suppose a Constant block has:

- **Constant value** set to a `Simulink.Parameter`
  object with a unit of `ft/s`
- **Output data type** set to a
  `Simulink.ValueType` object with a unit of
  `m/s`

During model compilation, the software issues a warning about the mismatched
units. The Constant block uses `ft/s` as the unit.

For another example, suppose a Constant block has:

- **Constant value** set to `[2 3]`
- **Output data type** set to a
  `Simulink.ValueType` object with dimensions of
  `1`

During model compilation, the software issues an error about the mismatched
dimensions. Mismatched complexity also results in an error.

The Constant block does not use the description of the value type.

For more information about value types, see Specify Common Set of Signal Properties as Value Type (Simulink).

## Description

Constant value

The Constant block generates a real or complex constant value signal. Use
this block to provide a constant signal input. The block generates scalar, vector, or
matrix output, depending on:

- The dimensionality of the **Constant value** parameter
- The setting of the **Interpret vector parameters as 1-D**
  parameter

The output of the block has the same dimensions and elements as the **Constant
value** parameter. If you specify for this parameter a vector that you want
the block to interpret as a vector, select the **Interpret vector parameters as
1-D** check box. Otherwise, if you specify a vector for the
**Constant value** parameter, the block treats that vector as a
matrix.

**Tip**

To output a constant enumerated value, consider using the Enumerated Constant (Simulink) block instead.
The Constant block provides block parameters that do not apply to
enumerated types, such as **Output minimum** and **Output
maximum**.

### Using Bus Objects as the Output Data Type

The Constant block supports nonvirtual buses as the output data type. Using
a bus object as the output data type can help simplify your model. If you use a bus
object as the output data type, set the **Constant value** to
`0` or to a MATLAB® structure that matches the bus object.

### Using Structures for the Constant Value of a Bus

The structure you specify must contain a value for every element of the bus
represented by the bus object. The block output is a nonvirtual bus signal.

You can use the `Simulink.Bus.createMATLABStruct` (Simulink)
to create a full structure that corresponds to a bus.

You can use `Simulink.Bus.createObject` (Simulink) to
create a bus object from a MATLAB structure.

If the signal elements in the output bus use numeric data types other than
`double`, you can specify the structure fields by using typed
expressions such as `uint16(37)` or untyped expressions such as
`37`. To control the field data types, you can use the bus
object as the data type of a `Simulink.Parameter`
object. To decide whether to use typed or untyped expressions, see Control Data Types of Initial Condition Structure Fields (Simulink).

### Setting Configuration Parameters to Support Using a Bus Object Data Type

To enable the use of a bus object as an output data type, before you start a simulation,
set **Configuration Parameters** > **Diagnostics** > **Data Validity** > **Advanced parameters** > **Underspecified initialization detection** to `Simplified`. For more information, see
Underspecified initialization detection (Simulink).
