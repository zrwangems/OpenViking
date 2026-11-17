---
type: simulink-block
title: 'Transfer Fcn'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Linear'
documentation_page: 'transferfcn'
documentation_source_path: 'slref/transferfcn.html'
language: en
---

# Transfer Fcn

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar
  direction: input
  data_types: double
- name: Port_1
  summary: Output signal scalar | vector
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Input signal scalar

Input signal, specified as a scalar with data type
`double`.

This port has direct feedthrough only when the numerator of the
transfer function is `0`.

**Data Types:** `double`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal, provided as a scalar or vector with data type
`double`.

- For a single-output system, the input and output of the block
  are scalar time-domain signals.
- For a multiple-output system, the input is a scalar, and the
  output is a vector, where each element is an output of the
  system.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Numerator coefficients
  summary: Vector or matrix of numerator coefficients [1] (default) | vector | matrix
  group: ''
  block_parameter: Numerator
  type: character vector, string
  values: vector | matrix
  default: '''[1]'''
- name: Denominator coefficients
  summary: Row vector of denominator coefficients [1 1] (default) | vector
  group: ''
  block_parameter: Denominator
  type: character vector | string
  values: vector
  default: '''[1 1]'''
- name: Parameter tunability
  summary: Tunable representation of block parameters in code Auto (default) | Optimized | Unconstrained
  group: ''
  block_parameter: ParameterTunability
  type: character vector, string
  values: '''Auto'' | ''Optimized'' | ''Unconstrained'''
  default: '''Auto'''
- name: Absolute tolerance
  summary: Absolute tolerance for computing block states auto (default) | scalar | vector
  group: ''
  block_parameter: AbsoluteTolerance
  values: '''auto'' (default) | ''-1'' | positive real scalar number | vector of positive real scalar numbers'
- name: State Name (e.g., 'position')
  summary: Option to assign unique names to states '' (default) | character vector | cell array of character vectors | MATLAB®
    variable | ...
  group: ''
  block_parameter: ContinuousStateAttributes
  values: ''''' (default) | valid MATLAB variable name'
```

### **Numerator coefficients** — Vector or matrix of numerator coefficients `[1]` (default) | vector | matrix

Define the numerator coefficients of the transfer function.

- For a single-output system, enter a vector for the numerator
  coefficients of the transfer function.
- For a multiple-output system, enter a matrix. Each row of this
  matrix contains the numerator coefficients of a transfer
  function that determines one of the block outputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Numerator` |
| **Type:** character vector, string |
| **Values:** vector | matrix |
| **Default:** `'[1]'` |

### **Denominator coefficients** — Row vector of denominator coefficients `[1 1]` (default) | vector

Define the row vector of denominator coefficients.

- For a single-output system, enter a vector for the denominator
  coefficients of the transfer function.
- For a multiple-output system, enter a vector containing the
  denominator coefficients common to all transfer functions of the
  system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector | string |
| **Values:** vector |
| **Default:** `'[1 1]'` |

### **Parameter tunability** — Tunable representation of block parameters in code `Auto` (default) | `Optimized` | `Unconstrained`

Tunability level of the numerator and denominator coefficients for
Accelerated simulation modes and deployed simulations using Simulink
Compiler™. Set this parameter to `Auto` to
allow Simulink to choose the appropriate level of parameter tunability.

Set this parameter to `Optimized` to generate a
representation of numerator and denominator coefficients in generated code
for accelerated and deployed simulations that is optimized for better
simulation performance.

Set this parameter to `Unconstrained` to generate a fully
tunable (between simulations) representation of the numerator and
denominator coefficients in the generated code for accelerated and deployed
simulations. To let Simulink determine the appropriate tunability level, select
`Auto`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ParameterTunability` |
| **Type:** character vector, string |
| **Values:** `'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **Default:** `'Auto'` |

### **Absolute tolerance** — Absolute tolerance for computing block states `auto` (default) | scalar | vector

Variable-step solvers use absolute and relative tolerances when choosing the step size to
determine whether the error in state calculations is acceptable.

To inherit the absolute tolerance from the **Absolute tolerance** configuration parameter, specify this parameter
value as `auto` or `-1`.

To specify an absolute tolerance for this block that overrides the value specified for
the **Absolute tolerance** configuration parameter:

- Enter a real, positive scalar value to use to compute all block
  states.
- Enter a real vector with dimensions that match the dimensions of the
  continuous states for the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AbsoluteTolerance` |
| **Values:** | `'auto'` (default) | `'-1'` | positive real scalar number | vector of positive real scalar numbers |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",AbsoluteTolerance="-1")`

### **State Name (e.g., 'position')** — Option to assign unique names to states `''` (default) | character vector | cell array of character vectors | MATLAB® variable | ...

Use this parameter to optionally assign names to the states of this block. The
names you assign apply only to the states of this block.

- To use default state names, leave this field blank
  (`''`).
- To assign a single name to a single state, enter the
  name between quotes. For example, to name a single
  state `position`, enter
  `'position'`.
- To assign names to multiple states, specify this
  parameter value as a cell array of character
  vectors. Each name in the cell array must be unique.
  For example, to assign the names
  `a`, `b`, and
  `c`, enter
  `{'a','b','c'}`.
- To specify the names using a MATLAB variable, enter the name of the
  variable without quotes. For example, to use the
  variable `names` to specify the
  state names, enter `names`.

You can specify a number of names that is less than the number of states in
the block. In this case, the state names are used for multiple states, and
the number of states must divide evenly into the number of state names. For
example, when you specify two names for a block that has four states, the
first name is used for the first two states, and the second name is used for
the last two states.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ContinuousStateAttributes` |
| **Values:** | `''` (default) | valid MATLAB variable name |
| **Data Types:** | `char` | `string` | `cell` |

**Example:** `set_param("MyModel/Descriptor
State-Space",ContinuousStateAttributes={'position','velocity'})`
## Libraries

Simulink / Continuous

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and
restrictions on speed and memory often found in embedded systems. The code generated
can contain dynamic allocation and freeing of memory, recursion, additional memory
overhead, and widely-varying execution times. While the code is functionally valid
and generally acceptable in resource-rich environments, smaller embedded targets
often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into
discrete equivalents that support production code generation. To start the Model
Discretizer, in the Simulink Editor, on the **Apps** tab, under
**Apps**, under **Control Systems**, click
**Model Discretizer**. One exception is the
Second-Order Integrator block because, for this block, the Model
Discretizer produces an approximate discretization.

## Version History

**Introduced before R2006a**

## Description

Model linear system as transfer function

The Transfer Fcn block models a linear system by a transfer function of the
Laplace-domain variable *`s`*. The block can model single-input
single-output (SISO) and single-input multiple-output (SIMO) systems.

### Conditions for Using This Block

The Transfer Fcn block assumes the following conditions:

- The transfer function has the form

  H(s)=y(s)u(s)=num(s)den(s)=num(1)snn−1+num(2)snn−2+…+num(nn)den(1)snd−1+den(2)snd−2+…+den(nd),

  where *u* and *y* are the system input and outputs,
  respectively, *nn* and *nd* are the number
  of numerator and denominator coefficients, respectively.
  *num(s)* and *den(s)* contain the
  coefficients of the numerator and denominator in descending powers of
  *s*.
- The order of the denominator must be greater than or equal to the order of the numerator.
- For a multiple-output system, all transfer functions have the same denominator and all numerators have the same order.

### Modeling a Single-Output System

For a single-output system, the input and output of the block are scalar time-domain signals. To model this system:

1. Enter a vector for the numerator coefficients of the
   transfer function in the **Numerator coefficients** field.
2. Enter a vector for the denominator coefficients of
   the transfer function in the **Denominator coefficients** field.

### Modeling a Multiple-Output System

For a multiple-output system, the block input is a scalar and the output is a vector, where each element is an output of the system. To model this system:

1. Enter a matrix in the **Numerator coefficients** field.

   Each *row* of this matrix contains the numerator coefficients of a transfer function that determines one of the block outputs.
2. Enter a vector of the denominator coefficients common
   to all transfer functions of the system in the **Denominator coefficients** field.

### Specifying Initial Conditions

A transfer function describes the relationship between input and output in Laplace
(frequency) domain. Specifically, it is defined as the Laplace transform of the
response (output) of a system with zero initial conditions to an impulse input.

Operations like multiplication and division of transfer functions rely on zero initial state. For example, you can decompose a single complicated transfer function into a series of simpler transfer functions. Apply them sequentially to get a response equivalent to that of the original transfer function. This will not be correct if one of the transfer functions assumes a non-zero initial state. Furthermore, a transfer function has infinitely many time domain realizations, most of whose states do not have any physical meaning.

For these reasons, Simulink® presets the initial conditions of the Transfer Fcn
block to zero. To specify initial conditions for a given transfer function, convert
the transfer function to its controllable, canonical state-space realization using
`tf2ss`. Then, use the State-Space block. The
`tf2ss` utility provides the `A`,
`B`, `C`, and `D` matrices
for the system.

For more information, type `help tf2ss` or
see the Control System Toolbox™ documentation.

### Transfer Function Display on the Block

The Transfer Fcn block displays the transfer function depending on how you
specify the numerator and denominator parameters.

- If you specify each parameter as an expression or a vector, the block
  shows the transfer function using the specified coefficients for the powers
  of *s*. If you specify a variable in parentheses, the
  block evaluates the variable.

  For example, if you specify the **Numerator
  coefficients** parameter value as `[3 2 1]`
  and the **Denominator coefficients** parameter value as
  `(den)`, where `den` is a workspace
  variable with a value of `[7 5 3 1]`, the block displays
  the equation using the specified values.

  Transfer Fcn block that displays the numerator and denominator of the transfer function both as a polynomial function of s.

  **Tip**

  When the block size is too small to accommodate the full numerator or
  denominator, the block icon displays the numerator as
  `num(s)` and the denominator as
  `den(s)`.

  A Transfer Fcn block that is not wide enough to display the equation.

  If you want the block to show the equation for the transfer function
  it implements, resize the block by dragging a corner.

  A pointer is positioned to drag the lower-right corner of the Transfer Fcn block, resizing the block so it is wide enough to display the equation that represents the transfer function.
- If you specify each parameter as a variable, the block
  shows the variable name followed by `(s)`.

  For example, if you specify the **Numerator coefficients** parameter as
  `num` and the **Denominator
  coefficients** parameter as `den`, the block
  icon shows the numerator of the transfer function as
  `num(s)` and the denominator as
  `den(s)`.

  Transfer Fcn block with the Numerator coefficients parameter specified as num and the Denominator coefficients parameter specified as den.
