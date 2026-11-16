---
type: simulink-block
title: 'State Transition Table'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: 'Chart Programming / Chart Programming Basics / Stateflow Charts'
documentation_page: 'statetransitiontable'
documentation_source_path: 'ref/statetransitiontable.html'
language: en
---

# State Transition Table

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

When you create input data in the Stateflow state transition table using the
**Symbols** pane, Stateflow creates a corresponding input port on the State
Transition Table block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### Output

### **Port\_1** — Output port scalar | vector | matrix

When you create output data in the Stateflow state transition table by using the
**Symbols** pane, Stateflow creates a corresponding output port on the State
Transition Table block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

**Note**

State Transition Table blocks also have Subsystem (Simulink) block parameters that you
can access by right-clicking the block and clicking **Block Parameters
(Subsystem)**. However, updating these block parameters is not
recommended.

### **Update method** — Method to update or wake up Stateflow state transition tables `Inherited` (default) | `Discrete` | `Continuous`

Method to update or wake up a Stateflow state transition table, specified as
`Inherited`,
`Discrete`, or
`Continuous`.

`Inherited`
:   Input from the Simulink model determines when the state transition table
    wakes up during a simulation.

    If you define input events for the state transition table, the
    signal from the Simulink block connected to the trigger port triggers the
    state transition table. The Simulink signal can be `Rising`, `Falling`, or `Either` (rising and falling), or in response
    to a `Function Call`. For
    more information, see Activate a Stateflow Chart by Sending Input Events.

    If you do not define input events, the Stateflow state transition table implicitly inherits
    triggers from the Simulink model. These implicit events are the discrete or
    continuous sample times of the Simulink signals that provide inputs to the state
    transition table. If you define data inputs, the state
    transition table wakes at the rate of the fastest data input. If
    you do not define any data input for the state transition table,
    the state transition table wakes up as defined by the execution
    behavior of its parent subsystem.

`Discrete`
:   The Stateflow state transition table wakes when the Simulink model generates an implicit event at regular time
    intervals that you specify in the **Sample
    Time** state transition table property. Other
    blocks in the Simulink model can have different sample times.

`Continuous`
:   The Stateflow state transition table updates its state during
    major time steps only, and computes outputs and local continuous
    variables during major and minor time steps. The state
    transition table can register zero crossings, which allows
    Simulink models to sample Stateflow state transition tables whenever state changes
    occur. The Stateflow state transition table computes derivatives for
    local continuous variables. For more information, see Continuous-Time Modeling in Stateflow.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **Values:** | `"INHERITED"` (default) | `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — Time interval that state transition table wakes up during simulation `-1` (default) | scalar | vector

The default time interval is `-1`, which indicates that
the Stateflow state transition table inherits the sample time from
Simulink.

Specify the time interval at which the state transition table wakes up
during simulation. The default value indicates that the state transition
table inherits the sample time from Simulink. For more information on specifying sample time, see Specify Sample Time (Simulink).

Do not use the **Sample Time** parameter in the
Subsystem block parameters. Instead, use the
Property Inspector.

#### Dependencies

To enable this parameter, set **Update method** to
`Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### **Create output for monitoring** — Whether to create active state data output `off` (default) | `on`

Whether to create an active state data output port for the state
transition table. For more information, see Monitor State Activity Through Active State Data.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `HasOutputData` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Output monitoring mode** — Monitoring mode for active state output `Child activity` (default) | `Leaf state activity`

Monitoring mode for the active state output data.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `OutputMonitoringMode` |
| **Values:** | `"ChildActivity"` (default) | `"LeafStateActivity"` |

### **Data name** — Name of active state data object `State_Transition_TableMode` (default) | scalar

Name of the active state data object for the state transition
table.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `OutputPortName` |
| **Values:** | `"State_Transition_TableMode"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### **Enum name** — Name of enumerated data type for active state data object `State_Transition_TableModeType` (default) | scalar

Name of the active state data object for the state transition
table.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `EnumTypeName` |
| **Values:** | `"State_Transition_TableModeType"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### **Define enumerated type manually** — Whether to define enumerated data type manually `off` (default) | `on`

Whether to define the enumerated data type for the active state data
output manually. For more information, see Define State Activity Enumeration Type.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.StateTransitionTableChart` object of the block
and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `DoNotAutogenerateEnum` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### Advanced

### **Execute (enter) chart at initialization** — Whether to initialize state configuration `off` (default) | `on`

Whether to initialize the state configuration of the state transition
table at time zero instead of at the first input event. For more
information, see Execution of a Chart at Initialization.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `ExecuteAtInitialization` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Saturate on integer overflow** — Whether data saturates on integer overflow `on` (default) | `off`

Whether the data in the state transition table
saturates on integer overflow. When you clear this
parameter, the data in the state transition table
wraps on integer overflow. For more information, see
Handle Integer and Enumeration Overflow for Chart Data.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Initialize outputs every time chart wakes up** — Whether to initialize output data `off` (default) | `on`

Whether to initialize the output data every time the state transition
table wakes up.

When you select this parameter, the state transition table resets its
output values every time that the state transition table wakes up, not
only at time 0. The state transition table resets the output values
whenever function call, edge trigger, or clock tick triggers the state
transition table. If you set an initial value for an output data object,
the output resets to that value. Otherwise, the output resets to zero.
Select this parameter to:

- Ensure that all outputs are defined in every state
  transition table execution.
- Prevent latching of outputs, that is, prevent values of
  outputs computed in previous executions.
- Provide all state transition table outputs with a
  meaningful initial value.

For more information, see Initial value.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `InitializeOutput` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Support variable-size arrays** — Whether the state transition table supports variable size data `on` (default) | `off`

Whether the state transition table supports variable-size data. For
more information, see Declare Variable-Size Data in Stateflow Charts.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SupportVariableSizing` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Enable super step semantics** — Whether to enable super step semantics `off` (default) | `on`

Whether to enable super step semantics for the state transition table.
Select this parameter to enable the state transition table to take
multiple transitions in each time step until it reaches a stable state.
This option is not available when you. For more information, see Super Step Semantics.

#### Dependencies

To enable this parameter, set **Update method**
to `Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `EnableNonTerminalStates` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Max iterations in a superstep** — Maximum number of transitions `1000` (default) | positive integer

The maximum number of transitions that can be completed in one super
step. For more information, see Super Step Semantics.

#### Dependencies

To enable this parameter, enable **Enable super step
semantics**.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `NonTerminalMaxCounts` |
| **Values:** | `1000` (default) | positive integer |
| **Data Types:** | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` |

### **After too many iterations** — Action if super step exceeds maximum number of transitions `Proceed` (default) | `Throw Error`

Action for Stateflow to take if super step exceeds maximum number of
transitions in one super step. For more information, see Super Step Semantics.

#### Dependencies

To enable this parameter, enable **Enable super step
semantics**.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `NonTerminalUnstableBehavior` |
| **Values:** | `"Proceed"` (default) | `"Throw Error"` |

### **Treat dimensions of length 1 as fixed size** — Whether state transition table treats non-scalar data with dimension of length 1 as fixed size `on` (default) | `off`

*Since R2023a*

Whether the state transition table treats non-scalar data with a
dimension of length 1 as fixed size. When you select this parameter, the
state transition table treats non-scalar data that have at least one
dimension of length 1 as fixed size, regardless of whether you enable
the **Variable
size** data property. When you clear this parameter,
the state transition table treats non-scalar data with the
**Variable size** property enabled as variable
size.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Action language** — Action language `MATLAB` (default) | `C`

Action language to use to program the state transition table,
specified as `MATLAB` or `C`. For more
information, see Differences Between MATLAB and C as Action Language Syntax.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `ActionLanguage` |
| **Values:** | `"MATLAB"` (default) | `"C"` |

### **State machine type** — State machine semantics `Classic` (default) | `Mealy` | `Moore`

State machine semantics implemented by the state transition table,
specified as `Classic`, `Mealy`, or
`Moore`. For more information, see Overview of Mealy and Moore Machines.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `StateMachineType` |
| **Values:** | `"Classic"` (default) | `"Mealy"` | `"Moore"` |

### Fixed-point properties

### **Treat these inherited Simulink signal types as fi objects** — Inherited Simulink signals to treat as `fi` objects `Fixed-point` (default) | `Fixed-point & Integer`

Inherited Simulink signals to treat as Fixed-Point Designer™
`fi` objects, specified as one of these values:

- `Fixed-point` — The state transition
  table treats all fixed-point inputs as `fi`
  objects.
- `Fixed-point & Integer` — The state
  transition table treats all fixed-point and integer inputs
  as `fi` objects.

This parameter applies only to state transition tables
that use MATLAB as the action language.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatAsFi` |
| **Values:** | `"Fixed-point"` (default) | `"Fixed-point & Integer"` |

### **MATLAB Function fimath** — Default `fimath` properties `Same as MATLAB` (default) | `Specify Other`

Default `fimath` object properties for the state
transition table, specified as one of these values:

- `Same as MATLAB` — The state transition
  table uses the same `fimath` object
  properties as the current default `fimath`
  object. The text box is dimmed and displays the current
  global `fimath` object in read-only
  form.
- `Specify other` — Specify your own
  `fimath` object in the text box.

For more information, see fimath Object Construction (Fixed-Point Designer).

#### Dependencies

To enable this parameter, set **Action
language** to
`MATLAB`.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.StateTransitionTableChart` object of the
block and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `EmlDefaultFimath` |
| **Values:** | `"Same as MATLAB Default"` (default) | `"Other:UserSpecified"` |

## Libraries

Stateflow

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Tunable Parameters**

You can use a tunable parameter in a State Transition Table
intended for HDL code generation. For details, see Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**Active State Output**

To generate an output port in the HDL code that
shows the active state, in the Properties window of the chart, select **Create
output for monitoring**. The output is an enumerated data type. See Simplify Stateflow Charts by Incorporating Active State Output.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Speed and Area Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Understand Delay Balancing in HDL Coder (HDL Coder) | When optimizations or block implementation options introduce delays along the critical path in a model, *Delay Balancing* detects introduction of new delays along one path, and then inserts matching delays on the other paths. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**Restrictions**

To learn about restrictions, see Introduction to Stateflow HDL Code Generation (HDL Coder).

When you apply optimizations, the block has these limitations:

- State Transition Table block that has **State Machine
  Type** property set to `Moore`
  does not support HDL optimizations.
- HDL optimizations are not supported for the block that has
  **Trigger** port.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2012b**

### R2023b: Convert to chart

To convert a state transition table to a Stateflow chart, use the object function `convertToChart`.

### R2023a: Add parallel states

To set the decomposition of a state transition table state to parallel, select
the state. In the **Modeling** tab, select **Set State Decomposition** > **Parallel
(AND)**.

### R2023a: Specify how to treat non-scalar data with dimension of length 1

With the new property **Treat dimensions of length 1 as fixed size**, you can specify
how state transition tables treat non-scalar data when at least one dimension has
length 1. Prior to R2023a, state transition tables treated non-scalar data with at
least one dimension of length 1 as fixed size, regardless of whether you enabled the
**Variable size** data
property.

### R2022b: Export contents of state transition tables

Export the contents of a state transition table as a structure array by calling
the object function `exportAsStruct`.

### R2022b: New keyboard shortcut

The keyboard shortcut to append a transition column to a state transition table is
now **Ctrl+K**. In previous releases, the shortcut was
**Ctrl+M**.

## Description

Represent modal logic in tabular format

The State Transition Table block represents a finite state machine in
tabular format. Instead of drawing states and transitions in a Stateflow® chart, you can use a state transition table to model a state machine in a
concise, compact format that requires minimal maintenance of graphical objects. For more
information, see Model Finite State Machines Using State Transition Tables.

To implement control logic, State Transition Table blocks can use
MATLAB® or C as the action language. For more information, see Differences Between MATLAB and C as Action Language Syntax.
