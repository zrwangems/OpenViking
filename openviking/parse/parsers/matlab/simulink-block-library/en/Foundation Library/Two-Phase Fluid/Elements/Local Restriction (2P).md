---
type: simulink-block
title: 'Local Restriction (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'localrestriction2p'
documentation_source_path: 'ref/localrestriction2p.html'
language: en
---

# Local Restriction (2P)

## Ports

### Input

### **AR** — Restriction area control signal, m^2 physical signal

Input physical signal that controls the flow restriction area. The signal
saturates when its value is outside the minimum and maximum restriction area limits,
specified by the **Minimum restriction area** and **Maximum
restriction area** parameters.

#### Dependencies

To enable this port, set the **Restriction type** parameter to
`Variable`.
### Conserving

### **A** — Inlet or outlet two-phase fluid

Two-phase fluid conserving port associated with the inlet or outlet of the local
restriction. The block has no intrinsic directionality.

### **B** — Inlet or outlet two-phase fluid

Two-phase fluid conserving port associated with the inlet or outlet of the local
restriction. The block has no intrinsic directionality.

## Parameters

### **Restriction type** — Whether restriction area can change during simulation `Variable` (default) | `Fixed`

Whether the restriction area can change during simulation:

- `Variable` — The input physical signal at port
  **AR** specifies the restriction area, which can vary during
  simulation. The **Minimum restriction area** and **Maximum
  restriction area** parameters specify the lower and upper bounds for the
  restriction area.
- `Fixed` — The restriction area, specified by the
  **Restriction area** block parameter value, remains constant
  during simulation.

### **Minimum restriction area** — Lower bound for restriction cross-sectional area `1e-10 m^2` (default) | positive scalar

Lower bound for the restriction cross-sectional area. You can use this parameter to
represent the leakage area. The input signal at port **AR** saturates
at this value to prevent the restriction area from further decreasing.

#### Dependencies

To enable this parameter, set **Restriction type** to
`Variable`.

### **Maximum restriction area** — Upper bound for restriction cross-sectional area `0.005 m^2` (default) | positive scalar

Upper bound for the restriction cross-sectional area. The input signal at port
**AR** saturates at this value to prevent the restriction area from
further increasing.

#### Dependencies

To enable this parameter, set **Restriction type** to
`Variable`.

### **Restriction area** — Area normal to flow path at restriction `1e-3 m^2` (default) | positive scalar

Area normal to the flow path at the restriction.

#### Dependencies

To enable this parameter, set **Restriction type** to
`Fixed`.

### **Pressure loss model** — Whether to assume uniform fluid density for momentum balance calculation `Bernoulli` (default) | `Control volume`

Equations to use for momentum balance calculation:

- `Bernoulli` — The block uses the Bernoulli equation,
  which assumes uniform density from inlet to outlet. This option is sometimes less
  accurate than the `Control volume` method, but it is more
  robust and provides faster simulation.
- `Control volume` — The block uses the control volume
  analysis without assuming uniform density. It models the flow from the inlet to the
  restriction as a flow contraction and the flow from the restriction to the outlet as
  a flow expansion.

### **Cross-sectional area at ports A and B** — Area normal to flow path at ports `0.01 m^2` (default) | positive scalar

Area normal to the flow path at ports **A** and
**B**. This area is assumed to be the same for both ports.

### **Discharge coefficient** — Ratio of actual mass flow rate to theoretical mass flow rate through restriction `0.64` (default) | unitless scalar between 0 and 1

The discharge coefficient is a semi-empirical parameter commonly used to
characterize the flow capacity of an orifice. This parameter represents the ratio of the
actual mass flow rate through the orifice to the ideal mass flow rate.

### **Laminar flow pressure ratio** — Pressure ratio for switching between laminar and turbulent regimes `0.999` (default) | unitless scalar between 0 and 1

Ratio of the outlet to the inlet port pressure at which the flow regime is assumed
to switch from laminar to turbulent. The prevailing flow regime determines the equations
used in simulation. If the flow is laminar, the pressure drop across the restriction is
linear with respect to the mass flow rate. If the flow is turbulent, the pressure drop
across the restriction is quadratic with respect to the mass flow rate.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2024a: Use Bernoulli equation to compute pressure losses

The Local Restriction (2P) block now has
the **Pressure loss model** parameter, which lets you choose between two
pressure loss models. The `Control volume` option, which is the
functionality available in previous releases, is more accurate in certain scenarios. The new
`Bernoulli` option, which assumes uniform fluid density from
inlet to outlet, is more robust and provides faster simulation.

This change has no compatibility impact. The `Bernoulli` option
is the default setting for new blocks, but when you open an existing model, the
Local Restriction (2P) blocks in it automatically have the
**Pressure loss model** parameter set to `Control
volume`.

### R2022b: Model both fixed and variable area restrictions

The Local Restriction (2P) block now has
the **Restriction type** parameter, which lets you switch between modeling
fixed and variable area restrictions. The block uses either the **Restriction
area** parameter or the input physical signal port **AR** to
specify the area of the local restriction.

In previous releases, the block modeled only fixed restrictions. The Two-Phase Fluid
library also contained a separate Variable Local Restriction
(2P) block, which is no longer available. This change has no compatibility
impact. When you open an existing model, all Variable Local Restriction
(2P) blocks in it are automatically replaced by Local
Restriction (2P) blocks with an exposed control port
**AR**.

## Description

Restriction in flow area in two-phase fluid network

The Local Restriction (2P) block models the pressure drop
due to a localized reduction in flow area, such as a valve or an orifice, in a two-phase fluid
network.

Ports **A** and **B** represent the restriction inlet
and outlet. The input physical signal at port **AR** specifies the
restriction area. Alternatively, you can specify a fixed restriction area as a block
parameter.

The block icon changes depending on the value of the **Restriction type**
parameter.

| Restriction Type | Block Icon |
| --- | --- |
| `Variable` | Variable Local Restriction (2P) block icon |
| `Fixed` | Fixed Local Restriction (2P) block icon |

The restriction is adiabatic. It does not exchange heat with the environment.

The restriction consists of a contraction followed by a sudden expansion in flow area.

**Local Restriction Schematic**

fluid flow through a local restriction

The fluid accelerates during the contraction, which causes the pressure to drop. After
passing through the restriction with some momentum loss, the fluid expands and decelerates
toward the outlet, allowing the pressure to rise slightly after the restriction. This pressure
loss model corresponds to the `Control volume` option of the
**Pressure loss model** parameter. It provides better accuracy but is less
robust and efficient than the default `Bernoulli` option, which
assumes uniform fluid density between the restriction inlet and outlet.

Use the `Bernoulli` option when:

- The local restriction is operating in a fully subcooled liquid regime. The fluid is
  approximately incompressible and the uniform density assumption is appropriate.
- The local restriction is used as an expansion valve in a refrigeration cycle. The
  fluid at the inlet is a subcooled liquid coming out of the condenser, therefore the
  uniform density assumption is appropriate.
- The local restriction is operating in a fully superheated vapor regime, but the flow
  velocity is low subsonic, which is typically the case in HVAC systems. In this case, the
  density also does not change much and the uniform density assumption is appropriate.

For all other situations, you can also use the `Bernoulli` option
to trade accuracy for a faster and more robust simulation.

### Mass Balance

The mass balance equation is

m˙A+m˙B=0,

where:

- m˙A and m˙B are the mass flow rates into the restriction through port
  **A** and port **B**.

### Energy Balance

The energy balance equation is

ϕA+ϕB=0,

where *ϕ*A and
*ϕ*B are the energy flow rates into the
restriction through port **A** and port **B**.

The local restriction is assumed to be adiabatic, and therefore, the change in specific
total enthalpy is zero. At port **A**,

uA+pAνA+wA22=uR+pRνR+wR22,

while at port **B**,

uB+pBνB+wB22=uR+pRνR+wR22,

where:

- *u*A,
  *u*B, and
  *u*R are the specific internal energies at
  port **A**, at port **B**, and the restriction
  aperture.
- *p*A,
  *p*B, and
  *p*R are the pressures at port
  **A**, port **B**, and the restriction
  aperture.
- *ν*A,
  *ν*B, and
  *ν*R are the specific volumes at port
  **A**, port **B**, and the restriction
  aperture.
- *w*A,
  *w*B, and
  *w*R are the ideal flow velocities at port
  **A**, port **B**, and the restriction
  aperture.

The block computes the ideal flow velocity as

wA=m˙idealνAS

at port **A**, as

wB=m˙idealνBS

at port **B**, and as

wR=m˙idealνRSR,

inside the restriction, where:

- m˙ideal is the ideal mass flow rate through the restriction.
- *S* is the flow area at port **A** and port
  **B**.
- *S*R is the flow area of the restriction
  aperture.

The block computes the ideal mass flow rate through the restriction as:

m˙ideal=m˙ACD,

where *C*D is the flow discharge
coefficient for the local restriction.

**Local Restriction Variables**

schematic representation of variables in a local restriction

### Momentum Balance if Using Bernoulli Equation

The mass flow from port **A** to port **B** is:

m˙A=CdSRΔp(Δp+Δplam2)1/42νinPRloss(1−(SRS)2),Δp=pA−pB,

where:

- *Δp*lam is the threshold pressure drop at
  which the flow begins to smoothly transition between laminar and turbulent.
- *v*in is the inlet specific volume. Which
  port serves as the inlet and which serves as the outlet depends on the pressure
  differential across the restriction. If pressure is greater at port
  **A** than at port **B**, then port
  **A** is the inlet; if pressure is greater at port
  **B**, then port **B** is the inlet.
- *PR*loss is the pressure loss ratio.

The pressure loss ratio, *PR*loss, is the ratio
of the pressure difference between the inlet and the outlet to the pressure difference
between the inlet and the restriction. It is a term that accounts for the pressure recovery
during the flow expansion after the restriction:

PRloss=1−(SRS)2(1−Cd2)−CdSRS1−(SRS)2(1−Cd2)+CdSRS.

### Momentum Balance if Using Control Volume Analysis

The mass flow from port **A** to port **B** for
turbulent flow is:

m˙A=CdSRΔp2|Δp|νRKT.

*K*T is defined as:

KT=(1+SRS)(1−νinνRSRS)−2SRS(1−νoutνRSRS),

where the subscript `in` denotes the inlet port and the
subscript `out` the outlet port. Which port serves as the inlet and which
serves as the outlet depends on the pressure differential across the restriction. If
pressure is greater at port **A** than at port **B**, then
port **A** is the inlet; if pressure is greater at port
**B**, then port **B** is the inlet.

The mass flow rate from port **A** to port **B** for
laminar flow is:

m˙A=CdSRΔp2ΔplamνR(1−SRS)2.

*Δp*lam denotes the threshold
pressure drop at which the flow begins to smoothly transition between laminar and turbulent:

Δplam=(pA+pB2)(1−Blam),

where *B*lam is the
**Laminar flow pressure ratio** parameter. The flow is laminar if the
pressure drop from port **A** to port **B** is below the
threshold value; otherwise, the flow is turbulent.

The pressure at the restriction area, *p*R, also
depends on the flow regime. When the flow is turbulent:

pR,T=pin−νR2(m˙ACdSR)2(1+SRS)(1−νinνRSRS).

When the flow is laminar:

pR,L=pA+pB2.

### Assumptions and Limitations

- The restriction is adiabatic. It does not exchange heat with its
  surroundings.
- The `Bernoulli` pressure loss model assumes uniform fluid
  density between the inlet and the outlet of the restriction.
