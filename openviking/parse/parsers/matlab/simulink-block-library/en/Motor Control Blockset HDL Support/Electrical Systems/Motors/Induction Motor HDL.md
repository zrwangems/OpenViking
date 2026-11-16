---
type: simulink-block
title: 'Induction Motor HDL'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'inductionmotorhdl'
documentation_source_path: '../mcb/ref/inductionmotorhdl.html'
language: en
---

# Induction Motor HDL

## Ports

### Input

### **Config** — Block configuration signal vector

Configuration signal for the Induction Motor HDL block containing the block
configuration parameters.

**Data Types:** `single`

### **PhaseVolt** — Stator terminal voltages `1`-by-`3` array

Stator terminal voltages, *Va*,
*Vb*, and
*Vc*, in V.

**Data Types:** `single`

### **LdTrq/Spd** — Load torque on motor or speed of motor shaft scalar

The port supports one of these inputs:

- *Tm* — Load torque on the motor shaft,
  in N·m.
- *ωm* — Angular velocity of the motor,
  in rad/s.

**Data Types:** `single`

### **Reset** — Reset bus signal scalar

Reset bus signal that the block uses to reset the internal integrators.

**Data Types:** `Boolean`
### Output

### **Info** — Bus signal bus

The bus signal contains these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | Stator phase current A | *ia* | A |
| `IbStator` | | | Stator phase current B | *ib* | A |
| `IcStator` | | | Stator phase current C | *ic* | A |
| `IdSync` | | | Direct axis current | *id* | A |
| `IqSync` | | | Quadrature axis current | *iq* | A |
| `VdSync` | | | Direct axis voltage | *vd* | V |
| `VqSync` | | | Quadrature axis voltage | *vq* | V |
| `MtrSpd` | | | Angular mechanical velocity of the rotor | *ωm* | rad/s |
| `MtrMechPos` | | | Rotor mechanical angular position | *θm* | rad |
| `MtrPos` | | | Rotor electrical angular position | *θe* | rad |
| `MtrTrq` | | | Electromagnetic torque | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | Mechanical power | *Pmot* | W |
| `PwrBus` | Electrical power | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | Resistive power loss | *Pelec* | W |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | Stored motor power | *Pstr* | W |

### **PhaseCurr** — Current for phase *a*, *b*, and *c* `1`-by-`3` array

Current for phase *a*, *b*, and
*c*, *ia*,
*ib*, and
*ic*, respectively, in A.

### **Torque** — Motor torque `scalar`

Motor torque, *Tmtr*, in N·m.

### **Speed** — Motor speed `scalar`

Angular speed of the motor, *ωmtr*, in
rad/s.

### **MtrElecAngle** — Motor electrical angle scalar

Electrical position of the motor, *θdq*,
in rad.

**Data Types:** `single`

## Parameters

### **Sample time (s)** — Sample time after which block executes again `1e-6` (default) | scalar

The fixed time interval (in seconds) between consecutive instances of block
execution.

## Libraries

Motor Control Blockset HDL Support / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

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

**Introduced in R2022b**

## Description

Three-phase induction motor

The Induction Motor HDL block implements a three-phase induction motor. The
block uses three-phase input voltages to regulate the individual phase currents, thereby
controlling the motor torque or speed.

The block generates code for fixed-step double- and single-precision targets using the
**Sample Time (s)** parameter. It supports code generation for FPGA
deployment and generates HDL-compatible code.

You can specify the induction motor parameters and operating mode using the
**Config** input port. You can also use the Induction Motor
Configuration block to generate the required configuration signal to specify at the
**Config** input port.

### Three-Phase Sinusoidal Model Electrical System

The block implements equations expressed in the stationary rotor reference
(*dq*) frame. The *d*-axis aligns with the
*a*-axis. All quantities in the rotor reference frame are referred to as
the stator.

The block uses these equations to calculate the electrical speed
(*ωem*) and slip speed
(*ωslip*).

ωem=Pωmωslip= ωsyn−ωem

To calculate the *dq* rotor electrical speed with respect to the rotor
*A*-axis (*dA*), the block uses the difference between
the stator *a*-axis (*da*) speed and the slip speed:

ωdA= ωda− ωem

To simplify the equations for the flux, voltage, and current transformations, the block
uses the rotor A-axis reference frame:

ωda=ωemωdA=0

| Calculation | Equation |
| --- | --- |
| Flux | ddt[λsdλsq]= [vsdvsq]− Rs[isdisq]− ωda[0−110][λsdλsq]ddt[λrdλrq]= [vrdvrq]− Rr[irdirq]− ωdA[0−110][λrdλrq]      [λsdλsqλrdλrq]= [Ls00LsLm00LmLm00LmLr00Lr][isdisqirdirq] |
| Current | [isdisqirdirq]= (1Lm2− LrLs)[−Lr00−LrLm00LmLm00Lm−Ls00−Ls][λsdλsqλrdλrq] |
| Inductance | Ls= Lls+LmLr= Llr+Lm |
| Electromagnetic torque | Te=PLm(isqird− isdirq) |
| Power invariant *dq* transformation to ensure that the *dq* and the three phase powers are equal | [vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]      [iaibic]= 23  [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq] |

The equations use these variables.

|  |  |
| --- | --- |
| *ωm* | Angular velocity of the rotor (rad/s) |
| *ωem* | Electrical rotor speed (rad/s) |
| *ωslip* | Electrical rotor slip speed (rad/s) |
| *ωsyn* | Synchronous rotor speed (rad/s) |
| *ωda* | dq stator electrical speed with respect to the stator a-axis (rad/s) |
| *ωdA* | dq stator electrical speed with respect to the rotor A-axis (rad/s) |
| *Θda* | dq stator electrical angle with respect to the stator a-axis (rad) |
| *ΘdA* | dq stator electrical angle with respect to the rotor A-axis (rad) |
| *Lq*,*Ld* | q- and d-axis inductances (H) |
| *Ls* | Stator inductance (H) |
| *Lr* | Rotor inductance (H) |
| *Lm* | Magnetizing inductance (H) |
| *Lls* | Stator leakage inductance (H) |
| *Llr* | Rotor leakage inductance (H) |
| *vsq*, *vsd* | Stator q- and d-axis voltages (V) |
| *isq*,*isd* | Stator q- and d-axis currents (A) |
| *λsq*,*λsd* | Stator q- and d-axis flux (Wb) |
| *irq*,*ird* | Rotor q- and d-axis currents (A) |
| *λrq*,*λrd* | Rotor q- and d-axis flux (Wb) |
| *va*,*vb*,*vc* | Stator voltage phases a, b, c (V) |
| *ia*, *ib*, *ic* | Stator currents phases a, b, c (A) |
| *Rs* | Resistance of the stator windings (Ohm) |
| *Rr* | Resistance of the rotor windings (Ohm) |
| *P* | Number of pole pairs |
| *Te* | Electromagnetic torque (Nm) |

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

### Power Accounting

For motor power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` |  | `PwrMtr` | Mechanical power | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | Electrical power | *Pbus* | Pbus= vania+ vbnib+vcnic |
|  | `PwrElecLoss` | Resistive power loss | *Pelec* | Pelec= −(Rsisd2+Rsisq2+−Rrird2+Rrirq2) |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | When **Port Configuration** is set to `Torque`:  Pmech= −(ωm2F+ |ωm|Tf)  When **Port Configuration** is set to `Speed`:  Pmech= 0 |
|  | `PwrMtrStored` | Stored motor power | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

The equations use these variables.

|  |  |
| --- | --- |
| *Rs* | Stator resistance (Ohm) |
| *Rr* | Rotor resistance (Ohm) |
| *ia*,*ib*,*ic* | Stator phase a, b, and c current (A) |
| *isq*,*isd* | Stator q- and d-axis currents (A) |
| *van*, *vbn*, *vcn* | Stator phase a, b, and c voltage (V) |
| *ωm* | Angular mechanical velocity of the rotor (rad/s) |
| *F* | Combined viscous damping of motor and load (N·m/(rad/s)) |
| *Te* | Electromagnetic torque (Nm) |
| *Tf* | Combined friction torque of motor and load (Nm) |
