---
type: simulink-block
title: 'Delta-Connected Load'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / RLC Assemblies'
documentation_page: 'deltaconnectedload'
documentation_source_path: 'ref/deltaconnectedload.html'
language: en
---

# Delta-Connected Load

## Ports

### Conserving

### **~** — Three-phase port electrical

Composite three-phase port.

For more information about composite and expanded three-phase ports,
see Three-Phase Ports.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a** — *a*-phase electrical

Electrical conserving port associated with the
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with the
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — *c*-phase electrical

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

### **Parameterization** — Parameterization `Specify by rated power and voltage` (default) | `Specify component values directly`

Select how to specify values for the R, L, and C components:

- `Specify by rated power and voltage`
  — Specify values for the R, L, and C components by rated
  powers at a rated voltage and frequency. This option is the
  default.
- `Specify component values directly`
  — Specify values for the R, L, and C components directly
  in terms of resistance, inductance, and capacitance.

Switching the **Parameterization** value resets the
**Component structure** value. Select the component
parameterization option first, and then the component structure. If you
later switch the **Parameterization** value, check the
**Component structure** value and reselect it, if
necessary.

### **Component structure** — Desired component combination `R` (default) | `L` | `C` | `Series RL` | `Series RC` | `Series LC` | `Series RLC` | `Parallel RL` | `Parallel RC` | `Parallel LC` | `Parallel RLC`

Select the desired combination of a resistor (R), capacitor (C), and
inductor (L), connected in series or in parallel.

### **Rated voltage** — Rated voltage `24e3` `V` (default) | nonnegative scalar

Voltage for which load powers are specified.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify by
rated power and voltage`.

### **Real power** — Total real dissipated power `1e3` `W` (default) | positive scalar

Total real power dissipated by three-phase load when supplied at the
rated voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify by
rated power and voltage` and **Component
structure** to either `R`,
`Series RL`, `Series
RC`, `Series RLC`,
`Parallel RL`, or `Parallel
RC`.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` (default) | positive scalar

Frequency for which you specify the reactive load powers.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify by
rated power and voltage`.

### **Inductive reactive power** — Inductive reactive power `1e2` `A*V` (default) | positive scalar

Total inductive reactive power that the three-phase load takes when
supplied at the rated voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify by
rated power and voltage` and **Component
structure** to either `L`,
`Series RL`, `Series
LC`, `Series RLC`,
`Parallel RL`, or `Parallel
LC`.

### **Capacitive reactive power** — Total capacitive reactive power `-1e2` `A*V` (default) | negative scalar

Total capacitive reactive power that the three-phase load takes when
supplied at the rated voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify by
rated power and voltage` and **Component
structure** to either `C`,
`Series RC`, `Series
LC`, `Series RLC`,
`Parallel RC`, or `Parallel
LC`.

### **Resistance** — Resistance `1` `Ohm` (default) | positive scalar

Resistance of each of the load limbs.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
component values` and **Component
structure** to either `R`,
`Series RL`, `Series
RC`, `Series RLC`,
`Parallel RL`, or `Parallel
RC`.

### **Inductance** — Inductance `0.001` `H` (default) | positive scalar

Inductance of each of the load limbs.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
component values` and **Component
structure** to either `L`,
`Series RL`, `Series
LC`, `Series RLC`,
`Parallel RL`, or `Parallel
LC`.

### **Capacitance** — Capacitance `1e-6` `F` (default) | positive scalar

Capacitance in each of the load limbs.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
component values` and **Component
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

### Initial Conditions

### **Terminal voltage magnitude** — Magnitude of terminal voltage `24e3` `V` (default) | nonnegative scalar

Magnitude of the terminal voltage.

#### Dependencies

To enable this parameter, set **Component
structure** to either `L`,
`C`, `Series
RL`, `Series RC`,
`Series LC`, `Series
RLC`, `Parallel RL`,
`Parallel RC`, or `Parallel
LC`.

### **Terminal voltage angle** — Angle of terminal voltage `0` `deg` (default) | scalar

Angle of the terminal voltage.

#### Dependencies

To enable this parameter, set **Component
structure** to either `L`,
`C`, `Series
RL`, `Series RC`,
`Series LC`, `Series
RLC`, `Parallel RL`,
`Parallel RC`, or `Parallel
LC`.

### **Frequency** — Frequency `60` `Hz` (default) | positive scalar

Frequency.

#### Dependencies

To enable this parameter, set **Component
structure** to either `L`,
`C`, `Series
RL`, `Series RC`,
`Series LC`, `Series
RLC`, `Parallel RL`,
`Parallel RC`, or `Parallel
LC`.

### Faults

To modify the faults, create a fault and, in the block dialog
box, click **Open fault properties**. To open the faults, in the Property
Inspector, click the **Fault behavior** link.

### **Connection fault** — Option to add fault to connection port `Add fault`

*Since R2024b*

Option to add a fault to the three-phase connection port of the
load.

To add a fault, click the **Add fault**
hyperlink.

#### Dependencies

To enable this parameter, set **Model two line
sections** to `Yes`.

### **Fault type** — Type of fault `Single-phase to ground (a-g)` (default) | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*Since R2024b*

Type of fault to model. The visibility of the related parameters
depends on the fault model.

#### Dependencies

To enable this parameter, add a fault to the block by clicking the
**Add fault** hyperlink next to the
**Connection fault** parameter.

### **Faulted phase-neutral resistance** — Faulted resistance between phase connection and neutral point `1e-3` `Ohm` (default) | positive scalar

*Since R2024b*

Resistance between the phase connection and the neutral point when the
fault is active.

#### Dependencies

To enable this parameter, add a fault to the block by clicking the
**Add fault** hyperlink next to the
**Connection fault** parameter, and set the
**Fault type** parameter to one of these options:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Faulted neutral-ground resistance** — Faulted resistance between neutral point and electrical reference `1e-3` `Ohm` (default) | positive scalar

*Since R2024b*

Resistance between the neutral point and the electrical reference when
fault is active.

#### Dependencies

To enable this parameter, add a fault to the block by clicking the
**Add fault** hyperlink next to the
**Connection fault** parameter, and set the
**Fault type** parameter to one of these options:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase to ground
  (a-b-c-g)`

### **Unfaulted phase-neutral conductance** — Unfaulted conductance between phase connection and neutral point `1e-6` `1/Ohm` (default) | positive scalar

*Since R2024b*

Conductance between the phase connection and the neutral point when
the fault is not active.

#### Dependencies

To enable this parameter, add a fault to the block by clicking the
**Add fault** hyperlink next to the
**Connection fault** parameter, and set the
**Fault type** parameter to one of these options:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

## Libraries

Simscape / Electrical / Passive / RLC Assemblies

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2024b: Model faults at the three-phase connection port

You can now model a phase-to-ground or a phase-to-phase fault at the three-phase
connection port of the load. To specify the value of the faulted resistances and the
unfaulted conductance, use the **Faulted phase-neutral
resistance**, **Faulted neutral-ground resistance**, and
**Unfaulted phase-neutral conductance** parameters.

### R2024b: The **Modeling Option** parameter has changed

The **Modeling option** parameter has been replaced
with the **Electrical connection** parameter inside the
**Main** section in the block dialog box or
Property Inspector.

If a model you created in an earlier release contains this block, the software
automatically sets the value of the **Electrical
connection** parameter to the value you specified for the **Modeling option** parameter.

## Description

Three-phase load wired in delta configuration

The Delta-Connected Load block models a three-phase
load wired in a delta configuration. Each limb of the load can include any combination
of a resistor (R), capacitor (C), and inductor (L), connected in series or in parallel.

You can specify values for the R, L, and C components directly in terms of resistance,
inductance, and capacitance, or by rated powers at a rated voltage and frequency.

- If you parameterize the block directly in terms or R, L, and C values, then
  for initialization, provide a three-element row vector of initial voltages for a
  capacitor and a three-element row vector of initial currents for an
  inductor.
- If you parameterize the block in terms of rated powers, then specify initial
  conditions in terms of an initial voltage, initial voltage phase, and initial
  frequency. For example, if the load is connected directly to a three-phase
  voltage source, then the initial conditions are identical to the source values
  for RMS line voltage, frequency, and phase shift. To specify zero initial
  voltage magnitude, set the initial voltage to 0.

For certain combinations of R, L, and C, for some circuit topologies, you should
specify parasitic resistance or conductance values that help the simulation to converge
numerically. These parasitic terms help create a small parallel resistive path for an
inductor and a small series resistance for a capacitor. When you parameterize the block
in terms of rated powers, the rated power values do not account for these small
parasitic terms. The rated powers represent only the R, L, and C values of the load
itself.

### Block Parameterization

These tables list the block parameters for each value of the **Component
structure** parameter, based on the
**Parameterization** option you select:

- `Specify by rated power and voltage`
- `Specify component values directly`

**Specify by Rated Power and Voltage**

| Component Structure | Main Parameters | Parasitics Parameters | Initial Conditions Parameters |
| --- | --- | --- | --- |
| `R` | Rated voltage  Real power | None | None |
| `L` | Rated voltage  Rated electrical frequency  Inductive reactive power | Parasitic parallel conductance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `C` | Rated voltage  Rated electrical frequency  Capacitive reactive power | Parasitic series resistance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Series RL` | Rated voltage  Rated electrical frequency  Real power  Inductive reactive power | Parasitic parallel conductance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Series RC` | Rated voltage  Rated electrical frequency  Real power  Capacitive reactive power | None | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Series LC` | Rated voltage  Rated electrical frequency  Inductive reactive power  Capacitive reactive power | Parasitic parallel conductance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Series RLC` | Rated voltage  Rated electrical frequency  Real power  Inductive reactive power  Capacitive reactive power | Parasitic parallel conductance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Parallel RL` | Rated voltage  Rated electrical frequency  Real power  Inductive reactive power | None | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Parallel RC` | Rated voltage  Rated electrical frequency  Real power  Capacitive reactive power | Parasitic series resistance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Parallel LC` | Rated voltage  Rated electrical frequency  Inductive reactive power  Capacitive reactive power | Parasitic series resistance | Terminal voltage magnitude  Terminal voltage angle  Frequency |
| `Parallel RLC` | Rated voltage  Rated electrical frequency  Real power  Inductive reactive power  Capacitive reactive power | Parasitic series resistance | Terminal voltage magnitude  Terminal voltage angle  Frequency |

**Specify Component Values Directly**

| Component Structure | Main Parameters | Parasitics Parameters | Initial Conditions Parameters |
| --- | --- | --- | --- |
| `R` | Resistance | None | None |
| `L` | Inductance | Parasitic parallel conductance | Initial inductor current [ Ia Ib Ic ] |
| `C` | Capacitance | Parasitic series resistance | Initial capacitor voltage [ Va Vb Vc ] |
| `Series RL` | Resistance  Inductance | Parasitic parallel conductance | Initial inductor current [ Ia Ib Ic ] |
| `Series RC` | Resistance  Capacitance | None | Initial capacitor voltage [ Va Vb Vc ] |
| `Series LC` | Inductance  Capacitance | Parasitic parallel conductance | Initial inductor current [ Ia Ib Ic ]  Initial capacitor voltage [ Va Vb Vc ] |
| `Series RLC` | Resistance  Inductance  Capacitance | Parasitic parallel conductance | Initial inductor current [ Ia Ib Ic ]  Initial capacitor voltage [ Va Vb Vc ] |
| `Parallel RL` | Resistance  Inductance | None | Initial inductor current [ Ia Ib Ic ] |
| `Parallel RC` | Resistance  Capacitance | Parasitic series resistance | Initial capacitor voltage [ Va Vb Vc ] |
| `Parallel LC` | Inductance  Capacitance | Parasitic series resistance | Initial inductor current [ Ia Ib Ic ]  Initial capacitor voltage [ Va Vb Vc ] |
| `Parallel RLC` | Resistance  Inductance  Capacitance | Parasitic series resistance | Initial inductor current [ Ia Ib Ic ]  Initial capacitor voltage [ Va Vb Vc ] |

### Faults

*Since R2024b*

To model a fault in the Delta-Connected Load block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Delta-Connected Load block allows you to model these types of fault at the three-phase
connection port:

- Single-phase-to-ground fault (a-g, b-g, or c-g)
- Two-phase fault (a-b, b-c, or c-a)
- Two-phase-to-ground fault (a-b-g, b-c-g, or c-a-g)
- Three-phase fault (a-b-c)
- Three-phase-to-ground fault (a-b-c-g)

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
section, you set the **Parameterization** parameter to
`Specify component values directly` and you do not set
the **Component structure** parameter to
`R`.
