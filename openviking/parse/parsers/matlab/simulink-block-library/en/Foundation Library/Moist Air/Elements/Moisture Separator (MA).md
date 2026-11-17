---
type: simulink-block
title: 'Moisture Separator (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'moistureseparatorma'
documentation_source_path: 'ref/moistureseparatorma.html'
language: en
---

# Moisture Separator (MA)

## Ports
```yaml
ports:
- name: W
  summary: Rate of water vapor removed, kg/s physical signal
  direction: output
- name: D
  summary: Rate of water droplets removed, kg/s physical signal
  direction: output
- name: A
  summary: Inlet or outlet moist air
  direction: conserving
- name: B
  summary: Inlet or outlet moist air
  direction: conserving
```

### Output

### **W** — Rate of water vapor removed, kg/s physical signal

Physical signal that outputs the rate of water vapor removed, in kg/s.

### **D** — Rate of water droplets removed, kg/s physical signal

Physical signal that outputs the rate of water droplets removed, in kg/s.
### Conserving

### **A** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the moisture
separator. This block has no intrinsic directionality.

### **B** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the moisture
separator. This block has no intrinsic directionality.
## Parameters
```yaml
parameters:
- name: Fraction of water vapor removed
  summary: Water vapor removal fraction 0.5 (default) | scalar in the range of [0,1]
  group: ''
- name: Removed water vapor condensed to liquid
  summary: Whether to condense removed water vapor off (default) | on
  group: ''
- name: Fraction of water droplets removed
  summary: Water droplet removal fraction 0.5 (default) | scalar in the range of [0,1]
  group: ''
- name: Nominal pressure drop
  summary: Pressure drop at nominal operating conditions 0.001 MPa (default) | scalar
  group: ''
- name: Nominal mass flow rate
  summary: Mass flow rate at nominal operating conditions 0.1 kg/s (default) | positive scalar
  group: ''
- name: Nominal density
  summary: Density at nominal operating conditions 0 kg/m^3 (default) | positive scalar
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Flow area at ports 0.01 m^2 (default) | positive scalar
  group: ''
- name: Fraction of nominal mixture mass flow rate for laminar flow transition
  summary: Ratio of threshold to nominal mass flow rates 1e-3 (default) | positive scalar
  group: ''
```

### **Fraction of water vapor removed** — Water vapor removal fraction `0.5` (default) | scalar in the range of [0,1]

Fraction of water vapor removed from the moist air flow through the block.

### **Removed water vapor condensed to liquid** — Whether to condense removed water vapor `off` (default) | `on`

Option to condense the removed water vapor to liquid. When you select this check
box, the block converts water vapor to liquid before removing it, which means that the
latent heat of the water vapor remains in the flow. In this case, the temperature change
across the block may be more significant.

### **Fraction of water droplets removed** — Water droplet removal fraction `0.5` (default) | scalar in the range of [0,1]

Fraction of water droplets removed from the moist air flow through the block.

### **Nominal pressure drop** — Pressure drop at nominal operating conditions `0.001 MPa` (default) | scalar

Pressure drop from the inlet to outlet at nominal operating conditions. The block
uses the nominal parameters to calculate the constant of proportionality between the
pressure drop and the mass flow rate.

### **Nominal mass flow rate** — Mass flow rate at nominal operating conditions `0.1 kg/s` (default) | positive scalar

Mass flow rate of the air mixture through the block at nominal operating conditions.
The block uses the nominal parameters to calculate the constant of proportionality
between the pressure drop and the mass flow rate.

### **Nominal density** — Density at nominal operating conditions `0 kg/m^3` (default) | positive scalar

Mass density of the moist air mixture inside the flow resistance at nominal
operating conditions. The block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate. Set this parameter to
zero to ignore the dependence of the pressure drop on the air mixture density.

### **Cross-sectional area at ports A and B** — Flow area at ports `0.01 m^2` (default) | positive scalar

Flow area at the ports of the separator. The block assumes that the ports are
identical in size.

### **Fraction of nominal mixture mass flow rate for laminar flow transition** — Ratio of threshold to nominal mass flow rates `1e-3` (default) | positive scalar

Ratio of the threshold mass flow rate to the nominal mass flow rate of the air
mixture. The block uses this parameter to set the threshold for the linearization of the
pressure drop.
## Libraries

Simscape / Foundation Library / Moist Air / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Remove water vapor and water droplets from moist air flow

The Moisture Separator (MA) block removes a specified
fraction of water vapor and water droplets from the flow through the block in a moist air
network. The block assumes that method that removes the moisture is mechanical, and that the
temperature change of the flow is negligible across the ports.

If the **Nominal density** parameter,
*ρnom*, is greater than zero, then the pressure
drop is

pA−pB=K1m˙Am˙A2+(flamm˙nom)2RTinpin

where:

- *ṁA* is the mass flow rate at port
  **A**.
- *ṁnom* is the value of the **Nominal
  mass flow rate** parameter.
- *flam* is the fraction of the nominal mixture
  mass flow rate for the laminar flow transition.
- *pin* is the inlet pressure,
  *p*A or
  *pB*, depending on flow direction.
- *Tin* is the inlet temperature,
  *T*A or
  *TB*, depending on flow direction.
- *R* is the specific gas constant.

The proportionality constant, *K1*, is

K1=Δpnomρnomm˙nom2

where *ρnom* is the value of the **Nominal
density** parameter and *Δpnom* is the
value of the **Nominal pressure drop** parameter.

If the **Nominal density** parameter is zero, then the pressure drop
is

pA−pB=K2m˙Am˙A2+(flamm˙nom)2

where the proportionality constant, *K1*, is

K2=Δpnomm˙nom2

Because the block assumes the flow resistance is adiabatic, the mixture specific total
enthalpies are equal,

hA+12(m˙ARTASpA)2=hB+12(m˙BRTBSpB)2

where:

- *hA* and
  *hB* are the specific enthalpies at ports
  **A** and **B**, respectively.
- *S* is the value of the **Cross-sectional area at ports A
  and B** parameter.

### Mass and Energy Balance

The mass balance equations for the moist air, water vapor, trace gas, and water droplets
are

m˙A+m˙B−m˙w,removed=0m˙wA+m˙wB−m˙w,removed=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙d,removed=0

where:

- *ṁwA* and
  *ṁwB* are the water vapor mass flow rates
  at ports **A** and **B**, respectively.
- *ṁgA* and
  *ṁgB* are the trace gas mass flow rates at
  ports **A** and **B**, respectively.
- *ṁdA* and
  *ṁdB* are the water droplets mass flow
  rates at ports **A** and **B**, respectively.

The water vapor removal rate is

m˙w,removed=θwm˙MA,inxw,in,

where:

- *θw* is the value of the
  **Fraction of water vapor removed** parameter.
- *ṁMA,in* is the moist air mass flow rate
  of the inflow port, which can be either port **A** or
  **B**.
- *xw,in* is the water vapor mass fraction
  at the inflow port, which can be either port **A** or
  **B**.

The water droplet removal rate is

m˙d,removed=θdm˙MA,inrd,in,

where:

- *θd* is the value of the
  **Fraction of water droplets removed** parameter.
- *rd,in* is the mass ratio of water
  droplets to moist air at the inflow port, which can be either port
  **A** or **B**.

The energy balance equation is

ΦA+ΦB−Φremoved=0,

where *ΦA* and
*ΦB* are the energy flow rates through ports
**A** and **B**, respectively.

*Φremoved* is the energy flow rate from the removed
water vapor and water droplets. This term does not represent heat or work and only includes
the specific enthalpy contributions from the removed the water vapor and water droplets,

Φremoved=m˙w,removedhw,in+m˙d,removedhd,in,

where *hw,in* and
*hd,in* are the water vapor and water droplet
specific enthalpies at the inflow port.

### Assumptions and Limitations

The block does not model any physics or thermodynamic effects related to removing water
vapor and water droplets.
