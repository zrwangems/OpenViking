---
type: simulink-block
title: 'PS Asynchronous Sample & Hold'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Discrete'
documentation_page: 'psasynchronoussamplehold'
documentation_source_path: 'ref/psasynchronoussamplehold.html'
language: en
---

# PS Asynchronous Sample & Hold

## Ports
```yaml
ports:
- name: U
  summary: Input physical signal, untyped physical signal
  direction: input
- name: T
  summary: Trigger physical signal, unitless physical signal
  direction: input
- name: Y
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **U** — Input physical signal, untyped physical signal

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **T** — Trigger physical signal, unitless physical signal

Input physical signal that triggers the sample-and-hold action. In the block icon,
this port is marked with the  (rising edge) sign.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **Y** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters:
- name: Initial output
  summary: Output at time zero 0 1 (default)
  group: ''
```

### **Initial output** — Output at time zero `0 1` (default)

The value and unit of the output signal at time zero. The first edit box represents
the signal value. The output of the block remains at this value until the block is
triggered by a rising trigger signal becoming positive.

The second combo box represents the signal unit. By default, the unit is
`1` (unitless). Specify a unit that is commensurate with the signal
unit at the input port **U**. You can select a unit from the drop-down
list or type the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a list of unit
abbreviations, see How to Specify Units in Block Dialogs
and Unit Definitions.
## Libraries

Simscape / Foundation Library / Physical Signals / Discrete

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Output sample-and-hold signal with external trigger

The PS Asynchronous Sample & Hold block sets the output
signal, *Y*, equal to the input signal, *U*, when the rising
edge of the trigger input becomes greater than zero. Use this block, in conjunction with other
physical signal blocks, to model discrete and event-based behaviors.

The Asynchronous PWM Voltage Source example illustrates how
you can use the PS Asynchronous Sample & Hold block to
build components with more complex behaviors. For an alternative discrete-time implementation,
see the Discrete-Time PWM Voltage Source example. The discrete-time
version is better suited to fixed-step solvers and hardware-in-the-loop applications, whereas
the asynchronous implementation is better suited to fast desktop simulation using
variable-step solvers.

The signal unit at the output port is determined by unit propagation rules.
