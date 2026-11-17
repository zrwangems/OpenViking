---
type: simulink-block
title: 'Pipe (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'pipeil'
documentation_source_path: 'ref/pipeil.html'
language: en
---

# Pipe (IL)

## Ports
```yaml
ports:
- name: A
  summary: Inlet or outlet isothermal liquid
  direction: conserving
- name: B
  summary: Inlet or outlet isothermal liquid
  direction: conserving
```

### Conserving

### **A** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the pipe.
This block has no intrinsic directionality.

### **B** — Inlet or outlet isothermal liquid

Isothermal liquid conserving port associated with the inlet or outlet of the pipe.
This block has no intrinsic directionality.
## Parameters
```yaml
parameters:
- name: Pipe length
  summary: The length of the pipe 5 m (default) | positive scalar
  group: Geometry
- name: Cross-sectional area
  summary: The internal area of the pipe 0.01 m^2 (default) | positive scalar
  group: Geometry
- name: Hydraulic diameter
  summary: Diameter of an equivalent cylindrical pipe with the same cross-sectional area 0.1128 m (default) | positive scalar
  group: Geometry
- name: Aggregate equivalent length of local resistances
  summary: The combined length of all local resistances present in the pipe 1 m (default) | positive scalar
  group: Friction
- name: Internal surface absolute roughness
  summary: Average depth of all surface defects on the internal surface of the pipe 15e-6 m (default) | positive scalar
  group: Friction
- name: Laminar flow upper Reynolds number limit
  summary: The Reynolds number above which flow begins to transition from laminar to turbulent 2000 (default) | scalar greater
    than 1
  group: Friction
- name: Turbulent flow lower Reynolds number limit
  summary: The Reynolds number below which flow begins to transition from turbulent to laminar 4000 (default) | scalar greater
    than Laminar flow upper Reynolds number limit value
  group: Friction
- name: Laminar friction constant for Darcy friction factor
  summary: Effect of pipe geometry on the viscous friction losses 64 (default) | positive scalar
  group: Friction
- name: Enable dynamic compressibility
  summary: Select whether to model fluid dynamic compressibility On (default) | Off
  group: Effects and Initial Conditions
- name: Enable fluid inertia
  summary: Select whether to model fluid inertia Off (default) | On
  group: Effects and Initial Conditions
- name: Initial liquid pressure
  summary: Liquid pressure at time zero 0.101325 MPa (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial mass flow rate from port A to port B
  summary: Mass flow rate at time zero 0 kg/s (default) | scalar
  group: Effects and Initial Conditions
```

### Geometry

### **Pipe length** — The length of the pipe `5 m` (default) | positive scalar

The length of the pipe along the direction of flow.

### **Cross-sectional area** — The internal area of the pipe `0.01 m^2` (default) | positive scalar

The internal area of the pipe normal to the direction of the flow.

### **Hydraulic diameter** — Diameter of an equivalent cylindrical pipe with the same cross-sectional area `0.1128 m` (default) | positive scalar

Diameter of an equivalent cylindrical pipe with the same cross-sectional area.

### Friction

### **Aggregate equivalent length of local resistances** — The combined length of all local resistances present in the pipe `1 m` (default) | positive scalar

The combined length of all local resistances present in the pipe. Local
resistances include bends, fittings, armatures, and pipe inlets and outlets. The
effect of the local resistances is to increase the effective length of the pipe
segment. This length is added to the geometrical pipe length only for friction
calculations. The liquid volume inside the pipe depends only on the pipe geometrical
length, defined by the **Pipe length** parameter.

### **Internal surface absolute roughness** — Average depth of all surface defects on the internal surface of the pipe `15e-6 m` (default) | positive scalar

Average depth of all surface defects on the internal surface of the pipe, which
affects the pressure loss in the turbulent flow regime.

### **Laminar flow upper Reynolds number limit** — The Reynolds number above which flow begins to transition from laminar to turbulent `2000` (default) | scalar greater than 1

The Reynolds number above which flow begins to transition from laminar to
turbulent. This number equals the maximum Reynolds number corresponding to fully
developed laminar flow.

### **Turbulent flow lower Reynolds number limit** — The Reynolds number below which flow begins to transition from turbulent to laminar `4000` (default) | scalar greater than **Laminar flow upper Reynolds number limit** value

The Reynolds number below which flow begins to transition from turbulent to
laminar. This number equals to the minimum Reynolds number corresponding to fully
developed turbulent flow.

### **Laminar friction constant for Darcy friction factor** — Effect of pipe geometry on the viscous friction losses `64` (default) | positive scalar

Dimensionless factor that encodes the effect of pipe cross-sectional geometry on
the viscous friction losses in the laminar flow regime. Typical values are 64 for a
circular cross section, 57 for a square cross section, 62 for a rectangular cross
section with an aspect ratio of 2, and 96 for a thin annular cross section [1].

### Effects and Initial Conditions

### **Enable dynamic compressibility** — Select whether to model fluid dynamic compressibility `On` (default) | `Off`

Select whether to account for the dynamic compressibility of the liquid. Dynamic
compressibility gives the liquid density a dependence on pressure, impacting the
transient response of the system at small time scales.

### **Enable fluid inertia** — Select whether to model fluid inertia `Off` (default) | `On`

Select whether to account for the flow inertia of the liquid. Flow inertia gives
the liquid a resistance to changes in mass flow rate.

#### Dependencies

To enable this check box, select the **Enable dynamic
compressibility** check box.

### **Initial liquid pressure** — Liquid pressure at time zero `0.101325 MPa` (default) | positive scalar

Liquid pressure in the pipe at the start of simulation.

#### Dependencies

To enable this parameter, select the **Enable dynamic
compressibility** check box.

### **Initial mass flow rate from port A to port B** — Mass flow rate at time zero `0 kg/s` (default) | scalar

Mass flow rate from port **A** to port **B** at
time zero.

#### Dependencies

To enable this parameter, select the **Enable fluid inertia**
check box.
## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Rigid conduit for fluid flow in isothermal liquid systems

The Pipe (IL) block models pipe flow dynamics in an
isothermal liquid network. The block accounts for viscous friction losses, and can also
account for dynamic compressibility and fluid inertia.

The pipe contains a constant volume of liquid. The liquid experiences pressure losses due
to viscous friction, following the Darcy-Weisbach equation.

### Pipe Effects

The block lets you include dynamic compressibility and fluid inertia effects. Turning on
each of these effects can improve model fidelity at the cost of increased equation
complexity and potentially increased simulation cost:

- When dynamic compressibility is off, the liquid is assumed to spend negligible time
  in the pipe volume. Therefore, there is no accumulation of mass in the pipe, and mass
  inflow equals mass outflow. This is the simplest option. It is appropriate when the
  liquid mass in the pipe is a negligible fraction of the total liquid mass in the
  system.
- When dynamic compressibility is on, an imbalance of mass inflow and mass outflow can
  cause liquid to accumulate or diminish in the pipe. As a result, pressure in the pipe
  volume can rise and fall dynamically, which provides some compliance to the system and
  modulates rapid pressure changes. This is the default option.
- If dynamic compressibility is on, you can also turn on fluid inertia. This effect
  results in additional flow resistance, besides the resistance due to friction. This
  additional resistance is proportional to the rate of change of mass flow rate.
  Accounting for fluid inertia slows down rapid changes in flow rate but can also cause
  the flow rate to overshoot and oscillate. This option is appropriate in a very long
  pipe. Turn on fluid inertia and connect multiple pipe segments in series to model the
  propagation of pressure waves along the pipe, such as in the water hammer
  phenomenon.

### Mass Balance

The mass conservation equation for the pipe is

m˙A+m˙B={0,if fluid dynamic compressibility is offp˙IβIρIV,if fluid dynamic compressibility is on

where:

- m˙A and m˙B are the mass flow rates through ports **A** and
  **B**.
- *V* is the pipe fluid volume.
- *p*I is the pressure inside the
  pipe.
- *ρ*I is the fluid density inside the
  pipe.
- *β*I is the fluid bulk modulus inside the
  pipe.

The fluid can be a mixture of pure liquid and a small amount of entrained air, as
specified by the Isothermal Liquid Properties (IL) block
connected to the circuit. Equations used to compute
*ρ*I and
*β*I, as well as port densities
*ρ*A and
*ρ*B in the viscous friction pressure loss
equations for each half pipe, depend on the selected isothermal liquid model. For detailed
information, see Isothermal Liquid Modeling Options.

### Momentum Balance

The table shows the momentum conservation equations for each half pipe.

|  |  |
| --- | --- |
| For half pipe adjacent to port **A** | pA−pI={Δpv,A,if fluid inertia is offΔpv,A+L2Sm¨A,if fluid inertia is on |
| For half pipe adjacent to port **B** | pB−pI={Δpv,B,if fluid inertia is offΔpv,B+L2Sm¨B,if fluid inertia is on |

In the equations:

- *p*, *p*A, and
  *p*B are the liquid pressures at port
  **A** and port **B**, respectively.
- *Δp*v,A and
  *Δp*v,B are the viscous friction pressure
  losses between the pipe volume center and ports **A** and
  **B**.
- *L* is the pipe length.
- *S* is the pipe cross-sectional area.

### Viscous Friction Pressure Losses

The table shows the viscous friction pressure loss equations for each half pipe.

|  |  |
| --- | --- |
| For half pipe adjacent to port **A** | Δpv,A={λμ(L+Leq2)m˙A2ρIDh2S,if ReA<RelamfA(L+Leq2)m˙A|m˙A|2ρIDhS2,if ReA>Retur |
| For half pipe adjacent to port **B** | Δpv,B={λμ(L+Leq2)m˙B2ρIDh2S,if ReB<RelamfB(L+Leq2)m˙B|m˙B|2ρIDhS2,if ReB≥Retur |

In the equations:

- *λ* is the pipe shape factor, used to calculate the Darcy friction
  factor in the laminar regime.
- *μ* is the dynamic viscosity of the liquid in the pipe.
- *L*eq is the aggregate equivalent length of
  the local pipe resistances.
- *D*h is the hydraulic diameter of the
  pipe.
- *f*A and
  *f*B are the Darcy friction factors in the
  pipe halves adjacent to ports **A** and **B**.
- *Re*A and
  *Re*B are the Reynolds numbers at ports
  **A** and **B**.
- *Re*lam is the Reynolds number above which
  the flow transitions to turbulent.
- *Re*tur is the Reynolds number below which
  the flow transitions to laminar.

When the Reynolds number is between *Re*lam and
*Re*tur, the flow is in transition between laminar
flow and turbulent flow. The pressure losses due to viscous friction during the transition
region follow a smooth connection between those in the laminar flow regime and those in the
turbulent flow regime.

The block computes the Reynolds numbers at ports **A** and
**B** based on the mass flow rate through the appropriate port:

Re=|m˙|DhμS.

The Darcy friction factors follow from the Haaland approximation for the turbulent regime:

f=1(−1.8log10(6.9Re+(13.7rDh)1.11))2,

where:

- *f* is the Darcy friction factor.
- *r* is the pipe surface roughness.

### Assumptions and Limitations

- The pipe wall is rigid.
- The flow is fully developed.
- The effect of gravity is negligible.
