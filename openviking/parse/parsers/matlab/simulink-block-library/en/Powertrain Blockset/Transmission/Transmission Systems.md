---
type: simulink-block
title: 'Automated Manual Transmission'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission'
documentation_page: 'automatedmanualtransmission'
documentation_source_path: 'ref/automatedmanualtransmission.html'
language: en
---

# Automated Manual Transmission

## Ports

### Input

### **Gear** — Gear number to engage `scalar`

Integer value of gear number to engage.

### **CltchCmd** — Clutch command `scalar`

Clutch pressure command.

#### Dependencies

To create this port, select **Control type**
parameter `External control`.

### **EngTrq** — Applied input torque `scalar`

Applied input torque, *Ti*,
typically from the engine crankshaft or dual mass flywheel damper, in
N·m.

### **DiffTrq** — Applied load torque `scalar`

Applied load torque, *Td*,
typically from the differential or driveshaft, in N·m.

### **Temp** — Oil temperature `scalar`

Oil temperature, in K. To determine the efficiency, the block uses a
4D lookup table that is a function of:

- Gear
- Input torque
- Input speed
- Oil temperature

#### Dependencies

To create this port, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.
### Output

### **Info** — Bus signal bus

Bus signal contains these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `Eng` | `EngTrq` | | Input applied torque | *Ti* | N·m |
| `EngSpd` | | Input drive shaft speed | *ωi* | rad/s |
| `Diff` | `DiffTrq` | | Output drive shaft torque | *Tt* | N·m |
| `DiffSpd` | | Output drive shaft speed | *ωt* | rad/s |
| `Cltch` | `CltchForce` | | Applied clutch force | *Fc* | N |
| `CltchLocked` | | Clutch lock status, Boolean:  - Locked — `0` - Unlocked —   `1` | N/A | N/A |
| `Trans` | `TransSpdRatio` | | Speed ratio at time *t* | ϕ(t) | N/A |
| `TransEta` | | Ratio of output power to input power | η | N/A |
| `TransGearCmd` | | Commanded gear | *Ncmd* | N/A |
| `TransGear` | | Engaged gear | *N* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | Engine power | *Peng* | W |
| `PwrDiffrntl` | Differential power | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrEffLoss` | Mechanical power loss | *Peffloss* | W |
| `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | W |
| `PwrCltchLoss` | Clutch power loss | *Pmech* | W |
| `PwrStored` | `PwrStoredTrans` | Rate change in rotational kinetic energy | *Pstr* | W |

### **EngSpd** — Angular speed `scalar`

Applied drive shaft angular speed input,
*ωi*, in rad/s.

### **DiffSpd** — Angular speed `scalar`

Drive shaft angular speed output,
*ωd*, in rad/s.

## Parameters

### **Control type** — Specify control type `Ideal integrated controller` (default) | `External control`

The AMT delivers drive shaft torque continuously by controlling
the pressure signals from the clutch. If you select **Control
type** parameter `Ideal integrated controller`,
the block generates idealized clutch pressure signals. To use your
own clutch control signals, select **Control type** parameter `External
control`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `cntrlType` |
| **Values:** | `Ideal integrated controller` (default) | `External control` |
| **Data Types:** | `character vector` |

#### Dependencies

This table summarizes the port configurations.

| Control Mode | Creates Ports |
| --- | --- |
| `External control` | `CltchCmd` |

### **Efficiency factors** — Specify efficiency calculation `Gear only` (default) | `Gear, input torque, input speed, and temperature`

To specify the block efficiency calculation, for **Efficiency factors**, select either of these options.

| Setting | Block Implementation |
| --- | --- |
| `Gear only` | Efficiency determined from a 1D lookup table that is a function of the gear. |
| `Gear, input torque, input speed, and temperature` | Efficiency determined from a 4D lookup table that is a function of:  - Gear - Input torque - Input speed - Oil temperature |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TransEffModelPopup` |
| **Values:** | `Gear only` (default) | `Gear, input torque, input speed, and temperature` |
| **Data Types:** | `character vector` |

#### Dependencies

| Setting Parameter To | Enables |
| --- | --- |
| `Gear only` | **Efficiency vector, eta** |
| `Gear, input torque, input speed, and temperature` | **Efficiency torque breakpoints, Trq\_bpts**  **Efficiency speed breakpoints, omega\_bpts**  **Efficiency temperature breakpoints, Temp\_bpts**  **Efficiency lookup table, eta\_tbl** |

#### Transmission

### **Input shaft inertia, Jin** — Inertia `.01` (default) | `scalar`

Input shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jin` |
| **Values:** | `.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Input shaft damping, bin** — Damping `.001` (default) | `scalar`

Input shaft damping, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bin` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial input velocity, omegain\_o** — Angular velocity `0` (default) | `scalar`

Angular velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegain_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Gear number vector, G** — Specify number of transmission speeds `[-1, 0, 1, 2, 3, 4, 5]` (default) | `vector`

Vector of integer gear commands used to specify the number of transmission
speeds. Neutral gear is `0`. For example, you can set these
parameter values.

| To Specify | Set **Gear number, G** To |
| --- | --- |
| Four transmission speeds, including neutral | `[0,1,2,3,4]` |
| Three transmission speeds, including neutral and reverse | `[-1,0,1,2,3]` |
| Five transmission speeds, including neutral and reverse | `[-1,0,1,2,3,4,5]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Transmission inertia
vector**, **Transmission damping vector**, and
**Efficiency vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `G` |
| **Values:** | `[-1, 0, 1, 2, 3, 4, 5]` (default) | `vector` |
| **Data Types:** | `double` |

### **Efficiency torque breakpoints, Trq\_bpts** — Breakpoints `[25, 50, 75, 100, 150, 200, 250]` (default) | `vector`

Torque breakpoints for efficiency table, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_bpts` |
| **Values:** | `[25, 50, 75, 100, 150, 200, 250]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.

### **Efficiency speed breakpoints, omega\_bpts** — Breakpoints `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `vector`

Speed breakpoints for efficiency table, rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_bpts` |
| **Values:** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.

### **Efficiency temperature breakpoints, Temp\_bpts** — Breakpoints `[313 358]` (default) | `vector`

Temperature breakpoints for efficiency table, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temp_bpts` |
| **Values:** | `[313 358]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.

### **Gear ratio vector, N** — Ratio of input speed to output speed `[-4.47, 1, 4.47, 2.47, 1.47, 1, 0.8]` (default) | `vector`

Vector of gear ratios (that is, input speed to output speed) with indices
corresponding to the ratios specified in **Gear number,
G**. For neutral, set the gear ratio to `1`. For
example, you can set these parameter values.

| To Specify Gear Ratios For | Set **Gear number, G** To | Set **Gear ratio, N** To |
| --- | --- | --- |
| Four transmission speeds, including neutral | `[0,1,2,3,4]` | `[1,4.47,2.47,1.47,1]` |
| Five transmission speeds, including neutral and reverse | `[-1,0,1,2,3,4,5]` | `[-4.47,1,4.47,2.47,1.47,1,0.8]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Transmission inertia
vector**, **Transmission damping vector**, and
**Efficiency vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N` |
| **Values:** | `[-4.47, 1, 4.47, 2.47, 1.47, 1, 0.8]` (default) | `vector` |
| **Data Types:** | `double` |

### **Transmission inertia vector, Jout** — Gear rotational inertia `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]` (default) | `vector`

Vector of gear rotational inertias, with indices corresponding to the
inertias specified in **Gear number, G**, in kg·m^2. For
example, you can set these parameter values.

| To Specify Inertia For | Set **Gear number, G** To | Set **Inertia, J** To |
| --- | --- | --- |
| Four gears, including neutral | `[0,1,2,3,4]` | `[0.01,2.28,2.04,0.32,0.028]` |
| Inertia for five gears, including reverse and neutral | `[-1,0,1,2,3,4,5]` | `[2.28,0.01,2.28,2.04,0.32,0.028,0.01]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Transmission inertia
vector**, **Transmission damping vector**, and
**Efficiency vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jout` |
| **Values:** | `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]` (default) | `vector` |
| **Data Types:** | `double` |

### **Transmission damping vector, bout** — Gear viscous damping coefficient `[.003 .001 .003 .0025 .002 .001 .001]` (default) | `vector`

Vector of gear viscous damping coefficients, with indices corresponding to
the coefficients specified in **Gear number, G**, in
N·m·s/rad. For example, you can set these parameter values.

| To Specify Damping For | Set **Gear number, G** To | Set **Damping, b** To |
| --- | --- | --- |
| Four gears, including neutral | `[0,1,2,3,4]` | `[0.001,0.003,0.0025, 0.002,0.001]` |
| Five gears, including reverse and neutral | `[-1,0,1,2,3,4,5]` | `[0.003,0.001,0.003, 0.0025,0.002,0.001,0.001]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Transmission inertia
vector**, **Transmission damping vector**, and
**Efficiency vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bout` |
| **Values:** | `[.003 .001 .003 .0025 .002 .001 .001]` (default) | `vector` |
| **Data Types:** | `double` |

### **Efficiency vector, eta** — Gear efficiency `[0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95]` (default) | `vector`

Vector of gear mechanical efficiency, with indices corresponding to the
efficiencies specified in **Gear number, G**. For example,
you can set these parameter values.

| To Specify Efficiency For | Set **Gear number, G** To | Set **Efficiency, eta** To |
| --- | --- | --- |
| Four gears, including neutral | `[0,1,2,3,4]` | `[0.9,0.9,0.9,0.9,0.95]` |
| Five gears, including reverse and neutral | `[-1,0,1,2,3,4,5]` | `[0.9,0.9,0.9, 0.9,0.9,0.95,0.95]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Transmission inertia
vector**, **Transmission damping vector**, and
**Efficiency vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta` |
| **Values:** | `[0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Gear only`.

### **Efficiency lookup table, eta\_tbl** — Gear efficiency `array`

Table of gear mechanical efficiency,
*ηN* as a function of gear,
input torque, input speed, and temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_tbl` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.

### **Initial output velocity, omegaout\_o** — Transmission `0` (default) | `scalar`

Transmission initial output rotational velocity,
*ωto*, in rad/s. If you
select **Start simulation with clutch locked**, the block
ignores the **Initial output velocity, omega\_o** parameter
value.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegaout_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial gear, G\_o** — Engaged gear `0` (default) | `scalar`

Initial gear to engage,
*Go*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `G_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Clutch and Synchronizer

### **Clutch pressure time constant, tauc** — Time `.02` (default) | `scalar`

Pressure input filter time constant,
*τc*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tauc` |
| **Values:** | `.02` (default) | `scalar` |
| **Data Types:** | `double` |

### **Synchronization time, ts** — Time `.25` (default) | `scalar`

Time required for gear selection and synchronization,
*ts*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ts` |
| **Values:** | `.25` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch time, tc** — Time `.5` (default) | `scalar`

Time required to engage and disengage the clutch during shift events,
*tc*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tc` |
| **Values:** | `.5` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Control type**
parameter `Ideal integrated controller`.

### **Effective clutch radius, R** — Radius `.2` (default) | `scalar`

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
| **Parameter:** | `R` |
| **Values:** | `.2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch force gain, K\_c** — Force `5e3` (default) | `scalar`

Open loop lock-up clutch gain,
*Kc*, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `K_c` |
| **Values:** | `5e3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch static friction coefficient, mus** — Coefficient `0.6` (default) | `scalar`

Dimensionless clutch disc coefficient of static friction,
*μs*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mus` |
| **Values:** | `0.6` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch kinematic friction coefficient, muk** — Coefficient `0.4` (default) | `scalar`

Dimensionless clutch disc coefficient of kinetic friction,
*μk*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `muk` |
| **Values:** | `0.4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Start simulation with clutch locked** — Select to initially lock clutch `off` (default) | `on`

Select to lock clutch initially.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `locked` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, select **Control type**
parameter `Ideal integrated controller`.

### **Start simulation with synchronizer locked** — Select to initially lock synchronizer `off` (default) | `on`

Select to initially lock synchronizer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ClutchLocked` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

## Libraries

Powertrain Blockset / Transmission / Transmission Systems

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Ideal automated manual transmission

The Automated Manual Transmission block implements
an ideal automated transmission (AMT). An AMT is a manual transmission
with additional actuators and an electronic control unit (ECU) to
regulate clutch and gear selection based on commands from a controller.
The number of gears is specified via an integer vector with corresponding
gear ratios, inertias, viscous damping, and efficiency factors. The
clutch and synchronization engagement rates are linear and adjustable.

Use the block for:

- Power and torque capacity sizing
- Determining gear ratio impact on fuel economy and
  performance

To determine the rotational drive shaft speed and reaction torque,
the Automated Manual Transmission block calculates:

- Clutch lock-up and clutch friction
- Locked rotational dynamics
- Unlocked rotational dynamics

To specify the block efficiency calculation, for **Efficiency factors**, select either of these options.

| Setting | Block Implementation |
| --- | --- |
| `Gear only` | Efficiency determined from a 1D lookup table that is a function of the gear. |
| `Gear, input torque, input speed, and temperature` | Efficiency determined from a 4D lookup table that is a function of:  - Gear - Input torque - Input speed - Oil temperature |

### Clutch Control

The AMT delivers drive shaft torque continuously by controlling
the pressure signals from the clutch. If you select **Control
type** parameter `Ideal integrated controller`,
the block generates idealized clutch pressure signals. To use your
own clutch control signals, select **Control type** parameter `External
control`.

### Clutch Lock-Up and Clutch Friction

Based on the clutch lock-up condition, the block implements
one of these friction models.

| If | Clutch Condition | Friction Model |
| --- | --- | --- |
| ωi≠NωdorTS<|Tf−Nwibi| | Unlocked | Tf=Tkwhere,Tk=FcReffμktanh[4(wiN−wd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) |
| ωi=NωtandTS≥|Tf−Nbiωi| | Locked | *Tf* = *Ts* |

The equations use these variables.

|  |  |
| --- | --- |
| *ωt* | Output drive shaft speed |
| *ωi* | Input drive shaft speed |
| *ωd* | Drive shaft speed |
| bi | Viscous damping |
| *Fc* | Applied clutch force |
| *N* | Engaged gear |
| Tf | Frictional torque |
| Tk | Kinetic frictional torque |
| Ts | Static frictional torque |
| Reff | Effective clutch radius |
| Ro | Annular disk outer radius |
| Ri | Annular disk inner radius |
| *μs* | Coefficient of static friction |
| *μk* | Coefficient of kinetic friction |

### Locked Rotational Dynamics

To model the rotational dynamics when the clutch is locked,
the block implements these equations.

ω˙dJN=ηNTd−ωiNbN+NTiωi=Nωd

The block determines the input torque, *Ti*,
through differentiation.

The equations use these variables.

|  |  |
| --- | --- |
| *ωi* | Input drive shaft speed |
| *ωd* | Drive shaft speed |
| *N* | Engaged gear |
| *bN* | Engaged gear viscous damping |
| *JN* | Engaged gear inertia |
| *ηN* | Engaged gear efficiency |
| *Td* | Drive shaft torque |
| *Ti* | Applied input torque |

### Unlocked Rotational Dynamics

To model the rotational dynamics when the clutch is unlocked, the block implements this
equation.

ω˙dJN=NTf−ωdbN+Td

where:

|  |  |
| --- | --- |
| *ωd* | Drive shaft speed |
| *N* | Engaged gear |
| *bN* | Engaged gear viscous damping |
| *JN* | Engaged gear inertia |
| *Td* | Drive shaft torque |
| *Ti* | Applied input torque |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrEng` | Engine power | *Peng* | ωiTi |
| `PwrDiffrntl` | Differential power | *Pdiff* | ωdTd |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrEffLoss` | Mechanical power loss | *Peffloss* | ωdTd(ηN−1) |
| `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | −bNωd2 −binωi2 |
| `PwrCltchLoss` | Clutch power loss | *Pmech* | When locked: 0  When unlocked: −Tk(ωi−Nωd) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredTrans` | Rate change in rotational kinetic energy | *Pstr* | When locked: ω˙iωi(Jin+JNN2)  When unlocked: Jinω˙iωi+JNω˙dωd |

The equations use these variables.

|  |  |
| --- | --- |
| *bN* | Engaged gear viscous damping |
| *JN* | Engaged gear rotational inertia |
| *Jin* | Flywheel rotational inertia |
| *ηN* | Engaged gear efficiency |
| *N* | Engaged gear ratio |
| *Ti* | Applied input torque, typically from the engine crankshaft or dual mass flywheel damper |
| *Td* | Applied load torque, typically from the differential or drive shaft |
| *ωd* | Initial input drive shaft rotational velocity |
| *ωi*, *ώi* | Applied drive shaft angular speed and acceleration |
