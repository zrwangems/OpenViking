---
type: simulink-block
title: 'Induction Motor'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'inductionmotor'
documentation_source_path: 'ref/inductionmotor.html'
language: en
---

# Induction Motor

## Ports

### Input

### **LdTrq** — Load torque on motor `scalar`

Load torque on the motor shaft,
*Tm*, in N·m.

#### Dependencies

To create this port, select `Torque` for
the **Port configuration** parameter.

### **Spd** — Rotor shaft speed `scalar`

Angular velocity of the rotor,
*ωm*, in rad/s.

#### Dependencies

To create this port, select `Speed` for
the **Port configuration** parameter.

### **PhaseVolt** — Stator terminal voltages `1`-by-`3` array

Stator terminal voltages,
*Va*,
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

### **PhaseCurr** — Phase a, b, c current `1`-by-`3` array

Phase a, b, c current, *ia*,
*ib*, and
*ic*, in A.

### **MtrTrq** — Motor torque `scalar`

Motor torque, *Tmtr*, in
N·m.

#### Dependencies

To create this port, select `Speed` for
the **Port configuration** parameter.

### **MtrSpd** — Motor speed `scalar`

Angular speed of the motor,
*ωmtr*, in rad/s.

#### Dependencies

To create this port, select `Torque` for
the **Port configuration** parameter.

## Parameters

#### Block Options

### **Simulation type** — Select simulation type `Continuous` (default) | `Discrete`

By default, the block uses a continuous sample time
during simulation. If you want to generate code for single-precision targets, considering
setting the parameter to `Discrete`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sim_type` |
| **Values:** | `Continuous` (default) | `Discrete` |
| **Data Types:** | `character vector` |

#### Dependencies

Setting **Simulation Type** to `Discrete`
creates the **Sample Time, Ts** parameter.

### **Sample time, Ts** — Sample time for discrete integration `0.001` (default) | `scalar`

Integration sample time for discrete simulation, in
s.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Simulation Type** to
`Discrete` creates the **Sample Time,
Ts** parameter.

### **Port configuration** — Select port configuration `Torque` (default) | `Speed`

This table summarizes the port configurations.

| Port Configuration | Creates Input Port | Creates Output Port |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **Values:** | `Torque` (default) | `Speed` |
| **Data Types:** | `character vector` |

#### Load Parameter Values

### **File** — Path to motor parameter ".m" or ".mat" file `scalar`

Enter the path to the motor parameter
".m" or ".mat" file that you saved using the Motor Control Blockset™ parameter estimation tool. You can also click the
**Browse** button to navigate and select the ".m" or
".mat" file, and update **File** parameter with the file
name and path. For details related to the motor parameter estimation
process, see Estimate PMSM Parameters Using Parameter Estimation Blocks.

- **Load from file** - Click this button to read
  the estimated motor parameters from the ".m" or ".mat" file
  (indicated by the **File** parameter) and load them
  to the motor block.
- **Save to file** - Click this button to read
  the motor parameters from the motor block and save them into a ".m"
  or ".mat" file (with a file name and location that you specify in
  the **File** parameter).

**Note**

Before you click **Save to file** button, ensure
that the target file name in the **File** parameter has
either ".m" or ".mat" extension. If you use any other file extension,
the block displays an error message.

#### Parameters

### **Number of pole pairs, P** — Pole pairs `2` (default) | `scalar`

Motor pole pairs, *P*.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `P` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Stator resistance and leakage inductance, Zs** — Resistance and inductance `[1.77 0.0139]` (default) | `vector`

Stator resistance, *RS*, in ohms
and leakage inductance, *Lls*, in
H.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Zs` |
| **Values:** | `[1.77 0.0139]` (default) | `vector` |
| **Data Types:** | `double` |

### **Rotor resistance and leakage inductance, Zr** — Resistance and inductance `[1.34 0.0121]` (default) | `vector`

Rotor resistance, *Rr*, in ohms
and leakage inductance, *Llr*, in
H.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Zr` |
| **Values:** | `[1.34 0.0121]` (default) | `vector` |
| **Data Types:** | `double` |

### **Magnetizing inductance, Lm** — Inductance `0.3687` (default) | `scalar`

Magnetizing inductance, *Lm*, in
H.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Lm` |
| **Values:** | `0.3687` (default) | `scalar` |
| **Data Types:** | `double` |

### **Physical inertia, viscous damping, static friction, mechanical** — Inertia, damping, friction `[0.001 0 0]` (default) | `vector`

Mechanical properties of the rotor:

- Inertia, *J*, in kg·m^2
- Viscous damping, *F*, in N·m/(rad/s)
- Static friction, *Tf*,
  in N·m

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `mechanical` |
| **Values:** | `[0.001 0 0]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Torque` for
the **Port configuration**.

#### Initial Values

### **Initial mechanical position, theta\_init** — Angular position `0` (default) | `scalar`

Initial rotor angular position,
*θm0*, in rad.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `theta_init` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial mechanical speed, omega\_init** — Angular speed `0` (default) | `scalar`

Initial angular velocity of the rotor,
*ωm0*, in rad/s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_init` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Torque` for
the **Port configuration**.

## Libraries

Powertrain Blockset / Propulsion / Electric Motors and Inverters Motor Control Blockset / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Three-phase induction motor

The Induction Motor block implements a three-phase induction motor. The
block uses the three-phase input voltages to regulate the individual phase currents,
allowing control of the motor torque or speed.

**Note**

The block parameters use per-phase values of a star-equivalent induction
motor.

By default, the block sets the **Simulation
Type** parameter to `Continuous` to use a continuous
sample time during simulation. If you want to generate code for fixed-step double- and
single-precision targets, considering setting the parameter to
`Discrete`. Then specify a **Sample Time, Ts**
parameter.

### Three-Phase Sinusoidal Model Electrical System

The block implements equations that are expressed in a stationary rotor reference
(dq) frame. The d-axis aligns with the a-axis. All quantities in the rotor reference
frame are referred to the stator.

Three-phase induction motor currents and magnetic fields

The block uses these equations to calculate the electrical speed
(*ωem*) and slip speed
(*ωslip*).

ωem=Pωmωslip= ωsyn−ωem

To calculate the dq rotor electrical speed with respect to the rotor A-axis
(*dA*), the block uses the difference between the stator a-axis
(*da*) speed and slip speed:

ωdA= ωda− ωem

To simplify the equations for the flux, voltage, and current transformations, the
block uses the rotor A-axis reference frame:

ωda=ωemωdA=0

| Calculation | Equation |
| --- | --- |
| Flux | ddt[λsdλsq]= [vsdvsq]− Rs[isdisq]− ωda[0−110][λsdλsq]ddt[λrdλrq]= [vrdvrq]− Rr[irdirq]− ωdA[0−110][λrdλrq]      [λsdλsqλrdλrq]= [Ls00LsLm00LmLm00LmLr00Lr][isdisqirdirq] |
| Current | [isdisqirdirq]= (1Lm2− LrLs)[−Lr00−LrLm00LmLm00Lm−Ls00−Ls][λsdλsqλrdλrq] |
| Inductance | Ls= Lls+LmLr= Llr+Lm |
| Electromagnetic torque | Te=PLm(isqird− isdirq) |
| Power invariant dq transformation to ensure that the dq and three phase powers are equal | [vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]      [iaibic]= 23  [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq] |

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

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Mechanical power | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | Electrical power | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrElecLoss` | Resistive power loss | *Pelec* | Pelec= −(Rsisd2+Rsisq2+−Rrird2+Rrirq2) |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | When **Port Configuration** is set to `Torque`:  Pmech= −(ωm2F+ |ωm|Tf)  When **Port Configuration** is set to `Speed`:  Pmech= 0 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrMtrStored` | Stored motor power | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

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
