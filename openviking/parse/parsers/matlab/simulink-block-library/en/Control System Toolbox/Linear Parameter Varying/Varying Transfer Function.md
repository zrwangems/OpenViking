---
type: simulink-block
title: 'Varying Transfer Function'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingtransferfunction'
documentation_source_path: 'ref/varyingtransferfunction.html'
language: en
---

# Varying Transfer Function

## Ports
```yaml
ports:
- name: u
  summary: Transfer function input scalar
  direction: input
- name: b0, b1, ...
  summary: Numerator coefficients scalar
  direction: input
- name: a1, a2, ...
  summary: Denominator coefficients scalar
  direction: input
- name: y
  summary: Transfer function output scalar
  direction: output
```

### Input

### **u** — Transfer function input scalar

Transfer function input signal.

### **b0, b1, ...** — Numerator coefficients scalar

Transfer function numerator coefficients. The number of coefficient
ports is determined by the **Transfer function order**
parameter.

For a zero-feedthrough transfer
function, clear the **Enable feedthrough** checkbox.
Clearing this checkbox disables the **b0** input
port. *(since R2023a)*

### **a1, a2, ...** — Denominator coefficients scalar

Transfer function denominator coefficients. The number of coefficient
ports is determined by the **Transfer function order**
parameter. The coefficient of the lowest-order term
(*a*0) is fixed to 1.

*Before R2023a: The denominator coefficients
are `a0`, `a1`,…. The coefficient
*a*N is fixed to 1. For more
information, see Varying Transfer Function block formula changed.*
### Output

### **y** — Transfer function output scalar

Transfer function output signal.
## Parameters
```yaml
parameters:
- name: Transfer function order
  summary: Number of poles N 1 (default) | positive integer
  group: ''
- name: Enable feedthrough
  summary: Add input port for feedthrough term on (default) | off
  group: ''
```

### **Transfer function order** — Number of poles N 1 (default) | positive integer

Transfer function order *N*, specified as a positive
integer. This parameter determines the number of coefficient input ports on
the block.

### **Enable feedthrough** — Add input port for feedthrough term `on` (default) | `off`

*Since R2023a*

Enable the **b0** input port for a transfer function with
direct feedthrough. For a zero-feedthrough transfer function, clear this
checkbox. Disabling the port for zero-feedthrough models is numerically more
reliable than feeding a zero-constant into the port.
## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2023a: Varying Transfer Function block formula changed

In R2023a, the Varying Transfer Function block formula was changed
to make the polynomial coefficient definitions consistent with the Discrete
Varying Transfer Function block. Block diagrams to which the block was
added in R2022b or earlier are unaffected by this change.

- A Varying Transfer Function block added to a Simulink® model in R2023a or later has an instantaneous transfer
  function described by:

  H(s)=b0+b1s−1+⋯+bNs−N1+a1s−1+⋯+aNs−N=b0sN+b1sN−1+⋯+bNsN+a1sN−1+⋯+aN.
- A block added in R2022b or before has an instantaneous transfer function
  described by:

  H(s)=b0+b1s+⋯bNsNa0+a1s+⋯aN−1sN−1+sN.

  Note that replacing a pre-R2023a block with the new block requires
  rewiring the coefficient inputs. For instance, consider the following
  second-order transfer function:

  H22b(s)=10+9s+8s27+6s+s2.

  Using a block added in R2022b or before, you wire up the block as shown in
  the following illustration. The block fixes `a2` to
  1.

  R2022b Varying Transfer Function block with Constant blocks wired to the coefficient inputs, b0 = 10, a0 = 7, b1 = 9, a1 = 6, b2 = 8

  To replace the block in R2023a or after, rewrite the transfer function as
  follows:

  H23a(s)=8+9s−1+10s−21+6s−1+7s−2.

  Rewire the block as shown. Now, the block fixes `a0` to
  1.

  R2023a Varying Transfer Function block with Constant blocks wired to the coefficient inputs, b0 = 8, a1 = 6, b1 = 9, a2 = 7, b2 = 10

### R2023a: Enable feedthrough checkbox added

For a zero-feedthrough transfer function, clear the **Enable
feedthrough** checkbox. Clearing this checkbox disables the
**b0** input port. Disabling the port for zero-feedthrough
models is numerically more reliable than feeding a zero-constant into the
port.

## Description

Transfer function with varying coefficients

This block implements a continuous-time transfer function with varying coefficients.
The instantaneous transfer function is given by:

H(s)=b0+b1s−1+⋯+bNs−N1+a1s−1+⋯+aNs−N=b0sN+b1sN−1+⋯+bNsN+a1sN−1+⋯+aN.

*N* is number of poles, specified with the **Transfer
function order** parameter. Feed the values of the coefficients *b*0,
*b*1,…,
*bN* and *a*1,
*a*2,…,
*a**N* to the corresponding block input ports.

**Note**

The above expression for *H*(*s*) applies only
to Varying Transfer Function blocks added to a model in R2023a or
later. For information about Varying Transfer Function blocks created
in R2022b or earlier, see Varying Transfer Function block formula changed.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the transfer-function coefficients depend on the block output
**y**. If you have such dependence, the resulting transfer
function causes an algebraic loop, because computing the block output value requires
knowing the block output value. This algebraic loop is prone to instability and
divergence. Instead of the output, try expressing the coefficients in terms of the
time *t* and the block input **u**.
