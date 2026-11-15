---
type: simulink-block
title: 'Proof Objective'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'proofobjective'
documentation_source_path: 'ref/proofobjective.html'
language: en
---

# Proof Objective

## Ports

### Input

### **Values** — Input signal scalar | cell array

The Proof Objective block accepts signals of
all built-in data types supported
by the Simulink software. For a discussion on the data types supported by
the Simulink software, see Data Types Supported by Simulink. The block does not
support complex input signals.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Enable** — Specify whether the block is enabled `on` (default) | `off`

Specify whether the block is enabled. If selected (the default), the
Simulink
Design Verifier software uses the block when proving properties of a model.
Clearing this option disables the block, that is, causes the Simulink
Design Verifier software to behave as if the Proof Objective block did not
exist. If this option is not selected, the block appears grayed out in the
Simulink Editor.

### **Values** — Specify the proof objective scalar | cell array

Specify the proof objective (see Specifying Proof Objectives).

### **Diaplay values** — Display the contents of values parameter `on` (default) | `off`

Specify whether the block displays the contents of its
**Values** parameter in the Simulink Editor. By default, this option is selected.

### **Pass through style** — Specify the proof objective `on` (default) | `off`

Specify whether the block displays an output port in the Simulink Editor. If selected (the default), the block displays its
output port, allowing its input signal to pass through as the block output.
If not selected, the block hides its output port and terminates the input
signal. The following graphics illustrate the appearance of the block in
each case.

**Pass through style: Selected**

**Pass through style: Deselected**

### **Stop simulation when the property is violated** — Specify whether to stop the simulation `on` (default) | `off`

Specify whether to stop the simulation if the simulation encounters a
signal that violates the property specified in the
**Values** parameter.

If you select this parameter and simulate the model, the simulation stops
if it encounters a violation of the specified property.

## Libraries

Simulink Design Verifier / Objectives and Constraints

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

## Version History

**Introduced in R2007a**

## Description

Define objectives that signals must satisfy when proving model properties

When operating in property-proving mode, the Simulink®
Design Verifier™ software proves that properties of your model satisfy specified criteria
(see Prove Model Properties Using Simulink Design Verifier). In this mode, you
can use Proof Objective blocks to define proof objectives for signals in your
model.

The **Values** parameter lets you specify acceptable values for the
block's input signal. If a signal value deviates from the acceptable values in
*any* time step, a property
violation occurs and the proof objective is falsified. The block applies the specified
**Values** parameter to its input signal, and the Simulink
Design Verifier software proves or disproves that the properties of your model satisfy the
specified criteria.

The block's parameter dialog box allows you to

- Enable or disable the objective.
- Specify that the block should display its **Values**
  parameter in the Simulink Editor.
- Specify that the block should display its output port.

**Note**

The Simulink and Simulink
Coder™ software ignore the Proof Objective block during model simulation and
code generation, respectively. The Simulink
Design Verifier software uses the Proof Objective block only when proving model
properties.

### Specifying Proof Objectives

Use the **Values** parameter to define values that a signal must
achieve during a proof simulation. Specify any
combination of scalars and intervals in the form of a MATLAB® cell array. For information about cell arrays, see Cell Arrays.

**Tip**

If the **Values** parameter specifies only one scalar value,
you do not need to enter it in the form of a MATLAB cell array.

Scalar values each comprise a single cell in the array, for example:

```
{0, 5}
```

A closed interval comprises a two-element vector as a cell in the array, where
each element specifies an interval endpoint:

```
{[1, 2]}
```

Alternatively, you can specify scalar values using the
`Sldv.Point` constructor, which accepts a single value as its
argument. You can specify intervals using the `Sldv.Interval`
constructor, which requires two input arguments, i.e., a lower bound and an upper
bound for the interval. Optionally, you can provide one of the following values as a
third input argument that specifies inclusion or exclusion of the interval
endpoints:

- `'()'` — Defines an open interval.
- `'[]'` — Defines a closed interval.
- `'(]'` — Defines a left-open
  interval.
- `'[)'` — Defines a right-open
  interval.

**Note**

By default, `Sldv.Interval` considers an interval to be
closed if you omit its third input argument.

As an example, the **Values** parameter

```
{0, [1, 3]}
```

specifies:

- `0` — a scalar
- `[1, 3]` — a closed interval

The **Values** parameter

```
{Sldv.Interval(0, 1, '[)'), Sldv.Point(1)}
```

specifies:

- `Sldv.Interval(0, 1, '[)')` — the
  right-open interval [0, 1)
- `Sldv.Point(1)` — a scalar

If you specify multiple scalars and intervals for a Proof Objective block, the
Simulink
Design Verifier software combines them using a logical OR operation during the
property proof. In this case, the software considers the entire proof objective to
be satisfied if any single scalar or interval
is satisfied.
