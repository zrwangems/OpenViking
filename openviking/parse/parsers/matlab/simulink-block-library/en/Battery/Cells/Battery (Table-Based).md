---
type: simulink-block
title: 'Battery (Table-Based)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cells'
documentation_page: 'batterytablebased'
documentation_source_path: 'ref/batterytablebased.html'
language: en
---

# Battery (Table-Based)

## Ports

### Output

### **SOC** — Battery charge level, C physical signal

Physical signal port that outputs the internal state of charge. Use this output port to change load behavior as a function of state of charge, without the complexity of building a charge state estimator. The state of charge is the normalized value estimated from the ratio of current charge with the nominal battery capacity, *qnom(T,n)*. The block estimates the current battery charge by integrating the battery terminal output current. To convert the state of charge into actual charge, you must use the correct nominal battery capacity for each temperature.

#### Dependencies

To enable this port, in the **Main** setting, set the **Expose SOC measurement port** parameter to `Yes`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the battery positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the battery negative terminal.

### **H** — Battery thermal mass thermal

Thermal conserving port that represents the battery thermal mass.

#### Dependencies

To enable this port, in the **Thermal** setting, set the **Thermal port** parameter to `Yes`.

## Parameters

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations (Simscape Electrical).

### Main

### **Vector of state-of-charge values, SOC** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of scalars in the range [0,1]

Vector of state-of-charge breakpoints defining the points at which you specify lookup data. This vector must be strictly ascending. The state-of-charge value is calculated with respect to the nominal battery capacity specified in the **Cell capacity, AH** parameter. `SOC` is the ratio of the available battery charge, *qbattery* and the nominal battery capacity, *qnom(T,n)*. You must make sure that, for each temperature, `SOC = 1` represents the respective battery charge capacity specified in the **Cell capacity, AH** parameter, assuming a fresh battery with a number of cycles, *N*, equal to 1 and *δAH(n = 1, Tfade) = 0*.

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH

### **Tabulate parameters over temperature** — Select whether to tabulate battery parameters over temperature `Yes` (default) | `No`

Select whether to tabulate battery parameters over temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_dependence` |
| **Values:** | `"yes"` (default) | `"no"` |

### **Current directionality** — Enable direction of current `Disabled` (default) | `Enabled`

Whether to enable current directionality. If you set this parameter to `Enabled`, the terminal resistance depends on the direction of the current.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_dir` |
| **Values:** | `"currentDirectionality"` (default) | `"noCurrentDirectionality"` |

### **Terminal voltage operating range [Min Max]** — Terminal voltage operating range `[0, inf]` `V` (default) | vector of positive numbers

Operating range of the terminal voltage. This parameter must be a vector of size `1`-by-`2` that defines the minimum and maximum values of the terminal voltage.

### **Vector of temperatures, T** — *T* breakpoints `[278, 293, 313]` `K` (default) | vector of positive numbers

Vector of temperature breakpoints defining the points at which you specify lookup data. This vector must be strictly ascending and greater than `0` `K`.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`Yes`.

### **Open-circuit voltage, V0(SOC,T)** — *V0* lookup table with temperature breakpoint `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` `V` (default) | matrix of nonnegative numbers

Lookup data for open-circuit voltages across the fundamental battery model at the specified SOC and temperature breakpoints.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`Yes`.

### **Open-circuit voltage, V0(SOC)** — *V0* lookup table `[3.5057, 3.566, 3.6337, 3.7127, 3.9259, 4.0777, 4.1928]` `V` (default) | matrix of nonnegative numbers

Lookup data for open-circuit voltages across the fundamental battery model at the specified SOC.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`No`.

### **Terminal resistance, R0(SOC,T)** — R0 lookup table with temperature breakpoint `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative numbers

Lookup data for series resistance of the battery at the specified SOC and temperature breakpoints.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`Yes` and the **Current
directionality** parameter is set to
`Disabled`.

### **Terminal resistance during discharging, R0(SOC,T)** — R0 lookup table with temperature breakpoint during discharging phase `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative numbers

Lookup data for series resistance of the battery at the specified SOC and temperature breakpoints during the discharging phase.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`Yes` and the **Current
directionality** parameter is set to
`Enabled`.

### **Terminal resistance during charging, R0(SOC,T)** — R0 lookup table with temperature breakpoint during charging phase `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative numbers

Lookup data for series resistance of the battery at the specified SOC and temperature breakpoints during the charging phase.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`Yes` and the **Current
directionality** parameter is set to
`Enabled`.

### **Terminal resistance, R0(SOC)** — R0 lookup table `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm` (default) | matrix of nonnegative numbers

Lookup data for series resistance of the battery at the specified SOC.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`No` and the **Current
directionality** parameter is set to
`Disabled`.

### **Terminal resistance during discharging, R0(SOC)** — R0 lookup table during discharging phase `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm` (default) | matrix of nonnegative numbers

Lookup data for series resistance of the battery at the specified SOC during the discharging phase.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`No` and the **Current
directionality** parameter is set to
`Enabled`.

### **Terminal resistance during charging, R0(SOC)** — R0 lookup table during charging phase `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm` (default) | matrix of nonnegative numbers

Lookup data for series resistance of the battery at the specified SOC during the charging phase.

#### Dependencies

This parameter is visible only when the **Tabulate parameters over
temperature** parameter is set to
`No` and the **Current
directionality** parameter is set to
`Enabled`.

### **Cell capacity, AH** — Battery capacity when fully charged `27` `hr*A` (default) | nonnegative scalar

Cell capacity of the battery. The block calculates the state of charge
by dividing the accumulated charge by this value. The block calculates
accumulated charge by integrating the battery current.

### **Self-discharge** — Select whether to model the self-discharge resistance of the battery `Disabled` (default) | `Enabled`

Select whether to model the self-discharge resistance of the battery. The block models this effect as a resistor across the terminals of the fundamental battery model.

As temperature increases, self-discharge resistance decreases, causing self-discharge to increase. If the decrease in resistance is too fast, thermal runaway of the battery and numerical instability can occur. You can resolve this instability by making any of these changes:

- Decrease the thermal resistance
- Decrease the gradient of the self-discharge resistance with respect to temperature
- Increase the self-discharge resistance

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_leak` |
| **Values:** | `"disabled"` (default) | `"enabled"` |

### **Self-discharge resistance, Rleak(T)** — Resistance that represents battery self-discharge at temperature breakpoints `[8000, 7000, 6000]` `Ohm` (default) | vector of positive numbers

Lookup data for self-discharge resistance of the battery at the specified temperature breakpoints. This resistance acts across the terminals of the fundamental battery model.

#### Dependencies

Enabled when the **Self-discharge** parameter is set to
`Enabled` and **Tabulate
parameters over temperature** is set to
`Yes`.

### **Self-discharge resistance, Rleak** — Resistance that represents battery self-discharge `7e3` `Ohm` (default) | positive scalar

Lookup data for self-discharge resistance of the battery. This resistance acts across the terminals of the fundamental battery model.

#### Dependencies

This parameter is visible only when the **Self-discharge** parameter is set
to `Enabled` and the **Tabulate
parameters over temperature** parameter is set to
`No`.

### **Extrapolation method for all tables** — Method of extrapolation for tables `Nearest` (default) | `Linear` | `Error`

Extrapolation method for all the table based parameters:

- `Linear` — Estimates values beyond the dataset by creating a tangent line at the end of the known data and extending it beyond that limit.
- `Nearest` — Extrapolates a value at query point that is the value at the nearest sample grid point.
- `Error` — Returns an error if the value goes beyond the known dataset. If you select this option, the block does not use extrapolation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `extrapolation_option` |
| **Values:** | `"nearest"` (default) | `"linear"` | `"error"` |

### **Expose SOC measurement port** — Method of extrapolation for tables `No` (default) | `Yes`

Whether to expose the state-of-charge measurement port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOC_port` |
| **Values:** | `"no"` (default) | `"yes"` | `"error"` |

### Dynamics

### **Charge dynamics** — Battery charge dynamics model `No dynamics` (default) | `One time-constant dynamics` | `Two time-constant dynamics` | `Three time-constant dynamics` | `Four time-constant dynamics` | `Five time-constant dynamics`

Select how to model battery charge dynamics. This parameter determines the number of parallel RC sections in the equivalent circuit:

- `No dynamics` — The equivalent circuit contains no parallel RC sections. There is no delay between terminal voltage and internal charging voltage of the battery.
- `One time-constant dynamics` — The equivalent circuit contains one parallel RC section. Specify the time constant using the **First time constant, tau1(SOC,T)** parameter if tabulating parameters over temperature or **First time constant, tau1(SOC)** otherwise.
- `Two time-constant dynamics` — The equivalent circuit contains two parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)** and **Second time constant, tau2(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)** and **Second time constant, tau2(SOC)** otherwise.
- `Three time-constant dynamics` — The equivalent circuit contains three parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)**, **Second time constant, tau2(SOC,T)**, and **Third time constant, tau3(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)**, **Second time constant, tau2(SOC)**, and **Third time constant, tau3(SOC)** otherwise.
- `Four time-constant dynamics` — The equivalent circuit contains four parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)**, **Second time constant, tau2(SOC,T)**, **Third time constant, tau3(SOC,T)**, and **Fourth time constant, tau4(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)**, **Second time constant, tau2(SOC)**, **Third time constant, tau3(SOC)**, and **Fourth time constant, tau4(SOC)** otherwise.
- `Five time-constant dynamics` — The equivalent circuit contains five parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)**, **Second time constant, tau2(SOC,T)**, **Third time constant, tau3(SOC,T)**, **Fourth time constant, tau4(SOC,T)**, and **Fifth time constant, tau5(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)**, **Second time constant, tau2(SOC)**, **Third time constant, tau3(SOC)**, **Fourth time constant, tau4(SOC)**, and **Fifth time constant, tau5(SOC)** otherwise.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_dyn` |
| **Values:** | `"off"` (default) | `"rc1"` | `"rc2"` | `"rc3"` | `"rc4"` | `"rc5"` |

### **First polarization resistance, R1(SOC,T)** — First RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive numbers

Lookup data for the first parallel RC resistance at the specified SOC and temperature breakpoints. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One
time-constant dynamics`, `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **First polarization resistance, R1(SOC)** — First RC resistance `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | matrix of positive numbers

Lookup data for the first parallel RC resistance at the specified SOC. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One
time-constant dynamics`, `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **First time constant, tau1(SOC,T)** — First RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive numbers

Lookup data for the first parallel RC time constant at the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One
time-constant dynamics`, `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **First time constant, tau1(SOC)** — First RC time constant `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | matrix of positive numbers

Lookup data for the first parallel RC time constant at the specified SOC.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One
time-constant dynamics`, `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Second polarization resistance, R2(SOC,T)** — Second RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive numbers

Lookup data for the second parallel RC resistance at the specified SOC and temperature breakpoints. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Second polarization resistance, R2(SOC)** — Second RC resistance `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | matrix of positive numbers

Lookup data for the second parallel RC resistance at the specified SOC. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Second time constant, tau2(SOC,T)** — Second RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive numbers

Lookup data for the second parallel RC time constant at the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Second time constant, tau2(SOC)** — Second RC time constant `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | matrix of positive numbers

Lookup data for the second parallel RC time constant at the specified SOC.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Third polarization resistance, R3(SOC,T)** — Third RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive numbers

Lookup data for the third parallel RC resistance at the specified SOC and temperature
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics`.

### **Third polarization resistance, R3(SOC)** — Third RC resistance `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | matrix of positive numbers

Lookup data for the third parallel RC resistance at the specified SOC. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Third time constant, tau3(SOC,T)** — Third RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive numbers

Lookup data for the third parallel RC time constant at the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Third time constant, tau3(SOC)** — Third RC time constant `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | matrix of positive numbers

Lookup data for the third parallel RC time constant at the specified SOC.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Fourth polarization resistance, R4(SOC,T)** — Fourth RC resistance at temperature breakpoints `[.014, .382, .407; .028, .006, .007; .014, .007, .006; .333, .956, .912]` `Ohm` (default) | matrix of positive numbers

Lookup data for the fourth parallel RC resistance at the specified SOC and temperature breakpoints. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four
time-constant dynamics` or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Fourth polarization resistance, R4(SOC)** — Fourth RC resistance `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive numbers

Lookup data for the fourth parallel RC resistance at the specified SOC. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four
time-constant dynamics` or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Fourth time constant, tau4(SOC,T)** — Fourth RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive numbers

Lookup data for the fourth parallel RC time constant at the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four
time-constant dynamics` or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Fourth time constant, tau4(SOC)** — Fourth RC time constant `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | matrix of positive numbers

Lookup data for the fourth parallel RC time constant at the specified SOC.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four
time-constant dynamics` or `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Fifth polarization resistance, R5(SOC,T)** — Fifth RC resistance at temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive numbers

Lookup data for the fifth parallel RC resistance at the specified SOC and temperature breakpoints. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Fifth polarization resistance, R5(SOC)** — Fifth RC resistance `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | matrix of positive numbers

Lookup data for the fifth parallel RC resistance at the specified SOC. This parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### **Fifth time constant, tau5(SOC,T)** — Fifth RC time constant at temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive numbers

Lookup data for the fifth parallel RC time constant at the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`Yes`.

### **Fifth time constant, tau5(SOC)** — Fifth RC time constant `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | matrix of positive numbers

Lookup data for the fifth parallel RC time constant at the specified SOC.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five
time-constant dynamics` and **Tabulate
parameters over temperature** to
`No`.

### Fade

### **Fade characteristic** — Select how to define fade characteristic `Disabled` (default) | `Equations` | `Lookup tables (temperature independent)` | `Lookup tables (constant temperature dependent)`

Select how to define fade characteristic:

- `Disabled` — The block does not model fade characteristic.
- `Equations` — The cell capacity
  and terminal resistance will be proportional to N whilst the open-circuit voltage will be
  proportional to *N*. If the self-discharge
  resistance or any number of the time constants are enabled,
  their values will be proportional to N.
- `Lookup tables (temperature independent)` — Set tabulated data for the percentage change in parameters as a function of *N*.
- `Lookup tables (constant temperature
  dependent)` — Set tabulated data for the
  percentage change in parameters as a function of
  *N* and temperature. This option is
  valid only if you simulate the battery with a constant
  temperature value.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_fade` |
| **Values:** | `"disabled"` (default) | `"equations"` | `"tableN"` | `"tableNandT"` |

### **Number of discharge cycles, N** — Reference number of cycles for percent change calculations `100` (default) | number from `1` to `Inf`

The number of charge-discharge cycles over which the specified percent changes occur.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Equations`.

### **Change in open-circuit voltage after N discharge cycles (%)** — Percent change in open-circuit voltage after *N* cycles `0` (default) | scalar

Percent change in the open-circuit voltage after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the open-circuit voltage increases. If you specify a negative value
for this parameter, the value of the open-circuit voltage decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Equations`.

### **Change in terminal resistance after N discharge cycles (%)** — Percent change in series resistance after *N* cycles `0` (default) | scalar

Percent change in the series resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Equations`.

### **Change in cell capacity after N discharge cycles (%)** — Percent change in cell capacity after *N* cycles `0` (default) | scalar

Percent change in the cell capacity after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Equations`.

### **Change in self-discharge resistance after N discharge cycles (%)** — Percent change in self-discharge resistance after *N* cycles `0` (default) | scalar

Percent change in the self-discharge resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Self-discharge** to `Enabled` and **Fade characteristic** to `Equations`.

### **Change in first polarization resistance after N discharge cycles (%)** — Percent change in first RC resistance after *N* cycles `0` (default) | scalar

Percent change in the first RC resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the first RC resistance increases. If you specify a negative value
for this parameter, the value of the first RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One time-constant dynamics`, `Two time-constant dynamics`, `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Equations`.

### **Change in second polarization resistance after N discharge cycles (%)** — Percent change in second RC resistance after *N* cycles `0` (default) | scalar

Percent change in the second RC resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the second RC resistance increases. If you specify a negative value
for this parameter, the value of the second RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two time-constant dynamics`, `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Equations`.

### **Change in third polarization resistance after N discharge cycles (%)** — Percent change in third RC resistance after *N* cycles `0` (default) | scalar

Percent change in the third RC resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the third RC resistance increases. If you specify a negative value
for this parameter, the value of the third RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Equations`.

### **Change in fourth polarization resistance after N discharge cycles (%)** — Percent change in fourth RC resistance after *N* cycles `0` (default) | scalar

Percent change in the fourth RC resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the fourth RC resistance increases. If you specify a negative value
for this parameter, the value of the fourth RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Equations`.

### **Change in fifth polarization resistance after N discharge cycles (%)** — Percent change in fifth RC resistance after *N* cycles `0` (default) | scalar

Percent change in the fifth RC resistance after the battery undergoes *N* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the fifth RC resistance increases. If you specify a negative value
for this parameter, the value of the fifth RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five time-constant dynamics` and **Fade characteristic** to `Equations`.

### **Vector of discharge cycle values, N** — Reference vector or numbers of cycles for percent change calculations `[0, 100, 200, 300]` (default) | number from `0` to `Inf`

Vector of numbers of charge-discharge cycles over which the specified percent changes occur.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup
tables (temperature independent)` or
`Lookup tables (constant temperature
dependent)`.

### **Vector of temperatures for fade data, Tfade** — Vector temperatures at which fade lookup tables has been extracted `[298.15, 323.15]` `K` (default) | number from `1` to `Inf`

Vector of temperatures at which fade lookup tables has been extracted. These temperatures are completely independent of **Vectors of temperatures, T** parameter from the **Main** tab.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup
tables (constant temperature dependent)`.

### **Percentage change in open-circuit voltage, dV0(N)** — Vector of percent change in open-circuit voltage after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent changes in the open-circuit voltage after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the open-circuit voltage increases. If you specify a negative value
for this parameter, the value of the open-circuit voltage decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percentage change in terminal resistance, dR0(N)** — Vector of percent change in series resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the series resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percentage change in cell capacity, dAH(N)** — Vector of percent change in cell capacity after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the cell capacity after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percentage change in self-discharge resistance, dRleak(N)** — Vector of percent change in self-discharge resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the self-discharge resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Self-discharge** to `Enabled` and **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percentage change in first polarization resistance, dR1(N)** — Vector of percent change in first RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the first RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the first RC resistance increases. If you specify a negative value
for this parameter, the value of the first RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One time-constant dynamics`, `Two time-constant dynamics`, `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percent change in second polarization resistance, dR2(N)** — Vector of percent change in second RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the second RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the second RC resistance increases. If you specify a negative value
for this parameter, the value of the second RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two time-constant dynamics`, `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percent change in third polarization resistance, dR3(N)** — Vector of percent change in third RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the third RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the third RC resistance increases. If you specify a negative value
for this parameter, the value of the third RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three time-constant dynamics`, `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percent change in fourth polarization resistance, dR4(N)** — Vector of percent change in fourth RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the fourth RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the fourth RC resistance increases. If you specify a negative value
for this parameter, the value of the fourth RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four time-constant dynamics`, or `Five time-constant dynamics` and **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percent change in fifth polarization resistance, dR5(N)** — Vector of percent change in fifth RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Vector of percent change in the fifth RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the fifth RC resistance increases. If you specify a negative value
for this parameter, the value of the fifth RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five time-constant dynamics` and **Fade characteristic** to `Lookup tables (temperature independent)`.

### **Percentage change in open-circuit voltage, dV0(N, Tfade)** — Matrix of percent change in open-circuit voltage after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent changes in the open-circuit voltage after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the open-circuit voltage increases. If you specify a negative value
for this parameter, the value of the open-circuit voltage decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup
tables (constant temperature dependent)`.

### **Percentage change in terminal resistance, dR0(N, Tfade)** — Matrix of percent change in series resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the series resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup
tables (constant temperature dependent)`.

### **Percentage change in cell capacity, dAH(N, Tfade)** — Matrix of percent change in cell capacity after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the cell capacity after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Fade characteristic** to `Lookup
tables (constant temperature dependent)`.

### **Percentage change in self-discharge resistance, dRleak(N, Tfade)** — Matrix of percent change in self-discharge resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the self-discharge resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Self-discharge** to
`Enabled` and **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`.

### **Percentage change in first polarization resistance, dR1(N, Tfade)** — Matrix of percent change in first RC resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the first RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the first RC resistance increases. If you specify a negative value
for this parameter, the value of the first RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `One
time-constant dynamics`, `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`.

### **Percent change in second polarization resistance, dR2(N, Tfade)** — Matrix of percent change in second RC resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the second RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the second RC resistance increases. If you specify a negative value
for this parameter, the value of the second RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Two
time-constant dynamics`, `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`.

### **Percent change in third polarization resistance, dR3(N, Tfade)** — Matrix of percent change in third RC resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the third RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the third RC resistance increases. If you specify a negative value
for this parameter, the value of the third RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Three
time-constant dynamics`, `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`.

### **Percent change in fourth polarization resistance, dR4(N, Tfade)** — Matrix of percent change in fourth RC resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the fourth RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the fourth RC resistance increases. If you specify a negative value
for this parameter, the value of the fourth RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Four
time-constant dynamics`, or `Five
time-constant dynamics` and **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`.

### **Percent change in fifth polarization resistance, dR5(N, Tfade)** — Matrix of percent change in fifth RC resistance after *N* cycles `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Matrix of percent change in the fifth RC resistance after the battery undergoes *N* discharge cycles.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of discharge cycles is zero.
If you do not define the zero breakpoint values, unexpected behavior
might occur depending on the extrapolation option.

**Note**

If you specify a positive value for this parameter, the value of
the fifth RC resistance increases. If you specify a negative value
for this parameter, the value of the fifth RC resistance decreases.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Five
time-constant dynamics` and **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`.

### Calendar Aging

### **Internal resistance calendar aging** — Calendar aging for internal resistance `Disabled` (default) | `Enabled`

Whether to enable calendar aging of the internal resistance of the battery.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_age_resistance` |
| **Values:** | `"disabled"` (default) | `"enabled"` |

### **Capacity calendar aging** — Calendar aging for capacity `Disabled` (default) | `Enabled`

Whether to enable calendar aging of the capacity of the battery.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_age_capacity` |
| **Values:** | `"disabled"` (default) | `"enabled"` |

### **Modeling option** — Calendar aging option `Equation-based` (default) | `Tabulated: temperature` | `Tabulated: time and temperature`

Modeling option for internal resistance and capacity calendar aging.

#### Dependencies

To enable this parameter, set either **Internal resistance calendar aging** or **Capacity calendar aging** to `Enabled`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_age_modeling` |
| **Values:** | `"equation"` (default) | `"tableT"` | `"tableTandTime"` |

### **Vector of time intervals** — Time intervals `[0]` `d` (default) | vector of scalars

Time intervals. This parameter must be equal in size to **Vector of storage temperatures**.

#### Dependencies

To enable this parameter, set **Modeling option** to either `Equation-based`, `Tabulated: temperature`, or `Tabulated: time and temperature`.

### **Vector of storage temperatures** — Storage temperatures `[273]` `K` (default) | vector of scalars

Set of storage temperatures. This parameter must be equal in size to **Vector of time intervals**.

#### Dependencies

To enable this parameter, set **Modeling option** to either `Equation-based`, `Tabulated: temperature`, or `Tabulated: time and temperature`.

### **Storage condition** — Storage condition `Specify open-circuit voltage during storage` (default) | `Specify state-of-charge during storage`

Whether to specify the open-circuit voltage or the state of charge during storage.

#### Dependencies

To enable this parameter, set **Modeling option** to `Equation-based`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `prm_age_OCV` |
| **Values:** | `"OCV"` (default) | `"SOC"` |

### **Normalized open-circuit voltage during storage, V/Vnom** — Normalized open-circuit voltage during storage `0.9` (default) | scalar

Normalized open-circuit voltage during storage.

#### Dependencies

To enable this parameter, set **Modeling option** to `Equation-based` and **Storage condition** to `Specify open-circuit voltage during storage`.

### **State of charge during storage** — Percentage state of charge during storage `60` (default) | positive number

State of charge during storage, in percentage.

#### Dependencies

To enable this parameter, set **Modeling option** to `Equation-based` and **Storage condition** to `Specify state-of-charge during storage`.

### **Terminal resistance linear scaling for voltage, b** — Voltage linear scaling in terminal resistance `2.2134e6` (default) | scalar

Linear scaling coefficient in terminal resistance for open-circuit voltage.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to `Equation-based`.

### **Terminal resistance constant offset for voltage, c** — Voltage constant offset in terminal resistance `1.632e6` (default) | scalar

Constant offset in terminal resistance for open-circuit voltage.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to `Equation-based`.

### **Terminal resistance temperature-dependent exponential increase, d** — Temperature-dependent exponential increase in terminal resistance `0.515833569` `V` (default) | scalar

Temperature-dependent exponential increase in terminal resistance.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to `Equation-based`.

### **Terminal resistance time exponent, a** — Time exponent in terminal resistance `0.75` (default) | scalar

Time exponent in terminal resistance.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to either `Equation-based` or `Tabulated: temperature`.

### **Capacity linear scaling for voltage, b** — Voltage linear scaling in capacity `1.5097e07` (default) | scalar

Linear scaling coefficient in capacity for open-circuit voltage.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to `Equation-based`.

### **Capacity constant offset for voltage, c** — Voltage constant offset in capacity `8.3625e06` (default) | scalar

Constant offset in capacity for open-circuit voltage.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to `Equation-based`.

### **Capacity temperature-dependent exponential increase, d** — Temperature-dependent exponential increase in capacity `0.6011` `V` (default) | scalar

Temperature-dependent exponential increase in capacity.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to `Equation-based`.

### **Capacity time exponent, a** — Time exponent in capacity `0.75` (default) | scalar

Time exponent in capacity.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to either `Equation-based` or `Tabulated: temperature`.

### **Vector of sampled temperatures for terminal resistance calendar aging, T\_ar** — Sampled temperatures for terminal resistance calendar aging `[273.15, 298.15, 323.15]` `K` (default) | vector of scalars

Vector of sampled temperatures for terminal resistance calendar aging.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to either `Tabulated: temperature` or `Tabulated: time and temperature`.

### **Percentage change in terminal resistance due to calendar aging, dR0(T\_ar)** — Percentage change in terminal resistance due to calendar aging `[0,0,0]` (default) | vector of scalars

Percentage change in terminal resistance due to calendar aging.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to
`Enabled` and **Modeling
option** to `Tabulated:
temperature`.

### **Time between terminal resistance beginning of life and dR(T\_ar) measurement** — Time between terminal resistance beginning of life and dR(T\_ar) measurement `100` `d` (default) | scalar

Time between the beginning of life of the terminal resistance and the dR(T\_ar) measurement.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to
`Enabled` and **Modeling
option** to `Tabulated:
temperature`.

### **Vector of sampled temperatures for capacity calendar aging, T\_ac** — Sampled temperatures for capacity calendar aging `[273.15, 298.15, 323.15]` `K` (default) | vector of scalars

Vector of sampled temperatures for capacity calendar aging.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to either `Tabulated: temperature` or `Tabulated: time and temperature`.

### **Percentage change in capacity due to calendar aging, dAH(T\_ac)** — Percentage change in capacity due to calendar aging `[0,0,0]` (default) | vector of scalars

Percentage change in capacity due to calendar aging.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to
`Enabled` and **Modeling
option** to `Tabulated:
temperature`.

### **Time between capacity beginning of life and dAH(T\_ac) measurement** — Time between capacity beginning of life and dAH(T\_ac) measurement `100` `d` (default) | scalar

Time between the beginning of life of the capacity and the dR(T\_ac) measurement.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to
`Enabled` and **Modeling
option** to `Tabulated:
temperature`.

### **Vector of sampled storage time intervals for terminal resistance calendar aging, t\_ar** — Sampled storage time intervals for terminal resistance calendar aging `[0, 90, 180, 270, 360]` `d` (default) | vector of scalars

Vector of sampled storage time intervals for terminal resistance calendar aging.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of time intervals is zero. If
you do not define the zero breakpoint values, unexpected behavior might
occur depending on the extrapolation option.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to `Tabulated: time and temperature`.

### **Percentage change in terminal resistance due to calendar aging, dR0(t\_ar,T\_ar)** — Percentage change in terminal resistance due to calendar aging `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` (default) | matrix of scalars

Percentage change in terminal resistance due to calendar aging.

#### Dependencies

To enable this parameter, set **Internal resistance calendar aging** to `Enabled` and **Modeling option** to `Tabulated: time and temperature`.

### **Vector of sampled storage time intervals for capacity calendar aging, t\_ac** — Sampled storage time intervals for capacity calendar aging `[0, 90, 180, 270, 360]` `d` (default) | vector of scalars

Vector of sampled storage time intervals for capacity calendar aging.

The block supports the definition of breakpoint values for the fading
and calendar aging options when the number of time intervals is zero. If
you do not define the zero breakpoint values, unexpected behavior might
occur depending on the extrapolation option.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to `Tabulated: time and temperature`.

### **Percentage change in capacity due to calendar aging, dAH(t\_ac,T\_ac)** — Percentage change in capacity due to calendar aging `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` (default) | matrix of scalars

Percentage change in capacity due to calendar aging.

#### Dependencies

To enable this parameter, set **Capacity calendar aging** to `Enabled` and **Modeling option** to `Tabulated: time and temperature`.

### Thermal

### **Thermal port** — Thermal port visibility `Omit` (default) | `Model`

Whether to expose the thermal port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `thermal_port` |
| **Values:** | `"omit"` (default) | `"model"` |

### **Simulation temperature** — Battery temperature `298.15` `K` (default) | positive number

Battery temperature used in lookup tables throughout simulation.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Omit` and **Tabulate
parameters over temperature** to
`Yes` or **Fade
characteristic** to `Lookup tables
(constant temperature dependent)`. For more
information, see Modeling Thermal Effects.

### **Thermal mass** — Thermal mass associated with thermal port `100` `J/K` (default)

Thermal mass associated with the thermal port H. It represents the
energy required to raise the temperature of the thermal port by one
degree.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`. For more information, see
Modeling Thermal Effects.

## Libraries

Simscape / Electrical / Sources Simscape / Battery / Cells

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2023b: Define breakpoint values for the fading and calendar aging options when the number of discharge cycles or time intervals is zero

You can define the breakpoint values for the fading and calendar aging options
when the number of discharge cycles or time intervals is zero.

If you do not define the zero breakpoint values:

- If you set the **Extrapolation method for all
  tables** parameter to `Linear`,
  the block might extrapolate an incorrect value depending on the table
  data. For example, the extrapolated capacity can rise above one, meaning
  that the capacity of the cell at that point is greater than the nominal
  capacity of the cell.
- If you set the **Extrapolation method for all
  tables** parameter to `Nearest`,
  the block extrapolates the nearest value. For a brand new battery, this
  means that the fading and calendar aging would have already
  occurred.
- If you set the **Extrapolation method for all
  tables** parameter to `Error`, the
  software throws an error if the number of discharge cycles or storage
  duration is lower than the lowest breakpoint for this table data.

## Description

Tabulated battery model

The Battery (Table-Based) block represents a high-fidelity
battery model. The block calculates open-circuit voltage as a function of charge level
and optional temperature using lookup tables and includes several modeling options:

- Self-discharge
- Battery fade
- Charge dynamics
- Calendar aging

**Note**

For all the table-based parameters, the Battery
(Table-Based) block supports linear interpolation only. For
extrapolation, set the **Extrapolation method for all tables**
parameter to either `Nearest`,
`Linear`, or `Error`.

For rows and columns, it follows the row-column convention, whereas rows are
indexed first and, subsequently, columns.

The plot shows a battery whose performance varies with temperature and state of charge changes, as typically found on a datasheet.

Use this block to parameterize batteries with complex open-circuit voltage behavior from datasheets or experimental results. For a simpler representation of a battery, see the Battery (Simscape Electrical) block.

The Battery (Table-Based) block has two optional ports that you can expose by setting the corresponding parameters. The extra physical signal port, **SOC**, outputs the internal state of charge. Use this functionality to change the load behavior as a function of state of charge, without the complexity of building a charge state estimator. To expose the **SOC** port, in the **Main** setting, set the **Expose SOC measurement port** parameter to `Yes`.

To expose the thermal port, in the **Thermal** setting, set the **Thermal port** parameter to `Model`. The thermal port represents the battery thermal mass.

You can also choose different built-in parameterizations for this block. For more information, see the Predefined Parameterization section.

The battery equivalent circuit is made up of the fundamental battery model, the self-discharge resistance *RSD*, the charge dynamics model, and the series resistance *R0*.

### Battery Model

The block calculates the open-circuit voltage, or the voltage across the fundamental battery model by interpolation:

v0=v0(SOC,T)

Where:

- *v0* is the open-circuit voltage of the battery. Specify the grid of lookup values using the **Open-circuit voltage, V0(SOC,T)** parameter if tabulating parameters over temperature, or **Open-circuit voltage, V0(SOC)** otherwise.
- `SOC` is the ratio of current charge to nominal battery capacity specified in the **Cell capacity, AH** parameter along with the effects of the temperature dependent fade percentage change in cell capacity, *δAH(n, Tfade)*, specified in the **Percentage change in cell capacity, dAH(N, Tfade)** parameter. Specify the SOC breakpoints using the **Vector of state-of-charge values, SOC** parameter. The block estimates the nominal battery capacity based on the number of cycles and the temperature of the battery by interpolating the specified temperature dependent fade characteristic and the **Cell capacity, AH** parameter.

  `SOC` represents the normalized data with respect to *qnom*.

  For the lookup-table based fade characteristic option,

  qnom(T,n)=(1+δAH(n,Tfade)100)\*AH Ah.

  For the equation-based fade characteristic option,

  qnom(T,n)=(1+δAH100nN)\*AH Ah.

  Finally, `SOC` is obtained from the following equation.

  SOC(t)=1qnom(T,n)∫(i(t)−Vopen(T,n,t)RSD(T,n))dt

  Where:

  - *qnom* is the cell capacity of the battery. Specify this value using the **Cell capacity, AH** parameter.
  - *N* is the reference number of discharge cycles over which you specify percent change of several battery parameters. Set this value using the **Number of discharge cycles, N** parameter.
  - *n* is the present number of cycles of the battery.
  - *δAH* is the percentage change in cell capacity of the battery after *N* discharge cycles.
- *T* is the battery temperature. Specify the *T* breakpoints using the **Vector of temperatures, T** parameter if tabulating the parameters over temperature.

The block also models the series resistance *R0* as a function of state of charge and optional temperature. Specify the grid of lookup values for the series resistance using the **Terminal resistance, R0(SOC,T)** parameter if tabulating the parameters over temperature, or **Terminal resistance, R0(SOC)** otherwise.

### Modeling Self-Discharge

When the battery terminals are open-circuit, it is still possible for internal currents to discharge the battery. This behavior is called self-discharge. To enable this effect, set the **Self-discharge** parameter to `Enabled`.

The block models these internal currents with a temperature-dependent resistance *RSD(T)* across the terminals of the fundamental battery model. You can specify the lookup values for this resistance using the **Self-discharge resistance, Rleak(T)** parameter if tabulating the parameters over temperature, or **Self-discharge resistance, Rleak** otherwise.

### Modeling Charge Dynamics

Batteries are not able to respond instantaneously to load changes. They require some time to achieve a steady-state. This time-varying property is a result of battery charge dynamics and is modeled using parallel RC sections in the equivalent circuit.

You can model battery charge dynamics using the **Charge dynamics** parameter:

- `No dynamics` — The equivalent circuit contains no parallel RC sections. There is no delay between terminal voltage and internal charging voltage of the battery.
- `One time-constant dynamics` — The equivalent circuit contains one parallel RC section. Specify the time constant using the **First time constant, tau1(SOC,T)** parameter if tabulating parameters over temperature or **First time constant, tau1(SOC)** otherwise.
- `Two time-constant dynamics` — The equivalent circuit contains two parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)** and **Second time constant, tau2(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)** and **Second time constant, tau2(SOC)** otherwise.
- `Three time-constant dynamics` — The equivalent circuit contains three parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)**, **Second time constant, tau2(SOC,T)**, and **Third time constant, tau3(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)**, **Second time constant, tau2(SOC)**, and **Third time constant, tau3(SOC)** otherwise.
- `Four time-constant dynamics` — The equivalent circuit contains four parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)**, **Second time constant, tau2(SOC,T)**, **Third time constant, tau3(SOC,T)**, and **Fourth time constant, tau4(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)**, **Second time constant, tau2(SOC)**, **Third time constant, tau3(SOC)**, and **Fourth time constant, tau4(SOC)** otherwise.
- `Five time-constant dynamics` — The equivalent circuit contains five parallel RC sections. Specify the time constants using the **First time constant, tau1(SOC,T)**, **Second time constant, tau2(SOC,T)**, **Third time constant, tau3(SOC,T)**, **Fourth time constant, tau4(SOC,T)**, and **Fifth time constant, tau5(SOC,T)** parameters if tabulating parameters over temperature or **First time constant, tau1(SOC)**, **Second time constant, tau2(SOC)**, **Third time constant, tau3(SOC)**, **Fourth time constant, tau4(SOC)**, and **Fifth time constant, tau5(SOC)** otherwise.

This diagram shows the equivalent circuit for the block configured with two time-constant dynamics.

In the diagram:

- *R1* and *R2* are the parallel RC resistances. Specify these values with the **First polarization resistance, R1(SOC,T)** and **Second polarization resistance, R2(SOC,T)** parameters, respectively, if tabulating parameters over temperature or **First polarization resistance, R1(SOC)** and **Second polarization resistance, R2(SOC)** otherwise.
- *C1* and
  *C2* are the parallel RC
  capacitances. The time constant *τ* for each parallel
  section relates the *R* and *C* values
  using the relationship C=τ/R. Specify *τ* for each section using
  the **First time constant, tau1(SOC,T)** and
  **Second time constant, tau2(SOC,T)** parameters,
  respectively, if tabulating parameters over temperature or
  **First time constant, tau1(SOC)** and
  **Second time constant, tau2(SOC)**
  otherwise.
- *R0* is the series resistance. Specify this value with the **Terminal resistance, R0(SOC,T)** parameter if tabulating parameters over temperature or **Terminal resistance, R0(SOC)** otherwise.

### Modeling Battery Fade

Battery fade is the deterioration of battery performance over repeated charge and discharge cycles. When the **Fade characteristic** parameter is set to `Equations`, the battery fade is modeled as follows.

The open-circuit voltage across the fundamental battery model fades proportionally with the number of discharge cycles *n*:

v0,fade=v0(1+δv0100nN)

Where *δv0* is the percent change in open-circuit voltage after *N* discharge cycles. Specify *δv0* using the  **Change in open-circuit voltage after N discharge cycles (%)** parameter.

**Note**

The Battery (Table-Based) block tracks the
current and integrates it over time. The number of discharge cycles
*n* increases by 1 every time an equivalent cell discharge
capacity is extracted.

The nominal charge, from which state of charge is calculated, fades with the square root of number of discharge cycles:

qnom,fade=qnom(1+δAH100nN)

All resistances in the battery model also fade with the square root of the number of discharge cycles:

Ri,fade=Ri(1+δRi100nN)

Where:

- *Ri* is the *i*th resistance
- *δRi* is the percent change in this resistance over *N* cycles

Depending on how you have configured the block, the resistances might include:

- The series resistance — Specify the percent change over *N* cycles using the **Change in terminal resistance after N discharge cycles (%)** parameter.
- The self-discharge resistance — Specify the percent change over *N* cycles using the **Change in self-discharge resistance after N discharge cycles (%)** parameter.
- The first charge dynamics resistance — Specify the percent change over
  *N* cycles using the **Change in first
  polarization resistance after N discharge cycles (%)**
  parameter.
- The second charge dynamics resistance — Specify the percent change over *N* cycles using the **Change in second polarization resistance after N discharge cycles (%)** parameter.
- The third charge dynamics resistance — Specify the percent change over *N* cycles using the **Change in third polarization resistance after N discharge cycles (%)** parameter.
- The fourth charge dynamics resistance — Specify the percent change over *N* cycles using the **Change in fourth polarization resistance after N discharge cycles (%)** parameter.
- The fifth charge dynamics resistance — Specify the percent change over *N* cycles using the **Change in fifth polarization resistance after N discharge cycles (%)** parameter.

**Note**

You can also model the battery fade characteristic by using lookup tables
(temperature independent) or lookup tables (constant temperature dependent).
Choosing any of these two options changes the blocks parameters accordingly. For
more information, see the Fade parameters
tab.

### Modeling Thermal Effects

The battery temperature is determined from a summation of all the ohmic losses included in the model:

MthT˙=∑iVT,i2/RT,i

Where:

- *M*th is the battery thermal mass.
- *i* corresponds to the *i*th ohmic loss contributor. Depending on how you have configured the block, the losses might include:

  - The series resistance
  - The self-discharge resistance
  - The first charge dynamics segment
  - The second charge dynamics segment
  - The third charge dynamics segment
  - The fourth charge dynamics segment
  - The fifth charge dynamics segment
- *VT,i* is the voltage drop across resistor *i*.
- *RT,i* is resistor *i*.

### Modeling Battery Aging

You can model the battery performance deterioration that occurs when the battery is not used. Calendar aging affects both the internal resistance and capacity. In particular, the resistance increase depends by various mechanisms such as the creation of Solid Electrolyte Interface (SEI) at both anode and cathode and the corrosion of the current collector. These processes mainly depends on the storage temperature, the storage state of charge, and time.

You can model the calendar aging in the Battery (Table-Based) block by setting the **Modeling option** parameter to:

- `Equation-based`
- `Tabulated: temperature`
- `Tabulated: time and temperature`

**Note**

The Battery (Table-Based) block only applies the calendar aging
during initialization. When you set the **Internal resistance calendar
aging** or **Capacity calendar aging** parameters
to `Enabled`, the block exposes the **Vector of
time intervals** parameter that represents the time the battery has
aged before the start of the simulation. Calendar aging during the simulation is
not covered with this option.

**Equation-based**

This equation defines the terminal resistance increase of the battery due to calendar aging:

αr(T,Voc)=(bVoc−c)e−qdkT,R=R0(1+∑i=1i=nαr(Ti,Voc)(tia−ti−1a)),

where:

- *Voc* is the **Normalized open-circuit voltage during storage, V/Vnom**.
- *R0* is the **Internal resistance**.
- *ti* is the time sample derived from the **Vector of time intervals** parameter.
- *Ti* is derived from the **Vector of temperatures, T** parameter.
- *b* is the **Terminal resistance linear scaling for voltage, b**.
- *c* is the **Terminal resistance constant offset for voltage, c**.
- *d* is the **Terminal resistance temperature-dependent exponential increase, d**.
- *a* is the **Terminal resistance time exponent, a**.
- *q* is the electron's elementary charge, in C.
- *k* is the Boltzmann constant, in J/K.

This equation defines the capacity decrease of the battery due to calendar aging:

αc(T,Voc)=(bVoc−c)e−qdkT,C=C0(1−∑i=1i=nαc(Ti,Voc)(tia−ti−1a)),

where:

- *C0* is the **initial capacity**.
- *b* is the **Capacity linear scaling for voltage, b**.
- *c* is the **Capacity constant offset for voltage, c**.
- *d* is the **Capacity temperature-dependent exponential increase, d**.
- *a* is the **Capacity time constant, a**.

If you set the **Storage condition** parameter to `Specify state-of-charge during storage`, the block converts the state of charge during storage into normalized open-circuit voltage using the tabulated voltage **V0** against the state of charge and the temperature during storage.

**Tabulated: temperature**

The aged terminal resistance is the product between the terminal resistance, *R0(SOC,T)*, the percentage resistance increase, *dR0*, and the power law that describes the time dependence of the calendar aging:

R0(SOC,T;tst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Tst,i)100(tast,i−tast,i−1tast,m)),

where:

- *T* is the battery temperature. Specify the *T* breakpoints using the **Vector of temperatures, T** parameter if tabulating the parameters over temperature.
- *Tst* is the **Vector of storage temperatures**.
- *tst,i* and *tst,i-1* are the time samples derived from the **Vector of time intervals**.
- *t0* is assumed to be null.
- *tst,m* is the moment in time at which the resistance increase, *dR0*, is measured.

The same equation applies to the calculation of the aged battery capacity.

**Tabulated: time and temperature**

The aged terminal resistance is the product between the terminal resistance, *R0(SOC,T)* and *dR0*:

R0(SOC,T;Δtst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Δtst,i,Tst,i)100).

The same equation applies to the calculation of the aged battery capacity.

### Predefined Parameterization

There are multiple available built-in parameterizations for the Battery (Table-Based) block.

This pre-parameterization data allows you to set up the block to represent components by specific suppliers. The parameterizations of these batteries match the discharge curves in the manufacturer data sheets. To load a predefined parameterization, double-click the Battery (Table-Based) block, click the **<click to select>** hyperlink of the **Selected part** parameter and, in the Block Parameterization Manager window, select the part you want to use from the list of available components.

The available pre-parameterized data model steady state electrical parameters of a lithium-ion battery. The **Open-circuit voltage, V0(SOC)**, **Terminal resistance, R0(SOC, T)**, **Cell capacity, AH**, **Percentage change in cell capacity, dAH**, and **Percentage change in Open-circuit voltage, dV0(N)** parameters are parameterized from characteristics curves in the manufacture datasheets. The change in series resistance with the battery cycle life, the thermal mass, and the dynamic RC network parameters are not parameterized. Instead, the net resistance of the RC network resistors is summed to the series resistance of the specific pre-parameterized data. If you need to fill the RC parameter data, subtract the net RC network resistance from the series resistance data.

The available data is parameterized for 1C discharge current for different temperatures up to the minimum terminal voltage in the datasheet. The data below the minimum terminal voltage is extrapolated. The **Open-circuit voltage, V0(SOC)** parameter is approximated to be temperature independent. At lower temperature, in the low SOC region, the terminal resistances are constant and equal to the value of the resistance at the minimum terminal voltage. This might lead to higher thermal losses.

**Note**

The predefined parameterizations of Simscape™ components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about pre-parameterization and for a list of the available components, see List of Pre-Parameterized Components (Simscape Electrical).

### Plot Basic Voltage-Charge Characteristics

You can plot the basic voltage-charge characteristics of the Battery (Table-Based) block without
building a complete model. Use the plots to explore the impact of your parameter
choices on device characteristics. If you parameterize the block from a datasheet,
you can compare your plots to the datasheet to check that you parameterized the
block correctly. If you have a complete working model but do not know which
manufactured part to use, you can compare your plots to datasheets to help you
decide.

To plot the basic characteristics, right-click the block and select
**Battery** > **Basic
characteristics** from the context menu. For more information
about the **Basic characteristics** option, see Plot Basic Voltage-Charge Characteristics of Battery Blocks (Simscape Electrical).
