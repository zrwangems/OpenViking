---
type: simulink-block
title: 'RLC (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / RLC Assemblies'
documentation_page: 'rlcthreephase'
documentation_source_path: 'ref/rlcthreephase.html'
language: en
---

# RLC (Three-Phase)

## Ports

### Conserving

### **~1** — Three-phase port electrical

Composite three-phase port.

For more information about composite and expanded three-phase ports,
see Three-Phase Ports.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **~2** — Three-phase port electrical

Composite three-phase port.

For more information about composite and expanded three-phase ports,
see Three-Phase Ports.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a1** — *a*-phase electrical

Electrical conserving port associated with the
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b1** — *b*-phase electrical

Electrical conserving port associated with the
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c1** — *c*-phase electrical

Electrical conserving port associated with the
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **a2** — *a*-phase electrical

Electrical conserving port associated with the
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b2** — *b*-phase electrical

Electrical conserving port associated with the
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c2** — *c*-phase electrical

Electrical conserving port associated with the
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

## Parameters

### Main

### **Electrical connection** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

*Since R2024b*

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical
conserving ports with a single block port. You can use composite
three-phase ports to build models that correspond to single-line
diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a
three-phase system using three separate electrical conserving
ports.

### **Component structure** — Desired component combination `R` (default) | `L` | `C` | `Series RL` | `Series RC` | `Series LC` | `Series RLC` | `Parallel RL` | `Parallel RC` | `Parallel LC` | `Parallel RLC`

Select the desired combination of a resistor (R), capacitor (C), and
inductor (L), connected in series or in parallel.

### **Resistance** — Resistance `1` `Ohm` (default) | positive scalar

Resistance of each of the line impedances.

#### Dependencies

To enable this parameter, set **Component
structure** to either `R`,
`Series RL`, `Series
RC`, `Series RLC`,
`Parallel RL`, or `Parallel
RC`.

### **Inductance** — Inductance `1e-3` `H` (default) | positive scalar

Inductance of each of the line impedances.

#### Dependencies

To enable this parameter, set **Component
structure** to either `L`,
`Series RL`, `Series
LC`, `Series RLC`,
`Parallel RL`, or `Parallel
LC`.

### **Capacitance** — Capacitance `1e-6` `F` (default) | positive scalar

Capacitance in each of the line impedances.

#### Dependencies

To enable this parameter, set **Component
structure** to either `C`,
`Series RC`, `Series
LC`, `Series RLC`,
`Parallel RC`, or `Parallel
LC`.

### Parasitics

### **Parasitic series resistance** — Parasitic series resistance `0` `Ohm` (default) | nonnegative scalar

Series resistance value added to all instances of capacitors in the
load.

#### Dependencies

To enable this parameter, set **Component
structure** to either `C`,
`Parallel RC`, or `Parallel
LC`.

### **Parasitic parallel conductance** — Parasitic parallel conductance `0` `1/Ohm` (default) | nonnegative scalar

Parallel conductance value added across all instances of inductors in
the load. This parameter represents small parasitic effects.

If you set **Component structure** to either
`Series RL`, `Series
LC`, or `Series RLC`, the
parasitic parallel conductance is connected across the full branch of
the block.

#### Dependencies

To enable this parameter, set **Component
structure** to either `L`,
`Series RL`, `Series
LC`, or `Series
RLC`.

### Faults

To modify the faults, create a fault and, in the block dialog
box, click **Open fault properties**. To open the faults, in the Property
Inspector, click the **Fault behavior** link.

### **Branch fault** — Option to add branch fault `Add fault`

*Since R2024b*

Option to add a branch fault in the RLC (Three-Phase) block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted phase** — Option to specify faulted phase `Phase a` (default) | `Phase b` | `Phase c` | `Phase a and b` | `Phase b and c` | `Phase c and a` | `Phase a, b and c`

*Since R2024b*

Option to specify the faulted phase of the RLC (Three-Phase) block. You can
specify one or more faulted phases.

#### Dependencies

To enable this parameter, add a fault to the RLC (Three-Phase) block by
clicking the **Add fault** hyperlink in the
**Branch fault** parameter.

### **Faulted resistance** — Resistance of faulted impedance components `0.01` `Ohm` (default) | positive scalar

*Since R2024b*

Resistance of the faulted impedance components.

#### Dependencies

To enable this parameter, add a fault to the RLC (Three-Phase) block by
clicking the **Add fault** hyperlink in the
**Branch fault** parameter.

## Libraries

Simscape / Electrical / Passive / RLC Assemblies

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2024b: Model branch faults

You can now model one or more faulted phases. The block models the faulted phase
as a resistor. To specify the value of the faulted resistance, use the
**Faulted resistance** parameter.

### R2024b: The **Modeling Option** parameter has changed

The **Modeling option** parameter has been replaced
with the **Electrical connection** parameter inside the
**Main** section in the block dialog box or
Property Inspector.

If a model you created in an earlier release contains this block, the software
automatically sets the value of the **Electrical
connection** parameter to the value you specified for the **Modeling option** parameter.

## Description

Three-phase impedance

The RLC (Three-Phase) block models a three-phase
impedance with two three-phase connections. Each of the three identical impedance
components can include any combination of a resistor (R), capacitor (C), and inductor
(L), connected in series or in parallel.

Define the values for the R, L, and C components by specifying the appropriate block
parameters. Do not set the parameter values to zero or infinity to remove terms.
Instead, select the correct option for the **Component structure**
parameter.

For certain combinations of R, L, and C, for some circuit topologies, you should
specify parasitic resistance or conductance values that help the simulation to converge
numerically. These parasitic terms help create a small parallel resistive path for an
inductor and a small series resistance for a capacitor.

### Faults

*Since R2024b*

To model a fault in the RLC (Three-Phase) block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The RLC (Three-Phase) block allows you to represent one or more faulted phases. The
block models the faulted phase as a resistor. To specify the value of the faulted
resistance, use the **Faulted resistance** parameter.

For example, this diagram shows the equivalent circuit of three-phase inductor branch.

Equivalent circuit of three-phase inductor branch. Top inductor is labeled La, middle inductor is labeled Lb, bottom inductor is labeled Lc.

When you add a branch fault and you set the **Faulted phase**
parameter to `Phase a`, this diagram shows the equivalent
circuit of the faulted three-phase inductor branch.

Equivalent circuit of faulted three-phase inductor branch. Top resistor is labeled Rfa, middle inductor is labeled Lb, bottom inductor is labeled Lc.

### Variables

To set the priority and initial target values for the block variables prior to
simulation, use the **Initial Targets** section in the block dialog
box or Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a
model. Using system scaling based on nominal values increases the simulation
robustness. Nominal values can come from different sources, one of which is the
**Nominal Values** section in the block dialog box or Property
Inspector. For more information, see System Scaling by Nominal Values.

For this block, the **Initial Targets** and **Nominal
Values** settings are visible only if, in the **Main**
section, you do not set the **Component structure** parameter to
`R`.
