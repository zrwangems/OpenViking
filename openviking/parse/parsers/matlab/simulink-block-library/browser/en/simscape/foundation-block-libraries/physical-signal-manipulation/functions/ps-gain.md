---
type: simulink-block
title: 'PS Gain'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Functions'
documentation_page: 'psgain'
documentation_source_path: 'ref/psgain.html'
language: en
---

# PS Gain

## Ports

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **Gain** — Multiplication coefficient `1 1` (default)

The multiplication coefficient. The first edit box represents the value of the
coefficient. You can specify both positive and negative values.

The second combo box represents the unit of the multiplication coefficient. By
default, the unit is `1` (unitless), which means that the output signal
at port **O** has the same unit as the input signal. If you specify a
different unit for the **Gain** parameter, then the signal unit at the
output port **O** is the input signal unit multiplied by the unit of
the **Gain** parameter. You can select a unit from the drop-down list
or type the desired unit name, such as `rpm`, or a valid expression,
such as `rad/s`. For more information and a list of unit abbreviations,
see How to Specify Units in Block Dialogs
and Unit Definitions.

## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Multiply input physical signal by constant

The PS Gain block performs element-wise multiplication of
the input physical signal by a constant value (gain). You specify the gain as the
**Gain** parameter value and unit.

The input signal value is multiplied by the value of the **Gain**
parameter.

The signal unit at the output port is determined by unit propagation rules. For example,
if the input signal is in `N` and the **Gain** parameter
unit is `m`, then the output physical signal has the unit of
`N*m`. For more information, see Physical Signal Unit Propagation.
