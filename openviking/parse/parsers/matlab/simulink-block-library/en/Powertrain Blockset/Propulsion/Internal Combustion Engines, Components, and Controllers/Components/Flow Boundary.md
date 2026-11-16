---
type: simulink-block
title: 'Flow Boundary'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'flowboundary'
documentation_source_path: 'ref/flowboundary.html'
language: en
---

# Flow Boundary

## Ports

### Input

### **Prs** — Pressure `scalar`

External input pressure, *P*, in Pa.

#### Dependencies

To create this port, select `External input` for
the **Pressure and temperature source** parameter.

### **Temp** — Temperature `scalar`

External input temperature, *T*, in K.

#### Dependencies

To create this port, select `External input` for
the **Pressure and temperature source** parameter.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `BndryPrs` | | | Boundary pressure | Pa |
| `BndryTemp` | | | Boundary temperature | K |
| `BndryEnth` | | | Boundary specific enthalpy | J/kg |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBndryFlw` | Heat flow rate to flow restriction | W |
| `PwrNotTrnsfrd` | `PwrEnv` | Heat flow rate to environment | W |
| `PwrStored` | | *Not used* | |

### **C** — Boundary pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the flow boundary:

- `Prs` — Pressure, *P*,
  in Pa
- `Temp` — Temperature, *T*,
  in K
- `Enth` — Specific enthalpy, *h*,
  in J/kg
- `MassFrac` — Mass fractions,
  dimensionless.

  Specifically, a bus with these mass fractions:

  - `O2MassFrac` — Oxygen
  - `N2MassFrac` — Nitrogen
  - `UnbrndFuelMassFrac` — Unburned fuel
  - `CO2MassFrac` — Carbon dioxide
  - `H2OMassFrac` — Water
  - `COMassFrac` — Carbon monoxide
  - `NOMassFrac` — Nitric oxide
  - `NO2MassFrac` — Nitrogen dioxide
  - `NOxMassFrac` — Nitric oxide and nitrogen dioxide
  - `PmMassFrac` — Particulate matter
  - `AirMassFrac` — Air
  - `BrndGasMassFrac` — Burned gas

## Parameters

#### Block Options

### **Pressure and temperature source** — Select source `External input` (default) | `Constant`

Pressure and temperature source.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PrsTempSrcPopup` |
| **Values:** | `External input` (default) | `Constant` |
| **Data Types:** | `character vector` |

#### Dependencies

The table summarizes the parameter and port dependencies.

| Value | Enables Parameters | Creates Ports |
| --- | --- | --- |
| `Constant` | **Pressure, Pcnst**  **Temperature, Tcnst** | None |
| `External input` | None | `Prs`  `Temp` |

### **Image type** — Icon color `Cold` (default) | `Hot`

Select color for block icon:

- `Cold` for blue
- `Hot` for red

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ImageTypePopup` |
| **Values:** | `Cold` (default) | `Hot` |
| **Data Types:** | `character vector` |

### **Pressure, Pcnst** — Constant `101325` (default) | `scalar`

Constant pressure, *P*, in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Pcnst` |
| **Values:** | `101325` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Constant`
for the **Pressure and temperature source**
parameter.

### **Temperature, Tcnst** — Constant `298.15` (default) | `scalar`

Constant temperature, *T*, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tcnst` |
| **Values:** | `298.15` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Constant`
for the **Pressure and temperature source**
parameter.

### **Specific heat at constant pressure, cp** — Constant `1005` (default) | `scalar`

Specific heat at constant pressure, in J/(kg·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `cp` |
| **Values:** | `1005` (default) | `scalar` |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Fundamental Flow

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Flow boundary for ambient temperature and pressure

The Flow Boundary block implements a flow boundary that typically represents
ambient temperature and pressure. Engine models require flow boundaries at the intake
inlet and exhaust outlet. In dynamic engine models, flow-modifying components (for
example, flow restriction, turbines, and compressors) connect to control volumes and
flow boundaries.

You can specify these block configurations:

- Constant pressure and temperature
- Externally input pressure and temperature

The Flow Boundary block outputs pressure, temperature,
and specific enthalpy:

h=cpT

The block models the mass fractions as dry air, resulting in
these mass fractions:

- *yN2* = 0.767
- *yO2* = .233

The equation uses these variables.

|  |  |
| --- | --- |
| *T* | Temperature |
| *h* | Specific enthalpy |
| *cp* | Specific heat at constant pressure |
| *yN2* | Nitrogen mass fraction |
| *yO2* | Oxygen mass fraction |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrBndrFlw` | Heat flow rate to flow restriction | *qorf* |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrEnv` | Heat flow rate to environment | -*qorf* |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | *Not used* | | |
