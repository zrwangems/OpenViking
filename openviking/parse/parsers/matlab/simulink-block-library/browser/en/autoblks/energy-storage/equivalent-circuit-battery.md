---
type: simulink-block
title: 'Equivalent Circuit Battery'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'equivalentcircuitbattery'
documentation_source_path: 'ref/equivalentcircuitbattery.html'
language: en
---

# Equivalent Circuit Battery

## Ports

### Inputs

### **CapInit** — Battery capacity `scalar`

Rated battery capacity at the nominal temperature,
*Capbatt*, in Ah.

#### Dependencies

To create this port, select `External
Input` for the **Initial battery
capacity** parameter.

### **BattCurr** — Battery network current `scalar`

Combined current flowing from the battery network,
*Iin*, in A.

### **BattTemp** — Battery temperature `scalar`

Battery temperature, *T*, in K.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `BattCurr` | | | Combined current flowing from the battery network | *Ibatt* | A |
| `BattAmpHr` | | | Battery energy | *LdAmpHr* | A\*h |
| `BattSoc` | | | State-of-charge capacity | *SOC* | NA |
| `BattVolt` | | | Combined voltage of the battery network | *Vout* | V |
| `BattPwr` | | | Battery power | *Pbatt* | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrLdBatt` | Battery network power | *PLdBatt* | W |
| `PwrNotTrnsfrd` | `PwrLossBatt` | Battery network power loss | *PLossBatt* | W |
| `PwrStored` | `PwrStoredBatt` | Battery network power stored | *PStoredBatt* | W |
| `HystState` | | | Hysteresis state variable | *Hstate* | 1 |
| `HystVolt` | | | Hysteresis voltage | *Vhyst* | V |
| `EntropicPwr` | | | Entropic reversible losses | *Pentropic* | W |

### **BattVolt** — Battery output voltage `scalar`

Combined voltage of the battery network, *Vout*,
in V.

## Parameters

#### Block Options

### **Initial battery capacity** — Input or parameter `Parameter` (default) | `External Input`

Initial battery capacity,
*Capbatt*, in Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CapacityCtrl` |
| **Values:** | `Parameter` (default) | `External Input` |
| **Data Types:** | `character vector` |

#### Dependencies

| Block Parameter **Initial battery capacity** Option | Creates |
| --- | --- |
| `External Input` | Input port `CapInit` |
| `Parameter` | Parameter **Initial battery capacity, BattCapInit** |

### **Output battery voltage** — Unfiltered or Filter `Unfiltered` (default) | `Filtered`

Select `Filtered` to apply a first-order filter
to the output battery voltage.

#### Dependencies

Setting **Output battery voltage** parameter to
`Filtered` creates these parameters:

- **Output battery voltage time constant, Tc**
- **Output battery voltage initial value, Vinit**

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputVlt` |
| **Values:** | `Unfiltered` (default) | `Filtered` |
| **Data Types:** | `character vector` |

### **Include current polarity** — Add current direction `off` (default) | `on`

Select this parameter to add current direction in the equivalent circuit
battery.

To improve calibration for charging and discharging processes,
select **Include current polarity**. To model the current polarity, the block
implements resistive and capacitive lookup tables with current direction.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `PolarityEnabled` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Include hysteresis** — Add hysteresis voltage `off` (default) | `on`

Select this parameter to add the hysteresis voltage.

Hysteresis voltage adds a state estimator for non-linear
voltage offsets when the battery current changes from charge to discharge. To calculate the
combined voltage of the battery network with hysteresis, select **Include
hysteresis**. The block uses these equations.

Hstate=∫(−Hstate•abs(Ibatt)−Ibatt)•HystRateCbattVHyst=Hstate•MaxHystVolt−InstHystVolt•sign(Ibatt)VT=VHyst+Em−IbattRo−∑1nVn

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `HusteresisEnabled` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Include entropic heating** — Add entropic heating `off` (default) | `on`

Select this parameter to add entropic heating.

Entropic heating accounts for power losses that occur during
the battery phase change. To calculate the battery network power loss with entropic heating,
select **Include entropic heating**. The block uses these equations.

Pentropic=−IBatt•T•EntdUdTPLossBatt=−(Ibatt2R0+∑1nVn2Rn+Pentropic)

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `EntropicEnabled` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Core Battery

### **Number of series RC pairs** — RC pairs `1` (default) | `0` | `2` | `3` | `4` | `5`

Number of series RC pairs. For lithium, typically 1 or 2. The value
`0` specifies that there are no RC elements in the
circuit.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumRC` |
| **Values:** | `1` (default) | `0` | `2` | `3` | `4` | `5` |
| **Data Types:** | `double` |

### **Open circuit voltage Em table data, Em** — Voltage table `[3.5042 3.5136; 3.5573 3.5646; 3.6009 3.6153; 3.6393 3.6565; 3.6742 3.6889; 3.7121 3.7214; 3.7937 3.8078; 3.8753 3.8945; 3.97 3.9859; 4.0764 4.0821; 4.1924 4.193]` (default) | `array`

Open circuit voltage table, *Em*,
in V. Function of SOC and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Em` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Series resistance table data, R0** — Resistance `array`

Series resistance table, *Ro*, in
ohms. Function of SOC and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R0` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Series charge resistance table data, R0Charge** — Charge resistance `array`

Series charge resistance table, in ohms. Function of SOC and battery
temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R0Charge` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include current
polarity**.

### **Series discharge resistance table data, R0Discharge** — Discharge resistance `array`

Series discharge resistance table, in ohms. Function of SOC and battery
temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `R0Discharge` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include current
polarity**.

### **State of charge breakpoints, SOC\_BP** — SOC breakpoints `[0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1]` (default) | `vector`

State-of-charge (SOC) breakpoints, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SOC_BP` |
| **Values:** | `[0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1]` (default) | `array` |
| **Data Types:** | `double` |

### **Temperature breakpoints, Temperature\_BP** — Battery `[293.15 313.15]` (default) | `vector`

Battery temperature breakpoints, K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temperature_BP` |
| **Values:** | `[293.15 313.15]` (default) | `vector` |
| **Data Types:** | `double` |

### **Battery capacity table, BattCap** — Capacity `[28 28]` (default) | `array`

Battery capacity, *Cbatt*, in Ah.
Function of battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattCap` |
| **Values:** | `[28 28]` (default) | `array` |
| **Data Types:** | `double` |

### **Initial battery capacity, BattCapInit** — Capacity `28` (default) | `scalar`

Initial battery capacity,
*Capbatt*, in Ah.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BattCapInit` |
| **Values:** | `28` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

| Block Parameter **Initial battery capacity** Option | Creates |
| --- | --- |
| `External Input` | Input port `CapInit` |
| `Parameter` | Parameter **Initial battery capacity, BattCapInit** |

### **Initial capacitor voltage, InitialCapVoltage** — Voltage `0` (default) | `array`

Initial capacitor voltage, in V. Dimension of vector must equal
the **Number of series RC pairs**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialCapVoltage` |
| **Values:** | `0` (default) | `array` |
| **Data Types:** | `double` |

### **Output battery voltage time constant, Tc** — Filter time constant `1/1000` (default) | `scalar`

Output battery voltage time constant,
*Tc*, in s. Used in a
first-order voltage filter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tc` |
| **Values:** | `1/1000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Output battery voltage** parameter to
`Filtered` creates these parameters:

- **Output battery voltage time constant, Tc**
- **Output battery voltage initial value, Vinit**

### **Output battery voltage initial value, Vinit** — Filter initial voltage `4.193` (default) | `scalar`

Output battery voltage initial value,
*Vinit*, in V. Used in a
first-order voltage filter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vinit` |
| **Values:** | `4.193` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Output battery voltage** parameter to
`Filtered` creates these parameters:

- **Output battery voltage time constant, Tc**
- **Output battery voltage initial value, Vinit**

#### R and C Table Data

### **Network resistance table data, R*`n`*** — Lookup table `[0.010342 0.0012244; 0.0067316 0.0011396; 0.0051156 0.0012661; 0.0043447 0.0012265; 0.0038826 0.0011163; 0.0034226 0.0009968; 0.003346 0.0011458; 0.0033222 0.001345; 0.0033201 0.0013091; 0.0032886 0.0010986; 0.0028114 0.0010309]` (default) | `array`

Network resistance table data for *`n`*-th RC pair,
in ohms, as a function of SOC and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rn` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Network capacitance table data, C*`n`*** — Lookup table `[2287.7 11897; 6122 24515; 18460 42098; 20975 44453; 15254 33098; 10440 24492; 13903 32975; 16694 40007; 15784 35937; 12165 26430; 9118 24795]` (default) | `array`

Network capacitance table data for *`n`*-th RC
pair, in F, as a function of SOC and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cn` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Network charge resistance table data, R*`n`*Charge** — Lookup table `[0.010342 0.0012244; 0.0067316 0.0011396; 0.0051156 0.0012661; 0.0043447 0.0012265; 0.0038826 0.0011163; 0.0034226 0.0009968; 0.003346 0.0011458; 0.0033222 0.001345; 0.0033201 0.0013091; 0.0032886 0.0010986; 0.0028114 0.0010309]` (default) | `array`

Network charge resistance table data for *`n`*-th
RC pair, in ohms, as a function of SOC and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RnCharge` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include current
polarity**.

### **Network charge capacitance table data, C*`n`*Charge** — Lookup table `[2287.7 11897; 6122 24515; 18460 42098; 20975 44453; 15254 33098; 10440 24492; 13903 32975; 16694 40007; 15784 35937; 12165 26430; 9118 24795]` (default) | `array`

Network charge capacitance table data for *`n`*-th
RC pair, in F, as a function of SOC and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CnCharge` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include current
polarity**.

### **Network discharge resistance table data, R*`n`*Discharge** — Lookup table `[0.010342 0.0012244; 0.0067316 0.0011396; 0.0051156 0.0012661; 0.0043447 0.0012265; 0.0038826 0.0011163; 0.0034226 0.0009968; 0.003346 0.0011458; 0.0033222 0.001345; 0.0033201 0.0013091; 0.0032886 0.0010986; 0.0028114 0.0010309]` (default) | `array`

Network discharge resistance table data for
*`n`*-th RC pair, in ohms, as a function of SOC and
battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RnDischarge` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include current
polarity**.

### **Network discharge capacitance table data, C*`n`*Disharge** — Lookup table `[2287.7 11897; 6122 24515; 18460 42098; 20975 44453; 15254 33098; 10440 24492; 13903 32975; 16694 40007; 15784 35937; 12165 26430; 9118 24795]` (default) | `array`

Network discharge capacitance table data for
*`n`*-th RC pair, in F, as a function of SOC and
battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CnDischarge` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include current
polarity**.

#### Cell Limits

### **Upper integrator voltage limit, Vu** — Maximum `-Inf` (default) | `scalar`

Upper voltage limit, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vu` |
| **Values:** | `-Inf` (default) | `scalar` |
| **Data Types:** | `double` |

### **Lower integrator voltage limit, Vl** — Minimum `-Inf` (default) | `scalar`

Lower voltage limit, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vl` |
| **Values:** | `-Inf` (default) | `scalar` |
| **Data Types:** | `double` |

#### Heating and Hysteresis

### **Entropic Coefficient, EntdUdT** — Lookup table `[-0.2226 -0.2922 -0.1085 -0.0580 0.1027 0.1195 0.0549 -0.0202 -0.0231 0.0165 0.0324]/1000` (default) | `vector`

Entropic coefficient table data,
*EntdUdT*, in V/K, as a function
of SOC.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EntdUdT` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include entropic
heating**.

### **Hysteresis Rate, HystRate** — Hysteresis rate 0.1 (default) | scalar

Hysteresis rate, dimensionless, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `HystRate` |
| **Values:** | 0.1 (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include
hysteresis**.

### **Maximum Hysteresis Voltage, MaxHystVolt** — Lookup table `[0 0;0 0;0 0;0 0;0 0; 0 0; 0 0; 0 0; 0 0; 0 0; 0 0]` (default) | `array`

Maximum hysteresis voltage table data, in V, as a function of SOC and
battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxHystVolt` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include
hysteresis**.

### **Instantaneous Hysteresis Voltage, InstHystVolt** — Lookup table `[0 0;0 0;0 0;0 0;0 0; 0 0; 0 0; 0 0; 0 0; 0 0; 0 0]` (default) | `array`

Instantaneous hysteresis voltage table data, in V, as a function of SOC
and battery temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InstHystVolt` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Include
hysteresis**.

## Libraries

Powertrain Blockset / Energy Storage and Auxiliary Drive / Network Battery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2024b: Model complex battery effects

Configure the Equivalent Circuit Battery block to model complex
battery effects such as current polarity, hysteresis, and entropic heating.

- The Equivalent Circuit Battery block has these parameters.

  - **Include current polarity** — Select
    this option to add current direction for resistance and
    capacitance lookup tables. Selecting this parameter enables
    these parameters on the **Core Battery**
    and **R and C Table Data** tabs.

    - **Core Battery**

      - **Series charge resistance table
        data, R0Charge**
      - **Series discharge resistance table
        data, R0Discharge**
    - **R and C Table Data**

      - **Network charge resistance table
        data,
        R*`n`*Charge**
      - **Network charge capacitance table
        data,
        C*`n`*Charge**
      - **Network discharge resistance table
        data,
        R*`n`*Discharge**
      - **Network discharge capacitance
        table data,
        C*`n`*Discharge**
  - **Include hysteresis** — Select this
    option to add a state estimator for non-linear voltage
    offsets when the battery changes from charge to discharge.
    Selecting this parameter enables these parameters in the
    **Heating and Hysteresis** tab.

    - **Hysteresis Rate,
      HystRate**
    - **Maximum Hysteresis Voltage,
      MaxHystVolt**
    - **Instantaneous Hysteresis Voltage,
      InstHystVolt**
  - **Include entropic heating** — Select
    this option to include power losses that occur during the
    battery phase change. Selecting this parameter enables this
    parameter in the **Heating and Hysteresis**
    tab.

    - **Entropic Coefficient, EntdUdT**
- The **Info** includes these bus signals.

  - `HystState`
  - `HystVolt`
  - `EntropicPwr`
- You can now set the **Number of series RC pairs** to
  `0`. This removes the RC elements from the
  circuit.

## Description

Resistor-capacitor (RC) circuit battery

The Equivalent Circuit Battery block implements
a resistor-capacitor (RC) circuit battery that you can parameterize
using equivalent circuit modeling (ECM). To simulate the state-of-charge
(SOC) and terminal voltage, the block uses load current and internal
core temperature.

The Equivalent Circuit Battery block calculates
the combined voltage of the network battery using parameter lookup
tables. The tables are functions of the SOC and battery temperature.
You can use the Estimation Equivalent Circuit Battery block
to help create the lookup tables.

Specifically, the Equivalent Circuit Battery block implements these parameters
as lookup tables that are functions of the SOC and battery temperature:

- Series resistance,
  *Ro*=ƒ(*SOC*,*T*)
- Battery open-circuit voltage,
  *Em*=ƒ(*SOC*,*T*)
- Battery capacity,
  *Cbatt*=ƒ(*T*)
- Network resistance,
  *Rn*=ƒ(*SOC*,*T*)
- Network capacitance,
  *Cn*=ƒ(*SOC*,*T*)

To calculate the combined voltage of the battery network, the
block uses these equations.

VT=Em−IbattRo−∑1nVnVn=∫0t[IbattCn−VnRnCn]dtSOC=−1Cbatt∫0tIbattdtIbatt=IinNpVout=NsVTPBattLoss=Ibatt2R0+∑1nVn2RnLdAmpHr=∫0tIbattdt

Positive
current indicates battery discharge. Negative current indicates battery
charge.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrLdBatt` | Battery network power | Vbatt=Vout   OR  Voutτs+1Pbatt=−VbattIbattPLdBatt= −Pbatt |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLossBatt` | Battery network power loss | PLossBatt=−(Ibatt2R0+∑1nVn2Rn) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredBatt` | Battery network power stored | PStoredBatt=PBatt+PLossBatt |

The equations use these variables.

|  |  |
| --- | --- |
| *SOC* | State-of-charge |
| *Em* | Battery open-circuit voltage |
| *Ibatt* | Per module battery current |
| *Iin* | Combined current flowing from the battery network |
| *Ro* | Series resistance |
| *Np* | Number parallel branches |
| *Np* | Number of RC pairs in series |
| *Vout*, *VT* | Combined voltage of the battery network |
| *Vn* | Voltage for *`n`*-th RC pair |
| *Rn* | Resistance for *`n`*-th RC pair |
| *Cn* | Capacitance for *`n`*-th RC pair |
| *Cbatt* | Battery capacity |
| *Pbatt* | Battery power |
| *PLossBatt* | Negative of battery network power loss |
| *PBattLoss* | Battery network power loss |
| *PStoredBatt* | Battery network power stored |
| *PLdBatt* | Battery network power |
| *T* | Battery temperature |

### Current Polarity, Hysteresis, and Entropic Heating

To incorporate current polarity, hysteresis voltage, and entropic heating into the
battery model, enable these block parameters:

- **Include current polarity**
- **Include hysteresis**
- **Include entropic heating**

**Current Polarity**

To improve calibration for charging and discharging processes,
select **Include current polarity**. To model the current polarity, the block
implements resistive and capacitive lookup tables with current direction.

**Hysteresis**

Hysteresis voltage adds a state estimator for non-linear
voltage offsets when the battery current changes from charge to discharge. To calculate the
combined voltage of the battery network with hysteresis, select **Include
hysteresis**. The block uses these equations.

Hstate=∫(−Hstate•abs(Ibatt)−Ibatt)•HystRateCbattVHyst=Hstate•MaxHystVolt−InstHystVolt•sign(Ibatt)VT=VHyst+Em−IbattRo−∑1nVn

**Entropic Heating**

Entropic heating accounts for power losses that occur during
the battery phase change. To calculate the battery network power loss with entropic heating,
select **Include entropic heating**. The block uses these equations.

Pentropic=−IBatt•T•EntdUdTPLossBatt=−(Ibatt2R0+∑1nVn2Rn+Pentropic)

The equations use these variables.

|  |  |
| --- | --- |
| *Hstate* | Hysteresis state variable |
| *HystRate* | Hysteresis rate |
| *VHyst* | Hysteresis voltage |
| *MaxHystVolt* | Maximum hysteresis voltage |
| *InstHystVolt* | Instantaneous hysteresis voltage |
| *EntdUdT* | Entropic coefficient |
| *Pentropic* | Entropic reversible losses |
