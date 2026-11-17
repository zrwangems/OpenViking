---
type: simulink-block
title: 'Flow Restriction'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components'
documentation_page: 'flowrestriction'
documentation_source_path: 'ref/flowrestriction.html'
language: en
---

# Flow Restriction

## Ports
```yaml
ports:
- name: A
  summary: Inlet orifice pressure, temperature, enthalpy, mass fractions two-way connector port
  direction: input
- name: B
  summary: Outlet orifice pressure, temperature, enthalpy, mass fractions two-way connector port
  direction: input
- name: Area
  summary: Orifice area scalar
  direction: input
- name: ThrPct
  summary: Throttle body percent open scalar
  direction: input
- name: A
  summary: Inlet mass flow rate, heat flow rate, temperature two-way connector port
  direction: output
- name: B
  summary: Outlet mass flow rate, heat flow rate, temperature two-way connector port
  direction: output
- name: Info
  summary: Bus signal bus
  direction: output
```

### Input

### **A** — Inlet orifice pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing orifice:

- `Prs` — Pressure, in Pa
- `Temp` — Temperature, in K
- `Enth` — Specific enthalpy,
  in J/kg
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

### **B** — Outlet orifice pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing orifice:

- `Prs` — Pressure, in Pa
- `Temp` — Temperature, in K
- `Enth` — Specific enthalpy,
  in J/kg
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

### **Area** — Orifice area `scalar`

External area input for orifice area, Aorf\_ext, in m^2.

#### Dependencies

To create this port, select `External input` for
the **Orifice area model** parameter.

### **ThrPct** — Throttle body percent open `scalar`

Percentage of throttle body that is open, Pctthr.

#### Dependencies

To create this port, select `Throttle body geometry` for
the **Orifice area model** parameter.
### Output

### **A** — Inlet mass flow rate, heat flow rate, temperature two-way connector port

Bus containing:

- `MassFlw` — Mass flow rate through inlet, in kg/s
- `HeatFlw` — Inlet heat flow rate, in J/s
- `Temp` — Inlet temperature,
  in K
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

### **B** — Outlet mass flow rate, heat flow rate, temperature two-way connector port

Bus containing:

- `MassFlw` — Outlet mass flow rate, in kg/s
- `HeatFlw` — Outlet heat flow rate, in J/s
- `Temp` — Outlet temperature,
  in K
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

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | | Description | Units |
| --- | --- | --- | --- | --- | --- |
| `Flw` | `PrsAdj` | | `DwnstrmPrs` | Downstream pressure | Pa |
| `UpstrmPrs` | Upstream pressure | Pa |
| `PrsRatio` | Pressure ratio | NA |
| `DwnstrmTemp` | Downstream temperature | K |
| `UpstrmTemp` | Upstream temperature | K |
| `OrfMassFlw` | | | Mass flow rate through orifice | kg/s |
| `Species` | | `O2MassFlw` | Oxygen mass flow rate | kg/s |
| `N2MassFlw` | Nitrogen mass flow rate | kg/s |
| `UnbrndFuelMassFlw` | Unburned gas mass flow rate | kg/s |
| `CO2MassFlw` | Carbon dioxide mass flow rate | kg/s |
| `H2OMassFlw` | Water mass flow rate | kg/s |
| `COMassFlw` | Carbon monoxide mass flow rate | kg/s |
| `NOMassFlw` | Nitric oxide mass flow rate | kg/s |
| `NO2MassFlw` | Nitrogen dioxide mass flow rate | kg/s |
| `NOxMassFlw` | Nitric oxide and nitrogen dioxide mass flow rate | kg/s |
| `PmMassFlw` | Particulate matter mass flow rate | kg/s |
| `AirMassFlw` | Air mass flow rate | kg/s |
| `BrnedGasMassFlw` | Burned gas mass flow rate | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrHeatFlwIn` | Heat flow rate at port A | W |
| `PwrHeatFlwOut` | Heat flow rate at port B | W |
| `PwrNotTrnsfrd` | | *Not used* | |
| `PwrStored` | | *Not used* | |
| `Area` | `FlwArea` | | | Cross-sectional flow area | m^2 |
| `EffctArea` | | | Effective orifice cross-sectional area | m^2 |
| `ThrAng` | | | Throttle area, if applicable | deg |
## Parameters
```yaml
parameters:
- name: Orifice area model
  summary: Select model Constant (default) | External input | Throttle body geometry
  group: ''
  block_parameter: AreaPopup
  values: Constant (default) | External input | Throttle body geometry
- name: Image type
  summary: Icon color Cold (default) | Hot
  group: ''
  block_parameter: ImageTypePopup
  values: Cold (default) | Hot
- name: Ratio of specific heats, gamma
  summary: Ratio 1.3998 (default) | scalar
  group: ''
  block_parameter: gamma
  values: 1.3998 (default) | scalar
- name: Ideal gas constant, R
  summary: Constant 287.05 (default) | scalar
  group: ''
  block_parameter: R
  values: 287.05 (default) | scalar
- name: Pressure ratio linearize limit, Plim
  summary: Limit 0.95 (default) | scalar
  group: ''
  block_parameter: Plim
  values: 0.95 (default) | scalar
- name: Constant area value, Aorf_cnst
  summary: Area .1 (default) | scalar
  group: ''
  block_parameter: Aorf_cnst
  values: .1 (default) | scalar
- name: Discharge coefficient, Cd_cnst
  summary: Coefficient 1 (default) | scalar
  group: ''
  block_parameter: Cd_cnst
  values: 1 (default) | scalar
- name: Discharge coefficient, Cd_ext
  summary: Coefficient 1 (default) | scalar
  group: ''
  block_parameter: Cd_ext
  values: 1 (default) | scalar
- name: Throttle diameter, Dthr
  summary: Diameter 50 (default) | scalar
  group: ''
  block_parameter: Dthr
  values: 50 (default) | scalar
- name: Discharge coefficient table, ThrCd
  summary: Coefficient [0.001; 0.735] (default) | vector
  group: ''
  block_parameter: ThrCd
  values: '[0.001; 0.735] (default) | vector'
- name: Angle breakpoints, ThrAngBpts
  summary: Angle [0; 90] (default) | vector
  group: ''
  block_parameter: ThrAngBpts
  values: '[0; 90] (default) | vector'
```

#### Block Options

### **Orifice area model** — Select model `Constant` (default) | `External input` | `Throttle body geometry`

Orifice area model.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AreaPopup` |
| **Values:** | `Constant` (default) | `External input` | `Throttle body geometry` |
| **Data Types:** | `character vector` |

#### Dependencies

The orifice area model enables the parameters on the **Area
Parameters** tab.

### **Image type** — Icon color `Cold` (default) | `Hot`

Block icon color:

- `Cold` for blue.
- `Hot` for red.

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

#### General

### **Ratio of specific heats, gamma** — Ratio `1.3998` (default) | `scalar`

Ratio of specific heats, *γ*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gamma` |
| **Values:** | `1.3998` (default) | `scalar` |
| **Data Types:** | `double` |

### **Ideal gas constant, R** — Constant `287.05` (default) | `scalar`

Ideal gas constant, R, in J/(kg·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R` |
| **Values:** | `287.05` (default) | `scalar` |
| **Data Types:** | `double` |

### **Pressure ratio linearize limit, Plim** — Limit `0.95` (default) | `scalar`

Pressure ratio limit to avoid singularities as the pressure ratio
approaches 1, Plim.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Plim` |
| **Values:** | `0.95` (default) | `scalar` |
| **Data Types:** | `double` |

#### Area

### **Constant area value, Aorf\_cnst** — Area `.1` (default) | `scalar`

Constant area value, Aorf\_cnst, in m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aorf_cnst` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Constant`
for the **Orifice area model** parameter.

### **Discharge coefficient, Cd\_cnst** — Coefficient `1` (default) | `scalar`

Discharge coefficient for constant area, Cdcnst.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cd_cnst` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Constant`
for the **Orifice area model** parameter.

### **Discharge coefficient, Cd\_ext** — Coefficient `1` (default) | `scalar`

Discharge coefficient for external area input, Cdext.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cd_ext` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External
input` for the **Orifice area model**
parameter.

### **Throttle diameter, Dthr** — Diameter `50` (default) | `scalar`

Throttle body diameter at opening, Dthr, in mm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Dthr` |
| **Values:** | `50` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Throttle body
geometry` for the **Orifice area
model** parameter.

### **Discharge coefficient table, ThrCd** — Coefficient `[0.001; 0.735]` (default) | `vector`

Discharge coefficient table,
*Cd\_thr*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ThrCd` |
| **Values:** | `[0.001; 0.735]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Throttle body
geometry` for the **Orifice area
model** parameter.

### **Angle breakpoints, ThrAngBpts** — Angle `[0; 90]` (default) | `vector`

Angle breakpoints, Thrang\_bpts, in deg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ThrAngBpts` |
| **Values:** | `[0; 90]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Throttle body
geometry` for the **Orifice area
model** parameter.
## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Fundamental Flow

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Isentropic ideal gas flow through an orifice

The Flow Restriction block models isentropic
ideal gas flow through an orifice. The block uses the conservation
of mass and energy to determine the mass flow rate. The flow velocity
is limited by choked flow.

You can specify these orifice area models:

- Constant
- External input
- Throttle body geometry

### Equations

The Flow Restriction block implements these equations.

| Calculation | Equations |
| --- | --- |
| Standard orifice | m˙orf=Γ⋅Ψ(Pratio)  Pratio=PdownstrPupstr  Γ=Aeff⋅PupstrR⋅Tupstr  Pcr=(2γ+1)γγ−1  Ψ={γ(2γ+1)γ+1γ−1Pratio<Pcr2γγ−1(Pratio2γ−Pratioγ+1γ)Pcr≤Pratio≤PlimPratio−1Plim−12γγ−1(Plim2γ−Plimγ+1γ)Plim<Pratio |
| Constituent mass flow rates | m˙i=m˙orfyupstr,i |
| Constant orifice area | Aeff=Aorf\_cnst⋅Cdcnst |
| External input orifice area | Aeff=Aorf\_ext⋅Cdext |
| Throttle body geometry | θthr=Pctthr⋅90100  Aeff\_thr=π4Dthr2Cd\_thr(θthr) |
| Heat flow rate | qorf=m˙orfhupstr |

The equations use these variables.

|  |  |
| --- | --- |
| Aeff, Aeff\_thr | Effective orifice cross-sectional area |
| Aorf\_cnst, Aorf\_ext | Orifice area |
| Cdcnst, Cdext | Discharge coefficient |
| R | Ideal gas constant |
| Pcr | Critical pressure at which choked flow occurs |
| *γ* | Ratio of specific heats |
| Γ | Flow function based on pressure ratio |
| Pratio | Pressure ratio |
| Pupstr | Upstream orifice pressure |
| Pdownstr | Downstream orifice pressure |
| Plim | Pressure ratio limit to avoid singularities as the pressure ratio approaches 1 |
| *yupstr,i* | Upstream species mass fraction for i = O2, N2, unburned fuel, CO2, H2O, CO, NO, NO2, PM, air, and burned gas |
| m˙i | Mass flow rate for i = O2, N2, unburned fuel, CO2, H2O, CO, NO, NO2, PM, air, and burned gas |
| θthr | Throttle angle |
| Pctthr | Percentage of throttle body that is open |
| *Cd\_thr* | Throttle discharge coefficient |
| Dthr | Throttle body diameter at opening |
| m˙orf | Orifice mass flow |
| *hupstr* | Upstream specific enthalpy |
| *qorf* | Heat flow rate |

The block uses the internal signal `FlwDir` to track the direction of the flow.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrHeatFlwIn` | Heat flow rate at port A | *qorf* |
| `PwrHeatFlwOut` | Heat flow rate at port B | -*qorf* |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | *Not used* | | |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | *Not used* | | |
