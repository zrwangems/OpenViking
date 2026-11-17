---
type: simulink-block
title: 'Pipe (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'pipetl'
documentation_source_path: 'ref/pipetl.html'
language: en
---

# Pipe (TL)

## Ports
```yaml
ports:
- name: A
  summary: Inlet or outlet thermal liquid
  direction: conserving
- name: B
  summary: Inlet or outlet thermal liquid
  direction: conserving
- name: H
  summary: Temperature of pipe wall thermal
  direction: conserving
```

### Conserving

### **A** — Inlet or outlet thermal liquid

Thermal liquid conserving port associated with the inlet or outlet of the pipe.
This block has no intrinsic directionality.

### **B** — Inlet or outlet thermal liquid

Thermal liquid conserving port associated with the inlet or outlet of the pipe.
This block has no intrinsic directionality.

### **H** — Temperature of pipe wall thermal

Thermal conserving port associated with the temperature of the pipe wall. This
temperature may differ from the temperature of the thermal liquid inside the
pipe.
## Parameters
```yaml
parameters:
- name: Pipe length
  summary: The length of the pipe 5 m (default)
  group: Geometry
- name: Cross-sectional area
  summary: The internal area of the pipe 0.01 m^2 (default)
  group: Geometry
- name: Hydraulic diameter
  summary: Diameter of an equivalent cylindrical pipe with the same cross-sectional area 0.1128 m (default)
  group: Geometry
- name: Aggregate equivalent length of local resistances
  summary: The combined length of all local resistances present in the pipe 1 m (default)
  group: Friction and Heat Transfer
- name: Internal surface absolute roughness
  summary: Average depth of all surface defects on the internal surface of the pipe 15e-6 m (default)
  group: Friction and Heat Transfer
- name: Laminar flow upper Reynolds number limit
  summary: The Reynolds number above which flow begins to transition from laminar to turbulent 2000 (default)
  group: Friction and Heat Transfer
- name: Turbulent flow lower Reynolds number limit
  summary: The Reynolds number below which flow begins to transition from turbulent to laminar 4000 (default)
  group: Friction and Heat Transfer
- name: Shape factor for laminar flow viscous friction
  summary: Effect of pipe geometry on the viscous friction losses 64 (default)
  group: Friction and Heat Transfer
- name: Nusselt number for laminar flow heat transfer
  summary: Ratio of convective to conductive heat transfer 3.66 (default)
  group: Friction and Heat Transfer
- name: Enable dynamic compressibility
  summary: Select whether to model fluid dynamic compressibility On (default) | Off
  group: Effects and Initial Conditions
- name: Enable fluid inertia
  summary: Select whether to model fluid inertia Off (default) | On
  group: Effects and Initial Conditions
- name: Initial liquid pressure
  summary: Liquid pressure at time zero 0.101325 MPa (default)
  group: Effects and Initial Conditions
- name: Initial liquid temperature
  summary: Liquid temperature at time zero 293.15 K (default)
  group: Effects and Initial Conditions
- name: Nominal liquid pressure
  summary: Liquid pressure at nominal operating conditions 0.101325 MPa (default)
  group: Effects and Initial Conditions
- name: Nominal liquid temperature
  summary: Liquid temperature at nominal operating conditions 293.15 K (default)
  group: Effects and Initial Conditions
- name: Initial mass flow rate from port A to port B
  summary: Mass flow rate at time zero 0 kg/s (default)
  group: Effects and Initial Conditions
```

### Geometry

### **Pipe length** — The length of the pipe `5 m` (default)

The length of the pipe along the direction of flow.

### **Cross-sectional area** — The internal area of the pipe `0.01 m^2` (default)

The internal area of the pipe normal to the direction of the flow.

### **Hydraulic diameter** — Diameter of an equivalent cylindrical pipe with the same cross-sectional area `0.1128 m` (default)

Diameter of an equivalent cylindrical pipe with the same cross-sectional area.

### Friction and Heat Transfer

### **Aggregate equivalent length of local resistances** — The combined length of all local resistances present in the pipe `1 m` (default)

The combined length of all local resistances present in the pipe. Local
resistances include bends, fittings, armatures, and pipe inlets and outlets. The
effect of the local resistances is to increase the effective length of the pipe
segment. This length is added to the geometrical pipe length only for friction
calculations. The liquid volume inside the pipe depends only on the pipe geometrical
length, defined by the **Pipe length** parameter.

### **Internal surface absolute roughness** — Average depth of all surface defects on the internal surface of the pipe `15e-6 m` (default)

Average depth of all surface defects on the internal surface of the pipe, which
affects the pressure loss in the turbulent flow regime.

### **Laminar flow upper Reynolds number limit** — The Reynolds number above which flow begins to transition from laminar to turbulent `2000` (default)

The Reynolds number above which flow begins to transition from laminar to
turbulent. This number equals the maximum Reynolds number corresponding to fully
developed laminar flow.

### **Turbulent flow lower Reynolds number limit** — The Reynolds number below which flow begins to transition from turbulent to laminar `4000` (default)

The Reynolds number below which flow begins to transition from turbulent to
laminar. This number equals to the minimum Reynolds number corresponding to fully
developed turbulent flow.

### **Shape factor for laminar flow viscous friction** — Effect of pipe geometry on the viscous friction losses `64` (default)

Dimensionless factor that encodes the effect of pipe cross-sectional geometry on
the viscous friction losses in the laminar flow regime. Typical values are 64 for a
circular cross section, 57 for a square cross section, 62 for a rectangular cross
section with an aspect ratio of 2, and 96 for a thin annular cross section [1].

### **Nusselt number for laminar flow heat transfer** — Ratio of convective to conductive heat transfer `3.66` (default)

Ratio of convective to conductive heat transfer in the laminar flow regime. Its
value depends on the pipe cross-sectional geometry and pipe wall thermal boundary
conditions, such as constant temperature or constant heat flux. Typical value is 3.66,
for a circular cross section with constant wall temperature [2].

### Effects and Initial Conditions

### **Enable dynamic compressibility** — Select whether to model fluid dynamic compressibility `On` (default) | `Off`

Select whether to account for the dynamic compressibility of the liquid. Dynamic
compressibility gives the liquid density a dependence on pressure and temperature,
impacting the transient response of the system at small time scales.

### **Enable fluid inertia** — Select whether to model fluid inertia `Off` (default) | `On`

Select whether to account for the flow inertia of the liquid. Flow inertia gives
the liquid a resistance to changes in mass flow rate.

#### Dependencies

To enable this check box, select the **Enable dynamic
compressibility** check box.

### **Initial liquid pressure** — Liquid pressure at time zero `0.101325 MPa` (default)

Liquid pressure in the pipe at the start of simulation.

#### Dependencies

To enable this parameter, select the **Enable dynamic
compressibility** check box.

### **Initial liquid temperature** — Liquid temperature at time zero `293.15 K` (default)

Liquid temperature in the pipe at the start of simulation.

### **Nominal liquid pressure** — Liquid pressure at nominal operating conditions `0.101325 MPa` (default)

Thermal liquid pressure at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass and energy conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

### **Nominal liquid temperature** — Liquid temperature at nominal operating conditions `293.15 K` (default)

Thermal liquid temperature at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

### **Initial mass flow rate from port A to port B** — Mass flow rate at time zero `0 kg/s` (default)

Mass flow rate from port **A** to port **B** at
time zero.

#### Dependencies

To enable this parameter, select the **Enable fluid inertia**
check box.
## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Rigid conduit for fluid flow in thermal liquid systems

The Pipe (TL) block represents a pipeline segment with a
fixed volume of liquid. The liquid experiences pressure losses due to viscous friction and
heat transfer due to convection between the fluid and the pipe wall. Viscous friction follows
from the Darcy-Weisbach equation, while the heat exchange coefficient follows from Nusselt
number correlations.

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

m˙A+m˙B={0,if fluid dynamic compressibility is 'off'Vρ(1βdpdt−αdTdt),if fluid dynamic compressibility is 'on'

where:

- m˙A and m˙B are the mass flow rates through ports **A** and
  **B**.
- *V* is the pipe fluid volume.
- *ρ* is the thermal liquid density in the pipe.
- *β* is the isothermal bulk modulus in the pipe.
- *α* is the isobaric thermal expansion coefficient in the
  pipe.
- *p* is the thermal liquid pressure in the pipe.
- *T* is the thermal liquid temperature in the pipe.

### Momentum Balance

The table shows the momentum conservation equations for each half pipe.

|  |  |
| --- | --- |
| For half pipe adjacent to port **A** | pA−p={Δpv,A,if fluid inertia is offΔpv,A+L2Sm¨A,if fluid inertia is on |
| For half pipe adjacent to port **B** | pB−p={Δpv,B,if fluid inertia is offΔpv,B+L2Sm¨B,if fluid inertia is on |

In the equations:

- *S* is the pipe cross-sectional area.
- *p*, *p*A, and
  *p*B are the liquid pressures in the pipe, at
  port **A** and port **B**.
- *Δp*v,A and
  *Δp*v,B are the viscous friction pressure
  losses between the pipe volume center and ports **A** and
  **B**.

### Viscous Friction Pressure Losses

The table shows the viscous friction pressure loss equations for each half pipe.

|  |  |
| --- | --- |
| For half pipe adjacent to port **A** | Δpv,A={λν(L+Leq2)m˙A2D2S,if ReA<RelfA(L+Leq2)m˙A|m˙A|2ρDS2,if ReA≥Ret |
| For half pipe adjacent to port **B** | Δpv,B={λν(L+Leq2)m˙B2D2S,if ReB<RelfB(L+Leq2)m˙B|m˙B|2ρDS2,if ReB≥Ret |

In the equations:

- *λ* is the pipe shape factor.
- *ν* is the kinematic viscosity of the thermal liquid in the
  pipe.
- *L*eq is the aggregate equivalent length of
  the local pipe resistances.
- *D* is the hydraulic diameter of the pipe.
- *f*A and
  *f*B are the Darcy friction factors in the
  pipe halves adjacent to ports **A** and **B**.
- ReA and *Re*B are the
  Reynolds numbers at ports **A** and **B**.
- Rel is the Reynolds number above which the flow transitions
  to turbulent.
- Ret is the Reynolds number below which the flow transitions
  to laminar.

The Darcy friction factors follow from the Haaland approximation for the turbulent regime:

f=1[−1.8log10(6.9Re+(13.7rD)1.11)]2,

where:

- *f* is the Darcy friction factor.
- *r* is the pipe surface roughness.

### Energy Balance

The energy conservation equation for the pipe is

Vd(ρu)dt=ϕA+ϕB+QH,

where:

- *Φ*A and
  *Φ*B are the total energy flow rates into
  the pipe through ports **A** and **B**.
- *Q*H is the heat flow rate into the pipe
  through the pipe wall.

### Wall Heat Flow Rate

The heat flow rate between the thermal liquid and the pipe wall is:

QH=Qconv+kSHD(TH−T),

where:

- *Q*H is the net heat flow rate.
- *Q*conv is the portion of the heat flow
  rate attributed to convection at nonzero flow rates.
- *k* is the thermal conductivity of the thermal liquid in the
  pipe.
- *S*H is the surface area of the pipe wall,
  the product of the pipe perimeter and length.
- *T*H is the temperature at the pipe
  wall.

Assuming an exponential temperature distribution along the pipe, the convective heat
transfer is

Qconv=|m˙avg|cp,avg(TH−Tin)(1−exp(−hcoeffSH|m˙avg|cp,avg)),

where:

- m˙avg=(m˙A−m˙B)/2 is the average mass flow rate from port **A** to
  port **B**.
- cpavg is the specific heat evaluated at the average temperature.
- *T*in is the inlet temperature depending
  on flow direction.

The heat transfer coefficient, *h*coeff, depends
on the Nusselt number:

hcoeff=NukavgD,

where *k*avg, is the thermal conductivity
evaluated at the average temperature. The Nusselt number depends on the flow regime. The
Nusselt number in the laminar flow regime is constant and equal to the **Nusselt
number for laminar flow heat transfer** parameter value. The Nusselt number in
the turbulent flow regime is computed from the Gnielinski correlation:

Nutur=favg8(Reavg−1000)Pravg1+12.7favg8(Pravg2/3−1),

where *f*avg is the Darcy friction factor at the
average Reynolds number, *Re*avg, and
*Pr*avg is the Prandtl number evaluated at the
average temperature. The average Reynolds number is computed as:

Reavg=|m˙avg|DSμavg,

where *μ*avg is the dynamic viscosity evaluated
at the average temperature. When the average Reynolds number is between the
**Laminar flow upper Reynolds number limit** and the **Turbulent
flow lower Reynolds number limit** parameter values, the Nusselt number follows a
smooth transition between the laminar and turbulent Nusselt number values.

### Assumptions and Limitations

- The pipe wall is rigid.
- The flow is fully developed.
- The effect of gravity is negligible.
