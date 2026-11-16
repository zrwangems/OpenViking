---
type: simulink-block
title: 'PMSM HDL'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'pmsmhdl'
documentation_source_path: '../mcb/ref/pmsmhdl.html'
language: en
---

# PMSM HDL

## Ports

### Input

### **Config** — Block configuration signal vector

Configuration signal for the PMSM HDL block containing the block configuration
parameters. For more information about the constituent parameters, see the
**Config** output of the PMSM
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
**Config** input, the port supports one of these inputs:

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
| `MtrSpd` | | | Angular mechanical velocity of the motor | *ωm* | rad/s |
| `MtrPos` | | | Motor mechanical angular position | *θm* | rad |
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

Electrical position of the motor, *θe*, in
rad.

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

Three-phase permanent magnet synchronous motor with sinusoidal back electromotive force

The PMSM HDL block implements a three-phase permanent magnet synchronous
motor (PMSM) with a sinusoidal back-electromotive force. The block uses three-phase input
voltages to regulate the individual phase currents, thereby controlling the motor torque or
speed.

The block generates code for fixed-step double- and single-precision targets using the
**Sample Time (s)** parameter. It supports code generation for FPGA
deployment and generates HDL-compatible code.

You can specify the PMSM parameters and operating mode using the
**Config** input port. You can also use the PMSM Configuration
block to generate the required configuration signal to specify at the
**Config** input port.

### Motor Construction

These diagrams show the interior and surface-mount PMSM construction with a single-pole
pair on the motor.

The motor magnetic field due to the permanent magnets creates a sinusoidal rate of
change of flux with the motor angle.

For the axes convention, the phase-*a* aligns with
*d*-axis when the motor angle *θr*
is zero.

### Three-Phase Sinusoidal Model Electrical System

The block implements these equations expressed in the motor flux reference frame
(*dq* frame). All quantities in the motor reference frame are referred to
as the stator.

ωe=Pωmddtid=1Ldvd−RLdid+LqLdPωmiq

ddtiq=1Lqvq−RLqiq−LdLqPωmid−λpmPωmLq

Te=1.5P[λpmiq+(Ld−Lq)idiq]

The *Lq* and
*Ld* inductances represent the relation between
the phase inductance and the motor position due to the saliency of the motor magnets. For a
surface mount PMSM, Ld=Lq.

The equations use these variables.

|  |  |
| --- | --- |
| *Lq*,*Ld* | *q*- and *d*-axis inductances (H) |
| *R* | Resistance of the stator windings (ohm) |
| *iq*,*id* | *q*- and *d*-axis currents (A) |
| *vq*, *vd* | *q*- and *d*-axis voltages (V) |
| *ωm* | Angular mechanical velocity of the motor (rad/s) |
| *ωe* | Angular electrical velocity of the motor (rad/s) |
| *λpm* | Permanent magnet flux linkage (Wb) |
| *Ke* | Back electromotive force (EMF) (Vpk\_LL/krpm, where Vpk\_LL is the peak voltage line-to-line measurement) |
| *Kt* | Torque constant (N·m/A)  *Kt* = Rated torque of motor / *Ia\_peak\_rated*, where *Ia\_peak\_rated* is the peak amplitude of phase-*a* at rated current operation. |
| *P* | Number of pole pairs |
| *Te* | Electromagnetic torque (Nm) |
| *Θe* | Electrical angle (rad) |

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
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Mechanical power | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | Electrical power | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrElecLoss` | Resistive power loss | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | When **Port Configuration** is set to `Torque`:  Pmech= −(ωm2F+ |ωm|Tf)  When **Port Configuration** is set to `Speed`:  Pmech= 0 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrMtrStored` | Stored motor power | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

The equations use these variables.

|  |  |
| --- | --- |
| *Rs* | Stator resistance (ohm) |
| *ia*,*ib*,*ic* | Stator phase *a*, *b*, and *c* current (A) |
| *isq*,*isd* | Stator *q*- and *d*-axis currents (A) |
| *van*, *vbn*, *vcn* | Stator phase *a*, *b*, and *c* voltage (V) |
| *ωm* | Angular mechanical velocity of the motor (rad/s) |
| *F* | Combined motor and load viscous damping N·m/(rad/s) |
| *Te* | Electromagnetic torque (Nm) |
| *Tf* | Combined motor and load friction torque (Nm) |

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
