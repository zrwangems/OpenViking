---
type: simulink-block
title: 'Cross-Junction (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Pipes & Fittings'
documentation_page: 'crossjunctionma'
documentation_source_path: 'ref/crossjunctionma.html'
language: en
---

# Cross-Junction (MA)

## Ports
```yaml
ports:
- name: A
  summary: Moist air port moist air
  direction: conserving
- name: B
  summary: Moist air port moist air
  direction: conserving
- name: C
  summary: Moist air port moist air
  direction: conserving
- name: D
  summary: Moist air port moist air
  direction: conserving
```

### Conserving

### **A** — Moist air port moist air

Moist air conserving port associated with the liquid port.

### **B** — Moist air port moist air

Moist air conserving port associated with the liquid port.

### **C** — Moist air port moist air

Moist air conserving port associated with the liquid port.

### **D** — Moist air port moist air

Moist air conserving port associated with the liquid port.
## Parameters
```yaml
parameters:
- name: Main line area (A,C)
  summary: Area of main path 0.01 m^2 (default) | positive scalar
  group: Junction Properties
- name: Branch line area (B,D)
  summary: Area of branch path 0.01 m^2 (default) | positive scalar
  group: Junction Properties
- name: Laminar flow pressure ratio
  summary: Pressure ratio at which flow transitions between laminar and turbulent regimes 0.999 (default) | positive scalar
  group: Junction Properties
- name: Zero-flow threshold pressure ratio
  summary: Pressure ratio that corresponds to stagnant flow 0.999999 (default) | positive scalar
  group: Junction Properties
- name: Loss coefficient configuration change time constant
  summary: Time scale of smoothing function 0.0001 s (default) | positive scalar
  group: Junction Properties
- name: Minimum valid flow ratio for coefficient calculation
  summary: Limit on flow ratios for coefficient calculations 0.2 (default) | positive scalar
  group: Junction Properties
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | scalar between 0 and 1
  group: Junction Properties
- name: Fluid inertia
  summary: Option to model fluid inertia off (default) | on
  group: Junction Properties
- name: Loss coefficient model
  summary: Loss coefficient type Idel'chik correlation (default) | Custom
  group: Junction Properties
- name: Report when flow configuration is invalid
  summary: Simulation warning mode for invalid flow configurations None (default) | Warning | Error
  group: Junction Properties
- name: Diverging flow loss coefficients
  summary: Option to specify loss coefficients for diverging flow on (default) | off
  group: Junction Properties
- name: Converging flow loss coefficients
  summary: Option to specify loss coefficients for converging flow on (default) | off
  group: Junction Properties
- name: Perpendicular flow loss coefficients
  summary: Option to specify loss coefficients for perpendicular flow off (default) | on
  group: Junction Properties
- name: Colliding flow loss coefficients
  summary: Option to specify loss coefficients for colliding flow off (default) | on
  group: Junction Properties
- name: Diverging flow straight loss coefficient
  summary: Diverging flow straight loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Diverging Flow Coefficients
- name: Diverging flow turning loss coefficient
  summary: Diverging flow turning loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Diverging Flow Coefficients
- name: Converging flow straight loss coefficient
  summary: Converging flow straight loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Converging Flow Coefficients
- name: Converging flow turning loss coefficient
  summary: Converging flow turning loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Converging Flow Coefficients
- name: Perpendicular flow straight loss coefficient
  summary: Perpendicular flow straight loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Perpendicular Flow Coefficients
- name: Perpendicular flow turning to inflow loss coefficient
  summary: Perpendicular flow turning to inflow loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Perpendicular Flow Coefficients
- name: Perpendicular flow turning to outflow loss coefficient
  summary: Perpendicular flow turning to outflow loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Perpendicular Flow Coefficients
- name: Colliding flow straight loss coefficient
  summary: Colliding flow straight loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Colliding Flow Coefficients
- name: Colliding flow turning loss coefficient
  summary: Colliding flow turning loss coefficient [1.12, 1.12] (default) | positive scalar or vector
  group: Colliding Flow Coefficients
```

### Junction Properties

### **Main line area (A,C)** — Area of main path `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the main flow path from port **A** to
port **C**.

### **Branch line area (B,D)** — Area of branch path `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the branch flow path from port **B** to
port **D**.

### **Laminar flow pressure ratio** — Pressure ratio at which flow transitions between laminar and turbulent regimes `0.999` (default) | positive scalar

Pressure ratio at which the moist air flow transitions between the laminar and
turbulent regimes.

### **Zero-flow threshold pressure ratio** — Pressure ratio that corresponds to stagnant flow `0.999999` (default) | positive scalar

Pressure ratio that the block uses to calculate the threshold beneath which the
flow is stagnant. The block uses this threshold to reduce numerical chatter during
simulation.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
either `Crane correlation`, `Rennels
correlation`, or `Custom`.

### **Loss coefficient configuration change time constant** — Time scale of smoothing function `0.0001 s` (default) | positive scalar

Time scale of the smoothing function. Use this parameter to ensure smooth
transitions by tuning the block dynamic behavior during flow reversals.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
either `Crane correlation`, `Rennels
correlation`, or `Custom`.

### **Minimum valid flow ratio for coefficient calculation** — Limit on flow ratios for coefficient calculations `0.2` (default) | positive scalar

Minimum value for any flow ratio that the block uses to calculate loss
coefficients. If the flow ratio is below this limit, it saturates at this value. The
block uses this parameter to limit the impact of differences in flow magnitude between
branches and to increase numerical stability if one branch has significantly less flow
than others.

Only adjust this setting if your model has numerical stability problems.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Idel'chik correlation`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | scalar between 0 and 1

Continuous smoothing factor that introduces a layer of gradual change to the flow
response when it approaches the limit specified by the **Minimum valid flow
ratio for coefficient calculation** parameter. Set this parameter to a
nonzero value less than one to increase the stability of your simulation.

Only adjust this setting if your model has numerical stability problems.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Idel'chik correlation`.

### **Fluid inertia** — Option to model fluid inertia `off` (default) | `on`

Whether to model fluid inertia, which lowers the risk of a block numerical issue
during flow reversals. Avoid modeling fluid inertia unless it is numerically
necessary, because it increases the computational cost.

### **Loss coefficient model** — Loss coefficient type `Idel'chik correlation` (default) | `Custom`

Junction loss coefficient model. Set this parameter to
`Custom` to specify individual diverging and converging
loss coefficients for each flow path segment.

### **Report when flow configuration is invalid** — Simulation warning mode for invalid flow configurations `None` (default) | `Warning` | `Error`

Simulation warning mode for operating conditions outside the valid flow
configurations. If you select `Warning`, the block generates
a warning for conditions outside the valid flow configurations. The warning does not
cause simulation to stop. If you select `Error`, the
simulation will stop for conditions outside the valid flow configurations.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Idel'chik correlation`.

### **Diverging flow loss coefficients** — Option to specify loss coefficients for diverging flow `on` (default) | `off`

Whether to specify loss coefficients for diverging flow.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom`.

### **Converging flow loss coefficients** — Option to specify loss coefficients for converging flow `on` (default) | `off`

Whether to specify loss coefficients for converging flow.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom`.

### **Perpendicular flow loss coefficients** — Option to specify loss coefficients for perpendicular flow `off` (default) | `on`

Whether to specify loss coefficients for perpendicular flow.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom`.

### **Colliding flow loss coefficients** — Option to specify loss coefficients for colliding flow `off` (default) | `on`

Whether to specify loss coefficients for colliding flow.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom`.

### Diverging Flow Coefficients

### **Diverging flow straight loss coefficient** — Diverging flow straight loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the straight portion of the diverging flow. When you specify
this parameter as a vector, the first element represents the loss coefficient when
ports **A** or **C** align to node 1. The second
element represents when ports **B** or **D** align
to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Diverging flow loss
coefficients**.

### **Diverging flow turning loss coefficient** — Diverging flow turning loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the turning portions of the diverging flow. When you specify
this parameter as a vector, the first element represents the loss coefficient when
ports **A** or **C** align to node 1. The second
element represents when ports **B** or **D** align
to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Diverging flow loss
coefficients**.

### Converging Flow Coefficients

### **Converging flow straight loss coefficient** — Converging flow straight loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the straight portion of the converging flow. When you specify
this parameter as a vector, the first element represents the loss coefficient when
ports **A** or **C** align to node 1. The second
element represents when ports **B** or **D** align
to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Converging flow loss
coefficients**.

### **Converging flow turning loss coefficient** — Converging flow turning loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the turning portions of the converging flow. When you specify
this parameter as a vector, the first element represents the loss coefficient when
ports **A** or **C** align to node 1. The second
element represents when ports **B** or **D** align
to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Converging flow loss
coefficients**.

### Perpendicular Flow Coefficients

### **Perpendicular flow straight loss coefficient** — Perpendicular flow straight loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the straight portion of the perpendicular flow. When you
specify this parameter as a vector, the first element represents the loss coefficient
when ports **A** or **C** align to node 1. The
second element represents when ports **B** or **D**
align to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Perpendicular flow loss
coefficients**.

### **Perpendicular flow turning to inflow loss coefficient** — Perpendicular flow turning to inflow loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the flow turning to inflow in the perpendicular flow. When
you specify this parameter as a vector, the first element represents the loss
coefficient when ports **A** or **C** align to node
1. The second element represents when ports **B** or
**D** align to node 1. The block behaves the same for all
orientations when you use a scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Perpendicular flow loss
coefficients**.

### **Perpendicular flow turning to outflow loss coefficient** — Perpendicular flow turning to outflow loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the flow turning to outflow in the perpendicular flow. When
you specify this parameter as a vector, the first element represents the loss
coefficient when ports **A** or **C** align to node
1. The second element represents when ports **B** or
**D** align to node 1. The block behaves the same for all
orientations when you use a scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Perpendicular flow loss
coefficients**.

### Colliding Flow Coefficients

### **Colliding flow straight loss coefficient** — Colliding flow straight loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the straight portion of the colliding flow. When you specify
this parameter as a vector, the first element represents the loss coefficient when
ports **A** or **C** align to node 1. The second
element represents when ports **B** or **D** align
to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Colliding flow loss
coefficients**.

### **Colliding flow turning loss coefficient** — Colliding flow turning loss coefficient `[1.12, 1.12]` (default) | positive scalar or vector

Loss coefficient for the turning portion of the colliding flow. When you specify
this parameter as a vector, the first element represents the loss coefficient when
ports **A** or **C** align to node 1. The second
element represents when ports **B** or **D** align
to node 1. The block behaves the same for all orientations when you use a
scalar.

#### Dependencies

To enable this parameter, set **Loss coefficient model** to
`Custom` and select **Colliding flow loss
coefficients**.
## Libraries

Simscape / Fluids / Moist Air / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Cross-junction in a moist air network

The Cross-Junction (MA) block represents a four-way
junction in a moist air network. The block abstracts the fluid interactions depending on the
direction of flow at each port, where ports **A** and **C**
are the main line and ports **B** and **D** are the branch
line. The block models losses with hydraulic loss coefficients and the results may be more
accurate for lower speed flows where you can neglect compressible flow effects.

### Mass, Momentum, and Energy Balance

The block conserves mass such that

m˙A+m˙B+m˙C+m˙D=0m˙wA+m˙wB+m˙wC+m˙wD=0m˙gA+m˙gB+m˙gC+m˙gD=0m˙dA+m˙dB+m˙dC+m˙dD=0

- *ṁi* is the mixture mass flow rate for a
  given port, *i*.
- m˙*wi* is the water vapor mass
  flow rate for a given port, *i*.
- m˙*gi* is the trace gas mass
  flow rate for a given port, *i*.
- m˙*di* is the water droplet
  mass flow rate for a given port, *i*.

The block determines which coefficient and vector element to use, then computes the
pressure difference to conserve momentum such that

pi−p1=Ii+ki2m˙im˙i2+m˙threshold2ρ¯Ai2,

where:

- ρ¯ is the average fluid density.
- *pi* is the pressure for a given port,
  *i*.
- *p1* is the pressure at node 1.
- *ki* is the flow coefficient that the
  block assigns to a given port, *i*. The **Loss coefficient
  model** parameter specifies the block method used to calculate
  *ki*.
- *Ii* is the fluid inertia for a given
  port, *i*.

The block calculates the inertia for each port as

IA=m¨AπAsideAmainIB=m¨BπAmainAsideIC=m¨CπAsideAmainID=m¨DπAmainAside

where *Amain* is the value of the
**Main line area (A,C)** parameter and
*Aside* is the value of the **Branch
line area (B,D)** parameter.

The block conserves energy such that

φA+φB+φC+φD=0.

### Idel'chik Correlation Coefficient Model

When you set the **Loss coefficient model** parameter to
`Idel'chik correlation`, the block calculates the pipe loss
coefficients according to [1]. The
Idel'chik model only supports flow converging to port **C** or flow
diverging from port **C**. To achieve expected results, orient the block
appropriately to the expected flow configuration of the model fluid network.

The block treats the junction as symmetrical about both the horizontal and vertical
planes such that *AA* =
*AC* is the value of the **Main line area (A,C)** parameter,
and *AB* =
*AD* is the value of the **Branch line area (B,D)** parameter,
where *AA,B,C,D* is the area of the corresponding
port.

Diagram of the two Idel'chik flow configurations: diverging flow and converging flow

In the case of a prohibited flow geometry, you can control the block behavior by using
the **Report when flow configuration is invalid** parameter. If the
**Report when flow configuration is invalid** parameter is
`None` or `Warning`, the model continues
to run in the prohibited flow configuration, but the results may not be correct.

**Converging Flow to Port C**

When the flow is converging to port **C**, the loss coefficients for
ports **A** and **C** are

kA=(1+(m˙Am˙C)2−(m˙Am˙C)21+m˙Am˙C(0.75+0.25m˙Am˙C)2)(m˙Am˙CACAA)−2kC=0

The converging flow loss coefficients for ports **B** and
**D** are

kB=(1+(m˙Bm˙CACAB)2−8(m˙Bm˙C)2[m˙Cm˙B−(1+m˙Dm˙B)]24−(1+m˙Dm˙B)m˙Bm˙C)(m˙Bm˙CACAB)−2kD=(1+(m˙Dm˙CACAD)2−8(m˙Dm˙C)2[m˙Cm˙D−(1+m˙Bm˙D)]24−(1+m˙Bm˙D)m˙Dm˙C)(m˙Dm˙CACAD)−2

**Diverging Flow From Port C**

When the flow diverges from port **C**, the loss coefficients for
ports **A** and **C** are

kA=0.4(m˙Cm˙A−1)2kC=0

The diverging flow loss coefficients for ports **B** and
**D** are

kB=A'(m˙Cm˙BABAC+1)2kD=A'(m˙Cm˙DADAC+1)2

where *A'=1* when m˙Bm˙CACAB≤0.8 or m˙Dm˙CACAD≤0.8 and *A'≈0.9* when m˙Bm˙CACAB>0.8 or m˙Dm˙CACAD>0.8. The block smooths the transition between *A' = 1* and
*A' = 0.9* using a hyperbolic tangent function.

According to [1], these loss coefficients are only applicable for diverging flow when
the ratio of the side branch diameter to the main branch diameter is less than or equal to
`2/3`. However, the expected error for ratios above
`2/3` is generally low enough that the block continues to use the above
loss coefficients.

### Custom Cross-Junction

When you set the **Loss coefficient model** parameter to
`Custom`, the block uses the user-defined loss parameters to
describe the pipe loss coefficient at each port.

For a custom cross-junction, the block allows four configurations diverging flow,
converging flow, perpendicular flow, and colliding flow:

- Diverging flow — Flow enters at node 1 and exits at nodes 2, 3, and 4.
- Converging flow — Flow enters at nodes 1, 2, and 4 and exits at node 3.
- Perpendicular flow — Flow enters at nodes 1 and 2 and exits at nodes 3 and
  4.
- Colliding flow — Flow enters at nodes 1 and 3 and exits at nodes 2 and 4.

This figure demonstrates these configurations.

Diagram of the four flow configurations: diverging flow, converging flow, perpendicular flow, and colliding flow

The block treats the junction as symmetrical about both the horizontal and vertical
planes such that *A1* =
*A3* and *A2* =
*A4*, where *A1,2,3,4* is the area of
the corresponding port in the figure. Using this symmetry, the block assumes the loss
coefficients from 1 to 2 and from 1 to 4 are identical during diverging, converging, and
colliding flow.

During simulation, the block continually checks the direction of flow at each port and
compares the result to the four possible flow configurations. When the block determines the
flow configuration, it adjusts the node that each port corresponds to. For example, when the
block experiences diverging flow where the fluid enters at port **A** and
exits at ports **B**, **C**, and **D**,
it assigns node 1 to port **A** as in the first panel of the figure. The
other panels show the assigned nodes for diverging flow entering at ports other than
**A**.

The four possible orientations of diverging flow, where the entry point is the reference node and can occur at any port.

For the custom cross-junction, all four flow configurations can occur in the same block
during a simulation. You only need to supply parameters for each condition that the block
experiences. If you use two-element vectors to specify the flow coefficients, the block uses
the first or second element depending on whether node 1 aligns with the main line or the
branch line. The first element corresponds to node 1 at port **A** or
**C**, and the second element corresponds to node 1 at port
**B** or **D**.

This table describes the conditions and coefficients for each operational mode used to
determine the loss coefficients.

| Flow Scenario | *ṁA* | *ṁB* | *ṁC* | *ṁD* | *kA* | *kB* | *kC* | *kD* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Diverging from node A | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *kdiv,turning,main* | *kdiv,straight,main* | *kdiv,turning,main* |
| Diverging from node B | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | *kdiv,turning,side* | 0 | *kdiv,turning,side* | *kdiv,straight,side* |
| Diverging from node C | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *kdiv,straight,main* | *kdiv,turning,main* | 0 | *kdiv,turning,main* |
| Diverging from node D | <*-ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kdiv,turning,side* | *kdiv,straight,side* | *kdiv,turning,side* | 0 |
| Converging to node A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *kconv,turning,main* | *kconv,straight,main* | *kconv,turning,main* |
| Converging to node B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | *kconv,turing,side* | 0 | *kconv,turing,side* | *kconv,straight,side* |
| Converging to node C | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kconv,straight,main* | *kconv,turning,main* | 0 | *kconv,turning,main* |
| Converging to node D | >*ṁthresh* | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *kconv,turing,side* | *kconv,straight,side* | *kconv,turing,side* | 0 |
| Perpendicular with main entry A | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *kperp,turning in,main* | *kperp,straight,main* | *kperp,turning out,main* |
| Perpendicular with main entry B | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *kperp,turning out,side* | 0 | *kperp,turning in,side* | *kperp,turning straight,side* |
| Perpendicular with main entry C | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | *kperp,straight,main* | *kperp,turning out,main* | 0 | *kperp,turning in,main* |
| Perpendicular with main entry D | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kperp,turning in,side* | *kperp,turning straight,side* | *kperp,turning out,side* | 0 |
| Colliding from main to branch | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | 0 | *kcoll,turning,main* | *kcoll,straight,main* | *kcoll,turning,main* |
| Colliding from branch to main | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kcoll,turning,side* | 0 | *kcoll,turning,side* | *kcoll,straight,side* |
| Stagnant | – | – | – | – | 1 or last valid | 1 or last valid | 1 or last valid | 1 or last valid |

The flow is stagnant when the mass flow rate conditions do not match any defined flow
scenario. The block uses these parameters to calculate the flow coefficients:

- *kdiv,straight,main* and
  *kdiv,straight,side* are the first and
  second elements of the **Diverging flow straight loss coefficient**
  parameter, respectively.
- *kdiv,turning,main* and
  *kdiv,turning,side* are the first and
  second elements of the **Diverging flow turning loss coefficient**
  parameter, respectively.
- *kconv,straight,main* and
  *kconv,straight,side* are the first and
  second elements of the **Converging flow straight loss coefficient**
  parameter, respectively.
- *kconv,turning,main* and
  *kconv,turning,side* are the first and
  second elements of the **Converging flow turning loss coefficient**
  parameter, respectively.
- *kperp,straight,main* and
  *kperp,straight,side* are the first and
  second elements of the **Perpendicular flow straight loss
  coefficient** parameter, respectively.
- *kperp,turning in,main* and
  *kperp,turning in,side* are the first and
  second elements of the **Perpendicular flow straight loss
  coefficient** parameter, respectively.
- *kperp,turning out,main* and
  *kperp,turning out,side* are the first and
  second elements of the **Perpendicular flow straight loss
  coefficient** parameter, respectively.
- *kcoll,straight,main* and
  *kcoll,straight,side* are the first and
  second elements of the **Colliding flow straight loss coefficient**
  parameter, respectively.
- *kcoll,turning,main* and
  *kcoll,turning,side* are the first and
  second elements of the **Colliding flow turning loss coefficient**
  parameter, respectively.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
