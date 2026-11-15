---
type: simulink-block
title: 'Local Restriction (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Elements'
documentation_page: 'localrestrictionil'
documentation_source_path: 'ref/localrestrictionil.html'
language: en
---

# Local Restriction (IL)

## Ports

### Input

### **AR** — Restriction area control signal, m^2 physical signal

Input physical signal that controls the flow restriction area. The signal
saturates when its value is outside the minimum and maximum restriction area limits,
specified by the block parameters.

#### Dependencies

This port is visible only if you set the **Restriction type**
parameter to `Variable`.
### Conserving

### **A** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the local
restriction. This block has no intrinsic directionality.

### **B** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the local
restriction. This block has no intrinsic directionality.

## Parameters

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

### **Minimum restriction area** — Lower bound for the restriction cross-sectional area `1e-10 m^2` (default) | positive scalar

The lower bound for the restriction cross-sectional area. You can use this parameter
to represent the leakage area. The input signal AR saturates at this value to prevent
the restriction area from decreasing any further.

#### Dependencies

Enabled when the **Restriction type** parameter is set to
`Variable`.

### **Maximum restriction area** — Upper bound for the restriction cross-sectional area `0.005 m^2` (default) | positive scalar

The upper bound for the restriction cross-sectional area. The input signal AR
saturates at this value to prevent the restriction area from increasing any
further.

#### Dependencies

Enabled when the **Restriction type** parameter is set to
`Variable`.

### **Restriction area** — Area normal to flow path at the restriction `1e-3 m^2` (default) | positive scalar

Area normal to flow path at the restriction.

#### Dependencies

Enabled when the **Restriction type** parameter is set to
`Fixed`.

### **Cross-sectional area at ports A and B** — Area normal to flow path at the ports `inf m^2` (default) | positive scalar

Area normal to flow path at ports **A** and **B**.
This area is assumed to be the same for the two ports. The `inf` value
assumes that the cross-sectional area at the ports is much greater than the restriction
area, and therefore all the
*S*R/*S* terms in the block
equations are negligibly small.

### **Discharge coefficient** — Ratio of actual mass flow rate to theoretical mass flow rate through restriction `0.64` (default) | positive scalar

The discharge coefficient is a semi-empirical parameter commonly used to
characterize the flow capacity of an orifice. This parameter is defined as the ratio of
the actual mass flow rate through the orifice to the ideal mass flow rate.

### **Critical Reynolds number** — Reynolds number for transition between laminar and turbulent regimes `150` (default) | positive scalar

The Reynolds number for the transition between laminar and turbulent regimes.

### **Pressure recovery** — Specify whether to account for pressure recovery `Off` (default) | `On`

Select the check box to account for pressure recovery at the local restriction
outlet.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Restriction in flow area in isothermal liquid network

The Local Restriction (IL) block models the pressure drop
due to a localized reduction in flow area, such as a valve or an orifice, in an isothermal
liquid network.

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

The block equations express the mass flow rate in terms of the pressure difference between
ports **A** and **B**:

m˙A+m˙B=0m˙A=CdSRΔp(Δp2+Δpcr2)1/42ρ¯PRloss(1−(SRS)2)Δp=pA−pBΔpcr=π4⋅ρ¯2SR(RecrνatmCd)2

ρ¯=ρA+ρB2

where:

- *Δp* is the pressure differential.
- *p*A and
  *p*B are pressures at ports
  **A** and **B**, respectively.
- *S*R is the cross-sectional area at the
  restriction.
- *S* is the cross-sectional area at ports **A** and
  **B**.
- *Δp*cr is the critical pressure differential
  for the transition between the laminar and turbulent flow regimes.
- *Re*cr is the critical Reynolds
  number.
- *ν*atm is the liquid kinematic viscosity at
  atmospheric pressure, which is a global parameter defined by the
  Isothermal Liquid Properties (IL) block connected to
  the circuit.
- *C*d is the discharge coefficient.
- ρ¯ is the average fluid mixture density.
- *ρ*A and
  *ρ*B are fluid mixture density values at ports
  **A** and **B**, respectively. Equations used to
  compute the fluid mixture density depend on the selected isothermal liquid model. For
  detailed information, see Isothermal Liquid Modeling Options.
- *PR*loss is the pressure loss ratio.

The pressure loss ratio, *PR*loss, depends on the
**Pressure recovery** check box:

- If pressure recovery is off, then

  PRloss=1.
- If pressure recovery is on, then

  PRloss=1−(SRS)2(1−Cd2)−CdSRS1−(SRS)2(1−Cd2)+CdSRS.

The cross-sectional area at the restriction, *S*R,
depends on the **Restriction type** parameter value:

- For variable restrictions,

  SR={Smin,AR≤SminSmax,AR≥SmaxAR,Smin<AR<Smax,

  where *AR* is the value of the input physical signal, and
  *S*min and
  *S*max are the values of the **Minimum
  restriction area** and **Maximum restriction area** block
  parameters, respectively.
- For fixed restrictions, *S*R is the value of
  the **Restriction area** parameter.

By default, the block assumes that the cross-sectional area at the restriction ports is
much greater than the restriction area, setting the **Cross-sectional area at ports A
and B** parameter value to `inf` and all the
*S*R/*S* terms in the equations to
0, to improve computation efficiency. Specify an actual value for the
**Cross-sectional area at ports A and B** parameter if the two
cross-sectional areas are comparable in size and their ratio has an impact on flow
computations.
