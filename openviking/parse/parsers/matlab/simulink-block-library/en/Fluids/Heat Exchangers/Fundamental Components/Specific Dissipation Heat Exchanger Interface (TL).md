---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger Interface (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'specificdissipationheatexchangerinterfacetl'
documentation_source_path: 'ref/specificdissipationheatexchangerinterfacetl.html'
language: en
---

# Specific Dissipation Heat Exchanger Interface (TL)

## Ports
```yaml
ports:
- name: CP
  summary: Isobaric specific heat of the thermal liquid, kJ/(kg*K) physical signal
  direction: output
- name: M
  summary: Mass flow rate of the thermal liquid, kg/s physical signal
  direction: output
- name: A
  summary: Fluid opening thermal liquid
  direction: conserving
- name: B
  summary: Fluid opening thermal liquid
  direction: conserving
- name: H
  summary: Thermal condition at the fluid entrance thermal
  direction: conserving
```

### Output

### **CP** — Isobaric specific heat of the thermal liquid, `kJ/(kg*K)` physical signal

Isobaric specific heat of the thermal liquid in the internal fluid
volume of the thermal interface.

### **M** — Mass flow rate of the thermal liquid, `kg/s` physical signal

Mass flow rate of the thermal liquid in the interior of the thermal
interface. The output signal is positive when the flow rate is directed
from port **A** to port **B** and
negative otherwise.
### Conserving

### **A** — Fluid opening thermal liquid

Opening through which thermal liquid can enter and exit the thermal
interface.

### **B** — Fluid opening thermal liquid

Opening through which thermal liquid can enter and exit the thermal
interface.

### **H** — Thermal condition at the fluid entrance thermal

Thermal port used to set the thermal condition at the thermal liquid
port serving as the thermal liquid entrance.
## Parameters
```yaml
parameters:
- name: Mass flow rate vector
  summary: Mass flow rates at which to specify pressure-drop data [.3, .5, 1, 1.5, 2, 2.5] kg/s (default) | *K*-element array
    with units of mass/time
  group: ''
- name: Pressure drop vector
  summary: Pressure-drop data corresponding to specified mass flow rates [3, 5, 10, 25, 35, 50] * 1e-3 MPa (default) | *K*-element
    array with units of pressure
  group: ''
- name: Reference inflow temperature
  summary: Temperature at which pressure-drop data is specified 293.15 K (default) | scalar with units of temperature
  group: ''
- name: Reference inflow pressure
  summary: Pressure at which pressure-drop tabulated data is specified 0.101325 MPa (default) | scalar with units of pressure
  group: ''
- name: Mass flow rate threshold for flow reversal
  summary: Mass flow rate below which to smooth numerical data 1e-6 kg/s (default) | scalar with units of mass/time
  group: ''
- name: Thermal Liquid volume
  summary: Volume of thermal liquid inside the heat exchanger 0.01 m^3 (default) | scalar with units of volume
  group: ''
- name: Cross-sectional area at ports A1 and B1
  summary: Flow area at the thermal liquid inlets 0.01 m^2 (default) | scalar with units of area
  group: ''
- name: Enable dynamic compressibility
  summary: Setting for liquid compressibility in heat exchanger On (default) | Off | scalar
  group: Effects and Initial Conditions
- name: Thermal Liquid nominal temperature
  summary: Temperature at nominal operating conditions 293.15 K (default) | scalar
  group: Effects and Initial Conditions
- name: Thermal Liquid nominal pressure
  summary: Pressure at nominal operating conditions 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
- name: Thermal Liquid initial temperature
  summary: Temperature in the thermal liquid channel at the start of simulation 293.15 K (default) | scalar with units of
    temperature
  group: Effects and Initial Conditions
- name: Thermal Liquid initial pressure
  summary: Pressure in the thermal liquid channel at the start of simulation 0.101325 MPa (default) | scalar with units of
    pressure
  group: Effects and Initial Conditions
```

#### Pressure Loss Tab

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

### **Thermal Liquid volume** — Volume of thermal liquid inside the heat exchanger `0.01 m^3` (default) | scalar with units of volume

Volume of thermal liquid occupying the heat exchanger at any given time.
The initial conditions specified in the **Effects and Initial
Conditions** tab apply to this volume. The volume is constant
during simulation.

### **Cross-sectional area at ports A1 and B1** — Flow area at the thermal liquid inlets `0.01 m^2` (default) | scalar with units of area

Flow area at the thermal liquid inlets. Inlets **A1** and
**B1** are assumed to be identical in size.

### Effects and Initial Conditions

### **Enable dynamic compressibility** — Setting for liquid compressibility in heat exchanger `On` (default) | `Off` | scalar

Option to model the pressure dynamics inside the heat exchanger.
Setting this parameter to `Off` removes the
pressure derivative terms from the component energy and mass
conservation equations. The pressure inside the heat exchanger is then
reduced to the weighted average of the two port pressures.

### **Thermal Liquid nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Thermal liquid temperature at nominal operating conditions. The block
uses this value to calculate the nominal density to use in the mass and
energy conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Thermal Liquid nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Thermal liquid pressure at nominal operating conditions. The block
uses this value to calculate the nominal density to use in the mass and
energy conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Thermal Liquid initial temperature** — Temperature in the thermal liquid channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the thermal liquid channel at the start of
simulation

### **Thermal Liquid initial pressure** — Pressure in the thermal liquid channel at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the thermal liquid channel at the start of
simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.
## Libraries

Simscape / Fluids / Heat Exchangers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024a: New block name

The block is now named Specific Dissipation Heat Exchanger Interface (TL). It was
previously named Simple Heat Exchanger Interface (TL).

## Description

Thermal interface between a thermal liquid and its surroundings

The Specific Dissipation Heat Exchanger Interface (TL)
block models the pressure drop and temperature change in a thermal liquid as it
traverses the length of a thermal interface such as that provided by a heat exchanger.
Heat transfer across the thermal interface is ignored. See the composite block diagram
of the Heat Exchanger (TL-TL) block for an
example showing how to combine the two blocks.

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
and **B**. The volume of the interface is fixed but the
compressibility of the fluid means that the mass inside the interface can change
with pressure and temperature. Whether compressibility is factored into the block
calculations depends on the setting of the **Enable dynamic
compressibility** parameter in the **Effects and Initial
Conditions** tab:

m˙A+m˙B={(dpdt1β−dTdtα)ρV,if Thermal Liquid dynamic compressibility is On0,otherwise,

where:

- *m˙\** are the mass
  flow rates in through the thermal liquid ports.
- *p* is the internal fluid pressure.
- *T* is the internal fluid temperature.
- *α* is the isobaric thermal expansion
  coefficient.
- *β* is the isothermal bulk modulus.
- *ρ* is the internal fluid density.
- *V* is the internal fluid volume.

If you clear the **Enable dynamic compressibility** checkbox, the
fluid is treated as incompressible and the mass flow rate in through one thermal
liquid port must exactly equal that out through the other thermal liquid port. The
rate of mass accumulation is, in this case, zero.

### Energy Balance

Energy can enter and exit the thermal interface in two ways: with fluid flow
through ports **A** and **B** and with heat flow
through port **H**. If you select **Enable dynamic
compressibility**, the energy balance is

∂E∂pdpdt+∂E∂TdTdt=ϕA+ϕB+QH,

where:

- *E* is the total energy in the internal fluid volume
  of the thermal interface.
- *ϕ*\* are the energy flow rates
  in through the thermal liquid ports.
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
they might have on the specified data. The overall pressure drop from one thermal
liquid port to the other is calculated from the individual pressure drops from each
thermal liquid port to the internal fluid volume:

pA−pB=ΔpA−ΔpB,

where:

- *p*\* are the fluid pressures
  at the thermal liquid ports.
- *Δp*\* are the pressure drops
  from the thermal liquid ports to the internal fluid volume:

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
  at the thermal liquid ports.

The asterisk denotes the thermal liquid port (**A** or
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
mass flow rates through the thermal liquid ports and *m˙th* is the mass flow rate
threshold specified in the block dialog box. This threshold determines the width of
the mass flow rate region over which to smooth the fluid density. The average mass
flow rate is defined as:

m˙avg=m˙A+m˙B2
