---
type: simulink-block
title: 'T-Junction (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'tjunctionil'
documentation_source_path: 'ref/tjunctionil.html'
language: en
---

# T-Junction (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port.

### **C** — Liquid port isothermal liquid

Liquid entry or exit port.

## Parameters

### **Main branch area (A-B)** — Cross-sectional area between ports A and B `0.01 m^2` (default) | positive scalar

Area of connecting pipe between ports **A** and
**B**.

### **Side branch area (A-C, B-C)** — Cross-sectional area of the side branch `0.01 m^2` (default) | positive scalar

Area of connecting pipe between ports **A** and
**C** and between ports **B** and
**C**.

### **Loss coefficient model** — Loss coefficient type `Crane correlation` (default) | `Rennels correlation` | `Custom` | `Constant Coefficients`

The junction loss coefficient model. Set this parameter to
`Custom` to specify individual diverging and
converging loss coefficients for each flow path segment.

### **Loss coefficient configuration change time constant** — Time scale of smoothing function `0.0001 s` (default) | positive scalar

Time scale of the smoothing function. Use this parameter to ensure smooth
transitions by tuning the block dynamic behavior during flow reversals.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to either `Crane
correlation`, `Rennels
correlation`, or
`Custom`.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the junction.

### **Zero-flow threshold Reynolds number** — Reynolds number that corresponds to stagnant flow `10` (default) | positive scalar

Reynolds number that the block uses to calculate the threshold beneath
which the flow is stagnant. The block uses this threshold to reduce
numerical chatter during simulation. This parameter does not have a physical
meaning, but must be small in comparison to the expected mass flow rate
values.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to either `Crane
correlation`, `Rennels
correlation`, or
`Custom`.

### **Main branch converging loss coefficient** — Converging flow loss coefficient between A and B `1.12` (default) | positive scalar

Loss coefficient for pressure loss calculations between ports
**A** and **B** for converging
flow.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Custom`.

### **Main branch diverging loss coefficient** — Diverging flow loss coefficient between A and B `1.12` (default) | positive scalar

Loss coefficient for pressure loss calculations between ports
**A** and **B** for diverging
flow.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Custom`.

### **Side branch converging loss coefficient** — Converging flow loss coefficient between C and main `1.12` (default) | positive scalar

Loss coefficient for pressure loss calculations between port
**C** and the main line for converging flow.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Custom`.

### **Side branch diverging loss coefficient** — Diverging flow loss coefficient between C and main `1.12` (default) | positive scalar

Loss coefficient for pressure loss calculations between port
**C** and the main line for diverging flow.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Custom`.

### **Junction radius of curvature** — Radius of curvature of the junction `0.001 m` (default) | positive scalar

Radius of the curvature of the junction used to calculate the loss
coefficients when **Loss coefficient model** is set to
`Rennels correlation`.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Rennels
correlation`.

### **Minimum valid flow ratio for coefficient calculation** — Limit on flow ratios for coefficient calculations `0.2` (default) | positive scalar

Minimum value for any flow ratio that the block uses to calculate loss
coefficients. If the flow ratio is below this limit, it saturates at this
value. The block uses this parameter to limit the impact of differences in
flow magnitude between branches and to increase numerical stability if one
branch has significantly less flow than others.

Only adjust this setting if your model has numerical stability problems.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Rennels
correlation`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | scalar between 0 and 1

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when it approaches the limit specified by the
**Minimum valid flow ratio for coefficient
calculation** parameter. Set this parameter to a nonzero value
less than one to increase the stability of your simulation.

Only adjust this setting if your model has numerical stability problems.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Rennels
correlation`.

### **Fluid inertia** — Option to model fluid inertia `off` (default) | `on`

Whether to model fluid inertia, which lowers the risk of a block
numerical issue during flow reversals. Avoid modeling fluid inertia unless
it is numerically necessary, because it increases the computational
cost.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Rennels
correlation`.

### **Loss coefficient A** — Loss coefficient for branch A `1` (default) | positive scalar

Loss coefficient for flow along branch A.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Constant
Coefficients`.

### **Loss coefficient B** — Loss coefficient for branch B `1` (default) | positive scalar

Loss coefficient for flow along branch B.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Constant
Coefficients`.

### **Loss coefficient C** — Loss coefficient for branch C `1` (default) | positive scalar

Loss coefficient for flow along branch C.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Constant
Coefficients`.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024b: New model for constant loss coefficients

Set **Loss coefficient model** to `Constant
Coefficients` to use a constant loss coefficient model. Use this
option when your model does not require high fidelity.

### R2024b: Robustness improvements enable block to more smoothly switch between mode chart states

The T-Junction (IL) block has new parameters and
functionality that enable the block to more smoothly switch between states in mode charts.
Adjust the **Loss coefficient configuration change time constant**
parameter to control the time scale of the smoothing function. Use the **Zero-flow
threshold Reynold number** parameter to calculate a non-zero mass flow rate
threshold for stagnant flow. You can also now optionally model fluid inertia, which lowers
the risk of a block numerical issue during flow reversals.

Results during flow reversals may be different than in previous releases. The behavior at
steady-state conditions has not changed.

### R2023a: New pipe loss coefficient models

The **Three-way junction type** parameter is renamed to the
**Loss coefficient model** parameter. Set **Three-way
junction type** to `Rennels correlation` to
use the new loss coefficient model. The `Standard` option
for this parameter is renamed to `Crane correlation` and
the `Custom` option remains unchanged.

### R2022b: Conversion to Mode Charts

The block uses mode charts to handle the different flow configurations. Results during flow
scenario transitions may be different than in previous releases. Results during flow
scenario transitions are not steady state and are not necessarily accurate.

## Description

Three-way junction in an isothermal liquid system

The T-Junction (IL) block models a three-way pipe junction with a branch line at port
**C** connected at a 90° angle to the main pipe line, between ports
**A** and **B**. You can specify a custom junction
or a junction that uses a Rennels correlation or Crane correlation loss coefficient.
When **Loss coefficient model** is set to
`Custom`, you can specify the loss coefficients of each
pipe segment for converging and diverging flows.

### Flow Direction

When the **Loss coefficient model** parameter is `Crane
correlation`, `Rennels correlation`, or
`Custom`, the block determines each loss coefficient
based on the flow configuration. The flow is *converging* when
the flow through port **C** merges into the main flow. The flow is
*diverging* when the branch flow splits from the main flow.
The flow direction between **A** and **I**, the
point where the branch meets the main, and **B** and
**I** must be consistent for all loss coefficients to be
applied. If they are not, as shown in the last two diagrams in the figure below, the
losses in the junction are approximated with the main branch loss coefficient for
converging or diverging flows.

Diagram showing possible flow scenarios for the T-Junction block. In a converging flow, 2 perpendicular branch flows meet at the center node. In a diverging flow, one flow enters the center node and divides into the other two perpendicular flows. For flow losses, two parallel flows meet or diverge

The block uses mode charts to determine each loss coefficient for a given flow
configuration. This
table
describes the conditions and coefficients for each operational mode.

| Flow Scenario | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| Stagnant | – | – | – | 1 or last valid value | 1 or last valid value | 1 or last valid value |
| Diverging from node A | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *Kmain,div* | *Kside,div* |
| Diverging from node B | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| Converging to node A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *Kmain,conv* | *Kside,conv* |
| Converging to node B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| Converging to node C (branch) when the **Loss coefficient model** parameter is `Crane correlation` or `Custom` | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | (*Kmain,conv* + *Kside,conv*)/2 | (*Kmain,conv* + *Kside,conv*)/2 | 0 |
| Diverging from node C (branch) when the **Loss coefficient model** parameter is `Crane correlation` or `Custom` | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | (*Kmain,div* + *Kside,div*)/2 | (*Kmain,div* + *Kside,div*)/2 | 0 |

When the **Loss coefficient model** parameter
`Rennels correlation`, the values for converging to
node C (branch) and diverging from node C (branch) are calculated directly.

The flow is stagnant when the mass flow rate conditions do not match any defined flow
scenario. Stagnant flow is permitted at the start of the simulation, but the block
does not revert to stagnant flow after it has achieved another mode. The mass flow
rate threshold, which is the point at which the flow in the pipe begins to reverse
direction, is

m˙thresh=Recυρ¯π4Amin,

where:

- *Re*c is the
  **Critical Reynolds number** parameter, beyond
  which the transitional flow regime begins.
- *ν* is the fluid viscosity.
- ρ¯ is the average fluid density.
- *Amin* is the smallest
  cross-sectional area in the pipe junction.

### Crane Correlation Coefficient Model

When you set the **Loss coefficient model** parameter to
`Crane correlation`, the pipe loss coefficients,
*Kmain* and
*Kside*, and the pipe friction
factor, *f*T, are calculated according to
Crane [1]:

Kmain,div=Kmain,conv=20fT,main,

Kside,div=Kside,conv=60fT,side.

In contrast to the custom junction type, the standard junction
loss coefficient is the same for both converging and diverging flows.
*K*A,
*K*B, and
*K*C are then calculated in the same
manner as custom junctions.

| Nominal size (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Friction factor, *fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

### Rennels Correlation Coefficient Model

When you set the **Loss coefficient model** parameter to
`Rennels correlation`, the block calculates the pipe
loss coefficients according to [2].

**Diverging Flow on Main Branch**

The main branch diverging loss coefficient is

Kmain,div=0.62−0.98m˙1m˙2+0.36(m˙1m˙2)2+0.03(m˙2m˙1)6,

where:

- m˙1 is the mass flow rate at the inflow of the main
  branch.
- m˙2 is the mass flow rate at the outflow of the main
  branch.

The value of *Kmain,div* saturates
when m˙2/m˙1 is equal to the value of the **Minimum valid flow
ratio for coefficient calculation** parameter.

The side branch diverging loss coefficient is

Kside,div=(0.81−1.13m˙1m˙3+(m˙1m˙3)2)(d3d1)4+1.12d3d1−1.08(d3d1)3+K\*,

where

- m˙3 is the mass flow rate at the outflow of the side
  branch.
- *d1* is the diameter of
  the main branch.
- *d3* is the diameter of
  the side branch.
- K\*=0.57−1.07(rd3)1/2−2.13rd3+8.24(rd3)3/2−8.48(rd3)2+2.90(rd3)5/2.
- *r* is the value of the **Junction radius
  of curvature** parameter.

The value of *Kside,div* saturates
when m˙3/m˙1 is equal to the value of the **Minimum valid flow
ratio for coefficient calculation** parameter.

**Converging Flow on Main Branch**

The main branch converging loss coefficient is

Kmain,conv=(m˙1m˙2)2−0.95−2CxC(m˙1m˙2−1)−2CM((m˙1m˙2)2−m˙1m˙2),

where

CM=0.23+1.46(rd3)−2.75(rd3)2+1.65(rd3)3CxC=0.08+0.56(rd3)−1.75(rd3)2+1.83(rd3)3

The value of *Kmain,conv* saturates
when m˙2/m˙1 is equal to the value of the **Minimum valid flow
ratio for coefficient calculation** parameter.

The side branch converging loss coefficient is

Kside,conv=(2CyC−1)+(d3d1)4[2(CxC−1)+2(2−CxC−CM)m˙1m˙3−0.92(m˙1m˙3)2],

where:

CyC=1−0.25(d3d1)1.3−[0.11rd3−0.65(rd3)+0.83(rd3)3](d3d1)2.

The value of *Kside,conv* saturates
when m˙3/m˙1 is equal to the value of the **Minimum valid flow
ratio for coefficient calculation** parameter.

**Converging or Diverging flow from Side Branch**

The loss coefficient when the flow is converging to the side branch is

Kconvtoside=(0.81−1.16rd+0.5rd)(m˙1m˙2)2−(0.95−1.65rd)m˙1m˙2+1.34−1.69rd,

where *d* is the diameter of the side branch. The value of
*Kconv to side* saturates when m˙2/m˙1 is equal to the value of the **Minimum valid flow
ratio for coefficient calculation** parameter.

The loss coefficient when the flow is diverging from the side branch is

Kdivfromside=0.59(m˙1m˙2)2+(1.18−1.84rd+1.16rd)m˙1m˙2−0.68+1.04rd−1.16rd.

The value of *Kdiv from side*
saturates when m˙2/m˙1 is equal to the value of the **Minimum valid flow
ratio for coefficient calculation** parameter.

### Custom T-Junction

When you set the **Loss coefficient model** parameter to
`Custom`, the block calculates the pipe loss
coefficient at each port, *K*, based on the user-defined loss
parameters for converging and diverging flow and mass flow rate at each port. You
must specify *Kmain,conv*,
*Kmain,div*,
*Kside,conv*, and
*Kside,div* as the **Main
branch converging loss coefficient**, **Main branch diverging
loss coefficient**, **Side branch converging loss
coefficient**, and **Side branch diverging loss
coefficient** parameters, respectively.

### Constant Coefficients T-Junction

When you set the **Loss coefficient model** parameter to
`Constant Coefficients`, the block models the junction
as a composite component of three Local Resistance
(IL) blocks joined at a center node. When the block uses this
setting, it does not use mode charts. Use this option if your model operates at
nominal conditions and does not require high fidelity.

### Mass and Momentum Balance

The block conserves mass in the junction such that

m˙A+m˙B+m˙C=0.

The block calculates the flow through the pipe junction using the
momentum conservation equations between ports **A**,
**B**, and **C**:

pA−pI=IA+KA2ρ¯Amain2m˙Am˙A2+m˙thresh2pB−pI=IB+KB2ρ¯Amain2m˙Bm˙B2+m˙thresh2pC−pI=IC+KC2ρ¯Aside2m˙Cm˙C2+m˙thresh2

where *I* represents the fluid inertia, and

IA=m¨Aπ⋅AsideAmainIB=m¨Bπ⋅AsideAmainIC=m¨Cπ⋅AmainAside

*Amain* is the
**Main branch area (A-B)** parameter and
*Aside* is the **Side branch
area (A-C, B-C)** parameter.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
