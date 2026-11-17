---
type: simulink-block
title: 'FEM-Parameterized Induction Machine (Squirrel Cage)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'femparameterizedinductionmachinesquirrelcage'
documentation_source_path: 'ref/femparameterizedinductionmachinesquirrelcage.html'
language: en
---

# FEM-Parameterized Induction Machine (Squirrel Cage)

## Ports
```yaml
ports:
- name: ~1
  summary: Stator positive-end connections electrical
  direction: conserving
- name: ~2
  summary: Stator negative-end connections electrical
  direction: conserving
- name: R
  summary: Machine rotor mechanical rotational
  direction: conserving
- name: C
  summary: Machine case mechanical rotational
  direction: conserving
- name: HA
  summary: '*a*-phase terminal thermal'
  direction: conserving
- name: HB
  summary: '*b*-phase terminal thermal'
  direction: conserving
- name: HC
  summary: '*c*-phase terminal thermal'
  direction: conserving
- name: HR
  summary: Rotor thermal
  direction: conserving
```

### Conserving

### **~1** — Stator positive-end connections electrical

Composite three-phase port associated with the stator positive-end connections. For more
information about three-phase ports, see Three-Phase Ports.

### **~2** — Stator negative-end connections electrical

Composite three-phase port associated with the stator negative-end connections.

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine case.

### **HA** — *a*-phase terminal thermal

Thermal conserving port associated with the *a*-phase
terminal.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB** — *b*-phase terminal thermal

Thermal conserving port associated with the *b*-phase
terminal.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HC** — *c*-phase terminal thermal

Thermal conserving port associated with the *c*-phase
terminal.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Option to enable thermal ports No thermal port (default) | Show thermal port
  group: ''
- name: Stator resistance, Rs
  summary: Stator resistance 0.25 Ohm (default) | positive scalar
  group: Resistance
- name: Tabulate rotor resistance with frequency
  summary: Option to tabulate rotor resistance with frequency Off (default) | On
  group: Resistance
- name: Referred rotor resistance, Rr_d
  summary: Referred rotor resistance 0.14 Ohm (default) | positive scalar
  group: Resistance
- name: Rotor AC frequency vector, fr
  summary: Rotor AC frequency vector [0, 5, 10, 15] Hz (default) | vector of nonnegative scalars
  group: Resistance
- name: Referred rotor resistance table, Rr_d(fr)
  summary: Referred rotor resistance table [.14, .14, .14, .14] Ohm (default) | vector of positive scalars
  group: Resistance
- name: Number of pole pairs
  summary: Machine pole pairs 1 (default) | positive integer
  group: Flux
- name: Stator d-axis current vector, iDS
  summary: Stator D-axis current vector [0, 150, 350, 500] A (default) | vector of nonnegative scalars
  group: Flux
- name: Stator q-axis current vector, iQS
  summary: Stator Q-axis current vector [0, 250, 500] A (default) | vector of nonnegative scalars
  group: Flux
- name: Stator d-axis flux linkage table, λds(ids,iqs)
  summary: Stator D-axis flux linkage table 4.4e-2 * repmat([0, 150, 350, 500]', 1, 3) Wb (default) | matrix of scalars
  group: Flux
- name: Stator q-axis flux linkage table, λqs(ids,iqs)
  summary: Stator Q-axis flux linkage table 2.1e-3 * repmat([0, 250, 500], 4, 1) Wb (default) | matrix of scalars
  group: Flux
- name: Interpolation method
  summary: Interpolation method Linear (default) | Smooth
  group: Flux
- name: Include rotor inertia
  summary: Option to include rotor inertia On (default) | Off
  group: Mechanical
- name: Rotor inertia
  summary: Rotor inertia 1e-3 kg*m^2 (default) | positive scalar
  group: Mechanical
- name: Rotor damping
  summary: Rotor damping 0 N*m*s/rad (default) | nonnegative scalar
  group: Mechanical
- name: Measurement temperature
  summary: Rated temperature 298.15 K (default) | real scalar
  group: Temperature Dependence
- name: Stator resistance temperature coefficient
  summary: Stator resistance temperature coefficient 3.93e-3 1/K (default) | nonnegative scalar
  group: Temperature Dependence
- name: Rotor resistance temperature coefficient
  summary: Rotor resistance temperature coefficient 3.93e-3 1/K (default) | nonnegative scalar
  group: Temperature Dependence
- name: Include stator and rotor thermal masses
  summary: Option to include stator and rotor thermal masses On (default) | Off
  group: Thermal Port
- name: Thermal mass for each stator winding
  summary: Winding thermal mass 100 J/K (default) | positive scalar
  group: Thermal Port
- name: Rotor thermal mass
  summary: Rotor thermal mass 200 J/K (default) | positive scalar
  group: Thermal Port
```

### **Modeling option** — Option to enable thermal ports `No thermal port` (default) | `Show thermal port`

Option to enable the thermal ports of the block and model the effects of generated
heat and machine temperature.

### Resistance

### **Stator resistance, Rs** — Stator resistance `0.25` `Ohm` (default) | positive scalar

Stator resistance.

### **Tabulate rotor resistance with frequency** — Option to tabulate rotor resistance with frequency `Off` (default) | `On`

Option to tabulate the rotor resistance with the frequency.

Clear this parameter to specify a constant rotor resistance at the
rated temperature.

Select this parameter to specify resistance as a function of frequency
at the rated temperature.

### **Referred rotor resistance, Rr\_d** — Referred rotor resistance `0.14` `Ohm` (default) | positive scalar

Rotor resistance referred to the stator.

#### Dependencies

To enable this parameter, clear the **Tabulate rotor
resistance with frequency** parameter.

### **Rotor AC frequency vector, fr** — Rotor AC frequency vector `[0, 5, 10, 15]` `Hz` (default) | vector of nonnegative scalars

Rotor AC frequency vector.

#### Dependencies

To enable this parameter, select the **Tabulate rotor
resistance with frequency** parameter.

### **Referred rotor resistance table, Rr\_d(fr)** — Referred rotor resistance table `[.14, .14, .14, .14]` `Ohm` (default) | vector of positive scalars

Table of rotor resistance referred to the stator as a function of the rotor AC frequency
vector.

#### Dependencies

To enable this parameter, select the **Tabulate rotor
resistance with frequency** parameter.

### Flux

### **Number of pole pairs** — Machine pole pairs `1` (default) | positive integer

Number of machine pole pairs.

### **Stator d-axis current vector, iDS** — Stator D-axis current vector `[0, 150, 350, 500]` `A` (default) | vector of nonnegative scalars

Stator *D*-axis current vector.

### **Stator q-axis current vector, iQS** — Stator Q-axis current vector `[0, 250, 500]` `A` (default) | vector of nonnegative scalars

Stator *Q*-axis current vector.

### **Stator d-axis flux linkage table, λds(ids,iqs)** — Stator D-axis flux linkage table `4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)` `Wb` (default) | matrix of scalars

Stator *D*-axis flux linkage table.

The default value corresponds to linear flux. Using linear flux is
equivalent to the modeling approach of the Induction Machine Squirrel
Cage block.

### **Stator q-axis flux linkage table, λqs(ids,iqs)** — Stator Q-axis flux linkage table `2.1e-3 * repmat([0, 250, 500], 4, 1)` `Wb` (default) | matrix of scalars

Stator *Q*-axis flux linkage table.

The default value corresponds to linear flux. Using linear flux is
equivalent to the modeling approach of the Induction Machine Squirrel
Cage block.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Interpolation method for approximating the output value when the input value is between
grid points:

- `Linear` — Use an extension of
  the linear algorithm for multidimensional interpolation. Select
  this option to get the best performance.
- `Smooth` — Use a modified
  Akima interpolation algorithm. Select this option to produce a
  continuous surface with continuous first-order
  derivatives.

For more information about interpolation methods, see `tablelookup`.

### Mechanical

### **Include rotor inertia** — Option to include rotor inertia `On` (default) | `Off`

Option to include rotor inertia.

### **Rotor inertia** — Rotor inertia `1e-3` `kg*m^2` (default) | positive scalar

Rotor inertia.

#### Dependencies

To enable this parameter, select the **Include rotor
inertia** parameter.

### **Rotor damping** — Rotor damping `0` `N*m*s/rad` (default) | nonnegative scalar

Rotor damping.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Rated temperature `298.15` `K` (default) | real scalar

Temperature at which you quote the motor parameters.

### **Stator resistance temperature coefficient** — Stator resistance temperature coefficient `3.93e-3` `1/K` (default) | nonnegative scalar

Coefficient α in the equation relating resistance to temperature for all three stator
windings. For more information, see Thermal Model for Actuator Blocks. The default value is for
copper.

### **Rotor resistance temperature coefficient** — Rotor resistance temperature coefficient `3.93e-3` `1/K` (default) | nonnegative scalar

Coefficient α in the equation relating resistance to temperature for the rotor. For more
information, see Thermal Model for Actuator Blocks. The default value is for
copper.

### Thermal Port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Include stator and rotor thermal masses** — Option to include stator and rotor thermal masses `On` (default) | `Off`

Option to include stator and rotor thermal masses.

### **Thermal mass for each stator winding** — Winding thermal mass `100` `J/K` (default) | positive scalar

Thermal mass value for each stator winding. The thermal mass is the
energy required to raise the temperature by one degree.

#### Dependencies

To enable this parameter, select the **Include stator and
rotor thermal masses** parameter.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default) | positive scalar

Thermal mass of the rotor. The thermal mass is the energy required to
raise the temperature of the rotor by one degree.

#### Dependencies

To enable this parameter, select the **Include stator and
rotor thermal masses** parameter.
## Libraries

Simscape / Electrical / Electromechanical / Asynchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Squirrel-cage-rotor induction machine defined in terms of magnetic flux linkage

The FEM-Parameterized Induction Machine (Squirrel Cage) block models a squirrel-cage-rotor
induction machine using magnetic flux linkage tables.

You can generate the magnetic flux linkage tables with a finite element tool such as ANSYS
Motor-CAD software.

You can access all the stator connections on the block. Therefore, you can model soft-start
regimes using a switch between wye and delta configurations.

Connect port **~1** to a three-phase circuit. To connect the
stator in delta configuration, connect a Phase Permute block between ports **~1** and **~2**. To connect the stator in wye
configuration, connect port **~2** to a Grounded Neutral (Three-Phase) or Floating Neutral (Three-Phase) block.

### Equations

A three-phase induction machine consists of an iron stator lamination with three copper
windings and a rotor with copper bars. In a squirrel-cage machine, the copper bars
are shorted together.

When a three-phase AC supply feeds the stator, the current produces a rotating magnetic
field. This rotating field induces currents in the rotor copper bars, which produce
a magnetic field in the rotor. The interaction between these magnetic fields and the
currents produces a torque in the rotor, which starts its motion.

The induction machine equations are expressed in a synchronous reference frame orientated
with the rotor field (SRFORF). This frame is synchronous with the stator and rotor
magnetic fields, and the *D*-axis is aligned with the rotor field
*D*-axis. The rotor magnetic flux linkage vector only has a
*D*-axis component in this frame. The
*Q*-axis component is zero.

λ′qr=0.

- λs→ is the stator magnetic field vector.
- λr→ is the rotor magnetic field vector.
- is→ is the stator current vector.

All of these vectors rotate at the synchronous speed
*ωe*. The synchronous angle
*θe* tracks the orientation of the
stator current vector.

The rotor current vector rotates at a speed given by this equation:

ωslip=ωe−Nppωr,

where *ωr* is the rotor mechanical speed
and *Npp* is the **Number of pole
pairs** parameter.

To express the stator *a*-, *b*-, and
*c*-phase voltages and currents in the SRFORF reference frame,
you can use the Park transform:

Ps=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5],

where *θe* is the time integral of the synchronous
speed:

θe=∫ωe dt.

You can then compute the *D*-axis and *Q*-axis
components of stator voltages and currents using these equations.

isdq0=Ps⋅isabcvsdq0=Ps⋅vsabc

The rotor *a*-, *b*-, and *c*-phase
voltages and currents do not rotate at the synchronous speed due to slip. Rotor
currents rotate at the slip speed
*ωslip*.

To express rotor DQ currents in the stationary frame (*a*,
*b*, and *c* phases) you can use the Park
transform:

Pr=2/3[cosθercos(θer−2π/3)cos(θer+2π/3)−sinθer−sin(θer−2π/3)−sin(θer+2π/3)0.50.50.5],

where *θer* is the rotor slip angle, equal to the
time integral of the slip speed:

θer=∫ωslip dt.

Then, you can compute the *a*, *b*, and
*c* components of rotor voltages and currents using these
equations.

irabc=Pr−1⋅irdq0vrabc=Pr−1⋅vrdq0

In the SRFORF reference frame, the stator and rotor currents, voltages, and fluxes are
related to these fundamental induction machine equations:

- Stator voltage equations

  vds=Rsids−ωeλqs+dλdsdtvqs=Rsiqs+ωeλds+dλqsdt
- Rotor voltage equations

  v′dr=R′ri′dr+dλ′drdtv′qr=R′ri′qr+ωslipλ′dr

  Use the latter rotor voltage equation to compute the slip speed, which
  you can then use to compute the synchronous speed for the reference
  frame transformations.

  ωslip  =  v′qr−R′ri′qrλ′dr.
- Squirrel cage equations: shorted rotor cage

  v′dr=0v′qr=0
- Flux-current relationships

  The magnetizing *D*-axis current is defined
  as

  id =  ids+  i′dr,

  and the flux-current relationships are

  λ′dr=λds−Ltidsλ′qr=λqs−Ltiqs

  where:

  - *λds* is the
    interpolated value of the **Stator d-axis flux
    linkage table, λds(ids,iqs)**  parameter
    computed for the particular combination of
    *id* and
    *iqs*.
  - *λqs* is the
    interpolated value of the **Stator q-axis flux
    linkage table, λqs(ids,iqs)**  parameter
    computed for the particular combination of
    *id* and
    *iqs*.
  - *Lt* is the
    interpolated value of the transient inductance computed from
    the magnetic flux linkage tables.

  An alternative form of the rotor flux-current relationships uses the
  *Lϕ* inductance

  λ′dr=Lϕidλ′qr=Lϕiq

  where *Lϕ* is the interpolated
  value of the magnetizing inductance table computed from the flux linkage
  tables.

  When you combine the latter equation for the
  *Q*-axis rotor flux with λ′qr=0 you obtain iq=0, which means that the referred rotor
  *Q*-axis current is equal and opposite to the
  stator *Q*-axis current:

  i′qr=−iqs.

  *Lϕ* is defined by this
  equation.

  Lϕ=Ls−Lt,

  where *Lt* is the transient
  inductance is defined as

  Lt=Ls−Lm2L′r.

  In these equations *Ls*,
  *Lm*, and L′r are the stator inductance, the magnetizing inductance,
  and the referred rotor inductance respectively. These equations relate
  these inductances:

  Ls=Lls+LmL′r=L′lr+Lm

  where *Lls* and L′lr are the stator leakage inductance and the referred
  rotor leakage inductance, respectively.
- Torque equation

  T=32Npp(λdsiqs−λqsids).

### Model Thermal Effects

You can expose thermal ports to simulate the effects of generated heat and motor
temperature. To expose the thermal ports and enable the **Temperature
Dependence** and **Thermal Port** parameters, set the
**Modeling option** parameter to one of these options:

- `No thermal port` — The block contains
  electrical conserving ports associated with the stator windings, but
  does not contain thermal ports.
- `Show thermal port` — The block contains
  expanded electrical conserving ports associated with the stator windings
  and thermal conserving ports for each of the windings and for the
  rotor.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
