---
type: simulink-block
title: 'CI Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Controllers'
documentation_page: 'cicontroller'
documentation_source_path: 'ref/cicontroller.html'
language: en
---

# CI Controller

## Ports

### Input

### **TrqCmd** — Commanded engine torque `scalar`

Commanded engine torque, *Trqcmd,input*,
in N·m.

### **EngSpd** — Measured engine speed `scalar`

Measured engine speed, *N*, in rpm.

### **Map** — Measured intake manifold absolute pressure `scalar`

Measured intake manifold absolute pressure, *MAP*,
in Pa.

### **Mat** — Measured intake manifold absolute temperature `scalar`

Measured intake manifold absolute temperature, *MAT*,
in K.

### **AmbPrs** — Ambient pressure `scalar`

Absolute ambient pressure, PAmb,
in Pa.

### **EgrVlvAreaPct** — EGR valve area percent `scalar`

Measured EGR valve area percent, *EGRap*, in
%.

### **VgtPos** — VGT speed `scalar`

Measured VGT rack position,
*VGTpos*.

### **VgtSpd** — VGT speed `scalar`

Measured VGT speed, *Nvgt*, in
rpm.

### **Ect** — Engine cooling temperature `scalar`

Engine cooling temperature,
*Tcoolant*, in K.

### **IgSw** — Ignition switch `Boolean`

State of the vehicle ignition switch, dimensionless.

#### Dependencies

To create this port, on the **Stop-Start** tab, select **Enable Engine Stop-Start**.

### **ESSEnable** — Engine Stop-Start Enable `Boolean`

Command to enable or disable the stop-start logic, dimensionless.

#### Dependencies

To create this port, on the **Stop-Start** tab, select **Enable Engine Stop-Start**. Select **External Enable Port**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | Description | Variable | Units |
| --- | --- | --- | --- |
| `InjPw` | Fuel injector pulse-width | Pwinj | ms |
| `EgrVlvAreaPctCmd` | EGR valve area percent command | *EGRcmd* | % |
| `TurbRackPosCmd` | VGT rack position command | *RPcmd* | N/A |
| `TrqCmd` | Engine torque | *Trqcmd* | N·m |
| `FuelMassTotCmd` | Commanded total fuel mass per injection | *Fcmd,tot* | mg |
| `FuelMainSoi` | Main start-of-injection timing | *MAINSOI* | degATDC |
| `FuelMassFlwCmd` | Commanded fuel mass flow rate | m˙fuel,cmd | kg/s |
| `EstIntkPortMassFlw` | Estimated port mass flow rate | m˙port,est | kg/s |
| `EstEngTrq` | Estimated engine torque | *Trqest* | N·m |
| `EstExhManGasTemp` | Estimated exhaust manifold gas temperature | *Texh,est* | K |
| `EstExhPrs` | Estimated exhaust back-pressure | *Pex* | Pa |
| `EstEGRFlow` | `EstEGRFlow` | `EstEGRFlow` | `EstEGRFlow` |
| `EstAfr` | Estimated air-fuel ratio | *AFRest* | N/A |
| `EngRevLimAct` | Flag that indicates if rev-limiter control is active | N/A | N/A |

### **InjPw** — Fuel injector pulse-width `scalar`

Fuel injector pulse-width, Pwinj,
in ms.

### **FuelMainSoi** — Fuel main injecting timing `scalar`

Main start-of-injection timing, *MAINSOI*, in degrees crank angle after top
dead center (degATDC).

### **TurbRackPosCmd** — Rack position `scalar`

VGT rack position command, *RPcmd*.

### **EgrVlvAreaPctCmd** — Intake cam phaser angle command `scalar`

EGR valve area percent command, *EGRcmd*.

## Parameters

### Controls

#### Air - EGR

### **EGR valve area percent, f\_egrcmd** — Lookup table `array`

The commanded exhaust gas recirculation
(EGR) valve area percent lookup table is a function of commanded torque
and engine speed

EGRcmd=fEGRcmd(Trqcmd,N)

where:

- *EGRcmd* is
  commanded EGR valve area percent, in percent.
- *Trqcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

3D plot of commanded EGR valve area percent versus commanded torque and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_egrcmd` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Commanded torque breakpoints, f\_egr\_tq\_bpt** — Breakpoints `[10 26.43 42.86 59.29 75.71 92.14 108.6 125 141.4 157.9 174.3 190.7 207.1 223.6 240]` (default) | `vector`

Commanded torque breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_egr_tq_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Speed breakpoints, f\_egr\_n\_bpt** — Breakpoints `[1000 1411 1821 2232 2643 3054 3464 3875 4286 4696 5107 5518 5929 6339 6750]` (default) | `vector`

Speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_egr_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Air - VGR

### **VGT rack position table, f\_rpcmd** — Lookup table `array`

The variable geometry turbocharger (VGT) rack position lookup
table is a function of commanded torque and engine speed

RPcmd=fRPcmd(Trqcmd,N)

where:

- *RPcmd* is
  VGT rack position command, in percent.
- *Trqcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

3D plot of rack position versus commanded torque and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_rpcmd` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Commanded torque breakpoints, f\_rp\_tq\_bpt** — Breakpoints `[10 26.43 42.86 59.29 75.71 92.14 108.6 125 141.4 157.9 174.3 190.7 207.1 223.6 240]` (default) | `vector`

Breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_rp_tq_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Speed breakpoints, f\_rp\_n\_bpt** — Breakpoints `[1000 1411 1821 2232 2643 3054 3464 3875 4286 4696 5107 5518 5929 6339 6750]` (default) | `vector`

Breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_rp_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Fuel

### **Injector slope, Sinj** — Slope `6.452` (default) | `scalar`

Fuel injector slope, Sinj, in mg/ms.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Sinj` |
| **Values:** | `6.452` (default) | `scalar` |
| **Data Types:** | `double` |

### **Stoichiometric air-fuel ratio, afr\_stoich** — Ratio `14.6` (default) | `scalar`

Stoichiometric air-fuel ratio,
*AFRstoich*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `afr_stoich` |
| **Values:** | `14.6` (default) | `scalar` |
| **Data Types:** | `double` |

### **Fuel lower heating value, fuel\_lhv** — Heat `42e6` (default) | `scalar`

Fuel lower heating value, in J/kg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `fuel_lhv` |
| **Values:** | `42e6` (default) | `scalar` |
| **Data Types:** | `double` |

### **Fuel mass per injection table, f\_fcmd\_tot** — Lookup table `array`

The commanded total fuel mass per injection
table is a function of the torque command and engine speed

Fcmd,tot=fFcmd,tot(Trqcmd,N)

where:

- *Fcmd,tot* = *F* is
  commanded total fuel mass per injection, in mg per cylinder.
- *Trqcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

3D plot of commanded total fuel mass per injection versus commanded torque and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_fcmd_tot` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Fuel main injection timing table, f\_main\_soi** — Lookup table `array`

The main start-of-injection (SOI) timing
lookup table is a function of commanded fuel mass and engine speed

MAINSOI=f(Fcmd,tot,N)

where:

- *MAINSOI* is the main start-of-injection timing, in degrees crank
  angle after top dead center (degATDC).
- *Fcmd,tot* = *F* is
  commanded fuel mass, in mg per injection.
- *N* is engine speed, in rpm.

3D plot of main start-of-injection timing versus commanded fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_main_soi` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Fuel main injection timing fuel breakpoints, f\_main\_soi\_f\_bpt** — Breakpoints `vector`

Fuel main injection timing fuel breakpoints, in mg per
injection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_main_soi_f_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Fuel main injection timing speed breakpoints, f\_main\_soi\_n\_bpt** — Breakpoints `[1000,1410.71428571429,1821.42857142857,2232.14285714286,2642.85714285714,3053.57142857143,3464.28571428571,3875,4285.71428571429,4696.42857142857,5107.14285714286,5517.85714285714,5928.57142857143,6339.28571428572,6750]` (default) | `vector`

Fuel main injection timing speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_main_soi_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Commanded torque breakpoints, f\_f\_tot\_tq\_bpt** — Breakpoints `[0 10 26.43 42.86 59.29 75.71 92.14 108.6 125 141.4 157.9 174.3 190.7 207.1 223.6 240]` (default) | `vector`

Commanded torque breakpoints, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_f_tot_tq_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Speed breakpoints, f\_f\_tot\_n\_bpt** — Breakpoints `[1000 1411 1821 2232 2643 3054 3464 3875 4286 4696 5107 5518 5929 6339 6750]` (default) | `vector`

Speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_f_tot_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Idle Speed

### **Base idle speed, N\_idle** — Speed `750` (default) | `scalar`

Base idle speed, *Nidle*, in
rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_idle` |
| **Values:** | `750` (default) | `scalar` |
| **Data Types:** | `double` |

### **Enable torque command limit, Trq\_idlecmd\_enable** — Torque `1` (default) | `scalar`

Torque to enable the idle speed controller,
*Trqidlecmd,enable*, in
N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_idlecmd_enable` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Maximum torque command, Trq\_idlecmd\_max** — Torque `50` (default) | `scalar`

Maximum idle controller commanded torque,
*Trqidlecmd,max*, in
N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_idlecmd_max` |
| **Values:** | `50` (default) | `scalar` |
| **Data Types:** | `double` |

### **Proportional gain, Kp\_idle** — PI Controller `0.05` (default) | `scalar`

Proportional gain for idle speed control,
*Kp,idle*, in
N·m/rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp_idle` |
| **Values:** | `0.05` (default) | `scalar` |
| **Data Types:** | `double` |

### **Integral gain, Ki\_idle** — PI Controller `0.2` (default) | `scalar`

Integral gain for idle speed control,
*Ki,idle*, in
N·m/(rpm·s).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ki_idle` |
| **Values:** | `0.2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Rev-limiter speed threshold, EngRevLim** — Engine speed limit `6000` (default) | `scalar`

Engine speed limit, *Nlim*, in rpm.

If the engine speed, *N*, exceeds the engine speed limit,
*Nlim*, the block sets the commanded
engine torque to 0.

To smoothly transition the torque command to 0 as the engine speed approaches the
speed limit, the block implements a lookup table multiplier. The lookup table multiplies
the torque command by a value that ranges from 0 (engine speed exceeds limit) to 1
(engine speed does not exceed the limit).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EngRevLim` |
| **Values:** | `6000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Stop-Start

### **Enable Engine Stop-Start** — Select to enable the engine stop-start logic `off` (default) | `on`

Select to enable the engine stop-start logic. Selecting this option will activate
additional parameters to modify the behavior of the Engine Stop-Start block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ESSEnable` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **External Enable Port** — Create input port `off` (default) | `on`

Select to add a port to the engine controller block which enables or disables the
stop-start logic.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ESSExternalPortEnable` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, on the **Stop-Start** tab, select
**Enable Engine Stop-Start**.

### **Engine stop time, EngStopTime** — Engine stop time `5` (default) | `scalar`

Engine stop time for the stop-start logic, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EngStopTime` |
| **Values:** | `5` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Stop-Start** tab, select
**Enable Engine Stop-Start**.

### **Catalyst light off time, CatLightOffTime** — Catalyst light off time `0` (default) | `scalar`

Catalyst light off time for the stop-start logic, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CatLightOffTime` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Stop-Start** tab, select
**Enable Engine Stop-Start**.

### **Sample time, Ts** — Sample time `0.01` (default) | `scalar`

Sample time for the stop-start logic, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **Values:** | `0.01` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Stop-Start** tab, select
**Enable Engine Stop-Start**.

### Estimation

#### Air

### **Number of cylinders, NCyl** — Engine cylinders `4` (default) | `scalar`

Number of engine cylinders, Ncyl.

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

### **Crank revolutions per power stroke, Cps** — Revolutions per stroke `2` (default) | `scalar`

Crankshaft revolutions per power stroke, Cps, in rev/stroke.

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

Displaced volume, Vd, in m^3.

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

### **Ideal gas constant air, Rair** — Constant `287` (default) | `scalar`

Ideal gas constant, Rair, in J/(kg·K).

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

Standard air pressure, Pstd, in Pa.

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

Standard air temperature, Tstd, in K.

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

### **Speed density volumetric efficiency, f\_nv** — Lookup table `array`

The volumetric efficiency lookup table
is a function of the intake manifold absolute pressure at intake valve
closing (IVC) and engine speed

ηv=fηv(MAP,N)

where:

- ηv is
  engine volumetric efficiency, dimensionless.
- *MAP* is intake manifold absolute
  pressure, in KPa.
- *N* is engine speed, in rpm.

3D plot of engine volumetric efficiency versus intake manifold absolute pressure and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Speed density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — Breakpoints `[95 100.3 105.7 111 116.4 121.7 127.1 132.4 137.8 143.1 148.4 153.8 159.1 164.5 169.8 175.2 180.5 185.9 191.2 196.6 201.9 207.2 212.6 217.9 223.3 228.6 234 239.3 244.7 250]` (default) | `vector`

Intake manifold pressure breakpoints for speed-density volumetric
efficiency lookup table, in KPa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv_prs_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Speed density engine speed breakpoints, f\_nv\_n\_bpt** — Breakpoints `[750 956.9 1164 1371 1578 1784 1991 2198 2405 2612 2819 3026 3233 3440 3647 3853 4060 4267 4474 4681 4888 5095 5302 5509 5716 5922 6129 6336 6543 6750]` (default) | `vector`

Engine speed breakpoints for speed-density volumetric efficiency
lookup table, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **EGR valve standard flow calibration, f\_egr\_stdflow** — Lookup table `array`

The standard exhaust gas recirculation (EGR)
mass flow is a lookup table that is a function of the standard flow
pressure ratio and EGR valve flow area

m˙egr,std=f(MAPPexh,est,EGRap)

where:

- m˙egr,std is
  the standard EGR valve mass flow, in g/s.
- *Pexh,est* is
  the estimated exhaust back-pressure, in Pa.
- *MAP* is the cycle average intake
  manifold absolute pressure, in Pa.
- *EGRap* is the measured EGR valve
  area, in percent.

3D plot of standard EGR valve mass flow versus cycle average intake manifold absolute pressure and measured EGR valve area

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_egr_stdflow` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **EGR valve standard flow pressure ratio breakpoints, f\_egr\_stdflow\_pr\_bpt** — Breakpoints `vector`

EGR valve standard flow pressure ratio breakpoints,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_egr_stdflow_pr_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **EGR valve standard flow area percent breakpoints, f\_egr\_stdflow\_egrap\_bpt** — Breakpoints `vector`

EGR valve standard flow area percent breakpoints, in percent.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_egr_stdflow_egrap_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Turbocharger pressure ratio, f\_turbo\_pr** — Lookup table `array`

The turbocharger pressure ratio, corrected
for variable geometry turbocharger (VGT) speed, is a lookup table
that is a function of the standard air mass flow and corrected turbocharger
speed, Prturbo=f(m˙airstd,Nvgtcorr),
where:

- *Prturbo* is
  the turbocharger pressure ratio, corrected for VGT speed.
- m˙airstd is
  the standard air mass flow, in g/s.
- *Nvgtcorr* is
  the corrected turbocharger speed, in rpm/K^(1/2).

3D plot of s turbocharger pressure ratio versus standard air mass flow and corrected turbocharger speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_turbo_pr` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Turbocharger pressure ratio standard flow breakpoints, f\_turbo\_pr\_stdflow\_bpt** — Breakpoints `vector`

Turbocharger pressure ratio standard flow breakpoints, in g/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_turbo_pr_stdflow_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Turbocharger pressure ratio corrected speed breakpoints, f\_turbo\_pr\_corrspd\_bpt** — Breakpoints `vector`

Turbocharger pressure ratio corrected speed breakpoints, in
rpm/K^(1/2).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_turbo_pr_corrspd_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Turbocharger pressure ratio VGT position correction, f\_turbo\_pr\_vgtposcorr** — Lookup table `array`

The variable geometry turbocharger pressure
ratio correction is a function of the rack position, *Prvgtcorr*=
ƒ(*VGTpos*), where:

- *Prvgtcorr* is
  the turbocharger pressure ratio correction.
- *VGTpos* is
  the variable geometry turbocharger (VGT) rack position.

Plot of turbocharger pressure ratio correction versus variable geometry turbocharger (VGT) rack position

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_turbo_pr_vgtposcorr` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Turbocharger pressure ratio VGT position correction breakpoints, f\_turbo\_pr\_vgtposcorr\_bpt** — Breakpoints `vector`

Turbocharger pressure ratio VGT position correction breakpoints,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_nv_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Torque - Simple Torque Lookup

### **Torque table, f\_tq\_nf** — Lookup table `array`

For the simple torque lookup table model, the CI engine uses
a lookup table is a function of engine speed and injected fuel mass, Tbrake=fTnf(F,N),
where:

- *Tq* = *Tbrake* is
  engine brake torque after accounting for engine mechanical and pumping
  friction effects, in N·m.
- *F* is injected fuel mass, in mg
  per injection.
- *N* is engine speed, in rpm.

3D plot of engine brake torque versus injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tq_nf` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Simple Torque Lookup`.

### **Torque table fuel mass per injection breakpoints, f\_tq\_nf\_f\_bpt** — Breakpoints `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]` (default) | `vector`

Torque table fuel mass per injection breakpoints, in mg per injection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tq_nf_f_bpt` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Simple Torque Lookup`.

### **Torque table speed breakpoints, f\_tq\_nf\_n\_bpt** — Breakpoints `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]` (default) | `vector`

Engine speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tq_nf_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Simple Torque Lookup`.

#### Torque - Torque Structure

### **Fuel mass per injection breakpoints, f\_tqs\_f\_bpt** — Breakpoints `vector`

Fuel mass per injection breakpoints, in mg per injection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_f_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Engine speed breakpoints, f\_tqs\_n\_bpt** — Breakpoints `[500 750 1000 1250 1500 1750 2000 2250 2500 2750 3000 3250 3500 3750 4000]` (default) | `vector`

Engine speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal main start of injection timing, f\_tqs\_mainsoi** — Optimal MAINSOI `array`

The optimal main start of injection (SOI) timing lookup table,
*ƒSOIc*, is a function of the engine speed and
injected fuel mass, *SOIc =
ƒSOIc(F,N)*, where:

- *SOIc* is optimal SOI timing, in
  degATDC.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal SOI timing versus injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mainsoi` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal intake manifold gas pressure, f\_tqs\_map** — Optimal intake MAP `array`

The optimal intake manifold gas pressure lookup table,
*ƒMAP*, is a function of the engine speed and
injected fuel mass, *MAP = ƒMAP(F,N)*, where:

- *MAP* is optimal intake manifold gas pressure, in Pa.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal intake manifold gas pressure versus injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_map` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal exhaust manifold gas pressure, f\_tqs\_emap** — Optimal exhaust MAP `array`

The optimal exhaust manifold gas pressure lookup table,
*ƒEMAP*, is a function of the engine speed and
injected fuel mass, *EMAP = ƒEMAP(F,N)*, where:

- *EMAP* is optimal exhaust manifold gas pressure, in Pa.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of exhaust manifold gas pressure versus injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_emap` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal intake manifold gas temperature, f\_tqs\_mat** — Optimal intake MAT `array`

The optimal intake manifold gas temperature lookup table,
*ƒMAT*, is a function of the engine speed and
injected fuel mass, *MAT = ƒMAT(F,N)*, where:

- *MAT* is optimal intake manifold gas temperature, in K.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal intake gas temperature versus compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mat` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal intake gas oxygen percent, f\_tqs\_o2pct** — Optimal intake gas oxygen `array`

The optimal intake gas oxygen percent lookup table,
*ƒO2*, is a function of the engine speed and
injected fuel mass, *O2PCT = ƒO2(F,N)*, where:

- *O2PCT* is optimal intake gas oxygen, in percent.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal intake gas oxygen versus compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_o2pct` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal fuel rail pressure, f\_tqs\_fuelpress** — Optimal fuel rail pressure `array`

The optimal fuel rail pressure lookup table,
*ƒfuelp*, is a function of the engine speed and
injected fuel mass, *FUELP = ƒfuelp(F,N)*, where:

- *FUELP* is optimal fuel rail pressure, in MPa.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal fuel rail pressure versus compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fuelpress` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal gross indicated mean effective pressure, f\_tqs\_imepg** — Optimal mean effective pressure `array`

The optimal gross indicated mean effective pressure lookup
table, *ƒimepg*, is a function of the engine speed and
injected fuel mass, *IMEPG = ƒimepg(F,N)*, where:

- *IMEPG* is optimal gross indicated mean effective pressure, in
  Pa.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal gross indicated mean effective pressure versus compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_imepg` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal friction mean effective pressure, f\_tqs\_fmep** — Optimal friction mean effective pressure `array`

The optimal friction mean effective pressure lookup table,
*ƒfmep*, is a function of the engine speed and
injected fuel mass, *FMEP = ƒfmep(F,N)*, where:

- *FMEP* is optimal friction mean effective pressure, in Pa.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal friction mean effective pressure versus compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fmep` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Optimal pumping mean effective pressure, f\_tqs\_pmep** — Optimal pumping mean effective pressure `array`

The optimal pumping mean effective pressure lookup table,
*ƒpmep*, is a function of the engine speed and
injected fuel mass, *PMEP = ƒpmep(F,N)*, where:

- *PMEP* is optimal pumping mean effective pressure, in Pa.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal pumping mean effective pressure versus intake manifold gas pressure ratio relative to compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_pmep` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Friction multiplier as a function of temperature, f\_tqs\_fric\_temp\_mod** — Friction multiplier `array`

Friction multiplier as a function of temperature, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fric_temp_mod` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Friction multiplier temperature breakpoints, f\_tqs\_fric\_temp\_bpt** — Breakpoints `vector`

Friction multiplier temperature breakpoints, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fric_temp_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Main start of injection timing efficiency multiplier, f\_tqs\_mainsoi\_eff** — MAINSOI efficiency multiplier `array`

The main start of injection (SOI) timing efficiency multiplier
lookup table, *ƒSOIeff*, is a function of the engine
speed and main SOI timing relative to optimal timing, *SOIeff =
ƒSOIeff(ΔSOI,N)*, where:

- *SOIeff* is main SOI timing efficiency
  multiplier, dimensionless.
- *ΔSOI* is main SOI timing relative to optimal timing, in
  degBTDC.
- *N* is engine speed, in rpm.

3D plot of SOI timing efficiency multiplier versus main SOI timing relative to optimal timing and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mainsoi_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Main start of injection timing relative to optimal timing breakpoints, f\_tqs\_mainsoi\_delta\_bpt** — Breakpoints `vector`

Main start of injection timing relative to optimal timing breakpoints, in
degBTDC.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mainsoi_delta_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas pressure efficiency multiplier, f\_tqs\_map\_eff** — Intake pressure efficiency multiplier `array`

The intake manifold gas pressure efficiency multiplier lookup
table, *ƒMAPeff*, is a function of the intake manifold
gas pressure ratio relative to optimal pressure ratio and lambda,
*MAPeff =
ƒMAPeff(MAPratio,λ)*, where:

- *MAPeff* is intake manifold gas pressure
  efficiency multiplier, dimensionless.
- *MAPratio* is intake manifold gas pressure
  ratio relative to optimal pressure ratio, dimensionless.
- *λ* is intake manifold gas lambda, dimensionless.

3D plot of intake manifold gas pressure efficiency multiplier versus intake manifold gas pressure ratio relative to optimal pressure ratio and intake manifold gas lambda

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_map_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas pressure ratio relative to optimal pressure ratio breakpoints, f\_tqs\_map\_ratio\_bpt** — Breakpoints `[0.8;0.85;0.9;0.95;1;1.05;1.1;1.15;1.2;1.25;1.3;1.35;1.4;1.45;1.5]` (default) | `vector`

Intake manifold gas pressure ratio relative to optimal pressure ratio breakpoints,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_map_ratio_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas lambda breakpoints, f\_tqs\_lambda\_bpt** — Breakpoints `[1.5 1.678571428571429 1.857142857142857 2.035714285714286 2.214285714285714 2.392857142857143 2.571428571428571 2.75 2.928571428571429 3.107142857142857 3.285714285714286 3.464285714285714 3.642857142857143 3.821428571428572 4]` (default) | `vector`

Intake manifold gas lambda breakpoints, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_lambda_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas temperature efficiency multiplier, f\_tqs\_mat\_eff** — Intake temperature efficiency multiplier `array`

The intake manifold gas temperature efficiency multiplier
lookup table, *ƒMATeff*, is a function of the engine
speed and intake manifold gas temperature relative to optimal temperature,
*MATeff =
ƒMATeff(ΔMAT,N)*, where:

- *MATeff* is intake manifold gas
  temperature efficiency multiplier, dimensionless.
- *ΔMAT* is intake manifold gas temperature relative to optimal
  temperature, in K.
- *N* is engine speed, in rpm.

3D plot of intake manifold gas temperature efficiency multiplier versus intake gas oxygen percent relative to optimal and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mat_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas temperature relative to optimal gas temperature breakpoints, f\_tqs\_mat\_delta\_bpt** — Breakpoints `[-55;-50;-45;-40;-35;-30;-25;-20;-15;-10;-5;0;5;10;15]` (default) | `vector`

Intake manifold gas temperature relative to optimal gas temperature breakpoints,
in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mat_delta_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas oxygen efficiency multiplier, f\_tqs\_o2pct\_eff** — Intake oxygen efficiency multiplier `array`

The intake manifold gas oxygen efficiency multiplier lookup
table, *ƒO2Peff*, is a function of the engine speed and
intake manifold gas oxygen percent relative to optimal, *O2Peff =
ƒO2Peff(ΔO2P,N)*, where:

- *O2Peff* is intake manifold gas oxygen
  efficiency multiplier, dimensionless.
- *ΔO2P* is intake gas oxygen percent relative to optimal, in
  percent.
- *N* is engine speed, in rpm.

3D plot of optimal intake manifold gas oxygen efficiency multiplier versus intake gas oxygen percent relative to optimal and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_o2pct_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake gas oxygen percent relative to optimal breakpoints, f\_tqs\_o2pct\_delta\_bpt** — Breakpoints `vector`

Intake gas oxygen percent relative to optimal breakpoints, in percent.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_o2pct_delta_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Fuel rail pressure efficiency multiplier, f\_tqs\_fuelpress\_eff** — Efficiency multiplier `array`

The fuel rail pressure efficiency multiplier lookup table,
*ƒFUELPeff*, is a function of the engine speed
and fuel rail pressure relative to optimal breakpoints, *FUELPeff
= ƒFUELPeff(ΔFUELP,N)*, where:

- *FUELPeff* is fuel rail pressure
  efficiency multiplier, dimensionless.
- *ΔFUELP* is fuel rail pressure relative to optimal, in
  MPa.
- *N* is engine speed, in rpm.

3D plot of fuel rail pressure efficiency multiplier versus fuel rail pressure relative to optimal and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fuelpress_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Fuel rail pressure relative to optimal breakpoints, f\_tqs\_fuelpress\_delta\_bpt** — Breakpoints `vector`

Fuel rail pressure relative to optimal breakpoints, in MPa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fuelpress_delta_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Fuel mass injection type identifier, f\_tqs\_f\_inj\_type** — Type identifier `0` (default) | `scalar`

Fuel mass injection type identifier, dimensionless.

In the CI Core Engine and CI
Controller blocks, you can represent multiple injections with the start of injection
(SOI) and fuel mass inputs to the model. To specify the type of injection, use the
**Fuel mass injection type identifier** parameter.

| Type of Injection | Parameter Value |
| --- | --- |
| Pilot | `0` |
| Main | `1` |
| Post | `2` |
| Passed | `3` |

The model considers `Passed` fuel injections and fuel injected
later than a threshold to be unburned fuel. Use the **Maximum start of injection angle
for burned fuel, f\_tqs\_f\_burned\_soi\_limit** parameter to specify the
threshold.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_f_inj_type` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Indicated mean effective pressure post inject correction, f\_tqs\_imep\_post\_corr** — Post inject correction `array`

The indicated mean effective pressure post inject correction
lookup table, *ƒIMEPpost*, is a function of the engine
speed and fuel rail pressure relative to optimal breakpoints,
*ΔIMEPpost =
ƒIMEPpost(ΔSOIpost,Fpost)*, where:

- *ΔIMEPpost* is indicated mean effective
  pressure post inject correction, in Pa.
- *ΔSOIpost* is indicated mean effective
  pressure post inject start of inject timing centroid, in degATDC.
- *Fpost* is indicated mean effective
  pressure post inject mass sum, in mg per injection.

3D plot of indicated mean effective pressure versus pressure post inject start of inject timing and pressure post inject mass sum

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_imep_post_corr` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Indicated mean effective pressure post inject mass sum breakpoints, f\_tqs\_f\_post\_sum\_bpt** — Breakpoints `[0 3.571428571428572 7.142857142857143 10.71428571428571 14.28571428571429 17.85714285714286 21.42857142857143 25 28.57142857142857 32.14285714285715 35.71428571428572 39.28571428571428 42.85714285714285 46.42857142857143 50]` (default) | `vector`

Indicated mean effective pressure post inject mass sum breakpoints, in mg per
injection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_f_post_sum_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Indicated mean effective pressure post inject start of inject timing centroid breakpoints, f\_tqs\_soi\_post\_cent\_bpt** — Breakpoints `[150 160.7142857142857 171.4285714285714 182.1428571428571 192.8571428571429 203.5714285714286 214.2857142857143 225 235.7142857142857 246.4285714285714 257.1428571428571 267.8571428571429 278.5714285714286 289.2857142857143 300]` (default) | `vector`

Indicated mean effective pressure post inject start of inject timing centroid
breakpoints, in degATDC.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_soi_post_cent_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Maximum start of injection angle for burned fuel, f\_tqs\_f\_burned\_soi\_limit** — Maximum SOI angle for burned fuel `500` (default) | `scalar`

Maximum start of injection angle for burned fuel, in degATDC.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_f_bpt` |
| **Values:** | `500` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

#### Exhaust

### **Exhaust gas specific heat at constant pressure, cp\_exh** — Specific heat `1005` (default) | `scalar`

Exhaust gas-specific heat, Cpexh, in J/(kg·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `cp_exh` |
| **Values:** | `1005` (default) | `scalar` |
| **Data Types:** | `double` |

#### Exhaust Temperature - Simple Torque Lookup

### **Exhaust temperature table, f\_t\_exh** — Lookup table `array`

The lookup table for the
exhaust temperature is a function of injected fuel mass and engine
speed

Texh=fTexh(F,N)

where:

- Texh is
  exhaust temperature, in K.
- *F* is injected fuel mass, in mg
  per injection.
- *N* is engine speed, in rpm.

3D plot of exhaust temperature versus engine speed and engine torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_t_exh` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Simple Torque Lookup`.

### **Fuel mass per injection breakpoints, f\_t\_exh\_f\_bpt** — Breakpoints `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]` (default) | `vector`

Engine load breakpoints used for exhaust temperature lookup table, in mg per
injection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_t_exh_f_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Simple Torque Lookup`.

### **Speed breakpoints, f\_t\_exh\_n\_bpt** — Breakpoints `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]` (default) | `vector`

Engine speed breakpoints used for exhaust temperature lookup table, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_t_exh_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Simple Torque Lookup`.

#### Exhaust Temperature - Torque Structure

### **Optimal exhaust manifold gas temperature, f\_tqs\_exht** — Optimal exhaust manifold gas temperature `array`

The optimal exhaust manifold gas temperature lookup table,
*ƒTexh*, is a function of the engine speed
engine speed and injected fuel mass, *Texhopt =
ƒTexh(F,N)*, where:

- *Texhopt* is optimal exhaust manifold gas
  temperature, in K.
- *F* is compression stroke injected fuel mass, in mg per
  injection.
- *N* is engine speed, in rpm.

3D plot of optimal exhaust manifold gas temperature versus compression stroke injected fuel mass and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Main start of injection timing exhaust temperature efficiency multiplier, f\_tqs\_exht\_mainsoi\_eff** — Main SOI timing efficiency multiplier `array`

The main start of injection (SOI) timing exhaust temperature
efficiency multiplier lookup table, *ƒSOIexhteff*, is a
function of the engine speed engine speed and injected fuel mass,
*SOIexhteff =
ƒSOIexhteff(ΔSOI,N)*, where:

- *SOIexhteff* is main SOI exhaust
  temperature efficiency multiplier, dimensionless.
- *ΔSOI* is main SOI timing relative to optimal timing, in
  degBTDC.
- *N* is engine speed, in rpm.

3D plot SOI exhaust temperature efficiency multiplier versus main SOI timing relative to optimal timing and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_mainsoi_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas pressure exhaust temperature efficiency multiplier, f\_tqs\_exht\_map\_eff** — Intake manifold efficiency multiplier `array`

The intake manifold gas pressure exhaust temperature efficiency
multiplier lookup table, *ƒMAPexheff*, is a function of
the intake manifold gas pressure ratio relative to optimal pressure ratio and lambda,
*MAPexheff =
ƒMAPexheff(MAPratio,λ)*, where:

- *MAPexheff* is intake manifold gas
  pressure exhaust temperature efficiency multiplier, dimensionless.
- *MAPratio* is intake manifold gas pressure
  ratio relative to optimal pressure ratio, dimensionless.
- *λ* is intake manifold gas lambda, dimensionless.

3D plot of intake manifold gas pressure exhaust temperature efficiency multiplier versus intake manifold gas pressure ratio relative to optimal pressure ratio and intake manifold gas lambda

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_map_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas temperature exhaust temperature efficiency multiplier, f\_tqs\_exht\_mat\_eff** — Intake manifold efficiency multiplier `array`

The intake manifold gas temperature exhaust temperature
efficiency multiplier lookup table, *ƒMATexheff*, is a
function of the engine speed and intake manifold gas temperature relative to optimal
temperature, *MATexheff =
ƒMATexheff(ΔMAT,N)*, where:

- *MATexheff* is intake manifold gas
  temperature exhaust temperature efficiency multiplier, dimensionless.
- *ΔMAT* is intake manifold gas temperature relative to optimal
  temperature, in K.
- *N* is engine speed, in rpm.

3D plot of intake manifold gas temperature exhaust temperature efficiency multiplier versus intake manifold gas temperature relative to optimal temperature and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_mat_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Intake manifold gas oxygen exhaust temperature efficiency multiplier, f\_tqs\_exht\_o2pct\_eff** — Intake manifold efficiency multiplier `array`

The intake manifold gas oxygen exhaust temperature efficiency
multiplier lookup table, *ƒO2Pexheff*, is a function of
the engine speed and intake manifold gas oxygen percent relative to optimal,
*O2Pexheff =
ƒO2Pexheff(ΔO2P,N)*, where:

- *O2Pexheff* is intake manifold gas oxygen
  exhaust temperature efficiency multiplier, dimensionless.
- *ΔO2P* is intake gas oxygen percent relative to optimal, in
  percent.
- *N* is engine speed, in rpm.

3D plot of optimal intake manifold gas oxygen exhaust temperature efficiency multiplier versus intake gas oxygen percent relative to optimal and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_o2pct_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Fuel rail pressure exhaust temperature efficiency multiplier, f\_tqs\_exht\_fuelpress\_eff** — Fuel rail pressure exhaust temperature efficiency multiplier `array`

The fuel rail pressure efficiency exhaust temperature
multiplier lookup table, *ƒFUELPexheff*, is a function
of the engine speed and fuel rail pressure relative to optimal breakpoints,
*FUELPexheff =
ƒFUELPexheff(ΔFUELP,N)*, where:

- *FUELPexheff* is fuel rail pressure
  exhaust temperature efficiency multiplier, dimensionless.
- *ΔFUELP* is fuel rail pressure relative to optimal, in
  MPa.
- *N* is engine speed, in rpm.

3D plot of fuel rail pressure exhaust temperature efficiency multiplier versus fuel rail pressure relative to optimal and engine speed

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_fuelpress_eff` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **Post-injection cylinder wall heat loss transfer coefficient, f\_tqs\_exht\_post\_inj\_wall\_htc** — Post-injection offset `0` (default) | `scalar`

Post-injection cylinder wall heat loss transfer coefficient, in W/K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_post_inj_wall_htc` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Compression-ignition controller that includes air mass flow, torque, and EGR estimation

The CI Controller block implements a compression-ignition (CI) controller with
air mass flow, torque, exhaust gas recirculation (EGR) flow, exhaust back-pressure, and
exhaust gas temperature estimation. You can use the CI Controller block
in engine control design or performance, fuel economy, and emission tradeoff studies.
The core engine block requires the commands that are output from the CI
Controller block.

The block uses the commanded torque and measured engine speed
to determine these open-loop actuator commands:

- Injector pulse-width
- Fuel injection timing
- Variable geometry turbocharger (VGT) rack position
- EGR valve area percent

The CI Controller block has two subsystems:

- The `Controller` subsystem —
  Determines the commands based on tables that are functions of commanded
  torque and measured engine speed.

  | Based On | Determines Commands for |
  | --- | --- |
  | Commanded torque  Measured engine speed | Injector pulse-width  Fuel injection timing  VGT rack position  EGR valve area percent |
- The `Estimator` subsystem —
  Determines estimates based on these engine attributes.

  | Based On | Estimates |
  | --- | --- |
  | Measured engine speed  Fuel injection timing  Cycle average intake manifold pressure and temperature  Fuel injector pulse-width  Absolute ambient pressure  EGR valve area percent  VGT rack position  VGT speed | Air mass flow  Torque  Exhaust gas temperature  Exhaust gas back-pressure  EGR valve gas mass flow |

The figure illustrates the signal flow.

CI Controller block connections showing combustion and fluid flow

The figure uses these variables.

|  |  |
| --- | --- |
| *N* | Engine speed |
| *MAP* | Cycle average intake manifold absolute pressure |
| *MAT* | Cycle average intake manifold gas absolute temperature |
| *EGRap*, *EGRcmd* | EGR valve area percent and EGR valve area percent command, respectively |
| *VGTpos* | VGT rack position |
| *Nvgt* | Corrected turbocharger speed |
| *RPcmd* | VGT rack position command |
| Pwinj | Fuel injector pulse-width |
| *MAINSOI* | Start of injection timing for main fuel injection pulse |

The Model-Based Calibration Toolbox™ was used to develop the
tables that are available with the Powertrain Blockset™.

### Controller

The controller governs the combustion process by commanding
VGT rack position, EGR valve area percent, fuel injection timing,
and injector pulse-width. Feedforward lookup tables, which are functions
of measured engine speed and commanded torque, determine the control
commands.

**Air**

The controller commands the EGR valve area percent and VGT rack
position. Changing the VGT rack position modifies the turbine flow
characteristics. At low-requested torques, the rack position can reduce
the exhaust back pressure, resulting in a low turbocharger speed and
boost pressure. When the commanded fuel requires additional air mass
flow, the rack position is set to close the turbocharger vanes, increasing
the turbocharger speed and intake manifold boost pressure.

The variable geometry turbocharger (VGT) rack position lookup
table is a function of commanded torque and engine speed

RPcmd=fRPcmd(Trqcmd,N)

where:

- *RPcmd* is
  VGT rack position command, in percent.
- *Trqcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

3D plot of rack position versus commanded torque and engine speed

The commanded exhaust gas recirculation
(EGR) valve area percent lookup table is a function of commanded torque
and engine speed

EGRcmd=fEGRcmd(Trqcmd,N)

where:

- *EGRcmd* is
  commanded EGR valve area percent, in percent.
- *Trqcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

3D plot of commanded EGR valve area percent versus commanded torque and engine speed

**Fuel**

To initiate combustion, a CI engine injects fuel directly into
the combustion chamber. After the injection, the fuel spontaneously
ignites, increasing cylinder pressure. The total mass of the injected
fuel and main injection timing determines the torque production.

Assuming constant fuel rail pressure, the CI controller commands
the injector pulse-width based on the total requested fuel mass:

Pwinj=Fcmd, totSinj

The equation uses these variables.

|  |  |
| --- | --- |
| Pwinj | Fuel injector pulse-width |
| *Sinj* | Fuel injector slope |
| *Fcmd,tot* | Commanded total fuel mass per injection |
| *MAINSOI* | Main start-of-injection timing |
| *N* | Engine speed |

The commanded total fuel mass per injection
table is a function of the torque command and engine speed

Fcmd,tot=fFcmd,tot(Trqcmd,N)

where:

- *Fcmd,tot* = *F* is
  commanded total fuel mass per injection, in mg per cylinder.
- *Trqcmd* is
  commanded engine torque, in N·m.
- *N* is engine speed, in rpm.

3D plot of commanded total fuel mass per injection versus commanded torque and engine speed

The main start-of-injection (SOI) timing
lookup table is a function of commanded fuel mass and engine speed

MAINSOI=f(Fcmd,tot,N)

where:

- *MAINSOI* is the main start-of-injection timing, in degrees crank
  angle after top dead center (degATDC).
- *Fcmd,tot* = *F* is
  commanded fuel mass, in mg per injection.
- *N* is engine speed, in rpm.

3D plot of main start-of-injection timing versus commanded fuel mass and engine speed

**Idle Speed**

When the commanded torque is below a threshold value, the idle
speed controller regulates the engine speed.

| If | Idle Speed Controller |
| --- | --- |
| *Trqcmd,input* < *Trqidlecmd,enable* | Enabled |
| *Trqidlecmd,enable* ≤ *Trqcmd,input* | Not enabled |

The idle speed controller uses a discrete PI controller to regulate
the target idle speed by commanding a torque.

The PI controller uses this transfer function:

Cidle(z)=Kp,idle+Ki,idletsz−1

The idle speed commanded torque must be less than the maximum
commanded torque:

0 ≤ *Trqidlecomd* ≤*Trqidlecmd,max*

Idle speed control is active under these conditions. If the
commanded input torque drops below the threshold for enabling the
idle speed controller (*Trqcmd,input* < *Trqidlecmd,enable*),
the commanded engine torque is given by:

*Trqcmd* = max(*Trqcmd,input*,*Trqidlecmd*).

The equations use these variables.

|  |  |
| --- | --- |
| *Trqcmd* | Commanded engine torque |
| *Trqcmd,input* | Input commanded engine torque |
| *Trqidlecmd,enable* | Threshold for enabling idle speed controller |
| *Trqidlecmd* | Idle speed controller commanded torque |
| *Trqidlecmd,max* | Maximum commanded torque |
| *Nidle* | Base idle speed |
| *Kp,idle* | Idle speed controller proportional gain |
| *Ki,idle* | Idle speed controller integral gain |

**Speed Limiter**

To prevent over revving the engine, the block implements an engine speed limit controller that
limits the engine speed to the value specified by the **Rev-limiter speed
threshold** parameter on the **Controls** > **Idle
Speed** tab.

If the engine speed, *N*, exceeds the engine speed limit,
*Nlim*, the block sets the commanded engine
torque to 0.

To smoothly transition the torque command to 0 as the engine speed approaches the speed
limit, the block implements a lookup table multiplier. The lookup table multiplies the
torque command by a value that ranges from 0 (engine speed exceeds limit) to 1 (engine speed
does not exceed the limit).

### Estimator

Using the CI Core Engine block, the CI
Controller block estimates the air mass flow rate, EGR valve
mass flow, exhaust back-pressure, engine torque, AFR, and exhaust
temperature from sensor feedback. The `Info` port
provides the estimated values, but block does not use them to determine
the open-loop engine actuator commands.

**Air Mass Flow**

To calculate the air mass flow, the compression-ignition (CI)
engine uses the CI Engine Speed-Density Air Mass Flow Model. The speed-density
model uses the speed-density equation to calculate the engine air
mass flow, relating the engine intake port mass flow to the intake
manifold pressure, intake manifold temperature, and engine speed.

**EGR Valve Mass Flow**

To calculate the estimated exhaust gas recirculation (EGR) valve mass flow, the block
calculates the EGR flow that would occur at standard temperature and pressure
conditions, and then corrects the flow to actual temperature and pressure
conditions. The block EGR calculation uses estimated exhaust back-pressure,
estimated exhaust temperature, standard temperature, and standard pressure.

m˙egr,est=m˙egr,stdPexh,estPstdTstdTexh,est

- The standard exhaust gas recirculation (EGR)
  mass flow is a lookup table that is a function of the standard flow
  pressure ratio and EGR valve flow area

  m˙egr,std=f(MAPPexh,est,EGRap)

  where:

  - m˙egr,std is
    the standard EGR valve mass flow, in g/s.
  - *Pexh,est* is
    the estimated exhaust back-pressure, in Pa.
  - *MAP* is the cycle average intake
    manifold absolute pressure, in Pa.
  - *EGRap* is the measured EGR valve
    area, in percent.

  3D plot of standard EGR valve mass flow versus cycle average intake manifold absolute pressure and measured EGR valve area

The equations use these variables.

|  |  |
| --- | --- |
| m˙egr,est | Estimated EGR valve mass flow |
| m˙egr,std | Standard EGR valve mass flow |
| Pstd | Standard pressure |
| Tstd | Standard temperature |
| *Texh,est* | Estimated exhaust manifold gas temperature |
| *MAP* | Measured cycle average intake manifold absolute pressure |
| *Pexh,est* | Estimated exhaust back-pressure |
| PAmb | Absolute ambient pressure |
| *EGRap* | Measured EGR valve area percent |

**Exhaust Back-Pressure**

To estimate the EGR valve mass flow, the block requires an estimate
of the exhaust back-pressure. To estimate the exhaust back-pressure,
the block uses the ambient pressure and the turbocharger pressure
ratio.

Pexh,est=PAmbPrturbo

For the turbocharger pressure ration calculation, the block
uses two lookup tables. The first lookup table determines the approximate
turbocharger pressure ratio as a function of turbocharger mass flow
and corrected turbocharger speed. Using a second lookup table, the
block corrects the approximate turbocharger pressure ratio for VGT
rack position.

Prturbo=f(m˙airstd,Nvgtcorr)f(VGTpos)where:Nvgtcorr=NvgtTexh,est

The equations use these variables.

|  |  |
| --- | --- |
| m˙egr,est | Estimated EGR valve mass flow |
| m˙egr,std | Standard EGR valve mass flow |
| m˙port,est | Estimated intake port mass flow rate |
| m˙airstd | Standard air mass flow |
| *EGRap* | Measured EGR valve area |
| *MAP* | Measured cycle average intake manifold absolute pressure |
| *MAT* | Measured cycle average intake manifold gas absolute temperature |
| Pstd | Standard pressure |
| Tstd | Standard temperature |
| *Texh,est* | Estimated exhaust manifold gas temperature |
| *Prvgtcorr* | Turbocharger pressure ratio correction for VGT rack position |
| *Prturbo* | Turbocharger pressure ratio |
| *Pexh,est* | Estimated exhaust back-pressure |
| PAmb | Absolute ambient pressure |
| *Nvgtcorr* | Corrected turbocharger speed |
| *VGTpos* | Measured VGT rack position |

The exhaust-back pressure calculation uses these lookup tables:

- The turbocharger pressure ratio, corrected
  for variable geometry turbocharger (VGT) speed, is a lookup table
  that is a function of the standard air mass flow and corrected turbocharger
  speed, Prturbo=f(m˙airstd,Nvgtcorr),
  where:

  - *Prturbo* is
    the turbocharger pressure ratio, corrected for VGT speed.
  - m˙airstd is
    the standard air mass flow, in g/s.
  - *Nvgtcorr* is
    the corrected turbocharger speed, in rpm/K^(1/2).

  3D plot of s turbocharger pressure ratio versus standard air mass flow and corrected turbocharger speed

  To calculate the standard air mass flow through the turbocharger,
  the block uses conservation of mass, the estimated intake port, and
  EGR mass flows (from the last estimated calculation). The calculation
  assumes negligible exhaust manifold filling dynamics.

  m˙airstd=(m˙port,est−m˙egr,est)PstdMAPMATTstd
- The variable geometry turbocharger pressure
  ratio correction is a function of the rack position, *Prvgtcorr*=
  ƒ(*VGTpos*), where:

  - *Prvgtcorr* is
    the turbocharger pressure ratio correction.
  - *VGTpos* is
    the variable geometry turbocharger (VGT) rack position.

  Plot of turbocharger pressure ratio correction versus variable geometry turbocharger (VGT) rack position

**Engine Torque**

To calculate the engine torque, you can configure the block to
use either of these torque models.

| Brake Torque Model | Description |
| --- | --- |
| CI Engine Torque Structure Model | The CI core engine torque structure model determines the engine torque by reducing the maximum engine torque potential as these engine conditions vary from nominal:  - Start of injection (SOI) timing - Exhaust back-pressure - Burned fuel mass - Intake manifold gas pressure, temperature, and oxygen percentage - Fuel rail pressure  To account for the effect of post-inject fuel on torque, the model uses a calibrated torque offset table. |
| CI Engine Simple Torque Model | For the simple engine torque calculation, the CI engine uses a torque lookup table map that is a function of engine speed and injected fuel mass. |

**Exhaust Temperature**

The exhaust temperature calculation depends on the torque model. For both torque models, the block implements lookup tables.

| Torque Model | Description | Equations |
| --- | --- | --- |
| `Simple Torque Lookup` | Exhaust temperature lookup table is a function of the injected fuel mass and engine speed. | Texh=fTexh(F,N) |
| `Torque Structure` | The nominal exhaust temperature, *Texhnom*, is a product of these exhaust temperature efficiencies:  - SOI timing - Intake manifold gas pressure - Intake manifold gas temperature - Intake manifold gas oxygen percentage - Fuel rail pressure - Optimal temperature  The exhaust temperature, *Texhnom*, is offset by a post temperature effect, *ΔTpost*, that accounts for post and late injections during the expansion and exhaust strokes. | Texhnom=SOIexhteffMAPexhteffMATexhteffO2pexhteffFUELPexhteffTexhoptTexh=Texhnom+ΔTpostSOIexhteff=fSOIexhteff(ΔSOI,N)MAPexhteff=fMAPexhteff(MAPratio,λ)MATexhteff=fMATexhteff(ΔMAT,N)O2pexhteff=fO2pexhteff(ΔO2p,N)Texhopt=fTexh(F,N) |

The equations use these variables.

|  |  |
| --- | --- |
| *F* | Compression stroke injected fuel mass |
| *N* | Engine speed |
| *Texh* | Exhaust manifold gas temperature |
| *Texhopt* | Optimal exhaust manifold gas temperature |
| *ΔTpost* | Post injection temperature effect |
| *Texhnom* | Nominal exhaust temperature |
| *SOIexhteff* | Main SOI exhaust temperature efficiency multiplier |
| *ΔSOI* | Main SOI timing relative to optimal timing |
| *MAPexheff* | Intake manifold gas pressure exhaust temperature efficiency multiplier |
| *MAPratio* | Intake manifold gas pressure ratio relative to optimal pressure ratio |
| *λ* | Intake manifold gas lambda |
| *MATexheff* | Intake manifold gas temperature exhaust temperature efficiency multiplier |
| *ΔMAT* | Intake manifold gas temperature relative to optimal temperature |
| *O2Pexheff* | Intake manifold gas oxygen exhaust temperature efficiency multiplier |
| *ΔO2P* | Intake gas oxygen percent relative to optimal |
| *FUELPexheff* | Fuel rail pressure exhaust temperature efficiency multiplier |
| *ΔFUELP* | Fuel rail pressure relative to optimal |

**Air-Fuel Ratio**

The measured engine speed and fuel injector pulse-width determine
the commanded fuel mass flow rate:

m˙fuel,cmd=NSinjPwinjNcylCps(60smin)(1000mgg)

The commanded total fuel mass flow and estimated port mass flow
rates determine the estimated AFR:

AFRest=m˙port,estm˙fuel,cmd

The equations use these variables.

|  |  |
| --- | --- |
| Pwinj | Fuel injector pulse-width |
| *AFRest* | Estimated air-fuel ratio |
| m˙fuel,cmd | Commanded fuel mass flow rate |
| Sinj | Fuel injector slope |
| *N* | Engine speed |
| *Ncyl* | Number of engine cylinders |
| *Cps* | Crankshaft revolutions per power stroke, rev/stroke |
| m˙port,est | Total estimated engine air mass flow at intake ports |
