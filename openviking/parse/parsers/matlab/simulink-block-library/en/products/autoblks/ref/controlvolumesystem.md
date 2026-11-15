---
type: simulink-block
title: 'Control Volume System'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'controlvolumesystem'
documentation_source_path: 'ref/controlvolumesystem.html'
language: en
---

# Control Volume System

## Ports

### Input

### **C** — Inlet mass flow rate, heat flow rate, mass fractions two-way connector port

Bus containing:

- `MassFlw` — Mass flow rate through inlet, in kg/s
- `HeatFlw` — Inlet heat flow rate, in J/s
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

#### Dependencies

To create input ports, specify the **Number of inlet
ports** parameter.

### **HeatTrnsfrRate** — Heat transfer `scalar`

External heat transfer input to control volume, *qhe*,
in Kg/s.

#### Dependencies

To create this port, select `External input` for
the **Heat transfer model** parameter.

### **ExtnlFlwVel** — External flow velocity scalar

External flow velocity, *Flwspd*,
in m/s.

#### Dependencies

To create this port, select `External wall convection` for
the **Heat transfer model** parameter.

### **ExtnlTemp** — Ambient temperature, K `scalar`

#### Dependencies

To create this port, select `External wall convection` for
the **Heat transfer model** parameter.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Vol` | `Prs` | | Volume pressure | Pa |
| `Temp` | | Volume temperature | K |
| `Enth` | | Volume specific enthalpy | J/kg |
| `Species` | `O2MassFrac` | Oxygen mass fraction | NA |
| `N2MassFrac` | Nitrogen mass fraction | NA |
| `UnbrndFuelMassFrac` | Unburned gas mass fraction | NA |
| `CO2MassFrac` | Carbon dioxide mass fraction | NA |
| `H2OMassFrac` | Water mass fraction | NA |
| `COMassFrac` | Carbon monoxide mass fraction | NA |
| `NOMassFrac` | Nitric oxide mass fraction | NA |
| `NO2MassFrac` | Nitrogen dioxide mass fraction | NA |
| `NOxMassFrac` | Nitric oxide and nitrogen dioxide mass fraction | NA |
| `PmMassFrac` | Particulate matter mass fraction | NA |
| `AirMassFrac` | Air mass fraction | NA |
| `BrndGasMassFrac` | Burned gas mass fraction | NA |
| `HeatTrnsfr` | `HeatTrnsfrRate` | | Wall heat transfer rate | J/s |
| `MassFlw` | | Average internal mass flow rate | kg/s |
| `IntrnTemp` | | Temperature of gas inside chamber | K |
| `PwrInfo` | `PwrTrnsfrd` | `PwrHeatFlwi` | Port *`i`* heat flow | W |
| `PwrNotTrnsfrd` | `PwrHeatTrnsfr` | Heat transfer rate from wall to control volume | W |
| `PwrStored` | `PwrHeatStored` | Rate of heat stored in the control volume | W |

### **C** — Outlet pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the outlet control volume:

- `Prs` — Chamber pressure,
  in Pa
- `Temp` — Gas temperature,
  in K
- `Enth` — Specific enthalpy,
  in J/kg
- `MassFrac` —
  Mass fractions, dimensionless.

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

#### Dependencies

To create outlet ports, specify the **Number of outlet
ports** parameter.

## Parameters

#### Block Options

### **Number of inlet ports** — Number of ports `1` (default) | `0` | `2` | `3` | `4`

Number of inlet ports.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumInletPorts` |
| **Values:** | `1` (default) | `0` | `2` | `3` | `4` |
| **Data Types:** | `double` |

#### Dependencies

To create inlet ports, specify the number.

### **Number of outlet ports** — Number of ports `1` (default) | `0` | `2` | `3` | `4`

Number of outlet ports.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumOutletPorts` |
| **Values:** | `1` (default) | `0` | `2` | `3` | `4` |
| **Data Types:** | `double` |

#### Dependencies

To create outlet ports, specify the number.

### **Heat transfer model** — Select model `Constant` (default) | `External input` | `External wall convection`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `HeatTransferModelPopup` |
| **Values:** | `Constant` (default) | `External input` | `External wall convection` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting `Constant` or `External
wall convection` enables the **Heat
Transfer** parameters.

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

#### General

### **Chamber volume, Vch** — Volume `0.0029` (default) | `scalar`

Chamber volume, *Vch*, in
m^3.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vch` |
| **Values:** | `0.0029` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial chamber pressure, Pinit** — Pressure `101325` (default) | `scalar`

Initial chamber pressure, *Pvol*,
in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Pinit` |
| **Values:** | `101325` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial chamber temperature, Tinit** — Temperature `298` (default) | `scalar`

Initial chamber temperature,
*Tvol*, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tinit` |
| **Values:** | `298` (default) | `scalar` |
| **Data Types:** | `double` |

### **Ideal gas constant, R** — Ideal gas constant `287` (default) | `scalar`

Ideal gas constant, *R*, in J/(kg\*K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R` |
| **Values:** | `287` (default) | `scalar` |
| **Data Types:** | `double` |

### **Specific heat capacity, cp** — Specific heat `1005` (default) | `scalar`

Specific heat capacity, *cp*, in
J/(kg·K).

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

#### Heat Transfer

### **Heat transfer rate, q\_he** — Rate `0` (default) | `scalar`

Constant heat transfer rate,
*qhe*, in J/s.

#### Dependencies

To enable this parameter, select `Constant`
for the **Heat transfer model** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `q_he` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **External convection heat transfer coefficient, ext\_tbl** — Manifold external air `[40 160 740 2000]` (default) | `vector`

External convection heat transfer coefficient,
*hext*, in W/(m^2K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ext_tbl` |
| **Values:** | `[40 160 740 2000]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **External velocity breakpoints, ext\_bpts** — Manifold external air `linspace(0,180,4)` (default) | `vector`

External velocity breakpoints,
*xext*, in m/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ext_bpts` |
| **Values:** | `linspace(0,180,4)` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **External convection area, Aext\_conv** — Manifold external air `0.125` (default) | `scalar`

External convection area,
*Aext\_conv*, in m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aext_conv` |
| **Values:** | `0.125` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Thermal mass, m\_wall** — Manifold wall general `7` (default) | `scalar`

Thermal mass, *mwall*, in
kg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `m_wall` |
| **Values:** | `7` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Wall heat capacity, cp\_wall** — Manifold wall general `900` (default) | `scalar`

Wall heat capacity, *cp\_wall*, in
J/(kg·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `cp_wall` |
| **Values:** | `900` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Initial mass temperature, Tmass** — Manifold wall general `293.15` (default) | `scalar`

Initial mass temperature, *Tmass*,
in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tmass` |
| **Values:** | `293.15` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **External wall thickness, Dext\_cond** — Manifold wall external `0.004` (default) | `scalar`

External wall thickness,
*Dext\_cond*, in m.

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

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Dext_cond` |
| **Values:** | `0.004` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **External conduction area, Aext\_cond** — Manifold wall external `0.003` (default) | `scalar`

External conduction area,
*Aext\_cond*, in m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aext_cond` |
| **Values:** | `0.003` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **External wall thermal conductivity, kext** — Manifold wall external `25` (default) | `scalar`

External wall thermal conductivity,
*kext*, in W/(m·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `kext` |
| **Values:** | `25` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Internal wall thickness, Dint\_cond** — Manifold wall internal `0.004` (default) | `scalar`

Internal wall thickness,
*Dint\_cond*, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Dint_cond` |
| **Values:** | `0.004` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Internal conduction area, Aint\_cond** — Manifold wall internal `0.003` (default) | `scalar`

Internal conduction area,
*Aint\_cond*, in m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aint_cond` |
| **Values:** | `0.003` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Internal wall thermal conductivity, kint** — Manifold wall internal `25` (default) | `scalar`

Internal wall thermal conductivity,
*kint*, in W/(m·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `kint` |
| **Values:** | `25` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Internal convection heat transfer coefficient, int\_tbl** — Manifold internal air `[40 160 740 2000]` (default) | `vector`

Internal convection heat transfer coefficient,
*hint*, in W/(m^2K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `int_tbl` |
| **Values:** | `[40 160 740 2000]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Internal mass flow rate breakpoints, int\_bpts** — Manifold internal air `linspace(0.0020,0.1100,4)` (default) | `vector`

Internal velocity breakpoints,
*xint*, in kg/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `int_bpts` |
| **Values:** | `linspace(0.0020,0.1100,4)` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
model** parameter.

### **Internal flow convection area, Aint\_conv** — Manifold internal air `0.125` (default) | `scalar`

Internal convection area,
*Aint\_conv*, in m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aint_conv` |
| **Values:** | `0.125` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `External wall
convection` for the **Heat transfer
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

Constant volume open thermodynamic system with heat transfer

The Control Volume System block models a constant
volume open thermodynamic system with heat transfer. The block uses
the conservation of mass and energy, assuming an ideal gas, to determine
the pressure and temperature. The block implements an automotive-specific Constant
Volume Pneumatic Chamber block that includes thermal effects
related to the under hood of passenger vehicles. You can specify heat
transfer models:

- Constant
- External input
- External wall convection

You can use the Control Volume System block to
represent engine components that contain volume, including pipes and
manifolds.

### Thermodynamics

The Control Volume System block implements a
constant volume chamber containing an ideal gas. To determine the
rate changes in temperature and pressure, the block uses the continuity
equation and the first law of thermodynamics.

dTvoldt=RTvolcvVchPvol(∑(qi−Tvolcvm˙i)−Qwall)dPvoldt=PvolTvoldTvoldt+RTvolVch∑m˙i

The block uses this equation for the volume-specific enthalpy.

hvol=cpTvol

The equations use these variables.

|  |  |
| --- | --- |
| m˙i | Mass flow rate at port |
| *qi* | Heat flow rate at port |
| *Vch* | Chamber volume |
| *Pvol* | Absolute pressure in the chamber |
| *R* | Ideal gas constant |
| *cv* | Specific heat at constant volume |
| *Tvol* | Absolute gas temperature |
| *Qwall* | Wall heat transfer rate |
| *hvol* | Volume-specific enthalpy |
| *cp* | Specific heat capacity |

### Mass Fractions

The Control Volume Source block is part of a
flow network. Blocks in the network determine the mass fractions that
the block will track during simulation. The block can track these
mass fractions:

- `O2` — Oxygen
- `N2` — Nitrogen
- `UnburnedFuel` — Unburned
  fuel
- `CO2` — Carbon dioxide
- `H2O` — Water
- `CO` — Carbon monoxide
- `NO` — Nitric oxide
- `NO2` — Nitrogen dioxide
- `PM` — Particulate matter
- `Air` — Air
- `BurnedGas` — Burned gas

Using the conservation of mass for each gas constituent, this
equation determines the rate change:

dyvol,jdt=RTvolPvolVch(∑m˙iyi,j+yvol,j∑m˙i)

The equations use these variables.

|  |  |
| --- | --- |
| *Vch* | Chamber volume |
| *Pvol* | Absolute pressure in the chamber |
| *R* | Ideal gas constant |
| *Tvol* | Absolute gas temperature |
| *yi,j* | I-th port mass fraction for j = O2, N2, unburned fuel, CO2, H2O, CO, NO, NO2, PM, air, and burned gas |
| *yvol,j* | Control volume mass fraction for j = O2, N2, unburned fuel, CO2, H2O, CO, NO, NO2, PM, air, and burned gas |
| m˙i | Mass flow rate for i = O2, N2, unburned fuel, CO2, H2O, CO, NO, NO2, PM, air, and burned gas |

### External Wall Convection Heat Transfer Model

To calculate the heat transfer, you can configure the Control
Volume Source block to calculate the heat transfer across
the wall of the control volume.

The block implements these equations to calculate the heat transfer, *Q1*,
from the internal control volume gas to the internal wall depth, *Dint\_cond*.

Q1=Q1,conv=Q1,cond

Q1,conv=hint(xint)•Aint\_conv•(Tint\_gas−Tw\_int)

Q1,cond=kint•Aint\_condDint\_cond•(Tw\_int−Tmass)

The block implements these equations to calculate the heat transfer, *Q2*,
from the external wall depth, *Dext\_cond* to
the external gas.

Q2=Q2,conv=hext(xext)•Aext\_conv•(Tw\_ext−Text\_gas)

Q2,cond=kext•Aext\_condDext\_cond•(Tmass−Tw\_ext)

This equation expresses the heat stored in the thermal mass.

dTmassdt=Q1−Q2cpwallmwall

The block determines the interior convection heat transfer coefficient
using a lookup table that is a function of the average mass flow rate.

m˙int\_gas=12∑|m˙i|

The equations use these variables.

|  |  |
| --- | --- |
| *Q1* | Heat flow from the internal gas to a specified wall depth |
| *Q1,conv* | Heat flow convection from the internal gas to the internal wall |
| *Q1,cond* | Conduction heat transfer rate |
| *Q2* | Heat transfer rate |
| *Q2,conv* | Convection heat transfer |
| *Q2,cond* | Heat flow conduction from the external middle portion of the wall to the external wall |
| *Qmass* | Heat stored in thermal mass |
| *hint* | Internal convection heat transfer coefficient |
| *xint* | Internal mass flow rate breakpoints |
| *Aint\_conv* | Internal flow convection area |
| *Tint\_gas* | Temperature of the gas inside the chamber |
| *Tw\_int* | Temperature of the inside wall of the chamber |
| *kint* | Internal wall thermal conductivity |
| *Aint\_cond* | Internal conduction area |
| *Dint\_cond* | Internal wall thickness |
| *hext* | External convection heat transfer coefficient |
| *xext* | External velocity breakpoints |
| *Aext\_conv* | External convection area |
| *Text\_gas* | External gas temperature |
| *Tw\_ext* | Temperature of the external wall of the chamber |
| *kext* | External wall thermal conductivity |
| *Aext\_cond* | External conduction area |
| *Dext\_cond* | External wall thickness |
| *Tmass* | Temperature of the thermal mass |
| *cp\_wall* | Wall heat capacity |
| *mwall* | Thermal mass |
| *Flwspd* | External flow velocity |
| m˙int\_gas | Average internal mass flow rate |

### Power Accounting

For the power accounting, the block implements these equation based on the number
of inlet and outlet ports.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrHeatFlwi` | Port *`i`* heat flow | *qi* |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrHeatTrnsfr` | Heat transfer rate from wall to control volume | -*Qwall* |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrHeatStored` | Rate of heat stored in the control volume | (∑​(qi)−Qwall) |

For example, if you configure your block with 3 input ports and 2 outlet ports,
the block implements these equations

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrHeatFlw1` | Inlet port 1 heat flow | *q1* |
| `PwrHeatFlw2` | Inlet port 2 heat flow | *q2* |
| `PwrHeatFlw3` | Inlet port 3 heat flow | *q3* |
| `PwrHeatFlw4` | Outlet port 4 heat flow | *q4* |
| `PwrHeatFlw5` | Outlet port 5 heat flow | *q5* |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrHeatTrnsfr` | Heat transfer rate from wall to control volume | -*Qwall* |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrHeatStored` | Rate of heat stored in the control volume | (∑​(qi)−Qwall) |
