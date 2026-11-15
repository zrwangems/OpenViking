---
type: simulink-block
title: 'PS Switch'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Nonlinear Operators'
documentation_page: 'psswitch'
documentation_source_path: 'ref/psswitch.html'
language: en
---

# PS Switch

## Ports

### Input

### **I1** — Input physical signal, untyped physical signal

First input physical signal. This signal is output if the control signal value at
port **I2** is greater than or equal to the
**Threshold** parameter value.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Control physical signal, untyped physical signal

Second input physical signal. This is the control signal for the switch.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I3** — Input physical signal, untyped physical signal

Third input physical signal. This signal is output if the control signal value at
port **I2** is less than the **Threshold** parameter
value.

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

### **Threshold** — Threshold value for opening and closing the switch `0.5 1` (default)

The threshold value for opening and closing the switch. If the control physical
signal, presented at the second (middle) input port **I2**, is greater
than or equal to this value, then the output is connected to the first input. Otherwise,
the output is connected to the third input.

The parameter unit must be commensurate with the unit of the control signal at port
**I2**. You can select a unit from the drop-down list or type the
desired unit name or expression. For more information and a list of unit abbreviations,
see How to Specify Units in Block Dialogs
and Unit Definitions.

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

**Introduced in R2009b**

### R2025a: Optional zero-crossing detection

Starting in R2025a, the block contains the **Enable zero-crossing
detection** check box. Clearing this check box provides the ability to disable
zero-crossing detection and increase simulation speed.

### R2019a: Unit propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Single-pole double-throw switch controlled by external physical signal

The PS Switch block compares the value of the physical
signal presented at the second (middle) input port to the threshold value:

- If the control input value is greater than or equal to the threshold, the output is
  connected to the first input. This is the default connection shown in the block
  icon.
- If the control input value is less than the threshold, the output is connected to the
  third input.

The second (middle) input port is the control port and it never connects to the output.

All the inputs and the output are physical signals. Untyped physical ports facilitate unit
propagation. Physical signals at the first and third input ports must have commensurate units.
The unit at the output port is determined by unit propagation rules. For more information, see
Physical Signal Unit Propagation.
