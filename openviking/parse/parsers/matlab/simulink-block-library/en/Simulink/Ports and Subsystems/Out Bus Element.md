---
type: simulink-block
title: 'Out Bus Element'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Ports and Subsystems'
documentation_page: 'outbuselement'
documentation_source_path: 'slref/outbuselement.html'
language: en
---

# Out Bus Element

## Ports

### Input

### **Port\_1** — Full or partial output for external port scalar | vector | matrix | array | bus

Connect a bus, signal, or message to pass to the corresponding external output
port of the parent subsystem or model.

When multiple Out Bus Element blocks are associated with the same
external port, the input to this block is an element of the bus at the output port.
The second text field in the block label specifies the element name.

When one Out Bus Element block is associated with the external
port, the input to this block is passed directly to the output port or nested in a bus
at the output port. To pass the input of the block to the output port without nesting
it in a bus, delete the text from the second text field in the block label.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit the element associated with an
Out Bus Element
block, in the Simulink® Editor, edit the block label.

To edit port, signal, and execution attributes, use the Property
Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of output port `OutBus` (default) | port name

Specify a port name that is not already in use by another block or
port within the system. The name appears on the parent
Subsystem or Model block.

To change the port name from the Simulink Editor, edit the first text field of the block
label.

Default Out Bus Element block with OutBus highlighted in block label

Multiple blocks can provide output for the same port as long as each
block provides output for a unique element of the port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `"OutBus"` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

### **Element** — Optional bus element specification `signal1` (default) | element path

To create a bus at the output port, specify an element in the second
text field of the block label.

Default Out Bus Element block with signal1 highlighted in block label

How you specify the element depends on where the element is in the bus
hierarchy.

- For an element at the top level of the output bus, specify the
  element name, for example, `constant`.
- For an element in a nested bus, specify the name of the nested
  bus, intermediary nested buses, and the leaf signal separated by
  dots, for example, `sinusoidal.sine`. This
  element path does not include the top-level bus.

Each output element must be unique and must not overlap with other
elements of the port. For example, for a nested bus, use one Out
Bus Element block that corresponds with the nested bus or
multiple Out Bus Element blocks that correspond with the
nested bus elements.

To output a signal, message, or bus without creating a bus, delete the
text from the second text field of the block label.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Element` |
| **Values:** | `"signal1"` (default) | element path in quotes |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Element="constant")`

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Element="sinusoidal.sine")`

### Port Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

*Before R2025a: To specify attributes, such as output name,
pause on the name of the top-level bus, signal, or message. Then, click Specify attributes. Alternatively, when available, click an
attribute summary.*

For information about the port name, see **Port
name**.

### **Port number** — Position of port on parent block `1` (default) | real integer

Specify the order in which the port that corresponds to the block appears on the parent
Subsystem or Model block.

- If you add a block that creates another port, the port number is the next available
  number.
- Deleting all blocks associated with a port deletes the port. Other ports are
  renumbered so that they are sequential and do not skip any numbers.
- Specifying a port number that exceeds the number of ports creates a port for that
  number and for any skipped sequential numbers.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **Values:** | `"1"` (default) | real integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

### **Output name** — Name of output bus, signal, or message in parent subsystem or model no default

*Since R2023a*

Specify the name of the output bus, signal, or message in the parent
subsystem or model. The name appears as a label on the line.

To display propagated labels for individual lines or all lines in a
model, see Display Propagated Signal Labels.

#### Dependencies

- To enable this parameter:

  - The block must be at the top level of a
    model.
  - The element must be the top-level bus, signal,
    or message.
- When you set **Data type** to a
  `Simulink.Bus` object, the software sets
  this parameter to `""`
  (empty).

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutputName` |
| **Values:** | `""` (default) | output name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/OutBus",OutputName="model-output")`

### **Initial output** — Initial output for parent conditionally executed subsystem `[]` (default) | scalar | structure

*Since R2024b*

For conditionally executed subsystems, specify the block output before
the subsystem executes and while the subsystem is disabled. To inherit
the initial output value from the input signal, apply both of these
default settings:

- Set **Initial output** to
  `[]`.
- Set **Output when
  disabled** to
  `held`.

The software attempts to inherit the output value from the input
signal. If the input signal is not a valid source for the initial output
value, the initial output value `[]` is treated as
`double(0)`. For more information, see Conditional Subsystem Initial Output Values.

For information about specifying an initial condition structure, see
Specify Initial Conditions for Bus Elements.

#### Tips

If the conditional subsystem is driving a Merge
block, you do not need to specify an initial condition for the
Out Bus Element block. For more information, see
Underspecified initialization detection.

#### Dependencies

To enable this parameter:

- The block must be at the top level of a conditionally
  executed subsystem or model.
- The element must be the top-level bus, signal, or
  message.

#### Limitations

- This block does not support an initial output of
  `inf` or
  `NaN`.
- When the input is a virtual bus, an **Initial
  output** value of `[]` is
  treated as `double(0)`.
- When the input contains a nonvirtual bus,
  **Initial output** does not support
  nonzero scalar values.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialOutput` |
| **Values:** | `'[]'` (default) | scalar in quotes | structure in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/condss/Output",InitialOutput="3")`

### **Output when disabled** — Output when parent conditionally executed subsystem is disabled `held` (default) | `reset`

*Since R2024b*

Specify what happens to the block output when the parent conditionally
executed subsystem is disabled.

- `held` — The output is held when the
  subsystem is disabled.
- `reset` — The output is reset to the
  value given by **Initial output** when the
  subsystem is disabled.

#### Tips

- If the output of the parent subsystem connects to a Merge block,
  do not set this parameter to
  `reset`.
- For an Out Bus Element block in a
  function-call subsystem, this parameter is meaningful only
  if the Function-Call Subsystem block connects
  to a state in a Stateflow® chart. For more information, see Bind a Function-Call Subsystem to a State (Stateflow).

#### Dependencies

To enable this parameter:

- The block must be at the top level of a conditional
  subsystem with valid enabling and disabling semantics.
  For example, an Out Bus Element block in
  an enabled subsystem supports this parameter, but an
  Out Bus Element block in a triggered
  subsystem does not support this parameter.
- The element must be the top-level bus, signal, or
  message.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputWhenDisabled` |
| **Values:** | `"held"` (default) | `"reset"` |

**Example:** `set_param("mdl/condss/Output",InitialOutput="3",OutputWhenDisabled="reset")`

### Signal Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify attributes, a parenthetical appears next to the name of the corresponding
bus, signal, or message. To display the specified attributes in full, click the attribute
summary.

Pointer paused on attribute summary next to bus name

*Before R2025a: To specify attributes, such as data type, pause on the
name of a bus, signal, or message. Then, click Specify attributes. Alternatively, when available, click an attribute
summary.*

### **Data type** — Data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

The data type of a bus, signal, or message can be inherited, specified directly, or
expressed as a data type object such as a `Simulink.NumericType` object.

You can specify any of these options:

- Inherited data type
- Built-in Simulink data type — For example, specify `single` or
  `uint8`. See Data Types Supported by Simulink.
- Fixed-point data type — Use the `fixdt` function. For example, specify
  `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded by
  `Enum:`. For example, specify `Enum:
  myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus` object preceded by `Bus:`. For example,
  specify `Bus: myBusObject`.
- Value type — Use the name of the `Simulink.ValueType` object preceded by `ValueType:`. For
  example, specify `ValueType: windVelocity`.
- Custom data type — Use a MATLAB expression that specifies the type. For example, you can
  specify a `Simulink.NumericType` object
  whose `DataTypeMode` property is set to a value other
  than `"Fixed-point: unspecified scaling"`.

When you specify a `Simulink.ValueType`
object as the data type, some parameters of the element are ignored. For example, the
**Min**, **Max**, and **Unit** parameters
are ignored. The software uses the corresponding properties of the
`Simulink.ValueType` object. For example, suppose you set
**Unit** to `ft/s` for an element. When the **Data
type** of the element specifies a `ValueType` object that has
`m/s` as its unit, the element uses `m/s` instead of
`ft/s`.

When you specify a `Simulink.Bus` object
as the data type, some parameters of the element are reset to their default values. For
example, the **Min**, **Max**, and **Unit**
parameters are reset. The software uses the corresponding properties of the
`Simulink.BusElement` objects in the `Simulink.Bus` object
instead.

#### Tips

- When you specify a bus using a `Simulink.Bus` object or a
  `Simulink.ValueType` object with a
  `Simulink.Bus` object data type, the Property Inspector
  and block dialog box display the elements defined by the corresponding
  `Simulink.BusElement` objects.
- To create a `Simulink.Bus` object using the Type
  Editor, click Open Type Editor.

#### Dependencies

To specify a `Simulink.Bus` object as the data type of a bus at a bus
element port, an
Out Bus Element
block must represent the bus or an element of the bus.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16)"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"string"` | `"Enum: <class name>"` | `"Bus: <object name>"` | `"ValueType: <object name>"` | data type expression in quotes |

**Example:** `set_param("mymodel/myBus.signal1",OutDataTypeStr="int32")`

### **Data mode** — Data mode of output element `inherit` (default) | `signal` | `message`

Specify the data mode of the output element.

- `inherit` — Output element inherits its data
  mode.
- `signal`  — Output element must be a signal or a bus
  that contains signals.
- `message` — Output element must be a message or a bus
  that contains messages.

#### Dependencies

To enable this parameter, the block must be at the top level of a model.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `DataMode` |
| **Values:** | `"inherit"` (default) | `"signal"` | `"message"` |

**Example:** `set_param("mymodel/OutBus",DataMode="signal")`

### **Bus virtuality** — Virtual or nonvirtual bus `inherit` (default) | `virtual` | `nonvirtual`

Specify whether to inherit the bus virtuality or define the bus as virtual or nonvirtual.
For more information, see Composite Interface Guidelines.

This parameter determines whether the blocks inherit or define the bus virtuality. If the
blocks define the bus virtuality and the virtuality of the input bus does not match, compiling
the model produces an error.

#### Dependencies

To enable this parameter, **Data type** must resolve to a
`Simulink.Bus` object. For example, set **Data type** to
a `Simulink.Bus` object or a `Simulink.ValueType` object that
specifies a `Simulink.Bus` object as its data type.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `BusVirtuality` |
| **Values:** | `"inherit"` (default) | `"virtual"` | `"nonvirtual"` |

**Example:** `set_param("mymodel/myBus.nestedBus",BusVirtuality="nonvirtual")`

### **Dimensions** — Signal dimensions `-1` (default) | integer | `1`-by-`2` vector of integers

Specify the dimensions of a signal.

- `-1` — The signal can have any dimensions.
- `N` — The signal must be a vector of size
  `N`.
- `[R C]` — The signal must be a matrix having `R`
  rows and `C` columns.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `1`. The software uses the
  dimensions specified by the `Simulink.BusElement` objects in the
  `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the dimensions specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `PortDimensions` |
| **Values:** | `"-1"` (default) | integer in quotes | `1`-by-`2` vector of integers in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/myBus.signal1",PortDimensions="[1
3]")`

### **Dimensions mode** — Option to allow only variable-size or fixed-size signals `Inherit` (default) | `Fixed` | `Variable`

Specify the type of signals allowed.

- `Inherit` — Allow variable-size and fixed-size
  signals.
- `Variable` — Allow only variable-size signals.
- `Fixed` — Allow only fixed-size signals. Do not allow
  variable-size signals.

When the signal is variable-sized, the **Dimensions** parameter specifies
the maximum dimensions of the signal.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `Inherit`. The
  software uses the dimensions modes specified by the `Simulink.BusElement`
  objects in the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the dimensions mode specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `VarSizeSig` |
| **Values:** | `"Inherit"` (default) | `"No"` | `"Yes"` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",VarSizeSig="No")`

### **Unit** — Physical unit `inherit` (default) | unit supported by Simulink software

Specify the physical unit of the signal. For a list of supported units, in the MATLAB Command Window, enter `showunitslist`.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `inherit`. The
  software uses the units specified by the `Simulink.BusElement` objects in
  the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the unit specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `Unit` |
| **Values:** | `"inherit"` (default) | unit supported by Simulink software in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/myBus.signal1",Unit="m/s")`

### **Complexity** — Numeric type `auto` (default) | `real` | `complex`

Specify the numeric type of the signal. To choose the numeric type of the signal, select
`auto`. Otherwise, choose a real or complex signal type.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `auto`. The
  software uses the complexity specified by the `Simulink.BusElement`
  objects in the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the complexity specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `SignalType` |
| **Values:** | `"auto"` (default) | `"real"` | `"complex"` |

**Example:** `set_param("mymodel/myBus.signal1",SignalType="real")`

### **Minimum** — Minimum value `[]` (default) | scalar

Lower value of the range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes such as SIL or
  external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `[]`. The software uses the
  minimum values specified by the `Simulink.BusElement` objects in the
  `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the minimum value specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `"[]"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",OutMin="0")`

### **Maximum** — Maximum value `[]` (default) | scalar

Upper value of the range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes such as SIL or
  external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `[]`. The software uses the
  maximum values specified by the `Simulink.BusElement` objects in the
  `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the maximum value specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `"[]"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",OutMax="2")`

### **Description** — Description of bus, signal, or message no default

Use the description to document information about the bus, signal, or message, such as
where it is used. This information does not affect processing.

#### Dependencies

- When **Data type** specifies a
  `Simulink.Bus` object, the software sets this parameter
  to `""` (empty). The software uses the description
  specified by the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the description specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `Description` |
| **Values:** | `""` (default) | description in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",Description="This signal is
used by...")`

### Execution Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify attributes, a parenthetical appears next to the name of the corresponding
bus, signal, or message. To display the specified attributes, click
Specify execution attributes.

Pointer paused on Specify execution attributes button next to bus name

*Before R2025a: To specify execution attributes, pause on the name
of a bus, signal, or message. Then, click Specify execution attributes.*

### **Sample time** — Sample time `-1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`-1`). For more options, see Types of Sample Time.

By default, the signal inherits its sample time.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",SampleTime="0.01")`

## Libraries

Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Ports & Subsystems HDL Coder / Sinks

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

This block can be used to simplify subsystem bus interfaces when you use the block
in subsystems that generate HDL code, but it is not included in the hardware
implementation.

To learn more about using buses for HDL code generation, see Buses (HDL Coder) and Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder).

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

**Data Type Support**

This block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2017a**

### R2025a: Specify port, signal, and execution attributes more easily

You can now specify port, signal, and execution attributes more easily.

- To toggle the display of port, signal, and execution attributes, click Show attributes or Hide attributes. Port, signal, and execution attributes
  now appear on tabs. The Show attributes or Hide attributes button replaces the buttons that appear
  when you pause on a bus, signal, or message name in a previous
  release.
- When you specify execution attributes, a parenthetical now appears next to
  the name of the corresponding bus, signal, or message. To display the
  specified attributes, click Specify execution attributes.
- To edit the port name, double-click the name of the top-level bus, signal,
  or message. Alternatively, on the **Port** tab, specify
  **Port name**.
- To change block colors, click Set color of blocks associated with selected elements and select a standard color or specify a
  custom color.
- To create a `Simulink.Bus` object using the Type
  Editor, on the **Signal** tab, click Open Type Editor.
- **Dims mode** is now named **Dimensions
  mode**.

### R2024b: Specify initial conditions

In conditionally executed subsystems and models, Out Bus Element
blocks now support initial conditions on the top-level element. For nonbus signals,
set **Initial output** to a value with the same dimensions and
complexity as the signal. For buses, set **Initial output** to a
MATLAB structure with fields that have the same names and hierarchy as the
elements of the bus. To specify what happens to the block output when the subsystem
is disabled, use the **Output when disabled** block
parameter.

### R2024a: Specify elements without bus objects or additional blocks

When a subsystem or model has an output bus element port, you do not need to
specify a `Simulink.Bus` object or add Out Bus Element
blocks to:

- Add elements to the output port.
- Specify attributes of the elements at the output port.

To add an element to the port, select the element that you want to contain the new
element. Then, click Add element and select one of these options:

- **Add element with block** — Add an element to the
  port and an Out Bus Element block that represents the
  element.
- **Add element without block** — Add an element to
  the port without adding an Out Bus Element block that
  represents the element.

To programmatically add elements to the output bus without adding blocks to the
block diagram, use the `Simulink.Bus.addElementToPort` function.

### R2024a: Select new options when dragging block to new location

When you press **Ctrl** and drag an Out Bus Element
block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — When the dragged block represents
  an element of the port and not the full port, add an element to the
  port.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — When the dragged block
  represents an element of the port and not the full port, add an element
  to the port. Otherwise, create a port.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `Out Bus
  Element`, and select the block from the menu.
- Copy and paste an Out Bus Element block.

In previous releases, these actions create a port or add an element to a
port.

### R2023a: Specify name of port output

For an Out Bus Element block at the top level of a model, use the
**Output
name** block parameter to specify the name of the top-level bus,
signal, or message that appears in a parent subsystem or model.

### R2023a: Property Inspector supports Out Bus Element blocks

The Property
Inspector supports In Bus Element and Out Bus
Element blocks.

### R2023a: Diagnostic messages link to related Out Bus Element blocks

Warning and error messages for In Bus Element and Out Bus
Element blocks now link to the corresponding block in the block diagram,
helping you quickly find the source of the warning or error. In previous releases,
warning and error messages refer to a hidden block and do not provide a link.

## Description

Specify output of external port

The Out Bus Element block provides a bus, signal, or message as the
output of an external port.

To group multiple buses, signals, or messages into an output bus, use multiple Out
Bus Element blocks that correspond with the same port. The Out Bus
Element blocks combine the functionality of a Bus Creator block and
an Outport block. All Out Bus Element blocks that correspond
with the same port share a dialog box.

For interfaces that include buses composed of many bus elements, Out Bus
Element blocks:

- Reduce signal line complexity and clutter in a block diagram.
- Allow you to more easily make incremental changes to the interface.
- Allow access to a bus element closer to the point of usage, avoiding the use of a
  Bus Creator and From block configuration.

To convert an interface to use Out Bus Element blocks, see Simplify Subsystem and Model Interfaces with Bus Element Ports.

The Out Bus Element block does not support mixing message and signal
elements as inputs.

When you save output data to the workspace or a file, bus data defined by groups of
root-level Out Bus Element blocks are logged along with root-level
Outport block data.
