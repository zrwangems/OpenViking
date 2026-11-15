---
type: simulink-block
title: 'Signal Specification'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'signalspecification'
---

# Signal Specification

Specify desired dimensions, sample time, data type, numeric type, and other attributes of signal

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Signal Specification block allows you to specify the attributes of the
signal connected to its input and output ports. If the specified attributes conflict with the
attributes specified by the blocks connected to its ports, the software displays an error when
it compiles the model. For example, at the beginning of a simulation, if no conflict exists,
the software eliminates the Signal Specification block from the compiled model.
In other words, the Signal Specification block is a virtual block. It exists
only to specify the attributes of a signal and plays no role in the simulation of the
model.

You can use the Signal Specification block to ensure that the actual
attributes of a signal meet desired attributes. For example, suppose that you and a
colleague are working on different parts of the same model. You use Signal
Specification blocks to connect your part of the model with your
colleague's. If your colleague changes the attributes of a signal without informing you,
the attributes entering the corresponding Signal Specification block do
not match. When you try to simulate the model, you get an error.

You can also use the Signal Specification block to ensure correct propagation
of signal attributes throughout a model. However, if some blocks have unspecified attributes
for the signals they accept or output, the model does not have enough information to propagate
attributes correctly. In these cases, the Signal Specification block can
provide the information the software needs. Using the Signal Specification
block also helps speed up model compilation when blocks are missing signal attributes.

The Signal Specification block supports signal label propagation. For more
information, see Signal Label Propagation.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal whose attributes to check, specified as a scalar, vector, matrix, or N-D
array. The block checks the attributes of the input signal against the
desired attributes you specify in the block dialog box. If the
attributes do not match, the block generates an error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal is the input signal when all attributes of the signal match those
specified in the dialog box. If the attributes do not match, the block
generates an error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Minimum** — Minimum value for range checking `[]` (default) | scalar

Specify the minimum value for the block output as a finite real double scalar
value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the minimum values specified
by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[ ]'` |

### **Maximum** — Maximum value for range checking `[]` (default) | scalar

Specify the maximum value for the block output as a finite real double
scalar value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the maximum values specified
by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[ ]'` |

### **Data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

Specify the desired output data type. If the data type of the input signal
does not match the value you specify, the block generates an error or
warning.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

You can specify any of these options:

- Inherited data type
- Built-in Simulink® data type — For example, specify
  `single` or
  `uint8`. See Data Types Supported by Simulink.
- Fixed-point data type — Use the `fixdt`
  function. For example, specify
  `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded by
  `Enum:`. For example, specify
  `Enum: myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus`
  object preceded by `Bus:`. For example, specify
  `Bus: myBusObject`.
- Simulink image data type — If you have Computer Vision Toolbox™, use the constructor for the `Simulink.ImageType` (Computer Vision Toolbox) object and specify the
  properties to describe the image. By default, the data type uses
  the `Simulink.ImageType(480,640,3)` expression
  that represents the rows, columns, and channels of the image
  respectively.
- Value type — Use the name of the `Simulink.ValueType` object preceded by
  `ValueType:`. For example, specify
  `ValueType: windVelocity`.
- Custom data type — Use a MATLAB® expression that specifies the type. For example,
  you can specify a `Simulink.NumericType` object whose
  `DataTypeMode` property is set to a value
  other than `'Fixed-point: unspecified
  scaling'`.

When you specify a `Simulink.ValueType` or
`Simulink.Bus` object as the data type, some parameters of the
Signal Specification block are ignored. For example, the **Min**,
**Max**, and **Unit** parameters of the
Signal Specification block are ignored. The software uses the corresponding properties of
the `Simulink.ValueType` object or the `Simulink.BusElement` objects
in the `Simulink.Bus` object instead. For example, suppose a block sets
**Unit** to `ft/s`. When the **Data type** of
the block specifies a `ValueType` object that has `m/s` as its
unit, the block uses `m/s` instead of `ft/s`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Value:** `'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Bus: <object name>' | 'ValueType: <object name>' | <data type expression> | Simulink.ImageType(480,640,3)` |
| **Default:** `'Inherit: auto'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the output data
type you specify on the block. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Require nonvirtual bus** — Accept only nonvirtual bus signals `off` (default) | `on`

If you specify a bus object as the data type, use this parameter to
specify whether to accept only nonvirtual bus signals.

- `off` — Specifies that a signal must come from a
  *virtual* bus.
- `on` — Specifies that a signal must come from a
  *nonvirtual* bus.

#### Dependencies

To enable this parameter, the **Data type** block parameter must
resolve to a `Simulink.Bus` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BusOutputAsStruct` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Unit (e.g., m, m/s^2, N\*m)** — Physical unit of the input signal to the block `inherit` (default) | `<Enter unit>`

Specify the physical unit of the input signal to the block. To specify a unit, begin
typing in the text box. As you type, the parameter displays potential matching units.
For a list of supported units, use the `showunitslist` function.

To constrain the unit system, click the link to the right of the parameter:

- If a Unit System Configuration block
  exists in the component, its dialog box opens. Use that dialog box to specify
  allowed and disallowed unit systems for the component.
- If a Unit System Configuration block
  does not exist in the component, the model Configuration Parameters dialog box
  displays. Use that dialog box to specify allowed and disallowed unit systems for
  the model.

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` or `Simulink.Bus` object. The
software uses the units specified by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus` object
instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Unit` |
| **Type:** character vector |
| **Values:** `'inherit'` | `'<Enter unit>'` |
| **Default:** `'inherit'` |

To specify the physical unit of the input signal to the block
without propagation, use `UnitNoProp`.

### **Dimensions (-1 for inherited)** — Dimensions of input and output signals `-1` (default) | `n` | `[m n]`

Specify the dimensions of the input and output signals.

- `-1` — Specifies that signals inherit
  dimensions.
- `n` — Specifies a vector of width
  `n`.
- `[m n]` — Specifies a matrix with
  `m` rows and `n`
  columns.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` object. The
software uses the dimensions specified by the `Simulink.ValueType`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Dimensions` |
| **Type:** character vector |
| **Values:** `'-1'` | `n` | `[m n]` |
| **Default:** `'-1'` |

### **Variable-size signal** — Allow signal to be variable-size, fixed-size, or both `Inherit` (default) | `No` | `Yes`

Specify the signal to be of variable-size, fixed size, or both.

- `Inherit` — Allows variable-size and
  fixed-size signals.
- `No` — Does not allow variable-size
  signals.
- `Yes` — Allows only variable-size
  signals.

When the signal is a variable-size signal, the **Dimensions**
parameter specifies the maximum dimensions of the signal.

#### Dependencies

- When **Data type** specifies a
  `Simulink.Bus` object, the simulation allows variable-size
  signals only with a disabled bus object.
- The software ignores the value of this parameter when **Data
  type** specifies a `Simulink.ValueType` object. The
  software uses the dimensions mode specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VarSizeSig` |
| **Type:** character vector |
| **Values:** `'Inherit'` | `'No'` | `'Yes'` |
| **Default:** `'Inherit'` |

### **Sample time (-1 for inherited)** — Time interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set
this parameter to `-1`. See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** Any valid sample time |
| **Default:** `'-1'` |

### **Signal type** — Complexity of signal `auto` (default) | `real` | `complex`

Specify the complexity of the input and output signals.

- `auto` — Accepts either
  `real` or
  `complex` as the numeric type.
- `real` — Specifies the numeric type as a
  real number.
- `complex` — Specifies the numeric type as
  a complex number.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the complexity specified by
the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SignalType` |
| **Type:** character vector |
| **Values:** `'auto'` | `'real'` | `'complex'` |
| **Default:** `'auto'` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Enumerated` | `Bus object` | `Value type` | `Expression`

Select the category of data to specify. For more information, see Specify Data Types Using Data Type Assistant.

`Inherit`
:   Inheritance rules for data types. Selecting `Inherit` enables
    `auto`.

`Built in`
:   Built-in data types. Selecting `Built in` enables a list of
    possible values:

    - `double` (default)
    - `single`
    - `int8`
    - `uint8`
    - `int16`
    - `uint16`
    - `int32`
    - `uint32`
    - `int64`
    - `uint64`
    - `boolean`

`Fixed point`
:   Fixed-point data types.

`Enumerated`
:   Enumerated data types. Selecting `Enumerated` enables a text
    box to the right, where you can enter a class name.

`Bus object`
:   Bus object. Selecting `Bus object` enables a text box
    to the right, where you enter the name of a bus object that you want to use to
    define the structure of the bus. To create or change a bus object, click
    **Edit** to the right of the text box.

`Value type`
:   Value type. Selecting `Value type` enables a text box
    to the right, where you enter the name of a value type that you want to use to
    define the properties of the signal. To create or change a value type, click
    **Edit** to the right of the text box.

`Expression`
:   Expressions that evaluate to data types. Selecting
    `Expression` enables a text box to the right, where you
    can enter the expression.

    Do not specify a bus object as the expression.

#### Dependencies

To enable this parameter, click the **Show data type assistant**
button .

### **Signedness** — Signed or unsigned `Signed`

Specify whether the fixed-point data is signed or unsigned. Signed data
can represent positive and negative values, but unsigned data represents
positive values only.

- `Signed`, specifies the fixed-point data
  as signed.
- `Unsigned`, specifies the fixed-point
  data as unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has a pass-through implementation.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**`Simulink.ValueType` Object Support**

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
