---
type: simulink-block
title: 'SI Core Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'sicoreengine'
documentation_source_path: 'ref/sicoreengine.html'
language: en
---

# SI Core Engine

## Ports

### Input

### **InjPw** — Fuel injector pulse-width `scalar`

Fuel injector pulse-width, Pwinj,
in ms.

### **SpkAdv** — Spark advance `scalar`

Spark advance, *SA*, in degrees crank angle
before top dead center (degBTDC).

#### Dependencies

To create this port, for the **Torque model** parameter,
select `Torque Structure`.

### **ICP** — Intake cam phase angle command `scalar`

Intake cam phase angle command, φICPCMD, in degCrkAdv, or crank degrees of advance relative to
the intake phaser park position.

#### Dependencies

To create this port, for the **Air mass flow model** parameter,
select `Dual-Independent Variable Cam Phasing`.

### **ECP** — Exhaust cam phase angle command `scalar`

Exhaust cam phase angle command, φECPCMD, in degCrkRet, or crank degrees of retard relative to
the exhaust phaser park position.

#### Dependencies

To create this port, for the **Air mass flow model** parameter,
select `Dual-Independent Variable Cam Phasing`.

### **AmbPrs** — Ambient pressure `scalar`

Ambient pressure, PAmb, in Pa.

#### Dependencies

To create this port, for the **Air mass flow model** parameter,
select `Dual-Independent Variable Cam Phasing`.

### **EngSpd** — Engine speed `scalar`

Engine speed, *N*, in rpm.

### **Ect** — Engine cooling temperature `scalar`

Engine cooling temperature,
*Tcoolant*, in K.

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intk** — Intake port pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the upstream:

- `Prs` — Pressure, in Pa
- `Temp` — Temperature, in K
- `Enth` — Specific enthalpy,
  in J/kg
- `MassFrac` — Intake port mass fractions,
  dimensionless. EGR mass flow at the intake port is burned
  gas.

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

### **Exh** — Exhaust port pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the exhaust:

- `Prs` — Pressure, in Pa
- `Temp` — Temperature, in K
- `Enth` — Specific enthalpy,
  in J/kg
- `MassFrac` —
  Exhaust port mass fractions, dimensionless.

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
### Output

### **Info** — Bus signal bus

Bus signal that contains these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `IntkGasMassFlw` | | | Engine intake air mass flow | m˙air | kg/s |
| `IntkAirMassFlw` | | | Engine intake port mass flow | m˙intk | kg/s |
| `NrmlzdAirChrg` | | | Engine load (that is, normalized cylinder air mass) corrected for final steady-state cam phase angles | L | N/A |
| `Afr` | | | Air-fuel ratio at engine exhaust port | AFR | N/A |
| `FuelMassFlw` | | | Fuel flow into engine | m˙fuel | kg/s |
| `FuelVolFlw` | | | Volumetric fuel flow | *Qfuel* | m3/s |
| `ExhManGasTemp` | | | Exhaust gas temperature at exhaust manifold inlet | Texh | K |
| `EngTrq` | | | Engine brake torque | Tbrake | N·m |
| `EngSpd` | | | Engine speed | N | rpm |
| `IntkCamPhase` | | | Intake cam phaser angle | φICP i | crank degrees advance relative to park |
| `ExhCamPhase` | | | Exhaust cam phaser angle | φECP | crank degrees retard relative to park |
| `CrkAng` | | | Engine crankshaft absolute angle | ∫0(360)CpsEngSpd18030dθ  where Cps is crankshaft revolutions per power stroke | degrees crank angle |
| `EgrPct` | | | EGR percent | *EGRpct* | N/A |
| `EoAir` | | | EO air mass flow rate | m˙exh | kg/s |
| `EoBrndGas` | | | EO burned gas mass flow rate | *yexh,b* | kg/s |
| `EoHC` | | | EO hydrocarbon emission mass flow rate | *yexh,HC* | kg/s |
| `EoCO` | | | EO carbon monoxide emission mass flow rate | *yexh,CO* | kg/s |
| `EoNOx` | | | EO nitric oxide and nitrogen dioxide emissions mass flow rate | *yexh,NOx* | kg/s |
| `EoCO2` | | | EO carbon dioxide emission mass flow rate | *yexh,CO2* | kg/s |
| `EoPm` | | | EO particulate matter emission mass flow rate | *yexh,PM* | kg/s |
| `CylPrs` | | | Cylinder pressure | N/A | Pa |
| `EngTrqCrk` | | | Crank-angle based engine torque | N/A | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrIntkHeatFlw` | Intake heat flow | m˙intkhintk | W |
| `PwrExhHeatFlw` | Exhaust heat flow | −m˙exhhexh | W |
| `PwrCrkshft` | Crankshaft power | −Tbrakeω | W |
| `PwrNotTrnsfrd` | `PwrFuel` | Fuel input power | m˙fuelLHV | W |
| `PwrLoss` | For **Torque model** set to `Simple Torque Lookup`:  All losses | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh | W |
| `PwrFricLoss` | For **Torque model** set to `Torque Structure`:  Friction loss | −Tfricω | W |
| `PwrPumpLoss` | For **Torque model** set to `Torque Structure`:  Pumping loss | −Tpumpω | W |
| `PwrHeatTrnsfrLoss` | For **Torque model** set to `Torque Structure`:  Heat transfer loss | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω | W |
| `PwrStored` | *Not used* | | | |

### **EngTrq** — Engine brake torque `scalar`

Engine brake torque, Tbrake, in N·m.

### **Intk** — Intake port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port

Bus containing:

- `MassFlwRate` — Intake port
  mass flow rate, in kg/s
- `HeatFlwRate` — Intake port
  heat flow rate, in J/s
- `Temp` — Intake port temperature,
  in K
- `MassFrac` —
  Intake port mass fractions, dimensionless.

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

### **Exh** — Exhaust port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port

Bus containing:

- `MassFlwRate` — Exhaust port
  mass flow rate, in kg/s
- `HeatFlwRate` — Exhaust heat
  flow rate, in J/s
- `Temp` — Exhaust temperature,
  in K
- `MassFrac` —
  Exhaust port mass fractions, dimensionless.

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

### **Air mass flow model** — Select air mass flow model `Dual-Independent Variable Cam Phasing` (default) | `Simple Speed-Density`

To calculate engine air mass flow, configure the SI engine to
use either of these air mass flow models.

| Air Mass Flow Model | Description |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | Uses the speed-density equation to calculate the engine air mass flow, relating the engine air mass flow to the intake manifold pressure and engine speed. Consider using this air mass flow model in engines with fixed valvetrain designs. |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | To calculate the engine air mass flow, the dual-independent cam phaser model uses:  - Empirical calibration parameters developed from engine   mapping measurements - Desktop calibration parameters derived from engine   computer-aided design (CAD) data  In contrast to typical embedded air mass flow calculations based on direct air mass flow measurement with an air mass flow (MAF) sensor, this air mass flow model offers:  - Elimination of MAF sensors in dual cam-phased valvetrain   applications - Reasonable accuracy with changes in altitude - Semiphysical modeling approach - Bounded behavior - Suitable execution time for electronic control unit (ECU)   implementation - Systematic development of a relatively small number of   calibration parameters |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `AirMassFlowOptionPopup` |
| **Values:** | `Dual-Independent Variable Cam Phasing` (default) | `Simple Speed-Density` |
| **Data Types:** | `character vector` |

#### Dependencies

The table summarizes the parameter dependencies.

| Air Mass Flow Model | Enables Parameters |
| --- | --- |
| `Dual-Independent Variable Cam Phasing` | **Cylinder volume at intake valve close table, f\_vivc**  **Cylinder volume intake cam phase breakpoints, f\_vivc\_icp\_bpt**  **Cylinder trapped mass correction factor, f\_tm\_corr**  **Normalized density breakpoints, f\_tm\_corr\_nd\_bpt**  **Engine speed breakpoints, f\_tm\_corr\_n\_bpt**  **Air mass flow, f\_mdot\_air**  **Exhaust cam phase breakpoints, f\_mdot\_air\_ecp\_bpt**  **Trapped mass flow breakpoints, f\_mdot\_trpd\_bpt**  **Air mass flow correction factor, f\_mdot\_air\_corr**  **Engine load breakpoints for air mass flow correction, f\_mdot\_air\_corr\_ld\_bpt**  **Engine speed breakpoints for air mass flow correction, f\_mdot\_air\_n\_bpt** |
| `Simple Speed Density` | **Speed-density volumetric efficiency, f\_nv**  **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt**  **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** |

### **Torque model** — Select torque model `Torque Structure` (default) | `Simple Torque Lookup`

To calculate the brake torque, configure the SI engine to use
either of these torque models.

| Brake Torque Model | Description |
| --- | --- |
| SI Engine Torque Structure Model | For the structured brake torque calculation, the SI engine uses tables for the inner torque, friction torque, optimal spark, spark efficiency, and lambda efficiency.  If you select **Crank angle pressure and torque** on the block **Torque** tab, you can:  - Simulate advanced closed-loop engine controls in desktop   simulations and on HIL bench, based on cylinder pressure   recorded from a model or laboratory test as a function of   crank angle. - Simulate driveline vibrations downstream of the engine due   to high-frequency crankshaft torsionals. - Simulate engine misfires due to lean operation or spark   plug fouling by using the injector pulse width input. - Simulate cylinder deactivation effect (closed intake and   exhaust valves, no injected fuel) on individual cylinder   pressures, mean-value airflow, mean-value torque, and   crank-angle-based torque. - Simulate the fuel-cut effect on individual cylinder   pressure, mean-value torque, and crank-angle-based   torque. |
| SI Engine Simple Torque Model | For the simple brake torque calculation, the SI engine block uses a torque lookup table map that is a function of engine speed and load. |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `TrqOptionPopup` |
| **Values:** | `Torque Structure` (default) | `Simple Torque Lookup` |
| **Data Types:** | `character vector` |

#### Dependencies

The table summarizes the parameter dependencies.

| Torque Model | Enables Parameters |
| --- | --- |
| `Torque Structure` | **Inner torque table, f\_tq\_inr**  **Friction torque table, f\_tq\_fric**  **Engine temperature modifier on friction torque, f\_fric\_temp\_mod**  **Engine temperature modifier breakpoints, f\_fric\_temp\_bpt**  **Pumping work table, f\_tq\_pump**  **Optimal spark table, f\_sa\_opt**  **Inner torque load breakpoints, f\_tq\_inr\_l\_bpt**  **Inner torque speed breakpoints, f\_tq\_inr\_n\_bpt**  **Spark efficiency table, f\_m\_sa**  **Spark retard from optimal, f\_del\_sa\_bpt**  **Lambda efficiency, f\_m\_lam**  **Lambda breakpoints, f\_m\_lam\_bpt** |
| `Simple Torque Lookup` | **Torque table, f\_tq\_nl**  **Torque table load breakpoints, f\_tq\_nl\_l\_bpt**  **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** |

#### Air

### **Number of cylinders, NCyl** — Engine cylinders `4` (default) | `scalar`

Number of engine cylinders, Ncyl.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `NCyl` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Crank revolutions per power stroke, Cps** — Revolutions per stroke `2` (default) | `scalar`

Crankshaft revolutions per power stroke, Cps, in rev/stroke.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Cps` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Total displaced volume, Vd** — Volume `0.0015` (default) | `scalar`

Displaced volume, Vd, in m^3.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Vd` |
| **Values:** | `0.0015` (default) | `scalar` |
| **Data Types:** | `double` |

### **Ideal gas constant air, Rair** — Constant `287` (default) | `scalar`

Ideal gas constant, Rair, in J/(kg·K).

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Rair` |
| **Values:** | `287` (default) | `scalar` |
| **Data Types:** | `double` |

### **Air standard pressure, Pstd** — Pressure `101325` (default) | `scalar`

Standard air pressure, Pstd, in Pa.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Pstd` |
| **Values:** | `101325` (default) | `scalar` |
| **Data Types:** | `double` |

### **Air standard temperature, Tstd** — Temperature `293.15` (default) | `scalar`

Standard air temperature, Tstd, in K.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Tstd` |
| **Values:** | `293.15` (default) | `scalar` |
| **Data Types:** | `double` |

### **Speed-density volumetric efficiency, f\_nv** — Lookup table `array`

The engine volumetric efficiency lookup table, fηv,
is a function of intake manifold absolute pressure and engine speed

ηv=fηv(MAP,N)

where:

- ηv is
  engine volumetric efficiency, dimensionless.
- *MAP* is intake manifold absolute
  pressure, in KPa.
- *N* is engine speed, in rpm.

3D plot of engine volumetric efficiency versus intake manifold absolute pressure and engine speed

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Simple
Speed-Density`.

### **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — Breakpoints `[31 40.6428571428571 50.2857142857143 59.9285714285714 69.5714285714286 79.2142857142857 88.8571428571429 98.5 108.142857142857 117.785714285714 127.428571428571 137.071428571429 146.714285714286 156.357142857143 166]` (default) | `array`

Intake manifold pressure breakpoints for speed-density volumetric
efficiency lookup table, in KPa.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv_prs_bpt` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Simple
Speed-Density`.

### **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `array`

Engine speed breakpoints for speed-density volumetric efficiency lookup
table, in rpm.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv_n_bpt` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Simple
Speed-Density`.

### **Cylinder volume at intake valve close table, f\_vivc** — 2-D lookup table `array`

The cylinder volume at intake valve close table (IVC), fVivc is
a function of the intake cam phaser angle

VIVC=fVivc(φICP)

where:

- VIVC is
  cylinder volume at IVC, in L.
- φICP is intake cam phaser angle in crank degrees of advance relative to
  the intake phaser park position.

Plot of cylinder volume versus intake cam phaser angle

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_vivc` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Cylinder volume intake cam phase breakpoints, f\_vivc\_icp\_bpt** — Breakpoints `[0 2.6316 5.2632 7.8947 10.5263 13.1579 15.7895 18.4211 21.0526 23.6842 26.3158 28.9474 31.5789 34.2105 36.8421 39.4737 42.1053 44.7368 47.3684 50]` (default) | `vector`

Cylinder volume intake cam phase breakpoints, in L.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_vivc_icp_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Cylinder trapped mass correction factor, f\_tm\_corr** — Lookup table `array`

The trapped mass correction factor table, fTMcorr,
is a function of the normalized density and engine speed

TMcorr=fTMcorr(ρnorm, N)

where:

- TMcorr,
  is trapped mass correction multiplier, dimensionless.
- ρnorm is
  normalized density, dimensionless.
- *N* is engine speed, in rpm.

3D plot of trapped mass correction multiplier versus normalized density and engine speed

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tm_corr` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Normalized density breakpoints, f\_tm\_corr\_nd\_bpt** — Breakpoints `[0.3 0.38947 0.47895 0.56842 0.65789 0.74737 0.83684 0.92632 1.0158 1.1053 1.1947 1.2842 1.3737 1.4632 1.5526 1.6421 1.7316 1.8211 1.9105 2]` (default) | `vector`

Normalized density breakpoints, dimensionless.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tm_corr_nd_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Engine speed breakpoints, f\_tm\_corr\_n\_bpt** — Breakpoints `[750 973.6842 1197.3684 1421.0526 1644.7368 1868.4211 2092.1053 2315.7895 2539.4737 2763.1579 2986.8421 3210.5263 3434.2105 3657.8947 3881.5789 4105.2632 4328.9474 4552.6316 4776.3158 5000]` (default) | `vector`

Engine speed breakpoints, in rpm.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tm_corr_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Intake mass flow, f\_mdot\_intk** — Lookup table `array`

The phaser intake mass flow model lookup table is a function of
exhaust cam phaser angles and trapped air mass flow

m˙intkideal=fintkideal(φECP,TMflow)

where:

- m˙intkideal is engine intake port mass flow at arbitrary cam phaser angles, in
  g/s.
- φECP is exhaust cam phaser angle in crank degrees of retard relative to
  the exhaust phaser park position.
- TMflow is flow rate equivalent to corrected trapped mass at the current
  engine speed, in g/s.

3D plot of air mass flow versus exhaust cam phaser angle and flow rate equivalent

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mdot_intk` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Exhaust cam phase breakpoints, f\_mdot\_air\_ecp\_bpt** — Breakpoints `[0 2.6316 5.2632 7.8947 10.5263 13.1579 15.7895 18.4211 21.0526 23.6842 26.3158 28.9474 31.5789 34.2105 36.8421 39.4737 42.1053 44.7368 47.3684 50]` (default) | `vector`

Exhaust cam phaser breakpoints for air mass flow lookup table, in crank
degrees of retard relative to park.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mdot_air_ecp_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Trapped mass flow breakpoints, f\_mdot\_trpd\_bpt** — Breakpoints `[0 5.7895 11.5789 17.3684 23.1579 28.9474 34.7368 40.5263 46.3158 52.1053 57.8947 63.6842 69.4737 75.2632 81.0526 86.8421 92.6316 98.4211 104.2105 110]` (default) | `vector`

Trapped mass flow breakpoints for air mass flow lookup table, in
g/s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mdot_trpd_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Air mass flow correction factor, f\_mdot\_air\_corr** — Lookup table `array`

The intake air mass flow correction lookup table, faircorr, is a function of ideal load and engine speed

m˙air=m˙intkidealfaircorr(Lideal,N)

where:

- Lideal is engine load (normalized cylinder air mass) at arbitrary cam
  phaser angles, uncorrected for final steady-state cam phaser angles,
  dimensionless.
- *N* is engine speed, in rpm.
- m˙air is engine intake air mass flow final correction at steady-state
  cam phaser angles, in g/s.
- m˙intkideal is engine intake port mass flow at arbitrary cam phaser angles, in
  g/s.

3D plot of engine intake air mass flow final correction versus engine load and engine speed

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mdot_air_corr` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Engine load breakpoints for air mass flow correction, f\_mdot\_air\_corr\_ld\_bpt** — Breakpoints `vector`

Engine load breakpoints for air mass flow final correction,
dimensionless.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mdot_air_corr_ld_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

### **Engine speed breakpoints for air mass flow correction, f\_mdot\_air\_n\_bpt** — Breakpoints `vector`

Engine speed breakpoints for air mass flow final correction, in
rpm.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `f_mdot_air_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Air mass flow
model** parameter, select `Dual-Independent
Variable Cam Phasing`.

#### Torque

### **Torque table, f\_tq\_nl** — Lookup table `[L x N] array`

For the simple torque lookup table model, the SI engine uses
a lookup table map that is a function of engine speed and load, Tbrake=fTnL(L,N),
where:

- Tbrake is
  engine brake torque after accounting for spark advance, AFR, and friction
  effects, in N·m.
- *L* is engine load, as a normalized
  cylinder air mass, dimensionless.
- *N* is engine speed, in rpm.

3D plot of engine brake torque after accounting for spark advance versus engine load and engine speed

The simple torque lookup model assumes that the calibration has negative torque
values to indicate the non-firing engine load (L) versus speed (N) condition. The
calibrated table (L-by-N) contains the non-firing data in the first table row
(1-by-N). When the fuel delivered to the engine is zero, the model uses the data in
the first table row (1-by-N) at or above 100 AFR. 100 AFR results from fuel cutoff
or very lean operation where combustion cannot occur.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Simple Torque Lookup`.

### **Torque table load breakpoints, f\_tq\_nl\_l\_bpt** — Breakpoints `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]` (default) | `vector` | `[1 x L] vector`

Engine load breakpoints, *L*, dimensionless.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Simple Torque Lookup`.

### **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector` | `[1 x N] vector`

Engine speed breakpoints, *N*, in rpm.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Simple Torque Lookup`.

### **Crank angle pressure and torque** — Enable Crank angle signals `off` (default) | `on`

If you select **Crank angle pressure and torque** on the block
**Torque** tab, you can:

- Simulate advanced closed-loop engine controls in desktop simulations
  and on HIL bench, based on cylinder pressure recorded from a model or
  laboratory test as a function of crank angle.
- Simulate driveline vibrations downstream of the engine due to
  high-frequency crankshaft torsionals.
- Simulate engine misfires due to lean operation or spark plug fouling
  by using the injector pulse width input.
- Simulate cylinder deactivation effect (closed intake and exhaust
  valves, no injected fuel) on individual cylinder pressures, mean-value
  airflow, mean-value torque, and crank-angle-based torque.
- Simulate the fuel-cut effect on individual cylinder pressure,
  mean-value torque, and crank-angle-based torque.

#### Dependencies

To enable this parameter, set **Torque model** to
`Torque Structure`.

### **Cylinder pressure, f\_crk\_prs** — Cylinder pressure table `L x M x N` array

Cylinder pressure table *Prs*, as a function of speed
*N*, load *L*, and crank angle
*M*, in Pa.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`. Select **Crank angle
pressure and torque**.

### **Brake torque, f\_crk\_btq** — Brake torque table `L x M x N` array

Brake torque table *Tbrake*, as a function
of speed *N*, load *L*, and crank angle
*M*, in N·m.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`. Select **Crank angle
pressure and torque**.

### **Speed breakpoints, f\_crk\_n\_bpt** — Speed breakpoints `[750 5000]` (default) | `1 x N` vector

Speed breakpoints, *N*, in rpm.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`. Select **Crank angle
pressure and torque**.

### **Load breakpoints, f\_crk\_l\_bpt** — Load breakpoints `[0.2 1.4]` (default) | `1 x L` vector

Load breakpoints, *L*. No dimension.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`. Select **Crank angle
pressure and torque**.

### **Crank angle breakpoints, f\_crk\_ang\_bpt** — Crank angle breakpoints `[60 660]` (default) | `1 x M` vector

Crank angle breakpoints, *M*, in deg.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`. Select **Crank angle
pressure and torque**.

### **TDC compression angles by cylinder, f\_crk\_tdc\_ang** — TDC compression angles by cylinder `[0 540 180 360]` (default) | vector

Top dead center (TDC) compression angles by cylinder, in deg.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`. Select **Crank angle
pressure and torque**.

### **Inner torque table, f\_tq\_inr** — Lookup table `array`

The inner
torque lookup table, fTqinr,
is a function of engine speed and engine load, Tqinr=fTqinr(L,N),
where:

- Tqinr is
  inner torque based on gross indicated mean effective pressure, in
  N·m.
- *L* is engine load at arbitrary cam
  phaser angles, corrected for final steady-state cam phaser angles,
  dimensionless.
- *N* is engine speed, in rpm.

3D plot of inner torque based on gross indicated mean effective pressure versus engine load at arbitrary cam phaser angles and engine speed

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Friction torque table, f\_tq\_fric** — Lookup table `array`

The friction torque lookup table, fTfric,
is a function of engine speed and engine load, Tfric=fTfric(L,N),
where:

- Tfric is
  friction torque offset to inner torque, in N·m.
- *L* is engine load at arbitrary cam
  phaser angles, corrected for final steady-state cam phaser angles,
  dimensionless.
- *N* is engine speed, in rpm.

3D plot of friction torque offset to inner torque versus engine load at arbitrary cam phaser angles and engine speed

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Engine temperature modifier on friction torque, f\_fric\_temp\_mod** — Lookup table `[3.96 3.22 2.56 2.26 2.11 2 1.9 1.83 1.76 1.7 1.65 1.6 1.55 1.49 1.44 1.41 1.38 1.35 1.32 1.3 1.27 1.25 1.24 1.21 1.2 1.18 1.16 1.15 1.13 1.12 1.11 1.1 1.09 1.08 1.07 1.06 1.05 1.05 1.04 1.03 1.02 1.02 1.01 1.01 1 1 1 0.999 0.997 0.995 0.993 0.991 0.989 0.987]` (default) | `vector` | `vector`

Engine temperature modifier on friction torque,
*ƒfric,temp*, dimensionless.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Engine temperature modifier breakpoints, f\_fric\_temp\_bpt** — Breakpoints `[274 276 278 280 282 284 286 288 290 292 294 296 298 300 302 304 306 308 310 312 314 316 318 320 322 324 326 328 330 332 334 336 338 340 342 344 346 348 350 352 354 356 358 360 362 364 366 368 370 372 374 376 378 380]` (default) | `vector` | `vector`

Engine temperature modifier breakpoints, in K.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Pumping torque table, f\_tq\_pump** — Lookup table `array`

The pumping torque lookup
table, *ƒTpump*, is a function of engine load and engine
speed,
`Tpump=ƒTpump(L,N)`, where:

- *Tpump* is pumping torque, in N·m.
- *L* is engine load, as a normalized cylinder air mass,
  dimensionless.
- *N* is engine speed, in rpm.

3D plot of pumping torque versus engine load and engine speed

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Optimal spark table, f\_sa\_opt** — Lookup table `array`

The optimal spark lookup table, fSAopt,
is a function of engine speed and engine load, SAopt=fSAopt(L,N),
where:

- *SAopt* is
  optimal spark advance timing for maximum inner torque at stoichiometric
  air-fuel ratio (AFR), in deg.
- *L* is engine load at arbitrary cam
  phaser angles, corrected for final steady-state cam phaser angles,
  dimensionless.
- *N* is engine speed, in rpm.

3D plot of optimal spark advance timing for maximum inner torque at stoichiometric air-fuel ratio (AFR) versus engine load and engine speed

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Inner torque load breakpoints, f\_tq\_inr\_l\_bpt** — Breakpoints `[0.2 0.28571 0.37143 0.45714 0.54286 0.62857 0.71429 0.8 0.88571 0.97143 1.0571 1.1429 1.2286 1.3143 1.4]` (default) | `vector`

Inner torque load breakpoints, dimensionless.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Inner torque speed breakpoints, f\_tq\_inr\_n\_bpt** — Breakpoints `[750 1053.5714 1357.1429 1660.7143 1964.2857 2267.8571 2571.4286 2875 3178.5714 3482.1429 3785.7143 4089.2857 4392.8571 4696.4286 5000]` (default) | `vector`

Inner torque speed breakpoints, in rpm.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Spark efficiency table, f\_m\_sa** — Lookup table `array`

The spark efficiency lookup table, fMsa,
is a function of the spark retard from optimal

Msa=fMsa(ΔSA)ΔSA=SAopt−SA

where:

- Msa is
  the spark retard efficiency multiplier, dimensionless.
- ΔSAis
  the spark retard timing distance from optimal spark advance, in deg.

Spark retard efficiency versus spark retard timing distance

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Spark retard from optimal, f\_del\_sa\_bpt** — Breakpoints `[0 0.75 1.5 2.25 3 3.75 4.5 5.25 6 6.75 7.5 8.25 9 9.75 10.5 11.25 12 12.75 13.5 14.25 15 15.75 16.5 17.25 18 18.75 19.5 20.25 21 21.75 22.5 23.25 24 24.75 25.5 26.25 27 27.75 28.5 29.25 30 30.75 31.5 32.25 33 33.75 34.5 35.25 36 36.75 37.5 38.25 39 39.75 40.5 41.25 42 42.75 43.5 44.25 45 45.75 46.5 47.25 48]` (default) | `vector`

Spark retard from optimal inner torque timing breakpoints, in deg.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Lambda efficiency, f\_m\_lam** — Lookup table `array`

The lambda efficiency lookup table, fMλ,
is a function of lambda, Mλ=fMλ(λ),
where:

- Mλ is
  the lambda multiplier on inner torque to account for the air-fuel
  ratio (AFR) effect, dimensionless.
- λ is
  lambda, AFR normalized to stoichiometric fuel AFR, dimensionless.

Plot of lambda multiplier versus lambda

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

### **Lambda breakpoints, f\_m\_lam\_bpt** — Breakpoints `[0.65 0.7 0.75 0.8 0.85 0.9 0.95 1 1.05 1.1]` (default) | `vector`

Lambda effect on inner torque lambda breakpoints, dimensionless.

#### Dependencies

To enable this parameter, for the **Torque model** parameter,
select `Torque Structure`.

#### Exhaust

### **Exhaust temperature table, f\_t\_exh** — Lookup table `array`

The exhaust temperature
lookup table, fTexh,
is a function of engine load and engine speed

Texh=fTexh(L,N)

where:

- *Texh* is
  engine exhaust temperature, in K.
- *L* is normalized cylinder air mass
  or engine load, dimensionless.
- *N* is engine speed, in rpm.

3D plot of engine exhaust temperature versus engine speed and engine load

### **Load breakpoints, f\_t\_exh\_l\_bpt** — Breakpoints `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]` (default) | `vector`

Engine load breakpoints used for exhaust temperature lookup table,
dimensionless.

### **Speed breakpoints, f\_t\_exh\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector`

Engine speed breakpoints used for exhaust temperature lookup table, in
rpm.

### **Exhaust gas specific heat at constant pressure, cp\_exh** — Specific heat `1005` (default) | `scalar`

Exhaust gas-specific heat, Cpexh, in J/(kg·K).

### **CO2 mass fraction table, f\_CO2\_frac** — Carbon dioxide (CO2) emission lookup table `array`

The SI Core Engine CO2 emission
mass fraction lookup table is a function of engine torque and engine
speed, *CO2 Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *CO2 Mass Fraction* is the CO2 emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of CO2 emission mass fraction versus engine speed and engine torque

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **CO2**.

### **CO mass fraction table, f\_CO\_frac** — Carbon monoxide (CO) emission lookup table `array`

The SI Core Engine CO emission
mass fraction lookup table is a function of engine torque and engine
speed, *CO Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *CO Mass Fraction* is the CO emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of CO emission mass fraction versus engine speed and engine torque

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **CO**.

### **HC mass fraction table, f\_HC\_frac** — Hydrocarbon (HC) emission lookup table `array`

The SI Core Engine HC emission
mass fraction lookup table is a function of engine torque and engine
speed, *HC Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *HC Mass Fraction* is the HC emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of HC emission mass fraction versus engine speed and engine torque

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **HC**.

### **NOx mass fraction table, f\_NOx\_frac** — Nitric oxide and nitrogen dioxide (NOx) emission lookup table `array`

The SI Core Engine NOx
emission mass fraction lookup table is a function of engine torque
and engine speed, *NOx Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *NOx Mass Fraction* is the NOx emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of NOx emission mass fraction versus commanded engine torque and engine speed

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **NOx**.

### **PM mass fraction table, f\_PM\_frac** — Particulate matter (PM) emission lookup table `array`

The SI Core Engine PM emission mass
fraction lookup table is a function of engine torque and engine speed where:

- *PM* is the PM emission mass fraction,
  dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **PM**.

### **Engine speed breakpoints, f\_exhfrac\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector`

Engine speed breakpoints used for the emission mass fractions lookup
tables, in rpm.

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **CO2**, **CO**,
**NOx**, **HC**, or
**PM**.

### **Engine torque breakpoints, f\_exhfrac\_trq\_bpt** — Breakpoints `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]` (default) | `vector`

Engine torque breakpoints used for the emission mass fractions lookup
tables, in N·m.

#### Dependencies

To enable this parameter, on the **Exhaust** tab,
select **CO2**, **CO**,
**NOx**, **HC**, or
**PM**.

#### Fuel

### **Injector slope, Sinj** — Slope `6.45161290322581` (default) | `scalar`

Fuel injector slope, Sinj, mg/ms.

### **Stoichiometric air-fuel ratio, afr\_stoich** — Air-fuel ratio `14.6` (default) | `scalar`

Air-fuel ratio, AFR.

### **Fuel lower heating value, fuel\_lhv** — Heating value `46e6` (default) | `scalar`

Fuel lower heating value, *LHV*, in J/kg.

### **Fuel specific gravity, fuel\_sg** — Specific gravity `0.745` (default) | `scalar`

Specific gravity of fuel,
*Sgfuel*, dimensionless.

## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Spark-ignition engine from intake to exhaust port

The SI Core Engine block implements a spark-ignition
(SI) engine from intake to exhaust port. You can use the block in
larger vehicle models, hardware-in-the-loop (HIL) engine control design,
or vehicle-level fuel economy and performance simulations.

The SI Core Engine block calculates:

- Brake torque
- Fuel flow
- Port gas mass flow, including exhaust gas recirculation (EGR)
- Air-fuel ratio (AFR)
- Exhaust temperature and exhaust mass flow rate
- Engine-out (EO) exhaust emissions

  - Hydrocarbon (HC)
  - Carbon monoxide (CO)
  - Nitric oxide and nitrogen dioxide (NOx)
  - Carbon dioxide (CO2)
  - Particulate matter (PM)

### Air Mass Flow

To calculate engine air mass flow, configure the SI engine to
use either of these air mass flow models.

| Air Mass Flow Model | Description |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | Uses the speed-density equation to calculate the engine air mass flow, relating the engine air mass flow to the intake manifold pressure and engine speed. Consider using this air mass flow model in engines with fixed valvetrain designs. |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | To calculate the engine air mass flow, the dual-independent cam phaser model uses:  - Empirical calibration parameters developed from engine   mapping measurements - Desktop calibration parameters derived from engine   computer-aided design (CAD) data  In contrast to typical embedded air mass flow calculations based on direct air mass flow measurement with an air mass flow (MAF) sensor, this air mass flow model offers:  - Elimination of MAF sensors in dual cam-phased valvetrain   applications - Reasonable accuracy with changes in altitude - Semiphysical modeling approach - Bounded behavior - Suitable execution time for electronic control unit (ECU)   implementation - Systematic development of a relatively small number of   calibration parameters |

### Brake Torque

To calculate the brake torque, configure the SI engine to use
either of these torque models.

| Brake Torque Model | Description |
| --- | --- |
| SI Engine Torque Structure Model | For the structured brake torque calculation, the SI engine uses tables for the inner torque, friction torque, optimal spark, spark efficiency, and lambda efficiency.  If you select **Crank angle pressure and torque** on the block **Torque** tab, you can:  - Simulate advanced closed-loop engine controls in desktop   simulations and on HIL bench, based on cylinder pressure   recorded from a model or laboratory test as a function of   crank angle. - Simulate driveline vibrations downstream of the engine due   to high-frequency crankshaft torsionals. - Simulate engine misfires due to lean operation or spark   plug fouling by using the injector pulse width input. - Simulate cylinder deactivation effect (closed intake and   exhaust valves, no injected fuel) on individual cylinder   pressures, mean-value airflow, mean-value torque, and   crank-angle-based torque. - Simulate the fuel-cut effect on individual cylinder   pressure, mean-value torque, and crank-angle-based   torque. |
| SI Engine Simple Torque Model | For the simple brake torque calculation, the SI engine block uses a torque lookup table map that is a function of engine speed and load. |

### Fuel Flow

To calculate the fuel flow, the SI Core Engine
block uses fuel injector characteristics and fuel injector pulse-width.

m˙fuel=NSinjPwinjNcylCps(60smin)(1000mgg)

To calculate the fuel economy for high-fidelity models, the block uses the
volumetric fuel flow.

Qfuel=m˙fuel(1000kgm3)Sgfuel

The equation uses these variables.

|  |  |
| --- | --- |
| m˙fuel | Fuel mass flow, g/s |
| ω | Engine rotational speed, rad/s |
| Cps | Crankshaft revolutions per power stroke, rev/stroke |
| Sinj | Fuel injector slope, mg/ms |
| Pwinj | Fuel injector pulse-width, ms |
| Ncyl | Number of engine cylinders |
| *N* | Engine speed, rpm |
| *Sgfuel* | Specific gravity of fuel |
| *Qfuel* | Volumetric fuel flow |

The block uses the internal signal `FlwDir` to track the direction of the flow.

### Air-Fuel Ratio

To calculate the air-fuel (AFR) ratio, the CI Core
Engine and SI Core Engine blocks implement this equation.

AFR=m˙airm˙fuel

The CI Core Engine uses this equation to calculate the
relative AFR.

λ=AFRAFRs

To calculate the exhaust gas recirculation (EGR), the blocks implement this
equation. The calculation expresses the EGR as a percent of the total intake port flow.

EGRpct=100m˙intk,bm˙intk=100yintk,b

The equations use these variables.

|  |  |
| --- | --- |
| AFR | Air-fuel ratio |
| *AFRs* | Stoichiometric air-fuel ratio |
| m˙intk | Engine air mass flow |
| m˙fuel | Fuel mass flow |
| λ | Relative AFR |
| *yintk,b* | Intake burned mass fraction |
| *EGRpct* | EGR percent |
| m˙intk,b | Recirculated burned gas mass flow rate |

### Exhaust

The block calculates the:

- Exhaust gas temperature
- Exhaust gas-specific enthalpy
- Exhaust gas mass flow rate
- Engine-out (EO) exhaust emissions:

  - Hydrocarbon (HC)
  - Carbon monoxide (CO)
  - Nitric oxide and nitrogen dioxide (NOx)
  - Carbon dioxide (CO2)
  - Particulate matter (PM)

The exhaust temperature determines the specific enthalpy.

hexh=CpexhTexh

The exhaust mass flow rate is the sum of the intake port air
mass flow and the fuel mass flow.

m˙exh=m˙intake+m˙fuel

To calculate the exhaust emissions, the block multiplies the
emission mass fraction by the exhaust mass flow rate. To determine
the emission mass fractions, the block uses lookup tables that are
functions of the engine torque and speed.

yexh,i=fi\_frac(Tbrake,N)m˙exh,i=m˙exhyexh,i

The fraction of air and fuel entering the intake port, injected
fuel, and stoichiometric AFR determine the air mass fraction that
exits the exhaust.

yexh,air=max[yin,air−m˙fuel+yin,fuelm˙intakem˙fuel+m˙intakeAFRs]

If the engine is operating at the stoichiometric or fuel rich
AFR, no air exits the exhaust. Unburned hydrocarbons and burned gas
comprise the remainder of the exhaust gas. This equation determines
the exhaust burned gas mass fraction.

yexh,b=max[(1−yexh,air−yexh,HC),0]

The equations use these variables.

|  |  |
| --- | --- |
| Texh | Engine exhaust temperature |
| hexh | Exhaust manifold inlet-specific enthalpy |
| Cpexh | Exhaust gas specific heat |
| m˙intk | Intake port air mass flow rate |
| m˙fuel | Fuel mass flow rate |
| m˙exh | Exhaust mass flow rate |
| yin,fuel | Intake fuel mass fraction |
| *yexh,i* | Exhaust mass fraction for i = CO2, CO, HC, NOx, air, burned gas, and PM |
| m˙exh,i | Exhaust mass flow rate for i = CO2, CO, HC, NOx, air, burned gas, and PM |
| *Tbrake* | Engine brake torque |
| *N* | Engine speed |
| *yexh,air* | Exhaust air mass fraction |
| *yexh,b* | Exhaust air burned mass fraction |

### Power Accounting

For the power accounting, the block implements equations that depend on **Torque model**.

When you set **Torque model** to `Simple Torque Lookup`, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrIntkHeatFlw` | Intake heat flow | m˙intkhintk |
| `PwrExhHeatFlw` | Exhaust heat flow | −m˙exhhexh |
| `PwrCrkshft` | Crankshaft power | −Tbrakeω |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFuel` | Fuel input power | m˙fuelLHV |
| `PwrLoss` | All losses | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | *Not used* | | |

When you set **Torque model** to `Torque Structure`, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrIntkHeatFlw` | Intake heat flow | m˙intkhintk |
| `PwrExhHeatFlw` | Exhaust heat flow | −m˙exhhexh |
| `PwrCrkshft` | Crankshaft power | −Tbrakeω |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFuel` | Fuel input power | m˙fuelLHV |
| `PwrFricLoss` | Friction loss | −Tfricω |
| `PwrPumpLoss` | Pumping loss | −Tpumpω |
| `PwrHeatTrnsfrLoss` | Heat transfer loss | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | *Not used* | | |

|  |  |
| --- | --- |
| *hexh* | Exhaust manifold inlet-specific enthalpy |
| *hintk* | Intake port specific enthalpy |
| m˙intk | Intake port air mass flow rate |
| m˙fuel | Fuel mass flow rate |
| m˙exh | Exhaust mass flow rate |
| *ω* | Engine speed |
| *Tbrake* | Brake torque |
| *Tpump* | Engine pumping work offset to inner torque |
| *Tfric* | Engine friction torque |
| *LHV* | Fuel lower heating value |
