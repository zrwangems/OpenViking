---
type: simulink-block
title: 'Flow Resistance (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'flowresistanceil'
documentation_source_path: 'ref/flowresistanceil.html'
language: en
---

# Flow Resistance (IL)

## Ports
```yaml
ports:
- name: A
  summary: Inlet or outlet isothermal liquid
  direction: conserving
- name: B
  summary: Inlet or outlet isothermal liquid
  direction: conserving
```

### Conserving

### **A** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the flow
resistance. This block has no intrinsic directionality.

### **B** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the flow
resistance. This block has no intrinsic directionality.
## Parameters
```yaml
parameters:
- name: Nominal pressure drop
  summary: Pressure drop at a known operating condition 0.001 MPa (default) | positive scalar
  group: ''
- name: Nominal mass flow rate
  summary: Mass flow rate at a known operating condition 0.1 kg/s (default) | positive scalar
  group: ''
- name: Fraction of nominal mass flow rate for laminar flow
  summary: Ratio of threshold to nominal mass flow rates 1e-3 (default) | scalar in the range [0,1]
  group: ''
```

### **Nominal pressure drop** — Pressure drop at a known operating condition 0.001 MPa (default) | positive scalar

Pressure drop from inlet to outlet at a known operating condition. The block uses
the nominal parameters to calculate the constant of proportionality between the pressure
drop and the mass flow rate.

### **Nominal mass flow rate** — Mass flow rate at a known operating condition 0.1 kg/s (default) | positive scalar

Mass flow rate through the component at a known operating condition. The block uses
the nominal parameters to calculate the constant of proportionality between the pressure
drop and the mass flow rate.

### **Fraction of nominal mass flow rate for laminar flow** — Ratio of threshold to nominal mass flow rates 1e-3 (default) | scalar in the range [0,1]

Ratio of the threshold mass flow rate to the nominal mass flow rate. The block uses
this parameter to calculate the threshold mass flow rate—and ultimately to set the
limits of linearization for the pressure drop.
## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

General resistance in an isothermal liquid branch

The Flow Resistance (IL) block models a general pressure
drop in an isothermal-liquid network branch. The pressure drop is proportional to the square
of the mass flow rate. The constant of proportionality is determined from a nominal operating
condition specified in the block dialog box.

Use this block when the only data available for a component is the typical pressure drop
and flow rate. This block is useful for representing complex components, where it is difficult
to determine theoretical pressure loss from the geometry.

The volume of fluid inside the flow resistance is assumed to be negligible. The mass flow
rate in through one port must then exactly equal the mass flow rate out through the other port:

m˙A+m˙B=0,

where m˙A and m˙B are defined as the mass flow rates into the component through ports
**A** and **B**,
respectively.

The pressure drop is assumed proportional to the square of the mass flow rate. The square
of the mass flow rate is linearized in a small laminar flow region near zero flow, resulting
in

pA−pB=Km˙Am˙A2+m˙lam2,

where:

- *p*A and
  *p*B are pressures at ports **A** and **B**, respectively.
- m˙lam is the mass flow rate threshold for laminar transition.

*K* is the proportionality constant,

K=Δpnomm˙nom2,

where *Δp*nom is the **Nominal pressure
drop** parameter value and m˙nom is the **Nominal mass flow rate**
parameter value.
