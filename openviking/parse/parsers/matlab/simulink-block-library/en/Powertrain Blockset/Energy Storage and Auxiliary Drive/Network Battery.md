---
type: simulink-block
title: 'Datasheet Battery'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage and Auxiliary Drive'
documentation_page: 'datasheetbattery'
documentation_source_path: 'ref/datasheetbattery.html'
language: en
---

# Datasheet Battery

## Ports
```yaml
ports:
- name: CapInit
  summary: Battery capacity scalar
  direction: input
- name: BattCurr
  summary: Battery load current scalar
  direction: input
- name: BattTemp
  summary: Battery temperature scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: BattVolt
  summary: Battery output voltage scalar
  direction: output
```

### Inputs

### **CapInit** — Battery capacity `scalar`

Rated battery capacity at the nominal temperature,
*Capbatt*, in Ah.

#### Dependencies

To create this port, select `External
Input` for the **Initial battery
capacity** parameter.

### **BattCurr** — Battery load current `scalar`

Combined current flowing from the battery network,
*Iin*, in A.

### **BattTemp** — Battery temperature `scalar`

Temperature measured at the battery housing, *T*,
in K.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `BattCurr` | | | Combined current flowing from the battery network | *Ibatt* | A |
| `BattAmpHr` | | | Battery energy | *LdAmpHr* | A\*h |
| `BattSoc` | | | State-of-charge capacity | *SOC* | NA |
| `BattVolt` | | | Combined voltage of the battery network | *Vout* | V |
| `BattPwr` | | | Battery network power | *Pbatt* | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrLdBatt` | Battery network power | *PLdBatt* | W |
| `PwrNotTrnsfrd` | `PwrLossBatt` | Battery network power loss | *PLossBatt* | W |
| `PwrStored` | `PwrStoredBatt` | Battery network power stored | *PStoredBatt* | W |

### **BattVolt** — Battery output voltage `scalar`

Combined voltage of the battery network,
*Vout*, in V.
## Parameters
```yaml
parameters:
- name: Initial battery capacity
  summary: Input or parameter Parameter (default) | External Input
  group: ''
  block_parameter: CapacityCtrl
  values: Parameter (default) | External Input
- name: Output battery voltage
  summary: Unfiltered or Filter Unfiltered (default) | Filtered
  group: ''
  block_parameter: OutputVlt
  values: Unfiltered (default) | Filtered
- name: Rated capacity at nominal temperature, BattChargeMax
  summary: Constant 100 (default) | scalar
  group: ''
  block_parameter: BattChargeMax
  values: 100 (default) | scalar
- name: Open circuit voltage table data, Em
  summary: 1-D lookup table 1-by-P matrix
  group: ''
  block_parameter: Em
  values: 1-by-P matrix
- name: State of charge breakpoints for open circuit voltage, SOCEmBp
  summary: Breakpoints 1-by-P matrix
  group: ''
  block_parameter: SOCEmBp
  values: 1-by-P matrix
- name: Internal resistance table data, RInt
  summary: 2-D lookup table N-by-M matrix
  group: ''
  block_parameter: RInt
  values: N-by-M matrix
- name: Battery temperature breakpoints, BattTempBp
  summary: Breakpoints [243.1 253.1 263.1 273.1 283.1 298.1 313.1] (default) | 1-by-N matrix
  group: ''
  block_parameter: BattTempBp
  values: '[243.1 253.1 263.1 273.1 283.1 298.1 313.1] (default) | 1-by-N matrix'
- name: State of charge breakpoints for internal resistance, SOCRintBp
  summary: Breakpoints [0 0.2 0.4 0.6 0.8 1] (default) | 1-by-M matrix
  group: ''
  block_parameter: SOCRintBp
  values: '[0 0.2 0.4 0.6 0.8 1] (default) | 1-by-M matrix'
- name: Number of cells in series, Ns
  summary: Integer 1 (default) | scalar
  group: ''
  block_parameter: Ns
  values: 1 (default) | scalar
- name: Number of cells in parallel, Np
  summary: Integer 1 (default) | scalar
  group: ''
  block_parameter: Np
  values: 1 (default) | scalar
- name: Initial battery capacity, BattCapInit
  summary: Capacity 100 (default) | scalar
  group: ''
  block_parameter: BattCapInit
  values: 100 (default) | scalar
- name: Output battery voltage time constant, Tc
  summary: Filter time constant 1/1000 (default) | scalar
  group: ''
  block_parameter: Tc
  values: -1 (default) | scalar
- name: Output battery voltage initial value, Vinit
  summary: Filter initial voltage 4.221 (default) | scalar
  group: ''
  block_parameter: Vinit
  values: -1 (default) | scalar
```

#### Block Options

### **Initial battery capacity** — Input or parameter `Parameter` (default) | `External Input`

Initial battery capacity,
*Capbatt*, in Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CapacityCtrl` |
| **Values:** | `Parameter` (default) | `External Input` |
| **Data Types:** | `character vector` |

#### Dependencies

| Block Parameter **Initial battery capacity** Option | Creates |
| --- | --- |
| `External Input` | Input port `CapInit` |
| `Parameter` | Parameter **Initial battery capacity, BattCapInit** |

### **Output battery voltage** — Unfiltered or Filter `Unfiltered` (default) | `Filtered`

Select `Filtered` to apply a first-order filter
to the output batter voltage.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputVlt` |
| **Values:** | `Unfiltered` (default) | `Filtered` |
| **Data Types:** | `character vector` |

#### Dependencies

Setting **Output battery voltage** parameter to
`Filtered` creates these parameters:

- **Output battery voltage time constant, Tc**
- **Output battery voltage initial value, Vinit**

### **Rated capacity at nominal temperature, BattChargeMax** — Constant `100` (default) | `scalar`

Rated battery capacity at the nominal temperature, in Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattChargeMax` |
| **Values:** | `100` (default) | `scalar` |
| **Data Types:** | `double` |

### **Open circuit voltage table data, Em** — 1-D lookup table `1`-by-`P` matrix

Open-circuit voltage data curve,
*Em*, as a function of the
discharged capacity for `P` operating points, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Em` |
| **Values:** | `1`-by-`P` matrix |
| **Data Types:** | `double` |

### **State of charge breakpoints for open circuit voltage, SOCEmBp** — Breakpoints `1`-by-`P` matrix

Discharge capacity breakpoints for `P` operating points,
dimensionless.

Although this parameter is the same as the **State of charge
breakpoints for internal resistance, SOCRintBp** parameter, the
block uses unique parameters for calibration flexibility.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOCEmBp` |
| **Values:** | `1`-by-`P` matrix |
| **Data Types:** | `double` |

### **Internal resistance table data, RInt** — 2-D lookup table `N`-by-`M` matrix

Internal resistance map, *Rint*,
as a function of `N` temperatures and `M`
SOCs, in ohms.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RInt` |
| **Values:** | `N`-by-`M` matrix |
| **Data Types:** | `double` |

### **Battery temperature breakpoints, BattTempBp** — Breakpoints `[243.1 253.1 263.1 273.1 283.1 298.1 313.1]` (default) | `1`-by-`N` matrix

Battery temperature breakpoints for `N` temperatures, in
K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattTempBp` |
| **Values:** | `[243.1 253.1 263.1 273.1 283.1 298.1 313.1]` (default) | `1`-by-`N` matrix |
| **Data Types:** | `double` |

### **State of charge breakpoints for internal resistance, SOCRintBp** — Breakpoints `[0 0.2 0.4 0.6 0.8 1]` (default) | `1`-by-`M` matrix

Battery capacity breakpoints for `M` SOCs,
dimensionless.

Although this parameter is the same as the **State of charge
breakpoints for open circuit voltage, SOCEmBp** parameter, the
block uses unique parameters for calibration flexibility.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOCRintBp` |
| **Values:** | `[0 0.2 0.4 0.6 0.8 1]` (default) | `1`-by-`M` matrix |
| **Data Types:** | `double` |

### **Number of cells in series, Ns** — Integer `1` (default) | `scalar`

Number of cells in series, dimensionless,
*Ns*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ns` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Number of cells in parallel, Np** — Integer `1` (default) | `scalar`

Number of cells in parallel, dimensionless,
*Np*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Np` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial battery capacity, BattCapInit** — Capacity `100` (default) | `scalar`

Initial battery capacity,
*Capbatt*, in Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattCapInit` |
| **Values:** | `100` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

| Block Parameter **Initial battery capacity** Option | Creates |
| --- | --- |
| `External Input` | Input port `CapInit` |
| `Parameter` | Parameter **Initial battery capacity, BattCapInit** |

### **Output battery voltage time constant, Tc** — Filter time constant `1/1000` (default) | `scalar`

Output battery voltage time constant,
*Tc*, in s. Used in a
first-order voltage filter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tc` |
| **Values:** | `-1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Output battery voltage** parameter to
`Filtered` creates these parameters:

- **Output battery voltage time constant, Tc**
- **Output battery voltage initial value, Vinit**

### **Output battery voltage initial value, Vinit** — Filter initial voltage `4.221` (default) | `scalar`

Output battery voltage initial value,
*Vinit*, in V. Used in a
first-order voltage filter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vinit` |
| **Values:** | `-1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Output battery voltage** parameter to
`Filtered` creates these parameters:

- **Output battery voltage time constant, Tc**
- **Output battery voltage initial value, Vinit**
## Libraries

Powertrain Blockset / Energy Storage and Auxiliary Drive / Datasheet Battery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2025a: Parameter Name and Description Changes

R2025a includes these Datasheet Battery block parameter name and
description changes. The updated names and descriptions describes their
functionality.

| Parameter | | R2025a Update | |
| --- | --- | --- | --- |
| Name | Description | Name | Description |
| `Em` | **Open circuit voltage table data** | `Em` | **Open circuit voltage, per cell** |
| `RInt` | **Internal resistance table data** | `RInt` | **Internal resistance, per cell** |
| `BattTempBp` | **Battery temperature breakpoints 1** | `BattTempBp` | **Battery temperature breakpoints** |
| `CapLUTBp` | **Open circuit voltage breakpoints 1** | `SOCEmBp` | **State of charge breakpoints for open circuit voltage** |
| `CapSOCBp` | **Battery capacity breakpoints 2** | `SOCRintBp` | **State of charge breakpoints for internal resistance** |

## Description

Lithium-ion, lithium-polymer, or lead-acid battery

The Datasheet Battery block implements a lithium-ion,
lithium-polymer, or lead-acid battery that you can parameterize using
manufacturer data. To create the open-circuit voltage and internal
resistance parameters that you need for the block, use the manufacturer
discharge characteristics by temperature data. For an example, see Generate Parameter Data for Datasheet Battery Block.

To determine the battery output voltage, the block uses lookup
tables for the battery open-circuit voltage and the internal resistance.
The lookup tables are functions of the state-of charge (SOC) and battery
temperature, characterizing the battery performance at various operating
points:

Em=f(SOC)Rint=f(T,SOC)

To calculate the voltage, the block implements these equations.

VT=Em−IbattRintIbatt=IinNpVout={NsVT     unfilteredVoutτs+1          filteredSOC=SOCo−1Capbatt∫0tIbattdtLdAmpHr=∫0tIbattdt

Positive current indicates battery
discharge. Negative current indicates battery charge.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrLdBatt` | Battery network power | Vbatt=Vout   OR  Voutτs+1Pbatt=−VbattIbattPLdBatt= −Pbatt |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLossBatt` | Battery network power loss | PLossBatt=−NpNsIbatt2Rint |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredBatt` | Battery network power stored | PStoredBatt=PBatt+PLossBatt |

The equations use these variables.

|  |  |
| --- | --- |
| *SOC* | State-of-charge |
| *SOCo* | Initial state-of-charge |
| *Em* | Battery open-circuit voltage |
| *Ibatt* | Per module battery current |
| *PLdBatt* | Battery network power |
| *Pbatt* | Battery power |
| *PLossBatt* | Battery network power loss |
| *PStoredBatt* | Battery network power stored |
| *Iin* | Combined current flowing from the battery network |
| *Rint* | Battery internal resistance |
| *Ns* | Number of cells in series |
| *Np* | Number of cells in parallel |
| *Vout*, *Vbatt* | Combined voltage of the battery network |
| *VT* | Per module battery voltage |
| *Capbatt* | Battery capacity |
| *LdAmpHr* | Battery energy |
