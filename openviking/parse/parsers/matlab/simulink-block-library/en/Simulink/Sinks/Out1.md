---
type: simulink-block
title: 'Outport'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'outport'
documentation_source_path: 'slref/outport.html'
language: en
---

# Outport

## Ports
```yaml
ports:
- name: Port_1
  summary: Outport signal scalar | vector
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus | image | datetime
```

### Input

### **Port\_1** — Outport signal scalar | vector

Input signal that flows through the outport to an external subsystem or model.

An Outport block can accept fixed-point and enumerated data types when
the block is not a root-level output port. The complexity and data type
of the block output are the same as its input.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
## Parameters
```yaml
parameters:
- name: Port number
  summary: Position of port on parent block 1 (default) | real integer
  group: Main
  block_parameter: Port
  values: '"1" (default) | real integer in quotes'
- name: Signal name
  summary: Signal name ' ' (default) | character vector
  group: Main
  block_parameter: SignalName
  type: character vector
  values: character vector
  default: ''' '''
- name: Icon display
  summary: Icon display Port number (default) | Signal name | Port number and signal name
  group: Main
  block_parameter: IconDisplay
  type: character vector
  values: '''Signal name'' | ''Port number'' | ''Port number and signal name'''
  default: '''Port number'''
- name: Specify output when source is unconnected
  summary: Specify unconnected output value off (default) | on
  group: Main
  block_parameter: OutputWhenUnconnected
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Constant value
  summary: Output value when the block is not connected 0 (default) | scalar | vector
  group: Main
  block_parameter: OutputWhenUnconnectedValue
  type: character vector
  values: scalar | vector
  default: '''0'''
- name: Interpret vector parameters as 1-D
  summary: Treat vectors as 1-D on (default) | off
  group: Main
  block_parameter: VectorParamsAs1DForOutWhenUnconnected
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Ensure outport is virtual
  summary: Ensure that outport is virtual off (default) | on
  group: Main
  block_parameter: EnsureOutportIsVirtual
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Output when disabled
  summary: Output when disabled held (default) | reset
  group: Main
  block_parameter: OutputWhenDisabled
  type: character vector
  values: '''held'' | ''reset'''
  default: '''held'''
- name: Initial output
  summary: Initial output for conditionally executed subsystems [] (default) | scalar | structure
  group: Main
  block_parameter: InitialOutput
  type: character vector
  values: '''[]'' | scalar | structure'
  default: '''[]'''
- name: Minimum
  summary: Minimum output value [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMin
  type: character vector
  values: '''[ ]''| scalar'
  default: '''[ ]'''
- name: Maximum
  summary: Maximum output value [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMax
  type: character vector
  values: '''[ ]''| scalar'
  default: '''[ ]'''
- name: Data type
  summary: 'Output data type Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16 | ...'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32''
    | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''string''
    | ''Enum: <class name>'' | ''Bus: <object name>'' | ''ValueType: <object name>'' | ''<data type expression>'' | Simulink.ImageType(480,640,3)'
  default: '''Inherit: auto'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Option to prevent fixed-point tools from overriding data types off (default) | on
  group: Signal Attributes
  block_parameter: LockScale
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output as nonvirtual bus in parent model
  summary: Output as nonvirtual bus in parent model off (default) | on
  group: Signal Attributes
  block_parameter: BusOutputAsStruct
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Unit (e.g., m, m/s^2, N\*m)
  summary: Physical unit of the input signal to the block inherit (default) | <Enter unit>
  group: Signal Attributes
  block_parameter: Unit
  type: character vector
  values: '''inherit'' | ''<Enter unit>'''
  default: '''inherit'''
- name: Port dimensions (-1 for inherited)
  summary: Port dimensions -1 (default) | integer | [integer, integer]
  group: Signal Attributes
  block_parameter: PortDimensions
  type: character vector
  values: '''-1'' | integer | [integer, integer]'
  default: '''-1'''
- name: Variable-size signal
  summary: Allow variable-size signals Inherit (default) | No | Yes
  group: Signal Attributes
  block_parameter: VarSizeSig
  type: character vector
  values: '''Inherit'' | ''No'' | ''Yes'''
  default: '''Inherit'''
- name: Signal type
  summary: Output signal type auto (default) | real | complex
  group: Signal Attributes
  block_parameter: SignalType
  type: character vector
  values: '''auto'' | ''real'' | ''complex'''
  default: '''auto'''
- name: Sample time (-1 for inherited)
  summary: Option to specify sample time -1 (default) | scalar
  group: Execution
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''-1'''
```

### Main

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

### **Signal name** — Signal name `' '` (default) | character vector

Specify the name of the corresponding signal data in the generated
code. Use this parameter to specify a name for the signal data when you
apply a storage class to a root-level Outport
block.

#### Dependencies

To enable this parameter, the block must be at the top level of a
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalName` |
| **Type:** character vector |
| **Values:** character vector |
| **Default:** `' '` |

### **Icon display** — Icon display `Port number` (default) | `Signal name` | `Port number and signal name`

Specify the information displayed on the block icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **Default:** `'Port number'` |

### **Specify output when source is unconnected** — Specify unconnected output value `off` (default) | `on`

Specify a constant output value for when source is not
connected.

#### Dependencies

Available for unconnected Outport blocks inside a Variant
Subsystem block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWhenUnconnected` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Constant value** — Output value when the block is not connected `0` (default) | scalar | vector

Specify a constant output value for when source is not
connected.

#### Dependencies

Available in a Variant Subsystem block for an unconnected
Outport block with **Specify output when
source is unconnected** selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWhenUnconnectedValue` |
| **Type:** character vector |
| **Values:** `scalar` | `vector` |
| **Default:** `'0'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to create a vector of length `N` at the output if
the **Constant value** parameter evaluates
to an `N`-element row or column vector.

#### Dependencies

Available in a Variant Subsystem block on an unconnected
Outport block when you select the
**Specify output when source is unconnected**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParamsAs1DForOutWhenUnconnected` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Ensure outport is virtual** — Ensure that outport is virtual `off` (default) | `on`

Clear this parameter to allow Simulink® to use a signal buffer on output port. This buffer, which
is the equivalent of a Signal Conversion block
but is not displayed on the canvas, ensures consistent initialization of
the Outport block signal.

If you select this parameter, Simulink tries to remove the signal buffer.

- If the signal buffer is not needed, Simulink removes the buffer.
- If the signal buffer is needed for data consistency and
  proper execution, Simulink displays an error indicating the buffer could
  not be removed.

Allow partial writes through Assignment
blocks.

For more information regarding this parameter, including examples with conditional
writes and partial writes, see Ensure Output Port Is Virtual.

**Note**

The block is always virtual if it is at the root-level of a model
and is driven by another Outport block inside an
Initialize Function
block, a Reset Function
block, a Reinitialize Function block or a Terminate Function
block.

#### Dependencies

This parameter applies to these blocks and this configuration parameter setting:

- Conditional subsystem
- Assignment
- Merge
- Model with root Outport block
- The **Underspecified
  initialization detection** configuration
  parameter must be set to
  `Simplified`. This block
  parameter is not available when the
  `Classic` option of the configuration
  parameter is selected. For more information about how to
  switch from classic to simplified initialization mode, see
  Convert from Classic to Simplified Initialization Mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnsureOutportIsVirtual` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Output when disabled** — Output when disabled `held` (default) | `reset`

Specify what happens to the block output when the subsystem is
disabled. Select `held` to indicate that the
output is held when the subsystem is disabled. Select
`reset` to indicate that the output is
reset to the value given by **Initial output** when the
subsystem is disabled.

#### Dependencies

Available when an Outport block is inside a conditional subsystem with
valid enabling and disabling semantics. For example, the parameter
is available for an Outport block inside an
Enabled Subsystem block and not for an
Outport block inside a Triggered
Subsystem block.

If an Outport block is inside a Function-Call Subsystem
block, this parameter is only meaningful if the Function-Call
Subsystem block is connected to a state in a Stateflow® chart. For more information, see Bind a Function-Call Subsystem to a State (Stateflow).

When connecting the output of a conditional subsystem to a Merge block, set
this parameter to `held`. Setting it to
`reset` returns an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWhenDisabled` |
| **Type:** character vector |
| **Values:** `'held' | 'reset'` |
| **Default:** `'held'` |

### **Initial output** — Initial output for conditionally executed subsystems `[]` (default) | scalar | structure

For conditionally executed subsystems, specify the block output before the subsystem
executes and while it is disabled. To inherit the initial output value
from the input signal, apply both of these default settings:

- Set **Initial output** parameter to
  `[]`.
- Set **Output when
  disabled** parameter to
  `held`.

Simulink attempts to inherit the output value from the input
signal. However, if the input signal is not a valid source for the
initial output value, the initial output value `[]` is
treated as `double(0)`. For more information, see Conditional Subsystem Initial Output Values.

For information about specifying an initial condition structure, see
Specify Initial Conditions for Bus Elements.

#### Tips

If the conditional subsystem is driving a Merge
block, you do not need to specify an Initial Condition (IC) for the
Outport block. For more information, see Underspecified initialization detection.

#### Dependencies

Available when an Outport block is inside a conditional
subsystem.

#### Limitations

- This block does not allow an initial output of
  `inf` or
  `NaN`.
- When the input is a virtual bus, an **Initial
  output** value `[]` is
  treated as `double(0)`.
- When the input contains a nonvirtual bus,
  **Initial output** does not support
  nonzero scalar values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector |
| **Values:** `'[]'` | scalar | structure |
| **Default:** `'[]'` |

### Signal Attributes

### **Minimum** — Minimum output value `[]` (default) | scalar

Lower value of the output range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` or `Simulink.Bus` object. The
software uses the minimum values specified by the `Simulink.ValueType` object
or the `Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Maximum** — Maximum output value `[]` (default) | scalar

Upper value of the output range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` or `Simulink.Bus` object. The
software uses the maximum values specified by the `Simulink.ValueType` object
or the `Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

Specify the output data type of the external input. The type can be
inherited, specified directly, or expressed as a data type object such
as a `Simulink.NumericType` object.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

You can specify any of these options:

- Inherited data type
- Built-in Simulink data type — For example, specify
  `single` or
  `uint8`. See Data Types Supported by Simulink.
- Fixed-point data type — Use the `fixdt`
  function. For example, specify
  `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded
  by `Enum:`. For example, specify
  `Enum: myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus` object preceded by
  `Bus:`. For example, specify
  `Bus: myBusObject`.
- Simulink image data type — If you have Computer Vision Toolbox™, use the constructor for the `Simulink.ImageType` (Computer Vision Toolbox) object and specify the
  properties to describe the image. By default, the data type
  uses the `Simulink.ImageType(480,640,3)`
  expression that represents the rows, columns, and channels
  of the image respectively.
- Value type — Use the name of the `Simulink.ValueType` object preceded by
  `ValueType:`. For example, specify
  `ValueType:
  windVelocity`.
- Custom data type — Use a MATLAB expression that specifies the type. For
  example, you can specify a `Simulink.NumericType` object whose
  `DataTypeMode` property is set to a
  value other than `'Fixed-point: unspecified
  scaling'`.

When you specify a `Simulink.ValueType` or
`Simulink.Bus` object as the data type, some parameters of the
Outport block are ignored. For example, the **Min**,
**Max**, and **Unit** parameters of the
Outport block are ignored. The software uses the corresponding properties of
the `Simulink.ValueType` object or the `Simulink.BusElement` objects
in the `Simulink.Bus` object instead. For example, suppose a block sets
**Unit** to `ft/s`. When the **Data type** of
the block specifies a `ValueType` object that has `m/s` as its
unit, the block uses `m/s` instead of `ft/s`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` | `Simulink.ImageType(480,640,3)` |
| **Default**: `'Inherit: auto'` |

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

### **Output as nonvirtual bus in parent model** — Output as nonvirtual bus in parent model `off` (default) | `on`

Specify the outport bus to be nonvirtual in the parent model. Select this
parameter if you want the bus emerging in the parent model to be nonvirtual. The bus
that is input to the port can be virtual or nonvirtual, regardless of the setting of
**Output as nonvirtual bus in parent model**.

Clear this parameter if you want the bus emerging in the parent model to be
virtual.

#### Tips

- In a nonvirtual bus, all signals must have the same sample time, even if the
  elements of the associated bus object specify inherited sample times. Any
  operation that would result in a nonvirtual bus that violates this requirement
  generates an error. For details, see Modify Sample Times for Nonvirtual Buses.

  To use a multirate signal for a virtual bus, in the root-level
  Outport block, set the **Sample time**
  parameter to inherited (`-1`).
- For the top model in a model reference hierarchy, code generation creates a
  C structure to represent the bus output of this block.
- For referenced models, select this option to create a C structure.
  Otherwise, code generation creates an argument for each leaf element of the
  bus.

#### Dependencies

To enable this parameter, **Data type** must resolve to a
`Simulink.Bus` object. For example, set **Data
type** to a `Simulink.Bus` object or a
`Simulink.ValueType` object that specifies a
`Simulink.Bus` object as its data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BusOutputAsStruct` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

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

### **Port dimensions (-1 for inherited)** — Port dimensions `-1` (default) | integer | [integer, integer]

Specify the dimensions that a signal must have to be connected to this Outport
block.

|  |  |
| --- | --- |
| `-1` | A signal of any dimensions can be connected to this port. |
| `N` | The signal connected to this port must be a vector of size `N`. |
| `[R C]` | The signal connected to this port must be a matrix having `R` rows and `C` columns. |

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` object. The
software uses the dimensions specified by the `Simulink.ValueType`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PortDimensions` |
| **Type**: character vector |
| **Values**: `'-1'` | integer | [integer, integer] |
| **Default**: `'-1'` |

### **Variable-size signal** — Allow variable-size signals `Inherit` (default) | `No` | `Yes`

Specify the type of signals allowed at the output of this port. To allow
variable-size and fixed-size signals, select `Inherit`. To
allow only variable-size signals, select `Yes`. To allow only
fixed-size signals, select `No`.

When the signal at this port is a variable-size signal, the **Port
dimensions** parameter specifies the maximum dimensions of the
signal.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` object. The
software uses the dimensions mode specified by the
`Simulink.ValueType` object instead.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `VarSizeSig` |
| **Type:** character vector |
| **Value:** `'Inherit'` | `'No'` | `'Yes'` |
| **Default:** `'Inherit'` |

### **Signal type** — Output signal type `auto` (default) | `real` | `complex`

Specify the numeric type of the signal output. To choose the numeric type of the
signal that is connected to its input, select `auto`.
Otherwise, choose a real or complex signal type.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the complexity specified
by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalType` |
| **Type:** character vector |
| **Values:** `'auto'` | `'real'` | `'complex'` |
| **Default:** `'auto'` |

### Execution

### **Sample time (-1 for inherited)** — Option to specify sample time `-1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`-1`). For more options, see Types of Sample Time.

By default, the block inherits its sample time based upon the context of the block
within the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'-1'` |
## Libraries

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sinks

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

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **BalanceDelays** | | **BalanceDelays** Setting | Description | | --- | --- | | `on` (default) | Detects introduction of delays on other paths in the DUT and inserts matching delays on the Outport block path. | | `off` | Disable delay balancing on output ports in your DUT subsystem to prevent HDL Coder from inserting matching delays when they are unnecessary. For example, disable **BalanceDelays** on an Outport block in your DUT subsystem when treating a manually added output port as a test point. |  **Note**  This property affects only DUT-level  Outport blocks. |
| **BidirectionalPort** | | **BidirectionalPort** Setting | Description | | --- | --- | | `on` | Specify the port as bidirectional.  The following requirements apply:  - The port must be in a Subsystem block   with black box implementation. - There must also be no   logic between the bidirectional port and the corresponding top-level   DUT subsystem port.  For more information, see Specify Bidirectional Ports (HDL Coder). | | `off` (default) | Do not specify the port as bidirectional. | |

| Target Specification | |
| --- | --- |
| **IOInterface** | Target platform interface type for DUT ports, specified as a character vector. The `IOInterface` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterface` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, in the **Set Target** > **Set Target Interface** step, in the **Target platform interface table**,    in the **Target Platform Interfaces** column, use    the drop-down list to set the target platform interface type. 2. Save the model.  The `IOInterface` value is saved as an HDL    block property of the port.  For example, to view the `IOInterface` value,    if the full path to your DUT port is `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | Target platform interface port mapping for DUT ports, specified as a character vector. The `IOInterfaceMapping` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterfaceMapping` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, in the **Set Target** > **Set Target Interface** step, in the **Target platform interface table**,    in the **Target Platform Interfaces** column, use    the drop-down list to set the target platform interface type. 2. In the **Bit Range / Address / FPGA Pin** column,    if you want to change the default value, enter a target platform interface    mapping. 3. Save the model.  The `IOInterfaceMapping` value is saved as    an HDL block property of the port.  For example, to view the `IOInterfaceMapping` value,    if the full path to your DUT port is `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | Target platform interface port mapping options for DUT ports, specified as a character vector. The `IOInterfaceOptions` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterfaceOptions` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, on the **Set Target** > **Set Target Interface** step, in the **Target    platform interface table**, in the    **Target Platform Interfaces**    column, map the input or output ports to an AXI4    subordinate interface. 2. In the **Interface    Options** column, if you want to change    the default initial value, click the    **Options** button and enter a    value for    **RegisterInitialValue**. 3. Save the model.  The `IOInterfaceOptions`    value is saved as an HDL block property of the    port.  For example, to view the    `IOInterfaceOptions` value, if    the full path to your DUT port is    `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

**`Simulink.ValueType` Object Support**

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2025a: Log `datetime` data

The Outport block supports logging `datetime` data.

### R2024a: **Source of initial output value** parameter has been removed

Starting in R2024a, for conditionally executed subsystems, the initial output value is
inherited from the input signal of the subsystem. The software sets the
**Initial output** parameter to `[]` and
**Output when disabled** parameter to
`held`.

### R2023b: Log unbounded variable-size signals

In normal and accelerator mode simulations, the Outport block supports
logging unbounded variable-size signals. Logging is not supported for nonvirtual
buses that contain unbounded variable-size signals.

## Description

Create output port for subsystem or external output

Outport blocks link signals from a system to a destination outside of
the system. They can connect signals flowing from a subsystem to other parts of the
model. They can also supply external outputs at the top level of a model
hierarchy.

Outport block port numbers are assigned according to these rules:

- Outport blocks within a root-level system or subsystem are
  numbered sequentially, starting with 1.
- If you add an Outport block, it is assigned the next available
  number.
- If you delete an Outport block, other port numbers are
  automatically renumbered to ensure that the Outport blocks are in
  sequence and that no numbers are omitted.

### Outport Blocks in a Subsystem

Outport blocks in a subsystem represent outputs from the subsystem. A signal
arriving at an Outport block in a subsystem flows out of the
associated output port on that Subsystem block. The Outport block
associated with an output port is the block whose **Port
number** parameter matches the relative position of the output port on
the Subsystem block. For example, the Outport block whose **Port number** parameter is `1` sends its
signal to the block connected to the topmost output port on the
Subsystem block.

If you renumber the **Port number** of an
Outport block, the block becomes connected to a different output
port. The block continues to send the signal to the same block outside the
subsystem.

You can directly edit port labels on a Subsystem block. For more
information, see Edit Port Labels on Subsystem Blocks.

**Tip**

For models that include buses composed of many bus elements, consider using In Bus
Element and Out Bus Element blocks. These
blocks:

- Reduce signal line complexity and clutter in a block diagram.
- Make it easier to change the interface incrementally.
- Allow access to a bus element closer to the point of usage, avoiding
  the use of a Bus Selector and Goto block
  configuration.

The In Bus Element block is of block type Inport
and the Out Bus Element block is of block type
Outport.

### Top-Level Outport Block in a Model Hierarchy

Outport blocks at the top level of a model hierarchy have two uses. They can
supply external outputs to the base MATLAB® workspace, and they provide a means for the `linmod`
and `trim` analysis functions to obtain output from the
system.

To supply external outputs to the workspace, use the **Configuration Parameters** > **Data Import/Export** pane (see Exporting Output Data to
the MATLAB Workspace) or the `sim` command. For example, if a system has more than one
Outport block and the save format is array, this command

```
[t,x,y] = sim(...);
```

writes `y` as a matrix, with each column containing data for a
different Outport block. The column order matches the order of the
port numbers for the Outport blocks.

If you specify more than one variable name after the second (state) argument, data
from each Outport block is written to a different variable. For
example, if the system has two Outport blocks, to save data from
Outport block 1 to `speed` and the data from
Outport block 2 to `dist`, specify this
command:

```
[t,x,speed,dist] = sim(...);
```

### Connecting Buses to Root-Level Outports

A root-level Outport block in a model can accept a virtual bus only if all
elements of the bus have the same data type. The Outport block
automatically unifies the bus to a vector having the same number of elements as the
bus, and provides that vector as output.

If you want a root-level Outport block of a model to accept a bus that
contains mixed types, set the Outport block **Data
type** to `Bus: <object name>`. If the bus is
virtual, it is converted to nonvirtual, as described in Virtual and Nonvirtual Bus Conversions.

### Associate Root-Level Outport Block with `Simulink.Signal` Object

To associate a root-level Outport block with a
`Simulink.Signal` object, use the Model Data Editor. See For Signals.
