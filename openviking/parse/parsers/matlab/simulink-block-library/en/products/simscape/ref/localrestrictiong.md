---
type: simulink-block
title: 'Local Restriction (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Gas Models / Elements'
documentation_page: 'localrestrictiong'
documentation_source_path: 'ref/localrestrictiong.html'
language: en
---

# Local Restriction (G)

## Ports

### Input

### **AR** — Restriction area control signal, m^2 physical signal

Input physical signal that controls the gas flow restriction area. The
signal saturates when its value is outside the minimum and maximum
restriction area limits, specified by the block parameters.

#### Dependencies

This port is visible only if you set the **Restriction
type** parameter to
`Variable`.
### Conserving

### **A** — Inlet or outlet gas

Gas conserving port associated with the inlet or outlet of the
local restriction. This block has no intrinsic directionality.

### **B** — Inlet or outlet gas

Gas conserving port associated with the inlet or outlet of the
local restriction. This block has no intrinsic directionality.

## Parameters

### **Restriction type** — Specify whether restriction area can change during simulation `Variable` (default) | `Fixed`

Select whether the restriction area can change during simulation:

- `Variable` — The input physical signal at
  port **AR** specifies the restriction area, which
  can vary during simulation. The **Minimum restriction
  area** and **Maximum restriction
  area** parameters specify the lower and upper bounds
  for the restriction area.
- `Fixed` — The restriction area, specified
  by the **Restriction area** block parameter value,
  remains constant during simulation. Port **AR** is
  hidden.

### **Minimum restriction area** — Lower bound for the restriction cross-sectional area `1e-10 m^2` (default)

The lower bound for the restriction cross-sectional area. You can use this
parameter to represent the leakage area. The input signal AR saturates at
this value to prevent the restriction area from decreasing any
further.

#### Dependencies

Enabled when the **Restriction type** parameter is
set to `Variable`.

### **Maximum restriction area** — Upper bound for the restriction cross-sectional area `0.005 m^2` (default)

The upper bound for the restriction cross-sectional area. The input signal
AR saturates at this value to prevent the restriction area from increasing
any further.

#### Dependencies

Enabled when the **Restriction type** parameter is
set to `Variable`.

### **Restriction area** — Area normal to flow path at the restriction `1e-3 m^2` (default)

Area normal to flow path at the restriction.

#### Dependencies

Enabled when the **Restriction type** parameter is
set to `Fixed`.

### **Cross-sectional area at ports A and B** — Area normal to flow path at the ports `0.01 m^2` (default)

Area normal to flow path at ports **A** and
**B**. This area is assumed the same for the two ports.

### **Discharge coefficient** — Ratio of actual mass flow rate to theoretical mass flow rate through restriction `0.64` (default)

Ratio of actual mass flow rate to the theoretical mass flow rate through
the restriction. The discharge coefficient is an empirical parameter that
accounts for nonideal effects.

### **Laminar flow pressure ratio** — Pressure ratio at which gas flow transitions between laminar and turbulent regimes `0.999` (default)

Pressure ratio at which the gas flow transitions between laminar and
turbulent regimes. The pressure loss is linear with respect to mass flow
rate in the laminar regime and quadratic with respect to mass flow rate in
the turbulent regime.

## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Restriction in flow area in gas network

The Local Restriction (G) block models the pressure drop due to
a localized reduction in flow area, such as a valve or an orifice, in a gas network.
Choking occurs when the restriction reaches the sonic condition.

Ports **A** and **B** represent the restriction inlet and
outlet. The input physical signal at port **AR** specifies the
restriction area. Alternatively, you can specify a fixed restriction area as a block
parameter.

The block icon changes depending on the value of the **Restriction
type** parameter.

| Restriction Type | Block Icon |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

The restriction is adiabatic. It does not exchange heat with the environment.

The restriction consists of a contraction followed by a sudden
expansion in flow area. The gas accelerates during the contraction,
causing the pressure to drop. The gas separates from the wall during
the sudden expansion, causing the pressure to recover only partially
due to the loss of momentum.

**Local Restriction Schematic**

**Caution**

Gas flow through this block can choke. If a Mass Flow Rate Source
(G) block or a Controlled Mass Flow Rate Source
(G) block connected to the Local Restriction
(G) block specifies a greater mass flow rate than the possible
choked mass flow rate, the simulation generates an error. For more information, see
Choked Flow.

### Mass Balance

The mass balance equation is:

m˙A+m˙B=0

where m˙A and m˙B are the mass flow rates at ports
**A** and **B**, respectively. Flow rate
associated with a port is positive when it flows into the block.

### Energy Balance

The energy balance equation is:

ΦA+ΦB=0

where *Φ*A and
*Φ*B are energy flow rates at ports
**A** and **B**, respectively.

The block is assumed adiabatic. Therefore, there is no change in specific total enthalpy
between port **A**, port **B**, and the
restriction:

hA+wA22=hR+wR22hB+wB22=hR+wR22

where *h* is the specific enthalpy at port **A**, port
**B**, or restriction R, as indicated by the subscript.

The ideal flow velocities at port **A**, port **B**, and the
restriction are:

wA=m˙idealρASwB=m˙idealρBSwR=m˙idealρRSR

where:

- *S* is the cross-sectional area at ports
  **A** and **B**.
- *S*R is the
  cross-sectional area at the restriction.
- *ρ* is the density of gas volume at port
  **A**, port **B**, or restriction R,
  as indicated by the subscript.

The theoretical mass flow rate without nonideal effects is:

m˙ideal=m˙ACd

where *C*d is the discharge
coefficient.

### Momentum Balance

The pressure difference between ports **A** and **B** is
based on a momentum balance for flow area contraction between the inlet and the
restriction, plus a momentum balance for sudden flow area expansion between the
restriction and the outlet.

For flow from port **A** to port **B**:

ΔpAB=ρR⋅wR⋅|wR|⋅(1+r2(1−rρRρA)−r(1−rρRρB))

where *r* is the area ratio, *r* = *S*R/*S*.

For flow from port **B** to port **A**:

ΔpBA=ρR⋅wR⋅|wR|⋅(1+r2(1−rρRρB)−r(1−rρRρA))

The pressure differences in the two preceding equations are
proportional to the square of the flow rate. This is the typical behavior
for turbulent flow. However, for laminar flow, the pressure difference
becomes linear with respect to flow rate. The laminar approximation
for the pressure difference is:

Δplam=ρRΔptransition2(1−r)

The threshold for transition from turbulent flow to laminar
flow is defined as *Δp*transition = *p*avg(1
— *B*lam),
where *B*lam is the pressure
ratio at the transition between laminar and turbulent regimes (**Laminar
flow pressure ratio** parameter value) and *p*avg =
(*p*A + *p*B)/2.

The pressure at the restriction is based on a momentum balance
for flow area contraction between the inlet and the restriction.

For flow from port **A** to port **B**:

pRAB=pA−ρR⋅wR⋅|wR|⋅1+r2(1−rρRρA)

For flow from port **B** to port **A**:

pRBA=pB+ρR⋅wR⋅|wR|⋅1+r2(1−rρRρB)

For laminar flow, the pressure at the restriction is approximately

pRlam=pavg−ρR⋅wR21−r22

The block uses a cubic polynomial in terms of (*p*A – *p*B) to
smoothly blend the pressure difference and the restriction pressure
between the turbulent regime and the laminar regime:

- When *Δp*transition ≤
  *p*A –
  *p*B,

  then *p*A –
  *p*B =
  *Δp*AB

  and *p*R =
  *p*RAB.
- When 0 ≤ *p*A –
  *p*B <
  *Δp*transition,

  then *p*A –
  *p*B is smoothly blended between
  *Δp*AB and
  *Δp*lam

  and *p*R is smoothly blended between
  *p*RAB
  and
  *p*Rlam.
- When –*Δp*transition <
  *p*A –
  *p*B ≤ 0,

  then *p*A –
  *p*B is smoothly blended between
  *Δp*BA and
  *Δp*lam

  and *p*R is smoothly blended between
  *p*RBA
  and
  *p*Rlam.
- When *p*A –
  *p*B ≤
  –*Δp*transition,

  then *p*A –
  *p*B =
  *Δp*BA

  and *p*R =
  *p*RBA.

### Choked Flow

When the flow through the restriction becomes choked, further
changes to the flow are dependent on the upstream conditions and are
independent of the downstream conditions.

If *A.p* is the Across variable at port **A** and
*p*Bchoked is the
hypothetical pressure at port **B**, assuming choked flow from port
**A** to port **B**, then

A.p−pBchoked=ρR⋅aR2(1+r2(1−rρRρA)−r(1−rρRρB))

where *a* is speed of sound.

If *B.p* is the Across variable at port **B** and
*p*Achoked is the
hypothetical pressure at port **A**, assuming choked flow from port
**B** to port **A**, then

B.p−pAchoked=ρR⋅aR2(1+r2(1−rρRρB)−r(1−rρRρA))

The actual pressures at ports **A** and **B**,
*p*A and
*p*B, respectively, depend on whether
choking has occurred.

For flow from port A to port B, *p*A = *A.p* and

pB={B.p,if B.p≥pBchokedpBchoked,if B.p<pBchoked

For flow from port **B** to port **A**, *p*B =
*B.p* and

pA={A.p,if A.p≥pAchokedpAchoked,if A.p<pAchoked

### Assumptions and Limitations

- The restriction is adiabatic. It does not exchange
  heat with the environment.
- This block does not model supersonic flow.
