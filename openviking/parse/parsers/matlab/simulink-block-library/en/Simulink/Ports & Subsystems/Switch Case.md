---
type: simulink-block
title: 'Switch Case'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'switchcase'
documentation_source_path: 'slref/switchcase.html'
language: en
---

# Switch Case

## Ports

### Input

### **u1 (logical operator)** — Value for case selection scalar

Input to the port labeled **u1** of a Switch
Case block can be:

- A scalar value with a built-in data type that Simulink supports. However, the Switch Case
  block does not support Boolean or fixed-point data types, and it
  truncates numeric inputs to 32-bit signed integers.
- A scalar value of any enumerated data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `enumerated`
### Output

### **case** — Action signal for a Switch Case Action Subsystem block scalar

Output from the **Case** and
**default** ports are action signals connected to
Switch Case Action Subsystem blocks.

## Parameters

### **Case conditions** — Specify case values `{1}` (default) | list of cases

Specify the cases values using MATLAB® cell notation.

{1}
:   Specify the output port labeled
    `case[1]`outputs an action signal when the
    input port value is `1`.

list of ports with case assignments
:   Specify multiple cases and ports using MATLAB cell notation. For example, entering
    `{1,[7,9,4]}` specifies that output port
    `case[1]` is run when the input value is
    `1`, and output port `case [7 9
    4]` is run when the input value is
    `7`, `9`, or
    `4`.

    You can use colon notation to specify a range of integer case
    conditions. For example, entering `{[1:5]}`
    specifies that output port **case[1 2 3 4 5]**
    is run when the input value is `1`,
    `2`, `3`,
    `4`, or `5`.

    Depending on block size, cases from a long list of case
    conditions are displayed in shortened form on the face of the
    Switch Case block, using a terminating
    ellipsis (...).

    You can use the name of an enumerated type to specify case
    conditions that include a case for every value in that
    enumerated type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CaseConditions` |
| **Type**: character vector |
| **Values**: `'{1}'` | list of cases in quotes |
| **Default**: `'{1}'` |

### **Show default case** — Control display of default output port `on` (default) | `off`

Control display of default output port.

on
:   Display default output port as the last case on the
    Switch Case block. This allows you to specify
    a default case that executes when the input value does not match
    any of the other case values.

off
:   Hide default output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowDefaultCase` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Control zero-crossing detection.

on
:   Detect zero crossings.

off
:   Do not detect zero crossings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Code generation not supported when this block is used inside a For Each
Subsystem block.

## Version History

**Introduced before R2006a**

## Description

Select subsystem execution using logic similar to switch statement

The Switch Case block with
Switch
Case Action Subsystem blocks containing
Action
Port blocks, implements switch logic to control subsystem execution. For an
example that uses the Switch Case block, see Select Subsystem Execution.

Model ex\_switch\_case\_block

A Switch Case block has a single input. To select a case, define the
input value using the **Case conditions** parameter. The cases are evaluated
top down starting with the first case.

Each case is associated with an output port that is attached to a Switch Case
Action Subsystem block. When a case is selected, the associated output port
sends an action signal to execute the subsystem.

A `default` case is selected after all of the other case conditions
evaluate to false. Providing a `default` case is optional, even if the
other case conditions do not exhaust every possible input value.

Cases for the Switch Case block contain an implied break after a
Switch Case Action Subsystem block is executed. Therefore, there is
no fall through behavior for the Simulink®
Switch Case block as found in standard C `switch`
statements.
