---
type: simulink-block
title: 'Constant Volume Chamber (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'constantvolumechamber2p'
documentation_source_path: 'ref/constantvolumechamber2p.html'
language: en
---

# Constant Volume Chamber (2P)

## Ports
```yaml
ports:
- name: A
  summary: Chamber inlet two-phase fluid
  direction: conserving
- name: B
  summary: Chamber inlet two-phase fluid
  direction: conserving
- name: C
  summary: Chamber inlet two-phase fluid
  direction: conserving
- name: D
  summary: Chamber inlet two-phase fluid
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **A** — Chamber inlet two-phase fluid

Two-phase fluid conserving port associated with the chamber inlet.

### **B** — Chamber inlet two-phase fluid

Two-phase fluid conserving port associated with the second chamber inlet.

#### Dependencies

To enable this port, set the **Number of ports** parameter to
`2`, `3`, or
`4`.

### **C** — Chamber inlet two-phase fluid

Two-phase fluid conserving port associated with the third chamber inlet.

#### Dependencies

To enable this port, set the **Number of ports** parameter to
`3` or `4`.

### **D** — Chamber inlet two-phase fluid

Two-phase fluid conserving port associated with the fourth chamber inlet. If a
chamber has four inlet ports, you can use the block as a junction in a cross
connection.

#### Dependencies

To enable this port, set the **Number of ports** parameter to
`4`.

### **H** — Thermal port thermal

Thermal conserving port through which the fluid in the chamber exchanges heat with
a thermal network.
## Parameters
```yaml
parameters:
- name: Chamber volume
  summary: Volume of fluid inside chamber 0.001 m^3 (default) | positive scalar
  group: Main
- name: Number of ports
  summary: Number of inlet ports in chamber 1 (default) | 2 | 3 | 4
  group: Main
- name: Cross-sectional area at port A
  summary: Inlet area normal to direction of flow 0.01 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port B
  summary: Inlet area normal to direction of flow 0.01 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port C
  summary: Inlet area normal to direction of flow 0.01 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port D
  summary: Inlet area normal to direction of flow 0.01 m^2 (default) | positive scalar
  group: Main
- name: Initial fluid energy specification
  summary: Thermodynamic variable to use in defining initial conditions Temperature (default) | Vapor quality | Vapor void
    fraction | Specific enthalpy | Specific internal energy
  group: Effects and Initial Conditions
- name: Initial pressure
  summary: Absolute pressure at start of simulation 0.101325 MPa (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial temperature
  summary: Absolute temperature at start of simulation 293.15 K (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial vapor quality
  summary: Mass fraction of vapor at start of simulation 0.5 (default) | unitless scalar between 0 and 1
  group: Effects and Initial Conditions
- name: Initial vapor void fraction
  summary: Volume fraction of vapor at start of simulation 0.5 (default) | unitless scalar between 0 and 1
  group: Effects and Initial Conditions
- name: Initial specific enthalpy
  summary: Specific enthalpy at start of simulation 1500 kJ/kg (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial specific internal energy
  summary: Specific internal energy at start of simulation 1500 kJ/kg (default) | positive scalar
  group: Effects and Initial Conditions
- name: Phase change time constant
  summary: Characteristic duration of a phase-change event 0.1 s (default) | positive scalar
  group: Effects and Initial Conditions
```

### Main

### **Chamber volume** — Volume of fluid inside chamber `0.001 m^3` (default) | positive scalar

Volume of fluid in the chamber. This volume is constant during simulation.

### **Number of ports** — Number of inlet ports in chamber `1` (default) | `2` | `3` | `4`

Number of inlet ports in the chamber. The chamber can have between one and four
ports, labeled from **A** to **D**. When you modify
the parameter value, the corresponding ports are exposed or hidden in the block
icon.

### **Cross-sectional area at port A** — Inlet area normal to direction of flow `0.01 m^2` (default) | positive scalar

Inlet area normal to the direction of flow at port **A**.

### **Cross-sectional area at port B** — Inlet area normal to direction of flow `0.01 m^2` (default) | positive scalar

Inlet area normal to the direction of flow at port **B**.

#### Dependencies

To enable this parameter, set **Number of ports** to
`2`, `3`, or
`4`.

### **Cross-sectional area at port C** — Inlet area normal to direction of flow `0.01 m^2` (default) | positive scalar

Inlet area normal to the direction of flow at port **C**.

#### Dependencies

To enable this parameter, set **Number of ports** to
`3` or `4`.

### **Cross-sectional area at port D** — Inlet area normal to direction of flow `0.01 m^2` (default) | positive scalar

Inlet area normal to the direction of flow at port **D**.

#### Dependencies

To enable this parameter, set **Number of ports** to
`4`.

### Effects and Initial Conditions

### **Initial fluid energy specification** — Thermodynamic variable to use in defining initial conditions `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Thermodynamic variable in terms of which to define the initial conditions of the
block.

The value for the **Initial fluid energy specification** parameter limits the
available initial states for the two-phase fluid. When **Initial fluid energy
specification** is:

- `Temperature` — Specify an initial state that is a
  subcooled liquid or superheated vapor. You cannot specify a liquid-vapor mixture
  because the temperature is constant across the liquid-vapor mixture
  region.
- `Vapor quality` — Specify an initial state that is a
  liquid-vapor mixture. You cannot specify a subcooled liquid or a superheated
  vapor because the liquid mass fraction is 0 and 1, respectively, across the
  whole region. Additionally, the block limits the pressure to below the critical
  pressure.
- `Vapor void fraction` — Specify an initial state that
  is a liquid-vapor mixture. You cannot specify a subcooled liquid or a
  superheated vapor because the liquid mass fraction is 0 and 1, respectively,
  across the whole region. Additionally, the block limits the pressure to below
  the critical pressure.
- `Specific enthalpy` — Specify the specific enthalpy of
  the fluid. The block does not limit the initial state.
- `Specific internal energy` — Specify the specific
  internal energy of the fluid. The block does not limit the initial state.

### **Initial pressure** — Absolute pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Pressure in the chamber at the start of simulation, specified against absolute
zero.

### **Initial temperature** — Absolute temperature at start of simulation `293.15 K` (default) | positive scalar

Temperature in the chamber at the start of simulation, specified against absolute
zero.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Temperature`.

### **Initial vapor quality** — Mass fraction of vapor at start of simulation `0.5` (default) | unitless scalar between 0 and 1

Mass fraction of vapor in the chamber at the start of simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Vapor quality`.

### **Initial vapor void fraction** — Volume fraction of vapor at start of simulation `0.5` (default) | unitless scalar between 0 and 1

Volume fraction of vapor in the chamber at the start of simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Vapor void fraction`.

### **Initial specific enthalpy** — Specific enthalpy at start of simulation `1500 kJ/kg` (default) | positive scalar

Specific enthalpy of the fluid in the chamber at the start of simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Specific enthalpy`.

### **Initial specific internal energy** — Specific internal energy at start of simulation `1500 kJ/kg` (default) | positive scalar

Specific internal energy of the fluid in the chamber at the start of
simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Specific internal
energy`.

### **Phase change time constant** — Characteristic duration of a phase-change event `0.1 s` (default) | positive scalar

Characteristic time to equilibrium of a phase-change event taking place in the
chamber. Increase this parameter to slow the rate of phase change or decrease it to
speed the rate.
## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2022b: Conditional inlet port visibility

The Constant Volume Chamber (2P) block can
have between one and four inlet ports, controlled by the **Number of
ports** parameter value.

In previous releases, the block had only one inlet port. The Two-Phase Fluid library
also contained separate two-port and three-port blocks, which are no longer available. This
change has no compatibility impact. When you open an existing model, all two-port and
three-port chamber blocks in it are automatically replaced by a Constant Volume Chamber (2P) block with the appropriate number of
conserving ports.

The four-port chamber was not available in previous releases.

## Description

Chamber with fixed volume of two-phase fluid and variable number of ports

The Constant Volume Chamber (2P) block models the
accumulation of mass and energy in a chamber containing a fixed volume of two-phase fluid. The
chamber can have between one and four inlets, labeled from **A**
to **D**, through which fluid can flow. The fluid volume can
exchange heat with a thermal network, such as a network that represents the chamber
surroundings, through the thermal port **H**.

The mass of the fluid in the chamber varies with density, a property that is generally a
function of pressure and temperature for a two-phase fluid. Fluid enters when the pressure
upstream of the inlet rises above the pressure in the chamber and exits when the pressure
gradient reverses. The effect in a model is often to smooth out sudden changes in pressure,
much like an electrical capacitor does with voltage.

The flow resistance between the inlet and interior of the chamber is assumed to be
negligible. The pressure in the interior is therefore equal to that at the inlet. Similarly,
the thermal resistance between the thermal port and interior of the chamber is assumed to be
negligible. The temperature in the interior is equal to the temperature at the thermal
port.

### Mass Balance

Mass can enter and exit the chamber through ports **A**,
**B**, **C**, and **D**. The volume of the chamber is fixed but the compressibility of
the fluid means that its mass can change with pressure and temperature. The rate of mass
accumulation in the chamber must exactly equal the mass flow rate through ports **A**, **B**, **C**, and **D**,

[(∂ρ∂p)udpdt+(∂ρ∂u)pdudt]V=m˙A+m˙B+m˙C+m˙D+ϵM,

where the left-hand side is the rate of mass accumulation and:

- *ρ* is the density.
- *p* is the pressure.
- *u* is the specific internal energy.
- *V* is the volume.
- m˙ is the mass flow rate.
- *ϵ*M is a correction term that accounts
  for a numerical error caused by the smoothing of the partial derivatives.

**Correction Term for Partial-Derivative Smoothing**

The block computes the partial derivatives in the mass balance equation by applying
the finite-difference method to the tabulated data in the Two-Phase Fluid Properties (2P) block and interpolating the results.
The block then smooths the partial derivatives at the phase-transition boundaries by means
of cubic polynomial functions. These functions apply between:

- The subcooled liquid and two-phase mixture phase domains when the vapor quality
  is in the 0–0.1 range.
- The two-phase mixture and superheated vapor phase domains when the vapor quality
  is in the 0–0.9 range.

The smoothing introduces a small numerical error that the block adjusts for by adding
to the mass balance the correction term *ϵ*M,
defined as:

ϵM=M−V/ντ.

where:

- *M* is the fluid mass in the chamber.
- *ν* is the specific volume.
- *τ* is the characteristic duration of a phase-change
  event.

The block obtains the fluid mass in the chamber from the equation:

dMdt=m˙A+m˙B+m˙C+m˙D.

### Energy Balance

Energy can enter and exit the chamber in two ways: with fluid flow through ports
**A**, **B**, **C**, and **D**, and with the heat flow
through port **H**. No work is done on or by the fluid inside
the chamber. The rate of energy accumulation in the internal fluid volume must then equal
the sum of the energy flow rates in through ports **A**,
**B**, **C**, **D**, and **H**,

E˙=ϕA+ϕB+ϕC+ϕD+​QH,

where:

- *ϕ* is energy flow rate.
- *Q* is heat flow rate.
- *E* is total energy.

Neglecting the kinetic energy of the fluid, the total energy in the chamber is:

E=Mu.

### Momentum Balance

The pressure drop due to viscous friction between the individual ports and the interior
of the chamber is assumed to be negligible. Gravity is ignored, as are other body forces.
The pressure in the internal fluid volume must therefore equal the pressure at ports
**A**, **B**, **C**, and **D**:

p=pA=pB=pC=pD.

### Assumptions and Limitations

- The chamber has a fixed volume of fluid.
- The flow resistance between the inlet and the interior of the chamber is
  negligible.
- The thermal resistance between the thermal port and the interior of the chamber is
  negligible.
- The kinetic energy of the fluid in the chamber is negligible.
