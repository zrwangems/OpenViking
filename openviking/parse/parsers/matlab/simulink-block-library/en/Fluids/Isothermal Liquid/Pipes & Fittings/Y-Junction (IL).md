---
type: simulink-block
title: 'Y-Junction (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'yjunctionil'
documentation_source_path: 'ref/yjunctionil.html'
language: en
---

# Y-Junction (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the liquid entrance
or exit of the junction.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the liquid entrance
or exit of the junction.

### **C** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the liquid entrance
or exit of the junction.

## Parameters

### **Main branch area (A-B)** — Cross-sectional area between ports A and B `0.01 m^2` (default) | positive scalar

Area of connecting pipe between ports **A** and
**B**.

### **Side branch area (C)** — Cross-sectional area of the side branch `0.004` `m^2` (default) | positive scalar

Area of connecting pipe between port **C** and the main
branch.

### **Loss coefficient model** — Loss coefficient type `Idel'chik correlation` (default) | `Custom`

Junction loss coefficient model. Set this parameter to
`Custom` to specify individual diverging and
converging loss coefficients for each flow path segment.

### **Loss coefficient configuration change time constant** — Time scale of smoothing function `0.0001 s` (default) | positive scalar

Time scale of the smoothing function. Use this parameter to ensure smooth
transitions by tuning the block dynamic behavior during flow reversals.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the junction.

### **Zero-flow threshold Reynolds number** — Reynolds number that corresponds to stagnant flow `10` (default) | positive scalar

Reynolds number that the block uses to calculate the threshold beneath
which the flow is stagnant. The block uses this threshold to reduce
numerical chatter during simulation. This parameter does not have a physical
meaning, but must be small in comparison to the expected mass flow rate
values.

### **Junction angle between (A-C)** — Offset angle of side branch `45` `deg` (default) | scalar between 15 and 60

Angle of the side branch offset with respect to the main branch.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Idel'chik
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
model** to `Idel'chik
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
model** to `Idel'chik
correlation`.

### **Fluid inertia** — Option to model fluid inertia `off` (default) | `on`

Whether to model fluid inertia, which lowers the risk of a block
numerical issue during flow reversals. Avoid modeling fluid inertia unless
it is numerically necessary, because it increases the computational
cost.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Idel'chik
correlation`.

### **Report when flow configuration is invalid** — Simulation warning mode for invalid flow configurations `None` (default) | `Warning` | `Error`

Simulation warning mode for operating conditions outside the valid flow
configurations. If you select `Warning`, the block
generates a warning for conditions outside the valid flow configurations.
The warning does not cause simulation to stop. If you select
`Error`, the simulation will stop for
conditions outside the valid flow configurations.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Idel'chik
correlation`.

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

Loss coefficient for pressure loss calculations between port **C** and
the main line for converging flow.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Custom`.

### **Side branch diverging loss coefficient** — Diverging flow loss coefficient between C and main `1.12` (default) | positive scalar

Loss coefficient for pressure loss calculations between port
**C** and the main line for diverging flow.

#### Dependencies

To enable this parameter, set **Loss coefficient
model** to `Custom`.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2024b: Robustness improvements enable block to more smoothly switch between mode chart states

The Y-Junction (IL) block has new parameters and
functionality that enable the block to more smoothly switch between states in mode charts.
Adjust the **Loss coefficient configuration change time constant**
parameter to control the time scale of the smoothing function. Use the **Zero-flow
threshold Reynold number** parameter to calculate a non-zero mass flow rate
threshold for stagnant flow. You can also now optionally model fluid inertia, which lowers
the risk of a block numerical issue during flow reversals.

Results during flow reversals may be different than in previous releases. The behavior at
steady-state conditions has not changed.

## Description

Y-junction in an isothermal liquid system

The Y-Junction (IL) block models a Y-junction consisting of a main branch and a side branch
in an isothermal liquid network. The path between ports **A** and
**B** is the main branch. The path between ports
**A** and **C** or between ports
**B** and **C** is the side branch.

### Flow Direction

The flow is *converging* when the flow through port
**C** merges into the main flow. The flow is
*diverging* when the branch flow splits from the main flow.

The block uses mode charts to determine each loss coefficient for a given flow
configuration. This
table
describes the conditions and coefficients when the **Loss coefficient
model** parameter is `Custom`.

| Flow Scenario | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| Stagnant | – | – | – | 1 or last valid value | 1 or last valid value | 1 or last valid value |
| Diverging from node A | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *Kmain,div* | *Kside,div* |
| Diverging from node B | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| Converging to node A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *Kmain,conv* | *Kside,conv* |
| Converging to node B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| Converging to node C (branch) | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | (*Kmain,conv* + *Kside,conv*)/2 | (*Kmain,conv* + *Kside,conv*)/2 | 0 |
| Diverging from node C (branch) | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | (*Kmain,div* + *Kside,div*)/2 | (*Kmain,div* + *Kside,div*)/2 | 0 |

This table describes the conditions and coefficients when the **Loss coefficient
model** parameter is `Idel'chik
correlation`.

| Flow Scenario | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| Stagnant | – | – | – | 1 or last valid value | 1 or last valid value | 1 or last valid value |
| Diverging from node A — Invalid | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | 1 | 1 |
| Diverging from node B | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| Converging to node A — Invalid | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | 1 | 1 |
| Converging to node B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| Converging to node C (branch) — Invalid | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | 1 | 1 | 0 |
| Diverging from node C (branch) — Invalid | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | 1 | 1 | 0 |

In stagnant flow, the mass flow rate conditions do not match any defined flow scenario.
Stagnant flow is permitted at the start of the simulation, but the block does not
revert to stagnant flow after it has achieved another mode. The mass flow rate
threshold, which is the point at which the flow in the pipe begins to reverse
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

### Idel'chik Correlation Coefficient Model

When you set the **Loss coefficient model** parameter to
`Idel'chik correlation`, the block calculates the pipe
loss coefficients according to [1].

**Flow Configuration**

The block supports two flow configurations between the main branch from ports
**A** and **B** and the side branch from
port **C**. The side branch is offset from the main branch at
an angle *α*, which is the value of the **Junction
angle between (A-C)** parameter.

In a converging flow, the flow enters at ports **A** and
**C** and exits at port **B**.

In a diverging flow, the flow enters at port **B** and exits at ports
**A** and **C**.

You can control the block behavior in a prohibited flow configuration by using
the **Report when flow configuration is invalid** parameter. If
the **Report when flow configuration is invalid** parameter is
set to `None` or `Warning`,
the model continues to run in the prohibited flow configuration, but the results
may not be correct.

**Converging Flow**

For a converging flow, the block calculates the loss coefficient of the side branch
between ports **C** and **B** using a
simplified version of Idel'chik that assumes the area of the main branch is
constant. The loss coefficient of the side branch is

Kside,conv=[1+(m˙Cm˙BABAC)2−2(ABAA)(1−m˙Cm˙B)2−2∗cosα∗ABAC(m˙Cm˙B)2][m˙Cm˙BACAB]−2,

where:

- m˙A,m˙B,m˙C are the mass flow rates from rates at ports
  **A**, **B**, and
  **C**, respectively.
- *AA*,
  *AB*,
  *AC* are fitting
  coefficients for ports **A**,
  **B**, and **C**,
  respectively.

The block calculates the loss coefficient of the main branch between ports
**A** and **B** using a simplified version
of Idel'chik that assumes the main branch area is constant and QC=QB+QS, where *Q* is the volumetric flow rate
through the specified port. The main branch loss coefficient is

Kmain,conv=[1−(1−m˙Cm˙B)2−2∗cosα∗ABAC(m˙Cm˙B)2][1−(m˙Cm˙B)2]−1.

**Diverging Flow**

For a diverging flow, the block calculates the loss coefficient of the side
branch between ports **C** and **B** as

Kside,div=A′[1+(m˙Cm˙BABAC)2−2∗cosα∗m˙Cm˙BABAC][m˙Cm˙BACAB]−2,

where

A'=12[1+tanh(4(RA′−0.8)0.8)]+0.92[1−tanh(4(RA′−0.8)0.8)]

and

RA′=m˙C2+m˙thresh2m˙B2+m˙thresh2.

The block calculates the loss coefficient of the main branch between ports
**A** and **B** as

Kmain,div=0.4(1−m˙Am˙BABAA)2(m˙Am˙B)−2.

### Custom Y-Junction

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
coefficient** parameters, respectively. The custom loss coefficient
model behavior for the Y-junction is the same as for the custom T-junction.

### Mass and Momentum Balance

The block conserves mass in the junction such that

m˙A+m˙B+m˙C=0.

Flow through the pipe junction behaves according to the momentum
conservation equations between ports **A**, **B**,
and **C**:

pA−pI=IA+KA2ρ¯Amain2m˙Am˙A2+m˙thresh2pB−pI=IB+KB2ρ¯Amain2m˙Bm˙B2+m˙thresh2pC−pI=IC+KC2ρ¯Aside2m˙Cm˙C2+m˙thresh2

where *I* represents the fluid inertia, and

IA=m¨Aπ⋅AsideAmainIB=m¨Bπ⋅AsideAmainIC=m¨Cπ⋅AmainAside

*Amain* is the
**Main branch area (A-B)** parameter and
*Aside* is the **Side branch
area (C)** parameter.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
