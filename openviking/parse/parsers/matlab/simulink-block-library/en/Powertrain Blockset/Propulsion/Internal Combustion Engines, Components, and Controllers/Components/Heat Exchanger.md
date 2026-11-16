---
type: simulink-block
title: 'Heat Exchanger'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'heatexchanger'
documentation_source_path: 'ref/heatexchanger.html'
language: en
---

# Heat Exchanger

## Ports

### Input

### **C** — Inlet mass flow rate, heat flow rate, temperature, mass fractions two-way connector port

Bus containing the heat exchanger:

- `MassFlwRate` — Mass flow
  rate at inlet, m˙, in kg/s
- `HeatFlwRate` — Heat flow
  rate at inlet, qin, in J/s
- `Temp` — Temperature at inlet, Tflw,in, in K
- `MassFrac` — Inlet mass fractions,
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

### **B** — Outlet volume pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the heat exchanger:

- `Prs` — Pressure at outlet, pvol,out, in Pa
- `Temp` — Temperature at outlet, Tvol,out, in K
- `Enth` — Specific enthalpy
  at outlet, hvol,out, in J/kg
- `MassFrac` — Outlet mass fractions,
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

### **Effct** — Heat exchanger effectiveness `scalar`

Heat exchanger effectiveness, εinput.

#### Dependencies

To create this port, set **Effectiveness model**
to `External input`.

### **CoolTemp** — Cooling medium temperature scalar

Cooling medium temperature, Tcool,input.

#### Dependencies

To create this port, set **Cooling medium temperature
input** to `External
input`
### Output

### **Info** — Heat exchanger data bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `InletTemp` | | | Heat exchanger inlet temperature | K |
| `OutletTemp` | | | Heat exchanger outlet temperature | K |
| `HeatTrnsfrRate` | | | Heat exchanger heat transfer rate | J/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrHeatFlwIn` | Heat flow rate at port C | W |
| `PwrHeatFlwOut` | Heat flow rate at port B | W |
| `PwrNotTrnsfrd` | `PwrHeatTrnsfr` | Heat transfer rate to cooling medium | W |
| `PwrStored` | | *Not used* | |

### **C** — Inlet flow pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the heat exchanger:

- `Prs` — Pressure at inlet, pflw,in, in Pa
- `Temp` — Temperature at inlet, Tin, in K
- `Enth` — Specific enthalpy
  at inlet, hin, in J/kg
- `MassFrac` — Inlet mass fractions,
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

### **B** — Outlet volume mass flow rate, heat flow rate, temperature, mass fractions two-way connector port

Bus containing the heat exchanger:

- `MassFlwRate` — Mass flow
  rate at outlet, m˙, in kg/s
- `HeatFlwRate` — Heat flow
  rate at outlet, qout, in J/s
- `Temp` — Temperature at outlet, Tout, in K
- `MassFrac` — Outlet mass fractions,
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

### **Effectiveness model** — Model type for heat effectiveness `Constant` (default) | `External input`

Type of model to calculate the heat exchanger effectiveness.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EffctModelPopup` |
| **Values:** | `Constant` (default) | `External input` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting:

- `External input` creates the
  `Effct` port.
- `Constant` enables the
  **Heat exchanger effectiveness,
  ep\_cnst** parameter.

### **Cooling medium temperature input** — Specify type `Constant` (default) | `External input`

Cooling medium temperature input.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CoolTempInputPopup` |
| **Values:** | `Constant` (default) | `External input` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting:

- `External input` creates the
  `CoolTemp` port.
- `Constant` enables the
  **Cooling medium temperature,
  T\_cool\_cnst** parameter.

### **Image type** — Icon color `Intercooler` (default) | `EGR cooler hot to cold` | `EGR cooler cold to hot`

Block icon color:

- `Intercooler` for blue, to indicate
  an intercooler
- `EGR cooler hot to cold` for red to
  blue, to indicate EGR from hot to cold
- `EGR cooler cold to hot` for blue to
  red, to indicate EGR from cold to hot

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

### **Heat exchanger effectiveness, ep\_cnst** — Effectiveness `0.7` (default) | `scalar`

Constant heat exchanger effectiveness, εcnst.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ep_cnst` |
| **Values:** | `0.7` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Constant`
for the **Effectiveness model** parameter.

### **Cooling medium temperature, T\_cool\_cnst** — Temperature `300` (default) | `scalar`

Constant cooling medium temperature, Tcool,cnst, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_cool_cnst` |
| **Values:** | `300` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Constant`
for the **Cooling medium temperature input**
parameter.

### **Specific heat at constant pressure, cp** — Specific heat `1005` (default) | `scalar`

Specific heat at constant pressure, cp, in J/(kg\*K).

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

Intercooler or exhaust gas recirculation (EGR) cooler

The Heat Exchanger block models a heat exchanger,
for example, an intercooler or exhaust gas recirculation (EGR) cooler.
The inlet (port C) connects to an engine flow component (flow restriction,
compressor, turbine, or engine block). The outlet (port B) connects
to a volume (control volume or environment). Based on the upstream
temperature, heat exchanger effectiveness, and cooling medium temperature,
the block determines the heat transfer rate and downstream temperature.

For the heat exchanger effectiveness and cooling medium temperature,
you can specify either a constant value or an external input. For
example, if you specify a heat exchanger effectiveness that is:

- Equal to 1, the downstream temperature is equal to
  the cooling medium temperature.
- Equal to 0, there is no heat transfer to the cooling
  medium. The downstream temperature is equal to the upstream temperature.

The block assumes no pressure drop. To model pressure losses,
use a Flow Restriction block.

### Equations

The Heat Exchanger block implements equations
that use these variables.

|  |  |
| --- | --- |
| Tupstr | Upstream temperature |
| Tdnstr | Downstream temperature |
| Tcool | Cooling medium temperature |
| Tcool,cnst | Constant cooling medium temperature |
| Tcool,input | External input cooling medium temperature |
| ε | Heat exchanger effectiveness |
| εcnst | Constant heat exchanger effectiveness |
| εinput | Input heat exchanger effectiveness |
| cp | Specific heat at constant pressure |
| qht | Heat exchanger heat transfer rate |
| pflw,in | Pressure at inlet |
| pvol,out | Pressure at outlet |
| Tvol,out | Temperature at outlet |
| hvol,out | Specific enthalpy at outlet |
| qin | Heat flow rate at inlet |
| qout | Heat flow rate at outlet |
| m˙ | Heat exchanger mass flow rate |
| Tflw,in | Temperature at inlet |
| Tin | Heat exchanger inlet temperature |
| Tout | Heat exchanger outlet temperature |
| hin | Inlet specific enthalpy |

**Heat Exchanger Effectiveness**

Heat exchanger effectiveness measures the effectiveness of heat
transfer from the incoming hot fluid to the cooling medium:

ε=Tupstr−TdnstrTupstr−Tcool

In an ideal heat exchanger, the downstream temperature
equals the cooling temperature. The effectiveness is equal to 1.

Tdnstr=Tcoolε=1

The Heat Exchanger block uses the effectiveness
to determine the downstream temperature and heat transfer rate.

Tdnstr=Tupstr−ε(Tupstr−Tcool)qht=m˙cp(Tupstr−Tdnstr)

**Fluid Flow**

Since the block assumes no pressure drop, Pflw,in=Pvol,out.

The flow component connection to the heat exchanger inlet determines
the direction of the mass flow. Based on the mass flow rate direction,
these temperature and heat flow equations apply.

| Fluid Flow | Mass Flow Rate | Temperatures and Heat Flow |
| --- | --- | --- |
| Forward — From engine flow component to outlet volume | m˙≥0 | Tupstr=Tflw,inTin=TupstrTout=Tdnstrqout=m˙cpTdnstr |
| Reverse — From outlet volume to engine flow component | m˙<0 | Tupstr=Tvol,outTin=TdnstrTout=Tvol,outhin=cpTdnstrqout=m˙hvol,out |

The block uses the internal signal `FlwDir` to track the direction of the flow.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrHeatFlwIn` | Heat flow rate at port C | *qin* |
| `PwrHeatFlwOut` | Heat flow rate at port B | -*qout* |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrHeatTrnsfr` | Heat transfer rate to cooling medium | -*qht* |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | | *Not used* | |
