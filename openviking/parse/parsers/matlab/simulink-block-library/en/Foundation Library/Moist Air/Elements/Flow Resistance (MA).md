---
type: simulink-block
title: 'Flow Resistance (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'flowresistancema'
documentation_source_path: 'ref/flowresistancema.html'
language: en
---

# Flow Resistance (MA)

## Ports
```yaml
ports:
- name: A
  summary: Inlet or outlet moist air
  direction: conserving
- name: B
  summary: Inlet or outlet moist air
  direction: conserving
```

### Conserving

### **A** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
flow resistance. This block has no intrinsic directionality.

### **B** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
flow resistance. This block has no intrinsic directionality.
## Parameters
```yaml
parameters:
- name: Nominal pressure drop
  summary: Pressure drop at a known operating condition 0.001 MPa (default)
  group: ''
- name: Nominal mixture mass flow rate
  summary: Mass flow rate at a known operating condition 0.1 kg/s (default)
  group: ''
- name: Nominal mixture density
  summary: Density at a known operating condition 0 kg/m^3 (default)
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Flow area at the ports of the flow resistance 0.01 m^2 (default)
  group: ''
- name: Fraction of nominal mixture mass flow rate for laminar flow transition
  summary: Ratio of threshold to nominal mass flow rates 1e-3 (default)
  group: ''
```

### **Nominal pressure drop** — Pressure drop at a known operating condition `0.001 MPa` (default)

Pressure drop from inlet to outlet at a known operating condition. The
block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate.

### **Nominal mixture mass flow rate** — Mass flow rate at a known operating condition `0.1 kg/s` (default)

Mass flow rate of the air mixture through the block at a known operating
condition. The block uses the nominal parameters to calculate the constant
of proportionality between the pressure drop and the mass flow rate.

### **Nominal mixture density** — Density at a known operating condition `0 kg/m^3` (default)

Mass density of the moist air mixture inside the flow resistance at a
known operating condition. The block uses the nominal parameters to
calculate the constant of proportionality between the pressure drop and the
mass flow rate. Set this parameter to zero to ignore the dependence of the
pressure drop on the air mixture density.

### **Cross-sectional area at ports A and B** — Flow area at the ports of the flow resistance `0.01 m^2` (default)

Flow area at the ports of the flow resistance. The ports are assumed to be
identical in size.

### **Fraction of nominal mixture mass flow rate for laminar flow transition** — Ratio of threshold to nominal mass flow rates `1e-3` (default)

Ratio of the threshold mass flow rate to the nominal mass flow rate of the
air mixture. The block uses this parameter to set the threshold for the
linearization of the pressure drop.
## Libraries

Simscape / Foundation Library / Moist Air / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

## Description

General resistance in a moist air branch

The Flow Resistance (MA) block models a general
pressure drop in a moist air network branch. The drop in pressure is proportional to the
square of the mixture mass flow rate and inversely proportional to the mixture density.
The constant of proportionality is determined from a nominal operating condition
specified in the block dialog box. Set the **Nominal mixture density**
parameter to zero to omit the density dependence.

Use this block when empirical data on the pressure losses and flow rates through a
component is available, but detailed geometry information is unavailable.

The block equations use these symbols.

|  |  |
| --- | --- |
| m˙ | Mass flow rate |
| *Φ* | Energy flow rate |
| *p* | Pressure |
| *ρ* | Density |
| *R* | Specific gas constant |
| *S* | Cross-sectional area |
| *K* | Proportionality constant |
| *h* | Specific enthalpy |
| *T* | Temperature |

Subscripts `a`, `w`, `d`, and
`g` indicate the properties of dry air, water vapor, water
droplets, and trace gas, respectively. Subscripts `A` and
`B` indicate the appropriate port.

Mass balance:

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

Energy balance:

ΦA+ΦB=0

If the **Nominal mixture density** parameter value,
*ρ*nom, is greater than zero, then the block
computes the pressure drop as

pA−pB=K1m˙Am˙A2+(flamm˙nom)2RTinpin

where:

- *f*lam is the fraction of nominal
  mixture mass flow rate for laminar flow transition.
- *p*in is the inlet pressure
  (*p*A or
  *p*B, depending on flow
  direction).
- *T*in is the inlet temperature
  (*T*A or
  *T*B, depending on flow
  direction).

The proportionality constant is computed from the nominal flow conditions as

K1=Δpnomρnomm˙nom2

If the **Nominal mixture density** parameter is set to zero, then the
block computes the pressure drop as

pA−pB=K2m˙Am˙A2+(flamm˙nom)2

where the proportionality constant is computed from the nominal flow conditions
as

K2=Δpnomm˙nom2

The flow resistance is assumed adiabatic, so the mixture specific total enthalpies are
equal

hA+12(m˙ARTASpA)2=hB+12(m˙BRTBSpB)2

### Assumptions and Limitations

- The resistance is adiabatic. It does not exchange heat with the
  environment.
- The pressure drop is assumed to be proportional to the square of the
  mixture mass flow rate and inversely proportional to the mixture density.
