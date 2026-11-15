---
type: simulink-block
title: 'Ideal Fixed Gear Transmission'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain and Transmission / Transmission – Systems and Converters'
documentation_page: 'idealfixedgeartransmission'
documentation_source_path: 'ref/idealfixedgeartransmission.html'
language: en
---

# Ideal Fixed Gear Transmission

## Ports

### Inputs

### **Gear** — Gear number to engage `scalar`

Integer value of gear number to engage,
*Gcmd*.

### **EngTrq** — Applied input torque `scalar`

Applied input torque, *Ti*,
typically from the engine crankshaft or dual mass flywheel damper, in
N·m.

### **DiffTrq** — Applied load torque `scalar`

Applied load torque, *To*,
typically from the differential, in N·m.

### **Temp** — Oil temperature `scalar`

Oil temperature, in K. To determine the efficiency, the block uses a
4D lookup table that is a function of:

- Gear
- Input torque
- Input speed
- Oil temperature

#### Dependencies

To enable this port, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `Eng` | `EngTrq` | | Applied input torque, typically from the engine crankshaft or dual mass flywheel damper | *Ti* | N·m |
| `EngSpd` | | Applied drive shaft angular speed input | *ωi* | rad/s |
| `Diff` | `DiffTrq` | | Applied load torque, typically from the differential | *To* | N·m |
| `DiffSpd` | | Drive shaft angular speed output | *ωo* | rad/s |
| `Trans` | `TransSpdRatio` | | Input to output speed ratio at time t | *Φ(t)* | N/A |
| `TransEta` | | Ratio of output power to input power | *ηN* | N/A |
| `TransGearCmd` | | Commanded gear | *Ncmd* | N/A |
| `TransGear` | | Engaged gear | *N* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | Engine power | *Peng* | W |
| `PwrDiffrntl` | Differential power | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrEffLoss` | Mechanical power loss | *Peffloss* | W |
| `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | W |
| `PwrStored` | `PwrStoredTrans` | Rate change in rotational kinetic energy | *Pstr* | W |

### **EngSpd** — Angular speed `scalar`

Applied drive shaft angular speed input,
*ωi*, in rad/s.

### **DiffSpd** — Angular speed `scalar`

Drive shaft angular speed output,
*ωo*, in rad/s.

## Parameters

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

### **Gear property interpolation method** — Interpolation `Nearest` (default) | `Linear` | `Flat` | `Cubic spline`

Method that the block uses to switch the gear ratio during gear
shifting.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `gearInterp` |
| **Values:** | `Nearest` (default) | `Linear` | `Flat` | `Cubic spline` |
| **Data Types:** | `character vector` |

#### Transmission

### **Gear number vector, G** — Specify number of transmission speeds `[-1,0,1,2,3,4,5]` (default) | `vector`

Vector of integer gear commands used to specify the number of transmission
speeds. Neutral gear is `0`. For example, you can set these
parameter values.

| To Specify | Set **Gear number, G** To |
| --- | --- |
| Four transmission speeds, including neutral | `[0,1,2,3,4]` |
| Three transmission speeds, including neutral and reverse | `[-1,0,1,2,3]` |
| Five transmission speeds, including neutral and reverse | `[-1,0,1,2,3,4,5]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Inertia
vector**, **Damping vector**, and **Efficiency
vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `G` |
| **Values:** | `[-1,0,1,2,3,4,5]` (default) | `vector` |
| **Data Types:** | `double` |

### **Efficiency torque breakpoints, Trq\_bpts** — Breakpoints `[25,50,75,100,150,200,250]` (default) | `vector`

Torque breakpoints for efficiency table.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_bpts` |
| **Values:** | `[25,50,75,100,150,200,250]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Gear, input torque, input speed, and
temperature`.

### **Efficiency speed breakpoints, omega\_bpts** — Breakpoints `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `vector`

Speed breakpoints for efficiency table, in rad/s.

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

Temperature breakpoints for efficiency table.

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

### **Gear ratio vector, N** — Ratio of input speed to output speed `[-4.47,4.47,4.47,2.47,1.47,1,0.8]` (default) | `vector`

Vector of gear ratios (that is, input speed to output speed) with indices
corresponding to the ratios specified in **Gear number,
G**. For neutral, set the gear ratio to `1`. For
example, you can set these parameter values.

| To Specify Gear Ratios For | Set **Gear number, G** To | Set **Gear ratio, N** To |
| --- | --- | --- |
| Four transmission speeds, including neutral | `[0,1,2,3,4]` | `[1,4.47,2.47,1.47,1]` |
| Five transmission speeds, including neutral and reverse | `[-1,0,1,2,3,4,5]` | `[-4.47,1,4.47,2.47, 1.47,1,0.8]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Inertia
vector**, **Damping vector**, and **Efficiency
vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N` |
| **Values:** | `[-4.47,4.47,4.47,2.47,1.47,1,0.8]` (default) | `vector` |
| **Data Types:** | `double` |

### **Inertia vector, Jout** — Gear rotational inertia `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]` (default) | `vector`

Vector of gear rotational inertias,
*JN*, with indices corresponding
to the inertias specified in **Gear number, G**, in kg\*m^2.
For example, you can set these parameter values.

| To Specify Inertia For | Set **Gear number, G** To | Set **Inertia, J** To |
| --- | --- | --- |
| Four gears, including neutral | `[0,1,2,3,4]` | `[0.01,2.28,2.04, 0.32,0.028]` |
| Inertia for five gears, including reverse and neutral | `[-1,0,1,2,3,4,5]` | `[2.28,0.01,2.28, 2.04,0.32,0.028,0.01]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Inertia
vector**, **Damping vector**, and **Efficiency
vector** parameters must be equal.

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

### **Damping vector, bout** — Gear viscous damping coefficient `[.003 .001 .003 .0025 .002 .001 .001]` (default) | `vector`

Vector of gear viscous damping coefficients,
*bN*, with indices
corresponding to the coefficients specified in **Gear number,
G**, in N·m·s/rad. For example, you can set these parameter
values.

| To Specify Damping For | Set **Gear number, G** To | Set **Damping, b** To |
| --- | --- | --- |
| Four gears, including neutral | `[0,1,2,3,4]` | `[0.001,0.003, 0.0025,0.002,0.001]` |
| Five gears, including reverse and neutral | `[-1,0,1,2,3,4,5]` | `[0.003,0.001, 0.003,0.0025, 0.002,0.001,0.001]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Inertia
vector**, **Damping vector**, and **Efficiency
vector** parameters must be equal.

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

### **Efficiency vector, eta** — Gear efficiency `[0.9,0.9,0.9,0.9,0.9,0.95,0.95]` (default) | `vector`

Vector of gear mechanical efficiency,
*ηN*, with indices corresponding
to the efficiencies specified in **Gear number, G**. For
example, you can set these parameter values.

| To Specify Efficiency For | Set **Gear number, G** To | Set **Efficiency, eta** To |
| --- | --- | --- |
| Four gears, including neutral | `[0,1,2,3,4]` | `[0.9,0.9,0.9,0.9,0.95]` |
| Five gears, including reverse and neutral | `[-1,0,1,2,3,4,5]` | `[0.9,0.9,0.9, 0.9,0.9,0.95,0.95]` |

Vector dimensions for the **Gear number
vector**, **Gear ratio vector**, **Inertia
vector**, **Damping vector**, and **Efficiency
vector** parameters must be equal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta` |
| **Values:** | `[0.9,0.9,0.9,0.9,0.9,0.95,0.95]` (default) | `vector` |
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

### **Initial gear number, G\_o** — Gear `0` (default) | `scalar`

Initial gear number,
*Go*, dimensionless.

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

### **Initial output velocity, omega\_o** — Output speed `0` (default) | `scalar`

Transmission initial output rotational velocity,
*ωo*, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial neutral input velocity, omegainN\_o** — Neutral gear input speed `0` (default) | `scalar`

Initial neutral gear input rotational velocity,
*ωNo*, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegainN_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Shift time constant, tau\_s** — Time `.01` (default) | `scalar`

Shift time constant, *τs*, in
s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau_s` |
| **Values:** | `.01` (default) | `scalar` |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Transmission / Transmission Systems Vehicle Dynamics Blockset / Powertrain / Transmission

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Ideal fixed gear transmission without clutch or synchronization

The Ideal Fixed Gear Transmission implements an idealized fixed-gear
transmission without a clutch or synchronization. Use the block to model the overall
gear ratio and power loss when you do not need a detailed transmission model, for
example, in component-sizing, fuel economy, and emission studies. The block implements a
transmission model with minimal parameterization or computational cost.

To specify the block efficiency calculation, for **Efficiency factors**, select either of these options.

| Setting | Block Implementation |
| --- | --- |
| `Gear only` | Efficiency determined from a 1D lookup table that is a function of the gear. |
| `Gear, input torque, input speed, and temperature` | Efficiency determined from a 4D lookup table that is a function of:  - Gear - Input torque - Input speed - Oil temperature |

The block uses this equation to determine the transmission dynamics:

ω˙iJNN2=ηN(ToN+Ti)−ωiN2bNωi=Nωo

The block filters the gear command signal:

GGcmd(s)=1τss+1

### Neutral Gear

When **Initial gear number, G\_o** is equal to
`0`, the initial gear is neutral. The block uses these
parameters to decouple the input flywheel from the downstream gearing.

- **Initial input velocity, omega\_o**
- **Initial neutral input velocity,
  omegainN\_o**

The block uses these equations for the neutral gear speed and flywheel.

ω˙neutralJNN2=ηNToN−ωneutralN2bNωneutral=Nωo

ω˙1JF=η@N=0Ti−b@N=0ωiJF=J@N=1−J@N=0

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrEng` | Engine power | *Peng* | ωiTi |
| `PwrDiffrntl` | Differential power | *Pdiff* | ωoTo |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrEffLoss` | Mechanical power loss | *Peffloss* | ωoTo(ηN−1) |
| `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | For  G=0:     −bNωi2|N2|For  G≠0:  −bNωi2 −bNωneutral2|N2| |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredTrans` | Rate change in rotational kinetic energy | *Pstr* | For  G=0:     JNN2ω˙iωiFor  G≠0:   JFω˙iωi+JNN2ω˙neutralωneutral |

The equations use these variables.

|  |  |
| --- | --- |
| *bN* | Engaged gear viscous damping |
| *JN* | Engaged gear rotational inertia |
| *JF* | Flywheel rotational inertia |
| *ηN* | Engaged gear efficiency |
| *G* | Engaged gear number |
| *Gcmd* | Gear number to engage |
| *N* | Engaged gear ratio |
| *Ti* | Applied input torque, typically from the engine crankshaft or dual mass flywheel damper |
| *To* | Applied load torque, typically from the differential or drive shaft |
| *ωo* | Initial input drive shaft rotational velocity |
| *ωi*, *ώi* | Applied drive shaft angular speed and acceleration |
| *ωNo* | Initial neutral gear input rotational velocity |
| *ωneutral* | Neutral gear drive shaft rotational velocity |
| *τs* | Shift time constant |
