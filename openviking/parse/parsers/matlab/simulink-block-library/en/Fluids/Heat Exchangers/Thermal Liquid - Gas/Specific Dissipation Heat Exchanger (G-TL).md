---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'specificdissipationheatexchangergtl'
documentation_source_path: 'ref/specificdissipationheatexchangergtl.html'
language: en
---

# Specific Dissipation Heat Exchanger (G-TL)

## Ports

### Conserving

### **A1** — Gas port gas

Opening for gas to enter and exit its side of the heat exchanger.

### **B1** — Gas port gas

Opening for gas to enter and exit its side of the heat exchanger.

### **A2** — Thermal liquid port thermal liquid

Opening for thermal liquid to enter and exit its side of the heat
exchanger.

### **B2** — Thermal liquid port thermal liquid

Opening for thermal liquid to enter and exit its side of the heat
exchanger.

## Parameters

### Heat Transfer

### **Gas 1 mass flow rate vector, mdot1** — Mass flow rate of gas at each breakpoint in lookup table for specific heat dissipation table numerical array with units of mass over time

Mass flow rate of gas at each breakpoint in the lookup table for the specific heat
dissipation table. The block inter- and extrapolates the breakpoints to obtain the
specific heat dissipation at any mass flow rate. Interpolation is
`linear` and extrapolation is `nearest`.

The mass flow rates can be positive, zero, or negative, but they must increase
monotonically from left to right. Their number must equal the number of rows in the
**Specific heat dissipation** table parameter. If the table has
*m* rows and *n* columns, the mass flow rate
vector must be *m* elements long.

### **Thermal Liquid 2 mass flow rate vector, mdot2** — Mass flow rate of thermal liquid at each breakpoint in lookup table for specific heat dissipation table numerical array with units of mass over time

Mass flow rate of thermal liquid at each breakpoint in the lookup table for the
specific heat dissipation table. The block inter- and extrapolates the breakpoints to
obtain the specific heat dissipation of the heat exchanger at any mass flow rate.
Interpolation is `linear` and extrapolation is
`nearest`.

The mass flow rates can be positive, zero, or negative, but they must increase
monotonically from left to right. Their number must equal the number of columns in the
**Specific heat dissipation table** parameter. If the table has
*m* rows and *n* columns, the mass flow rate
vector must be *n* elements long.

### **Specific heat dissipation table, SD(mdot1, mdot2)** — Specific heat dissipation at each breakpoint in lookup table over mass flow rates of gas and thermal liquid numerical array with units of power over temperature

Specific heat dissipation at each breakpoint in its lookup table over the mass
flow rates of gas and thermal liquid. The block inter- and extrapolates the
breakpoints to obtain the effectiveness at any pair of gas and thermal liquid mass
flow rates. Interpolation is `linear` and extrapolation is
`nearest`.

The specific heat dissipation values must be not be negative. They must align from
top to bottom in order of increasing mass flow rate in the gas channel, and from left
to right in order of increasing mass flow rate in the thermal liquid channel. The
number of rows must equal the size of the **Gas 1 mass flow rate
vector** parameter, and the number of columns must equal the size of the
**Thermal liquid 2 mass flow rate vector** parameter.

If your heat exchanger data sheet supplies the heat transfer coefficients,
multiply the provided heat transfer coefficients by the surface area to calculate the
specific dissipation.

### **Check if violating maximum specific dissipation** — Warning condition for specific heat dissipation in excess of minimum heat capacity rate `Warning` (default) | `None` | `Error`

Warning condition for specific heat dissipation in excess of minimum heat capacity
rate. Heat capacity rate is the product of mass flow rate and specific heat, and its
minimum value is the lowest between the flows. This minimum gives the specific
dissipation for a heat exchanger with maximum effectiveness and cannot be exceeded.
See the Specific Dissipation Heat Transfer block for more detail.

### Gas 1

### **Mass flow rate vector** — Mass flow rate at each breakpoint in lookup table for pressure drop numerical array with units of mass per unit time

Mass flow rate at each breakpoint in the lookup table for the pressure drop. The
block uses linear interpolation and nearest extrapolation to obtain the pressure drop
at any mass flow rate.

The mass flow rates can be positive, zero, or negative and they can span across
laminar, transient, and turbulent zones. The vector must have the same number of
elements as the **Pressure drop vector** parameter and these elements
must increase monotonically from left to right.

### **Pressure drop vector** — Pressure drop at each breakpoint in lookup table over mass flow rate numerical array with units of pressure

Pressure drop at each breakpoint in its lookup table over the mass flow rate. The
block uses linear interpolation and nearest extrapolation to obtain the pressure drop
at any mass flow rate.

The pressure drops can be positive, zero, or negative, and they can span across
laminar, transient, and turbulent zones. The vector must have the same number of
elements as the **Mass flow rate vector** parameter and these
elements must increase monotonically from left to right.

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
discontinuities. See the Simple Heat Exchanger Interface block for detail on the
calculations.

### **Gas 1 volume** — Volume of fluid in the gas flow channel `0.01 m^3` (default) | scalar with units of length cubed

Volume of fluid in the gas flow channel.

### **Cross-sectional area at ports A1 and B1** — Flow area at the inlet and outlet of the flow channel `0.01 m^2` (default) | scalar with units of length squared

Flow area at the inlet and outlet of the gas flow channel. Ports in the same flow
channel are of the same size.

### Thermal Liquid 2

### **Mass flow rate vector** — Mass flow rate at each breakpoint in lookup table for pressure drop numerical array with units of mass per unit time

Mass flow rate at each breakpoint in the lookup table for the pressure drop. The
block uses linear interpolation and nearest extrapolation to obtain the pressure drop
at any mass flow rate.

The mass flow rates can be positive, zero, or negative and they can span across
laminar, transient, and turbulent zones. The vector must have the same number of
elements as the **Pressure drop vector** parameter and these elements
must increase monotonically from left to right.

### **Pressure drop vector** — Pressure drop at each breakpoint in lookup table over mass flow rate numerical array with units of pressure

Pressure drop at each breakpoint in its lookup table over the mass flow rate. The
block uses linear interpolation and nearest extrapolation to obtain the pressure drop
at any mass flow rate.

The pressure drops can be positive, zero, or negative, and they can span across
laminar, transient, and turbulent zones. The vector must have the same number of
elements as the **Mass flow rate vector** parameter and these
elements must increase monotonically from left to right.

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
discontinuities. See the Simple Heat Exchanger Interface block for detail on the
calculations.

### **Thermal Liquid 2 volume** — Volume of fluid in the thermal liquid flow channel `0.01 m^3` (default) | scalar with units of length cubed

Volume of fluid in the thermal liquid flow channel.

### **Cross-sectional area at ports A2 and B2** — Flow area at the inlet and outlet of the flow channel `0.01 m^2` (default) | scalar with units of length squared

Flow area at the inlet and outlet of the thermal liquid flow channel. Ports in the
same flow channel are of the same size.

### Effects and Initial Conditions

### **Enable Gas 1 dynamic compressibility** — Option to model pressure dynamics in the gas channel `On` (default) | `Off`

Option to model the pressure dynamics in the gas channel. If you clear this
checkbox, the block removes the pressure derivative terms from the component energy
and mass conservation equations.

### **Gas 1 nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Gas temperature at nominal operating conditions. The block uses this value to
calculate the nominal density to use in the mass and energy conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Gas 1 dynamic
compressibility** checkbox.

### **Gas 1 nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Gas pressure at nominal operating conditions. The block uses this value to
calculate the nominal density to use in the mass and energy conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Gas 1 dynamic
compressibility** checkbox.

### **Gas 1 initial temperature** — Temperature in the gas channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the gas channel at the start of simulation

### **Gas 1 initial pressure** — Pressure in the gas channel at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the gas channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable Gas 1 dynamic
compressibility**.

### **Enable Thermal Liquid 2 dynamic compressibility** — Option to model pressure dynamics in the thermal liquid channel `On` (default) | `Off`

Option to model the pressure dynamics in the thermal liquid channel. If you clear
this checkbox, the block removes the pressure derivative terms from the component
energy and mass conservation equations. The pressure inside the heat exchanger is then
reduced to the weighted average of the two port pressures.

### **Thermal Liquid 2 initial temperature** — Temperature in the thermal liquid channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the thermal liquid channel at the start of simulation.

### **Enable Thermal Liquid 2 dynamic compressibility** — Option to model pressure dynamics in the thermal liquid channel `On` (default) | `Off`

Option to model the pressure dynamics in the thermal liquid channel. If you clear
this checkbox, the block removes the pressure derivative terms from the component
energy and mass conservation equations. The pressure inside the heat exchanger is then
reduced to the weighted average of the two port pressures.

### **Thermal Liquid 2 nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Thermal liquid temperature at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Thermal Liquid 2 dynamic
compressibility** checkbox.

### **Thermal Liquid 2 nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Thermal liquid pressure at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass and energy conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Thermal Liquid 2 dynamic
compressibility** checkbox.

### **Thermal Liquid 2 initial temperature** — Temperature in the thermal liquid channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the thermal liquid channel at the start of simulation

### **Thermal Liquid 2 initial pressure** — Pressure in the thermal liquid channel at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the thermal liquid channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable Thermal Liquid 2 dynamic
compressibility** .

## Libraries

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Optionally model dynamic compressibility

The Specific Dissipation Heat Exchanger (G-TL) block can now optionally model dynamic compressibility by using the **Enable dynamic compressibility** parameter. Previously, this block always modeled pressure dynamics, which can cause models to take longer to achieve steady state. Clear the **Enable dynamic compressibility** parameter to prevent dynamic compressibility modeling.

### R2024a: Models simple heat exchanger modeling option from Heat Exchanger (G-TL) block

Previously, the Heat Exchanger (G-TL) block
used the **Modeling option** parameter to model two block variants. This
parameter has been removed and the two block variants are now two separate blocks. The
Specific Dissipation Heat Exchanger (G-TL) block uses the heat transfer
model that was previously used when **Modeling option** was
`Simple model`. To use the block model used when
**Modeling option** was `E-NTU Model`, see the
Heat Exchanger (G-TL) block.

## Description

Heat exchanger parameterized by specific dissipation data for systems with gas and thermal liquid flows

The Specific Dissipation Heat Exchanger (G-TL) block models the
complementary cooling and heating of fluids held briefly in thermal contact across a thin
conductive wall. The fluids are single phase with pure gas on one side, pure liquid on the
other. Neither fluid can switch phase and so, as latent heat is never released, the exchange
is strictly one of sensible heat.

Sensible heat exchangers abound in machinery. The fuel heaters that in some jets keep ice
from precipitating in fuel lines and from choking fuel strainers work by blasting bleed air
still hot from the compressor over the fuel lines. The oil coolers that in some motorcycles
keep lubricating oil from overheating work likewise by rushing ram air at ambient temperature
over the oil lines. The bleed and ram air are gas flows and the fuel and oil are thermal
liquid flows.

### Heat Transfer Model

The block heat transfer model depends specific dissipation, which is a measure of the
heat transfer rate observed when gas and thermal liquid inlet temperatures differ by one
degree. Its product with the inlet temperature difference gives the expected heat transfer rate

Q=ξ(TIn,G−TIn,TL),

where *ξ* is specific dissipation and
*TIn* is inlet temperature for gas (subscript
`G`) or thermal liquid (subscript `TL`). The specific
dissipation is a tabulated function of the mass flow rates into the exchanger through the
gas and thermal liquid inlets:

ξ=f(m˙In,G,m˙In,TL),

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

See the Specific Dissipation Heat
Transfer block for more detail on the heat transfer calculations.

### Composite Structure

The block is a composite component. A Specific Dissipation Heat
Exchanger Interface (G) block models the gas flow and a Specific Dissipation Heat
Exchanger Interface (TL) block models the thermal liquid flow. Mass,
momentum, and energy conservation in the flow channels derive from the corresponding
interface blocks. A Specific Dissipation Heat
Transfer block captures the heat exchanged across the wall between the
flows.
