---
type: simulink-block
title: 'Specific Dissipation Heat Transfer'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'specificdissipationheattransfer'
documentation_source_path: 'ref/specificdissipationheattransfer.html'
language: en
---

# Specific Dissipation Heat Transfer

## Ports

### Input

### **CP1** — Isobaric specific heat of controlled fluid 1 physical signal

Isobaric specific heat of controlled fluid 1.

### **CP2** — Isobaric specific heat of controlled fluid 2 physical signal

Isobaric specific heat of controlled fluid 2.

### **M1** — Entrance mass flow rate of controlled fluid 1 physical signal

Entrance mass flow rate of controlled fluid 1. Positive mass flow rate
values correspond to specific dissipation values for normal operating
conditions. Specific dissipation values obtained during reversed flow
correspond to negative mass flow rate values.

### **M2** — Entrance mass flow rate of controlled fluid 2 physical signal

Entrance mass flow rate of controlled fluid 2. Positive mass flow rate
values correspond to specific dissipation values for normal operating
conditions. Specific dissipation values obtained during reversed flow
correspond to negative mass flow rate values.
### Conserving

### **H1** — Entrance temperature of controlled fluid 1 thermal

Entrance temperature of controlled fluid 1.

### **H2** — Entrance temperature of controlled fluid 2 thermal

Entrance temperature of controlled fluid 2.

## Parameters

### **Thermal Liquid mass flow rate vector, mdot1** — Entrance mass flow rate at which to specify specific-dissipation data `[.3, .5, .6, .7, 1, 1.4, 1.9, 2.3] kg/s` (default) | *M*-element array with units of mass/time

Array of mass flow rates at the inlet for controlled fluid 1. Each value
corresponds to a row in the specific dissipation lookup table. Positive mass
flow rate values correspond to specific dissipation values for normal
operating conditions. Specific dissipation values obtained during reversed
flow correspond to negative mass flow rate values.

### **Controlled fluid mass flow rate vector, mdot2** — Entrance mass flow rate at which to specify specific-dissipation data `[.3, .5, 1, 1.3, 1.7, 2, 2.6, 3.3] kg/s` (default) | *N*-element array with units of mass/time

Array of mass flow rates at the inlet for controlled fluid 2. Each value
corresponds to a row in the specific dissipation lookup table. Positive mass
flow rate values correspond to specific dissipation values for normal
operating conditions. Specific dissipation values obtained during reversed
flow correspond to negative mass flow rate values.

### **Specific dissipation table, SD(mdot1, mdot2)** — Specific dissipation values corresponding to specified mass flow rates 8-by-8 matrix with units of `kW/K` (default) | *M*-by-*N* matrix with units of power/temperature

Matrix of specific dissipation values corresponding to the specified mass
flow rate arrays for controlled fluids 1 and 2. The block uses the tabulated
data to calculate the heat transfer at the simulated operating
conditions.

If your heat exchanger data sheet supplies the heat transfer coefficients
based on inlet temperatures, multiply the provided heat transfer
coefficients by the surface area to calculate the specific dissipation.

### **Mass flow rate threshold for flow reversal** — Mass flow rate below which to smooth numerical data `1e-3 kg/s` (default) | scalar with units of mass/time

Mass flow rate below which to initiate a smooth flow reversal to prevent
discontinuities in the simulation data.

### **Check if violating maximum specific dissipation** — Option to warn if the specific dissipation exceeds the maximum allowed value `Warning` (default) | `None` | `Error`

Option to warn if the specific dissipation exceeds the maximum value
described in the block description.

## Libraries

Simscape / Fluids / Heat Exchangers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Simple heat transfer model between two general fluids

The Specific Dissipation Heat Transfer block models the
heat transfer between two fluids given only minimal knowledge of component parameters.
The fluids are controlled by physical signals, with these providing the entrance mass
flow rate and isobaric specific heat for each. Thermal ports set the entrance
temperatures of the fluids.

The rate of heat transfer is calculated from the specific dissipation, a parameter
specified in tabulated form as a function of the entrance mass flow rates. The specific
dissipation quantifies the amount of heat exchanged between the fluids per unit of time
when the entrance temperatures differ by one degree.

This block does not model pressure losses and other aspects of flow mechanics. These
effects are captured by the heat exchanger interface blocks. Combine this block with
either the Specific Dissipation
Heat Exchanger Interface (G) or Specific Dissipation
Heat Exchanger Interface (TL) blocks to model a heat exchanger.

### Heat Transfer Rate

Heat flows from the warmer fluid to the cooler fluid, at a rate proportional to
the difference between the fluid entrance temperatures. The heat flow rate is
positive if fluid 1 enters at a higher temperature than fluid 2 and therefore if
heat flows from fluid 1 to fluid 2:

Q=ξ(TIn,1−TIn,2),

where *T*\*,in are the
fluid entrance temperatures, determined by the conditions at thermal port
**H1** for fluid 1 and **H2** for fluid 2.
*ξ* is the specific dissipation obtained from the specified
tabulated data at the given mass flow rates:

ξ=f(m˙1,m˙2)

where m˙ are the entrance mass flow rates, specified through physical
signal port **M1** for fluid 1 and **M2** for
fluid 2.

The specific dissipation is the heat exchanger heat transfer rate divided by the
difference in inlet temperatures

ξ=QTIn,1−TIn,2.

The specific dissipation is also equal to the overall heat transfer coefficient
defined based on inlet temperature multiplied by the heat transfer surface area or
the heat capacity rate multiplied by the effectiveness factor, for whichever fluid
has a smaller value.

**Maximum Heat Transfer Rate**

The heat transfer rate is constrained so that the specific dissipation used in
the calculations can never exceed the maximum value:

ξmax=min(C1,C2),

where *C*\* are the
thermal capacity rates of the controlled fluids, each defined as:

C\*=m˙\*cp,\*,

with *c*p,\* denoting
the isobaric specific heat of the fluid, specified through physical signal port
**CP1** for fluid 1 and **CP2** for fluid
2. The constraint on the maximum heat transfer rate is implemented in the form
of a piecewise function:

Q={ξmax(T1,in−T2,in),if SD>SDmaxξ(T1,in−T2,in),otherwise,

The block issues a warning whenever the heat flow rate
exceeds the maximum value, if the **Check if violating maximum specific
dissipation** parameter is
`Warning`.
