---
type: simulink-block
title: 'Sudden Area Change (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Pipes and Fittings'
documentation_page: 'suddenareachangetl'
documentation_source_path: 'ref/suddenareachangetl.html'
language: en
---

# Sudden Area Change (TL)

## Ports

### Conserving

### **A** — Section inlet thermal liquid

Fluid entry or exit point to the area change section.

### **B** — Section inlet thermal liquid

Fluid entry or exit point to the area change section.

## Parameters

### **Local loss parameterization** — Method of flow loss calculating `Semi-empirical` (default) | `Tabulated data - loss coefficient vs. Reynolds number`

Parameterization for calculating the loss coefficient due to the sudden
area change. Select `Semi-empirical formulation` to
automatically compute the loss coefficient from the cross-sectional areas at
ports **A** and **B**. Select
`Tabulated data - Loss coefficient vs. Reynolds
number` to specify a 1-D lookup table for the loss
coefficient with respect to the flow Reynolds number.

### **Cross-sectional area at port A** — Inlet area at A `0.02` `m^2` (default) | positive scalar

Area normal to the direction of flow at inlet **A**. This
value must be greater than the cross-sectional area at
**B**.

### **Cross-sectional area at port B** — Inlet area at B `0.01` `m^2` (default) | positive scalar

Area normal to the direction of flow at **B**. This value
must be smaller than the cross-sectional area at
**A**.

### **Critical Reynolds number** — Transitional Reynolds number associated with smallest area in section `150` (default) | positive scalar

Reynolds number at which flow transitions between laminar and turbulent
regimes in the contraction portion of the sudden area change. This parameter
is visible only when the **Loss coefficient specification**
parameter is set to `Semi-empirical
formulation`.

### **Contraction correction factor** — Loss coefficient scaling factor `1` (default) | positive scalar

Scaling factor for adjusting the loss coefficient value in the contraction
portion of the sudden area change. The block multiplies the loss coefficient
factor calculated from the semi-empirical expression by this factor. This
parameter is visible only when the **Loss coefficient
specification** parameter is set to `Semi-empirical
formulation`.

### **Expansion correction factor** — Loss coefficient scaling factor `1` (default) | positive scalar

Scaling factor for adjusting the loss coefficient value in the expansion
portion of the sudden area change. The block multiplies the loss coefficient
factor calculated from the semi-empirical expression by this factor. This
parameter is visible only when the **Loss coefficient
specification** parameter is set to `Semi-empirical
formulation`.

### **Reynolds number vector** — Vector of Reynolds numbers for tabular parameterization `[10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]` (default) | vector

Vector of Reynolds numbers for the tabular parameterization of loss
coefficients. You specify the **Contraction loss coefficient
vector** and **Expansion loss coefficient
vector** parameters at these Reynolds numbers.

This parameter is visible only when the **Loss coefficient
specification** parameter is set to `Tabulated data
- Loss coefficient vs. Reynolds number`.

### **Contraction loss coefficient vector** — Vector of loss coefficients for tabular parameterization `[4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]` (default) | 1-by-*n* vector

Vector of loss coefficients for the contraction portion of the area
change. Specify the loss coefficients at the Reynolds numbers in the
**Reynolds number vector** parameter. The block uses
the Reynolds number and loss coefficient vectors to construct a 1-D lookup
table.

This parameter is visible only when the **Loss coefficient
specification** parameter is set to `Tabulated data
— Loss coefficient vs. Reynolds number`.

### **Expansion loss coefficient vector** — Vector of loss coefficients for tabular parameterization `[4, 2.3, 1.65, 1.35, 1.15, .9, .75, .65, .9, .65]` (default) | 1-by-*n* vector

Vector of loss coefficients for the expansion portion of the area change.
Specify the loss coefficients at the Reynolds numbers in the
**Reynolds number vector** parameter. The block uses
the Reynolds number and loss coefficient vectors to construct a 1-D lookup
table.

This parameter is visible only when the **Loss coefficient
specification** parameter is set to `Tabulated data
— Loss coefficient vs. Reynolds number`.

## Libraries

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Sudden expansion or contraction in flow area

The Sudden Area Change (TL) block models the minor pressure losses due
to a sudden change in flow cross-sectional area. The area change is a contraction from
port **A** to port **B** and an expansion from port
**B** to port **A**. This component is adiabatic.
It does not exchange heat with its surroundings.

**Sudden Area Change Schematic**

The pressure drop across a sudden expansion is primarily due to turbulence
mixing in the expansion zone. Across a sudden contraction, it is primarily due to flow
detachment at the contraction zone entrance. The figure shows the expansion and
contraction zones of the sudden area change.

### Mass Balance

The mass conservation equation in the sudden area change is

m˙A+m˙B=0,

where:

- m˙A and m˙B are the mass flow rates into the sudden area change
  through ports A and B.

### Momentum Balance

The momentum conservation equation in the sudden area change is

pA−pB=m˙22ρ(1SB2−1SA2)+ϕLoss,

where:

- *p*A and
  *p*B are the pressures at
  ports A and B.
- m˙ is the average mass flow rate.
- *ρ* is the average fluid density.
- *S*A and
  *S*B are the flow
  cross-sectional areas at ports A and B.
- *Φ*Loss is the mechanical
  energy loss due to the sudden area change.

The mechanical energy loss is

ϕLoss=KLossm˙22ρSB2,

where:

- *K*Loss is the loss
  coefficient.

If the **Loss coefficient specification** parameter is set to
`Semi-empirical formulation`, the loss coefficient for
a sudden expansion is computed as

KLoss=Ke(1−SBSA)2,

while for a sudden contraction it is computed as

KLoss=Kc2(1−SBSA),

where:

- *K*e is the correction factor
  in the expansion zone.
- *K*c is the correction factor
  in the contraction zone.

In the transition zone between sudden expansion and sudden contraction behavior,
the block smooths the loss coefficient

KLoss=Ke(1−SBSA)2+λ2[Kc2(1−SBSA)−Ke(1−SBSA)2],

where

λ=tanh(3m˙am˙Cr)+1,

where *ṁCr* is the
threshold mass flow rate for flow reversal,

m˙Cr=ReCrμπ4SB.

If the **Loss coefficient specification** parameter is set to
`Tabulated data — Loss coefficient vs. Reynolds
number`, the block obtains the loss coefficient from tabular data
provided as a function of the Reynolds number.

### Energy Balance

The energy conservation equation in the sudden area change is

ϕA+ϕB=0,

where:

- *Φ*A and
  *Φ*B are the energy flow
  rates into the sudden area change through ports A and B.
