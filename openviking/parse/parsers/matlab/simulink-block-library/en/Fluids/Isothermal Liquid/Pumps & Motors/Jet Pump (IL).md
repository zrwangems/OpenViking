---
type: simulink-block
title: 'Jet Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'jetpumpil'
documentation_source_path: 'ref/jetpumpil.html'
language: en
---

# Jet Pump (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: S
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
```

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the motive liquid inlet port.

### **S** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the suction liquid inlet port.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the mixed fluid outlet port.
## Parameters
```yaml
parameters:
- name: Nozzle exit area
  summary: Nozzle exit area 1e-4m^2 (default) | positive scalar
  group: ''
- name: Nozzle exit to throat area ratio
  summary: Nozzle outlet to throat area 0.25 (default) | positive scalar
  group: ''
- name: Diffuser inlet to outlet area ratio
  summary: Diffuser geometry ratio 0.25 (default) | positive scalar
  group: ''
- name: Primary flow nozzle loss coefficient
  summary: Primary flow friction loss coefficient 0.05 (default) | positive scalar
  group: ''
- name: Secondary flow entry loss coefficient
  summary: Secondary flow friction loss coefficient 0.005 (default) | positive scalar
  group: ''
- name: Throat loss coefficient
  summary: Throat friction loss coefficient 0.1 (default) | positive scalar
  group: ''
- name: Diffuser loss coefficient
  summary: Diffuser friction loss coefficient 0.1 (default) | positive scalar
  group: ''
- name: Minimum allowable nozzle pressure
  summary: Minimum pressure at nozzle outlet 1 Pa (default) | positive scalar
  group: ''
```

### **Nozzle exit area** — Nozzle exit area `1e-4``m^2` (default) | positive scalar

Cross-sectional area of the nozzle exit at its widest section.

### **Nozzle exit to throat area ratio** — Nozzle outlet to throat area `0.25` (default) | positive scalar

Characteristic ratio of the nozzle outlet and throat cross-sectional
areas.

### **Diffuser inlet to outlet area ratio** — Diffuser geometry ratio `0.25` (default) | positive scalar

Characteristic ratio of the diffuser inlet and outlet cross-sectional
areas.

### **Primary flow nozzle loss coefficient** — Primary flow friction loss coefficient `0.05` (default) | positive scalar

Loss coefficient that characterizes the losses in pressure due to nozzle
friction in the motive flow.

### **Secondary flow entry loss coefficient** — Secondary flow friction loss coefficient `0.005` (default) | positive scalar

Loss coefficient that characterizes the losses in pressure in the suction
flow due to the suction inlet friction.

### **Throat loss coefficient** — Throat friction loss coefficient `0.1` (default) | positive scalar

Loss coefficient that characterizes the losses in pressure in the mixture
due to throat friction.

### **Diffuser loss coefficient** — Diffuser friction loss coefficient `0.1` (default) | positive scalar

Loss coefficient that characterizes the losses in pressure due in the
mixed flow due to friction in the diffuser.

### **Minimum allowable nozzle pressure** — Minimum pressure at nozzle outlet `1` `Pa` (default) | positive scalar

Minimum allowed pressure in the jet pump. If the pressures at the nozzle
exit fall below this value, the block simulates the effects of cavitation by
restricting the fluid velocity to the velocity at the minimum nozzle
pressure.
## Libraries

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Liquid-liquid jet pump in an isothermal liquid network

The Jet Pump (IL) block models a liquid-liquid jet pump in an isothermal liquid network. The
motive and suction fluids in the jet pump are the same. The motive fluid enters the
primary nozzle at port **A** and draws in the suction fluid through
input port **S**. After mixing in the throat, the combined flow expands
through the diffuser and discharges at port **B**. The total pressure
change over the pump is the sum of the individual contributions of friction and area
change in each section of the pump and momentum changes in the throat. The sign
convention for the equations correspond to positive flow into the throat.

Diagram of jet pump. One liquid flows through a nozzle and out a throat and diffuser. The other liquid flows up through a second port to propel the first fluid. The second fluid also exits out of the diffuser.

### Changes in Pressure Due to Area Changes

The mass flow rate is conserved in the pump

m˙A+m˙S+m˙B=0,

where m˙A is the mass flow rate through port
**A**, m˙S is the mass flow rate through port
**S**, and m˙A is the mass flow rate through port
**B**.

Using mass conservation and the Bernoulli Principle, you can express the area changes over
the pump segments in terms of pressure change. The pressure change associated with
the nozzle is

Δpa,Nozzle=m˙A4ρAN2,

or 0, whichever is greater.
*AN* is the value of the
**Nozzle exit area** parameter and *ρ* is the
fluid density.

The pressure change due to the area at the suction inlet is

Δpa,Annulus=m˙S4ρ(AT−AN)2,

or 0, whichever is greater.
*AT* is the cross-sectional area of the
throat. The pressure change over the diffuser expansion is

Δpa,Diffuser=−m˙B22ρAT2(1−a2),

where *a* is the value of the **Diffuser
inlet to outlet area ratio** parameter.

**Reversed Flows**

In the case of reversed flow, the block does not model the effect of the
nozzle area on pressure change, and the flow traveling from the throat through
the nozzle does not undergo any pressure gain. This behavior ensures the
numerical stability of the block during simulation of reversed flows.

### Changes in Pressure Due to Mixing

The motive and suction flows mix in the throat. The change in pressure from mixing is

Δpmixing=m˙A2b+m˙S21−b−m˙B2ρAT,

where *b* is the value of the **Nozzle
exit to throat area ratio** parameter, which is defined between the
largest and smallest cross-sectional areas of the nozzle.

### Pressure Losses Due to Friction

The flow loses pressure due to due to friction in the nozzle, secondary suction inlet,
throat, and diffuser. The block calculates these losses based on a coefficient for
each section and the area, or area ratio, between different sections of the pump.
Friction causes pressure loss regardless of the flow direction. The pressure loss in
the nozzle due to friction is

Δpf,Nozzle=KNm˙A|m˙A|2ρAN2,

where *KN* is the value
of the **Primary flow nozzle loss coefficient** parameter. The
pressure loss due to friction in the suction flow through the annulus is

Δpf,Annulus=KSm˙S|m˙S|2ρ(AT−AN)2,

where *KS* is the value
of the **Secondary flow entry loss coefficient** parameter. The
pressure loss in the throat due to friction is

Δpf,Throat=KTm˙B|m˙B|2ρAT2,

where *KT* is the value
of the **Throat loss coefficient** parameter. The pressure loss in
the diffuser due to friction is

Δpf,Diffuser=KDm˙B|m˙B|2ρAT2,

where *KD* is the value
of the **Diffuser loss coefficient** parameter. The sign
corresponds to negative flow from the throat toward port **B**.
Because the block defines losses for the regions of highest velocity in the flow,
the block uses the throat area, which is equal to the diffuser inlet area, in the
diffuser loss equation.

### Saturation Pressure in the Nozzle

Cavitation occurs when a region of low pressure in the flow falls below the vapor
saturation pressure, which creates pockets of vapor in the liquid and impedes any
further increase in flow through the pump. You can model this flow rate limit by
specifying a minimum nozzle pressure. If the flow pressure is more than the value of
the **Minimum allowable nozzle pressure** parameter, the fluid
velocity remains constant. Between the nozzle and the diffuser, the pressure change
is either

pB−pN=Δpmixing+Δpf,Throat+Δpf,Diffuser−Δpa,Diffuser

or pB−pN,min, whichever is smaller.

The total pressure change in the nozzle is

pA−pN=Δpa,Nozzle+Δpf,Nozzle.

The total pressure change in the annulus is

pS−pN=Δpa,Annulus+Δpf,Annulus.

### Assumptions and Limitations

- The motive and suction liquids are the same.
- Mixing in the throat is uniform and complete.
- The nozzle inlet is much larger than the nozzle outlet, and the
  suction jet annulus is much smaller than the suction inlet.
- For reversed flows, the block does not model change in pressure due to
  the nozzle.
- The block models any effect of cavitation as a maximum limit on the
  flow rate in the throat.
