---
type: simulink-block
title: 'PS Constant'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Sources'
documentation_page: 'psconstant'
documentation_source_path: 'ref/psconstant.html'
language: en
---

# PS Constant

## Ports

### Output

### **O** — Output physical signal, typed by the block parameter value physical signal

Output physical signal. The signal value and unit are determined by the value and
unit of the **Constant** parameter.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **Constant** — Signal value and unit `1 1` (default)

The value and unit of the output signal at port **O**. The first
edit box represents the signal value. You can specify both positive and negative
values.

The second combo box represents the unit of the output signal. By default, the unit
is `1` (unitless). You can select a unit from the drop-down list or
type the desired unit name, such as `rpm`, or a valid expression, such
as `rad/s`. For more information and a list of unit abbreviations, see
How to Specify Units in Block Dialogs
and Unit Definitions.

## Libraries

Simscape / Foundation Library / Physical Signals / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Generate constant physical signal

The PS Constant block generates a physical signal of a
constant value. You specify the value and unit of the signal as the
**Constant** parameter.
