---
type: simulink-block
title: 'Truth Table'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: ''
documentation_page: 'truthtable'
documentation_source_path: 'ref/truthtable.html'
language: en
---

# Truth Table

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

When you create input data in the Stateflow® truth table using the **Symbols** pane,
Stateflow creates a corresponding input port on the Truth
Table block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### Output

### **Port\_1** — Output port scalar | vector | matrix

When you create output data in the Stateflow truth table by using the **Symbols**
pane, Stateflow creates a corresponding output port on the Truth
Table block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

**Note**

Truth Table blocks also have Subsystem (Simulink) block parameters that you
can access by right-clicking the block and clicking **Block Parameters
(Subsystem)**. However, updating these block parameters is not
recommended.

### **Update method** — Method to update or wake up a Stateflow truth table `Inherited` (default) | `Discrete` | `Continuous`

Method to update or wake up a Stateflow truth table, specified as
`Inherited`, `Discrete`,
or `Continuous`.

`Inherited`
:   Input from the Simulink model determines when the truth table wakes up
    during a simulation (default).

    If you define input events for the truth table, the
    Stateflow truth table is explicitly triggered by a signal on
    its trigger port originating from a connected Simulink block. You can set this trigger input event to
    occur in response to a Simulink signal. The Simulink signal can be `Rising`, `Falling`, or `Either` (rising and falling), or in response
    to a `Function Call`. For
    more information, see Activate a Stateflow Chart by Sending Input Events.

    If you do not define input events, the Stateflow truth table implicitly inherits triggers from the
    Stateflow model. These implicit events are the discrete or
    continuous sample times of the Stateflow signals providing inputs to the truth table. If
    you define data inputs, the truth table awakens at the rate of
    the fastest data input. If you do not define any data input for
    the truth table, the truth table wakes up as defined by the
    execution behavior of its parent subsystem.

`Discrete`
:   The Simulink model generates an implicit event at regular time
    intervals to awaken the Stateflow truth table at the rate that you specify in the
    **Sample Time** truth table parameter.
    Other blocks in the Simulink model can have different sample times.

`Continuous`
:   The Stateflow truth table updates its state during major time
    steps only, although it computes outputs and local continuous
    variables during major and minor time steps. For more
    information, see Continuous-Time Modeling in Stateflow.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.TruthTableChart` object of the block and change
the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **Values:** | `"INHERITED"` (default) | `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — Time interval that a Stateflow truth table wakes up during simulation `-1` (default) | scalar | vector

Time interval that a truth table wakes up during simulation, specified by
a scalar or a vector. The default time interval is `-1`,
which indicates that the Stateflow truth table inherits the sample time from Simulink.

Do not use the **Sample Time** parameter in the
Subsystem block parameters. Instead, use the
Property Inspector.

#### Dependencies

To enable this parameter, set **Update method** to
`Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the `Stateflow.TruthTableChart` object of the block and change
the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | string scalar | character vector |
| **Data Types:** | `string` | `char` |

### Advanced

### **Saturate on integer overflow** — Whether data saturates on integer overflow `on` (default) | `off`

Whether the data in the truth table saturates on
integer overflow. When you clear this parameter, the
data in the truth table wraps on integer overflow.
For more information, see Handle Integer and Enumeration Overflow for Chart Data.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.TruthTableChart` object of the block and
change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Support variable-size arrays** — Whether the truth table supports variable size data `on` (default) | `off`

Whether the truth table supports variable-size data. For more
information, see Declare Variable-Size Data in Stateflow Charts.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.TruthTableChart` object of the block and
change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SupportVariableSizing` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Treat dimensions of length 1 as fixed size** — Whether truth table treats non-scalar data with dimension of length 1 as fixed size `on` (default) | `off`

*Since R2023a*

Whether the truth table treats non-scalar data with a dimension of
length 1 as fixed size. When you select this parameter, the truth table
treats non-scalar data that have at least one dimension of length 1 as
fixed size, regardless of whether you enable the **Variable
size** data property. When you clear this parameter,
the truth table treats non-scalar data with the **Variable
size** property enabled as variable size.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.TruthTableChart` object of the block and
change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Overspecification** — Level of diagnostic when truth table is overspecified `"Error"` (default) | `"Warning"` | `"None"`

Level of diagnostic action when the truth table is overspecified,
specified as `"Error"`, `"Warning"`,
or `"None"`. For more information, see Correct Overspecified and Underspecified Truth Tables.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.TruthTableChart` object of the block and
change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `OverSpecDiagnostic` |
| **Values:** | `"Error"` (default) | `"Warning"` | `"None"` |

### Fixed-point properties

### **Treat these inherited Simulink signal types as fi objects** — Inherited Simulink signals to treat as `fi` objects `Fixed-point` (default) | `Fixed-point & Integer`

Inherited Simulink signals to treat as Fixed-Point Designer™
`fi` objects, specified as one of these values:

- `Fixed-point` — The truth table treats
  all fixed-point inputs as `fi`
  objects.
- `Fixed-point & Integer` — The truth
  table treats all fixed-point and integer inputs as
  `fi` objects.

This parameter applies only to truth tables that use
MATLAB as the action language.

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.TruthTableChart` object of the block and
change the object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatAsFi` |
| **Values:** | `"Fixed-point"` (default) | `"Fixed-point & Integer"` |

### **MATLAB Chart fimath** — Default `fimath` object properties `Same as MATLAB` (default) | `Specify Other`

Default `fimath` object properties for the truth table,
specified as one of these values:

- `Same as MATLAB` — The truth table uses
  the same `fimath` object properties as the
  current default `fimath` object. The text box
  is dimmed and displays the current global
  `fimath` object in read-only form.
- `Specify other` — Specify your own
  `fimath` object in the text box.

For more information, see fimath Object Construction (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, access the
`Stateflow.TruthTableChart` object of the block and
change the object property by using dot notation.

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

You can use a tunable parameter in a Truth Table block intended
for HDL code generation. For details, see Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

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

- HDL optimizations are not supported for the block that has
  **Trigger** port.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023a: Specify how to treat non-scalar data with dimension of length 1

With the new parameter **Treat
dimensions of length 1 as fixed size**, you can specify how truth
tables treat non-scalar data when at least one dimension has length 1. Prior to
R2023a, truth tables treated non-scalar data with at least one dimension of length 1
as fixed size, regardless of whether you enabled the **Variable size** data
property.

## Description

Represent logical decision-making behavior with conditions, decisions, and actions

The Truth Table block represents combinatorial logic design in a
tabular format. You can use truth table blocks to model decision making behavior based
on a set of conditions. For more information, see Use Truth Tables to Model Combinatorial Logic.

To implement control logic, Truth Table blocks use MATLAB® as the action language.
