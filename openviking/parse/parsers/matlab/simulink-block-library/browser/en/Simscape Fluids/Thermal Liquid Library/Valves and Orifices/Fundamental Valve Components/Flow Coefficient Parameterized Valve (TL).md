---
type: simulink-block
title: 'Flow Coefficient Parameterized Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Valves and Orifices / Fundamental Valve Components'
documentation_page: 'flowcoefficientparameterizedvalvetl'
documentation_source_path: 'ref/flowcoefficientparameterizedvalvetl.html'
language: en
---

# Flow Coefficient Parameterized Valve (TL)

## Ports

### Input

### **L** — Valve control signal, `unitless` physical signal

Port through which to specify the signal that controls the opening of
the valve (in certain valve types associated with
*stroke* or *lift percent*).
The valve is fully closed at a value of `0` and fully
open at a value of `1`.
### Conserving

### **A** — Flow passage thermal liquid

Opening through which the flow can enter or exit the flow resistance.
Which of the ports serves as inlet and which as outlet depends on the
direction of flow.

### **B** — Flow passage thermal liquid

Opening through which the flow can enter or exit the flow resistance.
Which of the ports serves as inlet and which as outlet depends on the
direction of flow.

## Parameters

### **Flow coefficient specification** — Parameterization by which to specify the flow coefficient of the valve `Cv coefficient (USG/min)` (default) | `Kv coefficient (m^3/h)`

Choice of flow coefficient to specify.
*C*v and
*K*v differ
in the physical conditions of their measurement and in the physical units of
their expression. Generally at least one of these is reported in product
data sheets provided by the manufacturer. Select the option for which data
is available.

### **Cv coefficient at maximum flow** — Flow coefficient expressed in imperial units for a maximally open valve `1` (default) | positive scalar in units of USG/min

Flow coefficient expressed in imperial units for a valve opened to full
capacity. This is the value reported in the valve data sheets when the
*C*v
coefficient is provided by the manufacturer.

### **Kv coefficient at maximum flow** — Flow coefficient expressed in SI units for a maximally open valve `1` (default) | positive scalar in units of m^3/h

Flow coefficient expressed in SI units for a valve opened to full
capacity. This is the value reported in the valve data sheets when the
*K*v
coefficient is provided by the manufacturer.

### **Cv coefficient at minimum flow** — Flow coefficient expressed in imperial units for a maximally closed valve `1e-4` (default) | positive scalar in units of USG/min

Flow coefficient expressed in imperial units for a valve that is closed
tight and devoid of all flow except for that due to internal leakage between
port **A** and port **B**. The primary
purpose of this parameter is to ensure the numerical robustness of the model
during simulation. Its exact value is less important than its being a very
small number greater than zero.

### **Kv coefficient at minimum flow** — Flow coefficient expressed in SI units for a maximally closed valve `1e-4` (default) | positive scalar in units of m^3/h

Flow coefficient expressed in SI units for a valve that is closed tight
and devoid of all flow except for that due to internal leakage between port
**A** and port **B**. The primary
purpose of this parameter is to ensure the numerical robustness of the model
during simulation. Its exact value is less important than it being a very
small number greater than zero.

### **Valve opening characteristics** — Parameterization by which to compute the valve opening fraction `Linear` (default) | `Quick opening``Equal percentages`

Choice of valve opening profile to use during simulation. The selection
made here determines how the control signal specified at port
**L** is converted into a valve opening fraction (and
opening area). See the block description for detail on the opening
parameterizations.

### **Exponent number** — Denominator of the exponent in the quick-opening parameterization 2 (default) | positive unitless scalar

Number by which to divide the exponent in the governing equation of the
quick-opening parameterization. Use a value greater than
`1` for a true quick-opening profile, one corresponding
to a valve that opens quickly from a maximally closed position but
progressively more slowly as it approaches the maximally opened
position.

### **Valve rangeability** — Base of the exponent in the equal-percentages parameterization `50` (default) | positive unitless scalar

Number to which the exponent is applied in the governing equation of the
equal-percentages parameterization. This number is the ratio between the
maximum and minimum flow rates through the valve (the first corresponding
obtained when the valve is maximally opened and the second when the valve is
maximally closed). Typical values range from `20` to
`50`.

### **Cross-sectional area at ports A and B** — Flow area at the inlet and outlet of the valve `0.01 m^2` (default) | positive scalar in units of area

Area normal to the flow path at each port. The ports are assumed to be
equal in size. The flow area specified here should match those of the inlets
of those components to which the valve connects.

### **Critical Reynolds number** — Reynolds number at which the flow switches between laminar and turbulent `150` (default) | positive unitless scalar

Reynolds number at which the fluid in the valve is expected to switch
between its laminar and turbulent flow regimes. The switch is assumed to
occur at once: the transition region that normally exists between the two
flow regimes is ignored.

## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Valve with flow area modeled in terms of its Cv or Kv flow coefficient

The Flow Coefficient Parameterized Valve (TL) block
models the flow characteristics of a valve using the flow coefficient as a means to
relate the flow rate through the ports to the pressure drop across them. The flow
coefficient parameterization suits those cases in which the internal geometry of a valve
is known in poor detail or in which the flow coefficient is the preferred means of
characterizing a valve. The valve model is sufficiently general in its assumptions that
it can be applied to a variety of valves; no single valve type is assumed in this
block.

### Flow Coefficient Parameterization

The flow coefficient measures the ease with which a fluid driven by a pressure
differential flows across a valve. It is an important parameter in the sizing of
valves and a convenient way of characterizing one in a model. In this role it is
especially useful, as it quantifies in a single number all of the losses incurred in
the flow passages of the valve. The flow coefficient is typically measured by the
valve manufacturer and reported in a data sheet provided for the valve.

Strictly speaking there are two flow coefficients in common use:
*C*v and
*K*v. These
describe what is fundamentally the same quantity: the volumetric flow rate of water
passing through a valve that has been opened to its maximum and set to some standard
operating conditions. The flow coefficients differ only in the temperature and
pressure drop established during the measurement (the operating conditions) and in
the physical units used in its expression:

- *C*v is measured at a generally
  accepted temperature of `60 °F` and pressure drop of
  `1 PSI`; it is expressed in imperial units of
  `US gpm`. This is the flow coefficient used in the
  model when the **Flow coefficient specification** block
  parameter is set to `Cv coefficient (USG/min)`
  [1].
- *K*v is measured at a generally
  accepted temperature of `15 °C` and pressure drop of
  `1 bar`; it is expressed in metric units of
  `m3/h`. This is the flow
  coefficient used in the model when the **Flow coefficient
  specification** block parameter is set to `Kv
  coefficient (m^3/h)`. [2].

Two values are required of the flow coefficient, a *maximum*
and a *minimum*. The maximum corresponds to a valve open to full
capacity; this is the value frequently reported in valve data sheets. The minimum
corresponds to a valve closed tight, when only leakage flow remains, if any at all.
This lower bound imposed on the flow coefficient serves primarily to ensure the
numerical robustness of the model. Its exact value is less important than its being
a (generally very small) number greater than zero.

### Valve Opening Parameterization

The opening fraction of the valve (the ratio of the valve opening area to its
maximum value) is determined during simulation from the input specified at port
**L**. This input is the *control signal*
and it is, in some valves, associated with *stroke* or
*lift percent*. The control signal can range in value from
`0` to `1`. If a lesser or greater value is
specified, it is adjusted to the nearest of the two limits. In other words, the
signal is *saturated* at `0` and
`1`.

The conversion from control signal to opening fraction depends on the
**Valve opening characteristics** parameterization selected in
the block. The calculation result is the same for all parameterizations when the
control signal is either `0` or `1`: a value of
`0` at port **L** always means a maximally
(though not necessarily *completely*) closed valve; a value of
`1` always means a maximally open valve. At intermediate
values, the opening fractions differ:

- `Linear` — The valve opening fraction (denoted *f*(*L*) in the figure) is equal to the control signal at port
  **L**. The two vary in tandem until the control signal
  either drops below zero (the valve is fully closed) or rises above its
  maximum value (the valve is fully open). The opening fraction ranges from
  `0` to `1` (a statement that does not
  apply to all valve opening parameterizations).

  f(L)=L.
- `Quick opening` — The valve opening fraction, *f*(*L*), is a power function of the control signal at port
  **L**. The opening fraction rises quickly with the
  control signal at values near `0` and slowly at values near
  `1`. The exponent (*α*) in the
  calculation determines how the opening rate changes with the control signal.
  The opening fraction ranges from `0` to
  `1`.

  f(L)=L1α,    α>1.
- `Equal percentage` — The valve opening fraction
  is an exponential function of the control signal at port
  **L**. The opening fraction rises slowly with the
  control signal at values near `0` and quickly at values
  near `1`. The base of the exponent (*R*,
  the *rangeability* of the valve, the ratio between the
  maximum and minimum flow rates through the ports) determines how the opening
  rate changes with the control signal. The opening fraction ranges from a
  small fraction (`0.02`–`0.05` for typical
  rangeability values of `20`–`50`) to
  `1`.

  f(L)=RL−1−1R1−1R,    R≈20−50.

### Mass Balance

The volume of fluid inside the valve, and therefore the mass of the same, is
assumed to be very small and it is, for modeling purposes, ignored. As a result, no
amount of fluid can accumulate there. By the principle of conservation of mass, the
mass flow rate into the valve through one port must therefore equal that out of the
valve through the other port:

m˙A+m˙B=0,

where m˙ is defined as the mass flow rate *into* the
valve through the port indicated by the subscript (**A** or **B**).

### Momentum Balance

The causes of those pressure losses incurred in the passages of the valve are
ignored in the block. Whatever their natures—sudden area changes, flow passage
contortions—only their cumulative effect is considered during simulation. It is this
cumulative effect that the flow coefficient of the valve enables the block to
capture in a model. This constant factors in the momentum balance of the valve
*indirectly*, by way of the effective opening area
(*S*) of the same:

pA−pB=m˙m˙2+m˙crρavgS2,

where:

- *p* is the pressure at the port indicated by the
  subscript (**A** or **B**).
- *ρ*avg is the arithmetic mean
  of the fluid densities at the ports.
- m˙ is the mass flow rate at a port.
- m˙cr is the critical mass flow rate, that at which the flow
  is assumed to switch between laminar and turbulent regimes:

  m˙cr=Recrμavgπ4S,

  where *Re*cr
  is the Reynolds number at the transition point and
  *μ*avg is the average of the
  dynamic viscosities at the ports.

The effective opening area (*S*) is the product of scaling of the
maximum opening area of the valve by the opening fraction (*f*(*L*)). The calculation imposes a lower bound on the opening area at
which only leakage flow remains:

S(L)={Smaxf(L),if Smaxf(L)>SminSmin,else,

where the subscripts `max` and
`min` refer to a valve in the fully opened and maximally closed
positions; the function *f*(*L*) is the opening fraction calculated from the control signal
specified at port **L**:

f(L)={L,Linear parameterizationL1/α,Quick opening parameterizationRL−1,Equal percentages parameterization,

where *α* is obtained from the
**Exponent number** block parameter and *R*
from the **Rangeability** parameter. The maximum opening area is
obtained by multiplying the (maximum) flow coefficient by an appropriate conversion factor:

SMax={λCCv,max,if Cv is usedλKKv,max,if Kv is used,

where:

- *λ*C is the conversion factor
  between the maximum flow coefficient in imperial units
  (*C*v,max) and the maximum
  opening area: `2.4015e-5 m^2`.
- *λ*K is the conversion factor
  between the maximum flow coefficient in SI units
  (*K*v,max) and the maximum
  opening area: `2.7765e-5 m^2`.

The minimum opening area in turn is obtained by multiplying the maximum opening
area by the ratio between minimum and maximum flow coefficients:

SMin={Cv,minCv,maxSmax,if Cv is usedKv,minKv,maxSmax,if Kv is used.

### Energy Balance

The valve is modeled as an adiabatic component. No heat exchange can occur between
the fluid and the wall that surrounds it. No work is done on or by the fluid as it
traverses from inlet to outlet. With these assumptions, energy can flow by advection
only, through ports **A** and **B**. By the principle of conservation of energy, the sum of the port
energy flows must then always equal zero:

ϕA+ϕB=0,

where *ϕ* is defined as the energy flow rate
*into* the valve through one of the ports (**A** or **B**).
