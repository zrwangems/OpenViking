---
type: simulink-block
title: 'PS Dead Zone'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Nonlinear Operators'
documentation_page: 'psdeadzone'
documentation_source_path: 'ref/psdeadzone.html'
language: en
---

# PS Dead Zone

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

### **Upper limit** — Dead zone upper bound `0.5 1` (default)

The upper limit, or end, of the dead zone.

The parameter unit must be commensurate with the unit of the input signal. You can
select a unit from the drop-down list or type the desired unit name, such as
`rpm`, or a valid expression, such as `rad/s`. For
more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Lower limit** — Dead zone lower bound `-0.5 1` (default)

The lower limit, or start, of the dead zone.

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

Provide region of zero output for physical signals

The PS Dead Zone block generates zero output when input
signal falls within a specified region, called a dead zone. You can specify the lower and
upper limits of the dead zone as block parameters. The block output depends on the input and
dead zone:

- If the input is within the dead zone (greater than the lower limit and less than the
  upper limit), the output is zero.
- If the input is greater than or equal to the upper limit, the output is the input
  minus the upper limit.
- If the input is less than or equal to the lower limit, the output is the input minus
  the lower limit.

Both the input and the output are physical signals. Untyped physical ports facilitate unit
propagation. The output signal has the same physical unit as the input signal.
