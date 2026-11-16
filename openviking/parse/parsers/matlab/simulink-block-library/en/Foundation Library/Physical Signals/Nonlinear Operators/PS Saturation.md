---
type: simulink-block
title: 'PS Saturation'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'pssaturation'
documentation_source_path: 'ref/pssaturation.html'
language: en
---

# PS Saturation

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

### **Upper limit** — Signal upper bound `0.5 1` (default)

The upper bound on the input signal. When the input signal to the PS
Saturation block is above this value, the output of the block is
clipped to this value.

The parameter unit must be commensurate with the unit of the input signal. You can
select a unit from the drop-down list or type the desired unit name, such as
`rpm`, or a valid expression, such as `rad/s`. For
more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Lower limit** — Signal lower bound `-0.5 1` (default)

The lower bound on the input signal. When the input signal to the PS
Saturation block is below this value, the output of the block is
clipped to this value.

The parameter unit must be commensurate with the unit of the input signal. You can
select a unit from the drop-down list or type the desired unit name, such as
`rpm`, or a valid expression, such as `rad/s`. For
more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Enable zero-crossing detection** — Whether to enable zero-crossing detection `on` (default) | `off`

Clear to disable zero-crossing detection and increase simulation speed. For more
information, see Managing Zero Crossings in Simscape Models.

## Libraries

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2025a: Optional zero-crossing detection

Starting in R2025a, the block contains the **Enable zero-crossing
detection** check box. Clearing this check box provides the ability to disable
zero-crossing detection and increase simulation speed.

### R2019a: Unit propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Limit range of physical signal

The PS Saturation block imposes upper and lower bounds on a
physical signal. When the input signal is within the range specified by the **Lower
limit** and **Upper limit** parameters, the input signal passes
through unchanged. When the input signal is outside these bounds, the signal is clipped to the
upper or lower bound.

When the **Lower limit** and **Upper limit** parameters
are set to the same value, the block outputs that value.

Both the input and the output are physical signals. Untyped physical ports facilitate unit
propagation. The output signal has the same physical unit as the input signal.
