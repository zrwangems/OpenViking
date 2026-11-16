---
type: simulink-block
title: 'Equivalent Consumption Minimization Strategy'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Supervisory Controllers'
documentation_page: 'equivalentconsumptionminimizationstrategy'
documentation_source_path: 'ref/equivalentconsumptionminimizationstrategy.html'
language: en
---

# Equivalent Consumption Minimization Strategy

## Ports

### Input

### **WhlTrqCmd** — Wheel torque command `scalar`

Wheel torque command.

**Data Types:** `double`

### **BattSoc** — Battery state of charge `scalar`

Battery state of charge.

**Data Types:** `double`

### **BattVolt** — Battery voltage `scalar`

Battery voltage.

**Data Types:** `double`

### **Gear** — Transmission gear `scalar`

Transmission gear.

**Data Types:** `double`

### **MtrSpd** — Motor speed `scalar`

Motor speed.

**Data Types:** `double`

### **VehSpd** — Vehicle speed `scalar`

Vehicle speed, in m/s.

**Data Types:** `double`

### **TransTemp** — Transmission temperature `scalar`

Transmission temperature, in K.

**Data Types:** `double`
### Output

### **Info** — Block data bus

Block data, returned as a bus signal that contains these block
values.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `EngTrqCmd` | | | Engine torque command | N·m |
| `MtrTrqCmd` | | | Motor torque command | N·m |
| `EquivFctr` | | | Equivalence factor | NA |
| `MinHamil` | | | Minimum Hamiltonian | kW |

### **EngTrqCmd** — Engine torque command `scalar`

Engine torque command, in N·m.

**Data Types:** `double`

### **MtrTrqCmd** — Motor torque command `scalar`

Motor torque command, in N·m.

**Data Types:** `double`

## Parameters

#### Block Options

### **Motor location** — Location of motor `P0` (default) | `P1` | `P2` | `P3` | `P4`

Specify the HEV motor location.

### **ECMS method** — ECMS method `Non-adaptive` (default) | `Adaptive`

Use the **ECMS method** parameter to implement
either an adaptive or non-adaptive ECMS method. The HEV architectures are charge-sustaining,
meaning the battery SOC must remain in a specified range because there is no plugin capability
to recharge the battery. The battery is an energy buffer, and all energy comes from the fuel if
the change in SOC is minimized over a drive cycle. To sustain the charge over a specified drive
cycle, the block implements either of these ECMS methods.

| ECMS Method | Description |
| --- | --- |
| `Non-adaptive` (default) | The block uses a constant ECMS equivalence factor.  - Use this method to determine the best fuel economy over a   drive cycle.  - If you change the drive cycle or HEV     architecture, retune the **ECMS weighting     factor** to maintain the ending     SOC. - By default, the block uses a single constant. |
| `Adaptive` | The block adjusts an ECMS equivalence factor by using the output of a PI controller.  - Use this method to maintain the SOC and minimize the delta   SOC over many drive cycles. The block:  - Tunes the PI controller gains.   - Sustains the SOC. - The PI controller minimizes the error between the target   SOC and current SOC. |

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EcmsMethod` |
| **Values:** | `Non-adaptive` (default) | `Adaptive` |
| **Data Types:** | `character vector` |

#### Differential

### **Differential gear ratio, N\_diff** — Differential gear ratio `3.32` (default) | `scalar`

Differential gear ratio. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_diff` |
| **Values:** | `3.32` (default) | `scalar` |
| **Data Types:** | `double` |

### **Differential efficiency factor, eta\_diff** — Differential efficiency factor `0.98` (default) | `scalar`

Differential efficiency factor. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_diff` |
| **Values:** | `0.98` (default) | `scalar` |
| **Data Types:** | `double` |

### **Loaded wheel radius, Re** — Loaded wheel radius `0.327` (default) | `scalar`

Loaded wheel radius, in m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Re` |
| **Values:** | `0.327` (default) | `scalar` |
| **Data Types:** | `double` |

#### Transmission

### **Transmission efficiency factors** — Transmission efficiency factors `Gear, input torque, input speed, and temperature` (default) | `Gear only`

Transmission efficiency factors.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TransEffFactors` |
| **Values:** | `Gear, input torque, input speed, and temperature` (default) | `Gear only` |
| **Data Types:** | `character vector` |

### **Transmission gear number vector, G\_trans** — Transmission gear number vector `[0 1 2 3 4 5 6]` (default) | `vector`

Transmission gear number vector. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `G_trans` |
| **Values:** | `[0 1 2 3 4 5 6]` (default) | `vector` |
| **Data Types:** | `double` |

### **Transmission gear ratio vector, N\_trans** — Transmission gear ratio vector `[1 4.212 2.637 1.8 1.386 1 0.772]` (default) | `vector`

Transmission gear ratio vector. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_trans` |
| **Values:** | `[1 4.212 2.637 1.8 1.386 1 0.772]` (default) | `vector` |
| **Data Types:** | `double` |

### **Transmission efficiency vector, eta\_trans** — Transmission efficiency vector `[1 1 1 1 1 1 1]` (default) | `vector`

Transmission efficiency vector. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_trans` |
| **Values:** | `[1 1 1 1 1 1 1]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Transmission efficiency factors**
to `Gear only`.

### **Transmission efficiency torque breakpoints, Trq\_trans\_bpts** — Transmission efficiency torque breakpoints `[25 50 75 100 150 200 250]` (default) | `vector`

Transmission efficiency torque breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_trans_bpts` |
| **Values:** | `[25 50 75 100 150 200 250]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Transmission efficiency factors** to
`Gear, input torque, input speed, and temperature`.

### **Transmission efficiency speed breakpoints, omega\_trans\_bpts** — Transmission efficiency speed breakpoints `[500.383141080919 749.619781962827 1002.676141478941 1250.957852702297 1499.239563925654 1747.521275149011 1995.802986372368 2501.915705404595 2998.479127851308 4001.155269330249 5003.83141080919]` (default) | `vector`

Transmission efficiency speed breakpoints, in rad/s.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_trans_bpts` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Transmission efficiency factors** to
`Gear, input torque, input speed, and temperature`.

### **Transmission efficiency temperature breakpoints, Temp\_trans\_bpts** — Transmission efficiency temperature breakpoints `[313 358]` (default) | `vector`

Transmission efficiency temperature breakpoints, in K.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temp_trans_bpts` |
| **Values:** | `[313 358]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Transmission efficiency factors** to
`Gear, input torque, input speed, and temperature`.

### **Transmission efficiency vector, eta\_trans\_tbl** — Transmission efficiency vector `array`

Transmission efficiency vector. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_trans_tbl` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Transmission efficiency factors** to
`Gear, input torque, input speed, and temperature`.

#### Engine

### **Speed breakpoints, f\_tbrake\_n\_bpt** — Speed breakpoints `[0 750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector`

Speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Commanded torque breakpoints, f\_tbrake\_t\_bpt** — Commanded torque breakpoints `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]` (default) | `vector`

Commanded torque breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_t_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Brake torque map, f\_tbrake** — Brake torque map `array`

Brake torque map, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Minimum engine torque command table, f\_tbrake\_min** — Minimum engine torque command table `vector`

Minimum engine torque command table, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_min` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Fuel flow map, f\_fuel** — Fuel flow map `array`

Fuel flow map, in kg/s.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_fuel` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Minimum engine torque command, HEVEngTrq\_min** — Minimum engine torque command `16.18610438796213` (default) | `scalar`

Minimum engine torque command, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `HEVEngTrq_min` |
| **Values:** | `16.18610438796213` (default) | `scalar` |
| **Data Types:** | `double` |

### **Fuel lower heating value, LHV** — Fuel lower heating value `46000000` (default) | `scalar`

Fuel lower heating value, in J/kg.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LHV` |
| **Values:** | `46000000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Engine idle speed, N\_idle** — Engine idle speed `750` (default) | `scalar`

Engine idle speed, in rpm.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_idle` |
| **Values:** | `750` (default) | `scalar` |
| **Data Types:** | `double` |

#### Battery

### **Battery state-of-charge breakpoints, SOC\_bpt** — Battery state-of-charge breakpoints `[0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1]` (default) | `vector`

Battery state-of-charge breakpoints. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOC_bpt` |
| **Values:** | `[0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1]` (default) | `vector` |
| **Data Types:** | `double` |

### **Battery charge limit table, ChrgLmt** — Battery charge limit table `[1 1 1 1 1 1 1 0.9 0.7 0.5 0]` (default) | `vector`

Battery charge limit table. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ChrgLmt` |
| **Values:** | `[1 1 1 1 1 1 1 0.9 0.7 0.5 0]` (default) | `vector` |
| **Data Types:** | `double` |

### **Battery discharge limit table, DischrgLmt** — Battery discharge limit table `[0 0.5 0.7 0.9 1 1 1 1 1 1 1]` (default) | `vector`

Battery discharge limit table. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DischrgLmt` |
| **Values:** | `[0 0.5 0.7 0.9 1 1 1 1 1 1 1]` (default) | `vector` |
| **Data Types:** | `double` |

### **Maximum battery current, BattCurrMax** — Maximum battery current `150` (default) | `scalar`

Maximum battery current, in A.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattCurrMax` |
| **Values:** | `150` (default) | `scalar` |
| **Data Types:** | `double` |

### **DC/DC converter efficiency, eta\_dcdc** — DC/DC converter efficiency `1` (default) | `scalar`

DC/DC converter efficiency. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_dcdc` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Maximum battery charge power, BattChrgPwrMax** — Maximum battery charge power `-30000` (default) | `scalar`

Maximum battery charge power, in W.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattChrgPwrMax` |
| **Values:** | `-30000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Maximum battery discharge power, BattDischrgPwrMax** — Maximum battery discharge power `46000` (default) | `scalar`

Maximum battery discharge power, in W.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattDischrgPwrMax` |
| **Values:** | `46000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Motor

### **Motor maximum torque table, f\_tmtr\_max** — Motor maximum torque table `vector`

Motor maximum torque table, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tmtr_max` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Motor speed breakpoints, f\_mtr\_w\_bpt** — Motor speed breakpoints `vector`

Motor speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mtr_w_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Motor torque breakpoints, f\_mtr\_t\_bpt** — Motor torque breakpoints `vector`

Motor torque breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mtr_t_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Motor efficiency map, f\_mtr\_eta** — Motor efficiency map `array`

Motor efficiency map. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mtr_eta` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Number of motor torque calculation points, Ngrid** — Number of motor torque calculation points `200` (default) | `scalar`

Number of motor torque calculation points. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ngrid` |
| **Values:** | `200` (default) | `scalar` |
| **Data Types:** | `double` |

### **P0 belt ratio, N\_P0** — P0 belt ratio `3` (default) | `scalar`

P0 belt ratio. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_P0` |
| **Values:** | `3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Motor location** to
`P0`.

#### Energy Management

### **ECMS weighting factor, ECMS\_s** — ECMS weighting factor `3.385` (default) | `scalar`

ECMS weighting factor. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ECMS_s` |
| **Values:** | `3.385` (default) | `scalar` |
| **Data Types:** | `double` |

### **Penalty factor power, a** — Penalty factor power `3` (default) | `scalar`

Penalty factor power. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PenaltyFctrPwr` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Adaptive ECMS proportional gain, ECMS\_Kp** — Adaptive ECMS proportional gain `0` (default) | `scalar`

Adaptive ECMS proportional gain. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ECMS_Kp` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **ECMS method** to
`Adaptive`.

### **Adaptive ECMS integral gain, ECMS\_Ki** — Adaptive ECMS integral gain `0` (default) | `scalar`

Adaptive ECMS integral gain. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ECMS_Ki` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **ECMS method** to
`Adaptive`.

### **Constraint penalty factor, PenaltyFctr** — Constraint penalty factor `10000000` (default) | `scalar`

Constraint penalty factor. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PenaltyFctr` |
| **Values:** | `10000000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Target battery state-of-charge, SOCTrgt** — Target battery state-of-charge `60` (default) | `scalar`

Target battery state-of-charge. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOCTrgt` |
| **Values:** | `60` (default) | `scalar` |
| **Data Types:** | `double` |

### **Minimum battery state-of-charge, SOCmin** — Minimum battery state-of-charge `40` (default) | `scalar`

Minimum battery state-of-charge. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOCmin` |
| **Values:** | `40` (default) | `scalar` |
| **Data Types:** | `double` |

### **Maximum battery state-of-charge, SOCmax** — Maximum battery state-of-charge `80` (default) | `scalar`

Maximum battery state-of-charge. No dimension.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOCmax` |
| **Values:** | `80` (default) | `scalar` |
| **Data Types:** | `double` |

### Acknowledgments

MathWorks® would like to acknowledge the contribution of Dr. Simona Onori to the ECMS
optimal control algorithm implemented in this block. Dr. Onori is a Professor of Energy
Resources Engineering at Stanford University. Her research interests include electrochemical
modeling, estimation and optimization of energy storage devices for automotive and
grid-level applications, hybrid and electric vehicles modeling and control, PDE modeling,
and model-order reduction and estimation of emission mitigation systems. She is a senior
member of IEEE®.

## Libraries

Powertrain Blockset / Propulsion / Supervisory Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Energy management controller for P0–P4 hybrid electric vehicles

Use the Equivalent Consumption Minimization Strategy (ECMS) block to
control the energy management of hybrid electric vehicles (HEVs). The block optimizes the
torque split between the engine and motor to minimize energy consumption while maintaining the
battery state of charge (SOC).

The HEV P0, P1, P2, P3, and P4 reference applications use the Equivalent
Consumption Minimization Strategy block for hybrid control.

Use the **Motor location** parameter to specify the HEV motor location.

Use the **ECMS method** parameter to implement
either an adaptive or non-adaptive ECMS method. The HEV architectures are charge-sustaining,
meaning the battery SOC must remain in a specified range because there is no plugin capability
to recharge the battery. The battery is an energy buffer, and all energy comes from the fuel if
the change in SOC is minimized over a drive cycle. To sustain the charge over a specified drive
cycle, the block implements either of these ECMS methods.

| ECMS Method | Description |
| --- | --- |
| `Non-adaptive` (default) | The block uses a constant ECMS equivalence factor.  - Use this method to determine the best fuel economy over a   drive cycle.  - If you change the drive cycle or HEV     architecture, retune the **ECMS weighting     factor** to maintain the ending     SOC. - By default, the block uses a single constant. |
| `Adaptive` | The block adjusts an ECMS equivalence factor by using the output of a PI controller.  - Use this method to maintain the SOC and minimize the delta   SOC over many drive cycles. The block:  - Tunes the PI controller gains.   - Sustains the SOC. - The PI controller minimizes the error between the target   SOC and current SOC. |

### ECMS Control Algorithm

The block implements a dynamic supervisory controller that determines the engine torque,
motor torque, starter, clutch, and brake pressure commands. Specifically, the block:

- Converts the driver accelerator pedal signal to a wheel torque request. To
  calculate the total powertrain torque at the wheels, the algorithm uses the maximum
  engine torque and motor torque curves and the transmission and differential gear
  ratios.
- Converts the driver brake pedal signal to a brake pressure request. The algorithm
  multiplies the brake pedal signal by a maximum brake pressure.
- Implements a regenerative braking algorithm for the traction motor to recover the
  maximum amount of kinetic energy from the vehicle.

  The block implements an ECMS algorithm[2]
  that optimizes the torque split between the engine and motor to minimize energy
  consumption while maintaining the battery SOC. Specifically, the ECMS:

  - Assigns a cost to electrical energy, so that using stored electrical energy
    is equal to consuming fuel energy.

    | Battery Mode | Equivalent Electrical Energy | Description |
    | --- | --- | --- |
    | Discharging | Positive | Battery discharges stored electrical energy when the electric machine is in use. |
    | Charging | Negative | Battery stores electrical energy from either the:  - Engine and electric machine acting as a generator - Electric machine acting as a generator during regenerative   braking |
  - Is an instantaneous minimization method that the software solves at every
    controller time step. To implement the strategy, the ECMS selects the optimal
    motor and engine torque in the optimization strategy to minimize the equivalent
    energy consumption.
  - Implements either an adaptive or non-adaptive ECMS method.
