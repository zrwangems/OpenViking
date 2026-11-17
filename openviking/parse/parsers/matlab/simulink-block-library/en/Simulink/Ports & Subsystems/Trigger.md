---
type: simulink-block
title: 'Trigger'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'trigger'
documentation_source_path: 'slref/trigger.html'
language: en
---

# Trigger

## Ports
```yaml
ports:
- name: Port_1
  summary: Value that describes control signal or message payload scalar | vector | matrix
  direction: output
  data_types: double | int8
```

### Output

### **Port\_1** — Value that describes control signal or message payload scalar | vector | matrix

If the **Trigger type** is
`rising`,
`falling`,
`either`, or
`function-call`, the port outputs a value
that identifies a control signal, returned as a scalar or vector. For
each element of the input signal, the value at a given time step
is:

- `1` for a signal that causes a rising
  trigger
- `-1` for a signal that causes a falling
  trigger
- `2` for a function-call event
- `0` in all other cases

If the **Trigger type** is
`message`, the port outputs data extracted
from message received at the control port.

#### Dependencies

To enable this port, select **Show output port**
or set **Trigger type** to
`message`.

**Data Types:** `double` | `int8`
## Parameters
```yaml
parameters:
- name: Trigger type
  summary: Select the type of control signal rising (default) | falling | either | function-call | message
  group: Main
  block_parameter: TriggerType
  type: character vector
  values: '''rising'' | ''falling'' | ''either'' | ''function-call'' | ''message'''
  default: '''rising'''
- name: Treat as Simulink function
  summary: Create Simulink Function block off (default) | on
  group: Main
  block_parameter: IsSimulinkFunction
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Execute function call asynchronously
  summary: Whether caller request to call function can wait for service execution off (default) | on
  group: Main
  block_parameter: AsynchronousFunction
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Function name
  summary: Specify function name for Simulink Function block f (default) | function name
  group: Main
  block_parameter: FunctionName
  type: character vector
  values: '''f'' | function name in quotes'
  default: '''f'''
- name: Function visibility
  summary: Select scope visibility of function scoped (default) | global | port
  group: Main
  block_parameter: FunctionVisibility
  type: character vector
  values: '''scoped'' | ''global'' | ''port'''
  default: '''scoped'''
- name: Scope to port
  summary: Specify name of exporting function port '' (default) | character vector
  group: Main
  block_parameter: ScopeName
  type: character vector
  values: port name in quotes
  default: ''''''
- name: Enable variant condition
  summary: Controls activating the variant control (condition) off (default) | on
  group: Main
  block_parameter: Variant
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Variant control
  summary: Specify variant control (condition) expression (inherit) (default) | logical expression
  group: Main
  block_parameter: VariantControl
  type: character vector
  values: '''(inherit)'' | logical expression | Simulink.VariantExpression object'
  default: '''(inherit)'''
- name: Generate preprocessor conditionals
  summary: Control enclosing variant choices off (default) | on
  group: Main
  block_parameter: GeneratePreprocessorConditionals
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: States when enabling
  summary: Select how to set block state values held (default) | reset | inherit
  group: Main
  block_parameter: StatesWhenEnabling
  type: character vector
  values: '''held'' | ''reset''| ''inherit'''
  default: '''held'''
- name: Propagate sizes of variable-size signals
  summary: Select when to propagate variable-size signals During execution (default) | Only when enabling
  group: Main
  block_parameter: PropagateVarSize
  type: character vector
  values: '''During execution'' | ''Only when enabling'''
  default: '''During execution'''
- name: Show output port
  summary: Control display of output port off (default) | on
  group: Main
  block_parameter: ShowOutputPort
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output data type
  summary: Select output port data type auto (default) | double | int8
  group: Main
  block_parameter: OutputDataType
  type: character vector
  values: '''auto'' | ''double'' | ''int8'''
  default: '''auto'''
- name: Sample time type
  summary: Select calling rate triggered (default) | periodic
  group: Main
  block_parameter: SampleTimeType
  type: character vector
  values: '''triggered'' | ''periodic'''
  default: '''triggered'''
- name: Sample time
  summary: Specify time interval 1 (default) | Ts | [Ts, To] | -1
  group: Main
  block_parameter: SampleTime
  type: character vector
  values: '''1'' | ''Ts''| ''[Ts, To]'' | ''-1'''
  default: '''1'''
- name: Enable zero-crossing detection
  summary: Control zero-crossing detection on (default) | off
  group: Main
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Initial trigger signal state
  summary: Select the initial state of the trigger signal compatibility (no trigger on first evaluation) (default) | zero
    | positive | negative
  group: Main
  block_parameter: InitialTriggerSignalState
  type: character vector
  values: '''compatibility (no trigger on first evaluation)'' | ''zero'' | ''positive'' | ''negative'''
  default: '''compatibility (no trigger on first evaluation)'''
- name: Trigger time
  summary: Specify when message input triggers execution of subsystem on message available (default) | on sample time hit
  group: Main
  block_parameter: TriggerTime
  type: character vector
  values: '''on message available'' | ''on sample time hit'''
  default: '''on message available'''
- name: Schedule as aperiodic partition
  summary: Specify immediate mode or scheduled mode for execution on (default) | off
  group: Main
  block_parameter: ScheduleAsAperiodic
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Port dimensions
  summary: Specify dimensions for the trigger signal 1 (default) | [n] | [m n] | -1
  group: Signal Attributes
  block_parameter: PortDimensions
  type: character vector
  values: '''1'' | ''[n]'' | ''[m n]'' | -1'
  default: '''1'''
- name: Trigger signal sample time
  summary: Specify time interval -1 (default) | Ts | [Ts, To]
  group: Signal Attributes
  block_parameter: TriggerSignalSampleTime
  type: character vector
  values: '''-1'' | ''Ts''| ''[Ts, To]'''
  default: '''-1'''
- name: Minimum
  summary: Specify minimum output value for the trigger signal [] (default) | real scalar
  group: Signal Attributes
  block_parameter: OutMin
  type: character vector
  values: '''[]'' | real scalar in quotes'
  default: '''[]'''
- name: Maximum
  summary: Specify maximum output value for the trigger signal [] (default) | real scalar
  group: Signal Attributes
  block_parameter: OutMax
  type: character vector
  values: '''[]'' | real scalar in quotes'
  default: '''[]'''
- name: Data type
  summary: 'Select output data type for the trigger signal Inherit: auto (default) | double | single | int8 | uint8 | int16
    | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^,0) | <data type expression>'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''
    | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: auto'''
- name: Mode
  summary: Select data type category Built in (default) | Fixed point | Expression
  group: Signal Attributes
- name: Interpolate data
  summary: Control how missing workspace data is estimated on (default) | off
  group: Signal Attributes
  block_parameter: Interpolate
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
```

### Main

### **Trigger type** — Select the type of control signal `rising` (default) | `falling` | `either` | `function-call` | `message`

Select the type of control signal that executes a subsystem or
model.

- `rising` — Trigger execution of
  subsystem or model when the control signal rises from a negative
  or zero value to a positive value. If the initial value is
  negative, a rising signal to zero triggers execution.
- `falling` — Trigger execution of
  subsystem or model when the control signal falls from a positive
  or a zero value to a negative value. If the initial value is
  positive, a falling signal to zero triggers execution.
- `either` — Trigger execution of
  subsystem or model when the control signal is either rising or
  falling.
- `function-call` — Execute subsystem
  or model when the control port receives a function-call event
  from a Stateflow chart, Function-Call Generator
  block, S-Function block, or Hit
  Crossing block.
- `message` — Trigger execution of
  subsystem when a message is available at the control port. The
  block must be inside a subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TriggerType` |
| **Type:** character vector |
| **Values:** `'rising'` | `'falling'` | `'either'` | `'function-call'` | `'message'` |
| **Default:** `'rising'` |

### **Treat as Simulink function** — Create Simulink Function block `off` (default) | `on`

Select this parameter to create a Simulink Function
block by configuring a Subsystem block that is callable
with arguments from a function caller. The Trigger block
must reside within the subsystem. You can edit the function prototype
that displays on the block face to specify input and output arguments
for the block.

Clear this parameter to remove the configuration.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to
`function-call`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IsSimulinkFunction` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Execute function call asynchronously** — Whether caller request to call function can wait for service execution `off` (default) | `on`

Specify whether to execute the Simulink Function block
asynchronously for a subsystem containing this Trigger
port block.

- Select this parameter to model *asynchronous
  execution* where the caller (client) makes a
  request to call the function (server). The function is executed
  based on the ordering defined in the Schedule Editor and then returns the output
  arguments to the caller.
- Clear this parameter to model *synchronous
  execution* where the caller calls the function
  and the function runs immediately then returns the output
  arguments to the caller.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call`,
select **Treat as a Simulink Function**, and set
**Function visibility** to
`port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AsynchronousFunction` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Function name** — Specify function name for Simulink Function block `f` (default) | function name

Specify the function name for a Simulink Function
block. Alternatively, you can specify the name by editing the function
prototype on the face of the block.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call` and
select **Treat as a Simulink Function**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionName` |
| **Type:** character vector |
| **Values:** `'f'` | function name in quotes |
| **Default:** `'f'` |

### **Function visibility** — Select scope visibility of function `scoped` (default) | `global` | `port`

Select scope of Simulink Function block within
subsystem or model.

- `scoped` — Limit accessibility of
  function to:

  - Hierarchic level containing the Simulink
    Function block and levels below.
  - One hierarchical level above with
    qualification.
- `global` — Function accessible from
  any part of the model hierarchy.
- `port` — Function accessible only
  through an exporting function port created by a Function
  Element block.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call` and
select **Treat as a Simulink Function**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionVisibility` |
| **Type:** character vector |
| **Values:** `'scoped'` | `'global'` | `'port'` |
| **Default:** `'scoped'` |

### **Scope to port** — Specify name of exporting function port `''` (default) | character vector

For a Simulink Function block with port visibility,
specify the name of the exporting function port created by a Function
Element block through which the function can be
called.

**Example:** `'ServerPort'`

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call`,
select **Treat as a Simulink Function**, and set
**Function visibility** to
`port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScopeName` |
| **Type:** character vector |
| **Values:** port name in quotes |
| **Default:** `''` |

### **Enable variant condition** — Controls activating the variant control (condition) `off` (default) | `on`

Control activating the variant control (condition) defined with the
**Variant Control** parameter.

Select this parameter to activate variant control of the subsystem.
Selecting this parameter:

- Enables the **Variant control**
  parameter.
- Displays a variant badge  on the face of the block
  indicating that variant conditions are enabled.

Clear this parameter to deactivate variant control of the
subsystem.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call` and
select **Treat as Simulink function**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Variant` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Variant control** — Specify variant control (condition) expression `(inherit)` (default) | logical expression

Specify variant control (condition) expression that executes a variant
Simulink Function block when the expression evaluates
to `true`.

- `(inherit)` — Default value for variant
  control. Inherits the variant condition from the corresponding
  Function Caller blocks in the model. When
  **Variant Control** is set as
  `(inherit)` the value for
  **Generate preprocessor conditionals** is
  inherited automatically from the Function Caller
  block in the model.
- logical expression — A logical (Boolean) expression or a
  `Simulink.VariantExpression` object
  representing a logical expression. The function is activated
  when the expression evaluates to `true`.

  If you want to generate code for your model, define the
  variables in the expression as
  `Simulink.Parameter` objects.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call`,
select **Treat as a Simulink Function**, and
select **Enable variant condition**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControl` |
| **Type:** character vector |
| **Values:** `'(inherit)'` | logical expression | `Simulink.VariantExpression` object |
| **Default:** `'(inherit)'` |

### **Generate preprocessor conditionals** — Control enclosing variant choices `off` (default) | `on`

Control enclosing variant choices within C preprocessor conditional
statements.

Select this parameter to enclose variant choices within C preprocessor
conditional statements (#if) when generating code for an ERT
target.

#### Dependencies

To display and enable this parameter, select **Enable
variant condition** .

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GeneratePreprocessorConditionals` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **States when enabling** — Select how to set block state values `held` (default) | `reset` | `inherit`

Select how to set block state values when the subsystem or model is
disabled.

- `held` — Leave the block states at
  their current values.
- `reset` — Reset the block state
  values.
- `inherit` — Use the
  `held` or
  `reset` setting from the parent
  subsystem initiating the function-call. If the parent of the
  initiator is the model root, the inherited setting is
  `held`. If the trigger has multiple
  initiators, set the parents of all initiators to either
  `held` or
  `reset`.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`function-call`.

This parameter setting applies only if the model explicitly
enables and disables the function-call subsystem. For
example:

- The function-call subsystem resides in an enabled
  subsystem. In this case, the model enables and disables
  the function-call subsystem along with the parent
  subsystem.
- The function-call initiator that controls the
  function-call subsystem resides in an enabled subsystem.
  In this case, the model enables and disables the
  function-call subsystem along with the enabled subsystem
  containing the function-call initiator.
- The function-call initiator is a Stateflow event bound to a particular state. See
  Control Function-Call Subsystems by Using bind Actions (Stateflow).
- The function-call initiator is an S-function that
  explicitly enables and disables the function-call
  subsystem. See `ssEnableSystemWithTid` for an
  example.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StatesWhenEnabling` |
| **Type:** character vector |
| **Values:** `'held'` | `'reset'`| `'inherit'` |
| **Default:** `'held'` |

### **Propagate sizes of variable-size signals** — Select when to propagate variable-size signals `During execution` (default) | `Only when enabling`

Select when to propagate variable-size signals.

- `During execution` — Propagate
  variable-size signals at each time step.
- `Only when enabling` — Propagate
  variable-size signals when executing a Subsystem
  block or Model block containing an
  Enable port, Trigger port with
  **Trigger type** set to
  `function-call`, or Action
  Port block. When you select this option, sample time
  must be periodic.

#### Dependencies

To display and enable this parameter for a Trigger
port block, set **Trigger type** to
`Function-call`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropagateVarSize` |
| **Type:** character vector |
| **Values:** `'During execution'` | `'Only when enabling'` |
| **Default:** `'During execution'` |

### **Show output port** — Control display of output port `off` (default) | `on`

Control display of an output port for a signal that identifies the
trigger signal or function-call event signal.

Select this parameter to display the output port and determine which
signal caused the trigger signal or function-call event. The width of
the output port signal is the width of the control signal. The signal
value is:

- `1` for a signal that causes a rising
  trigger
- `-1` for a signal that causes a falling
  trigger
- `2` for a function-call event
- `0` in all other cases

Clear this parameter to remove the output port.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to an option other than
`message`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputPort` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output data type** — Select output port data type `auto` (default) | `double` | `int8`

Select the output port data type for the signal that identifies the
trigger signal or function-call event signal.

- `auto` — Data type from the port connected to
  the output
- `double` — Double value
- `int8` — Integer value

#### Dependencies

To enable this parameter, select **Show output
port**.

The Trigger block ignores the **Data type override** setting for the Fixed-Point
Tool.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputDataType` |
| **Type**: character vector |
| **Values**: `'auto'` | `'double'` | `'int8'` |
| **Default**: `'auto'` |

### **Sample time type** — Select calling rate `triggered` (default) | `periodic`

Select the calling rate for a subsystem or model.

- `triggered`
  — Apply to applications that do not have a periodic
  function-call frequency. A function-call initiator can execute a
  triggered (aperiodic) function-call subsystem one or more times
  per time step and can provide a series of aperiodic
  function-call events.
- `periodic` — A function-call
  initiator can execute a periodic function-call system only once
  per time step and must provide a series of periodic
  function-call events.. A Stateflow chart is an example of a function-call
  initiator.

#### Dependencies

To enable this parameter, set **Trigger type**
to `Function-call`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTimeType` |
| **Type**: character vector |
| **Values**: `'triggered'` | `'periodic'` |
| **Default**: `'triggered'` |

### **Sample time** — Specify time interval `1` (default) | `Ts` | `[Ts, To]` | `-1`

Specify the time interval between function calls to a subsystem or
model containing this Trigger port block. If the actual
calling rate for the subsystem or model differs from the time interval
this parameter specifies, the software displays an error.

- `Ts` — Scalar where `Ts` is
  the time interval
- `[Ts, To]` — Vector where
  `Ts` is the time interval and
  `To` is the initial time offset
- `-1` — Inherited time interval from the
  control signal

#### Dependencies

To enable this parameter, set **Trigger type**
to `function-call` and **Sample
time type** to
`periodic`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: `'1'` | `'Ts'`| `'[Ts, To]'` | `'-1'` |
| **Default**: `'1'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Select this parameter to detect zero crossings.

#### Dependencies

To enable this parameter, set **Trigger type** to
`rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Initial trigger signal state** — Select the initial state of the trigger signal `compatibility (no trigger on first evaluation)` (default) | `zero` | `positive` | `negative`

Select the initial state of the trigger control signal.

- `compatibility (no trigger on first
  evaluation)` — No trigger at the first
  evaluation of trigger signal. If you choose this option and the
  Trigger block is in a subsystem where the
  states are reset, the block does not reset.
- `zero` — Zero. Helps to evaluate a
  rising or falling trigger signal at the first time step.
- `positive` — Positive value. Helps to
  evaluate a falling trigger signal at the first time step.
- `negative` — Negative value. Helps to
  evaluate a rising trigger signal at the first time step.

#### Dependencies

To display and activate this parameter, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialTriggerSignalState` |
| **Type**: character vector |
| **Values**: `'compatibility (no trigger on first evaluation)'` | `'zero'` | `'positive'` | `'negative'` |
| **Default**: `'compatibility (no trigger on first evaluation)'` |

### **Trigger time** — Specify when message input triggers execution of subsystem `on message available` (default) | `on sample time hit`

For a subsystem triggered by message input, specify timing of execution.

- `on message available` — Trigger
  execution of subsystem and pull messages whenever one or
  more messages are available at the control port.
- `on sample time hit` — At each
  time step, check whether a message is available at the
  control port. If so, pull one message and trigger execution
  of subsystem. If no message is available, do not execute
  subsystem at that time step.

#### Dependencies

To display and activate this parameter, set **Trigger
type** to `message`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TriggerTime` |
| **Type**: character vector |
| **Values**: `'on message available'` | `'on sample time hit'` |
| **Default**: `'on message available'` |

### **Schedule as aperiodic partition** — Specify immediate mode or scheduled mode for execution `on` (default) | `off`

For a subsystem triggered by message availability, specify execution
mode.

Clear this parameter for *immediate mode*, in
which the subsystem executes as soon as a message is available at the
control port, which pushes the message to the subsystem without a queue
buffering the message.

Select this parameter for *scheduled mode*, which
allows subsystem execution to be deferred after a specific Simulink® task while staying at the same time step.

#### Dependencies

To display and activate this parameter, set **Trigger
type** to `message` and
**Trigger time** to `on message
available`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScheduleAsAperiodic` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### Signal Attributes

### **Port dimensions** — Specify dimensions for the trigger signal `1` (default) | `[n]` | `[m n]` | `-1`

Specify dimensions for the trigger signal attached externally a
Model block and passed into the referenced
model.

- `1` — Scalar signal
- `[n]` — Vector signal of width
  `n`
- `[m n]` — Matrix signal having
  `m` rows and `n`
  columns
- `-1` — Inherited dimensions

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PortDimensions` |
| **Type**: character vector |
| **Values**: `'1'` | `'[n]'` | `'[m n]'` | `-1` |
| **Default**: `'1'` |

### **Trigger signal sample time** — Specify time interval `-1` (default) | `Ts` | `[Ts, To]`

Specify time interval between block method executions for the block
driving the trigger signal.

- `-1` — Inherited time interval
- `Ts` — Scalar where `Ts` is
  the time interval
- `[Ts, To]` — Vector where
  `Ts` is the time interval and
  `To` is the initial time offset

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TriggerSignalSampleTime` |
| **Type**: character vector |
| **Values**: `'-1'` | `'Ts'`| `'[Ts, To]'` |
| **Default**: `'-1'` |

### **Minimum** — Specify minimum output value for the trigger signal `[]` (default) | real scalar

Specify minimum value for the trigger signal attached externally to a
Model block and passed to the inside of the
block.

The software uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can
  remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | real scalar in quotes |
| **Default**: `'[]'` |

### **Maximum** — Specify maximum output value for the trigger signal `[]` (default) | real scalar

Specify maximum value for the trigger signal attached externally to a
Model block and passed to the inside of the
block.

The software uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can
  remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | real scalar in quotes |
| **Default**: `'[]'` |

### **Data type** — Select output data type for the trigger signal `Inherit: auto` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `<data type expression>`

Select data type for the trigger signal attached externally to a
Model block and passed to the inside of the
block.

- `Inherit: auto` — Inherited data
  type
- `double` — Double-precision floating
  point
- `single` — Single-precision floating
  point
- `int8` — Signed 8-bit integer
- `uint8` — Unsigned 8-bit
  integer
- `int16` — Signed 16-bit
  integer
- `uint16` — Unsigned 16-bit
  integer
- `int32` — Signed 32-bit
  integer
- `uint32` — Unsigned 32-bit
  integer
- `int64` — Signed 64-bit
  integer
- `uint64` — Unsigned 64-bit
  integer
- `boolean` — Boolean with a value of
  `true` or `false`
- `fixdt(1,16)` — Signed 16-bit fixed
  point number with binary point undefined
- `fixdt(1,16,0)` — Signed 16-bit fixed
  point number with binary point set to zero
- `fixdt(1,16,2^,0)` — Signed 16-bit
  fixed point number with slope set to `2^0` and
  bias set to `0`
- `<data type expression>` — Data
  type object, for example a `Simulink.NumericType`
  object

You cannot enter the name of a `Simulink.Bus` object as
a data type expression.

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: auto'` |

### **Mode** — Select data type category `Built in` (default) | `Fixed point` | `Expression`

Select data type category and display drop-down lists to help you
define the data type.

- `Built in` — Display menus for data
  type and **Data type override**.
- `Fixed point` — Display menus for
  **Signedness**,
  **Scaling**, and **Data type
  override**.
- `Expression` — Display text box for
  entering an expression.

#### Dependencies

To enable this parameter, select the Show data type assistant
button .

### **Interpolate data** — Control how missing workspace data is estimated `on` (default) | `off`

Control how missing workspace data is estimated when loading data from
the MATLAB® workspace.

Select this parameter to linearly interpolate output at time steps for
which no corresponding workspace data exists.

Clear this parameter to set the output at such time steps equal to the
output at the most recent time step for which data exists.

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Interpolate` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |
## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

For more information, see HDL Code Generation in Triggered Subsystem.

**HDL Architecture**

This block has one default HDL architecture.

**Restriction**

You cannot generate HDL code for a Trigger Block that has **Trigger
type** set to `function-call` or
`message`.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Add trigger or function port to subsystem or model

The Trigger block adds an external signal or message port to control
the execution of a subsystem or a model. To enable this functionality, add this block to
a Subsystem block or at the root level of a model that is referenced in a
Model block.

Then, configure the Trigger block to execute a subsystem or
model:

- Once at each time step, when the value of the control signal changes in a way
  that you specify.
- Multiple times during a time step, when the control signal is a function-call
  event from a Stateflow® chart, Function-Call Generator block, or
  S-Function block.
- Based on messages received at the control port.
