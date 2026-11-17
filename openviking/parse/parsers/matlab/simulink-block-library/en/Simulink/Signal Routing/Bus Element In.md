---
type: simulink-block
title: 'In Bus Element'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'inbuselement'
documentation_source_path: 'slref/inbuselement.html'
language: en
---

# In Bus Element

## Ports

### Output

### **Port\_1** — Selected input from external port scalar | vector | matrix | array | bus

Select a bus, signal, or message from the corresponding external input
port of the parent subsystem or model.

While you can select bus elements, you cannot select elements of
arrays of buses.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit the element associated with an
In Bus Element
block, in the Simulink® Editor, edit the block label.

To edit port, signal, execution, and message
attributes, use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of input port `InBus` (default) | port name

Specify a port name that is not already in use by another block or
port within the system. The name appears on the parent
Subsystem or Model block.

To change the port name from the Simulink Editor, edit the first text field of the block
label.

Default In Bus Element block with InBus highlighted in block label

Multiple blocks can access the same port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `"InBus"` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

### **Element** — Optional bus element specification `signal1` (default) | element path

When the port receives a bus from the parent system, optionally
specify an element to select from the bus.

To specify the element that the block selects, in the Simulink Editor, edit the second text field of the block
label.

In Bus Element block with signal1 highlighted in block label

How you specify the element depends on where the element is in the bus
hierarchy.

- For an element at the top level of the input bus, specify the
  element name, for example, `constant`.
- For an element in a nested bus, specify the name of the nested
  bus, intermediary nested buses, and the leaf signal separated by
  dots, for example, `sinusoidal.sine`. This
  element path does not include the top-level bus.

Multiple blocks can access the same element.

To select the top-level signal, message, or bus, delete the text from
the second text field of the block label.

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
In Bus Element
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

### **Data mode** — Data mode of input element `inherit` (default) | `signal` | `message`

Specify the data mode of the input element.

- `inherit` — Input element inherits its data
  mode.
- `signal`  — Input element must be a signal or a bus
  that contains signals.
- `message` — Input element must be a message or a bus
  that contains messages.

When you choose `message` as the data mode of a message
or bus, an envelope button appears next to the message or bus. Use the envelope button
to specify custom queue properties.

#### Tips

To specify different custom queue properties for each message in a bus, set the
**Data mode** parameter for each message instead of the
bus.

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

**Example:** `set_param("mymodel/InBus",DataMode="signal")`

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

### **Events** — Option to trigger model partition based on flow of data into port cell array of event trigger objects

*Since R2022b*

The **Events** parameter stores the event triggers
associated with the port. *Event triggers* create
schedule events based on the runtime activity at a particular location
in the model. The schedule for the model specifies the partitions that
execute in response to the schedule event, as well as the priority of
execution. To configure the schedule for your model, use the Schedule Editor.

The table summarizes the event triggers you can configure on
root-level input ports. Each event trigger maps an *input
event* related to the flow of data into the port to the
name of the schedule event to trigger. You can configure an input port
with one event trigger for each input event.

| Input Event | Input Event Description | Event Trigger Object |
| --- | --- | --- |
| Input write | An *input write* event occurs each time the input port value updates. | `simulink.event.InputWrite` |
| Input write timeout | An *input write timeout* event occurs each time the input port value does not update within a specified amount of time. | `simulink.event.InputWriteTimeout` |
| Input write lost | An *input write lost* event occurs each time a new input port value overwrites unprocessed data. | `simulink.event.InputWriteLost` |

#### Event Triggers on Bus Ports

When you configure event triggers on a bus port, determine where
to specify the event triggers based on the virtuality of the
bus.

- Virtual bus — Specify event triggers on leaf elements of
  the bus. Event triggers are not supported on the virtual bus
  itself.
- Nonvirtual bus — Specify event triggers on the bus. Event
  triggers are not supported on elements of nonvirtual
  buses.

In Bus Element blocks must select each element that
has one or more event triggers.

#### Dependencies

To enable this parameter:

- The port must be a root-level input port in a rate-based
  model.
- If the port loads a nonvirtual bus, in the hierarchical
  tree, select the bus. Event triggers are not supported on
  elements of a nonvirtual bus.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param`
function. Specify the element as the model
name,
a forward slash, and the port name or bus element path. For a bus
element port, the bus element path provides the hierarchy from the
top-level bus to the target element, separating each name in the
hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `EventTriggers` |
| **Values:** | `[]` (default) | `1`-by-`1` cell array | `2`-by-`1` cell array | `3`-by-`1` cell array |

**Example:** `set_param("mymodel/InBusNonvirtual",EventTriggers={inputWrite,writeTimeout,writeLost})`
specifies event triggers for the nonvirtual bus named
`InBusNonvirtual`.

**Example:** `set_param("mymodel/InBus.signal1",EventTriggers={inputWrite,writeTimeout,writeLost})`
specifies event triggers for a leaf element named
`signal1` of the virtual bus named
`InBus`.

### Queue Attributes

Queue attributes are visible only when the block is at the top level of a model and you
set the **Data
mode** parameter to `message`.

To specify queue attributes, next to the name of a bus or message, click Use default queue attributes.

Pointer paused on Use default queue attributes button next to bus name

### **Use default queue attributes** — Default or custom queue specifications on (default) | off

Use this parameter to select between default or custom queue
specifications.

To use the default queue properties, leave the parameter selected. In this case,
for each message bus element, a LIFO overwriting queue of capacity 1 is automatically
inserted.

To use custom specifications, clear the parameter and configure the queue
properties. Queue attributes are applicable if there is no storage block placed
outside a component.

For more information, see Specify Queue Properties for Message Interface.

#### Dependencies

To enable this parameter for an element, set the **Data
mode** of the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueUseDefaultAttributes` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueUseDefaultAttributes="off")`

### **Queue capacity** — Message storage capacity 1 (default) | scalar

Specify the number of messages elements the queue can store.

#### Dependencies

To enable this parameter for an element, set the **Data
mode** of the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueCapacity` |
| **Values:** | `"1"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueCapacity="10")`

### **Queue type** — Choose FIFO or LIFO queue `LIFO` (default) | `FIFO`

Choose one of these queue types:

- `FIFO` — First-in-first-out
- `LIFO` — Last-in-first-out

#### Dependencies

To enable this parameter for an element, set the **Data mode** of
the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueType` |
| **Values:** | `"LIFO"` (default) | `"FIFO"` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueType="FIFO")`

### **Queue overwriting** — Queue message overwriting policy on (default) | off

Select this parameter to choose between two queue overwriting policies.

- If you select the parameter, an incoming message element overwrites the oldest
  message if the queue is full.
- If you clear the parameter, the block does not accept new messages if the
  queue is full.

#### Dependencies

To enable this parameter for an element, set the **Data
mode** of the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueOverwriting` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueOverwriting="off")`

## Libraries

Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Ports & Subsystems HDL Coder / Sources

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

This block can be used to simplify subsystem bus interfaces when you use the block in
subsystems that generate HDL code, but it is not included in the hardware
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

### R2024b: Propagate element names as signal labels

You can now propagate element names from In Bus Element blocks. For
example, for an In Bus Element block labeled
`InBus.nonconstant.chirp`, the propagated name is
`chirp`.

For more information, see Signal Label Propagation.

### R2024a: Select new options when dragging block to new location

When you press **Ctrl** and drag an In Bus Element
block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — Add an element to the
  port.
- **Duplicate** — Create a duplicate In Bus
  Element block.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — Create a duplicate
  In Bus Element block.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `In Bus
  Element`, and select the block from the menu.
- Copy and paste an In Bus Element block.

In previous releases, these actions create a port, add an element to a port, or
duplicate a block.

### R2023b: Specify elements without bus objects or additional blocks at subsystem interfaces

At both subsystem and model interfaces, you can specify the elements of an input
bus without In Bus Element blocks to represent each element or a
`Simulink.Bus` object to define the bus hierarchy. Previously,
only In Bus Element blocks at model interfaces supported this
functionality.

To add the elements, click the Add element button arrow. Then, select **Add element
without block**.

### R2023a: Property Inspector supports In Bus Element blocks

The Property
Inspector supports In Bus Element and Out Bus
Element blocks.

### R2023a: Diagnostic messages link to related In Bus Element blocks

Warning and error messages for In Bus Element and Out Bus
Element blocks now link to the corresponding block in the block diagram,
helping you quickly find the source of the warning or error. In previous releases,
warning and error messages refer to a hidden block and do not provide a link.

## Description

Select input from external port

The In Bus Element block selects input from an external port that
receives a bus, signal, or message.

When the port receives a bus, the In Bus Element block combines the
functionality of an Inport block and a Bus Selector block. To
select multiple elements from the bus, use multiple In Bus Element blocks. All
In Bus Element blocks that correspond with the same port share a dialog
box.

For interfaces that include buses composed of many bus elements, In Bus
Element blocks:

- Reduce signal line complexity and clutter in a block diagram.
- Allow you to more easily make incremental changes to the interface.
- Allow access to a bus element closer to the point of usage, avoiding the use of a
  Bus Selector and Goto block configuration.

To convert an interface to use In Bus Element blocks, see Simplify Subsystem and Model Interfaces with Bus Element Ports.

The In Bus Element block does not support mixing message and signal
elements as outputs.
