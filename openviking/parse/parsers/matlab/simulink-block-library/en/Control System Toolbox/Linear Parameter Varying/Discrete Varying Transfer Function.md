---
type: simulink-block
title: 'Discrete Varying Transfer Function'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingtransferfunction'
documentation_source_path: 'ref/discretevaryingtransferfunction.html'
language: en
---

# Discrete Varying Transfer Function

## Ports

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
parameter.
### Output

### **y** — Transfer function output scalar

Transfer function output signal.

## Parameters

### **Transfer function order** — Number of poles 1 (default) | positive integer

Transfer function (number of poles), specified as a positive integer. This
parameter determines the number of coefficient input ports on the
block.

### **Enable feedthrough** — Add input port for feedthrough term `on` (default) | `off`

*Since R2023a*

Enable the **b0** input port for a transfer function with
direct feedthrough. For a zero-feedthrough transfer function, clear this
checkbox. Disabling the port for zero-feedthrough models is numerically more
reliable than feeding a zero-constant into the port.

### **Sample time (-1 for inherited)** — Block sample time –1 (default) | positive scalar

Block sample time, specified as either –1 (inherited sample time) or a
positive scalar value.

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2017b**

### R2023a: Enable feedthrough checkbox added

For a zero-feedthrough transfer function, clear the **Enable
feedthrough** checkbox. Clearing this checkbox disables the
**b0** input port. Disabling the port for zero-feedthrough
models is numerically more reliable than feeding a zero-constant into the
port.

## Description

Discrete-time transfer function with varying coefficients

This block implements a discrete-time transfer function with varying coefficients. The
instantaneous transfer function is given by:

H(z)=b0+b1/z+⋯+bN/zN1+a1/z+⋯+aN/zN,

where *N* is number of poles, specified with the **Transfer
function order** parameter. Feed the values of the coefficients *a*1, …,
*aN* and *b*0,
*b*1, …,
*bN* to the corresponding block input ports.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the transfer-function coefficients depend on the block output
**y**. If you have such dependence, the resulting transfer
function causes an algebraic loop, because computing the block output value
requires knowing the block output value. This algebraic loop is prone to instability
and divergence. Instead, try expressing the coefficients in terms of the time
*t* and the block input **u**.
