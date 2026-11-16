---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger Interface (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'specificdissipationheatexchangerinterfaceg'
documentation_source_path: 'ref/specificdissipationheatexchangerinterfaceg.html'
language: en
---

# Specific Dissipation Heat Exchanger Interface (G)

## Ports

### Output

### **CP** — Isobaric specific heat of gas, `kJ/(kg*K)` physical signal

Isobaric specific heat of the gas in the internal fluid volume of the
thermal interface.

### **M** — Mass flow rate of the thermal liquid, `kg/s` physical signal

Mass flow rate of the gas in the internal fluid volume of the
interface. The output signal is positive when the flow rate is directed
from port **A** to port **B** and
negative otherwise.
### Conserving

### **A** — Fluid opening gas

Opening through which gas can enter and exit the thermal
interface.

### **B** — Fluid opening gas

Opening through which gas can enter and exit the thermal
interface.

### **H** — Thermal condition at the fluid entrance thermal

Thermal port used to set the thermal condition at the gas port serving
as the gas entrance.

## Parameters

#### Pressure Loss

### **Mass flow rate vector** — Mass flow rates at which to specify pressure-drop data `[.3, .5, 1, 1.5, 2, 2.5] kg/s` (default) | *K*-element array with units of mass/time

Array of mass flow rates at which to specify the pressure drop tabulated
data.

### **Pressure drop vector** — Pressure-drop data corresponding to specified mass flow rates `[3, 5, 10, 25, 35, 50] * 1e-3 MPa` (default) | *K*-element array with units of pressure

Array of pressure drops from inlet to outlet corresponding to the
tabulated mass flow rate data.

### **Reference inflow temperature** — Temperature at which pressure-drop data is specified `293.15 K` (default) | scalar with units of temperature

Temperature at which the tabulated pressure-drop data is specified.

### **Reference inflow pressure** — Pressure at which pressure-drop tabulated data is specified `0.101325 MPa` (default) | scalar with units of pressure

Pressure at which the tabulated pressure-drop data is specified. The block
uses this parameter to calculate a third reference parameter, the reference
density. The reference that it uses to scale the tabulated pressure drop
data for pressures and temperatures deviating from the reference
conditions.

### **Mass flow rate threshold for flow reversal** — Mass flow rate below which to smooth numerical data `1e-6 kg/s` (default) | scalar with units of mass/time

Mass flow rate below which to initiate a smooth flow reversal to prevent
discontinuities in the simulation data.

### **Gas volume** — Volume of gas inside the heat exchanger `0.01 m^3` (default) | scalar with units of volume

Volume of gas occupying the heat exchanger at any given time. The initial
conditions specified in the **Effects and Initial
Conditions** tab apply to this volume. The volume is constant
during simulation.

### **Cross-sectional area at ports A1 and B1** — Flow area at the gas inlets `0.01 m^2` (default) | scalar with units of area

Flow area at the gas inlets. Inlets **A1** and
**B1** are assumed to be identical in size.

#### Effects and Initial Conditions

### **Enable dynamic compressibility** — Option to model pressure dynamics in the gas channel `On` (default) | `Off`

Option to model the pressure dynamics in the gas channel. If you clear
this checkbox, the block removes the pressure derivative terms from the
component energy and mass conservation equations.

### **Nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Gas temperature at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Gas pressure at nominal operating conditions. The block uses this value to
calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Initial pressure** — Pressure at the start of simulation `0.101325 MPa` (default) | scalar

Pressure in the gas channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial pressure priority** — Pressure parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial pressure**
parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial temperature** — Temperature at the start of simulation `293.15 K` (default) | scalar

Temperature in the gas channel at the start of simulation.

### **Initial temperature priority** — Temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial
temperature** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

## Libraries

Simscape / Fluids / Heat Exchangers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2025a: Optionally model dynamic compressibility

The Specific Dissipation Heat Exchanger Interface (G) block can now optionally model dynamic compressibility by using the **Enable dynamic compressibility** parameter. Previously, this block always modeled pressure dynamics, which can cause models to take longer to achieve steady state. Clear the **Enable dynamic compressibility** parameter to prevent dynamic compressibility modeling.

### R2024a: New block name

The block is now named Specific Dissipation Heat Exchanger Interface (G). It was
previously named Simple Heat Exchanger Interface (G).

## Description

Thermal interface between a gas and its surroundings

The Specific Dissipation Heat Exchanger Interface (G)
block models the pressure drop and temperature change in a gas as it traverses the
length of a thermal interface such as that provided by a heat exchanger. Heat transfer
across the thermal interface is ignored. See the composite block diagram of the
Heat Exchanger
(G-G) block for an example showing how to combine the two
blocks.

The pressure drop is calculated as a function of mass flow rate from tabulated data
specified at some reference pressure and temperature. The calculation is based on linear
interpolation if the mass flow rate is within the bounds of the tabulated data and on
nearest-neighbor extrapolation otherwise. In other words, neighboring data points
connect through straight-line segments, with those at the mass flow rate bounds
extending horizontally outward.

**Linear interpolation (left) and nearest-neighbor extrapolation (right)**

The block calculations rely on the states and properties of the fluid temperature,
density, and specific internal energy at the entrance to the thermal interface. The
entrance changes abruptly from one port to the other during flow reversal, introducing
discontinuities in the values of these variables. To eliminate these discontinuities,
the block smooths the affected variables at mass flow rates below a specified threshold
value.

**Smoothing of entrance temperature below mass flow rate threshold**

### Mass Balance

Mass can enter and exit the thermal interface through ports **A**
and**B**. When you select **Enable dynamic
compressibility**, the mass balance is

∂M∂pdpdt+∂M∂TdTdt=m˙A+m˙B,

where:

- *M* is the mass of the internal fluid volume of the
  thermal interface.
- *p* is the internal fluid pressure.
- *T* is the internal fluid temperature.
- *m˙\** are the mass
  flow rates in through the gas ports.

When you clear the **Enable dynamic compressibility** checkbox,
the mass balance is

m˙A+m˙B=0.

### Energy Balance

Energy can enter and exit the thermal interface in two ways: with fluid flow
through ports **A** and **B** and with heat flow
through port **H**. When you select **Enable dynamic
compressibility**, the energy balance is

∂E∂pdpdt+∂E∂TdTdt=ϕA+ϕB+QH,

where:

- *E* is the total energy in the internal fluid volume
  of the thermal interface.
- *ϕ*\* are the energy flow rates
  in through the gas ports.
- *Q* is the heat flow rate in through the thermal
  port.

If you clear the **Enable dynamic compressibility** checkbox, the
energy balance is

dEdt=ϕA+ϕB+QH,

where the total internal energy is

E=ρ0uV.

The block calculates the constant
*ρ0* from the **Nominal
liquid temperature** and **Nominal liquid pressure**
parameters.

### Momentum Balance

The pressure drop calculation is based entirely on tabulated data that you
specify. The causes of the pressure drop are ignored, except in the effects that
they might have on the specified data. The overall pressure drop from one gas port
to the other is calculated from the individual pressure drops from each gas port to
the internal fluid volume:

pA−pB=ΔpA−ΔpB,

where:

- *p*\* are the fluid pressures
  at the gas ports.
- *Δp*\* are the pressure drops
  from the gas ports to the internal fluid volume:

  Δp\*=p\*−p,

  with *p* as the pressure in the
  internal fluid volume.

The tabulated data is specified at a reference pressure and temperature from which
a third reference parameter, the *reference density*, is
calculated. The ratio of the reference density to the actual port density serves as
a correction factor in the individual pressure drop equations, each defined as:

Δp\*=Δp(m˙\*)ρRρ\*,

where:

- *Δp(m˙)* is the tabulated pressure drop
  function.
- *ρ*\* are the fluid densities
  at the gas ports.

The asterisk denotes the gas port (**A** or
**B**) at which a parameter or variable is defined. Subscript R
denotes a reference value. The density at the interface entrance is smoothed below
the mass flow rate threshold by introducing a hyperbolic term *ɑ*:

ρ\*,smooth=ρ\*(1+α2)+ρ(1−α2),

where *ρ*smooth is the
smoothed density at the entrance port, *ρ*\*
is the unsmoothed density at the same port, and *ρ* is the density
in the internal fluid volume. The hyperbolic smoothing term is defined as:

α=tanh(4m˙avgm˙th),

where *m˙avg* is the average of the
mass flow rates through the gas ports and *m˙th* is the mass flow rate
threshold specified in the block dialog box. This threshold determines the width of
the mass flow rate region over which to smooth the fluid density. The average mass
flow rate is defined as:

m˙avg=m˙A+m˙B2
