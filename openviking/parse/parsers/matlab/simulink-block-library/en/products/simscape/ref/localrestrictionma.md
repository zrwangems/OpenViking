---
type: simulink-block
title: 'Local Restriction (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Elements'
documentation_page: 'localrestrictionma'
documentation_source_path: 'ref/localrestrictionma.html'
language: en
---

# Local Restriction (MA)

## Ports

### Input

### **AR** — Restriction area control signal, m^2 physical signal

Input physical signal that controls the air flow restriction area. The
signal saturates when its value is outside the minimum and maximum
restriction area limits, specified by the block parameters.

#### Dependencies

This port is visible only if you set the **Restriction
type** parameter to
`Variable`.
### Conserving

### **A** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
local restriction. This block has no intrinsic directionality.

### **B** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
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

Lower bound for the restriction cross-sectional area. You can use this
parameter to represent the leakage area. The input signal
**AR** saturates at this value to prevent the
restriction area from decreasing any further.

#### Dependencies

Enabled when the **Restriction type** parameter is
set to `Variable`.

### **Maximum restriction area** — Upper bound for the restriction cross-sectional area `0.005 m^2` (default)

Upper bound for the restriction cross-sectional area. The input signal
**AR** saturates at this value to prevent the
restriction area from increasing any further.

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
**B**. This area is assumed to be the same for the two
ports.

### **Discharge coefficient** — Ratio of actual mass flow rate to theoretical mass flow rate through the restriction `0.64` (default)

Ratio of actual mass flow rate to the theoretical mass flow rate through
the restriction. The discharge coefficient is an empirical parameter that
accounts for nonideal effects.

### **Laminar flow pressure ratio** — Pressure ratio at which air flow transitions between laminar and turbulent regimes `0.999` (default)

Pressure ratio at which the moist air flow transitions between laminar and
turbulent regimes. The pressure loss is linear with respect to mass flow
rate in the laminar regime and quadratic with respect to mass flow rate in
the turbulent regime.

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

Restriction in flow area in moist air network

The Local Restriction (MA) block models the pressure
drop due to a localized reduction in flow area, such as a valve or an orifice, in a
moist air network. Choking occurs when the restriction reaches the sonic condition.

Ports **A** and **B** represent the restriction
inlet and outlet. The input physical signal at port **AR** specifies
the restriction area. Alternatively, you can specify a fixed restriction area as a block
parameter.

The block icon changes depending on the value of the **Restriction
type** parameter.

| Restriction Type | Block Icon |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

The restriction is adiabatic. It does not exchange heat with the environment.

The restriction consists of a contraction followed by a sudden expansion in flow area.
The moist air accelerates during the contraction, causing the pressure to drop. The
moist air separates from the wall during the sudden expansion, causing the pressure to
recover only partially due to the loss of momentum.

**Local Restriction Schematic**

**Caution**

Moist air flow through this block can choke. If a Mass Flow Rate
Source (MA) block or a Controlled Mass Flow Rate
Source (MA) block connected to the Local
Restriction (MA) block specifies a greater mass flow rate than
the possible choked mass flow rate, the simulation generates an error. For more
information, see Choked Flow.

The block equations use these symbols.

|  |  |
| --- | --- |
| m˙ | Mass flow rate |
| *Φ* | Energy flow rate |
| *p* | Pressure |
| *ρ* | Density |
| *R* | Specific gas constant |
| *S* | Cross-sectional area |
| *C*d | Discharge coefficient |
| *h* | Specific enthalpy |
| *c*p | Specific heat at constant pressure |
| *T* | Temperature |

Subscripts `a`, `w`, `d`, and
`g` indicate the properties of dry air, water vapor, water
droplets, and trace gas, respectively. Subscripts `lam` and
`tur` indicate the laminar and turbulent regime, respectively.
Subscripts `A` and `B` indicate the appropriate port.
Subscript `R` indicates the restriction.

Mass balance:

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

Energy balance:

ΦA+ΦB=0

When the flow is not choked, the mixture mass flow rate (positive from port
**A** to port **B**) in the turbulent regime is

m˙tur=CdSR(pA−pB)2ρR|pA−pB|KturKtur=(1+SRS)(1−ρRρinSRS)−2SRS(1−ρRρoutSRS)

Subscripts `in` and `out` indicate the inlet and
outlet, respectively. If *p*A ≥
*p*B, the inlet is port
**A** and the outlet is port **B**; otherwise,
they are reversed. The cross-sectional area *S* is assumed to be equal
at ports **A** and **B**.
*S*R is the area at the restriction.

The mixture mass flow rate equation is derived by combining the equations from two
control volume analyses:

- Momentum balance for flow area contraction from the inlet to the
  restriction
- Momentum balance for sudden flow area expansion from the restriction to the
  outlet

In the analysis for the flow area contraction, pressure
*p*in acts on the area at the inlet,
*S*, and pressure *p*R acts
on the area at the restriction, *S*R. The
pressure acting on the area outside the restriction, *S* −
*S*R, is assumed to be
(*p*in*S* +
*p*R*S*R)/(*S*
+ *S*R).

In the analysis for the flow area expansion, the pressure acting on both the area at
the restriction, *S*R, and the area outside the
restriction, *S* − *S*R, is
assumed to be *p*R, because of flow separation
from the restriction. The pressure acting on the area at the outlet ,
*S*, is equal to *p*out.

The mixture mass flow rate (positive from port **A** to port
**B**) in the laminar regime is linearized with respect to the
pressure difference:

m˙lam=CdSR(pA−pB)2ρRΔpthreshold(1−SRS)2

where the threshold for transition between the laminar and turbulent regime is defined
based on the laminar flow pressure ratio,
*B*lam, as

Δpthreshold=(pA+pB2)(1−Blam)

When |pA−pB|≥Δpthreshold, the flow is assumed to be turbulent and therefore m˙unchoked=m˙tur.

When |pA−pB|<Δpthreshold, m˙unchoked smoothly transitions to m˙lam.

When the flow is choked, the velocity at the restriction is equal to the speed of
sound and cannot increase any further. Assuming the flow is choked, the mixture mass
flow rate is

m˙choked=CdSRpRγRRTR

where γR=cpR/(cpR−R). Therefore, the actual mixture mass flow rate is equal to m˙unchoked, but is limited in magnitude by m˙choked:

m˙A={−m˙choked,if m˙unchoked≤−m˙chokedm˙unchoked,if -m˙choked<m˙unchoked<m˙chokedm˙choked,if m˙unchoked≥m˙choked

The expression for the pressure at the restriction is obtained by considering the
momentum balance for flow area contraction from the inlet to the restriction only.

pR=pin−12ρR(m˙ACdSR)2(1+SRS)(1−ρRρinSRS)

The local restriction is assumed adiabatic, so the mixture specific total enthalpies
are equal. Therefore, the changes in mixture specific enthalpies are:

hA−hR=(1ρR2SR2−1ρA2S2)m˙A22CD2hB−hR=(1ρR2SR2−1ρB2S2)m˙B22CD2

### Assumptions and Limitations

- The restriction is adiabatic. It does not exchange heat with the
  environment.
- This block does not model supersonic flow.
