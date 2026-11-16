---
type: simulink-block
title: 'Mapped SI Engine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Propulsion'
documentation_page: 'mappedsiengine'
documentation_source_path: 'ref/mappedsiengine.html'
language: en
---

# Mapped SI Engine

## Ports

### Input

### **TrqCmd** — Commanded torque `scalar`

Torque, *Tcmd*, in N·m.

### **EngSpd** — Engine speed `scalar`

Engine speed, *N*, in rpm.

### **EngTemp** — Engine temperature `scalar`

Engine temperature, *TempEng*, in K.

#### Dependencies

To enable this port, select **Input engine temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `IntkGassMassFlw` | | | Engine air mass flow output | kg/s |
| `NrmlzdAirChrg` | | | Normalized engine cylinder air mass | N/A |
| `Afr` | | | Air-fuel ratio (AFR) | N/A |
| `FuelMassFlw` | | | Engine fuel flow output | kg/s |
| `FuelVolFlw` | | | Volumetric fuel flow | m3/s |
| `ExhManGasTemp` | | | Engine exhaust gas temperature | K |
| `EngTrq` | | | Engine torque output | N·m |
| `EngSpd` | | | Engine speed | rpm |
| `CrkAng` | | | Engine crankshaft absolute angle  ∫0(360)CpsEngSpd18030dθ  where Cps is crankshaft revolutions per power stroke. | degrees crank angle |
| `Bsfc` | | | Engine brake-specific fuel consumption (BSFC) | g/kWh |
| `EoHC` | | | Engine out hydrocarbon emission mass flow | kg/s |
| `EoCO` | | | Engine out carbon monoxide emission mass flow rate | kg/s |
| `EoNOx` | | | Engine out nitric oxide and nitrogen dioxide emissions mass flow | kg/s |
| `EoCO2` | | | Engine out carbon dioxide emission mass flow | kg/s |
| `EoPM` | | | Engine out particulate matter emission mass flow | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCrkshft` | Crankshaft power | W |
| `PwrNotTrnsfrd` | `PwrFuel` | Fuel input power | W |
| `PwrLoss` | Power loss | W |
| `PwrStored` | | *Not used* | |

### **EngTrq** — Engine brake torque `scalar`

Engine brake torque, Tbrake, in N·m.

## Parameters

#### Block Options

### **Include turbocharger lag effect** — Increase time constant `off` (default) | `on`

To model turbocharger lag, select **Include
turbocharger lag effect**. During throttle control, the time constant
models the manifold filling and emptying dynamics. When the torque request requires a
turbocharger boost, the block uses a larger time constant to represent the turbocharger lag.
The block uses these equations.

|  |  |
| --- | --- |
| Dynamic torque | dTbrakedt=1τeng(Tstdy−Tbrake) |
| Boost time constant | τbst={τbst,rising       when Tstdy>Tbrakeτbst,falling      when Tstdy≤Tbrake |
| Final time constant | τeng={τthr       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) |

The equations use these variables.

|  |  |
| --- | --- |
| *Tbrake* | Brake torque |
| *Tstdy* | Steady-state target torque |
| *τbst* | Boost time constant |
| *τbst,rising*, *τbst,falling* | Boost rising and falling time constant, respectively |
| *τeng* | Final time constant |
| *τthr* | Time constant during throttle control |
| *ƒbst(N)* | Boost torque speed line |
| *N* | Engine speed |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TurboLagCheckbox` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting **Include turbocharger lag effect** enables
these parameters:

- **Boost torque line,
  f\_tbrake\_bst**
- **Time constant below boost line,
  tau\_thr**
- **Rising torque boost time constant,
  tau\_bst\_rising**
- **Falling torque boost time constant,
  tau\_bst\_falling**

### **Input engine temperature** — Create input port `off` (default) | `on`

Select this to create the `EngTemp` input port.

The block enables you to specify lookup tables for these engine
characteristics. The lookup tables, developed with the Model-Based Calibration Toolbox, are functions of commanded torque,
*Tcmd*, brake torque,
*Tbrake*, and engine speed,
*N*. If you select **Input engine temperature**, the tables
are also a function of engine temperature,
*TempEng*.

| Table | **Input Engine Temperature** Parameter Setting | |
| --- | --- | --- |
| `off` | `on` |
| Power | *ƒ(Tcmd,N)* | *ƒ(Tcmd,N,TempEng)* |
| Air | *ƒ(Tbrake,N)* | *ƒ(Tbrake,N,TempEng)* |
| Fuel |
| Temperature |
| Efficiency |
| HC |
| CO |
| NOx |
| CO2 |
| PM |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EngTmpInpEnbl` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Configuration

### **Calibrate Maps** — Calibrate tables with measured data `selection`

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 2D lookup
tables using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import firing data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).    | Required Data | Optional Data | | --- | --- | | - Engine speed, rpm - Engine torque, N·m | - Air mass flow rate, kg/s - Brake specific fuel consumption,   g/(kW·h) - CO2 mass flow rate, kg/s - CO mass flow rate, kg/s - Exhaust temperature, K - Fuel mass flow rate, kg/s - HC mass flow rate, kg/s - NOx mass flow rate, kg/s - Particulate matter mass flow rate,   kg/s |  Collect firing data at steady-state operating conditions when injectors deliver the fuel. Data should cover the engine speed and torque operating range. Model-Based Calibration Toolbox uses the firing data boundary as the maximum torque.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Import non-firing data | Import this non-firing data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`.    - Engine speed, rpm - Engine torque, N·m  Collect non-firing (motoring) data at steady-state operating conditions when fuel is cut off. All non-firing torque points must be less than zero. Non-firing data is a function of engine speed only. |
| Generate response models | For both firing and non-firing data, the Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the firing and non-firing response models and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update the block lookup table and breakpoint parameters with the calibration. |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Breakpoints for commanded torque, f\_tbrake\_t\_bpt** — Breakpoints `1`-by-`M` vector

Breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_f_bpt` |
| **Values:** | `1`-by-`M` vector |
| **Data Types:** | `double` |

### **Breakpoints for engine speed input, f\_tbrake\_n\_bpt** — Breakpoints `1`-by-`N` vector

Breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_t_bpt` |
| **Values:** | `1`-by-`M` vector |
| **Data Types:** | `double` |

### **Breakpoints for temperature input, f\_tbrake\_engtmp\_bpt** — Breakpoints `[233.15 273.15 373.15]` (default) | `1`-by-`L` vector

Breakpoints, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_engtmp_bpt` |
| **Values:** | `1`-by-`L` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

### **Number of cylinders, NCyl** — Number `4` (default) | `scalar`

Number of cylinders.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NCyl` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Crank revolutions per power stroke, Cps** — Crank revolutions `2` (default) | `scalar`

Crank revolutions per power stroke.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cps` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Total displaced volume, Vd** — Volume `0.0015` (default) | `scalar`

Volume displaced by engine, in m^3.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vd` |
| **Values:** | `0.0015` (default) | `scalar` |
| **Data Types:** | `double` |

### **Fuel lower heating value, Lhv** — Heating value `45e6` (default) | `scalar`

Fuel lower heating value, *LHV*, in J/kg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lhv` |
| **Values:** | `45e6` (default) | `scalar` |
| **Data Types:** | `double` |

### **Fuel specific gravity, Sg** — Specific gravity `0.745` (default) | `scalar`

Specific gravity of fuel,
*Sgfuel*, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Sg` |
| **Values:** | `0.832` (default) | `scalar` |
| **Data Types:** | `double` |

### **Ideal gas constant air, Rair** — Constant `287` (default) | `scalar`

Ideal gas constant of air and residual gas entering the engine intake
port, in J/(kg\*K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rair` |
| **Values:** | `287` (default) | `scalar` |
| **Data Types:** | `double` |

### **Air standard pressure, Pstd** — Pressure `101325` (default) | `scalar`

Standard air pressure, in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Pstd` |
| **Values:** | `101325` (default) | `scalar` |
| **Data Types:** | `double` |

### **Air standard temperature, Tstd** — Temperature `293.15` (default) | `scalar`

Standard air temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tstd` |
| **Values:** | `293.15` (default) | `scalar` |
| **Data Types:** | `double` |

### **Boost torque line, f\_tbrake\_bst** — Boost lag `1`-by-`M` vector

Boost torque line, *ƒbst(N)*, in
N·m.

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_bst` |
| **Values:** | `1`-by-`M` vector |
| **Data Types:** | `double` |

### **Time constant below boost line, tau\_thr** — Time constant below `0.2` (default) | `scalar`

Time constant below boost line,
*τthr*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau_thr` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

### **Rising torque boost time constant, tau\_bst\_rising** — Rising time constant `1.5` (default) | `scalar`

Rising torque boost time constant,
*τbst,rising*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau_bst_rising` |
| **Values:** | `1.0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

### **Falling torque boost time constant, tau\_bst\_falling** — Falling time constant `1` (default) | `scalar`

Falling torque boost time constant,
*τbst,falling*, in s.

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau_bst_falling` |
| **Values:** | `0.7` (default) | `scalar` |
| **Data Types:** | `double` |

#### Power

### **Brake torque map, f\_tbrake** — 2D lookup table `M`-by-`N` matrix

The engine torque lookup table is a function of commanded engine
torque and engine speed, *T* = ƒ(*Tcmd*, *N*),
where:

- *T* is engine torque, in N·m.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing actual torque as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

### **Plot brake torque map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Brake torque map, f\_tbrake\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine torque lookup table is a
function of commanded engine torque, engine speed, and engine temperature,
*T* = ƒ(*Tcmd*,
*N*,
*TempEng*), where:

- *T* is engine torque, in N·m.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### Air

### **Air mass flow map, f\_air** — 2D lookup table `M`-by-`N` matrix

The engine air mass flow lookup table is a function of
commanded engine torque and engine speed, m˙intk = ƒ(*Tcmd*, *N*), where:

- m˙intk is engine air mass flow, in kg/s.
- *Tcmd* is commanded engine torque, in
  N·m.
- *N* is engine speed, in rpm.

Plot showing air mass flow as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_air` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot air mass map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Air mass flow map, f\_air\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine air mass flow lookup table is
a function of commanded engine torque, engine speed, and engine temperature, m˙intk = ƒ(*Tcmd*,
*N*,
*TempEng*), where:

- m˙intk is engine air mass flow, in kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_air_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### Fuel

### **Fuel flow map, f\_fuel** — 2D lookup table `M`-by-`N` matrix

The engine fuel mass flow lookup table is a function of commanded
engine torque and engine speed, *MassFlow* = ƒ(*Tcmd*, *N*),
where:

- *MassFlow* is engine fuel mass flow,
  in kg/s.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing fuel mass flow as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_fuel` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot fuel flow map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Fuel flow map, f\_fuel\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine fuel mass flow lookup table is
a function of commanded engine torque, engine speed, and engine temperature,
*MassFlow* =
ƒ(*Tcmd*, *N*,
*TempEng*), where:

- *MassFlow* is engine fuel mass flow, in
  kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_fuel_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### Temperature

### **Exhaust temperature map, f\_texh** — 2D lookup table `M`-by-`N` matrix

The engine exhaust temperature lookup table is a function of
commanded engine torque and engine speed, *Texh* =
ƒ(*Tcmd*, *N*),
where:

- *Texh* is
  exhaust temperature, in K.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing exhaust temperature as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_texh` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot exhaust temperature map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Exhaust temperature map, f\_texh\_3d** — 3D lookup table `array`

The engine exhaust temperature lookup
table is a function of commanded engine torque, engine speed, and engine
temperature, *Texh* =
ƒ(*Tcmd*,
*N*,
*TempEng*), where:

- *Texh* is exhaust
  temperature, in K.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_texh_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### Efficiency

### **BSFC map, f\_eff** — 2D lookup table `M`-by-`N`-by-`L` array

The brake-specific fuel consumption (BSFC) efficiency is a function
of commanded engine torque and engine speed, *BSFC* =
ƒ(*Tcmd*, *N*),
where:

- *BSFC* is BSFC, in g/kWh.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing BSFC as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_eff` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot BSFC map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **BSFC map, f\_eff\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The brake-specific fuel consumption
(BSFC) efficiency is a function of commanded engine torque, engine speed,
and engine temperature, *BSFC* =
ƒ(*Tcmd*,
*N*,
*TempEng*), where:

- *BSFC* is BSFC, in g/kWh.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_eff_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### HC

### **EO HC map, f\_hc** — 2D lookup table `M`-by-`N` matrix

The engine-out hydrocarbon emissions are a function of commanded
engine torque and engine speed, *EO HC* = ƒ(*Tcmd*, *N*),
where:

- *EO HC* is engine-out hydrocarbon
  emissions, in kg/s.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing EO HC as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_hc` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot EO HC map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **EO HC map, f\_hc\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine-out hydrocarbon emissions are
a function of commanded engine torque, engine speed, and engine temperature,
*EO HC* =
ƒ(*Tcmd*, *N*,
*TempEng*), where:

- *EO HC* is engine-out hydrocarbon emissions,
  in kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_hc_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### CO

### **EO CO map, f\_co** — 2D lookup table `M`-by-`N` matrix

The engine-out carbon monoxide emissions are a function of commanded
engine torque and engine speed, *EO CO* = ƒ(*Tcmd*, *N*),
where:

- *EO CO* is engine-out carbon monoxide
  emissions, in kg/s.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing EO CO as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_co` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot EO CO map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **EO HC map, f\_hc\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine-out hydrocarbon emissions are
a function of commanded engine torque, engine speed, and engine temperature,
*EO HC* =
ƒ(*Tcmd*, *N*,
*TempEng*), where:

- *EO HC* is engine-out hydrocarbon emissions,
  in kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_co_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### NOx

### **EO NOx map, f\_nox** — 2D lookup table `M`-by-`N` matrix

The engine-out nitric oxide and nitrogen dioxide emissions are
a function of commanded engine torque and engine speed, *EO
NOx* = ƒ(*Tcmd*, *N*),
where:

- *EO NOx* is engine-out nitric oxide
  and nitrogen dioxide emissions, in kg/s.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing EO NOX as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nox` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot EO NOx map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **EO NOx map, f\_nox\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine-out nitric oxide and nitrogen
dioxide emissions are a function of commanded engine torque, engine speed,
and engine temperature, *EO NOx* =
ƒ(*Tcmd*,
*N*,
*TempEng*), where:

- *EO NOx* is engine-out nitric oxide and
  nitrogen dioxide emissions, in kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nox_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### CO2

### **EO CO2 map, f\_co2** — 2D lookup table `M`-by-`N` matrix

The engine-out carbon dioxide emissions are a function of commanded
engine torque and engine speed, *EO CO2* = ƒ(*Tcmd*, *N*),
where:

- *EO CO2* is engine-out carbon dioxide
  emissions, in kg/s.
- *Tcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

Plot showing EO CO2 as a function of engine speed and commanded torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_co2` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot CO2 map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **EO CO2 map, f\_co2\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine-out carbon dioxide emissions
are a function of commanded engine torque, engine speed, and engine
temperature, *EO CO2* =
ƒ(*Tcmd*,
*N*,
*TempEng*), where:

- *EO CO2* is engine-out carbon dioxide
  emissions, in kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_co2_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

#### PM

### **EO PM map, f\_pm** — 2D lookup table `M`-by-`N` matrix

The engine-out particulate matter emissions are a function of commanded
engine torque and engine speed, where:

- *EO PM* is engine-out PM emissions, in
  kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_pm` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot EO PM map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **EO PM map, f\_pm\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

The engine-out particulate matter emissions are a function of commanded
engine torque, engine speed, and engine temperature, where:

- *EO PM* is engine-out PM emissions, in
  kg/s.
- *Tcmd* is commanded
  engine torque, in N·m.
- *N* is engine speed, in rpm.
- *TempEng* is engine
  temperature, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_pm_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

## Libraries

Powertrain Blockset / Propulsion / Combustion Engines Vehicle Dynamics Blockset / Powertrain / Propulsion

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Spark-ignition engine model using lookup tables

The Mapped SI Engine block implements a mapped spark-ignition (SI)
engine model using power, air mass flow, fuel flow, exhaust temperature, efficiency, and
emission performance lookup tables. You can use the block for:

- Hardware-in-the-loop (HIL) engine control design
- Vehicle-level fuel economy and performance simulations

The block enables you to specify lookup tables for these engine
characteristics. The lookup tables, developed with the Model-Based Calibration Toolbox™, are functions of commanded torque,
*Tcmd*, brake torque,
*Tbrake*, and engine speed,
*N*. If you select **Input engine temperature**, the tables
are also a function of engine temperature,
*TempEng*.

| Table | **Input Engine Temperature** Parameter Setting | |
| --- | --- | --- |
| `off` | `on` |
| Power | *ƒ(Tcmd,N)* | *ƒ(Tcmd,N,TempEng)* |
| Air | *ƒ(Tbrake,N)* | *ƒ(Tbrake,N,TempEng)* |
| Fuel |
| Temperature |
| Efficiency |
| HC |
| CO |
| NOx |
| CO2 |
| PM |

To bound the Mapped SI Engine block output, the block does not
extrapolate the lookup table data.

### Virtual Calibration

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 2D lookup
tables using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import firing data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).    | Required Data | Optional Data | | --- | --- | | - Engine speed, rpm - Engine torque, N·m | - Air mass flow rate, kg/s - Brake specific fuel consumption,   g/(kW·h) - CO2 mass flow rate, kg/s - CO mass flow rate, kg/s - Exhaust temperature, K - Fuel mass flow rate, kg/s - HC mass flow rate, kg/s - NOx mass flow rate, kg/s - Particulate matter mass flow rate,   kg/s |  Collect firing data at steady-state operating conditions when injectors deliver the fuel. Data should cover the engine speed and torque operating range. Model-Based Calibration Toolbox uses the firing data boundary as the maximum torque.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Import non-firing data | Import this non-firing data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`.    - Engine speed, rpm - Engine torque, N·m  Collect non-firing (motoring) data at steady-state operating conditions when fuel is cut off. All non-firing torque points must be less than zero. Non-firing data is a function of engine speed only. |
| Generate response models | For both firing and non-firing data, the Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the firing and non-firing response models and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update the block lookup table and breakpoint parameters with the calibration. |

### Cylinder Air Mass

The block calculates the normalized cylinder air mass using
these equations.

MNom=PstdVdNcylRairTstdL=(60smin)Cps⋅m˙air(1000gKg)Ncyl⋅N⋅MNom

The equations use these variables.

|  |  |
| --- | --- |
| *L* | Normalized cylinder air mass |
| MNom | Nominal engine cylinder air mass at standard temperature and pressure, piston at bottom dead center (BDC) maximum volume, in kg |
| Cps | Crankshaft revolutions per power stroke, rev/stroke |
| Pstd | Standard pressure |
| Tstd | Standard temperature |
| Rair | Ideal gas constant for air and burned gas mixture |
| Vd | Displaced volume |
| Ncyl | Number of engine cylinders |
| *N* | Engine speed |
| m˙intk | Engine air mass flow, in g/s |

### Turbocharger Lag

To model turbocharger lag, select **Include
turbocharger lag effect**. During throttle control, the time constant
models the manifold filling and emptying dynamics. When the torque request requires a
turbocharger boost, the block uses a larger time constant to represent the turbocharger lag.
The block uses these equations.

|  |  |
| --- | --- |
| Dynamic torque | dTbrakedt=1τeng(Tstdy−Tbrake) |
| Boost time constant | τbst={τbst,rising       when Tstdy>Tbrakeτbst,falling      when Tstdy≤Tbrake |
| Final time constant | τeng={τthr       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) |

The equations use these variables.

|  |  |
| --- | --- |
| *Tbrake* | Brake torque |
| *Tstdy* | Steady-state target torque |
| *τbst* | Boost time constant |
| *τbst,rising*, *τbst,falling* | Boost rising and falling time constant, respectively |
| *τeng* | Final time constant |
| *τthr* | Time constant during throttle control |
| *ƒbst(N)* | Boost torque speed line |
| *N* | Engine speed |

### Fuel Flow

To calculate the fuel economy for high-fidelity models, the block uses the volumetric fuel flow.

Qfuel=m˙fuel(1000kgm3)Sgfuel

The equation uses these variables.

|  |  |
| --- | --- |
| m˙fuel | Fuel mass flow |
| *Sgfuel* | Specific gravity of fuel |
| *Qfuel* | Volumetric fuel flow |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrCrkshft` | Crankshaft power | −τengω |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFuel` | Fuel input power | m˙fuelLHV |
| `PwrLoss` | Power loss | τengω−m˙fuelLHV |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | | *Not used* | |

The equations use these variables.

|  |  |
| --- | --- |
| *LHV* | Fuel lower heating value |
| *ω* | Engine speed, rad/s |
| m˙fuel | Fuel mass flow |
| *τeng* | Fuel mass per injection time constant |
