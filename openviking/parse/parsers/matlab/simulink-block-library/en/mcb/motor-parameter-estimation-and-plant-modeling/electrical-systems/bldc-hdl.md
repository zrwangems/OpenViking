---
type: simulink-block
title: 'BLDC HDL'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'bldchdl'
documentation_source_path: 'ref/bldchdl.html'
language: en
---

# BLDC HDL

## Ports

### Input

### **Config** — Block configuration signal vector

Configuration signal for the BLDC HDL block containing the block
configuration parameters. For more information about the constituent
parameters, see the **Config** output port description in the
BLDC
Configuration block.

**Data Types:** `single`

### **PhaseVolt** — Stator terminal voltages `1`-by-`3` array

Stator terminal voltages *Va*,
*Vb*, and
*Vc*, in V.

**Data Types:** `single`

### **LdTrq/Spd** — Load torque on motor or speed of motor shaft scalar

Based on the mode of operation defined by the **Port
Configuration** parameter available in the multiplexed
**Config** input, the port supports one of these
inputs:

- *Tm* — Load torque on the
  motor shaft in N·m.
- *ωm* — Angular velocity of the
  motor in rad/s.

**Data Types:** `single`

### **Reset** — Reset bus signal scalar

Bus signal that the block uses to reset the internal integrators.

**Data Types:** `Boolean`
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

Phase currents *ia*, *ib*, and *ic*, in A of phases a, b, and c, respectively.

### **Torque** — Motor torque `scalar`

Motor torque, *Tmtr*, in N·m.

### **Speed** — Motor speed `scalar`

Angular speed of the motor, *ωmtr*,
in rad/s.

### **MtrElecAngle** — Motor electrical angle scalar

Electrical position of the motor,
*θe*, in rad.

**Data Types:** `single`

## Parameters

### **Sample time (s)** — Sample time of block `1e-6` (default) | scalar

The fixed time interval (in seconds) between consecutive instances of block
execution.

## Libraries

Motor Control Blockset HDL Support / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation
and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2023b**

## Description

Three-phase brushless DC motor with trapezoidal flux distribution

The BLDC block implements a three-phase brushless DC (BLDC) motor with a
trapezoidal back electromotive force that remains constant for a position range of 120
electrical degrees. The block uses the three-phase input voltages to regulate the individual
phase currents, allowing control of the motor torque or speed.

### Motor Construction

This figure shows a motor with a single pole pair.

The rotor magnetic field due to the permanent magnets creates a trapezoidal rate of
change of flux with the motor angle.

For the axes convention, the phase-*a* aligns with
*d*-axis when the motor angle *θr*is zero.

### Three-Phase Sinusoidal Model Electrical System

Instead of the standard *dq* reference frame, the block uses
*d’q’* reference frame, which is defined by these transformation
equations.

vd'=23((va−Ria−Ea)cosθe+(vb−Rib−Eb)cos(θe−2π3)+(vc−Ric−Ec)cos(θe+2π3))

vq'=−2π3((va−Ria−Ea)sinθe+(vb−Rib−Eb)sin(θe−2π3)+(vc−Ric−Ec)sin(θe+2π3))

Ea=Pωm∂ψa∂θeEb=Pωm∂ψb∂θeEc=Pωm∂ψc∂θe

ia=id'cosθe−iq'sinθeib=id'cos(θe−2π3)−iq'sin(θe−2π3)ic=id'cos(θe+2π3)−iq'sin(θe+2π3)

The block implements these equations expressed in the *dq* and
*d’q’* reference frame of the BLDC motor. All quantities in the
motor reference frame are with respect to the stator phase A.

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
| *θe* | Electrical angle (rad) |
| *va*, *vb*, *vc* | Stator phase A, B, and C voltages (V) |
| *ia*, *ib*, *ic* | Stator phase A, B, and C currents (A) |
| *Ea*, *Eb*, *Ec* | Back EMF of stator phases A, B, and C (V/m/s) |
| *ψa*, *ψb*, *ψc* | Total fluxes linking each stator winding (Wb) |

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
