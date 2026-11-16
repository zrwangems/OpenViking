---
type: simulink-block
title: 'Local Resistance (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pipes and Fittings'
documentation_page: 'localresistanceil'
documentation_source_path: 'ref/localresistanceil.html'
language: en
---

# Local Resistance (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the pipe segment. Flow is positive from
port **A** to port **B**.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the pipe segment. Flow is positive from
port **A** to port **B**.

## Parameters

### **Local loss parametrization** — Loss factor calculation method `Constant` (default) | `Tabulated data - loss coefficient vs. Reynolds number`

Method of calculating the pipe segment loss factor. The loss factor is
parameterized by either a linear relationship between the segment pressure
drop and constant loss factor or by interpolation of user-provided loss
factor and Reynolds number data.

### **Forward flow loss coefficient (from A to B)** — Loss coefficient for flow from A to B `1` (default) | positive scalar

Loss coefficient associated with pressure loss for flows from port
**A** to port **B**.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to
`Constant`.

### **Reverse flow loss coefficient (from B to A)** — Loss coefficient for flow from B to A `1` (default) | positive scalar

Loss coefficient associated with pressure loss for flows from port
**B** to port **A**.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to
`Constant`.

### **Reynolds number vector** — Vector of Reynolds numbers for tabular parameterization `[-500, -200, -100, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]` (default) | 1-by-*n* vector

Vector of Reynolds numbers for the tabular parameterization of the loss
coefficient. The vector elements must correspond one-to-one with the
elements in the **Loss coefficient vector** parameter. The
elements are listed in ascending order.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to `Tabulated data - loss
coefficient vs. Reynolds number`.

### **Loss coefficient vector** — Vector of loss coefficients for tabular parameterization `[.65, .75, .9, 1.15, 1.35, 1.65, 2.3, 3.1, 4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]` (default) | 1-by-*n* vector

Vector of loss coefficients for the tabular parameterization of the loss
coefficient. The vector elements must correspond one-to-one with the
elements in the **Reynolds number vector** parameter. The
elements must be greater than 0.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to `Tabulated data - loss
coefficient vs. Reynolds number`.

### **Flow area** — Segment cross-sectional area `1e-3 m^2` (default) | positive scalar

Cross-sectional area of the pipe segment.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Pipe resistances in an isothermal liquid system

The Local Resistance (IL) block models pressure loss due to user-defined pipe
resistances in an isothermal liquid system. You can specify different loss coefficients
for forward and reversed flows through the pipe segment. For pipe bends, you can also
choose to use the Isothermal Liquid library blocks Pipe Bend (IL) and Elbow (IL) or, for area
changes, the Area Change (IL) block.

The loss factor is parameterized by either a constant relationship based on the pipe
pressure or by user-supplied tabular data for loss coefficients based on the Reynolds
number.

### Constant Loss Factor

Segments with loss factors that remain constant over a range of flow velocities
are calculated as:

kloss=kloss,BA+(kloss,AB−kloss,BA)2[tanh(3ΔpΔpcrit)+1],

where:

- *k*loss,AB and
  *k*loss,BA are the
  **Forward flow loss coefficient (from A to B)** and
  **Reverse flow loss coefficient (from B to A)**
  parameters, respectively.
- *Δp* is the pressure difference
  *p*A –
  *p*B.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, which is the flow regime
transition point between laminar and turbulent flow:

Δpcrit=ρ¯2kloss,crit(νRecritDh)2,

where:

- *k*loss,crit is the loss
  factor associated with the critical pressure, and is based on an average
  of the forward and reverse loss coefficients.
- *ν* is the fluid kinematic viscosity.
- ρ¯ is the average fluid density.
- *D*h is the segment hydraulic
  diameter, which is the equivalent diameter of a pipe with a non-circular
  cross-section: Dh=4Aflowπ, where *A*flow
  is the **Flow area**.

### Tabulated Loss Coefficient

The loss coefficient can alternatively be interpolated from user-provided Reynolds
number and loss coefficient data. The vector of Reynolds numbers can have both
positive and negative values, indicating forward and reverse flow, respectively: kloss=TLU(Re).

### Mass Flow Rate

Mass is conserved through the valve:

m˙A+m˙B=0.

The mass flow rate through the valve is calculated as:

m˙=Aflow2ρ¯klossΔp[Δp2+Δpcrit2]1/4,

where *k*loss is the flow
loss coefficient, which is selected between the **Forward flow loss
coefficient (from A to B)** and **Reverse flow loss coefficient
(from B to A)** based on the block flow direction.
