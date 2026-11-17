---
type: simulink-block
title: 'Local Restriction (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'localrestrictiontl'
documentation_source_path: 'ref/localrestrictiontl.html'
language: en
---

# Local Restriction (TL)

## Ports
```yaml
ports:
- name: AR
  summary: Restriction area control signal, m^2 physical signal
  direction: input
- name: A
  summary: Inlet or outlet thermal liquid
  direction: conserving
- name: B
  summary: Inlet or outlet thermal liquid
  direction: conserving
```

### Input

### **AR** — Restriction area control signal, m^2 physical signal

Input physical signal that controls the flow restriction area. The signal
saturates when its value is outside the minimum and maximum restriction area limits,
specified by the block parameters.

#### Dependencies

This port is visible only if you set the **Restriction type**
parameter to `Variable`.
### Conserving

### **A** — Inlet or outlet thermal liquid

Thermal liquid conserving port associated with the inlet or outlet of the local
restriction. This block has no intrinsic directionality.

### **B** — Inlet or outlet thermal liquid

Thermal liquid conserving port associated with the inlet or outlet of the local
restriction. This block has no intrinsic directionality.
## Parameters
```yaml
parameters:
- name: Restriction type
  summary: Specify whether restriction area can change during simulation Variable (default) | Fixed
  group: ''
- name: Minimum restriction area
  summary: Lower bound for the restriction cross-sectional area 1e-10 m^2 (default)
  group: ''
- name: Maximum restriction area
  summary: Upper bound for the restriction cross-sectional area 0.005 m^2 (default)
  group: ''
- name: Restriction area
  summary: Area normal to flow path at the restriction 1e-3 m^2 (default)
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Area normal to flow path at the ports 0.01 m^2 (default)
  group: ''
- name: Discharge coefficient
  summary: Ratio of actual mass flow rate to theoretical mass flow rate through restriction 0.64 (default)
  group: ''
- name: Pressure recovery
  summary: Specify whether to account for pressure recovery On (default) | Off
  group: ''
- name: Critical Reynolds number
  summary: Reynolds number for transition between laminar and turbulent regimes 12 (default)
  group: ''
```

### **Restriction type** — Specify whether restriction area can change during simulation `Variable` (default) | `Fixed`

Select whether the restriction area can change during simulation:

- `Variable` — The input physical signal at port
  **AR** specifies the restriction area, which can vary during
  simulation. The **Minimum restriction area** and **Maximum
  restriction area** parameters specify the lower and upper bounds for the
  restriction area.
- `Fixed` — The restriction area, specified by the
  **Restriction area** block parameter value, remains constant
  during simulation. Port **AR** is hidden.

### **Minimum restriction area** — Lower bound for the restriction cross-sectional area `1e-10 m^2` (default)

The lower bound for the restriction cross-sectional area. You can use this parameter
to represent the leakage area. The input signal AR saturates at this value to prevent
the restriction area from decreasing any further.

#### Dependencies

Enabled when the **Restriction type** parameter is set to
`Variable`.

### **Maximum restriction area** — Upper bound for the restriction cross-sectional area `0.005 m^2` (default)

The upper bound for the restriction cross-sectional area. The input signal AR
saturates at this value to prevent the restriction area from increasing any
further.

#### Dependencies

Enabled when the **Restriction type** parameter is set to
`Variable`.

### **Restriction area** — Area normal to flow path at the restriction `1e-3 m^2` (default)

Area normal to flow path at the restriction.

#### Dependencies

Enabled when the **Restriction type** parameter is set to
`Fixed`.

### **Cross-sectional area at ports A and B** — Area normal to flow path at the ports `0.01 m^2` (default)

Area normal to flow path at ports **A** and **B**.
This area is assumed to be the same for the two ports.

### **Discharge coefficient** — Ratio of actual mass flow rate to theoretical mass flow rate through restriction `0.64` (default)

The discharge coefficient is a semi-empirical parameter commonly used to
characterize the flow capacity of an orifice. This parameter is defined as the ratio of
the actual mass flow rate through the orifice to the ideal mass flow rate.

### **Pressure recovery** — Specify whether to account for pressure recovery `On` (default) | `Off`

Select the check box to account for pressure recovery at the local restriction
outlet.

### **Critical Reynolds number** — Reynolds number for transition between laminar and turbulent regimes `12` (default)

The Reynolds number for the transition between laminar and turbulent regimes. The
default value corresponds to a sharp-edged orifice.
## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Restriction in flow area in thermal liquid network

The Local Restriction (TL) block models the pressure drop
due to a localized reduction in flow area, such as a valve or an orifice, in a thermal liquid
network.

Ports **A** and **B** represent the restriction inlet
and outlet. The input physical signal at port **AR** specifies the
restriction area. Alternatively, you can specify a fixed restriction area as a block
parameter.

The block icon changes depending on the value of the **Restriction type**
parameter.

| Restriction Type | Block Icon |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

The restriction is adiabatic. It does not exchange heat with the environment.

The restriction consists of a contraction followed by a sudden expansion in flow area. The
fluid accelerates during the contraction, causing the pressure to drop. In the expansion zone,
if the **Pressure recovery** check box is cleared, the momentum of the
accelerated fluid is lost. If the **Pressure recovery** check box is
selected, the sudden expansion recovers some of the momentum and allows the pressure to rise
slightly after the restriction.

**Local Restriction Schematic**

### Mass Balance

The mass balance in the restriction is

0=m˙A+m˙B,

where:

- m˙A is the mass flow rate into the restriction through port
  **A**.
- m˙B is the mass flow rate into the restriction through port
  **B**.

### Momentum Balance

The pressure difference between ports **A** and **B**
follows from the momentum balance in the restriction:

Δp=ρ2(1−SR2S2)vRvR2+vRc2vR=m˙ACdρSRvRc=RecμCdρπ4SR

where:

- *Δp* is the pressure differential.
- *ρ* is the liquid density.
- *μ* is the liquid dynamic viscosity.
- *S* is the cross-sectional area at ports **A**
  and **B**.
- *S*R is the cross-sectional area at the
  restriction.
- *v*R is fluid velocity at the
  restriction.
- *v*Rc is the critical fluid
  velocity.
- *Re*c is the critical Reynolds
  number.
- *C*d is the discharge coefficient.

If pressure recovery is off, then

pA−pB=Δp,

where:

- *p*A is the pressure at port
  **A**.
- *p*B is the pressure at port
  **B**.

If pressure recovery is on, then

pA−pB=Δp1−(SRS)2(1−Cd2)−CdSRS1−(SRS)2(1−Cd2)+CdSRS.

### Energy Balance

The energy balance in the restriction is

ϕA+ϕB=0,

where:

- *ϕ*A is the energy flow rate into the
  restriction through port **A**.
- *ϕ*B is the energy flow rate into the
  restriction through port **B**.

### Assumptions and Limitations

- The restriction is adiabatic. It does not exchange heat with its
  surroundings.
- The dynamic compressibility and thermal capacity of the liquid in the restriction
  are negligible.
