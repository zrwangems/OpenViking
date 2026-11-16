---
type: simulink-block
title: 'Switch'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'switch'
documentation_source_path: '../simscape/ref/switch.html'
language: en
---

# Switch

## Ports

### Input

### **PS** — Control signal, unitless physical signal

Input physical signal that controls whether the switch is open or closed.
### Conserving

### **p** — Electric terminal electrical

Electrical conserving port associated with one of the switch terminals. The block
has no intrinsic directionality.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **n** — Electric terminal electrical

Electrical conserving port associated with the other switch terminal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **Closed resistance R\_closed** — Resistance of closed switch `0.01 Ohm` (default) | positive scalar

The resistance of the switch when it is closed. The parameter value must be greater
than zero.

### **Open conductance G\_open** — Conductance of open switch `1e-8 1/Ohm` (default) | positive scalar

The conductance of the switch when it is open. The parameter value must be greater
than zero.

### **Threshold** — Threshold value for opening and closing switch `0.5` (default) | unitless scalar

The threshold value for opening and closing the switch. If the external physical
signal at port **PS** is greater than this value, then the switch is
closed, otherwise the switch is open.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Switch controlled by external physical signal

The Switch block models a switch controlled by an external
physical signal. If the external physical signal at port **PS** is greater
than the value specified in the **Threshold** parameter, then the switch is
closed, otherwise the switch is open.

Electrical switches add discontinuities to your model, and therefore your choice of the
solver can influence the model behavior. For detailed information about the solver settings,
see Making Optimal Solver Choices for Physical Simulation.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
