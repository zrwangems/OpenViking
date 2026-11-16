---
type: simulink-block
title: 'Compressor'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Boost'
documentation_page: 'compressor'
documentation_source_path: 'ref/compressor.html'
language: en
---

# Compressor

## Ports

### Input

### **Ds** — Drive shaft speed two-way connector port

`ShftSpd` — Signal containing the drive
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
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `CmprsOutletTemp` | | | Temperature exiting the compressor | K |
| `DriveshftPwr` | | | Drive shaft power | W |
| `DriveshftTrq` | | | Drive shaft torque | N·m |
| `CmprsMassFlw` | | | Mass flow rate through compressor | kg/s |
| `PrsRatio` | | | Pressure ratio | N/A |
| `DriveshftCorrSpd` | | | Corrected drive shaft speed | rad/s |
| `CmprsEff` | | | Compressor isentropic efficiency | N/A |
| `CorrMassFlw` | | | Corrected mass flow rate | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | Power transmitted from the shaft | W |
| `PwrHeatFlwIn` | Heat flow rate at port A | W |
| `PwrHeatFlwOut` | Heat flow rate at port B | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Power loss | W |
| `PwrStored` | | *Not used* | W |

### **Ds** — Drive shaft torque two-way connector port

`Trq` — Signal containing the drive
shaft torque, τcomp, in N·m.

### **A** — Inlet mass flow rate, heat flow rate, temperature, mass fractions two-way connector port

Bus containing:

- `MassFlwRate` — Mass flow
  rate through inlet,m˙comp, in kg/s
- `HeatFlwRate` — Inlet heat
  flow rate, qinlet, in J/s
- `Temp` — Inlet temperature,
  in K
- `MassFrac` —
  Inlet mass fractions, dimensionless.

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

- `MassFlwRate` — Outlet mass
  flow rate, m˙comp, in kg/s
- `HeatFlwRate` — Outlet heat
  flow rate, qoutlet, in J/s
- `Temp` — Outlet temperature,
  in K
- `MassFrac` —
  Outlet mass fractions, dimensionless.

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

#### Performance Tables

### **Calibrate Performance Maps** — Calibrate tables with measured data `selection`

If you have Model-Based Calibration Toolbox, click **Calibrate Performance Maps** to virtually calibrate the
mass flow rate and turbine efficiency lookup tables using measured data. The dialog box steps
through these tasks.

| Task | Description |
| --- | --- |
| Import compressor data | Import this compressor data from a file. For more information, see Using Data (Model-Based Calibration Toolbox).  - Speed, Spd, in rad/s - Mass flow rate, MassFlwRate, in kg/s - Pressure ratio, PrsRatio, dimensionless - Efficiency, Eff, dimensionless    The speed, mass flow rate, pressure ratio, and efficiency are in the 2nd-5th columns of the data file, respectively. The first and second rows of the data file provide the variable names and units. For example, use this format.  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... |    Model-Based Calibration Toolbox limits the speed and pressure ratio breakpoint values to the maximum values in the file.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | Model-Based Calibration Toolbox fits the imported data to the response models.  | Data | Response Model | | --- | --- | | Mass flow rate | Extended ellipse response model described in *Modeling and Control of Engines and Drivelines*2 | | Efficiency | Polynomial |    To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response model and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these mass flow rate and efficiency parameters with the calibration.  - **Corrected mass flow rate table,   mdot\_corr\_tbl** - **Efficiency table, eta\_comp\_tbl** - **Corrected speed breakpoints,   w\_corr\_bpts1** - **Pressure ratio breakpoints,   Pr\_bpts2** |

### **Corrected mass flow rate table, mdot\_corr\_tbl** — Lookup table `array`

Corrected mass flow rate lookup table, m˙corr,tbl, as a function of corrected driveshaft speed,
*ωcorr*, and pressure ratio,
*pr*, in kg/s.

Corrected mass flow rate as a function of driveshaft speed and pressure ratio.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mdot_corr_tbl` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Efficiency table, eta\_comp\_tbl** — Lookup table `array`

Efficiency lookup table, ηcomb,tbl, as a function of corrected driveshaft speed,
*ωcorr*, and pressure ratio,
*pr*, dimensionless.

Efficiency as a function of driveshaft speed and pressure ratio.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_comp_tbl` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Corrected speed breakpoints, w\_corr\_bpts1** — Breakpoints `vector`

Corrected drive shaft speed breakpoints, ωcorr,bpts1, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_corr_bpts1` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Pressure ratio breakpoints, Pr\_bpts2** — Breakpoints `vector`

Pressure ratio breakpoints, pr,bpts2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Pr_bpts2` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Reference temperature, T\_ref** — Reference `293.15` (default) | `scalar`

Lookup table reference temperature, Tref, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_ref` |
| **Values:** | `293.15` (default) | `scalar` |
| **Data Types:** | `double` |

### **Reference pressure, P\_ref** — Reference `101325` (default) | `scalar`

Lookup table reference pressure, Pref, in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `P_ref` |
| **Values:** | `101325` (default) | `scalar` |
| **Data Types:** | `double` |

#### Gas Properties

### **Ideal gas constant, R** — Constant `287` (default) | `scalar`

Ideal gas constant, R, in J/(kg\*K).

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

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Compressor for boosted engines

The Compressor block simulates engine boost by
using the drive shaft energy to increase the intake manifold pressure.
The block is a component of supercharger and turbocharger models.
The block uses two-way ports to connect to the inlet and outlet control
volumes and the drive shaft. The control volumes provide the pressure,
temperature, and specific enthalpy for the compressor to calculate
the mass and energy flow rates. To calculate the torque and flow rates,
the drive shaft provides the speed to the compressor. Typically, compressor
manufacturers provide the mass flow rate and efficiency tables as
a function of corrected speed and pressure ratio. You can specify
the lookup tables to calculate the mass flow rate and efficiency.
The block does not support reverse mass flow.

If you have Model-Based Calibration Toolbox™, click **Calibrate Performance Maps** to virtually
calibrate the mass flow rate and turbine efficiency lookup tables using measured
data.

The mass flows from the inlet control volume to the outlet
control volume.

Schematic showing mass flows from the inlet control volume to the outlet control volume.

### Virtual Calibration

If you have Model-Based Calibration Toolbox, click **Calibrate Performance Maps** to virtually calibrate the
mass flow rate and turbine efficiency lookup tables using measured data. The dialog box steps
through these tasks.

| Task | Description |
| --- | --- |
| Import compressor data | Import this compressor data from a file. For more information, see Using Data (Model-Based Calibration Toolbox).  - Speed, Spd, in rad/s - Mass flow rate, MassFlwRate, in kg/s - Pressure ratio, PrsRatio, dimensionless - Efficiency, Eff, dimensionless    The speed, mass flow rate, pressure ratio, and efficiency are in the 2nd-5th columns of the data file, respectively. The first and second rows of the data file provide the variable names and units. For example, use this format.  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... |    Model-Based Calibration Toolbox limits the speed and pressure ratio breakpoint values to the maximum values in the file.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | Model-Based Calibration Toolbox fits the imported data to the response models.  | Data | Response Model | | --- | --- | | Mass flow rate | Extended ellipse response model described in *Modeling and Control of Engines and Drivelines*2 | | Efficiency | Polynomial |    To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response model and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these mass flow rate and efficiency parameters with the calibration.  - **Corrected mass flow rate table,   mdot\_corr\_tbl** - **Efficiency table, eta\_comp\_tbl** - **Corrected speed breakpoints,   w\_corr\_bpts1** - **Pressure ratio breakpoints,   Pr\_bpts2** |

### Thermodynamics

The block uses these equations to model the thermodynamics.

| Calculation | Equations |
| --- | --- |
| Forward mass flow | m˙comp>0  p01=pinlet  p02=poutlet  T01=Tinlet  h01=hinlet |
| First law of thermodynamics | W˙comp=m˙compcp(T01−T02) |
| Isentropic efficiency | ηcomp=h02s−h01h02−h01=T02s−T01T02−T01 |
| Isentropic outlet temperature, assuming ideal gas and constant specific heats | T02s=T01(p02p01)γ−1γ |
| Specific heat ratio | γ=cpcp−R |
| Outlet temperature | T02=T01+T01ηcomb{(p02p01)γ−1γ−1} |
| Heat flows | qinlet=m˙comph01  qoutlet=m˙comph02=m˙compcpT02 |
| Corrected mass flow rate | m˙corr=m˙compT01/Trefp01/pref |
| Corrected speed | ωcorr=ωT01/Tref |
| Pressure ratio | pr=p01p02 |

The block uses the internal signal `FlwDir` to track the direction of the flow.

The equations use these variables.

|  |  |
| --- | --- |
| pinlet, p01 | Inlet control volume total pressure |
| Tinlet, T01 | Inlet control volume total temperature |
| hinlet, h01 | Inlet control volume total specific enthalpy |
| poutlet, p02 | Outlet control volume total pressure |
| Toutlet | Outlet control volume total temperature |
| houtlet | Outlet control volume total specific enthalpy |
| W˙comp | Drive shaft power |
| T02 | Outlet total temperature |
| h02 | Outlet total specific enthalpy |
| m˙comp | Mass flow rate through compressor |
| qinlet | Inlet heat flow rate |
| qoutlet | Outlet heat flow rate |
| ηcomp | Compressor isentropic efficiency |
| T02s | Isentropic outlet total temperature |
| h02s | Isentropic outlet total specific enthalpy |
| R | Ideal gas constant |
| cp | Specific heat at constant pressure |
| γ | Specific heat ratio |
| m˙corr | Corrected mass flow rate |
| ω | Drive shaft speed |
| ωcorr | Corrected drive shaft speed |
| Tref | Lookup table reference temperature |
| Pref | Lookup table reference pressure |
| τcomp | Compressor drive shaft torque |
| pr | Pressure ratio |
| ηcomb,tbl | Compressor efficiency 3-D lookup table |
| m˙corr,tbl | Corrected mass flow rate 3-D lookup table |
| ωcorr,bpts1 | Corrected speed breakpoints |
| pr,bpts2 | Pressure ratio breakpoints |

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
