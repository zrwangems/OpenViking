---
type: simulink-block
title: 'Estimation Equivalent Circuit Battery'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'estimationequivalentcircuitbattery'
documentation_source_path: 'ref/estimationequivalentcircuitbattery.html'
language: en
---

# Estimation Equivalent Circuit Battery

## Ports

### Inputs

### **BattCurr** — Battery network current `scalar`

Combined current flowing from the battery network,
*Iin*, in A.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | Description | Variable | Units |
| --- | --- | --- | --- |
| `CapVolt` | Voltage for *`n`*-th RC pair | *Vn* | V |

### **BattVolt** — Battery output voltage `scalar`

Combined voltage of the battery network, *Vout*,
in V.

### **BattSoc** — Battery SOC `scalar`

Battery state-of-charge, *SOC*.

## Parameters

#### Core Battery

### **Number of series RC pairs** — RC pairs `1` (default) | `2` | `3` | `4` | `5`

Number of series RC pairs. For lithium, typically 1 or 2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumRC` |
| **Values:** | `1` (default) | `2` | `3` | `4` | `5` |
| **Data Types:** | `double` |

### **Open circuit voltage Em table data, Em** — Voltage table `[3.8 3.8 3.8 3.8 3.8 3.8]` (default) | `array`

Open-circuit voltage table, *Em*,
in V. Function of SOC.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Em` |
| **Values:** | `[3.8 3.8 3.8 3.8 3.8 3.8]` (default) | `array` |
| **Data Types:** | `double` |

### **Series resistance table data, R0** — Resistance `[0.01 0.01 0.01 0.01 0.01 0.01]` (default) | `array`

Series resistance table, *Ro*, in
ohms. Function of SOC.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R0` |
| **Values:** | `[0.01 0.01 0.01 0.01 0.01 0.01]` (default) | `array` |
| **Data Types:** | `double` |

### **State of charge breakpoints, SOC\_BP** — SOC breakpoints `[0 .2 .4 .6 .8 1]` (default) | `vector`

State-of-charge (SOC) breakpoints, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOC_BP` |
| **Values:** | `[0 .2 .4 .6 .8 1]` (default) | `vector` |
| **Data Types:** | `double` |

### **Battery capacity, BattCap** — Capacity `27.6250` (default) | `scalar`

Battery capacity, *Cbatt*, in
Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattCap` |
| **Values:** | `27.6250` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial battery capacity, BattCapInit** — Capacity `27.6250` (default) | `scalar`

Initial battery capacity,
*Cbatto*, in Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattCapInit` |
| **Values:** | `27.6250` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial capacitor voltage, InitialCapVoltage** — Voltage `0` (default) | `vector`

Initial capacitor voltage, in V. Dimension of vector must equal
the **Number of series RC pairs**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialCapVoltage` |
| **Values:** | `0` (default) | `vector` |
| **Data Types:** | `double` |

#### R and C Table Data

### **Network resistance table data, R*`n`*** — Lookup table `[0.005 0.005 0.005 0.005 0.005 0.005]` (default) | `array`

Network resistance table data for *`n`*-th RC pair,
as a function of SOC, in ohms.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R` |
| **Values:** | `[0.005 0.005 0.005 0.005 0.005 0.005]` (default) | `array` |
| **Data Types:** | `double` |

### **Network capacitance table data, C*`n`*** — Lookup table `[10000 10000 10000 10000 10000 10000]` (default) | `array`

Network capacitance table data for *`n`*-th RC
pair, as a function of SOC, in F.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `C` |
| **Values:** | `[10000 10000 10000 10000 10000 10000]` (default) | `array` |
| **Data Types:** | `double` |

#### Cell Limits

### **Upper Integrator Voltage Limit, Vu** — Maximum `Inf` (default) | `scalar`

Upper voltage limit, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vu` |
| **Values:** | `Inf` (default) | `scalar` |
| **Data Types:** | `double` |

### **Lower Integrator Voltage Limit, Vl** — Minimum `Inf` (default) | `scalar`

Lower voltage limit, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vl` |
| **Values:** | `Inf` (default) | `scalar` |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Energy Storage and Auxiliary Drive / Network Battery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Resistor-capacitor (RC) circuit battery that determines combined voltage using lookup tables

The Estimation Equivalent Circuit Battery block implements a resistor-capacitor
(RC) circuit battery model that determines the combined voltage of a network battery
using parameter lookup tables. The tables are functions of the state-of-charge (SOC).
Consider using the block for estimating battery voltage and SOC, not in system-level
models.

To acquire the SOC, the block integrates the charge and discharge currents. The block
implements these values as lookup tables that are functions of the SOC:

- Series resistance,
  *Ro*=ƒ(*SOC*)
- Battery open-circuit voltage,
  *Em*=ƒ(*SOC*)
- Network resistance,
  *Rn*=ƒ(*SOC*)
- Network capacitance,
  *Cn*=ƒ(*SOC*)

To calculate the combined voltage of the battery network, the
block uses these equations.

VT=Em−IbattRo−∑1nVnVn=∫0t[IbattCn−VnRnCn]dtSOC=−1Cbatt∫0tIbattdtIbatt=IinVout=VT

Positive
current indicates battery discharge. Negative current indicates battery
charge.

The equations use these variables.

|  |  |
| --- | --- |
| *SOC* | State-of-charge |
| *Em* | Battery open-circuit voltage |
| *Ibatt* | Per module battery current |
| *Iin* | Combined current flowing from the battery network |
| *Ro* | Series resistance |
| *n* | Number of RC pairs in series |
| *Vout*, *VT* | Combined voltage of the battery network |
| *Vn* | Voltage for *`n`*-th RC pair |
| *Rn* | Resistance for *`n`*-th RC pair |
| *Cn* | Capacitance for *`n`*-th RC pair |
| *Cbatt* | Battery capacity |
