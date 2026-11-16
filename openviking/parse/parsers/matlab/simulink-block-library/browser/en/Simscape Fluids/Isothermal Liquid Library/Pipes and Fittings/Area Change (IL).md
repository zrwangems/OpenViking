---
type: simulink-block
title: 'Area Change (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pipes and Fittings'
documentation_page: 'areachangeil'
documentation_source_path: 'ref/areachangeil.html'
language: en
---

# Area Change (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry port.

### **B** — Liquid port isothermal liquid

Liquid exit port.

## Parameters

### **Cone angle** — Gradual area change angle `30` (default) | positive scalar

Angle of expansion for a gradual area change parameterized as a
cone.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to `Semi-empirical
correlation - gradual area change`.

### **Local loss parameterization** — Model of hydraulic losses `Semi-empirical correlation - sudden area change` (default) | `Semi-empirical correlation - gradual area change` | `Tabulated data - loss coefficient vs. Reynolds number`

Model of hydraulic losses due to area change. You can choose from two
analytical, semi-empirical formulations or you can provide your own data by
selecting `Tabulated data - loss coefficient vs. Reynolds
number`.

### **Cross-sectional area at port A** — Area at port A `0.02 m^2` (default) | positive scalar

Area at the section entrance, port **A**.

### **Cross-sectional area at port B** — area at port B `0.01 m^2` (default) | positive scalar

Area at the section exit, port **B**.

### **Reynolds number vector** — Vector of Reynolds number values for tabular parameterization `[10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]` (default) | `1-by-n vector`

Vector of Reynolds number values for the tabular parameterization of the area change. The
elements must correspond one-to-one with the elements of the
**Contraction loss coefficient vector** and the
**Expansion loss coefficient vector** parameters. The
vector values are listed in ascending order.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to `Tabulated data - loss
coefficient vs. Reynolds number`.

### **Contraction loss coefficient vector** — Vector of loss coefficients for an area contraction `[5, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]` (default) | 1-by-*n* vector

Vector of loss coefficients for an area contraction corresponding to the
**Reynolds number vector** parameter, where
*n* is the length of the **Reynolds number
vector**. The elements are listed in descending order and must
be greater than 0.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to `Tabulated data - loss
coefficient vs. Reynolds number`.

### **Expansion loss coefficient vector** — Vector of loss coefficients for an area expansion `[3.1, 2.3, 1.65, 1.35, 1.15, .9, .75, .65, .9, .65]` (default) | `1-by-n vector`

Vector of loss coefficients for an area expansion corresponding to the **Reynolds
number vector** parameter, where *n* is the
length of the **Reynolds number vector**. The elements are
listed in descending order and must be greater than 0.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to `Tabulated data - loss
coefficient vs. Reynolds number`.

### **Expansion correction factor** — Coefficient in semi-empirical loss factor equation `1` (default) | positive scalar

Coefficient used in the semi-empirical calculation of the area expansion
loss factor.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to either:

- `Semi-empirical correlation - sudden area
  change`
- `Semi-empirical correlation - gradual area
  change`

### **Contraction correction factor** — Coefficient in semi-empirical loss factor equation `1` (default) | positive scalar

Coefficient used in the semi-empirical calculation of the area contraction
loss factor.

#### Dependencies

To enable this parameter, set **Local loss
parameterization** to either:

- `Semi-empirical correlation - sudden area
  change`
- `Semi-empirical correlation - gradual area
  change`

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Area expansion or contraction along a pipe in an isothermal liquid network

The Area Change (IL) block models a sudden or a gradual area change along a pipe with
fixed areas and variable flow direction. When the fluid moves from port
**A** to port **B**, it experiences an area
contraction. When the fluid flows from port **B** to port
**A**, it experiences an area expansion. The inlet and outlet areas
can be equal.

Both semi-empirical and tabular formulations are available for correlating flows to
losses.

### Semi-Empirical Formulation

In the semi-empirical, analytical formulation, losses in pressure and velocity are
characterized by a *Hydraulic loss coefficient*,
*K*, in terms of a user-defined **Contraction
correction factor**,
*C*contraction, and **Expansion
correction factor**,
*C*expansion, from Crane [1]. The
coefficient that characterizes area change is calculated from both expansion and
contraction loss factors and based on the flow rate through the block.

For gradual conical area contractions between 0 and 45 degrees, the contraction loss factor is:

Kcontraction=0.8Ccontractionsin(θ2)(1−R),

where *R* is the port area ratio AsmallerAbigger. For gradual area contraction between 45 and 180 degrees:

Kcontraction=Ccontraction2sin(θ2)(1−R),

where *θ* is the **Cone
angle**. A sudden area change has an angle of 180 degrees. In this case,
the loss factor is calculated as Kcontraction=C2(1−R).

For gradual conical area expansions between 0 and 45 degrees, the expansion loss
factor is:

Kexpansion=2.6Cexpansionsin(θ2)(1−R)2,

and for gradual area expansion between 45 and 180 degrees:

Kexpansion=Cexpansion(1−R)2.

The hydraulic loss coefficient for the pipe change segment is
calculated from these values as:

K=Kexpansion+Kcontraction−Kexpansion2(tanh(3m˙Am˙th)+1),

where:

- m˙A is the mass flow rate through
  port **A**. Mass is conserved through the segment: m˙A+m˙B=0.
- m˙th is the threshold mass flow rate for flow reversal,
  which is based on the **Critical Reynolds number**,
  *Re*c:

  m˙th=RecARυρ¯Dh,

  where:

  - *A*R is the smallest
    segment area (either the **Cross-sectional area at port
    A** or the **Cross-sectional area at port
    B**.)
  - *ν* is the fluid kinematic viscosity.
  - ρ¯ is the average fluid density.
  - *D*h is the hydraulic
    diameter at *A*R: Dh=4ARπ.

### Tabulated Data Parameterization

The loss factor can also be parameterized with user-provided data interpolated from the
Reynolds number at the smallest area, which in turn is a function of the
**Critical Reynolds number**

K=TLU(Re).

Linear interpolation is employed between data points, and
nearest-neighbor extrapolation is employed beyond the table boundaries.

### Pressure Differential

The pressure differential over the area change is

pA−pB=m˙22ρ¯AR2(1−R2)+Δploss,

where the pressure loss is:

Δploss=K2ρ¯AR2m˙Am˙A2+m˙th2.
