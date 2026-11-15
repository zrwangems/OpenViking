---
type: simulink-block
title: 'Local Resistance (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Pipes and Fittings'
documentation_page: 'localresistancema'
documentation_source_path: 'ref/localresistancema.html'
language: en
---

# Local Resistance (MA)

## Ports

### Conserving

### **A** — Liquid port moist air

Moist air conserving port associated with the entry or exit port to the pipe
segment. Flow is positive from port **A** to port
**B**.

### **B** — Liquid port moist air

Moist air conserving port associated with the entry or exit port to the pipe
segment. Flow is positive from port **A** to port
**B**.

## Parameters

### **Local loss parametrization** — Loss factor calculation method `Constant` (default) | `Tabulated data - loss coefficient vs. Reynolds number`

Method of calculating the pipe segment loss factor. You can parameterize the loss
factor as either a linear relationship between the segment pressure drop and constant
loss factor or by specifying the loss factor and Reynolds number data.

### **Forward flow loss coefficient (from A to B)** — Loss coefficient for flow from port A to B `1` (default) | positive scalar

Loss coefficient associated with pressure loss for flows from port
**A** to port **B**.

#### Dependencies

To enable this parameter, set **Local loss parameterization** to
`Constant`.

### **Reverse flow loss coefficient (from B to A)** — Loss coefficient for flow from port B to A `1` (default) | positive scalar

Loss coefficient associated with pressure loss for flows from port
**B** to port **A**.

#### Dependencies

To enable this parameter, set **Local loss parameterization** to
`Constant`.

### **Reynolds number vector** — Reynolds numbers for tabular parameterization `[-500, -200, -100, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]` (default) | 1-by-*n* vector

Vector of Reynolds numbers for the tabular parameterization of the loss coefficient.
The vector elements must correspond one-to-one with the elements in the **Loss
coefficient vector** parameter. List the elements in ascending order.

#### Dependencies

To enable this parameter, set **Local loss parameterization** to
`Tabulated data - loss coefficient vs. Reynolds
number`.

### **Loss coefficient vector** — Loss coefficients for tabular parameterization `[.65, .75, .9, 1.15, 1.35, 1.65, 2.3, 3.1, 4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]` (default) | 1-by-*n* vector

Vector of loss coefficients for the tabular parameterization of the loss
coefficient. The vector elements must correspond one-to-one with the elements in the
**Reynolds number vector** parameter. The elements must be greater
than 0.

#### Dependencies

To enable this parameter, set **Local loss parameterization** to
`Tabulated data - loss coefficient vs. Reynolds
number`.

### **Flow area** — Segment cross-sectional area `1e-3 m^2` (default) | positive scalar

Cross-sectional area of the pipe segment.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

## Libraries

Simscape / Fluids / Moist Air / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To
model water droplets, select **Enable entrained water droplets** in the
Moist Air Properties
(MA) block connected to your moist air network.

## Description

Pipe resistance in a moist air network

The Local Resistance (MA) block models the pressure loss
due to user-defined pipe resistance in a moist air network. You can specify different loss
coefficients for forward and reversed flows through the pipe segment.

You can parameterize the loss factor as either a constant relationship based on the pipe
pressure or by specifying tabular data for loss coefficients based on the Reynolds number.

### Constant Loss Factor

When you set **Local loss parameterization** to
`Constant`, the losses remain constant over the range of flow
velocities. The loss factor is

kloss=kloss,BA+(kloss,AB−kloss,BA)2[tanh(3ΔpΔpcrit)+1],

where:

- *kloss,AB* and
  *kloss,BA* are the values of the
  **Forward flow loss coefficient (from A to B)** and
  **Reverse flow loss coefficient (from B to A)** parameters,
  respectively.
- *Δp* is the pressure difference, which is
  *pA* –
  *pB*.

The critical pressure difference, *Δpcrit*, is
the pressure differential associated with the **Critical Reynolds number**
parameter, *Recrit*, which is the flow regime
transition point between laminar and turbulent flow,

Δpcrit=ρ¯2kloss,crit(νRecritDh)2,

where:

- *kloss,crit* is the loss factor associated
  with the critical pressure. The value is based on an average of the forward and
  reverse loss coefficients.
- *ν* is the fluid kinematic viscosity.
- ρ¯ is the average fluid density.
- *Dh* is the segment hydraulic diameter,
  which is the equivalent diameter of a pipe with a non-circular cross-section, Dh=4Aflowπ, where *Aflow* is the value
  of the **Flow area** parameter.

### Tabulated Loss Coefficient

When you set **Local loss parameterization** to `Tabulated
data - loss coefficient vs. Reynolds number`, you can interpolate the loss
coefficient from the Reynolds number and the loss coefficient data. The vector of Reynolds
numbers can have both positive and negative values, which indicate forward and reverse flow,
respectively: kloss=TLU(Re).

### Mass Flow Rate

The block conserves mass such that

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where:

- m˙*B* is the mixture mass flow
  rate at port **B**.
- m˙*wA* and m˙*wB* are the water vapor mass
  flow rates at ports **A** and **B**,
  respectively.
- m˙*gA* and m˙*gB* are the trace gas mass
  flow rates at ports **A** and **B**,
  respectively.
- m˙*dA* and m˙*dB* are the water droplets
  mass flow rates at ports **A** and **B**,
  respectively.

The mass flow rate through the valve is

m˙=Aflow2ρ¯klossΔp[Δp2+Δpcrit2]1/4,

where *kloss* is the flow loss
coefficient.

### Energy Balance

The block balances energy such that

ΦA+ΦB=0,

where:

- *ϕA* is the energy flow rate at port
  **A**.
- *ϕB* is the energy flow rate at port
  **B**.
