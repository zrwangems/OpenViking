---
type: simulink-block
title: 'Interior PMSM'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'interiorpmsm'
documentation_source_path: 'ref/interiorpmsm.html'
language: en
---

# Interior PMSM

## Ports
```yaml
ports:
- name: LdTrq
  summary: Load torque on motor scalar
  direction: input
- name: Spd
  summary: Motor shaft speed scalar
  direction: input
- name: PhaseVolt
  summary: Stator terminal voltages 1-by-3 array
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: PhaseCurr
  summary: Phase a, b, c current 1-by-3 array
  direction: output
- name: MtrTrq
  summary: Motor torque scalar
  direction: output
- name: MtrSpd
  summary: Motor speed scalar
  direction: output
```

### Input

### **LdTrq** — Load torque on motor `scalar`

Load torque on the motor shaft,
*Tm*, in N·m.

#### Dependencies

To create this port, select `Torque` for
the **Mechanical input configuration**
parameter.

### **Spd** — Motor shaft speed `scalar`

Angular velocity of the motor,
*ωm*, in rad/s.

#### Dependencies

To create this port, select `Speed` for
the **Mechanical input configuration**
parameter.

### **PhaseVolt** — Stator terminal voltages `1`-by-`3` array

Stator terminal voltages,
*Va*,
*Vb*, and
*Vc*, in V.

#### Dependencies

To create this port, select `Speed` or
`Torque` for the **Mechanical
input configuration** parameter.
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

### **PhaseCurr** — Phase a, b, c current `1`-by-`3` array

Phase a, b, c current, *ia*,
*ib*, and
*ic*, in A.

### **MtrTrq** — Motor torque `scalar`

Motor torque, *Tmtr*, in
N·m.

#### Dependencies

To create this port, select `Speed` for
the **Mechanical input configuration**
parameter.

### **MtrSpd** — Motor speed `scalar`

Angular speed of the motor,
*ωmtr*, in rad/s.

#### Dependencies

To create this port, select `Torque` for
the **Mechanical input configuration**
parameter.
## Parameters
```yaml
parameters:
- name: Mechanical input configuration
  summary: Select port configuration Torque (default) | Speed
  group: ''
  block_parameter: port_config
  values: Torque (default) | Speed
- name: Simulation type
  summary: Select simulation type Continuous (default) | Discrete
  group: ''
  block_parameter: sim_type
  values: Continuous (default) | Discrete
- name: Sample Time (Ts)
  summary: Sample time for discrete integration 0.001 (default) | scalar
  group: ''
  block_parameter: Ts
  values: 0.001 (default) | scalar
- name: File
  summary: Path to motor parameter ".m" or ".mat" file file name
  group: ''
- name: Number of pole pairs (P)
  summary: Pole pairs 4 (default) | scalar
  group: ''
  block_parameter: P
  values: 4 (default) | scalar
- name: Stator resistance per phase (Rs)
  summary: Resistance 0.02 (default) | scalar
  group: ''
  block_parameter: Rs
  values: 0.02 (default) | scalar
- name: Stator d-axis and q-axis inductance (Ldq)
  summary: Inductance [1.7e-3 3.2e-3] (default) | vector
  group: ''
  block_parameter: Ldq
  values: 0.001 (default) | scalar
- name: Permanent flux linkage constant (lambda_pm)
  summary: Flux [1.7e-3 3.2e-3] (default) | vector
  group: ''
  block_parameter: lambda_pm
  values: 0.2205 (default) | scalar
- name: Back-emf constant (Ke)
  summary: Back electromotive force 159.9771 (default) | scalar
  group: ''
  block_parameter: Ke
  values: 0.001 (default) | scalar
- name: Physical inertia, viscous damping, static friction (mechanical)
  summary: Inertia, damping, friction [0.002700,4.924e-4,0] (default) | vector
  group: ''
  block_parameter: mechanical
  values: '[0.002700,4.924e-4,0] (default) | vector'
- name: Initial d-axis and q-axis current (idq0)
  summary: Current [0 0] (default) | vector
  group: ''
  block_parameter: idq0
  values: '[0 0] (default) | vector'
- name: Initial mechanical position (theta_init)
  summary: Angle 0 (default) | scalar
  group: ''
  block_parameter: theta_init
  values: 0 (default) | scalar
- name: Initial mechanical speed (omega_init)
  summary: Speed 0 (default) | scalar
  group: ''
  block_parameter: omega_init
  values: 0 (default) | scalar
```

#### Block Options

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

By default, the block uses a continuous sample time during simulation. If you want to generate code for single-precision targets, considering setting the parameter to `Discrete`.

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

Setting **Simulation type** to `Discrete` creates the **Sample Time, Ts** parameter.

### **Sample Time (Ts)** — Sample time for discrete integration `0.001` (default) | `scalar`

Integration sample time for discrete
simulation, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Simulation type** to
`Discrete` creates the **Sample
Time, Ts** parameter.

#### Load Parameters

### **File** — Path to motor parameter ".m" or ".mat" file file name

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

### **Number of pole pairs (P)** — Pole pairs `4` (default) | `scalar`

Motor pole pairs, *P*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `P` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Stator resistance per phase (Rs)** — Resistance `0.02` (default) | `scalar`

Stator phase resistance per phase,
*Rs*, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rs` |
| **Values:** | `0.02` (default) | `scalar` |
| **Data Types:** | `double` |

### **Stator d-axis and q-axis inductance (Ldq)** — Inductance `[1.7e-3 3.2e-3]` (default) | `vector`

Stator d-axis and q-axis inductance,
*Ld*,
*Lq*, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ldq` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Permanent flux linkage constant (lambda\_pm)** — Flux `[1.7e-3 3.2e-3]` (default) | `vector`

Permanent flux linkage constant,
*λpm*, in Wb.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lambda_pm` |
| **Values:** | `0.2205` (default) | `scalar` |
| **Data Types:** | `double` |

### **Back-emf constant (Ke)** — Back electromotive force `159.9771` (default) | `scalar`

Back electromotive force, EMF,
*Ke*, in Vpk\_LL/krpm. Vpk\_LL is
the peak voltage line-to-line measurement.

To calculate the permanent flux linkage constant, the block implements
this equation.

λpm=13⋅Ke1000P⋅602π

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ke` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Physical inertia, viscous damping, static friction (mechanical)** — Inertia, damping, friction `[0.002700,4.924e-4,0]` (default) | `vector`

Mechanical properties of the motor:

- Inertia, *J*, in kg.m^2
- Viscous damping, *F*, in N·m/(rad/s)
- Static friction, *Tf*,
  in N·m

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mechanical` |
| **Values:** | `[0.002700,4.924e-4,0]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set the **Mechanical input
configuration** parameter to
`Torque`.

#### Initial Values

### **Initial d-axis and q-axis current (idq0)** — Current `[0 0]` (default) | `vector`

Initial q- and d-axis currents, *iq,
id*, in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `idq0` |
| **Values:** | `[0 0]` (default) | `vector` |
| **Data Types:** | `double` |

### **Initial mechanical position (theta\_init)** — Angle `0` (default) | `scalar`

Initial motor angular position,
*θm0*, in rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `theta_init` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial mechanical speed (omega\_init)** — Speed `0` (default) | `scalar`

Initial angular velocity of the motor,
*ωm0*, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_init` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set the **Mechanical input
configuration** parameter to
`Torque`.
## Libraries

Powertrain Blockset / Propulsion / Electric Motors and Inverters Motor Control Blockset / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Three-phase interior permanent magnet synchronous motor with sinusoidal back electromotive force

The Interior PMSM block implements a three-phase interior permanent
magnet synchronous motor (PMSM) with sinusoidal back electromotive force. The block uses
the three-phase input voltages to regulate the individual phase currents, allowing
control of the motor torque or speed.

By default, the block sets the **Simulation
type** parameter to `Continuous` to use a
continuous sample time during simulation. If you want to generate code for fixed-step
double- and single-precision targets, considering setting the parameter to
`Discrete`. Then specify a **Sample Time,
Ts** parameter.

On the **Parameters** tab, if you
select `Back-emf constant (Ke)`, the block implements this
equation to calculate the permanent flux linkage constant.

λpm=13⋅Ke1000P⋅602π

### Motor Construction

This figure shows the motor construction with a single pole pair on the
rotor.

PMSM interior motor with a two-pole rotor

The motor magnetic field due to the permanent magnets creates a sinusoidal rate of
change of flux with motor angle.

For the axes convention, the *a*-phase and permanent magnet
fluxes are aligned when motor angle *θr* is
zero.

### Three-Phase Sinusoidal Model Electrical System

The block implements these equations, expressed in the motor flux reference frame
(dq frame). All quantities in the motor reference frame are referred to the stator.

ωe=Pωmddtid=1Ldvd−RLdid+LqLdPωmiq

ddtiq=1Lqvq−RLqiq−LdLqPωmid−λpmPωmLq

Te=1.5P[λpmiq+(Ld−Lq)idiq]

The *Lq* and
*Ld* inductances represent the
relation between the phase inductance and the motor position due to the saliency of
the motor.

The equations use these variables.

|  |  |
| --- | --- |
| *Lq*,*Ld* | q- and d-axis inductances (H) |
| *R* | Resistance of the stator windings (ohm) |
| *iq*,*id* | q- and d-axis currents (A) |
| *vq*, *vd* | q- and d-axis voltages (V) |
| *ωm* | Angular mechanical velocity of the motor (rad/s) |
| *ωe* | Angular electrical velocity of the motor (rad/s) |
| *λpm* | Permanent flux linkage constant (Wb) |
| *Ke* | Back electromotive force (EMF) (Vpk\_LL/krpm, where Vpk\_LL is the peak voltage line-to-line measurement) |
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

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Mechanical power | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | Electrical power | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrElecLoss` | Resistive power loss | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | When **Mechanical input configuration** is set to `Torque`:  Pmech= −(ωm2F+ |ωm|Tf)  When **Mechanical input configuration** is set to `Speed`:  Pmech= 0 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrMtrStored` | Stored motor power | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

The equations use these variables.

|  |  |
| --- | --- |
| *R*s | Stator resistance (ohm) |
| *ia*,*ib*,*ic* | Stator phase a, b, and c current (A) |
| *isq*,*isd* | Stator q- and d-axis currents (A) |
| *van*, *vbn*, *vcn* | Stator phase a, b, and c voltage (V) |
| *ωm* | Angular mechanical velocity of the rotor (rad/s) |
| *F* | Combined motor and load viscous damping (N·m/(rad/s)) |
| *Te* | Electromagnetic torque (Nm) |
| *Tf* | Combined motor and load friction torque (Nm) |

### Amplitude Invariant *dq* Transformation

The block uses these equations to implement the amplitude invariant
*dq* transformation to ensure that the *dq*
and three phase amplitudes are equal.

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
