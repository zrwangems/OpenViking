---
type: simulink-block
title: 'Two-Phase Fluid Predefined Properties (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Utilities'
documentation_page: 'twophasefluidpredefinedproperties2p'
documentation_source_path: 'ref/twophasefluidpredefinedproperties2p.html'
language: en
---

# Two-Phase Fluid Predefined Properties (2P)

## Ports

### Conserving

### **A** — Connection port two-phase fluid

Two-phase fluid conserving port that connects the block to the
network. This port connects to any point on a two-phase connection line
within a block diagram. When you connect the Two-Phase
Fluid Predefined Properties (2P) block to a network
line, the fluid properties are propagated to all blocks in the circuit.

## Parameters

### **Two-phase fluid** — Working fluid `Water (R-718)` (default) | `Ammonia (R-717)` | `Carbon dioxide (R-744)` | `Isobutane (R-600a)` | `Propane (R-290)` | `R-1233zd(E)` | `R-1234yf` | `R-134a` | `R-22` | `R-32` | `R-404A` | `R-407C` | `R-410A`

Predefined working fluid options.

### **Atmospheric pressure** — Environmental pressure `0.101325` MPa (default) | positive scalar

Environmental pressure of the system.

### **Pressure and specific internal energy outside valid range** — Whether to notify when pressure or specific internal energy are outside valid range `Error` (default) | `Warning` | `None`

Select what happens if the fluid pressure or specific internal energy go
beyond the valid range during simulation:

- `None` ― The block does not return an
  error if the properties go out of range.
- `Warning` ― The block issues a warning,
  but continues the simulation.
- `Error` ― The block returns an error and
  stops the simulation.

### **Dynamic pressure threshold for flow reversal** — Sets region in which numerical smoothing is applied `0.01` Pa (default) | positive scalar

Sets region in which numerical smoothing is applied. A transition region
is defined around 0 MPa between the positive and negative values of the
**Dynamic pressure threshold for flow reversal**.
Within this transition region, the calculated properties are adjusted to
ensure a smooth transition.

## Libraries

Simscape / Fluids / Two-Phase Fluid / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2024b: Use new pre-defined two-phase fluids

You can now model Propane (R-290), R-32, and R-1233zd(E) as pre-defined fluids in
the two-phase domain.

### R2023a: Control block behavior when fluid properties go out of range during simulation

Previously, if fluid properties went beyond the valid range during simulation, the block
would return an error. You can now use the new **Pressure and specific
internal energy outside valid range** parameter to control the block
behavior if fluid properties go out of range during simulation.

## Description

Predefined working fluids for two-phase networks

The Two-Phase Fluid Predefined Properties (2P) block sets the working fluid properties
of your two-phase system. The available predefined fluids are:

- Water (R-718)
- R-134a
- R-1234yf
- R-1233zd(E)
- R-404A
- R-410A
- R-407C
- R-22
- R-32
- Ammonia (R-717)
- Carbon dioxide (R-744)
- Isobutane (R-600a)
- Propane (R-290)

If you would like to specify your own working fluid properties, use the
Foundation Library Two-Phase Fluid Properties (2P) block. If you do not specify a fluid, the
system defaults will apply. See Specify Fluid Properties for more
details.

### Fluid Properties Range

**Water (R-718)**

The fluid properties are provided for a pressure range of 0.001 to 95 MPa, and
temperature range (at 1 atmosphere) of 273.16 to 1,245.8 K.

**R-134a**

The fluid properties are provided for a pressure range of 0.001 to 5.5 MPa,
and temperature range (at 1 atmosphere) of 177.08 to 424.4 K.

**R-1234yf**

The fluid properties are provided for a pressure range of 0.04 to 3.2 MPa, and
temperature range (at 1 atmosphere) of 223.52 to 387.45 K.

**R-1233zd(E)**

The fluid properties are provided for a pressure range of 0.001 to 9 MPa, and
temperature range (at 1 atmosphere) of 202.29 to 500.24 K.

**R-404A**

The fluid properties are provided for a pressure range of 0.003 to 12 MPa, and
temperature range (at 1 atmosphere) of 171.6 to 550.94 K.

**R-410A**

The fluid properties are provided for a pressure range of 0.001 to 6 MPa, and
temperature range (at 1 atmosphere) of 146.19 to 427.25 K.

**R-407C**

The fluid properties are provided for a pressure range of 0.001 to 6 MPa, and
temperature range (at 1 atmosphere) of 158.85 to 427.92 K.

**R-22**

The fluid properties are provided for a pressure range of 0.001 to 8 MPa, and
temperature range (at 1 atmosphere) of 120.77 to 519.49 K.

**R-32**

The fluid properties are provided for a pressure range of 0.0001 to 7 MPa, and
temperature range (at 1 atmosphere) of 138.91 to 375.55 K.

**Ammonia (R-717)**

The fluid properties are provided for a pressure range of 0.008 to 95 MPa, and
temperature range (at 1 atmosphere) of 195.5 to 543.9 K.

**Carbon dioxide (R-744)**

The fluid properties are provided for a pressure range of 0.55 to 50 MPa, and
temperature range (at 1 MPa) of 216.94 to 1,389.4 K. Note that the triple point
of carbon dioxide is higher than atmospheric pressure, and therefore the minimum
valid pressure is adjusted accordingly. When using carbon dioxide as the working
fluid, ensure that connected blocks with initial pressure parameters, such as a
Reservoir (2P) block, are equal to or greater this minimum pressure.

**Isobutane (R-600a)**

The fluid properties are provided for a pressure range of 0.0001 to 15 MPa,
and temperature range (at 1 atmosphere) of 121.02 to 516.64 K.

**Propane (R-290)**

The fluid properties are provided for a pressure range of 0.0001 to 18 MPa,
and temperature range (at 1 atmosphere) of 94.21 to 554.92 K.

### Visualizing Fluid Properties

To visualize the:

- Specific volume
- Specific entropy
- Temperature
- Kinematic viscosity
- Thermal conductivity
- Prandtl number

of the network fluid as a function of specific internal energy or specific
enthalpy and pressure, right-click on the block and select **Fluids** > **Plot Fluid Properties (3D)**:

or **Fluids** > **Plot Fluid Properties (Contours)**:

Use the **Reload Data** button to regenerate the
plot whenever the fluid selection or fluid parameters change.
