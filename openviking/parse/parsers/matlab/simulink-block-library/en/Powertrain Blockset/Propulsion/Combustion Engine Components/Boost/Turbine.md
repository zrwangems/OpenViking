---
type: simulink-block
title: 'Turbine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Boost'
documentation_page: 'turbine'
documentation_source_path: 'ref/turbine.html'
language: en
---

# Turbine

## Ports
```yaml
ports:
- name: Ds
  summary: Drive shaft speed two-way connector port
  direction: input
- name: A
  summary: Inlet pressure, temperature, enthalpy, mass fractions two-way connector port
  direction: input
- name: B
  summary: Outlet pressure, temperature, enthalpy, mass fractions two-way connector port
  direction: input
- name: RackPos
  summary: Rack position scalar
  direction: input
- name: WgAreaPct
  summary: Wastegate area percent scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: Ds
  summary: Drive shaft torque two-way connector port
  direction: output
- name: A
  summary: Inlet mass flow rate, heat flow rate, temperature, mass fractions two-way connector port
  direction: output
- name: B
  summary: Outlet mass flow rate, heat flow rate, temperature, mass fractions two-way connector port
  direction: output
```

### Input

### **Ds** — Drive shaft speed two-way connector port

`ShaftSpd` — Signal containing the drive
shaft angular speed, ω, in rad/s.

### **A** — Inlet pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the inlet control volume:

- `InPrs` — Pressure, pinlet, in Pa
- `InTemp` — Temperature, Tinlet, in K
- `InEnth` — Specific enthalpy, hinlet, in J/kg

### **B** — Outlet pressure, temperature, enthalpy, mass fractions two-way connector port

Bus containing the outlet control volume:

- `OutPrs` — Pressure, poutlet, in Pa
- `OutTemp` — Temperature, Toutlet, in K
- `OutEnth` — Specific enthalpy, houtlet, in J/kg

### **RackPos** — Rack position `scalar`

Variable geometry turbine rack position, Lrack.

#### Dependencies

To create this port, select `Variable
geometry` for the **Turbine type**
parameter.

### **WgAreaPct** — Wastegate area percent `scalar`

Wastegate valve area percent, Awgpctcmd.

#### Dependencies

To create this port, select **Include
wastegate**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `TurbOutletTemp` | | | Temperature exiting the turbine | K |
| `DriveshftPwr` | | | Drive shaft power | W |
| `DriveshftTrq` | | | Drive shaft torque | N·m |
| `TurbMassFlw` | | | Turbine mass flow rate | kg/s |
| `PrsRatio` | | | Pressure ratio | N/A |
| `DriveshftCorrSpd` | | | Corrected drive shaft speed | rad/s |
| `TurbEff` | | | Turbine isentropic efficiency | N/A |
| `CorrMassFlw` | | | Corrected mass flow rate | kg/s |
| `WgArea` | | | Wastegate valve area | m^2 |
| `WgMassFlw` | | | Mass flow rate through the wastegate valve | kg/s |
| `WgOutletTemp` | | | Temperature exiting the wastegate valve | K |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | Power transmitted from the shaft | W |
| `PwrHeatFlwIn` | Heat flow rate at port A | W |
| `PwrHeatFlwOut` | Heat flow rate at port B | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Power loss | W |
| `PwrStored` | | *Not used* | |

### **Ds** — Drive shaft torque two-way connector port

`Trq` — Signal containing the drive
shaft torque, τturb, in N·m.

### **A** — Inlet mass flow rate, heat flow rate, temperature, mass fractions two-way connector port

Bus containing:

- `MassFlwRate` — Total mass
  flow rate through wastegate valve and turbine, –m˙total, in kg/s
- `HeatFlwRate` — Total inlet heat flow rate, –qinlet, in J/s
- `Temp` — Total inlet temperature, Tinlet, in K
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

### **B** — Outlet mass flow rate, heat flow rate, temperature, mass fractions two-way connector port

Bus containing:

- `MassFlwRate` — Turbine mass
  flow rate through wastegate valve and turbine, m˙turb, in kg/s
- `HeatFlwRate` — Total outlet heat flow rate, qoutlet, in J/s
- `Temp` — Total outlet temperature, Toutflw, in K
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
## Parameters
```yaml
parameters:
- name: Turbine type
  summary: Select turbine type Fixed geometry (default) | Variable geometry
  group: ''
- name: Include wastegate
  summary: Select on (default) | off
  group: ''
- name: Calibrate Performance Maps
  summary: Calibrate tables with measured data selection
  group: ''
- name: Corrected mass flow rate table, mdot_corrfx_tbl
  summary: Lookup table array
  group: ''
- name: Efficiency table, eta_turbfx_tb
  summary: Lookup table array
  group: ''
- name: Corrected speed breakpoints, w_corrfx_bpts1
  summary: Fixed geometry [0 1552 3104 4657 6209 7761 9313 1.087e+04 1.242e+04 1.397e+04] (default) | vector
  group: ''
- name: Pressure ratio breakpoints, Pr_fx_bpts2
  summary: Fixed geometry [1 1.333 1.667 2 2.333 2.667 3 3.333 3.667 4] (default) | vector
  group: ''
- name: Corrected mass flow rate table, mdot_corrvr_tbl
  summary: Lookup table array
  group: ''
- name: Efficiency table, eta_turbvr_tbl
  summary: Lookup table array
  group: ''
- name: Corrected speed breakpoints, w_corrvr_bpts2
  summary: Variable geometry [0 1752 3504 5257 7009 8761 1.051e+04 1.227e+04 1.402e+04 1.577e+04] (default) | vector
  group: ''
- name: Pressure ratio breakpoints, Pr_vr_bpts2
  summary: Variable geometry [1 1.306 1.611 1.917 2.222 2.528 2.833 3.139 3.444 3.75] (default) | vector
  group: ''
- name: Rack breakpoints, L_rack_bpts3
  summary: Variable geometry [0 0.2 0.3 0.5 0.7 1] (default) | vector
  group: ''
- name: Reference temperature, T_ref
  summary: Temperature 293.15 (default) | scalar
  group: ''
- name: Reference pressure, P_ref
  summary: Pressure 101325 (default) | scalar
  group: ''
- name: Wastegate flow area, A_wgopen
  summary: Area 0.0003 (default) | scalar
  group: ''
- name: Pressure ratio linearize limit, Plim_wg
  summary: Area, m^2 0.95 (default) | scalar
  group: ''
- name: Ideal gas constant, R
  summary: Constant 287 (default) | scalar
  group: ''
- name: Specific heat at constant pressure, cp
  summary: Specific heat 1005 (default) | scalar
  group: ''
```

#### Block Options

### **Turbine type** — Select turbine type `Fixed geometry` (default) | `Variable geometry`

Turbine type.

#### Dependencies

The table summarizes the parameter and port dependencies.

| Value | Enables Parameters | Creates Ports |
| --- | --- | --- |
| `Fixed geometry` | **Corrected mass flow rate table, mdot\_corrfx\_tbl**  **Efficiency table, eta\_turbfx\_tbl**  **Corrected speed breakpoints, w\_corrfx\_bpts1**  **Pressure ratio breakpoints, Pr\_fx\_bpts2** | None |
| `Variable geometry` | **Corrected mass flow rate table, mdot\_corrvr\_tbl**  **Efficiency table, eta\_turbvr\_tbl**  **Corrected speed breakpoints, w\_corrvr\_bpts2**  **Pressure ratio breakpoints, Pr\_vr\_bpts2**  **Rack breakpoints, L\_rack\_bpts3** | `RP` |

### **Include wastegate** — Select on (default) | off

#### Dependencies

Selecting the **Include wastegate** parameter enables:

- **Wastegate flow area, A\_wgopen**
- **Pressure ratio linearize limit,
  Plim\_wg**

#### Performance Tables

### **Calibrate Performance Maps** — Calibrate tables with measured data `selection`

If you have Model-Based Calibration Toolbox, click **Calibrate Performance Maps** to virtually calibrate the
corrected mass flow rate and turbine efficiency lookup tables using measured data. The dialog
box steps through these tasks.

| Task | Description |
| --- | --- |
| Import turbine data | Import this turbine data from a file. For more information, see Using Data (Model-Based Calibration Toolbox).  | **Turbine type** | Data | | --- | --- | | `Fixed geometry` | - Speed, Spd, in rad/s - Corrected mass flow rate, MassFlwRate, in   kg/s - Pressure ratio, PrsRatio,   dimensionless - Efficiency, Eff, dimensionless  The speed, corrected mass flow rate, pressure ratio, and efficiency are in the 2nd-5th columns of the data file, respectively. The first and second rows of the data file provide the variable names and units. For example, use this format.  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... | | | `Variable geometry` | - Speed, Spd, in rad/s - Corrected mass flow rate, MassFlwRate,   kg/s - Rack position, RackPos, dimensionless - Pressure ratio, PrsRatio,   dimensionless - Efficiency, Eff, dimensionless  Include data for several test points at each rack position operating point.  The speed, corrected mass flow rate, rack position, pressure ratio, and efficiency are in the 2nd-6th columns of the data file, respectively. The first and second rows of the data file provide the variable names and units. For example, use this format.  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | RackPos | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  |  | | Data: | `8373.3` | `0.02` | `1` | `1.21` | `0.44` | |  | ... | ... |  | ... | ... | |    Model-Based Calibration Toolbox limits the speed and pressure ratio breakpoint values to the maximum values in the file.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | Model-Based Calibration Toolbox fits the imported data and generates response models.  | **Turbine type** | Description | | --- | --- | | `Fixed geometry` | | Data | Response Model | | --- | --- | | Corrected mass flow rate | Square root turbine flow model described in *Modeling and Control of Engines and Drivelines*2 | | Efficiency | Blade speed ratio (BSR) model described in *Modeling and Control of Engines and Drivelines*2 | | | `Variable geometry` | Model-Based Calibration Toolbox uses a point-by-point test plan to fit the data. For each rack position, the block uses these response models to fit the corrected mass flow rate and efficiency data.  | Data | Response Model | | --- | --- | | Corrected mass flow rate | Square root turbine flow model described in *Modeling and Control of Engines and Drivelines*2 | | Efficiency | Blade speed ratio (BSR) model described in *Modeling and Control of Engines and Drivelines*2 | |  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response model and generates calibrated tables.  | **Turbine type** | Description | | --- | --- | | `Fixed geometry` | Model-Based Calibration Toolbox uses the response models for the corrected mass flow rate and efficiency tables. | | `Variable geometry` | Model-Based Calibration Toolbox fills the corrected mass flow rate and efficiency tables for each rack position. Model-Based Calibration Toolbox then combines the rack position-dependent tables into 3D lookup tables for corrected mass flow rate and efficiency. |  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these corrected mass flow rate and efficiency parameters with the calibration.  | **Turbine type** | Parameters | | --- | --- | | `Fixed geometry` | - **Corrected mass flow rate table,   mdot\_corrfx\_tbl** - **Efficiency table,   eta\_turbfx\_tbl** - **Corrected speed breakpoints,   w\_corrfx\_bpts1** - **Pressure ratio breakpoints,   Pr\_fx\_bpts2** | | `Variable geometry` | - **Corrected mass flow rate table,   mdot\_corrvr\_tbl** - **Efficiency table,   eta\_turbvr\_tbl** - **Corrected speed breakpoints,   w\_corrvr\_bpts2** - **Pressure ratio breakpoints,   Pr\_vr\_bpts2** - **Rack breakpoints,   L\_rack\_bpts3** | |

### **Corrected mass flow rate table, mdot\_corrfx\_tbl** — Lookup table `array`

Corrected mass flow rate lookup table for fixed geometry, m˙corrfx,tbl, as a function of corrected driveshaft speed,
*ωcorr*, and pressure ratio,
*pr*, in kg/s.

Mass flow rate versus corrected driveshaft speed and pressure ratio.

#### Dependencies

To enable this parameter, select `Fixed
geometry` for the **Turbine type**
parameter.

### **Efficiency table, eta\_turbfx\_tb** — Lookup table `array`

Efficiency lookup table for fixed geometry, ηturbfx,tbl, as a function of corrected driveshaft speed,
*ωcorr*, and pressure ratio,
*pr*, dimensionless.

Efficiency as a function of corrected driveshaft speed and pressure ratio.

#### Dependencies

To enable this parameter, select `Fixed
geometry` for the **Turbine type**
parameter.

### **Corrected speed breakpoints, w\_corrfx\_bpts1** — Fixed geometry `[0 1552 3104 4657 6209 7761 9313 1.087e+04 1.242e+04 1.397e+04]` (default) | `vector`

Corrected drive shaft speed breakpoints for fixed geometry, ωcorrfx,bpts1, in rad/s.

#### Dependencies

To enable this parameter, select `Fixed
geometry` for the **Turbine type**
parameter.

### **Pressure ratio breakpoints, Pr\_fx\_bpts2** — Fixed geometry `[1 1.333 1.667 2 2.333 2.667 3 3.333 3.667 4]` (default) | `vector`

Pressure ratio breakpoints for fixed geometry, prfx,bpts2.

#### Dependencies

To enable this parameter, select `Fixed
geometry` for the **Turbine type**
parameter.

### **Corrected mass flow rate table, mdot\_corrvr\_tbl** — Lookup table `array`

Corrected mass flow rate lookup table for variable geometry, m˙corrvr,tbl, as a function of corrected driveshaft speed,
*ωcorr*, and pressure ratio,
*pr*, in kg/s.

Mass flow rate as a function of corrected driveshaft speed and pressure ratio.

#### Dependencies

To enable this parameter, select `Variable
geometry` for the **Turbine type**
parameter.

### **Efficiency table, eta\_turbvr\_tbl** — Lookup table `array`

Efficiency lookup table for variable geometry, ηturbvr,tbl, as a function of corrected driveshaft speed,
*ωcorr*, and pressure ratio,
*pr*, dimensionless.

Efficiency as a function of corrected driveshaft speed and pressure ratio.

#### Dependencies

To enable this parameter, select `Variable
geometry` for the **Turbine type**
parameter.

### **Corrected speed breakpoints, w\_corrvr\_bpts2** — Variable geometry `[0 1752 3504 5257 7009 8761 1.051e+04 1.227e+04 1.402e+04 1.577e+04]` (default) | `vector`

Corrected drive shaft speed breakpoints for variable geometry, ωcorrvr,bpts1, in rad/s.

#### Dependencies

To enable this parameter, select `Variable
geometry` for the **Turbine type**
parameter.

### **Pressure ratio breakpoints, Pr\_vr\_bpts2** — Variable geometry `[1 1.306 1.611 1.917 2.222 2.528 2.833 3.139 3.444 3.75]` (default) | `vector`

Pressure ratio breakpoints for variable geometry.

#### Dependencies

To enable this parameter, select `Variable
geometry` for the **Turbine type**
parameter.

### **Rack breakpoints, L\_rack\_bpts3** — Variable geometry `[0 0.2 0.3 0.5 0.7 1]` (default) | `vector`

Rack position breakpoints for variable geometry, Lrack,bpts3.

#### Dependencies

To enable this parameter, select `Variable
geometry` for the **Turbine type**
parameter.

### **Reference temperature, T\_ref** — Temperature `293.15` (default) | `scalar`

Performance map reference temperature, Tref, in K.

### **Reference pressure, P\_ref** — Pressure `101325` (default) | `scalar`

Performance map reference pressure, Pref, in Pa.

#### Wastegate

### **Wastegate flow area, A\_wgopen** — Area `0.0003` (default) | `scalar`

Area of fully opened wastegate valve, Awgopen, in m^2.

#### Dependencies

To enable **Wastegate flow area, A\_wgopen**, select
the **Include wastegate** parameter.

### **Pressure ratio linearize limit, Plim\_wg** — Area, m^2 `0.95` (default) | `scalar`

#### Dependencies

Flow restriction linearization limit, plim,wg.

To enable **Pressure ratio linearize limit,
Plim\_wg**, select the **Include wastegate**
parameter.

#### Properties

### **Ideal gas constant, R** — Constant `287` (default) | `scalar`

Ideal gas constant R, in J/(kg·K).

### **Specific heat at constant pressure, cp** — Specific heat `1005` (default) | `scalar`

Specific heat at constant pressure, cp, in J/(kg·K).
## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Turbine for boosted engines

The Turbine block uses the conservation of mass
and energy to calculate mass and heat flow rates for turbines with
either fixed or variable geometry. You can configure the block with
a wastegate valve to bypass the turbine. The block uses two-way ports
to connect to the inlet and outlet control volumes and the drive shaft.
You can specify the lookup tables to calculate the mass flow rate
and turbine efficiency. Typically, turbine manufacturers provide the
mass flow rate and efficiency tables as a function of corrected speed
and pressure ratio. The block does not support reverse mass flow.

If you have Model-Based Calibration Toolbox™, click **Calibrate Performance Maps** to virtually
calibrate the mass flow rate and turbine efficiency lookup tables using measured
data.

The mass flows from the inlet control volume to outlet control
volume.

Schematic showing wastegate and turbine.

The Turbine block implements equations to model
the performance, wastegate flow, and combined flow.

### Virtual Calibration

If you have Model-Based Calibration Toolbox, click **Calibrate Performance Maps** to virtually calibrate the
corrected mass flow rate and turbine efficiency lookup tables using measured data. The dialog
box steps through these tasks.

| Task | Description |
| --- | --- |
| Import turbine data | Import this turbine data from a file. For more information, see Using Data (Model-Based Calibration Toolbox).  | **Turbine type** | Data | | --- | --- | | `Fixed geometry` | - Speed, Spd, in rad/s - Corrected mass flow rate, MassFlwRate, in   kg/s - Pressure ratio, PrsRatio,   dimensionless - Efficiency, Eff, dimensionless  The speed, corrected mass flow rate, pressure ratio, and efficiency are in the 2nd-5th columns of the data file, respectively. The first and second rows of the data file provide the variable names and units. For example, use this format.  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... | | | `Variable geometry` | - Speed, Spd, in rad/s - Corrected mass flow rate, MassFlwRate,   kg/s - Rack position, RackPos, dimensionless - Pressure ratio, PrsRatio,   dimensionless - Efficiency, Eff, dimensionless  Include data for several test points at each rack position operating point.  The speed, corrected mass flow rate, rack position, pressure ratio, and efficiency are in the 2nd-6th columns of the data file, respectively. The first and second rows of the data file provide the variable names and units. For example, use this format.  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | RackPos | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  |  | | Data: | `8373.3` | `0.02` | `1` | `1.21` | `0.44` | |  | ... | ... |  | ... | ... | |    Model-Based Calibration Toolbox limits the speed and pressure ratio breakpoint values to the maximum values in the file.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | Model-Based Calibration Toolbox fits the imported data and generates response models.  | **Turbine type** | Description | | --- | --- | | `Fixed geometry` | | Data | Response Model | | --- | --- | | Corrected mass flow rate | Square root turbine flow model described in *Modeling and Control of Engines and Drivelines*2 | | Efficiency | Blade speed ratio (BSR) model described in *Modeling and Control of Engines and Drivelines*2 | | | `Variable geometry` | Model-Based Calibration Toolbox uses a point-by-point test plan to fit the data. For each rack position, the block uses these response models to fit the corrected mass flow rate and efficiency data.  | Data | Response Model | | --- | --- | | Corrected mass flow rate | Square root turbine flow model described in *Modeling and Control of Engines and Drivelines*2 | | Efficiency | Blade speed ratio (BSR) model described in *Modeling and Control of Engines and Drivelines*2 | |  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response model and generates calibrated tables.  | **Turbine type** | Description | | --- | --- | | `Fixed geometry` | Model-Based Calibration Toolbox uses the response models for the corrected mass flow rate and efficiency tables. | | `Variable geometry` | Model-Based Calibration Toolbox fills the corrected mass flow rate and efficiency tables for each rack position. Model-Based Calibration Toolbox then combines the rack position-dependent tables into 3D lookup tables for corrected mass flow rate and efficiency. |  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these corrected mass flow rate and efficiency parameters with the calibration.  | **Turbine type** | Parameters | | --- | --- | | `Fixed geometry` | - **Corrected mass flow rate table,   mdot\_corrfx\_tbl** - **Efficiency table,   eta\_turbfx\_tbl** - **Corrected speed breakpoints,   w\_corrfx\_bpts1** - **Pressure ratio breakpoints,   Pr\_fx\_bpts2** | | `Variable geometry` | - **Corrected mass flow rate table,   mdot\_corrvr\_tbl** - **Efficiency table,   eta\_turbvr\_tbl** - **Corrected speed breakpoints,   w\_corrvr\_bpts2** - **Pressure ratio breakpoints,   Pr\_vr\_bpts2** - **Rack breakpoints,   L\_rack\_bpts3** | |

### Thermodynamics

The block uses these equations to model the thermodynamics.

| Calculation | Equations |
| --- | --- |
| Forward mass flow | m˙turb>0  p01=pinlet  p02=poutlet  T01=Tinlet  h01=hinlet |
| First law of thermodynamics | W˙turb=m˙turbcp(T01−T02) |
| Isentropic efficiency | ηturb=h01−h02h01−h02s=T01−T02T01−T02s |
| Isentropic outlet temperature, assuming ideal gas, and constant specific heats | T02s=T01(p02p01)γ−1γ |
| Specific heat ratio | γ=cpcp−R |
| Outlet temperature | T02=T01+ηturbT01{1−(p02p01)γ−1γ} |
| Heat flows | qin,turb=m˙turbcpT01  qout,turb=m˙turbcpT02 |
| Drive shaft torque | τturb=W˙turbω |

The equations use these variables.

|  |  |
| --- | --- |
| pinlet,p01 | Inlet control volume total pressure |
| Tinlet, T01 | Inlet control volume total temperature |
| hinlet, h01 | Inlet control volume total specific enthalpy |
| poutlet, p02 | Outlet control volume total pressure |
| Toutlet | Outlet control volume total temperature |
| houtlet | Outlet control volume total specific enthalpy |
| W˙turb | Drive shaft power |
| T02 | Temperature exiting the turbine |
| h02 | Outlet total specific enthalpy |
| m˙turb | Turbine mass flow rate |
| qin,turb | Turbine inlet heat flow rate |
| qout,turb | Turbine outlet heat flow rate |
| ηturb | Turbine isentropic efficiency |
| T02s | Isentropic outlet total temperature |
| h02s | Isentropic outlet total specific enthalpy |
| R | Ideal gas constant |
| cp | Specific heat at constant pressure |
| γ | Specific heat ratio |
| τturb | Drive shaft torque |

### Performance Lookup Tables

The block implements lookup tables based on these equations.

| Calculation | Equation | |
| --- | --- | --- |
| Corrected mass flow rate | m˙corr=m˙turbT01/Trefp01/pref | |
| Corrected speed | ωcorr=ωT01/Tref | |
| Pressure expansion ratio | pr=p01p02 | |
| Efficiency lookup table | Fixed geometry (3-D table) | ηturbfx,tbl=f(ωcorr,pr) |
| Variable geometry (3-D table) | ηturbvr,tbl=f(ωcorr,pr,Lrack) |
| Corrected mass flow lookup table | Fixed geometry (3-D table) | m˙corrfx,tbl=f(ωcorr,pr) |
| Variable geometry (3-D table) | m˙corrvr,tbl=f(ωcorr,pr,Lrack) |

The equations use these variables.

|  |  |
| --- | --- |
| p01 | Inlet control volume total pressure |
| pr | Pressure expansion ratio |
| p02 | Outlet control volume total pressure |
| Pref | Lookup table reference pressure |
| T01 | Inlet control volume total temperature |
| Tref | Lookup table reference temperature |
| m˙turb | Turbine mass flow rate |
| ω | Drive shaft speed |
| ωcorr | Corrected drive shaft speed |
| Lrack | Variable geometry turbine rack position |
| ηturbfx,tbl | Efficiency 3-D lookup table for fixed geometry |
| m˙corrfx,tbl | Corrected mass flow rate 3-D lookup table for fixed geometry |
| ηturbvr,tbl | Efficiency 3-D lookup table for variable geometry |
| m˙corrvr,tbl | Corrected mass flow rate 3-D lookup table for variable geometry |

### Wastegate

To calculate the wastegate heat and mass flow rates, the Turbine block
uses a Flow Restriction block. The Flow Restriction block
uses the wastegate flow area.

Awg=AwgpctcmdAwgopen100

The equation uses these variables.

|  |  |
| --- | --- |
| Awgpctcmd | Wastegate valve area percent command |
| Awg | Wastegate valve area |
| Awgopen | Wastegate valve area when fully open |

### Combined Flow

To represent flow through the wastegate valve and turbine, the
block uses these equations.

| Calculation | Equations | |
| --- | --- | --- |
| Blocks not configured with a wastegate valve | m˙wg=qwg=0 | |
| Total mass flow rate | m˙total=m˙turb+m˙wg | |
| Total heat flow rate | qinlet=qin,turb+qwg  qoutlet=qout,turb+qwg | |
| Combined temperature exiting the wastegate valve and turbine | Toutflw={qoutletm˙totalcpm˙total>m˙threshT02+Toutflw,wg2else | |

The block uses the internal signal `FlwDir` to track the direction of the flow.

The equations use these variables.

|  |  |
| --- | --- |
| m˙total | Total mass flow rate through the wastegate valve and turbine |
| m˙turb | Turbine mass flow rate |
| m˙wg | Mass flow rate through the wastegate valve |
| qinlet | Total inlet heat flow rate |
| qoutlet | Total outlet heat flow rate |
| qin,turb | Turbine inlet heat flow rate |
| qout,turb | Turbine outlet heat flow rate |
| qwg | Wastegate valve heat flow rate |
| T02 | Temperature exiting the turbine |
| Toutflw | Total temperature exiting the block |
| Toutflw,wg | Temperature exiting the wastegate valve |
| m˙thresh | Mass flow rate threshold to prevent dividing by zero |
| cp | Specific heat at constant pressure |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrDriveshft` | Power transmitted from the shaft | −W˙turb |
| `PwrHeatFlwIn` | Heat flow rate at port A | qoutlet |
| `PwrHeatFlwOut` | Heat flow rate at port B | qoutlet |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLoss` | Power loss | −qinlet−qoutlet+W˙turb |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | *Not used* | | |

The equations use these variables.

|  |  |
| --- | --- |
| W˙turb | Drive shaft power |
| qoutlet | Total outlet heat flow rate |
| qinlet | Total inlet heat flow rate |
