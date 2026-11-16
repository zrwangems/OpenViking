---
type: simulink-block
title: 'Simplified Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / System-Level Modeling'
documentation_page: 'simplifiedgenerator'
documentation_source_path: 'ref/simplifiedgenerator.html'
language: en
---

# Simplified Generator

## Ports

### Input

### **Pref** — Reference power, in pu physical signal

Physical signal input port that specifies the per-unit reference power.
### Conserving

### **R** — Rotor mechanical rotational

Mechanical rotational conserving port associated with the rotor.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the case.

### **~** — Three-phase port three-phase electrical

Composite three-phase electrical conserving port.

For more information about composite and expanded three-phase ports, see Three-Phase Ports.

#### Dependencies

To enable this port, set **Electrical connection** to
`Composite three-phase ports`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral phase.

### **a** — *a*-phase electrical

Electrical conserving port associated with the *a*-phase.

#### Dependencies

To enable this port, set **Electrical connection** to
`Expanded three-phase ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with the *b*-phase.

#### Dependencies

To enable this port, set **Electrical connection** to
`Expanded three-phase ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with the *c*-phase.

#### Dependencies

To enable this port, set **Electrical connection** to
`Expanded three-phase ports`.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### General

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Option to choose composite or expanded three-phase ports. For more information,
see Three-Phase Ports.

### **Rated power** — Rated power `100e3` `W` (default) | nonnegative scalar

Rated power.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` (default) | positive scalar

Rated electrical frequency.

### **Internal source voltage (phase-to-phase RMS)** — Internal source voltage `1485` `V` (default) | nonnegative scalar

Internal source voltage.

### **Source impedance** — Source impedance parameterization `X/R Ratio` (default) | `Series RL`

Source impedance parameterization method. Choose one of these options:

- `X/R Ratio` — Specify the ratio of the series
  connected reactance to resistance.
- `Series RL` — Specify the resistance and
  inductance.

### **Short circuit power** — Short circuit power `1e6` `A*V` (default) | positive scalar

Short circuit power.

#### Dependencies

To enable this parameter, set **Source impedance** to
`X/R Ratio`.

### **X/R ratio** — X/R ratio `15` (default) | positive scalar

Ratio of the series connected reactance to resistance.

#### Dependencies

To enable this parameter, set **Source impedance** to
`X/R Ratio`.

### **Inductance** — Inductance `0.01` `H` (default) | positive scalar

Inductance.

#### Dependencies

To enable this parameter, set **Source impedance** to
`Series RL`.

### **Resistance** — Resistance `0.1` `Ohm` (default) | positive scalar

Resistance.

#### Dependencies

To enable this parameter, set **Source impedance** to
`Series RL`.

### **Source impedance parasitic parallel conductance** — Source impedance parasitic parallel conductance `0` `1/Ohm` (default) | nonnegative scalar

Parasitic parallel conductance of source impedance.

### **Percentage mechanical efficiency** — Percentage mechanical efficiency `95` (default) | positive scalar

Mechanical efficiency, as a percentage.

### **Active power frequency droop** — Active power frequency droop `0.1` `Hz` (default) | nonnegative scalar

Frequency droop of active power.

### **Droop filter time constant** — Droop filter time constant `1e-2` `s` (default) | scalar

Droop filter time constant.

### **Rotor inertia** — Rotor inertia `1` `kg*m^2` (default) | positive scalar

Resistance of the rotor to change in motion.

### **Rotor damping** — Rotor damping `0` `N*m*s/rad` (default) | nonnegative scalar

Rotor damping.

### **Electrical power measurement filter time constant** — Electrical power measurement filter time constant `1e-3` `s` (default) | nonnegative scalar

Filter time constant of the electrical power measurement.

## Libraries

Simscape / Electrical / Electromechanical

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Behavioral model of an electromechanical generator

The Simplified Generator block implements a behavioral
model of an electromechanical generator. Use the **Pref** port to
specify the reference power. The block supplies the reference power to the mechanical network
and supplies the electrical power required to satisfy the mechanical power demand and account
tor losses. This figure shows the circuit configuration of the block. The block acts as a
constant voltage source with a series source impedance.

- *V*ie is the supply voltage.
- *I*S is the series source current.
- *R*S is the series source resistance.
- *L*S is the series source inductance.

The Simplified Generator block operates in both
grid-connected and islanded mode. In grid-connected mode, the mechanical power tracks the
reference power and the electrical power you need to supply to the grid to account for losses.
The active power flow depends on the ratio of the series connected reactance to resistance for
the entire electrical network. To achieve the expected behavior, you need to tune the
**Active power frequency droop** and **Droop filter time
constant** parameters as well as the block impedance. To choose how to specify the
block the impedance, set the **Source impedance** parameter to one of these
options:

- `X/R Ratio` — Specify the ratio of the series connected
  reactance to resistance.
- `Series RL` — Specify the resistance and inductance.

During islanded mode, the block acts like a constant voltage AC supply because maintaining
frequency takes priority over the mechanical power tracking the power reference.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Assumptions and Limitations

This block requires an electrical network with a high ratio of series connected
reactance to resistance.
