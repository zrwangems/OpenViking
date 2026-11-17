---
type: simulink-block
title: 'CI Core Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Core Engine'
documentation_page: 'cicoreengine'
documentation_source_path: 'ref/cicoreengine.html'
language: en
---

# CI Core Engine

## Ports
```yaml
ports:
- name: FuelMass
  summary: Fuel injector pulse-width vector
  direction: input
- name: Soi
  summary: Start of fuel injection timing vector
  direction: input
- name: EngSpd
  summary: Engine speed scalar
  direction: input
- name: FuelPrs
  summary: Fuel rail pressure scalar
  direction: input
- name: Ect
  summary: Engine cooling temperature scalar
  direction: input
- name: Intk
  summary: Intake port pressure, temperature, enthalpy, mass fractions two-way connector port
  direction: input
- name: Exh
  summary: Exhaust port pressure, temperature, enthalpy, mass fractions two-way connector port
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: EngTrq
  summary: Engine brake torque scalar
  direction: output
- name: Intk
  summary: Intake port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port
  direction: output
- name: Exh
  summary: Exhaust port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port
  direction: output
```

### Input

### **FuelMass** — Fuel injector pulse-width `vector`

Fuel mass per injection,
*mfuel,inj*, in
mg per injection.

### **Soi** — Start of fuel injection timing `vector`

Fuel injection timing, *SOI*, in degrees crank angle
after top dead center (degATDC). First vector value,
`Soi(1)`, is main injection timing.

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

### **EngSpd** — Engine speed `scalar`

Engine speed, *N*, in rpm.

### **FuelPrs** — Fuel rail pressure `scalar`

Fuel rail pressure, *FUELP*, in MPa.

#### Dependencies

To enable this parameter, for **Torque model**, select
`Torque Structure`.

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
- `MassFrac` —
  Intake port mass fractions, dimensionless. Exhaust gas recirculation
  (EGR) mass flow at the intake port is burned gas.

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

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `IntkGasMassFlw` | | | Engine intake air mass flow. | m˙air | kg/s |
| `IntkAirMassFlw` | | | Engine intake port mass flow. | m˙intk | kg/s |
| `NrmlzdAirChrg` | | | Engine load (that is, normalized cylinder air mass) corrected for final steady-state cam phase angles | L | N/A |
| `Afr` | | | Air-fuel ratio at engine exhaust port | AFR | N/A |
| `FuelMassFlw` | | | Fuel flow into engine | m˙fuel | kg/s |
| `FuelVolFlw` | | | Volumetric fuel flow | *Qfuel* | m3/s |
| `ExhManGasTemp` | | | Exhaust gas temperature at exhaust manifold inlet | Texh | K |
| `EngTrq` | | | Engine brake torque | Tbrake | N·m |
| `EngSpd` | | | Engine speed | N | rpm |
| `IntkCamPhase` | | | Intake cam phaser angle | φICP i | degrees crank advance |
| `ExhCamPhase` | | | Exhaust cam phaser angle | φECP | degrees crank retard |
| `CrkAng` | | | Engine crankshaft absolute angle | ∫0(360)CpsEngSpd18030dθ  where Cps is crankshaft revolutions per power stroke | degrees crank angle |
| `EgrPct` | | | EGR percent | *EGRpct* | N/A |
| `EoAir` | | | EO air mass flow rate | m˙exh | kg/s |
| `EoBrndGas` | | | EO burned gas mass flow rate | *yexh,b* | kg/s |
| `EoHC` | | | EO hydrocarbon emission mass flow rate | *yexh,HC* | kg/s |
| `EoCO` | | | EO carbon monoxide emission mass flow rate | *yexh,CO* | kg/s |
| `EoNOx` | | | EO nitric oxide and nitrogen dioxide emissions mass flow rate | *yexh,NOx* | kg/s |
| `EoCO2` | | | EO carbon dioxide emission mass flow rate | *yexh,CO2* | kg/s |
| `EoPm` | | | EO particulate matter emission mass flow rate | *yexh,PM* | kg/s |
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
- `ExhManGasTemp` — Intake port
  temperature, in K
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
- `ExhManGasTemp` — Exhaust
  port temperature, in K
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
```yaml
parameters:
- name: Torque model
  summary: Select torque model Torque Structure (default) | Simple Torque Lookup
  group: Block Options
  block_parameter: TrqOptionPopup
  values: Torque Structure (default) | Simple Torque Lookup
- name: Number of cylinders, NCyl
  summary: Engine cylinders 4 (default) | scalar
  group: Air
  block_parameter: NCyl
  values: 4 (default) | scalar
- name: Air standard temperature, Pstd
  summary: Temperature 293.15 (default) | scalar
  group: Air
  block_parameter: Pstd
  values: 293.15 (default) | scalar
- name: Crank revolutions per power stroke, Cps
  summary: Revolutions per stroke 2 (default) | scalar
  group: Air
  block_parameter: Cps
  values: 2 (default) | scalar
- name: Total displaced volume, Vd
  summary: Volume 0.0015 (default) | scalar
  group: Air
  block_parameter: Vd
  values: 0.0015 (default) | scalar
- name: Ideal gas constant air, Rair
  summary: Constant 287.05 (default) | scalar
  group: Air
  block_parameter: Rair
  values: 287.05 (default) | scalar
- name: Air standard pressure, Pstd
  summary: Pressure 101325 (default) | scalar
  group: Air
  block_parameter: Pstd
  values: 101325 (default) | scalar
- name: Speed-density volumetric efficiency, f_nv
  summary: Lookup table array
  group: Air
  block_parameter: f_nv
  values: array
- name: Speed-density intake manifold pressure breakpoints, f_nv_prs_bpt
  summary: Breakpoints vector
  group: Air
  block_parameter: f_nv_prs_bpt
  values: vector
- name: Speed-density engine speed breakpoints, f_nv_n_bpt
  summary: Breakpoints vector
  group: Air
  block_parameter: f_nv_n_bpt
  values: vector
- name: Torque table, f_tq_nf
  summary: Lookup table array
  group: Torque
  block_parameter: f_tq_nf
  values: array
- name: Torque table fuel mass per injection breakpoints, f_tq_nf_f_bpt
  summary: Breakpoints [0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286
    50] (default) | vector
  group: Torque
  block_parameter: f_tq_nf_f_bpt
  values: array
- name: Torque table speed breakpoints, f_tq_nf_n_bpt
  summary: Breakpoints [1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429
    5517.8571 5928.5714 6339.2857 6750] (default) | vector
  group: Torque
  block_parameter: f_tq_nf_n_bpt
  values: vector
- name: Fuel mass per injection breakpoints, f_tqs_f_bpt
  summary: Breakpoints vector
  group: Torque
  block_parameter: f_tqs_f_bpt
  values: vector
- name: Engine speed breakpoints, f_tqs_n_bpt
  summary: Breakpoints [500 750 1000 1250 1500 1750 2000 2250 2500 2750 3000 3250 3500 3750 4000] (default) | vector
  group: Torque
  block_parameter: f_tqs_n_bpt
  values: vector
- name: Optimal main start of injection timing, f_tqs_mainsoi
  summary: Optimal MAINSOI array
  group: Torque
  block_parameter: f_tqs_mainsoi
  values: array
- name: Optimal intake manifold gas pressure, f_tqs_map
  summary: Optimal intake MAP array
  group: Torque
  block_parameter: f_tqs_map
  values: array
- name: Optimal exhaust manifold gas pressure, f_tqs_emap
  summary: Optimal exhaust MAP array
  group: Torque
  block_parameter: f_tqs_emap
  values: array
- name: Optimal intake manifold gas temperature, f_tqs_mat
  summary: Optimal intake MAT array
  group: Torque
  block_parameter: f_tqs_mat
  values: array
- name: Optimal intake gas oxygen percent, f_tqs_o2pct
  summary: Optimal intake gas oxygen array
  group: Torque
  block_parameter: f_tqs_o2pct
  values: array
- name: Optimal fuel rail pressure, f_tqs_fuelpress
  summary: Optimal fuel rail pressure array
  group: Torque
  block_parameter: f_tqs_fuelpress
  values: array
- name: Optimal gross indicated mean effective pressure, f_tqs_imepg
  summary: Optimal mean effective pressure array
  group: Torque
  block_parameter: f_tqs_imepg
  values: array
- name: Optimal friction mean effective pressure, f_tqs_fmep
  summary: Optimal friction mean effective pressure array
  group: Torque
  block_parameter: f_tqs_fmep
  values: array
- name: Optimal pumping mean effective pressure, f_tqs_pmep
  summary: Optimal pumping mean effective pressure array
  group: Torque
  block_parameter: f_tqs_pmep
  values: array
- name: Friction multiplier as a function of temperature, f_tqs_fric_temp_mod
  summary: Friction multiplier array
  group: Torque
  block_parameter: f_tqs_fric_temp_mod
  values: array
- name: Friction multiplier temperature breakpoints, f_tqs_fric_temp_bpt
  summary: Breakpoints vector
  group: Torque
  block_parameter: f_tqs_fric_temp_bpt
  values: vector
- name: Main start of injection timing efficiency multiplier, f_tqs_mainsoi_eff
  summary: MAINSOI efficiency multiplier array
  group: Torque
  block_parameter: f_tqs_mainsoi_eff
  values: array
- name: Main start of injection timing relative to optimal timing breakpoints, f_tqs_mainsoi_delta_bpt
  summary: Breakpoints vector
  group: Torque
  block_parameter: f_tqs_mainsoi_delta_bpt
  values: vector
- name: Intake manifold gas pressure efficiency multiplier, f_tqs_map_eff
  summary: Intake pressure efficiency multiplier array
  group: Torque
  block_parameter: f_tqs_map_eff
  values: array
- name: Intake manifold gas pressure ratio relative to optimal pressure ratio breakpoints, f_tqs_map_ratio_bpt
  summary: Breakpoints [0.8;0.85;0.9;0.95;1;1.05;1.1;1.15;1.2;1.25;1.3;1.35;1.4;1.45;1.5] (default) | vector
  group: Torque
  block_parameter: f_tqs_map_ratio_bpt
  values: vector
- name: Intake manifold gas lambda breakpoints, f_tqs_lambda_bpt
  summary: Breakpoints [1.5 1.678571428571429 1.857142857142857 2.035714285714286 2.214285714285714 2.392857142857143 2.571428571428571
    2.75 2.928571428571429 3.107142857142857 3.285714285714286 3.464285714285714 3.642857142857143 3.821428571428572 4] (default)
    | vector
  group: Torque
  block_parameter: f_tqs_lambda_bpt
  values: vector
- name: Intake manifold gas temperature efficiency multiplier, f_tqs_mat_eff
  summary: Intake temperature efficiency multiplier array
  group: Torque
  block_parameter: f_tqs_mat_eff
  values: array
- name: Intake manifold gas temperature relative to optimal gas temperature breakpoints, f_tqs_mat_delta_bpt
  summary: Breakpoints [-55;-50;-45;-40;-35;-30;-25;-20;-15;-10;-5;0;5;10;15] (default) | vector
  group: Torque
  block_parameter: f_tqs_mat_delta_bpt
  values: vector
- name: Intake manifold gas oxygen efficiency multiplier, f_tqs_o2pct_eff
  summary: Intake oxygen efficiency multiplier array
  group: Torque
  block_parameter: f_tqs_o2pct_eff
  values: array
- name: Intake gas oxygen percent relative to optimal breakpoints, f_tqs_o2pct_delta_bpt
  summary: Breakpoints vector
  group: Torque
  block_parameter: f_tqs_o2pct_delta_bpt
  values: vector
- name: Fuel rail pressure efficiency multiplier, f_tqs_fuelpress_eff
  summary: Efficiency multiplier array
  group: Torque
  block_parameter: f_tqs_fuelpress_eff
  values: array
- name: Fuel rail pressure relative to optimal breakpoints, f_tqs_fuelpress_delta_bpt
  summary: Breakpoints vector
  group: Torque
  block_parameter: f_tqs_fuelpress_delta_bpt
  values: vector
- name: Fuel mass injection type identifier, f_tqs_f_inj_type
  summary: Type identifier 0 (default) | scalar
  group: Torque
  block_parameter: f_tqs_f_inj_type
  values: 0 (default) | scalar
- name: Indicated mean effective pressure post inject correction, f_tqs_imep_post_corr
  summary: Post inject correction array
  group: Torque
  block_parameter: f_tqs_imep_post_corr
  values: array
- name: Indicated mean effective pressure post inject mass sum breakpoints, f_tqs_f_post_sum_bpt
  summary: Breakpoints [0 3.571428571428572 7.142857142857143 10.71428571428571 14.28571428571429 17.85714285714286 21.42857142857143
    25 28.57142857142857 32.14285714285715 35.71428571428572 39.28571428571428 42.85714285714285 46.42857142857143 50] (default)
    | vector
  group: Torque
  block_parameter: f_tqs_f_post_sum_bpt
  values: vector
- name: Indicated mean effective pressure post inject start of inject timing centroid breakpoints, f_tqs_soi_post_cent_bpt
  summary: Breakpoints [150 160.7142857142857 171.4285714285714 182.1428571428571 192.8571428571429 203.5714285714286 214.2857142857143
    225 235.7142857142857 246.4285714285714 257.1428571428571 267.8571428571429 278.5714285714286 289.2857142857143 300] (default)
    | vector
  group: Torque
  block_parameter: f_tqs_soi_post_cent_bpt
  values: vector
- name: Maximum start of injection angle for burned fuel, f_tqs_f_burned_soi_limit
  summary: Maximum SOI angle for burned fuel 500 (default) | scalar
  group: Torque
  block_parameter: f_tqs_f_bpt
  values: 500 (default) | scalar
- name: Exhaust temperature table, f_t_exh
  summary: Lookup table array
  group: Exhaust
  block_parameter: f_t_exh
  values: array
- name: Fuel mass per injection breakpoints, f_t_exh_f_bpt
  summary: Breakpoints [0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286
    50] (default) | vector
  group: Exhaust
  block_parameter: f_t_exh_f_bpt
  values: vector
- name: Speed breakpoints, f_t_exh_n_bpt
  summary: Breakpoints [1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429
    5517.8571 5928.5714 6339.2857 6750] (default) | vector
  group: Exhaust
  block_parameter: f_t_exh_n_bpt
  values: vector
- name: Optimal exhaust manifold gas temperature, f_tqs_exht
  summary: Optimal exhaust manifold gas temperature array
  group: Exhaust
  block_parameter: f_tqs_exht
  values: array
- name: Main start of injection timing exhaust temperature efficiency multiplier, f_tqs_exht_mainsoi_eff
  summary: Main SOI timing efficiency multiplier array
  group: Exhaust
  block_parameter: f_tqs_exht_mainsoi_eff
  values: array
- name: Intake manifold gas pressure exhaust temperature efficiency multiplier, f_tqs_exht_map_eff
  summary: Intake manifold efficiency multiplier array
  group: Exhaust
  block_parameter: f_tqs_exht_map_eff
  values: array
- name: Intake manifold gas temperature exhaust temperature efficiency multiplier, f_tqs_exht_mat_eff
  summary: Intake manifold efficiency multiplier array
  group: Exhaust
  block_parameter: f_tqs_exht_mat_eff
  values: array
- name: Intake manifold gas oxygen exhaust temperature efficiency multiplier, f_tqs_exht_o2pct_eff
  summary: Intake manifold efficiency multiplier array
  group: Exhaust
  block_parameter: f_tqs_exht_o2pct_eff
  values: array
- name: Fuel rail pressure exhaust temperature efficiency multiplier, f_tqs_exht_fuelpress_eff
  summary: Fuel rail pressure exhaust temperature efficiency multiplier array
  group: Exhaust
  block_parameter: f_tqs_exht_fuelpress_eff
  values: array
- name: Post-injection cylinder wall heat loss transfer coefficient, f_tqs_exht_post_inj_wall_htc
  summary: Post-injection offset 0 (default) | scalar
  group: Exhaust
  block_parameter: f_tqs_exht_post_inj_wall_htc
  values: 0 (default) | scalar
- name: CO2 mass fraction table, f_CO2_frac
  summary: Carbon dioxide (CO2) emission lookup table array
  group: Exhaust
  block_parameter: f_CO2_frac
  values: array
- name: CO mass fraction table, f_CO_frac
  summary: Carbon monoxide (CO) emission lookup table array
  group: Exhaust
  block_parameter: f_CO_frac
  values: array
- name: HC mass fraction table, f_HC_frac
  summary: Hydrocarbon (HC) emission lookup table array
  group: Exhaust
  block_parameter: f_HC_frac
  values: array
- name: NOx mass fraction table, f_NOx_frac
  summary: Nitric oxide and nitrogen dioxide (NOx) emission lookup table array
  group: Exhaust
  block_parameter: f_NOx_frac
  values: array
- name: PM mass fraction table, f_PM_frac
  summary: Particulate matter (PM) emission lookup table array
  group: Exhaust
  block_parameter: f_PM_frac
  values: array
- name: Engine speed breakpoints, f_exhfrac_n_bpt
  summary: Breakpoints [750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857
    2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000] (default)
    | vector
  group: Exhaust
  block_parameter: f_exhfrac_n_bpt
  values: vector
- name: Engine torque breakpoints, f_exhfrac_trq_bpt
  summary: Breakpoints [0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286
    95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175] (default)
    | vector
  group: Exhaust
  block_parameter: f_exhfrac_trq_bpt
  values: vector
- name: Exhaust gas specific heat at constant pressure, cp_exh
  summary: Specific heat 1005 (default) | scalar
  group: Exhaust
  block_parameter: cp_exh
  values: 1005 (default) | scalar
- name: Stoichiometric air-fuel ratio, afr_stoich
  summary: Air-fuel ratio 14.6 (default) | scalar
  group: Fuel
  block_parameter: afr_stoich
  values: 14.6 (default) | scalar
- name: Fuel lower heating value, fuel_lhv
  summary: Heating value 42e6 (default) | scalar
  group: Fuel
  block_parameter: fuel_lhv
  values: 42e6 (default) | scalar
- name: Fuel specific gravity, fuel_sg
  summary: Specific gravity 0.832 (default) | scalar
  group: Fuel
  block_parameter: fuel_sg
  values: 0.832 (default) | scalar
```

### Block Options

### **Torque model** — Select torque model `Torque Structure` (default) | `Simple Torque Lookup`

To calculate the engine torque, you can configure the block to
use either of these torque models.

| Brake Torque Model | Description |
| --- | --- |
| CI Engine Torque Structure Model | The CI core engine torque structure model determines the engine torque by reducing the maximum engine torque potential as these engine conditions vary from nominal:  - Start of injection (SOI) timing - Exhaust back-pressure - Burned fuel mass - Intake manifold gas pressure, temperature, and oxygen percentage - Fuel rail pressure  To account for the effect of post-inject fuel on torque, the model uses a calibrated torque offset table. |
| CI Engine Simple Torque Model | For the simple engine torque calculation, the CI engine uses a torque lookup table map that is a function of engine speed and injected fuel mass. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrqOptionPopup` |
| **Values:** | `Torque Structure` (default) | `Simple Torque Lookup` |
| **Data Types:** | `character vector` |

### Air

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

### **Air standard temperature, Pstd** — Temperature `293.15` (default) | `scalar`

Standard air temperature,
*Tstd*, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Pstd` |
| **Values:** | `293.15` (default) | `scalar` |
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

### **Ideal gas constant air, Rair** — Constant `287.05` (default) | `scalar`

Ideal gas constant, Rair, in J/(kg·K).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rair` |
| **Values:** | `287.05` (default) | `scalar` |
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

### **Speed-density volumetric efficiency, f\_nv** — Lookup table `array`

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

### **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — Breakpoints `vector`

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

### **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** — Breakpoints `vector`

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

### Torque

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

### Exhaust

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

#### Emissions

### **CO2 mass fraction table, f\_CO2\_frac** — Carbon dioxide (CO2) emission lookup table `array`

The CI Core Engine CO2 emission
mass fraction lookup table is a function of engine torque and engine
speed, *CO2 Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *CO2 Mass Fraction* is the CO2 emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of CO2 emission mass fraction versus engine speed and engine torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_CO2_frac` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**CO2**.

### **CO mass fraction table, f\_CO\_frac** — Carbon monoxide (CO) emission lookup table `array`

The CI Core Engine CO emission
mass fraction lookup table is a function of engine torque and engine
speed, *CO Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *CO Mass Fraction* is the CO emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of CO emission mass fraction versus engine speed and engine torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_CO_frac` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**CO**.

### **HC mass fraction table, f\_HC\_frac** — Hydrocarbon (HC) emission lookup table `array`

The CI Core Engine HC emission
mass fraction lookup table is a function of engine torque and engine
speed, *HC Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *HC Mass Fraction* is the HC emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of HC emission mass fraction versus engine speed and engine torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_HC_frac` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**HC**.

### **NOx mass fraction table, f\_NOx\_frac** — Nitric oxide and nitrogen dioxide (NOx) emission lookup table `array`

The CI Core Engine NOx
emission mass fraction lookup table is a function of engine torque
and engine speed, *NOx Mass Fraction* = ƒ(*Speed*, *Torque*),
where:

- *NOx Mass Fraction* is the NOx emission
  mass fraction, dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

3D plot of NOx emission mass fraction versus engine speed and engine torque

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_NOx_frac` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**NOx**.

### **PM mass fraction table, f\_PM\_frac** — Particulate matter (PM) emission lookup table `array`

The CI Core Engine PM emission mass fraction
lookup table is a function of engine torque and engine speed where:

- *PM* is the PM emission mass fraction,
  dimensionless.
- *Speed* is engine speed, in rpm.
- *Torque* is engine torque, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_PM_frac` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**PM**.

### **Engine speed breakpoints, f\_exhfrac\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector`

Engine speed breakpoints used for the emission mass fractions lookup tables, in
rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_exhfrac_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**CO2**, **CO**, **NOx**,
**HC**, or **PM**.

### **Engine torque breakpoints, f\_exhfrac\_trq\_bpt** — Breakpoints `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]` (default) | `vector`

Engine torque breakpoints used for the emission mass fractions lookup tables, in
N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_exhfrac_trq_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, on the **Exhaust** tab, select
**CO2**, **CO**, **NOx**,
**HC**, or **PM**.

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

### Fuel

### **Stoichiometric air-fuel ratio, afr\_stoich** — Air-fuel ratio `14.6` (default) | `scalar`

Air-fuel ratio, AFR.

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

### **Fuel lower heating value, fuel\_lhv** — Heating value `42e6` (default) | `scalar`

Fuel lower heating value, *LHV*, in J/kg.

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

### **Fuel specific gravity, fuel\_sg** — Specific gravity `0.832` (default) | `scalar`

Specific gravity of fuel,
*Sgfuel*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `fuel_sg` |
| **Values:** | `0.832` (default) | `scalar` |
| **Data Types:** | `double` |
## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Compression-ignition engine from intake to exhaust port

The CI Core Engine block implements a compression-ignition
(CI) engine from intake to the exhaust port. You can use the block
for hardware-in-the-loop (HIL) engine control design or vehicle-level
fuel economy and performance simulations.

The CI Core Engine block calculates:

- Brake torque
- Exhaust temperature
- Air-fuel ratio (AFR)
- Fuel rail pressure
- Engine-out (EO) exhaust emissions:

  - Hydrocarbon (HC)
  - Carbon monoxide (CO)
  - Nitric oxide and nitrogen dioxide (NOx)
  - Carbon dioxide (CO2)
  - Particulate matter (PM)

### Air Mass Flow

To calculate the air mass flow, the compression-ignition (CI)
engine uses the CI Engine Speed-Density Air Mass Flow Model. The speed-density
model uses the speed-density equation to calculate the engine air
mass flow, relating the engine intake port mass flow to the intake
manifold pressure, intake manifold temperature, and engine speed.

### Brake Torque

To calculate the engine torque, you can configure the block to
use either of these torque models.

| Brake Torque Model | Description |
| --- | --- |
| CI Engine Torque Structure Model | The CI core engine torque structure model determines the engine torque by reducing the maximum engine torque potential as these engine conditions vary from nominal:  - Start of injection (SOI) timing - Exhaust back-pressure - Burned fuel mass - Intake manifold gas pressure, temperature, and oxygen percentage - Fuel rail pressure  To account for the effect of post-inject fuel on torque, the model uses a calibrated torque offset table. |
| CI Engine Simple Torque Model | For the simple engine torque calculation, the CI engine uses a torque lookup table map that is a function of engine speed and injected fuel mass. |

### Fuel Flow

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

To calculate the engine
fuel mass flow, the CI Core Engine block uses fuel mass flow delivered by the
injectors and the engine airflow.

m˙fuel=N⋅NcylCps(60smin)(1000mgg)∑mfuel,inj

To calculate the fuel economy for high-fidelity models, the block uses the
volumetric fuel flow.

Qfuel=m˙fuel(1000kgm3)Sgfuel

The equation uses these variables.

|  |  |
| --- | --- |
| m˙fuel | Fuel mass flow, g/s |
| *mfuel,inj* | Fuel mass per injection |
| Cps | Crankshaft revolutions per power stroke, rev/stroke |
| Ncyl | Number of engine cylinders |
| *N* | Engine speed, rpm |
| *Qfuel* | Volumetric fuel flow |
| *Sgfuel* | Specific gravity of fuel |

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

### Exhaust Temperature

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

### EO Exhaust Emissions

The block calculates these engine-out (EO) exhaust emissions:

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
