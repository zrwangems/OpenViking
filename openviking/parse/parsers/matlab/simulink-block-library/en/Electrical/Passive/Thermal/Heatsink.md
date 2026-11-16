---
type: simulink-block
title: 'Heatsink'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Thermal'
documentation_page: 'heatsink'
documentation_source_path: 'ref/heatsink.html'
language: en
---

# Heatsink

## Ports

### Input

### **v** — Flow speed physical

Physical input port associated with the flow speed.

#### Dependencies

To enable this port, set **Convection** to
`Forced - specify flow speed`.
### Conserving

### **A** — Ambient temperature thermal

Thermal conserving port associated with the ambient
temperature.

### **C** — Case thermal

Thermal conserving port associated with the case.

## Parameters

### Steady State

### **Parameterization** — Parameterization type `Assume rectangular parallel fins` (default) | `Datasheet` | `Tabulated convection and fin efficiency`

Whether to parameterize the block as a function of rectangular parallel fins, datasheet,
or tabulated convection and fin efficiency.

### **Convection** — Convection type `Natural` (default) | `Forced - specify flow speed`

Whether the block models natural convection or uses convection values provided by an
input port.

### **Fin height** — Fin height `38.1e-3` `m` (default) | positive scalar

Height of the fin.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
rectangular parallel fins`.

### **Fin thickness** — Fin thickness `6.5e-4` `m` (default) | positive scalar

Thickness of the fin.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
rectangular parallel fins`.

### **Fin depth** — Fin depth `139.7e-3` `m` (default) | positive scalar

Depth of the fin.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
rectangular parallel fins`.

### **Gap between fins** — Gap between fins `9.4e-3` `m` (default) | positive scalar

Gap between fins.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
rectangular parallel fins` and
**Convection** to `Forced - specify
flow speed`.

### **Number of fins** — Number of fins `11` (default) | positive scalar

Number of fins. The value of this parameter must be equal to or
greater than `1`.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
rectangular parallel fins`.

### **Fin thermal conductivity** — Fin thermal conductivity `237` `W/(m*K)` (default) | positive scalar

Thermal conductivity of the fins.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
rectangular parallel fins`.

### **Vector of temperature rises above ambient, T** — Vector of temperature rises above ambient temperature `[10, 30, 50, 70, 90]` `K` (default) | vector of positive scalars

Vector of temperature rises above the ambient temperature. The values
in this parameter must be positive and strictly ascending.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Datasheet` or `Tabulated
convection and fin efficiency`.

### **Vector of fluid flow speed, v** — Vector of fluid flow speed `[0, 1, 2, 3]` `m/s` (default) | vector of positive scalars

Vector of fluid flow speed. The values in this parameter must be positive and strictly
ascending.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Datasheet` or `Tabulated
convection and fin efficiency`, and
**Convection** to `Forced - specify
flow speed`.

### **Corresponding heat dissipated to ambient, Q\_TLU1(T)** — Corresponding heat dissipated to ambient against temperature `[6.1, 23.6, 44.5, 67.5, 92.3]` `W` (default) | vector of positive scalars

Vector of heat values dissipated to the ambient temperature tabulated against the
temperature rise above the ambient temperature. The values in this
parameter correspond to the values in the **Vector of
temperature rises above ambient, T** parameter. The values
in this parameter must be positive and ascending.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Datasheet` and
**Convection** to
`Natural`.

### **Corresponding heat dissipated to ambient, Q\_TLU2(T, v)** — Corresponding heat dissipated to ambient against temperature and flow speed `[6.1, 18.8, 22.8, 25.7; 23.6, 61.1, 73, 81.5; 44.5, 106.4, 125.9, 140.1; 67.5, 153.5, 180.7, 200.3; 92.3, 202.1, 236.9, 262]` `W` (default) | vector of positive scalars

Vector of heat values dissipated to the ambient temperature tabulated against the flow
speed and temperature rise above the ambient temperature. The values in
this parameter correspond to the values in the **Vector of
temperature rises above ambient, T** parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Datasheet` and
**Convection** to `Forced - specify
flow speed`.

### **Corresponding convective heat transfer coefficient, h\_TLU1(T)** — Corresponding convective heat transfer coefficient against temperature `[5.4, 7.02, 7.98, 8.68, 9.26]` `W/(m^2*K)` (default) | vector of positive scalars

Convective heat transfer coefficient tabulated against the temperature rise above the
ambient temperature.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Tabulated
convection and fin efficiency` and
**Convection** to
`Natural`.

### **Corresponding convective heat transfer coefficient, h\_TLU2(T, v)** — Corresponding convective heat transfer coefficient against temperature and flow speed `[5.4, 17.86, 22.17, 25.41; 7.02, 19.49, 23.8, 27.03; 7.97, 20.44, 24.75, 27.99; 8.68, 21.15, 25.46, 28.69; 9.26, 21.73, 26.04, 29.27]` (default) | `W/(m^2*K)` | vector of positive scalars

Convective heat transfer coefficient tabulated against fluid flow speed caused by forced
convection, and temperature rise above the ambient temperature caused by
natural convection.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Tabulated
convection and fin efficiency` and
**Convection** to `Forced - specify
flow speed`.

### **Vector of convective heat transfer coefficients, h** — Vector of convective heat transfer coefficients `[5, 10, 15, 20, 25, 30]` `W/(m^2*K)` (default) | vector of positive scalars

Convective heat transfer coefficients. This parameter depends on the temperature
difference caused by natural convection, and the fluid flow speed caused
by forced convection. The values of this parameter must be positive and
strictly ascending.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Tabulated
convection and fin efficiency`.

### **Corresponding fin efficiency (percent), eff\_TLU(h)** — Fin efficiency that corresponds to heat transfer coefficients `[96.97, 94.16, 91.53, 89.08, 86.78, 84.62]` (default) | vector of positive scalars

Fin efficiency tabulated against different convective heat transfer
coefficients. Fin efficiency is the actual heat dissipated by the fin
divided by the heat it would dissipate if all its volume was at case
temperature. This parameter depends on fin geometry and fin thermal
conductivity.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Tabulated
convection and fin efficiency`.

### **Total heat exchange surface area** — Total heat exchange surface area `0.1171` `m^2` (default) | positive scalar

Total area of the surface of the heat exchange.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Tabulated
convection and fin efficiency`.

### Fluid Properties

To enable these settings, set **Parameterization** to `Assume
rectangular parallel fins`.

### **Fluid kinematic viscosity** — Fluid kinematic viscosity `1.51e-5` `m^2/s` (default) | positive scalar

Kinematic viscosity of the fluid.

### **Fluid thermal diffusivity** — Fluid thermal diffusivity `2.07e-5` `m^2/s` (default) | positive scalar

Thermal diffusivity of the fluid.

### **Fluid thermal conductivity** — Fluid thermal conductivity `25e-3` `W/(m*K)` (default) | positive scalar

Thermal conductivity of the fluid.

### **Fluid coefficient of volume thermal expansion** — Fluid coefficient of volume thermal expansion `3.3e-3` `1/K` (default) | positive scalar

Fluid coefficient of the volume thermal expansion.

### Dynamics

### **Heatsink mass** — Heatsink mass `0.35` `kg` (default) | positive scalar

Mass of the heatsink.

### **Heatsink specific heat** — Heatsink specific heat `437` `J/(K*kg)` (default) | positive scalar

Specific heat of the heatsink.

## Libraries

Simscape / Electrical / Passive / Thermal

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Dissipate heat from power semiconductors to ambient temperature

The Heatsink block models a heatsink that dissipates heat
from power semiconductors. The heat from the case conducts through the fins and
dissipates to the ambient temperature through convection. The environment and the
working fluid are the same

You can parameterize this block from a datasheet, from tabulated heat transfer properties,
or from geometry that assumes an empirical convection correlation. If you set the
**Convection** parameter to `Forced - specify flow
speed`, the **v** input port specifies the flow
speed.

### Parameterization: Datasheet

To parameterize the Heatsink block from a datasheet, set the
**Parameterization** parameter to
`Datasheet` and specify both the **Vector of
temperature rises above ambient, T** and **Corresponding heat
dissipated to ambient, Q\_TLU1(T)** parameters.

If you enable forced convection in the system by setting **Convection** to
`Forced - specify flow speed`, specify both the
**Vector of temperature rises above ambient, T** and
**Corresponding heat dissipated to ambient, Q\_TLU2(T,v)**
parameters.

### Parameterization: Tabulated Convection and Fin Efficiency

To parameterize the Heatsink block based on the convection
coefficient as a function of the coolant flow speed and temperature difference with
the ambient temperature and the fin efficiency as a function of the convective
coefficient, set the **Parameterization** parameter to
`Tabulated convection and fin efficiency`.

The block uses this equation to calculate the dissipated heat:

Qdissipated=h(vfluid,ΔT)⋅Atotal⋅Eff(h)100⋅(Theatsink−Tambient),

where:

- `h(vfluid,ΔT)` is the
  convective heat transfer coefficient tabulated against the fluid flow
  speed (for forced convection) and the temperature rise above the ambient
  temperature.
- `Atotal` is the total heat
  exchange surface area.
- `Eff(h)` is the fin efficiency, in percent values,
  tabulated against different convective heat transfer coefficients. The
  fin efficiency is the actual heat dissipated by the fin divided by the
  heat it would dissipate if all its volume was at the case temperature.
  This value depends on fin geometry and fin thermal conductivity.

### Parameterization: Assume Rectangular Parallel Fins

If you set the **Parameterization** parameter to
`Assume rectangular parallel fins`, the block uses this
equation to calculate the dissipated heat:

Qdissipated=h(vfluid,ΔT)⋅Atotal⋅Eff(h)100⋅(Theatsink−Tambient),

where:

- h(vfluid,ΔT)=hnatural(ΔT)+hforced(vfluid)
- hnatural(ΔT)=kfluidH(0.825+0.387RaH1/6(1+(0.492Pr)9/16)8/27)2
- hforced(vfluid)=kfluidb(1(RePr2)3+1(0.664RePr0.331+3.65Re)3)−0.33
- RaH=gβναH3abs(ΔT) is the Rayleigh number.
- Re=b2νdabs(vfluid) is the Reynolds number.
- `g = 9.81 m/s2` is the
  acceleration of gravity.
- `β` is the coefficient of volume thermal expansion of
  the fluid.
- `ν` is the fluid kinematic viscosity.
- `α` is the fluid thermal diffusivity.
- `kfluid` is the fluid thermal
  conductivity.
- `H` is the fin height.
- `d` is the fin depth.
- `t` is the fin thickness.
- `b` is the gap between fins.

If one side of size `t x d` is welded in the base, this equation
calculates the total heat exchange area:

Atotal=(2H(d+t)+dt)N.

Then this equation computes the efficiency of a rectangular fin:

Eff(h)=100tanh(2hktH)2hktH

where `k` is the fin thermal
conductivity.
