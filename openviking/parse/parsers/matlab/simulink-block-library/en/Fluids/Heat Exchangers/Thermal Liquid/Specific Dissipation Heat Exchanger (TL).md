---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'specificdissipationheatexchangertl'
documentation_source_path: 'ref/specificdissipationheatexchangertl.html'
language: en
---

# Specific Dissipation Heat Exchanger (TL)

## Ports
```yaml
ports:
- name: A1
  summary: Thermal liquid port thermal liquid
  direction: conserving
- name: B1
  summary: Thermal liquid port thermal liquid
  direction: conserving
- name: H2
  summary: Entrance temperature of controlled fluid 2 thermal
  direction: conserving
- name: CP2
  summary: Isobaric specific heat of controlled fluid physical signal
  direction: input
- name: M2
  summary: Mass flow rate of controlled fluid physical signal
  direction: input
```

### Conserving

### **A1** — Thermal liquid port thermal liquid

Opening for thermal liquid to enter and exit its side of the heat
exchanger.

### **B1** — Thermal liquid port thermal liquid

Opening for thermal liquid to enter and exit its side of the heat
exchanger.

### **H2** — Entrance temperature of controlled fluid 2 thermal

Entrance temperature of controlled fluid 2.
### Input

### **CP2** — Isobaric specific heat of controlled fluid physical signal

Instantaneous value of the isobaric specific heat for the controlled
fluid.

### **M2** — Mass flow rate of controlled fluid physical signal

Instantaneous value of the mass flow rate of the controlled
fluid.
## Parameters
```yaml
parameters:
- name: Thermal liquid mass flow rate vector, mdot1
  summary: Mass flow rate of thermal liquid at each breakpoint in lookup table for specific heat dissipation table numerical
    array with units of mass over time
  group: Heat Transfer
- name: Controlled fluid mass flow rate vector, mdot2
  summary: Mass flow rate of controlled fluid at each breakpoint in lookup table for specific heat dissipation table numerical
    array with units of mass over time
  group: Heat Transfer
- name: Specific heat dissipation table, SD(mdot1,mdot2)
  summary: Specific heat dissipation at each breakpoint in lookup table over mass flow rates of thermal liquid and controlled
    fluid numerical array with units of power over temperature
  group: Heat Transfer
- name: Check if violating maximum specific dissipation
  summary: Warning condition for specific heat dissipation in excess of minimum heat capacity rate Warning (default) | None
    | Error
  group: Heat Transfer
- name: Mass flow rate vector
  summary: Mass flow rate at each breakpoint in lookup table for pressure drop numerical array with units of mass per unit
    time
  group: Pressure Loss
- name: Pressure drop vector
  summary: Pressure drop at each breakpoint in lookup table over mass flow rate numerical array with units of pressure
  group: Pressure Loss
- name: Reference inflow temperature
  summary: Absolute inlet temperature assumed in tabulated data 293.15 K (default) | scalar with units of temperature
  group: Pressure Loss
- name: Reference inflow pressure
  summary: Absolute inlet pressure assumed in tabulated data 0.101325 MPa (default) | scalar with units of pressure
  group: Pressure Loss
- name: Mass flow rate threshold for flow reversal
  summary: Upper bound of numerically smooth region for mass flow rate 1e-3 kg/s (default) | scalar with units of mass/time
  group: Pressure Loss
- name: Thermal liquid volume
  summary: Volume of fluid in the thermal liquid flow channel 0.01 m^3 (default) | scalar with units of length cubed
  group: Pressure Loss
- name: Cross-sectional area at ports A1 and B1
  summary: Flow area at the inlet and outlet of the flow channel 0.01 m^2 (default) | scalar with units of length squared
  group: Pressure Loss
- name: Enable Thermal Liquid dynamic compressibility
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

### Heat Transfer

### **Thermal liquid mass flow rate vector, mdot1** — Mass flow rate of thermal liquid at each breakpoint in lookup table for specific heat dissipation table numerical array with units of mass over time

Mass flow rate of thermal liquid at each breakpoint in the lookup
table for the specific heat dissipation table. The block inter- and
extrapolates the breakpoints to obtain the specific heat dissipation of
the heat exchanger at any mass flow rate. Interpolation is
`linear` and extrapolation is
`nearest`.

The mass flow rates can be positive, zero, or negative, but they must
increase monotonically from left to right. Their number must equal the
number of columns in the **Specific heat dissipation
table** parameter. If the table has *m*
rows and *n* columns, the mass flow rate vector must
be *n* elements long.

### **Controlled fluid mass flow rate vector, mdot2** — Mass flow rate of controlled fluid at each breakpoint in lookup table for specific heat dissipation table numerical array with units of mass over time

Mass flow rate of controlled fluid at each breakpoint in the lookup
table for the specific heat dissipation table. The block inter- and
extrapolates the breakpoints to obtain the specific heat dissipation of
the heat exchanger at any mass flow rate. Interpolation is
`linear` and extrapolation is
`nearest`.

The mass flow rates can be positive, zero, or negative, but they must
increase monotonically from left to right. Their number must equal the
number of columns in the **Specific heat dissipation
table** parameter. If the table has *m*
rows and *n* columns, the mass flow rate vector must
be *n* elements long.

### **Specific heat dissipation table, SD(mdot1,mdot2)** — Specific heat dissipation at each breakpoint in lookup table over mass flow rates of thermal liquid and controlled fluid numerical array with units of power over temperature

Specific heat dissipation at each breakpoint in its lookup table over
the mass flow rates of thermal liquid and controlled fluid. The block
inter- and extrapolates the breakpoints to obtain the effectiveness at
any pair of thermal liquid and controlled fluid mass flow rates.
Interpolation is `linear` and extrapolation is
`nearest`.

The specific heat dissipation values must be not be negative. They
must align from top to bottom in order of increasing mass flow rate in
the thermal liquid channel, and from left to right in order of
increasing mass flow rate in the controlled fluid channel. The number of
rows must equal the size of the **Thermal liquid mass flow rate
vector** parameter, and the number of columns must equal
the size of the **Controlled fluid mass flow rate
vector** parameter.

If your heat exchanger data sheet supplies the heat transfer
coefficients, multiply the provided heat transfer coefficients by the
surface area to calculate the specific dissipation.

### **Check if violating maximum specific dissipation** — Warning condition for specific heat dissipation in excess of minimum heat capacity rate `Warning` (default) | `None` | `Error`

Warning condition for specific heat dissipation in excess of minimum
heat capacity rate. Heat capacity rate is the product of mass flow rate
and specific heat, and its minimum value is the lowest between the
flows. This minimum gives the specific dissipation for a heat exchanger
with maximum effectiveness and cannot be exceeded. See the
Specific Dissipation Heat Transfer block for more
detail.

### Pressure Loss

### **Mass flow rate vector** — Mass flow rate at each breakpoint in lookup table for pressure drop numerical array with units of mass per unit time

Mass flow rate at each breakpoint in the lookup table for the pressure
drop. The block inter- and extrapolates the breakpoints to obtain the
pressure drop at any mass flow rate. Interpolation is
`linear` and extrapolation is
`nearest`.

The mass flow rates can be positive, zero, or negative and they can
span across laminar, transient, and turbulent zones. They must, however,
increase monotonically from left to right. Their number must equal the
size of the **Pressure drop vector** parameter, with
which they are to combine to complete the tabulated breakpoints.

### **Pressure drop vector** — Pressure drop at each breakpoint in lookup table over mass flow rate numerical array with units of pressure

Pressure drop at each breakpoint in its lookup table over the mass
flow rate. The block inter- and extrapolates the breakpoints to obtain
the pressure drop at any mass flow rate. Interpolation is
`linear` and extrapolation is
`nearest`.

The pressure drops can be positive, zero, or negative, and they can
span across laminar, transient, and turbulent zones. They must, however,
increase monotonically from left to right. Their number must equal the
size of the **Mass flow rate vector** parameter, with
which they are to combine to complete the tabulated breakpoints.

### **Reference inflow temperature** — Absolute inlet temperature assumed in tabulated data `293.15 K` (default) | scalar with units of temperature

Absolute temperature established at the inlet in the gathering of the
tabulated pressure drops. The reference inflow temperature and pressure
determine the fluid density assumed in the tabulated data. During
simulation, the ratio of reference to actual fluid densities multiplies
the tabulated pressure drop to obtain the actual pressure drop.

### **Reference inflow pressure** — Absolute inlet pressure assumed in tabulated data `0.101325 MPa` (default) | scalar with units of pressure

Absolute pressure established at the inlet in the gathering of the
tabulated pressure drops. The reference inflow temperature and pressure
determine the fluid density assumed in the tabulated data. During
simulation, the ratio of reference to actual fluid densities multiplies
the tabulated pressure drop to obtain the actual pressure drop.

### **Mass flow rate threshold for flow reversal** — Upper bound of numerically smooth region for mass flow rate `1e-3 kg/s` (default) | scalar with units of mass/time

Mass flow rate below which its value is numerically smoothed to avoid
discontinuities known to produce simulation errors at zero flow. See the
Specific Dissipation Heat Exchanger Interface (TL)
block (on which the `Simple Model` variant is
based) for detail on the calculations for the thermal liquid side of the
exchanger.

### **Thermal liquid volume** — Volume of fluid in the thermal liquid flow channel `0.01 m^3` (default) | scalar with units of length cubed

Volume of fluid in the thermal liquid flow channel.

### **Cross-sectional area at ports A1 and B1** — Flow area at the inlet and outlet of the flow channel `0.01 m^2` (default) | scalar with units of length squared

Flow area at the inlet and outlet of the thermal liquid flow channel.
The ports are of the same size.

### Effects and Initial Conditions

### **Enable Thermal Liquid dynamic compressibility** — Setting for liquid compressibility in heat exchanger `On` (default) | `Off` | scalar

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

To enable this parameter, clear the **Enable Thermal
Liquid dynamic compressibility** checkbox.

### **Thermal Liquid nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Thermal liquid pressure at nominal operating conditions. The block
uses this value to calculate the nominal density to use in the mass and
energy conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable Thermal
Liquid dynamic compressibility** checkbox.

### **Thermal Liquid initial temperature** — Temperature in the thermal liquid channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the thermal liquid channel at the start of
simulation

### **Thermal Liquid initial pressure** — Pressure in the thermal liquid channel at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the thermal liquid channel at the start of
simulation.

#### Dependencies

To enable this parameter, select **Enable Thermal Liquid
dynamic compressibility** .
## Libraries

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2024a: Models simple heat exchanger modeling option from Heat Exchanger (TL) block

Previously, the Heat Exchanger (TL) block used
the **Modeling option** parameter to model two block variants. This
parameter has been removed and the two block variants are now two separate blocks.
The Specific Dissipation Heat Exchanger (TL) block uses the heat
transfer model that was previously used when **Modeling option**
was `Simple model`. To use the block model used when
**Modeling option** was `E-NTU Model`,
see the Heat Exchanger (TL) block.

## Description

Heat exchanger parameterized by specific dissipation data for systems with thermal liquid and controlled flows

The Specific Dissipation Heat Exchanger (TL) block
models the cooling and heating of fluids through conduction over a thin wall. The
properties of a single-phase thermal liquid are defined on the **Thermal
Liquid** tab. The second fluid is a controlled fluid, which is specified
only by the user-defined parameters on the **Controlled Fluid** tab. It
does not receive any properties from the domain fluid network. The heat exchange between
the fluids is based on the thermal liquid sensible heat.

### Heat Transfer Model

Heat transfer by the simple model is based on specific dissipation:

Q=ξ(TIn,Th−TIn,C),

where:

- *ξ* is specific dissipation, which is a function of
  the mass flow rates of the thermal and controlled liquids.
- *TIn,Th* is the thermal liquid
  inlet temperature.
- *TIn,C* is the controlled
  liquid inlet temperature.

The simple model is based on linear interpolation of user-provided
tabulated data and does not capture individual features of the heat
exchanger.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Composite Structure

The Heat Exchanger (TL) block is a composite of the Specific
Dissipation Heat Exchanger Interface (TL) and Specific
Dissipation Heat Transfer blocks:
