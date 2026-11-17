---
type: simulink-block
title: 'Simple Engine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Propulsion'
documentation_page: 'simpleengine'
documentation_source_path: 'ref/simpleengine.html'
language: en
---

# Simple Engine

## Ports
```yaml
ports:
- name: TrqCmd
  summary: Commanded torque scalar
  direction: input
- name: EngSpd
  summary: Engine speed scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: EngTrq
  summary: Engine brake torque scalar
  direction: output
```

### Input

### **TrqCmd** — Commanded torque `scalar`

Torque, in N·m.

### **EngSpd** — Engine speed `scalar`

Engine speed, in rpm.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `IntkGasMassFlw` (zeroed out intentionally) | | | Engine air mass flow output | kg/s |
| `NrmlzdAirChrg` (zeroed out intentionally) | | | Normalized engine cylinder air mass | N/A |
| `Afr` (zeroed out intentionally) | | | Air-fuel ratio (AFR) | N/A |
| `FuelMassFlw` | | | Engine fuel flow output | kg/s |
| `FuelVolFlw` | | | Volumetric fuel flow | m3/s |
| `ExhManGasTemp` (zeroed out intentionally) | | | Engine exhaust gas temperature | K |
| `EngTrq` | | | Engine torque output | N·m |
| `EngSpd` | | | Engine speed | rpm |
| `CrkAng` (zeroed out intentionally) | | | Engine crankshaft absolute angle  ∫0(360)CpsEngSpd18030dθ  where Cps is crankshaft revolutions per power stroke. | deg |
| `Bsfc` | | | Engine brake-specific fuel consumption (BSFC) | g/kWh |
| `EoHC` (zeroed out intentionally) | | | Engine out hydrocarbon emission mass flow | kg/s |
| `EoCO` (zeroed out intentionally) | | | Engine out carbon monoxide emission mass flow rate | kg/s |
| `EoNOx` (zeroed out intentionally) | | | Engine out nitric oxide and nitrogen dioxide emissions mass flow | kg/s |
| `EoCO2` (zeroed out intentionally) | | | Engine out carbon dioxide emission mass flow | kg/s |
| `EoPM` (zeroed out intentionally) | | | Engine out particulate matter emission mass flow | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCrkshft` | Crankshaft power | W |
| `PwrNotTrnsfrd` | `PwrFuel` | Fuel input power | W |
| `PwrLoss` | Power loss | W |
| `PwrStored` | | *Not used* | |

### **EngTrq** — Engine brake torque `scalar`

Engine brake torque, in N·m.
## Parameters
```yaml
parameters:
- name: Engine maximum torque, f_tqmax
  summary: Breakpoints [75.679776480773256 75.679776480773256 97.173658538143172 116.84042599160529 152.21029882684542 175
    174.99889520597083 174.99996520122858 175 175 175 175 175 175 175 175] (default) | vector
  group: ''
  block_parameter: f_tqmax
  values: vector
- name: Breakpoints for engine speed input, f_tqmax_n_bpt
  summary: Breakpoints [0 750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857
    2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000] (default)
    | vector
  group: ''
  block_parameter: f_tqmax_n_bpt
  values: vector
- name: Fuel lower heating value, Lhv
  summary: Heating value 4.6E+7 (default) | scalar
  group: ''
  block_parameter: Lhv
  values: 4.6E+7 (default) | scalar
- name: Fuel specific gravity, Sg
  summary: Specific gravity 0.745 (default) | scalar
  group: ''
  block_parameter: Sg
  values: 0.745 (default) | scalar
- name: Average brake specific fuel consumption, BsfcAvg
  summary: Average brake specific fuel consumption 350 (default) | scalar
  group: ''
  block_parameter: BsfcAvg
  values: 350 (default) | scalar
```

### **Engine maximum torque, f\_tqmax** — Breakpoints `[75.679776480773256 75.679776480773256 97.173658538143172 116.84042599160529 152.21029882684542 175 174.99889520597083 174.99996520122858 175 175 175 175 175 175 175 175]` (default) | `vector`

Breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqmax` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Breakpoints for engine speed input, f\_tqmax\_n\_bpt** — Breakpoints `[0 750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector`

Breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqmax_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Fuel lower heating value, Lhv** — Heating value `4.6E+7` (default) | `scalar`

Fuel lower heating value, in J/kg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lhv` |
| **Values:** | `4.6E+7` (default) | `scalar` |
| **Data Types:** | `double` |

### **Fuel specific gravity, Sg** — Specific gravity `0.745` (default) | `scalar`

Specific gravity of fuel, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Sg` |
| **Values:** | `0.745` (default) | `scalar` |
| **Data Types:** | `double` |

### **Average brake specific fuel consumption, BsfcAvg** — Average brake specific fuel consumption `350` (default) | `scalar`

Average brake specific fuel consumption, in g/kwh.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BsfcAvg` |
| **Values:** | `350` (default) | `scalar` |
| **Data Types:** | `double` |
## Libraries

Powertrain Blockset / Propulsion / Combustion Engines Vehicle Dynamics Blockset / Powertrain / Propulsion

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Simplified engine model using lookup tables

The Simple Engine block implements a simplified engine model using a
maximum torque vs engine speed table, two scalar fuel mass properties, and one scalar engine
efficiency parameter to estimate engine torque and fuel flow. You can use the block for:

- Hardware-in-the-loop (HIL) engine control design
- Vehicle-level fuel economy and performance simulations
