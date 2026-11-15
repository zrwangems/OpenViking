---
type: simulink-block
title: 'Flow Resistance (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Liquid Models / Elements'
documentation_page: 'flowresistancetl'
documentation_source_path: 'ref/flowresistancetl.html'
language: en
---

# Flow Resistance (TL)

## Ports

### Conserving

### **A** — Flow resistance port thermal liquid

Port through which the thermal liquid enters or exits the flow
resistance.

### **B** — Flow resistance port thermal liquid

Port through which the thermal liquid enters or exits the flow
resistance.

## Parameters

### **Nominal pressure drop** — Pressure drop at a known operating condition 0.001 MPa (default)

Pressure drop from inlet to outlet at a known operating condition. The
block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate.

### **Nominal mass flow rate** — Mass flow rate at a known operating condition 0.1 kg/s (default)

Mass flow rate through the component at a known operating condition. The
block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate.

### **Cross-sectional area at ports A and B** — Flow area at the ports of the flow resistance 0.01 m^2 (default)

Flow area at the ports of the flow resistance. The ports are assumed to be
identical in size.

### **Fraction of nominal mass flow rate for laminar flow** — Ratio of threshold to nominal mass flow rates 1e-3 (default)

Ratio of the threshold mass flow rate to the nominal mass flow rate. The
block uses this parameter to calculate the threshold mass flow rate—and
ultimately to set the limits of linearization for the pressure drop.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

General resistance in a thermal liquid branch

The Flow Resistance (TL) block models a general
pressure drop in a thermal-liquid network branch. The pressure drop is proportional to
the square of the mass flow rate. The constant of proportionality is determined from a
nominal operating condition specified in the block dialog box.

Use this block when the only data available for a component is the typical pressure
drop and flow rate. This block is useful for representing complex components, where it
is difficult to determine theoretical pressure loss from the geometry.

### Mass Balance

The volume of fluid inside the flow resistance is assumed to be negligible. The
mass flow rate in through one port must then exactly equal the mass flow rate out
through the other port:

m˙A+m˙B=0,

where m˙A and m˙B are defined as the mass flow rates into the component through
ports **A** and **B**,
respectively.

### Energy Balance

Energy can enter and leave the flow resistance through the thermal liquid ports
only. No heat exchange occurs between the wall and the environment. In addition, no
work is done on or by the fluid. The energy flow rate in through one port must then
exactly equal the energy flow rate out through the other port:

ϕA+ϕB=0,

where *ϕ*A and
*ϕ*B are the energy flow rates into the
flow resistance through ports **A** and **B**.

### Momentum Balance

The pressure drop is assumed proportional to the square of the mass flow rate. The
square of the mass flow rate is linearized in a small laminar flow region near zero
flow, resulting in

pA−pB=Km˙Am˙A2+m˙lam2,

where:

- *p*A and
  *p*B are pressures at ports
  **A** and **B**, respectively.
- m˙lam is the mass flow rate threshold for laminar
  transition.

*K* is the proportionality constant,

K=Δpnomm˙nom2,

where *Δp*nom is the **Nominal
pressure drop** parameter value and m˙nom is the **Nominal mass flow
rate** parameter value.
