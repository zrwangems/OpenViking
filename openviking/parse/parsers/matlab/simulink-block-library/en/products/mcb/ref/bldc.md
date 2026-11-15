---
type: simulink-block
title: 'BLDC'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'bldc'
documentation_source_path: 'ref/bldc.html'
language: en
---

# BLDC

## Ports

### Input

### **LdTrq** — Load torque on motor `scalar`

Load torque on the motor shaft, *Tm*, in
N·m.

#### Dependencies

To enable this port, set the **Mechanical input configuration**
parameter to `Torque`.

### **Spd** — Motor shaft speed `scalar`

Angular velocity of the motor, *ωm*, in
rad/s.

#### Dependencies

To enable this port, set the **Mechanical input configuration**
parameter to `Speed`.

### **PhaseVolt** — Stator terminal voltages `1`-by-`3` array

Stator terminal voltages, *Va*,
*Vb*, and
*Vc*, in V.
### Output

### **Info** — Bus signal bus

The bus signal contains these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | Stator phase current A | *ia* | A |
| `IbStator` | | | Stator phase current B | *ib* | A |
| `IcStator` | | | Stator phase current C | *ic* | A |
| `IdSync` | | | *d'* axis current | *id'* | A |
| `IqSync` | | | *q'* axis current | *iq'* | A |
| `VdSync` | | | *d'* axis voltage | *vd'* | V |
| `VqSync` | | | *q'* axis voltage | *vq'* | V |
| `MtrSpd` | | | Angular mechanical velocity of the motor | *ωm* | rad/s |
| `MtrPos` | | | Motor mechanical angular position | *θm* | rad |
| `MtrTrq` | | | Electromagnetic torque | *Te* | N·m |
| `MtrHall` | | | Hall sensor output | - | - |
| `BackEMF` | | | Back EMF generated in motor | *Ea*, *Eb*, *Ec* | V/m/s |

### **PhaseCurr** — Phase a, b, c current 1-by-3 array

Phase a, b, c current, *ia*,
*ib*, and
*ic*, in A.

### **MtrTrq** — Motor torque scalar

Motor torque, *Tmtr*, in N·m.

#### Dependencies

To enable this port, set the **Mechanical input configuration**
parameter to `Speed`.

### **MtrSpd** — Motor speed scalar

Angular speed of the motor, *ωmtr*, in
rad/s.

#### Dependencies

To enable this port, set the **Mechanical input configuration**
parameter to `Torque`.

## Parameters

### Block Options

### **Mechanical input configuration** — Select port configuration `Torque` (default) | `Speed`

This table summarizes the port configurations.

| Port Configuration | Creates Input Port | Creates Output Port |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **Values:** | `Torque` (default) | `Speed` |
| **Data Types:** | `character vector` |

### **Simulation type** — Select simulation type `Continuous` (default) | `Discrete`

By default, the block uses a continuous sample
time during simulation. If you want to generate code for single-precision targets, set
the parameter to `Discrete`.

### **Sample time (s)** — Sample time for discrete integration `25e-6` (default) | `scalar`

Integration sample time for discrete simulation,
in s.

#### Dependencies

To enable this parameter, set **Simulation type** to
`Discrete`.

### Parameters

### **Number of pole pairs** — Pole pairs of motor `4` (default) | `scalar`

Motor pole pairs, *P*.

### **Stator resistance per phase (Ohm)** — Stator resistance in each phase `0.36` (default) | `scalar`

Stator resistance per phase, *Rs*, in
ohms.

### **Stator d-axis inductance (H)** — Stator inductance across d-axis `2e-4` (default) | `scalar`

Stator inductance across *d*-axis,
*Ld*, in H.

### **Stator q-axis inductance (H)** — Stator inductance across q-axis `2e-4` (default) | `scalar`

Stator inductance across *q*-axis,
*Lq*, in H.

### **Permanent flux linkage constant (Wb)** — Flux-linkage constant `0.0064` (default) | `scalar`

Permanent flux linkage constant, *λpm*, in
Wb.

### **Inertia (kgm^2)** — Rotor inertia `7.0616e-06` (default) | `scalar`

Rotor inertia, *J*, in kg.m^2.

### **Viscous damping (Nm/rad/s)** — Viscous damping `2.6369e-06` (default) | `scalar`

Viscous damping, *F*, in N·m/(rad/s).

### **Static friction (Nm)** — Static friction `0` (default) | `scalar`

Static friction, *Tf*, in N·m.

### Initial Values

### **Initial d-axis current (A)** — Initial current across *d'*-axis `0` (default) | `scalar`

Initial d-axis current, *id'*, in
A.

### **Initial q-axis current (A)** — Initial current across *q'*-axis `0` (default) | `scalar`

Initial q-axis current, *iq'*, in
A.

### **Initial rotor mechanical position (rad)** — Initial mechanical position of rotor `0` (default) | `scalar`

Initial angular position of motor, *θm0*,
in rad.

### **Initial rotor mechanical speed (rad/s)** — Initial mechanical speed of rotor `0` (default) | `scalar`

Initial angular velocity of the motor,
*ωm0*, in rad/s.

#### Dependencies

To enable this parameter, set **Mechanical input
configuration** to `Torque`.

## Libraries

Motor Control Blockset / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Three-phase brushless DC motor with trapezoidal flux distribution

The BLDC block implements a three-phase brushless DC (BLDC) motor with a
trapezoidal back electromotive force that remains constant for a position range of 120
electrical degrees. The block uses the three-phase input voltages to regulate the individual
phase currents, allowing control of the motor torque or speed.

By default, the block sets the **Simulation
type** parameter to `Continuous` to use a continuous
sample time during simulation. If you want to use the block for fixed-step simulation, set the
parameter to `Discrete`. Then specify a **Sample time
(s)** parameter.

### Motor Construction

This figure shows a motor with a single pole pair.

The motor magnetic field due to the permanent magnets creates a trapezoidal rate of
change of flux with the motor angle.

For the axes convention, the *a*-phase and permanent magnet fluxes
align when the motor angle *θr* is zero.

### Three-Phase Sinusoidal Model Electrical System

Instead of the standard *dq* reference frame, the block uses
*d’q’* reference frame, which is defined by these transformation
equations.

vd'=23((va−Ria−Ea)cosθe+(vb−Rib−Eb)cos(θe−2π3)+(vc−Ric−Ec)cos(θe+2π3))

vq'=−2π3((va−Ria−Ea)sinθe+(vb−Rib−Eb)sin(θe−2π3)+(vc−Ric−Ec)sin(θe+2π3))

Ea=Pωm∂ψa∂θeEb=Pωm∂ψb∂θeEc=Pωm∂ψc∂θe

ia=id'cosθe−iq'sinθeib=id'cos(θe−2π3)−iq'sin(θe−2π3)ic=id'cos(θe+2π3)−iq'sin(θe+2π3)

The block implements these equations, expressed in the *dq* and
*d’q’* reference frame of the BLDC motor. All quantities in the motor
reference frame are with respect to the stator phase A.

ωe=Pωmddtid'=1Ldvd'+LqLdPωmiq'

ddtiq'=1Lqvq'−LdLqPωmid'

Te=1.5P((Ld−Lq)id'iq')+P(∂ψa∂θeia+∂ψb∂θeib+∂ψc∂θeic)

This table describes the variables used in these equations.

|  |  |
| --- | --- |
| *Lq*,*Ld* | q- and d-axis inductances (H) |
| *R* | Resistance of the stator windings (ohm) |
| *iq'*,*id'* | *q'*- and *d'*-axis currents (A) |
| *vq'*, *vd'* | *q'*- and *d'*-axis voltages (V) |
| *ωm* | Angular mechanical velocity of the motor (rad/s) |
| *ωe* | Angular electrical velocity of the motor (rad/s) |
| *P* | Number of pole pairs |
| *Te* | Electromagnetic torque (Nm) |
| *Θe* | Electrical angle (rad) |
| *Va*, *Vb*, *Vc* | Stator phase A, B, and C voltages (V) |
| *ia*, *ib*, *ic* | Stator phase A, B, and C currents (A) |
| *Ea*, *Eb*, *Ec* | Back EMF of stator phases A, B, and C (V/m/s) |
| *Ψa*, *Ψb*, *Ψc* | Total fluxes linking each stator winding (Wb) |

### Mechanical System

The motor angular velocity is given by:

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

The equations use these variables.

|  |  |
| --- | --- |
| *J* | Combined inertia of motor and load (kgm^2) |
| *F* | Combined viscous friction of motor and load (N·m/(rad/s)) |
| *θm* | Motor mechanical angular position (rad) |
| *Tm* | Motor shaft torque (Nm) |
| *Te* | Electromagnetic torque (Nm) |
| *Tf* | Motor shaft static friction torque (Nm) |
| *ωm* | Angular mechanical velocity of the motor (rad/s) |

### Amplitude Invariant *dq* Transformation

The block uses these equations to implement amplitude invariant *dq*
transformation to ensure that the *dq* and three phase amplitudes are
equal.

[vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]

[iaibic]=   [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq]

The equations use these variables.

|  |  |
| --- | --- |
| *Θda* | *dq* stator electrical angle with respect to the rotor *a*-axis (rad) |
| *vsq*, *vsd* | Stator *q*- and *d*-axis voltages (V) |
| *isq*,*isd* | Stator *q*- and *d*-axis currents (A) |
| *va*,*vb*,*vc* | Stator voltage phases *a*, *b*, *c* (V) |
| *ia*, *ib*, *ic* | Stator currents phases *a*, *b*, *c* (A) |

### Trapezoidal Rate of Change of Flux

The rotor magnetic field due to the permanent magnets create a trapezoidal rate of
change of flux with the rotor angle. This figure shows the rate of change of flux for the
three phases of a three-phase BLDC motor.
