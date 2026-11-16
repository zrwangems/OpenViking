---
type: simulink-block
title: 'Bidirectional DC-DC'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage and Auxiliary Drive / DC-DC'
documentation_page: 'bidirectionaldcdc'
documentation_source_path: 'ref/bidirectionaldcdc.html'
language: en
---

# Bidirectional DC-DC

## Ports

### Inputs

### **VoltCmd** — Commanded voltage `scalar`

DC-to-DC converter commanded output voltage,
*VoltCmd*, in V.

### **SrcVolt** — Input voltage `scalar`

Source input voltage to DC-to-DC converter,
*SrcVolt*, in V.

### **LdCurr** — Load current `scalar`

Load current of DC-to-DC converter,
*LdAmp*, in A.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `SrcPwr` | | | Source power to DC-to-DC converter | *SrcPwr* | W |
| `LdPwr` | | | Load power from DC-to-DC converter | *LdPwr* | W |
| `PwrLoss` | | | Power loss | *PwrLoss* | W |
| `LdVoltCmd` | | | Commanded load voltage of DC-to-DC converter before application of time constant | *LdVoltCmd* | V |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBusSrc` | Source power to DC-to-DC converter | *Psrc* | W |
| `PwrBusLd` | Load power from DC-to-DC converter | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Converter power loss | *Ploss* | W |
| `PwrStored` | *Not used* | | | |

### **LdVolt** — Load voltage `scalar`

Load voltage of DC-to-DC converter,
*LdVolt*, in V.

### **SrcCurr** — Source current `scalar`

Source current draw from DC-to-DC converter,
*SrcAmp*, in A.

## Parameters

#### Electrical Control

### **Converter response time constant, Tc** — Constant `1/1000` (default) | `scalar`

Converter response time, *τ*, in s.

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

### **Converter response initial voltage, Vinit** — Voltage `0` (default) | `scalar`

Initial load voltage of the DC-to-DC converter,
*Vinit*, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vinit` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Converter power limit, Plimit** — Power `100000` (default) | `scalar`

Initial load voltage of the DC-to-DC converter,
*Plimit*, in W.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Plimit` |
| **Values:** | `100000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Electrical Losses

### **Parameterize losses by** — Loss calculation `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated efficiency data`

This table summarizes the loss options used to calculate electrical
options.

| Parameter Option | Description |
| --- | --- |
| `Single efficiency measurement` | Electrical loss calculated using a constant value for conversion efficiency. |
| `Tabulated loss data` | Electrical loss calculated as a function of load current and voltage. DC-to-DC converter data sheets typically provide loss data in this format. When you use this option, provide data for all the operating quadrants in which the simulation will run. If you provide partial data, the block assumes the same loss pattern for other quadrants. The block does not extrapolate loss that is outside the range voltage and current that you provide. The block allows you to account for fixed losses that are still present for zero voltage or current.  If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 2-D lookup table using measured data. |
| `Tabulated efficiency data` | Electrical loss calculated using conversion efficiency that is a function of load current and voltage. When you use this option, provide data for all the operating quadrants in which the simulation will run. If you provide partial data, the block assumes the same efficiency pattern for other quadrants. The block:  - Assumes zero loss when either the voltage or current is   zero. - Uses linear interpolation to determine the loss. At lower   power conditions, for calculation accuracy, provide efficiency   at low voltage and low current. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `param_loss` |
| **Values:** | `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated efficiency data` |
| **Data Types:** | `character vector` |

### **Overall DC to DC converter efficiency, eff** — Constant `98` (default) | `scalar`

Overall conversion efficiency, *Eff*, in %.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eff` |
| **Values:** | `98` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Single efficiency measurement`.

### **Vector of voltages (v) for tabulated loss, v\_loss\_bp** — Breakpoints `[0 200 400 600 800 1000]` (default) | `1`-by-`M` vector

Tabulated loss breakpoints for `M` load voltages, in
V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `v_loss_bp` |
| **Values:** | `[0 200 400 600 800 1000]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Vector of currents (i) for tabulated loss, i\_loss\_bp** — Breakpoints `[0 25 50 75 100]` (default) | `1`-by-`N` vector

Tabulated loss breakpoints for `N` load currents, in
A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `i_loss_bp` |
| **Values:** | `[0 25 50 75 100]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Corresponding losses, losses\_table** — 2-D lookup table `N`-by-`M` matrix

Electrical loss map, as a function of `N` load currents
and `M` load voltages, in W.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `losses_table` |
| **Values:** | `N`-by-`M` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Vector of voltages (v) for tabulated efficiency, v\_eff\_bp** — Breakpoints `[200 400 600 800 1000]` (default) | `1`-by-`M` vector

Tabulated efficiency breakpoints for `M` load voltages,
in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `v_eff_bp` |
| **Values:** | `[200 400 600 800 1000]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated efficiency data`.

### **Vector of currents (i) for tabulated efficiency, i\_eff\_bp** — Breakpoints `[25 50 75 100]` (default) | `1`-by-`N` vector

Tabulated efficiency breakpoints for `N` load currents,
in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `i_eff_bp` |
| **Values:** | `[25 50 75 100]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated efficiency data`.

### **Corresponding efficiency, efficiency\_table** — 2-D lookup table `N`-by-`M` matrix

Electrical efficiency map, as a function of
`N` load currents and `M` load
voltages, in %.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `efficiency_table` |
| **Values:** | `N`-by-`M` matrix |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated efficiency data`.

### **Calibrate Maps** — Calibrate tables with measured data `selection`

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the lookup table using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/autoblks/autoblksutilities/mbctemplates/MappedDCDCConverterDataset.xlsx`. For more information, see Using Data (Model-Based Calibration Toolbox).  Required data:  - Current, A - Voltage, V - Power loss, W  Collect data at steady-state operating conditions.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | The Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response models and generates calibrated table.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these block lookup table and breakpoint parameters with the calibration.  - **Vector of voltages (v) for tabulated loss, v\_loss\_bp** - **Vector of currents (i) for tabulated loss, i\_loss\_bp** - **Corresponding losses, losses\_table** |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CalLossMapsButton` |
| **Values:** | selection |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

## Libraries

Powertrain Blockset / Energy Storage and Auxiliary Drive / DC-DC

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

DC-to-DC converter that supports bidirectional boost and buck

The Bidirectional DC-DC block implements a DC-to-DC converter that
supports bidirectional boost and buck (lower) operation. Unless the DC-to-DC conversion
limits the power, the output voltage tracks the voltage command. You can specify
electrical losses or measured efficiency.

Depending on your battery system configuration, the voltage might not be at a
potential that is required by electrical system components such has inverters and
motors. You can use the block to boost or buck the voltage. Connect the block to the
battery and one of these blocks:

- Mapped Motor
- IM Controller
- Interior PM Controller
- Surface Mount PM Controller

To calculate the electrical loss during the DC-to-DC conversion, use
**Parameterize losses by**.

| Parameter Option | Description |
| --- | --- |
| `Single efficiency measurement` | Electrical loss calculated using a constant value for conversion efficiency. |
| `Tabulated loss data` | Electrical loss calculated as a function of load current and voltage. DC-to-DC converter data sheets typically provide loss data in this format. When you use this option, provide data for all the operating quadrants in which the simulation will run. If you provide partial data, the block assumes the same loss pattern for other quadrants. The block does not extrapolate loss that is outside the range voltage and current that you provide. The block allows you to account for fixed losses that are still present for zero voltage or current.  If you have Model-Based Calibration Toolbox™, click **Calibrate Maps** to virtually calibrate the 2-D lookup table using measured data. |
| `Tabulated efficiency data` | Electrical loss calculated using conversion efficiency that is a function of load current and voltage. When you use this option, provide data for all the operating quadrants in which the simulation will run. If you provide partial data, the block assumes the same efficiency pattern for other quadrants. The block:  - Assumes zero loss when either the voltage or current is   zero. - Uses linear interpolation to determine the loss. At lower   power conditions, for calculation accuracy, provide efficiency   at low voltage and low current. |

**Note**

The block does not support inversion. The polarity of the input voltage
matches the polarity of the output voltage.

### Theory

The Bidirectional DC-DC block uses the commanded voltage and the
actual voltage to determine whether to boost or buck (lower) the voltage. You can
specify a time constant for the voltage response.

| If | Then |
| --- | --- |
| *Voltcmd* > *SrcVolt* | Boost |
| *Voltcmd* < *SrcVolt* | Buck |

The Bidirectional DC-DC block uses a time constant-based regulator
to provide a fixed output voltage that is independent of load current. Using the
output voltage and current, the block determines the losses of the DC-to-DC
conversion. The block uses the conversion losses to calculate the input current. The
block accounts for:

- Bidirectional current flow

  - Source to load — Battery discharge
  - Load to source — Battery charge
- Rated power limits

The block provides voltage control that is power limited based on these equations.
The voltage is fixed. The block does not implement a voltage drop because the load
current approximates DC-to-DC conversion with a bandwidth that is greater than the
load current draw.

|  |  |
| --- | --- |
| DC-to-DC converter load voltage | LdVoltCmd=min(VoltCmd,PlimitLdAmp,0)LdVolt=LdVoltCmd⋅1τs+1 |
| Power loss for single efficiency source to load | PwrLoss=100−EffEff⋅LdVolt⋅LdAmp |
| Power loss for single efficiency load to source | PwrLoss=100−EffEff⋅|LdVolt⋅LdAmp| |
| Power loss for tabulated efficiency | PrwLoss=f(LdVolt,LdAmp) |
| Source current draw from DC-to-DC converter | SrcAmp=LdPwr+PrwLossSrcVolt |
| Source power from DC-to-DC converter | SrcPwr=SrcAmp⋅SrcVolt |

### Virtual Calibration

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the lookup table using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/autoblks/autoblksutilities/mbctemplates/MappedDCDCConverterDataset.xlsx`. For more information, see Using Data (Model-Based Calibration Toolbox).  Required data:  - Current, A - Voltage, V - Power loss, W  Collect data at steady-state operating conditions.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | The Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response models and generates calibrated table.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these block lookup table and breakpoint parameters with the calibration.  - **Vector of voltages (v) for tabulated loss, v\_loss\_bp** - **Vector of currents (i) for tabulated loss, i\_loss\_bp** - **Corresponding losses, losses\_table** |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrBusSrc` | Source power to DC-to-DC converter | *Psrc* | Psrc= SrcPwr |
| `PwrBusLd` | Load power from DC-to-DC converter | *Pbus* | Pbus= −LdVolt |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLoss` | Converter power loss | *Ploss* | Ploss= PwrLoss |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | | *Not used* | | |

The equations use these variables.

|  |  |
| --- | --- |
| *VoltCmd* | DC-to-DC converter commanded output voltage |
| *SrcVolt* | Source input voltage to DC-to-DC converter |
| *LdAmp* | Load current of DC-to-DC converter |
| *LdVolt* | Load voltage of DC-to-DC converter |
| *SrcAmp* | Source current draw from DC-to-DC converter |
| *τ* | Conversion time constant |
| *Vinit* | Initial load voltage of the DC-to-DC converter |
| *Plimit* | Output power limit for DC-to-DC converter |
| *Eff* | Input to output efficiency |
| *SrcPwr* | Source power to DC-to-DC converter |
| *LdPwr* | Load power from DC-to-DC converter |
| *PwrLoss* | Power loss |
| *LdVoltCmd* | Commanded load voltage of DC-to-DC converter before application of time constant |
