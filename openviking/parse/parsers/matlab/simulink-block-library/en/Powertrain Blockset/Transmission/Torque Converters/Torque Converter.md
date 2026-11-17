---
type: simulink-block
title: 'Torque Converter'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission / Torque Converters'
documentation_page: 'torqueconverter'
documentation_source_path: 'ref/torqueconverter.html'
language: en
---

# Torque Converter

## Ports
```yaml
ports:
- name: ImpTrq
  summary: Applied impeller torque scalar
  direction: input
- name: TurbTrq
  summary: Applied turbine torque scalar
  direction: input
- name: Clutch Force
  summary: Applied clutch force scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: ImpSpd
  summary: Impeller speed scalar
  direction: output
- name: TurbSpd
  summary: Turbine speed scalar
  direction: output
```

### Inputs

### **ImpTrq** — Applied impeller torque `scalar`

Applied input torque, typically from the engine crankshaft or dual
mass flywheel, in N·m.

### **TurbTrq** — Applied turbine torque `scalar`

Applied turbine torque, typically from the transmission, in
N·m.

### **Clutch Force** — Applied clutch force `scalar`

Applied clutch force, typically from a hydraulic actuator, in
N.

#### Dependencies

To create this port, select `External lock-up input` for
the **Lock-up clutch configuration** parameter.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Imp` | `ImpTrq` | | Applied input torque | N·m |
| `ImpSpd` | | Impeller rotational shaft speed | rad/s |
| `Turb` | `TurbTrq` | | Applied turbine torque | N·m |
| `TurbSpd` | | Turbine rotational shaft speed | rad/s |
| `Cltch` | `CltchForce` | | Applied clutch force | N |
| `CltchLocked` | | Clutch locked or unlocked state | N/A |
| `TrqConv` | `TrqConvSpdRatio` | | Turbine to impeller speed ratio | N/A |
| `TrqConvEta` | | Torque conversion efficiency | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrImp` | Applied impeller power | W |
| `PwrTurb` | Applied turbine output power | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Mechanical damping loss | W |
| `PwrFluidCplingLoss` | Heat loss to transmission fluid | W |
| `PwrCltchLoss` | Clutch slip power loss | W |
| `PwrStored` | `PwrStoredImp` | Rate change in impeller rotational kinetic energy | W |
| `PwrStoredTurb` | Rate change in turbine rotational kinetic energy | W |

### **ImpSpd** — Impeller speed `scalar`

Impeller rotational shaft speed, ωi, in rad/s.

### **TurbSpd** — Turbine speed `scalar`

Turbine rotational shaft speed, ωt, in rad/s.
## Parameters
```yaml
parameters:
- name: Lock-up clutch configuration
  summary: Select lock-up clutch configuration Lock-up (default) | No lock-up | External lock-up input
  group: ''
  block_parameter: TCType
  values: Lock-up (default) | No lock-up | External lock-up input
- name: Impeller shaft inertia, Ji
  summary: Inertia .1 (default) | scalar
  group: ''
  block_parameter: Ji
  values: .1 (default) | scalar
- name: Impeller shaft viscous damping, bi
  summary: Viscous damping coefficient .001 (default) | scalar
  group: ''
  block_parameter: bi
  values: .001 (default) | scalar
- name: Turbine shaft inertia, Jt
  summary: Inertia .1 (default) | scalar
  group: ''
  block_parameter: Jt
  values: .1 (default) | scalar
- name: Turbine shaft viscous damping, bt
  summary: Viscous damping coefficient .001 (default) | scalar
  group: ''
  block_parameter: bt
  values: .001 (default) | scalar
- name: Initial impeller shaft velocity, omegai_o
  summary: Angular velocity 0 (default) | scalar
  group: ''
  block_parameter: omegai_o
  values: 0 (default) | scalar
- name: Initial turbine shaft velocity, omegat_o
  summary: Angular velocity 0 (default) | scalar
  group: ''
  block_parameter: omegat_o
  values: 0 (default) | scalar
- name: Speed ratio vector, phi
  summary: Ratio [ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97] (default) | vector
  group: ''
  block_parameter: phi
  values: '[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97] (default) | vector'
- name: Capacity factor parameterization
  summary: Select factor ratio type Input speed / sqrt(input torque) (default) | Absorbed torque / input speed^2
  group: ''
  block_parameter: KType
  values: Input speed / sqrt(input torque) (default) | Absorbed torque / input speed^2
- name: Capacity vector, psi
  summary: Vector [12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00] (default) | vector
  group: ''
  block_parameter: psi
  values: '[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00] (default) | vector'
- name: Torque ratio vector, zeta
  summary: Vector [2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983] (default) | vector
  group: ''
  block_parameter: zeta
  values: '[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983] (default) | vector'
- name: Fluid torque response time constant (set to 0 to disable), tauTC
  summary: Time constant .02 (default) | scalar
  group: ''
  block_parameter: tauTC
  values: .02 (default) | scalar
- name: Interpolation method
  summary: Select interpolation method Linear (default) | Flat | Nearest
  group: ''
  block_parameter: InterpMethod
  values: Linear (default) | Flat | Nearest
- name: Clutch force equivalent net radius, Reff
  summary: Effective radius .3 (default) | scalar
  group: ''
  block_parameter: Reff
  values: .3 (default) | scalar
- name: Static friction coefficient, mus
  summary: Coefficient 1.2 (default) | scalar
  group: ''
  block_parameter: mus
  values: 1.2 (default) | scalar
- name: Kinetic friction coefficient, muk
  summary: Coefficient 1 (default) | scalar
  group: ''
  block_parameter: muk
  values: 1 (default) | scalar
- name: Start simulation with clutch initially locked
  summary: Select to initially lock clutch off (default) | on
  group: ''
  block_parameter: Jin
  values: off (default) | on
- name: Lock-up speed ratio threshold, philu
  summary: Threshold .85 (default) | scalar
  group: ''
  block_parameter: philu
  values: 0.1 (default) | scalar
- name: Minimum lock-up engagement speed, omegal
  summary: Angular velocity 900*pi/30 (default) | scalar
  group: ''
  block_parameter: omegal
  values: 0.1 (default) | scalar
- name: Lock-up disengagement speed, omegau
  summary: Angular velocity 800*pi/30 (default) | scalar
  group: ''
  block_parameter: omegau
  values: 0.1 (default) | scalar
- name: Lock-up clutch force gain, K_c
  summary: Gain 5000 (default) | scalar
  group: ''
  block_parameter: K_c
  values: 0.1 (default) | scalar
- name: Lock-up clutch time constant, tauC
  summary: Time constant .0500 (default) | scalar
  group: ''
  block_parameter: tauC
  values: 0.1 (default) | scalar
```

#### Configuration

### **Lock-up clutch configuration** — Select lock-up clutch configuration `Lock-up` (default) | `No lock-up` | `External lock-up input`

| To Model | Select |
| --- | --- |
| Fluid-coupling only | `No lock-up` |
| Automatic clutch engagement | `Lock-up` |
| Clutch pressure as input from an external signal | `External lock-up input` |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `TCType` |
| **Values:** | `Lock-up` (default) | `No lock-up` | `External lock-up input` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable the **Clutch** parameters, select
`Lock-up` or `External lock-up
input` for the **Lock-up clutch
configuration** parameter.

#### Torque Converter

### **Impeller shaft inertia, Ji** — Inertia `.1` (default) | `scalar`

Impeller shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ji` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Impeller shaft viscous damping, bi** — Viscous damping coefficient `.001` (default) | `scalar`

Impeller shaft viscous damping, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bi` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Turbine shaft inertia, Jt** — Inertia `.1` (default) | `scalar`

Turbine shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jt` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Turbine shaft viscous damping, bt** — Viscous damping coefficient `.001` (default) | `scalar`

Turbine shaft viscous damping, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bt` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial impeller shaft velocity, omegai\_o** — Angular velocity `0` (default) | `scalar`

Initial impeller shaft velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegai_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial turbine shaft velocity, omegat\_o** — Angular velocity `0` (default) | `scalar`

Initial turbine shaft velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegat_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Speed ratio vector, phi** — Ratio `[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]` (default) | `vector`

Vector of turbine speed to impeller speed ratios. Breakpoints for the
capacity and torque multiplication vectors.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `phi` |
| **Values:** | `[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]` (default) | `vector` |
| **Data Types:** | `double` |

### **Capacity factor parameterization** — Select factor ratio type `Input speed / sqrt(input torque)` (default) | `Absorbed torque / input speed^2`

| To Set Factor Ratio to | Select |
| --- | --- |
| Impeller angular velocity to square root impeller torque | `Input speed / sqrt(input torque)` |
| Impeller absorbed torque to square of impeller angular velocity | `Absorbed torque / input speed^2` |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `KType` |
| **Values:** | `Input speed / sqrt(input torque)` (default) | `Absorbed torque / input speed^2` |
| **Data Types:** | `character vector` |

### **Capacity vector, psi** — Vector `[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]` (default) | `vector`

| **Capacity factor parameterization** Setting | Capacity Vector Units |
| --- | --- |
| `Input speed / sqrt(input torque)` | (rad/s)/(N·m)^0.5 |
| `Absorbed torque / input speed^2` | N·m/(rad/s)^2 |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `psi` |
| **Values:** | `[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]` (default) | `vector` |
| **Data Types:** | `double` |

### **Torque ratio vector, zeta** — Vector `[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]` (default) | `vector`

Vector of turbine torque to impeller speed ratios.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zeta` |
| **Values:** | `[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]` (default) | `vector` |
| **Data Types:** | `double` |

### **Fluid torque response time constant (set to 0 to disable), tauTC** — Time constant `.02` (default) | `scalar`

To account for the delay in torque calculations due to changing input
torque, specify the fluid torque transfer time constant, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tauTC` |
| **Values:** | `.02` (default) | `scalar` |
| **Data Types:** | `double` |

### **Interpolation method** — Select interpolation method `Linear` (default) | `Flat` | `Nearest`

Interpolates the torque ratio and capacity factor functions between
the discrete relative velocity values.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InterpMethod` |
| **Values:** | `Linear` (default) | `Flat` | `Nearest` |
| **Data Types:** | `character vector` |

#### Clutch

### **Clutch force equivalent net radius, Reff** — Effective radius `.3` (default) | `scalar`

The effective radius, Reff, used with the applied clutch friction force to determine the friction force,
in m. The effective radius is defined as:

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

The equation uses these variables.

|  |  |
| --- | --- |
| Ro | Annular disk outer radius |
| Ri | Annular disk inner radius |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Reff` |
| **Values:** | `.3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the **Clutch** parameters, select
`Lock-up` or `External lock-up
input` for the **Lock-up clutch
configuration** parameter.

### **Static friction coefficient, mus** — Coefficient `1.2` (default) | `scalar`

Dimensionless clutch disc coefficient of static friction.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mus` |
| **Values:** | `1.2` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the **Clutch** parameters, select
`Lock-up` or `External lock-up
input` for the **Lock-up clutch
configuration** parameter.

### **Kinetic friction coefficient, muk** — Coefficient `1` (default) | `scalar`

Dimensionless clutch disc coefficient of kinetic friction.

To enable the **Clutch** parameters, select
`Lock-up` or `External lock-up input` for the **Lock-up clutch
configuration** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `muk` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Start simulation with clutch initially locked** — Select to initially lock clutch `off` (default) | `on`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jin` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, select `Lock-up` or
`External lock-up input` for the
**Lock-up clutch configuration** parameter.

### **Lock-up speed ratio threshold, philu** — Threshold `.85` (default) | `scalar`

Set speed ratio threshold that engages clutch lock-up.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `philu` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Lock-up`
for the **Lock-up clutch configuration**
parameter.

### **Minimum lock-up engagement speed, omegal** — Angular velocity `900*pi/30` (default) | `scalar`

Set the minimum impeller speed that engages clutch lock-up, in
rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegal` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Lock-up`
for the **Lock-up clutch configuration**
parameter.

### **Lock-up disengagement speed, omegau** — Angular velocity `800*pi/30` (default) | `scalar`

Set the minimum impeller speed that disengages clutch lock-up, in
rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegau` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Lock-up`
for the **Lock-up clutch configuration**
parameter.

### **Lock-up clutch force gain, K\_c** — Gain `5000` (default) | `scalar`

Open loop clutch lock-up force gain, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `K_c` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Lock-up`
for the **Lock-up clutch configuration**
parameter.

### **Lock-up clutch time constant, tauC** — Time constant `.0500` (default) | `scalar`

Open loop clutch lock-up time constant, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tauC` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Lock-up`
for the **Lock-up clutch configuration**
parameter.
## Libraries

Powertrain Blockset / Transmission / Torque Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Three-part torque converter consisting of an impeller, turbine, and stator

The Torque Converter block implements a three-part torque converter consisting
of an impeller, turbine, and stator with an optional clutch lock-up capability. The
block can simulate driving (power flowing from impeller to turbine) and coasting (power
from turbine dissipated in torque converter hydraulic fluid).

You can specify torque converter characteristics:

- Speed ratio — Ratio of turbine angular speed
  to impeller angular speed
- Torque ratio — Ratio of turbine torque to impeller
  torque
- Capacity factor parameterization — Function
  of input speed or input torque

Optional clutch lock-up configurations include:

- No lock-up — Model fluid-coupling only
- Lock-up — Model automatic clutch engagement
- External lock-up — Model clutch pressure as
  input from an external signal

### Dynamics

**Clutch Lock-Up Condition and Clutch Friction**

Based on the clutch lock-up condition, the block implements
these friction models.

| If | Clutch Condition | Friction Model |
| --- | --- | --- |
| ωi≠ωtorTS<|Jt(Ji+Jt)[Ti+Tf−ωi(bt+bi)]| | Unlocked | Tf=Tkwhere:Tk=FcReffmktanh[4(ωi−ωt)]Ts=FcReffmsReff=2(Ro3-Ri3)3(Ro2-Ri2) |
| ωi=ωtandTS≥|Jt(Ji+Jt)[Ti+Tf-wt(bt+bi)+wtbt]| | Locked | *Tf* = *Ts* |

**Locked Rotational Dynamics**

To model the rotational dynamics if the clutch is locked, the
block implements equations.

ω˙(Ji+Jt)=Ti−ω(bi+bt)+Textω=ωi=ωt

The rotational velocity represents both the impeller and turbine
rotational velocities.

**Unlocked Rotational Dynamics**

To model the rotational dynamics if the clutch is unlocked,
the block implements equations.

ω˙iJi=Ti−ωibi−Tf−Tpω˙tJt=Text−ωtbt+Tf+TtTp= ωi2ψ(ϕ)Tt= Tpζ(ϕ)

To approximate the torque multiplication lag between the impeller
and turbine, you can specify the parameter **Fluid torque
response time constant (set to 0 to disable), tauc [s]**.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrImp` | Applied impeller power | *Pimp* | ωiTi |
| `PwrTurb` | Applied turbine output power | *Pturb* | ωtTt |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | −btωt2−biωi2 |
| `PwrFluidCplingLoss` | Heat loss to transmission fluid | *Pflloss* | −(Tpωi−Thydωt) |
| `PwrCltchLoss` | Clutch slip power loss | *Pcltloss* | −Tk(ωi−ωt) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredImp` | Rate change in impeller rotational kinetic energy | *Pstrimp* | ω˙iωiJi |
| `PwrStoredTurb` | Rate change in turbine rotational kinetic energy | *Pstrturb* | ω˙tωtJt |

The block implements equations that use these variables.

|  |  |
| --- | --- |
| Tf | Frictional torque |
| Tk | Kinetic frictional torque |
| Ts | Static frictional torque |
| Ti | Applied input torque |
| Tp | Impeller reaction torque |
| Text | Externally applied turbine torque |
| ψ(ϕ) | Torque conversion capacity factor |
| ζ(ϕ) | Torque ratio |
| ωi | Impeller rotational shaft speed |
| ωt | Turbine rotational shaft speed |
| Ji | Impeller rotational inertia |
| Jt | Turbine rotational inertia |
| bi | Impeller rotational viscous damping |
| bt | Turbine rotational viscous damping |
| Reff | Effective clutch radius |
| Ro | Annular disk outer radius |
| Ri | Annular disk inner radius |
