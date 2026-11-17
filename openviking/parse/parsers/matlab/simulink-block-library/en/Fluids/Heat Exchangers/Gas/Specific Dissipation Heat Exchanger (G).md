---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'specificdissipationheatexchangerg'
documentation_source_path: 'ref/specificdissipationheatexchangerg.html'
language: en
---

# Specific Dissipation Heat Exchanger (G)

## Ports
```yaml
ports:
- name: A1
  summary: Gas port gas
  direction: conserving
- name: B1
  summary: Gas port gas
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

### **A1** — Gas port gas

Opening for gas to enter and exit its side of the heat exchanger.

### **B1** — Gas port gas

Opening for gas to enter and exit its side of the heat exchanger.

### **H2** — Entrance temperature of controlled fluid 2 thermal

Entrance temperature of controlled fluid 2.
### Input

### **CP2** — Isobaric specific heat of controlled fluid physical signal

Instantaneous value of the isobaric specific heat for the controlled fluid.

### **M2** — Mass flow rate of controlled fluid physical signal

Instantaneous value of the mass flow rate of the controlled fluid.
## Parameters
```yaml
parameters:
- name: Gas mass flow rate vector, mdot1
  summary: Mass flow rate of gas at each breakpoint in lookup table for specific heat dissipation table numerical array with
    units of mass over time
  group: Heat Transfer
- name: Controlled fluid mass flow rate vector, mdot2
  summary: Mass flow rate of controlled fluid at each breakpoint in lookup table for specific heat dissipation table numerical
    array with units of mass over time
  group: Heat Transfer
- name: Specific heat dissipation table, SD(mdot1,mdot2)
  summary: Specific heat dissipation at each breakpoint in lookup table over mass flow rates of gas and controlled fluid numerical
    array with units of power over temperature
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
- name: Gas volume
  summary: Volume of fluid in the gas flow channel 0.01 m^3 (default) | scalar with units of length cubed
  group: Pressure Loss
- name: Cross-sectional area at ports A1 and B1
  summary: Flow area at the inlet and outlet of the flow channel 0.01 m^2 (default) | scalar with units of length squared
  group: Pressure Loss
- name: Enable Gas dynamic compressibility
  summary: Option to model pressure dynamics in the gas channel On (default) | Off
  group: Effects and Initial Conditions
- name: Gas nominal temperature
  summary: Temperature at nominal operating conditions 293.15 K (default) | scalar
  group: Effects and Initial Conditions
- name: Gas nominal pressure
  summary: Pressure at nominal operating conditions 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
- name: Gas initial temperature
  summary: Temperature in the gas channel at the start of simulation 293.15 K (default) | scalar
  group: Effects and Initial Conditions
- name: Gas initial pressure
  summary: Pressure in the gas channel at the start of simulation 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
```

### Heat Transfer

### **Gas mass flow rate vector, mdot1** — Mass flow rate of gas at each breakpoint in lookup table for specific heat dissipation table numerical array with units of mass over time

Mass flow rate of gas at each breakpoint in the lookup table for the specific heat
dissipation table. The block inter- and extrapolates the breakpoints to obtain the
specific heat dissipation of the heat exchanger at any mass flow rate. Interpolation
is `linear` and extrapolation is `nearest`.

The mass flow rates can be positive, zero, or negative, but they must increase
monotonically from left to right. Their number must equal the number of columns in the
**Specific heat dissipation table** parameter. If the table has
*m* rows and *n* columns, the mass flow rate
vector must be *n* elements long.

### **Controlled fluid mass flow rate vector, mdot2** — Mass flow rate of controlled fluid at each breakpoint in lookup table for specific heat dissipation table numerical array with units of mass over time

Mass flow rate of controlled fluid at each breakpoint in the lookup table for the
specific heat dissipation table. The block inter- and extrapolates the breakpoints to
obtain the specific heat dissipation of the heat exchanger at any mass flow rate.
Interpolation is `linear` and extrapolation is
`nearest`.

The mass flow rates can be positive, zero, or negative, but they must increase
monotonically from left to right. Their number must equal the number of columns in the
**Specific heat dissipation table** parameter. If the table has
*m* rows and *n* columns, the mass flow rate
vector must be *n* elements long.

### **Specific heat dissipation table, SD(mdot1,mdot2)** — Specific heat dissipation at each breakpoint in lookup table over mass flow rates of gas and controlled fluid numerical array with units of power over temperature

Specific heat dissipation at each breakpoint in its lookup table over the mass
flow rates of gas and controlled fluid. The block inter- and extrapolates the
breakpoints to obtain the effectiveness at any pair of gas and controlled fluid mass
flow rates. Interpolation is `linear` and extrapolation is
`nearest`.

The specific heat dissipation values must be not be negative. They must align from
top to bottom in order of increasing mass flow rate in the gas channel, and from left
to right in order of increasing mass flow rate in the controlled fluid channel. The
number of rows must equal the size of the **Gas mass flow rate
vector** parameter, and the number of columns must equal the size of the
**Controlled fluid mass flow rate vector** parameter.

If your heat exchanger data sheet supplies the heat transfer coefficients,
multiply the provided heat transfer coefficients by the surface area to calculate the
specific dissipation.

### **Check if violating maximum specific dissipation** — Warning condition for specific heat dissipation in excess of minimum heat capacity rate `Warning` (default) | `None` | `Error`

Warning condition for specific heat dissipation in excess of minimum heat capacity
rate. Heat capacity rate is the product of mass flow rate and specific heat, and its
minimum value is the lowest between the flows. This minimum gives the specific
dissipation for a heat exchanger with maximum effectiveness and cannot be exceeded.
See the Specific Dissipation
Heat Transfer block for more detail.

### Pressure Loss

### **Mass flow rate vector** — Mass flow rate at each breakpoint in lookup table for pressure drop numerical array with units of mass per unit time

Mass flow rate at each breakpoint in the lookup table for the pressure drop. The
block inter- and extrapolates the breakpoints to obtain the pressure drop at any mass
flow rate. Interpolation is `linear` and extrapolation is
`nearest`.

The mass flow rates can be positive, zero, or negative and they can span across
laminar, transient, and turbulent zones. They must, however, increase monotonically
from left to right. Their number must equal the size of the **Pressure drop
vector** parameter, with which they are to combine to complete the
tabulated breakpoints.

### **Pressure drop vector** — Pressure drop at each breakpoint in lookup table over mass flow rate numerical array with units of pressure

Pressure drop at each breakpoint in its lookup table over the mass flow rate. The
block inter- and extrapolates the breakpoints to obtain the pressure drop at any mass
flow rate. Interpolation is `linear` and extrapolation is
`nearest`.

The pressure drops can be positive, zero, or negative, and they can span across
laminar, transient, and turbulent zones. They must, however, increase monotonically
from left to right. Their number must equal the size of the **Mass flow rate
vector** parameter, with which they are to combine to complete the
tabulated breakpoints.

### **Reference inflow temperature** — Absolute inlet temperature assumed in tabulated data `293.15 K` (default) | scalar with units of temperature

Absolute temperature established at the inlet in the gathering of the tabulated
pressure drops. The reference inflow temperature and pressure determine the fluid
density assumed in the tabulated data. During simulation, the ratio of reference to
actual fluid densities multiplies the tabulated pressure drop to obtain the actual
pressure drop.

### **Reference inflow pressure** — Absolute inlet pressure assumed in tabulated data `0.101325 MPa` (default) | scalar with units of pressure

Absolute pressure established at the inlet in the gathering of the tabulated
pressure drops. The reference inflow temperature and pressure determine the fluid
density assumed in the tabulated data. During simulation, the ratio of reference to
actual fluid densities multiplies the tabulated pressure drop to obtain the actual
pressure drop.

### **Mass flow rate threshold for flow reversal** — Upper bound of numerically smooth region for mass flow rate `1e-3 kg/s` (default) | scalar with units of mass/time

Mass flow rate below which its value is numerically smoothed to avoid
discontinuities known to produce simulation errors at zero flow. See the
Specific Dissipation
Heat Exchanger Interface (G) block for detail on the calculations
for the gas side of the exchanger.

### **Gas volume** — Volume of fluid in the gas flow channel `0.01 m^3` (default) | scalar with units of length cubed

Volume of fluid in the gas flow channel.

### **Cross-sectional area at ports A1 and B1** — Flow area at the inlet and outlet of the flow channel `0.01 m^2` (default) | scalar with units of length squared

Flow area at the inlet and outlet of the gas flow channel. The ports are of the
same size.

### Effects and Initial Conditions

### **Enable Gas dynamic compressibility** — Option to model pressure dynamics in the gas channel `On` (default) | `Off`

Option to model the pressure dynamics in the gas channel. If you clear this
checkbox, the block removes the pressure derivative terms from the component energy
and mass conservation equations.

### **Gas nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Gas temperature at nominal operating conditions. The block uses this value to
calculate the nominal density to use in the mass and energy conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Gas dynamic
compressibility** checkbox.

### **Gas nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Gas pressure at nominal operating conditions. The block uses this value to
calculate the nominal density to use in the mass and energy conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Gas dynamic
compressibility** checkbox.

### **Gas initial temperature** — Temperature in the gas channel at the start of simulation `293.15 K` (default) | scalar

Temperature in the gas channel at the start of simulation.

### **Gas initial pressure** — Pressure in the gas channel at the start of simulation `0.101325 MPa` (default) | scalar

Pressure in the gas channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable Gas dynamic
compressibility** .
## Libraries

Simscape / Fluids / Heat Exchangers / Gas

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Optionally model dynamic compressibility

The Specific Dissipation Heat Exchanger (G) block can now optionally model dynamic compressibility by using the **Enable dynamic compressibility** parameter. Previously, this block always modeled pressure dynamics, which can cause models to take longer to achieve steady state. Clear the **Enable dynamic compressibility** parameter to prevent dynamic compressibility modeling.

### R2024a: Models simple heat exchanger modeling option from Heat Exchanger (G) block

Previously, the Heat Exchanger
(G) block used the **Modeling option** parameter to model
two block variants. This parameter has been removed and the two block variants are now two
separate blocks. The Specific Dissipation Heat Exchanger (G) block uses the
heat transfer model that was previously used when **Modeling option** was
`Simple model`. To use the block model used when
**Modeling option** was `E-NTU Model`, see the
Heat Exchanger (G) block.

## Description

Heat exchanger parameterized by specific dissipation data for systems with gas and controlled flows

The Specific Dissipation Heat Exchanger (G) block models
heat exchange between a gas, which flows between ports **A1** and
**B1**, and an external, *controlled* fluid via a
physical signal.

### Heat Transfer Model

The block heat transfer model depends on the concept of *specific
dissipation*, a measure of the heat transfer rate observed when gas and
controlled fluid inlet temperatures differ by one degree. Its product with the inlet
temperature difference gives the expected heat transfer rate:

Q=ξ(TIn,1−TIn,2),

where *ξ* is specific dissipation and
*T*In is inlet temperature for gas (subscript
`1`) or controlled fluid (subscript `2`). The specific
dissipation is a tabulated function of the mass flow rates into the exchanger through the
gas and controlled fluid inlets:

ξ=f(m˙1,m˙2)

To accommodate reverse flows, the tabulated data can extend over positive
and negative flow rates, in which case the inlets can also be thought of as outlets.

The specific dissipation is the heat exchanger heat transfer rate divided by the
difference in inlet temperatures

ξ=QTIn,1−TIn,2.

The specific dissipation is also equal to the overall heat transfer coefficient defined
based on inlet temperature multiplied by the heat transfer surface area or the heat capacity
rate multiplied by the effectiveness factor, for whichever fluid has a smaller value.

The heat transfer model, as it relies almost entirely on tabulated data, and as that
data normally derives from experiment, requires little detail about the exchanger. Flow
arrangement, mixing condition, and number of shell or tube passes, if relevant to the heat
exchanger modeled, are assumed to manifest entirely in the tabulated data.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Composite Structure

The block is a composite component. A Specific Dissipation Heat
Exchanger Interface (G) block models the gas flow. Physical signals for
the heat transfer coefficient and mass flow rate, along with a thermal port for temperature,
capture the controlled flow. A Specific Dissipation Heat
Transfer block models the heat exchanged across the wall between the
flows.
