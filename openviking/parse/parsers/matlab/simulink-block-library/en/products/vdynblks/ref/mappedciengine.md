---
type: simulink-block
title: 'Mapped CI Engine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain'
documentation_page: 'mappedciengine'
documentation_source_path: 'ref/mappedciengine.html'
language: en
---

# Mapped CI Engine

## Ports

### Input

### **FuelMassCmd** — Injected fuel mass command `scalar`

Injected fuel mass command, *F*, in mg/inj.

#### Dependencies

To enable this port, for **Input command**,
select `Fuel mass`.

### **TrqCmd** — Torque command `scalar`

Torque command, *T*, in N·m.

#### Dependencies

To enable this port, for **Input command**,
select `Torque`.

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
| `IntkGasMassFlw` | | | Engine air mass flow output | kg/s |
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

### **EngTrq** — Power `scalar`

Engine power, Tbrake, in N·m.

## Parameters

#### Block Options

### **Input command** — Table functions `Fuel mass` (default) | `Torque`

The lookup tables, developed with the Model-Based Calibration Toolbox, are functions of injected fuel mass, *F*, engine torque,
*T*, engine speed, *N*, and engine temperature,
*TempEng*.

| **Input Command** Setting | **Input Engine Temperature** Parameter Setting | Lookup Tables |
| --- | --- | --- |
| `Fuel mass` | `off` | *ƒ(F,N)* |
| `on` | *ƒ(F,N,TempEng)* |
| `Torque` | `off` | *ƒ(T,N)* |
| `on` | *ƒ(T,N,TempEng)* |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InputCmdPopup` |
| **Values:** | `Fuel mass` (default) | `Torque` |
| **Data Types:** | `character vector` |

#### Dependencies

- Selecting `Fuel mass` enables
  **Breakpoints for commanded fuel mass input,
  f\_tbrake\_f\_bpt**.
- Selecting `Torque` enables
  **Breakpoints for commanded torque input,
  f\_tbrake\_t\_bpt**.
- Selecting **Input engine temperature**
  enables **Breakpoints for temperature input,
  f\_tbrake\_engtmp\_bpt**.

### **Include turbocharger lag effect** — Increase time constant `off` (default) | `on`

To model turbocharger
lag, select **Include turbocharger lag effect**. Turbocharger lag limits the
maximum fuel mass per injection. To model the maximum fuel mass per injection, the block uses a
first-order system with a time constant. At low torque, the engine does not require boost to
provide sufficient air flow. When the requested fuel mass requires boost, the block uses a time
constant to determine the maximum fuel mass per injection. The block uses these equations for
the specified **Input command** setting.

| Calculation | **Input command** Parameter Setting | |
| --- | --- | --- |
| `Fuel mass` | `Torque` |
| Dynamic torque | dFmaxdt=1τeng(Fcmd−Fmax) | dTmaxdt=1τeng(Tcmd−Tmax) |
| Fuel mass per injection or torque - with turbocharger lag | F={Fcmd       when Fcmd<FmaxFmax      when Fcmd≥Fmax | Ttarget={Tcmd       when Tcmd<TmaxTmax      when Tcmd≥Tmax |
| Fuel mass per injection or torque- without turbocharger lag | F=Fcmd=Fmax | Ttarget=Tcmd=Tmax |
| Boost time constant | τbst={τbst,rising       when Fcmd>Fmaxτbst,falling      when Fcmd≤Fmax | τbst={τbst,rising       when Tcmd>Tmaxτbst,falling      when Tcmd≤Tmax |
| Final time constant | τeng={τnat       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) | |

The equations use these variables.

|  |  |
| --- | --- |
| *Tbrake* | Brake torque |
| *F* | Fuel mass per injection |
| *Fcmd*, *Fmax* | Commanded and maximum fuel mass per injection, respectively |
| *Ttarget*, *Tcmd*, *Tmax* | Target, commanded, and maximum torque, respectively |
| *τbst* | Boost time constant |
| *τbst,rising*, *τbst,falling* | Boost rising and falling time constant, respectively |
| *τeng* | Final time constant |
| *τnat* | Time constant below the boost torque speed line |
| *ƒbst(N)* | Boost torque/speed line |
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
  tau\_nat**
- **Rising maximum fuel mass boost time constant,
  tau\_bst\_rising**
- **Falling maximum fuel mass boost time constant,
  tau\_bst\_falling**

### **Input engine temperature** — Create input port `off` (default) | `on`

Select this to create the `EngTemp` input port.

The lookup tables, developed with the Model-Based Calibration Toolbox, are functions of injected fuel mass, *F*, engine torque,
*T*, engine speed, *N*, and engine temperature,
*TempEng*.

| **Input Command** Setting | **Input Engine Temperature** Parameter Setting | Lookup Tables |
| --- | --- | --- |
| `Fuel mass` | `off` | *ƒ(F,N)* |
| `on` | *ƒ(F,N,TempEng)* |
| `Torque` | `off` | *ƒ(T,N)* |
| `on` | *ƒ(T,N,TempEng)* |

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
| Import firing data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).  | **Input command** | Required Data | Optional Data | | --- | --- | --- | | `Fuel mass` | - Engine speed, rpm - Commanded fuel mass per injection, mg - Engine torque, N·m | - Air mass flow rate, kg/s - Brake specific fuel consumption,   g/(kW·h) - CO2 mass flow rate, kg/s - CO mass flow rate, kg/s - Exhaust temperature, K - Fuel mass flow rate, kg/s - HC mass flow rate, kg/s - NOx mass flow rate, kg/s - Particulate matter mass flow rate,   kg/s | | `Torque` | - Engine speed, rpm - Engine torque, N·m |  Collect firing data at steady-state operating conditions when injectors deliver the fuel. Data should cover the engine speed and torque operating range. Model-Based Calibration Toolbox uses the firing data boundary as the maximum torque.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Import non-firing data | Import this non-firing data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`.  - Engine speed, rpm - Engine torque, N·m    Collect non-firing (motoring) data at steady-state operating conditions when fuel is cut off. All non-firing torque points must be less than zero. Non-firing data is a function of engine speed only. |
| Generate response models | For both firing and non-firing data, the Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the firing and non-firing response models and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update the block lookup table and breakpoint parameters with the calibration. |

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Breakpoints for commanded fuel mass input, f\_tbrake\_f\_bpt** — Breakpoints `1`-by-`M` vector

Breakpoints, in mg/inj.

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

#### Dependencies

Setting **Input command** to `Fuel
mass` enables this parameter.

### **Breakpoints for commanded torque input, f\_tbrake\_t\_bpt** — Breakpoints `1`-by-`M` vector

Breakpoints, in N·m.

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

#### Dependencies

Setting **Input command** to
`Torque` enables this parameter.

### **Breakpoints for engine speed input, f\_tbrake\_n\_bpt** — Breakpoints `1`-by-`N` vector

Breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_n_bpt` |
| **Values:** | `1`-by-`N` vector |
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

### **Fuel specific gravity, Sg** — Specific gravity `0.832` (default) | `scalar`

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
port, in J/(kg·K).

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

### **Boost torque line, f\_tbrake\_bst** — Boost lag `[90,95,95,95,96,100,104,104,104,100,95,85,75,67,60,55]` (default) | `1`-by-`M` vector

Boost torque line, *ƒbst(N)*, in
N·m.

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

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

### **Time constant below boost line, tau\_nat** — Time constant below `0.1` (default) | `scalar`

Time constant below boost line,
*τnat*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau_nat` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

### **Rising maximum fuel mass boost time constant, tau\_bst\_rising** — Rising time constant `1.0` (default) | `scalar`

Rising maximum fuel mass boost time constant,
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

### **Falling maximum fuel mass boost time constant, tau\_bst\_falling** — Falling time constant `0.7` (default) | `scalar`

Falling maximum fuel mass boost time constant,
*τbst,falling*, in s.

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

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

### **Turbocharger time constant blend fuel mass fraction, f\_blend\_frac** — Time constant `0.01` (default) | `scalar`

Turbocharger time constant blend fuel mass fraction, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_blend_frac` |
| **Values:** | `0.01` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include turbocharger lag
effect**.

#### Power

### **Brake torque map, f\_tbrake** — 2D lookup table `M`-by-`N` matrix

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine brake torque lookup table is a function of commanded fuel mass and engine speed, Tbrake = ƒ(*F*, *N*), where:  - Tbrake is   engine torque, in N·m. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing actual torque as a function of engine speed and commanded fuel |
| `Torque` | The engine brake torque lookup table is a function of target torque and engine speed, Tbrake = ƒ(*Ttarget*, *N*), where:  - Tbrake is engine torque, in N·m. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Plot brake torque map** — Plot table button

Click to plot table.

#### Dependencies

To enable this parameter, clear **Input engine temperature**.

### **Brake torque map, f\_tbrake\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine brake torque lookup table is a function of commanded fuel mass and engine speed, Tbrake = ƒ(*F*, *N*, *TempEng*), where:  - Tbrake is engine torque, in N·m. - *F* is commanded fuel mass,   in mg per injection. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine brake torque lookup table is a function of target torque and engine speed, Tbrake = ƒ(*Ttarget*, *N*, *TempEng*), where:  - Tbrake is engine torque, in N·m. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The air mass flow lookup table is a function of commanded fuel mass and engine speed, m˙intk = ƒ(*Fmax*, *N*), where:  - m˙intk is engine air mass flow, in kg/s. - *Fmax* is commanded fuel mass, in mg per   injection. - *N* is engine speed, in rpm.    Plot showing air mass flow as a function of engine speed and commanded fuel |
| `Torque` | The air mass flow lookup table is a function of maximum torque and engine speed, m˙intk = ƒ(*Tmax*, *N*), where:  - m˙intk is engine air mass flow, in   kg/s. - *Tmax*   is maximum torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The air mass flow lookup table is a function of commanded fuel mass and engine speed, m˙intk = ƒ(*Fmax*, *N*, *TempEng*), where:  - m˙intk is engine air mass flow, in   kg/s. - *Fmax*   is commanded fuel mass, in mg per   injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The air mass flow lookup table is a function of maximum torque and engine speed, m˙intk = ƒ(*Tmax*, *N*, *TempEng*), where:  - m˙intk is engine air mass flow, in   kg/s. - *Tmax*   is maximum torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine fuel flow lookup table is a function of commanded fuel mass and engine speed, *MassFlow*= ƒ(*F*, *N*), where:  - *MassFlow* is engine fuel mass flow,   in kg/s. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing fuel mass flow as a function of engine speed and commanded fuel |
| `Torque` | The engine fuel flow lookup table is a function of target torque and engine speed, *MassFlow* = ƒ(*Ttarget*, *N*), where:  - *MassFlow* is engine fuel   mass flow, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine fuel flow lookup table is a function of commanded fuel mass, engine speed, and engine temperature, *MassFlow*= ƒ(*F*, *N*, *TempEng*), where:  - *MassFlow* is engine fuel   mass flow, in kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine fuel flow lookup table is a function of target torque and engine speed, and engine temperature, *MassFlow* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *MassFlow* is engine fuel   mass flow, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine exhaust temperature table is a function of commanded fuel mass and engine speed, *Texh*= ƒ(*F*, *N*), where:  - *Texh*is exhaust   temperature, in K. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing exhaust temperature as a function of engine speed and commanded fuel |
| `Torque` | The engine exhaust temperature table is a function of target torque and engine speed, *Texh* = ƒ(*Ttarget*, *N*), where:  - *Texh*   is exhaust temperature, in K. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

### **Exhaust temperature map, f\_texh\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine exhaust temperature table is a function of commanded fuel mass and engine speed, *Texh*= ƒ(*F*, *N*, *TempEng*), where:  - *Texh*is   exhaust temperature, in K. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine exhaust temperature table is a function of target torque and engine speed, *Texh* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *Texh*   is exhaust temperature, in K. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

### **BSFC map, f\_eff** — 2D lookup table `M`-by-`N` matrix

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The brake-specific fuel consumption (BSFC) efficiency is a function of commanded fuel mass and engine speed, *BSFC*= ƒ(*F*, *N*), where:  - *BSFC* is BSFC, in g/kWh. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing BSFC as a function of engine speed and commanded fuel |
| `Torque` | The brake-specific fuel consumption (BSFC) efficiency is a function of target torque and engine speed, *BSFC* = ƒ(*Ttarget*, *N*), where:  - *BSFC* is BSFC, in   g/kWh. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The brake-specific fuel consumption (BSFC) efficiency is a function of commanded fuel mass and engine speed, *BSFC*= ƒ(*F*, *N*, *TempEng*), where:  - *BSFC* is BSFC, in   g/kWh. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The brake-specific fuel consumption (BSFC) efficiency is a function of target torque and engine speed, *BSFC* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *BSFC* is BSFC, in   g/kWh. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out hydrocarbon emissions are a function of commanded fuel mass and engine speed, *EO HC*= ƒ(*F*, *N*), where:  - *EO HC* is engine-out hydrocarbon   emissions, in kg/s. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing EO HC as a function of engine speed and commanded fuel |
| `Torque` | The engine-out hydrocarbon emissions are a function of target torque and engine speed, *EO HC* = ƒ(*Ttarget*, *N*), where:  - *EO HC* is engine-out   hydrocarbon emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out hydrocarbon emissions are a function of commanded fuel mass and engine speed, *EO HC*= ƒ(*F*, *N*, *TempEng*), where:  - *EO HC* is engine-out   hydrocarbon emissions, in kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine-out hydrocarbon emissions are a function of target torque and engine speed, *EO HC* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *EO HC* is engine-out   hydrocarbon emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out carbon monoxide emissions are a function of commanded fuel mass and engine speed, *EO CO*= ƒ(*F*, *N*), where:  - *EO CO* is engine-out carbon monoxide   emissions, in kg/s. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing EO CO as a function of engine speed and commanded fuel |
| `Torque` | The engine-out carbon monoxide emissions are a function of target torque and engine speed, *EO CO* = ƒ(*Ttarget*, *N*), where:  - *EO CO* is engine-out   carbon monoxide emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

### **EO CO map, f\_co\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out carbon monoxide emissions are a function of commanded fuel mass and engine speed, *EO CO*= ƒ(*F*, *N*, *TempEng*), where:  - *EO CO* is engine-out   carbon monoxide emissions, in kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine-out carbon monoxide emissions are a function of target torque and engine speed, *EO CO* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *EO CO* is engine-out   carbon monoxide emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out nitric oxide and nitrogen dioxide emissions are a function of commanded fuel mass and engine speed, *EO NOx*= ƒ(*F*, *N*), where:  - *EO NOx* is engine-out nitric oxide   and nitrogen dioxide emissions, in kg/s. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing EO NOX as a function of engine speed and commanded fuel |
| `Torque` | The engine-out nitric oxide and nitrogen dioxide emissions are a function of target torque and engine speed, *EO NOx* = ƒ(*Ttarget*, *N*), where:  - *EO NOx* is engine-out   nitric oxide and nitrogen dioxide emissions, in   kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out nitric oxide and nitrogen dioxide emissions are a function of commanded fuel mass, engine speed, and engine temperature, *EO NOx*= ƒ(*F*, *N*, *TempEng*), where:  - *EO NOx* is engine-out   nitric oxide and nitrogen dioxide emissions, in   kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine-out nitric oxide and nitrogen dioxide emissions are a function of target torque, engine speed, and engine temperature, *EO NOx* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *EO NOx* is engine-out   nitric oxide and nitrogen dioxide emissions, in   kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out carbon dioxide emissions are a function of commanded fuel mass and engine speed, *EO CO2*= ƒ(*F*, *N*), where:  - *EO CO2* is engine-out carbon dioxide   emissions, in kg/s. - *F* is commanded fuel mass, in mg   per injection. - *N* is engine speed, in rpm.    Plot showing EO CO2 as a function of engine speed and commanded fuel |
| `Torque` | The engine-out carbon dioxide emissions are a function of target torque and engine speed, *EO CO2* = ƒ(*Ttarget*, *N*), where:  - *EO CO2* is engine-out   carbon dioxide emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out carbon dioxide emissions are a function of commanded fuel mass, engine speed, and engine temperature, *EO CO2*= ƒ(*F*, *N*, *TempEng*), where:  - *EO CO2* is engine-out   carbon dioxide emissions, in kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine-out carbon dioxide emissions are a function of target torque, engine speed, and engine temperature, *EO CO2* = ƒ(*Ttarget*, *N*, *TempEng*), where:  - *EO CO2* is engine-out   carbon dioxide emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out PM emissions are a function of commanded fuel mass and engine speed, where:  - *EO PM* is engine-out PM   emissions, in kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. |
| `Torque` | The engine-out PM emissions are a function of target torque and engine speed, *EO PM* = ƒ(*Ttarget*, *N*), where:  - *EO PM* is engine-out PM   emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. |

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

| **Input Command** Setting | Description |
| --- | --- |
| `Fuel mass` | The engine-out PM emissions are a function of commanded fuel mass, engine speed, and engine temperature, where:  - *EO PM* is engine-out PM   emissions, in kg/s. - *F* is commanded fuel mass,   in mg per injection. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |
| `Torque` | The engine-out PM emissions are a function of target torque, engine speed, and engine temperature, *EO PM* = ƒ(*Ttarget*, *N*, *T*), where:  - *EO PM* is engine-out PM   emissions, in kg/s. - *Ttarget*   is target torque, in N·m. - *N* is engine speed, in   rpm. - *TempEng*   is engine temperature, in K. |

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

Compression-ignition engine model using lookup tables

The Mapped CI Engine block implements a mapped compression-ignition
(CI) engine model using power, air mass flow, fuel flow, exhaust temperature,
efficiency, and emission performance lookup tables. You can use the block for:

- Hardware-in-the-loop (HIL) engine control design
- Vehicle-level fuel economy and performance simulations

The lookup tables, developed with the Model-Based Calibration Toolbox™, are functions of injected fuel mass, *F*, engine torque,
*T*, engine speed, *N*, and engine temperature,
*TempEng*.

| **Input Command** Setting | **Input Engine Temperature** Parameter Setting | Lookup Tables |
| --- | --- | --- |
| `Fuel mass` | `off` | *ƒ(F,N)* |
| `on` | *ƒ(F,N,TempEng)* |
| `Torque` | `off` | *ƒ(T,N)* |
| `on` | *ƒ(T,N,TempEng)* |

The block enables you to specify lookup tables for these engine characteristics:

- Power
- Air
- Fuel
- Temperature
- Efficiency
- Hydrocarbon (HC) emissions
- Carbon monoxide (CO) emissions
- Nitric oxide and nitrogen dioxide (NOx) emissions
- Carbon dioxide (CO2) emissions
- Particulate matter (PM) emissions

To bound the Mapped CI Engine block output, the block does not
extrapolate the lookup table data.

### Virtual Calibration

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 2D lookup
tables using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import firing data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).  | **Input command** | Required Data | Optional Data | | --- | --- | --- | | `Fuel mass` | - Engine speed, rpm - Commanded fuel mass per injection, mg - Engine torque, N·m | - Air mass flow rate, kg/s - Brake specific fuel consumption,   g/(kW·h) - CO2 mass flow rate, kg/s - CO mass flow rate, kg/s - Exhaust temperature, K - Fuel mass flow rate, kg/s - HC mass flow rate, kg/s - NOx mass flow rate, kg/s - Particulate matter mass flow rate,   kg/s | | `Torque` | - Engine speed, rpm - Engine torque, N·m |  Collect firing data at steady-state operating conditions when injectors deliver the fuel. Data should cover the engine speed and torque operating range. Model-Based Calibration Toolbox uses the firing data boundary as the maximum torque.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Import non-firing data | Import this non-firing data from a file. For example, open `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`.  - Engine speed, rpm - Engine torque, N·m    Collect non-firing (motoring) data at steady-state operating conditions when fuel is cut off. All non-firing torque points must be less than zero. Non-firing data is a function of engine speed only. |
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

To model turbocharger
lag, select **Include turbocharger lag effect**. Turbocharger lag limits the
maximum fuel mass per injection. To model the maximum fuel mass per injection, the block uses a
first-order system with a time constant. At low torque, the engine does not require boost to
provide sufficient air flow. When the requested fuel mass requires boost, the block uses a time
constant to determine the maximum fuel mass per injection. The block uses these equations for
the specified **Input command** setting.

| Calculation | **Input command** Parameter Setting | |
| --- | --- | --- |
| `Fuel mass` | `Torque` |
| Dynamic torque | dFmaxdt=1τeng(Fcmd−Fmax) | dTmaxdt=1τeng(Tcmd−Tmax) |
| Fuel mass per injection or torque - with turbocharger lag | F={Fcmd       when Fcmd<FmaxFmax      when Fcmd≥Fmax | Ttarget={Tcmd       when Tcmd<TmaxTmax      when Tcmd≥Tmax |
| Fuel mass per injection or torque- without turbocharger lag | F=Fcmd=Fmax | Ttarget=Tcmd=Tmax |
| Boost time constant | τbst={τbst,rising       when Fcmd>Fmaxτbst,falling      when Fcmd≤Fmax | τbst={τbst,rising       when Tcmd>Tmaxτbst,falling      when Tcmd≤Tmax |
| Final time constant | τeng={τnat       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) | |

The equations use these variables.

|  |  |
| --- | --- |
| *Tbrake* | Brake torque |
| *F* | Fuel mass per injection |
| *Fcmd*, *Fmax* | Commanded and maximum fuel mass per injection, respectively |
| *Ttarget*, *Tcmd*, *Tmax* | Target, commanded, and maximum torque, respectively |
| *τbst* | Boost time constant |
| *τbst,rising*, *τbst,falling* | Boost rising and falling time constant, respectively |
| *τeng* | Final time constant |
| *τnat* | Time constant below the boost torque speed line |
| *ƒbst(N)* | Boost torque/speed line |
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
