---
type: simulink-block
title: 'S-R Flip-Flop'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'srflipflop'
documentation_source_path: '../simulink/ref_extras/srflipflop.html'
language: en
---

# S-R Flip-Flop

## Ports
```yaml
ports:
- name: S
  summary: Set input scalar
  direction: input
  data_types: double | Boolean
- name: R
  summary: Reset input scalar
  direction: input
  data_types: double | Boolean
- name: Q
  summary: Output signal Q scalar
  direction: output
  data_types: double | Boolean
- name: '!Q'
  summary: Output signal !Q scalar
  direction: output
  data_types: double | Boolean
```

### Input

### **S** — Set input scalar

*Set* input, specified as a scalar, vector, or
matrix.

#### Dependencies

The data types that the S-R Flip-Flop block accepts
depend on the setting of the **Implement logic signals as
boolean data (vs. double)** configuration
parameter:

- `On` — S-R Flip-Flop block
  accepts only real scalar signals of type
  `boolean`.
- `Off` — S-R Flip-Flop
  block accepts real scalar signals of type
  `boolean` or `double`
  (both inputs must have the same type).

**Data Types:** `double` | `Boolean`

### **R** — Reset input scalar

*Reset* input, specified as a scalar, vector, or
matrix.

#### Dependencies

The data types that the S-R Flip-Flop block accepts
depend on the setting of the **Implement logic signals as
boolean data (vs. double)** configuration
parameter:

- `On` — S-R Flip-Flop block
  accepts only real scalar signals of type
  `boolean`
- `Off` — S-R Flip-Flop
  block accepts real scalar signals of type
  `boolean` or `double`
  (both inputs must have the same type).

**Data Types:** `double` | `Boolean`
### Output

### **Q** — Output signal Q scalar

Output signal **Q**, with the same dimensions and
data type as the input.

**Data Types:** `double` | `Boolean`

### **!Q** — Output signal !Q scalar

Output signal **!Q**, with the same dimensions and
data type as the input.

**Data Types:** `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Initial condition (state of Q)
  summary: Initial value of output Q 0 (default) | scalar
  group: ''
  block_parameter: initial_condition
  type: character vector
  values: scalar
  default: '''0'''
```

### **Initial condition (state of Q)** — Initial value of output Q `0` (default) | scalar

Specify the initial value of the output **Q**. A nonzero
value is treated as true (`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `initial_condition` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |
## Libraries

Simulink Extras / Flip Flops

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2008b**

## Description

Model an S-R flip-flop

The S-R Flip-Flop block models a simple Set-Reset flip-flop constructed using
NOR gates.

The S-R Flip-Flop block has two inputs, **S** and
**R** (**S** stands for Set and
**R** stands for Reset) and two outputs, **Q** and
its complement, **!Q**.

The truth table for the S-R Flip-Flop block follows. In this truth
table, **Q**n-1 is the output at the previous
time step.

**Note**

The S-R Flip-Flop block treats a nonzero input as true
(`1`).

| S | R | Q n | !Q n |
| --- | --- | --- | --- |
| 0 | 0 | Q n-1 | !Q n-1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

When **S** is 1 and **R** is 0, the flip-flop goes to the
set state (**Q**n is 1). When
**R** is 1 and **S** is 0, the flip-flop goes to
the reset state (**Q**n is 0). When both
**S** and **R** are 0, the flip-flop stays in the
previous state (**Q**n is
**Q**n-1).

**Tip**

Avoid the state where **R** and **S** are both
1. In this state, both **Q** and **!Q** are 0.
This state is undefined because **!Q** is not the complement of
**Q**. To handle this state, consider the J-K Flip-Flop block.

### Logic Signals as Boolean or Double Data Types

The **Implement logic signals as boolean data (vs. double)**
configuration parameter setting affects the input and output data types of the
S-R Flip-Flop block because this block is a masked subsystem that
uses the Combinatorial Logic block. For more
information about this configuration parameter, see Implement logic signals as Boolean data (vs. double).
