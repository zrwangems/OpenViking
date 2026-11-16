---
type: simulink-block
title: 'Flow Resistance (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'flowresistanceg'
documentation_source_path: 'ref/flowresistanceg.html'
language: en
---

# Flow Resistance (G)

## Ports

### Conserving

### **A** — Inlet or outlet gas

Gas conserving port associated with the inlet or outlet of the flow
resistance. This block has no intrinsic directionality.

### **B** — Inlet or outlet gas

Gas conserving port associated with the inlet or outlet of the flow
resistance. This block has no intrinsic directionality.

## Parameters

### **Nominal pressure drop** — Pressure drop at a known operating condition `0.001 MPa` (default)

Pressure drop from inlet to outlet at a known operating condition. The
block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate.

### **Nominal mass flow rate** — Mass flow rate at a known operating condition `0.1 kg/s` (default)

Mass flow rate through the component at a known operating condition. The
block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate.

### **Nominal density** — Density at a known operating condition `0 m^3/kg` (default)

Mass density inside the flow resistance at a known operating condition.
The block uses the nominal parameters to calculate the constant of
proportionality between the pressure drop and the mass flow rate. Set this
parameter to zero to ignore the dependence of the pressure drop on the fluid
density.

### **Cross-sectional area at ports A and B** — Flow area at the ports of the flow resistance `0.01 m^2` (default)

Flow area at the ports of the flow resistance. The ports are assumed to be
identical in size.

### **Fraction of nominal mass flow rate for laminar flow** — Ratio of threshold to nominal mass flow rates `1e-3` (default)

Ratio of the threshold mass flow rate to the nominal mass flow rate. The
block uses this parameter to calculate the threshold mass flow rate—and
ultimately to set the limits of linearization for the pressure drop.

## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

General resistance in a gas branch

The Flow Resistance (G) block models a general pressure
drop in a gas network branch. The pressure drop is proportional to the square of the
mass flow rate and to the density of the gas. The constant of proportionality is
determined from a nominal operating condition specified in the block dialog box.

Use this block when the only data available for a component is its pressure drop as a
function of its mass flow rate. Combine the block with others to create a custom
component that more accurately captures the pressure drop that it induces—for example, a
heat exchanger based on a chamber block.

### Mass Balance

The volume of gas inside the flow resistance is assumed to be negligible. The mass
flow rate in through one port must then exactly equal the mass flow rate out through
the other port:

m˙A+m˙B=0,

where m˙A and m˙B are defined as the mass flow rates into the component through
ports **A** and **B**,
respectively.

### Energy Balance

Energy can enter and leave the flow resistance through the gas conserving ports
only. No heat exchange occurs between the wall and the environment. In addition, no
work is done on or by the fluid. The energy flow rate in through one port must then
exactly equal the energy flow rate out through the other port:

ϕA+ϕB=0,

where *ϕ*A and
*ϕ*B are the energy flow rates into the
flow resistance through ports **A** and **B**.

### Momentum Balance

The relevant external forces on the fluid include those due to pressure at the
ports and those due to viscous friction at the component walls. Gravity is ignored
as are other body forces. Expressing the frictional forces in terms of a loss factor
*ξ* yields the semi-empirical expression:

Δp=ξm˙22ρS2,

where:

- *Δp* is the pressure drop from port **A** to port **B**—that is, *p*A +
  *p*B.
- *ξ* is the loss factor.
- *ρ* is the fluid density.
- *S* is the flow area.

The pressure drop equation is implemented with two modifications. First, to allow
for a change in sign upon reversal of flow direction, it is rewritten:

Δp=ξm˙|m˙|2ρS2,

where the pressure drop is positive only if the mass flow rate is
too. Second, to eliminate singularities due to flow reversal—which can pose a
challenge for numerical solvers during simulation—it is linearized in a small region
of near-zero flow:

Δp=ξm˙m˙2+​m˙Th22ρS2,

where m˙Th is a threshold mass flow rate below which the pressure drop is
linearized. The figure shows the modified pressure drop against the local mass flow
rate (curve **I**):

- Above m˙Th, the pressure drop approximates that expressed in the
  original equation (curve **II**) and it
  varies with m˙2. This dependence is commensurate with that observed in
  turbulent flows.
- Below m˙Th, the pressure drop approximates a straight line with
  slope partly dependent on m˙Th (curve **III**) and it
  varies with m˙. This dependence is commensurate with that observed in
  laminar flows.

For ease of modeling, the loss factor *ξ* is not required as a
block parameter. Instead, it is automatically computed from the nominal condition
specified in the block dialog box:

ξ2S2=ρ\*Δp\*m˙\*2,

where the asterisk (\*) denotes a value at the nominal operating
condition. Underlying all of these calculations is the assumption that the threshold
mass flow rate m˙Th is much smaller than the nominal value m˙\*. Replacing the fraction *ξ*/(2S2) in the expression for the pressure drop yields:

Δp=ρ\*Δp\*ρm˙\*2(m˙m˙2+m˙Th2).

or, equivalently:

Δp=Cm˙ρm˙2+m˙Th2,

where *C* is a constant of proportionality
between the pressure drop across the flow resistance and the local mass flow rate.
It is defined as:

C=ρ\*Δp\*m˙\*2.

If the fluid density is assumed to be invariant, then its nominal and actual
values must always be equal. This is the case whenever the nominal value is
specified in the block dialog box as `0`—a special value used to
signal to the block that the fluid density is a constant. The ratio of the two is
then `1` and the fraction *C*/*ρ* reduces to:

Cρ=Δp\*m˙\*2.
