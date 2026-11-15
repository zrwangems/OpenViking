---
type: simulink-block
title: 'Test Condition'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Generate Tests / Basics of Test Generation'
documentation_page: 'testcondition'
documentation_source_path: 'ref/testcondition.html'
language: en
---

# Test Condition

## Ports

### Input

### **Port\_1** — Input signal specified as a scalar or cell array scalar | cell array

The Test Condition block accepts signals of
all built-in data types supported
by the Simulink software. For more information about supported data types,
see Data Types Supported by Simulink. The block does not
support complex input signals.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal returned as a scalar or a cell array scalar | cell array

The Test Condition block returns signals of all built-in data types
supported by the Simulink software. For more information about supported data types,
see Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Enable** — Whether block is enabled `on` (default) | `off`

Select this parameter to generate tests for a model. Clearing this option
disables the block. If this option is cleared, the block appears dimmed in
the Simulink Editor.

### **Type** — Whether the block behaves as a Test Condition or Proof Assumption block `Test Condition` (default) | `Assumption`

Specify whether the block behaves as a Test Condition or Proof Assumption
block. Select `Assumption` to transform the Test
Condition block into a Proof Assumption block.

### **Values** — Test condition scalar | cell array

Use the **Values** parameter to constrain signal values
in test cases. Specify any combination
of scalars and intervals in the form of a MATLAB® cell array. For more information, see Set Parameters Using Parameter Configuration File.

Alternatively, you can specify scalar values using the
`Sldv.Point` constructor, which accepts a single value
as its argument. You can also specify intervals using the
`Sldv.Interval` constructor, which requires two input
arguments, one for the lower bound and one for the upper bound for the
interval.

For example, the **Values** parameter

```
{0, [1, 3]}
```

specifies:

- `0` — A scalar
- `[1, 3]` — A closed interval

The **Values** parameter

```
{Sldv.Interval(0, 1, '[)'), Sldv.Point(1)}
```

specifies:

- `Sldv.Interval(0, 1, '[)')`
  — The right-open interval [0, 1)
- `Sldv.Point(1)` — A scalar

If you specify multiple scalars and intervals for a Test Condition block,
the Simulink
Design Verifier™ software combines them using a logical OR operation when
generating test cases. Consequently, the software considers the entire test
condition to be satisfied if
any
single scalar or interval is satisfied.

Within a single scalar or interval, a test condition is generated with a
logical AND operation. In this case, all
signals must satisfy the
constraints in order for the input to satisfy the condition.

For example, consider a two-dimensional open interval:

```
Sldv.Interval([-5 -5],[5 2],'()')
```

The zero vector `[0 0]` satisfies the condition because
the zero elements are within the intervals `-5` to
`5` and `-5` to
`2`.

The vector `[0 3]` does not satisfy the condition because
the second element 3 falls outside the interval `-5` to
`2`.

### **Display values** — Display the contents of values parameter `on` (default) | `off`

Specify whether the block displays the contents of its
**Values** parameter in the Simulink Editor.

### **Pass through style (show Outport)** — Whether block displays an output port in the Simulink Editor `on` (default) | `off`

If selected, the block displays its output port, which allows the input
signal to pass through to the block output. If not selected, the block hides
its output port and terminates the input signal.

**Example:** The following graphics illustrate the appearance of the block in
each case.

**Pass through style: Selected**

**Pass through style: Cleared**

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

Constrain signal values in test cases

The Test Condition block defines test conditions for signals in models that are
operating in test generation mode. (See ). Use the
**Values** parameter to specify constraints on signal values. The
block applies the specified **Values** parameter to its input signal
and attempts to produce test cases.

You can use the block to:

- Enable or disable the condition.
- Specify whether the block should display its **Values**
  parameter in the Simulink® Editor.
- Specify whether the block should display its output port.

When you generate code using Simulink and Simulink
Coder™, the Test Condition block is ignored. The Test Condition block does not
modify the signal during model simulation, and only uses the signal to generate test
conditions.
