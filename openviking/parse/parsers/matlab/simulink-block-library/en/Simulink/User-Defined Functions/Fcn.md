---
type: simulink-block
title: 'Fcn'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'fcn'
documentation_source_path: 'slref/fcn.html'
language: en
---

# Fcn

## Ports
```yaml
ports:
- name: In
  summary: Input to a Fcn block scalar | vector
  direction: input
  data_types: single | double
- name: Out
  summary: Output from a Fcn block scalar
  direction: output
  data_types: single | double
```

### Input

### **In** — Input to a Fcn block scalar | vector

The Fcn block accepts and outputs signals of type
`single` or `double`.

For more information, see Data Types Supported by Simulink in the Simulink® documentation.

**Data Types:** `single` | `double`
### Output

### **Out** — Output from a Fcn block scalar

The Fcn block accepts and outputs signals of type
`single` or `double`.

For more information, see Data Types Supported by Simulink in the Simulink documentation.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Expression
  summary: Specify the mathematical expression mathematical expression
  group: ''
  block_parameter: Expr
  type: character vector
  values: mathematical expression
  default: '''sin(u(1)*exp(2.3*(-u(2))))'''
- name: Sample time
  summary: Specify sample time in the block scalar
  group: ''
```

### **Expression** — Specify the mathematical expression mathematical expression

Specify the mathematical expression to apply to the input. Expression
components are listed above. The expression must be mathematically
well-formed (uses matched parentheses, proper number of function arguments,
and so on). The expression has restrictions on tunability (see Limitations).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Expr` |
| **Type:** character vector |
| **Value:** mathematical expression |
| **Default:** `'sin(u(1)*exp(2.3*(-u(2))))'` |

### **Sample time** — Specify sample time in the block scalar

**Note**

This parameter is not visible in the block dialog box unless it is explicitly set
to a value other than `-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.
## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |

**HDL Block Properties**

| General | |
| --- | --- |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

## Version History

**Introduced before R2006a**

### R2023a: Fcn Block Restored to User-Defined Library

The Fcn block has been restored to the **Simulink** > **User-Defined** library.

## Description

Apply specified expression to input

The Fcn block applies the specified mathematical expression to its input.
The expression can include one or more of these components:

- `u` — The input to the block. If `u`
  is a vector, `u(i)` represents the *i*th
  element of the vector; `u(1)` or `u` alone
  represents the first element.
- Numeric constants.
- Arithmetic operators (+ - `*` / ^).
- Relational operators (`== != > < >= <=`) —
  The expression returns 1 if the relation is true; otherwise, it returns
  0.
- Logical operators (&& || !) — The expression returns 1 if the
  relation is true; otherwise, it returns 0.
- Parentheses.
- Mathematical functions — `abs`,
  `acos`, `asin`, `atan`,
  `atan2`, `ceil`, `cos`,
  `cosh`, `exp`, `floor`,
  `hypot`, `log`, `log10`,
  `power`, `rem`, `sgn`
  (equivalent to `sign` in MATLAB®), `sin`, `sinh`,
  `sqrt`, `tan`, and
  `tanh`.

  **Note**

  The Fcn block does not support `round` and
  `fix`. Use the Rounding Function block
  to apply these rounding modes.
- Workspace variables — Variable names that are not recognized in the
  preceding list of items are passed to MATLAB for evaluation. Matrix or vector elements must be specifically
  referenced. For example, use `A(1,1)` instead of
  `A` for the first element in the matrix.

The Fcn block observes these rules of operator precedence:

1. `( )`
2. `^`
3. `+ -` (unary)
4. `!`
5. `* /`
6. `+ -`
7. `> < <= >=`
8. `== !=`
9. `&&`
10. `||`

The expression differs from a MATLAB expression in that the expression cannot perform matrix computations.
Also, this block does not support the colon operator (`:`).

Block input can be a scalar or vector. The output is always a scalar. For vector
output, consider using the Math Function block. If a block input is
a vector and the function operates on input elements individually (for example, the
`sin` function), the block operates on only the first vector
element.
