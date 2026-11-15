---
type: simulink-block
title: 'Chart'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: 'Chart Programming / Chart Programming Basics / Stateflow Charts'
documentation_page: 'chart'
documentation_source_path: 'ref/chart.html'
language: en
---

# Chart

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

When you create input data in the Stateflow chart using the **Symbols** pane,
Stateflow creates a corresponding input port on the
Chart block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### Output

### **Port\_1** — Output port scalar | vector | matrix

When you create output data in the Stateflow chart by using the **Symbols** pane,
Stateflow creates a corresponding output port on the
Chart block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

**Note**

Charts also have Subsystem (Simulink) block parameters that you
can access by right-clicking the chart and clicking **Block Parameters
(Subsystem)**. However, updating these parameters is not
recommended.

### **Update method** — Method to update or wake up Stateflow charts `Inherited` (default) | `Discrete` | `Continuous`

Method to update or wake up a Stateflow chart, specified as `Inherited`,
`Discrete`, or
`Continuous`.

`Inherited`
:   Input from the Simulink model determines when the chart wakes up during a
    simulation.

    If you define input events for the chart, the signal from the
    Simulink block connected to the trigger port triggers the
    chart. The Simulink signal can be `Rising`, `Falling`, or `Either` (rising and falling), or in response
    to a `Function Call`. For
    more information, see Activate a Stateflow Chart by Sending Input Events.

    If you do not define input events, the Stateflow chart implicitly inherits triggers from the
    Simulink model. These implicit events are the discrete or
    continuous sample times of the Simulink signals that provide inputs to the chart. If you
    define data inputs, the chart wakes at the rate of the fastest
    data input. If you do not define any data input for the chart,
    the chart wakes up as defined by the execution behavior of its
    parent subsystem.

`Discrete`
:   The Stateflow chart wakes when the Simulink model generates an implicit event at regular time
    intervals that you specify in the **Sample
    Time** chart property. Other blocks in the
    Simulink model can have different sample times.

`Continuous`
:   The Stateflow chart updates its state during major time steps
    only, and computes outputs and local continuous variables during
    major and minor time steps. The chart can register zero
    crossings, which allows Simulink models to sample Stateflow charts whenever state changes occur. The
    Stateflow chart computes derivatives for local continuous
    variables. For more information, see Continuous-Time Modeling in Stateflow.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **Values:** | `"INHERITED"` (default) | `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample Time** — Time interval that a Stateflow chart wakes up during simulation `-1` (default) | scalar | vector

Specify the time interval at which the chart wakes up during simulation.
The default value indicates that the chart inherits the sample time from
Simulink. For more information on specifying sample time, see Specify Sample Time (Simulink).

Do not use the **Sample Time** parameter in the
Subsystem block parameters. Instead, use the
Property Inspector.

#### Dependencies

To enable this parameter, set **Update method** to
`Discrete`.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### **Enable zero-crossing detection** — Whether to enable zero-crossing detection on state transitions in the chart `on` (default) | `off`

Whether to enable zero-crossing detection on state transitions in the
chart. For more information, see Continuous-Time Modeling in Stateflow.

#### Dependencies

To enable this parameter, set **Update method** to
`Continuous`.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `EnableZeroCrossings` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Enable C-bit operations** — Whether to enable C-bit operations in the chart `off` (default) | `on`

Whether to use bit operations in state and transition actions in the
chart, specified as a numeric or logical 1 (true) or 0 (false).

#### Dependencies

To enable this parameter, set **Action language**
to `C`.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `EnableBitOps` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Create output for monitoring** — Whether to create active state data output `off` (default) | `on`

Whether to create an active state data output port for the chart. For more
information, see Monitor State Activity Through Active State Data.

#### Dependencies

To enable this parameter, create a Stateflow state, state transition table, or atomic subchart.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `HasOutputData` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Output monitoring mode** — Monitoring mode for active state output `Child activity` (default) | `Leaf state activity`

Monitoring mode for the active state output data. For more information,
see Monitor State Activity Through Active State Data.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `OutputMonitoringMode` |
| **Values:** | `"ChildActivity"` (default) | `"LeafStateActivity"` |

### **Data name** — Name of active state data object `ChartMode` | scalar

Name of the active state data object for the state transition
table.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `OutputPortName` |
| **Values:** | `"ChartMode"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### **Enum name** — Name of enumerated data type for active state data object `ChartModeType` | scalar

Name of the active state data object for the state transition
table.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `EnumTypeName` |
| **Values:** | `"ChartModeType"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### **Define enumerated type manually** — Whether to define enumerated data type manually `off` (default) | `on`

Whether to define the enumerated data type for the active state data
output manually. For more information, see Define State Activity Enumeration Type.

#### Dependencies

To enable this parameter, enable **Create output for
monitoring**.

#### Programmatic Use

To set the chart parameter value programmatically, access the `Stateflow.Chart` object of
the chart and change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `DoNotAutogenerateEnum` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### Advanced

### **Execute (enter) chart at initialization** — Whether to initialize state configuration `off` (default) | `on`

Whether to initialize the state configuration of the chart at time
zero instead of at the first input event. For more information, see
Execution of a Chart at Initialization.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `ExecuteAtInitialization` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Saturate on integer overflow** — Whether data saturates on integer overflow `on` (default) | `off`

Whether the data in the chart saturates on integer
overflow. When you clear this parameter, the data in
the chart wraps on integer overflow. For more
information, see Handle Integer and Enumeration Overflow for Chart Data.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Initialize outputs every time chart wakes up** — Whether to initialize output data `on` (default) | `off`

Whether to initialize the output data every time the chart wakes
up.

When you select this parameter, the chart resets its output values
every time that the chart wakes up, not only at time 0. The chart resets
the output values whenever function call, edge trigger, or clock tick
triggers the chart. If you set an initial value for an output data
object, the output resets to that value. Otherwise, the output resets to
zero. Select this parameter to:

- Ensure that all outputs are defined in every chart
  execution.
- Prevent latching of outputs, that is, prevent values of
  outputs computed in previous executions.
- Provide all chart outputs with a meaningful initial
  value.

For more information, see Initial value.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `InitializeOutput` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Support variable-size arrays** — Whether the chart supports variable size data `on` (default) | `off`

Whether the chart supports variable-size data. For more information,
see Declare Variable-Size Data in Stateflow Charts.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `SupportVariableSizing` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Export chart level functions** — Whether to export chart-level functions `off` (default) | `on`

Whether to export chart-level functions to other blocks in the
Simulink model. For more information, see Export Stateflow Functions for Reuse.

#### Dependencies

To enable this parameter, add a function to your chart.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `ExportChartFunctions` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Treat exported functions as globally visable** — Whether exported functions are globally visible `off` (default) | `on`

Whether exported functions from the chart are globally visible in the
Simulink model. When this property is enabled, blocks throughout
the model can call functions exported from the chart without using
qualified notation.

#### Dependencies

To enable this parameter, enable **Export chart level
functions**.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `AllowGlobalAccessToExportedFunctions` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Enable super step semantics** — Whether to enable super step semantics `off` (default) | `on`

Whether to enable super step semantics for the chart. Select this
parameter to enable the chart to take multiple transitions in each time
step until it reaches a stable state. This option is not available when
you set the chart property **Update method** to
`Continuous`. For more information, see Super Step Semantics.

#### Dependencies

To enable this parameter, set **Update method**
to `Discrete`.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

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

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

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

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `NonTerminalUnstableBehavior` |
| **Values:** | `"Proceed"` (default) | `"Throw Error"` |

### **Treat dimensions of length 1 as fixed size** — Whether chart treats non-scalar data with dimension of length 1 as fixed size `on` (default) | `off`

*Since R2022b*

Whether the chart treats non-scalar data with a dimension of length 1
as fixed size. When you select this parameter, the chart treats
non-scalar data that have at least one dimension of length 1 as fixed
size, regardless of whether you enable the **Variable
size** data property. When you clear this parameter,
the chart treats non-scalar data with the **Variable
size** property enabled as variable size.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Variant activation time** — Active choice of the variant blocks or variant parameters at different stages of the simulation and code generation workflow `update diagram analyze all choices` (default) | `code compile`

Specify which block variants Stateflow analyzes during simulation and code generation. Based on
the option you choose, Stateflow determines if the generated code must contain only the
active choice or both active and inactive choices.

- `update diagram analyze all choices`
  — When you select this option, Stateflow analyzes both active and inactive choices for
  incompatibilities in signal attributes and generates code only
  for the active choice.
- `code compile` — When you select this
  option, Stateflow analyzes both active and inactive choices of
  variant transitions and generates code for both the active and
  inactive choices. The choices are enclosed in C preprocessor
  conditional statements #if and #endif that are conditionally
  compiled when you compile the generated code.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `VariantActivationTime` |
| **Values:** | `"update diagram analyze all choices"` (default) | `"code compile"` |

### **Action language** — Action language `MATLAB` (default) | `C`

Action language to use to program the chart, specified as
`MATLAB` or `C`. For more
information, see Differences Between MATLAB and C as Action Language Syntax.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `ActionLanguage` |
| **Values:** | `"MATLAB"` (default) | `"C"` |

### **State machine type** — State machine semantics `Classic` (default) | `Mealy` | `Moore`

State machine semantics implemented by the chart, specified as
`Classic`, `Mealy`, or
`Moore`. For more information, see Overview of Mealy and Moore Machines.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `StateMachineType` |
| **Values:** | `"Classic"` (default) | `"Mealy"` | `"Moore"` |

### Fixed-point properties

### **Treat these inherited Simulink signal types as fi objects** — Inherited Simulink signals to treat as `fi` objects `Fixed-point` (default) | `Fixed-point & Integer`

Inherited Simulink signals to treat as Fixed-Point Designer™
`fi` objects, specified as one of these values:

- `Fixed-point` — The chart treats all
  fixed-point inputs as `fi` objects.
- `Fixed-point & Integer` — The chart
  treats all fixed-point and integer inputs as
  `fi` objects.

#### Dependencies

To enable this parameter, set **Action
language** to
`MATLAB`.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatAsFi` |
| **Values:** | `"Fixed-point"` (default) | `"Fixed-point & Integer"` |

### **MATLAB Chart fimath** — Default `fimath` properties `Same as MATLAB` (default) | `Specify Other`

Default `fimath` properties for the chart, specified as
one of these values:

- `Same as MATLAB` — The chart uses the
  same `fimath` object properties as the
  current default `fimath` object. The text box
  is dimmed and displays the current global
  `fimath` object in read-only form.
- `Specify other` — Specify your own
  `fimath` object in the text box one of
  two ways:

  - Constructing the `fimath` object
    inside the text box.
  - Constructing the `fimath` object in
    the MATLAB or model workspace and then entering
    its variable name in the text box. If you use this
    option and plan to share your model with others,
    define the variable in the model workspace.

For more information, see fimath Object Construction (Fixed-Point Designer).

#### Dependencies

To enable this parameter, set **Action
language** to
`MATLAB`.

#### Programmatic Use

To set the chart parameter value programmatically, access the
`Stateflow.Chart` object
of the chart and change the object property by using dot
notation.

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

**HDL Architecture**

This block has one default HDL architecture.

**Active State Output**

To generate an output port in the HDL code that
shows the active state, in the Properties window of the chart, select **Create
output for monitoring**. The output is an enumerated data type. See Simplify Stateflow Charts by Incorporating Active State Output.

**Registered Output**

To insert an output register that delays the chart output by a simulation
cycle, use the OutputPipeline (HDL Coder) block property.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ClockDrivenOutput** | Enable clock-driven outputs to prevent combinatorial logic from driving the output and to allow an immediate output update when the clock signal and state change. The default is `off`. When you set **ClockDrivenOutput** to `on`, HDL Coder adds an output register that updates when the state updates. The final output variable is then assigned a value from the clock-drive register. This option is available only for Moore charts. |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **GuardIndexVariables** | Specify whether to hoist array indices out of conditional statements or not. When you enable certain optimizations such as RAM Mapping, loop streaming, sharing, and so on, expressions are moved out of the array indices. A temporary variable is created for the expression that might result in an index out-of- bounds error during simulation. The default is `off`. See GuardIndexVariables (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **InstantiateFunctions** | Generate a VHDL® `entity` or Verilog® `module` for each function. The default is `off`. See also InstantiateFunctions (HDL Coder). |
| **LoopOptimization** | Unroll, stream, or do not optimize loops. The default is `none`. See also LoopOptimization (HDL Coder). |
| **MapPersistentVarsToRAM** | Map persistent arrays to RAM. The default is `off`. See also MapPersistentVarsToRAM (HDL Coder). |
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

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

To learn about restrictions of using charts, see Introduction to Stateflow HDL Code Generation (HDL Coder).

When you apply optimizations, the block has these limitations:

- Stateflow Chart that has **State Machine Type**
  property set to `Moore` does not support HDL
  optimizations.
- HDL optimizations are not supported for the Stateflow Chart that has
  **Trigger** port.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

**PLC Block properties**

|  |  |
| --- | --- |
| **UseExternalDefinition** | Suppress block definition in generated code. The default is `Off`. See also UseExternalDefinition (Simulink PLC Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Implicit ordering of transitions and parallel states will be removed

In a future release, the property **User-specified state/transition
execution order** will be removed. This property applies only to charts
that use C as the action language.

- When you enable this property, charts execute transitions and parallel states in the order you created them. You can also manually determine the execution order.
- When you disable this property, charts execute transitions and parallel states according to an implicit order defined by physical position.

  Transitions execute according to:

  1. The hierarchical level of the parent of each transition.
  2. The labels of the transition, in this order:

     1. Labels with events and conditions.
     2. Labels with events.
     3. Labels with conditions.
     4. No label.
  3. The angular surface position of the transition source. The transition with the smallest clock position has the highest priority. For example, a transition with a 2 o'clock position has a higher priority than a transition with a 4 o'clock position. A transition with a 12 o'clock source position has the lowest priority.

  Parallel states execute in this order:

  1. Top to bottom.
  2. Left to right.

To ensure your implicitly ordered charts remain compatible, enable the
**User-specified state/transition execution order**
property.

### R2023b: Convert to state transition table

To convert a chart to a state transition table, use the function `convertToSTT`.

### R2023a: Specify how to treat non-scalar data with dimension of length 1

With the new property **Treat dimensions of length 1 as fixed size**, you can specify
how charts treat non-scalar data when at least one dimension has length 1. Prior to
R2023a, charts treated non-scalar data with at least one dimension of length 1 as
fixed size, regardless of whether you enabled the **Variable size** data
property.

## Description

Implement control logic with finite state machine

The Chart block graphically represents a finite state machine. In a
Stateflow® chart, states and transitions form the basic building blocks of a
sequential modal logic system. States correspond to operating modes and transitions
represents the passage of the system from one operating mode to another. For more
information, see Model a Finite State Machine.

To implement control logic, Stateflow charts can use MATLAB® or C as the action language. For more information, see Differences Between MATLAB and C as Action Language Syntax.
