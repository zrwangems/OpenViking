---
type: simulink-block
title: 'Mapped Motor'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors, Inverters, and Controllers'
documentation_page: 'mappedmotor'
documentation_source_path: 'ref/mappedmotor.html'
language: en
---

# Mapped Motor

## Ports

### Input

### **BattVolt** — Battery voltage scalar

Supplied voltage, *BattVolt*, in volts (DC).

### **TrqCmd** — Commanded motor torque scalar

Commanded motor torque,
*Trqcmd*, in N·m.

### **LdTrq** — Motor load torque scalar

Motor load torque, *Tload*, in
N·m.

#### Dependencies

To enable this port, set **Port configuration**
to `Torque`.

### **MtrSpd** — Motor output shaft speed scalar

Motor shaft speed, *Mtrspd*,
in rad/s.

#### Dependencies

To enable this port, set **Port configuration**
to `Speed`.
### Output

### **Info** — Bus signal bus

The bus signal contains these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `MtrTrq` | | | Motor output shaft torque | N·m |
| `MechPwr` | | | Mechanical power | W |
| `PwrLoss` | | | Internal inverter and motor power loss | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | Mechanical power | W |
| `PwrBus` | Electrical power | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Motor power loss | W |
| `PwrStored` | `PwrStoredShft` | Motor power stored | W |

### **BattCurr** — Battery current scalar

Supplied current draw or demand,
*Ibatt*, in amperes
(DC).

### **MtrTrq** — Motor torque scalar

Motor output shaft torque,
*Mtrtrq*, in N·m.

#### Dependencies

To enable this port, set **Port configuration**
to `Speed`.

### **MtrSpd** — Motor shaft speed scalar

Motor shaft speed, *Mtrspd*,
in rad/s.

#### Dependencies

To enable this port, set **Port configuration**
to `Torque`.

## Parameters

#### Block Options

### **Port configuration** — Port configuration `Torque` (default) | `Speed`

This table summarizes the port configurations.

| Port Configuration | Enables Ports |
| --- | --- |
| `Torque` | - Input `LdTrq` - Outport `MtrSpd` |
| `Speed` | - Input `MtrSpd` - Outport `MtrTrq` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **Values:** | `Torque` (default) | `Speed` |
| **Data Types:** | `character vector` |

### **Import Torque Limits Calibration** — Method to directly import torque limits calibration tables selection

If you have your own torque-speed-voltage envelope calibration,
you can directly import it. This table steps through the tasks.

| Task | Description |
| --- | --- |
| Select parameterization | On the **Electrical Torque** tab, set **Parameterized by** to `Tabulated torque-speed-voltage envelope`. |
| Select electrical torque calibration data file | Navigate to the calibration data file folder, for example, `<matlabroot>/toolbox/autoblks/`.  Select the calibration data file, for example, `MotorCalibrationImportData.xlsx`.  Click **Open**. |
| Import torque limits data | Click **Import Torque Limits Calibration**. The block reads and imports the data in the spreadsheet **MaxTorque** and **MinTorque** tabs. |

### **Calibrate Maps** — Method to calibrate loss table with measured data selection

If you have Model-Based Calibration Toolbox, you can virtually calibrate a 2-D or 3-D measured loss lookup table.

1. On the **Electrical Losses** tab, set **Parameterize
   losses by** to either:

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. Click **Calibrate Maps**.

The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import loss data | Import loss data from a file, for example, open `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).    | **Parameterize losses by** | Required Data | | --- | --- | | `Tabulated loss data` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `Tabulated loss data with temperature` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  Collect motor data at steady-state operating conditions. Data should cover the motor speed, torque, and temperature operating range.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response model and generates the calibrated table.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these parameters with the calibration.  | **Parameterize losses by** | Parameters | | --- | --- | | `Tabulated loss data` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Loss table,   losses\_table** | | `Tabulated loss data with temperature` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Temperature breakpoints for   losses, Temp\_eff\_bp** - **Loss table,   losses\_table\_3d** | |

### **Import Loss Calibration** — Method to directly import loss calibration table selection

If you have your own loss calibration versus torque, speed,
supplied DC voltage, and temperature, you can directly import it. This table steps through the
tasks.

| Task | Description |
| --- | --- |
| Select parameterization | On the **Electrical Losses** tab, set **Parameterize losses by** to `Tabulated loss data with temperature and voltage`. |
| Select calibration data file | Navigate to the calibration data file folder, for example, `<matlabroot>/toolbox/autoblks/`.  Select the calibration data file, for example, `MotorCalibrationImportData.xlsx`.  Click **Open**. |
| Import loss data | Click **Import Loss Calibration**. The block reads and imports the data in the spreadsheet **PowerLoss** tab. |

### **Import Efficiency Calibration** — Method to directly import efficiency calibration table selection

If you have your own efficiency calibration versus torque,
speed, supplied DC voltage, and temperature, you can directly import it. This table steps
through the tasks.

| Task | Description |
| --- | --- |
| Select parameterization | On the **Electrical Losses** tab, set **Parameterize losses by** to `Tabulated efficiency data with temperature and voltage`. |
| Select calibration data file | Navigate to the calibration data file folder, for example, `<matlabroot>/toolbox/autoblks/`.  Select the calibration data file, for example, `MotorCalibrationImportData.xlsx`.  Click **Open**. |
| Import efficiency data | Click **Import Efficiency Calibration**. The block reads and imports the data in the spreadsheet **Efficiency** tab. |

#### Electrical Torque

### **Parameterized by** — Parameterization method for torque envelope `Tabulated torque-speed envelope` (default) | `Maximum torque and power` | `Tabulated torque-speed-voltage envelope`

| Setting | Block Implementation |
| --- | --- |
| `Tabulated torque-speed envelope` | Range specified as a set of shaft speed data points with corresponding maximum torque values. Minimum torque is set to the negative of maximum torque. |
| `Maximum torque and power` | Range specified using the maximum torque and maximum power values. |
| `Tabulated torque-speed-voltage envelope` | Range specified as a set of speed and supplied DC voltage data points with their corresponding maximum and minimum torque values.  To directly import your own torque-limits calibration tables, click **Import Torque Limits Calibration**. |

For any of these methods, the block implements a torque envelope similar
to the one in this figure. If **Parameterized by** is set to
`Tabulated torque-speed-voltage envelope`, the envelope
adds supplied DC voltage as a third axis.

Plot of torque envelope versus speed, indicating permissible steady-state operation

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `param_by` |
| **Values:** | `Tabulated torque-speed envelope` (default) | `Maximum torque and power` | `Tabulated torque-speed-voltage envelope` |
| **Data Types:** | `character vector` |

### **Speed breakpoints for maximum torque, w\_t** — Rotational speeds `[0 375 750 800]` (default) | vector

Rotational speeds spanning permissible steady-state range, in rad/s. To
avoid poor performance due to an infinite slope in the torque-speed curve,
specify a vector of rotational speed breakpoints that does not contain
duplicate consecutive values.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_t` |
| **Values:** | `[0 375 750 800]` (default) | vector |
| **Data Types:** | `double` |

### **Maximum torque values, T\_t** — Torque `[0.09 0.08 0.07 0]` (default) | vector

Maximum permissible torque values, in N·m.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_t` |
| **Values:** | `[0.09 0.08 0.07 0]` (default) | vector |
| **Data Types:** | `double` |

### **Maximum torque, torque\_max** — Torque `0.1` (default) | scalar

The maximum permissible motor torque, in N·m.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Maximum torque and power`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `torque_max` |
| **Values:** | `0.1` (default) | scalar |
| **Data Types:** | `double` |

### **Maximum power, power\_max** — Power `30` (default) | scalar

The maximum permissible motor power, in W.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Maximum torque and power`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `power_max` |
| **Values:** | `30` (default) | scalar |
| **Data Types:** | `double` |

### **Torque control time constant, Tc** — Time constant `0.02` (default) | scalar

Time constant with which the motor driver tracks a torque demand, in
s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tc` |
| **Values:** | `0.02` (default) | scalar |
| **Data Types:** | `double` |

### **Maximum torque as a function of speed and voltage, Tmax\_w\_V** — Torque `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]` (default) | vector

Maximum permissible torque, including sign, at a given set of speed and
supplied DC voltage breakpoints, in N·m.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed-voltage
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tmax_w_V` |
| **Values:** | `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]` (default) | vector |
| **Data Types:** | `double` |

### **Speed breakpoints for maximum torque, w\_Tmax\_bp** — Rotational speeds `[ 0 375 750 800 ]` (default) | vector

Speed at each value of maximum torque, in rad/s.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed-voltage
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_Tmax_bp` |
| **Values:** | `[ 0 375 750 800 ]` (default) | vector |
| **Data Types:** | `double` |

### **Voltage breakpoints for maximum torque, V\_Tmax\_bp** — Voltage `[ 500 750 900 ]` (default) | vector

Supplied DC voltage at each value of maximum torque, in volts (DC).

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed-voltage
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `V_Tmax_bp` |
| **Values:** | `[ 500 750 900 ]` (default) | vector |
| **Data Types:** | `double` |

### **Minimum torque as a function of speed and voltage, Tmin\_w\_V** — Torque `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]` (default) | vector

Minimum permissible torque, including sign, at a given set of speed and
supplied DC voltage breakpoints, in N·m.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed-voltage
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tmin_w_V` |
| **Values:** | `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]` (default) | vector |
| **Data Types:** | `double` |

### **Speed breakpoints for minimum torque, w\_Tmin\_bp** — Rotational speeds `[ 0 375 750 800 ]` (default) | vector

Speed at each value of minimum torque, in rad/s.

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed-voltage
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_Tmin_bp` |
| **Values:** | `[ 0 375 750 800 ]` (default) | vector |
| **Data Types:** | `double` |

### **Voltage breakpoints for minimum torque, V\_Tmin\_bp** — Voltage `[ 500 750 900 ]` (default) | vector

Supplied DC voltage at each value of minimum torque, in volts (DC).

#### Dependencies

To create this parameter, for **Parameterized by**,
select `Tabulated torque-speed-voltage
envelope`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `V_Tmin_bp` |
| **Values:** | `[ 500 750 900 ]` (default) | vector |
| **Data Types:** | `double` |

#### Electrical Losses

### **Parameterize losses by** — Parameterization method for electrical losses `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage`

| Setting | Block Implementation |
| --- | --- |
| `Single efficiency measurement` | Efficiency calculated using three loss terms. One term is constant, and measured at zero speed and torque:    - Fixed losses independent of torque and speed,   *P*0. Use   *P*0 to account   for fixed converter losses.    Two terms depend on operating conditions. The block determines their coefficients from the efficiency *η*0 measured at an efficiency setpoint, where motor torque is *τ*0 and motor speed is *ω*0:    - A torque-dependent electrical loss *k**τ*2, where *k* is a constant   and *τ* is the torque. This term represents   ohmic losses in the copper windings. - A speed-dependent electrical loss *kw**ω*2, where   *kw* is a   constant and *ω* is the speed. This term   represents iron losses due to eddy currents. |
| `Tabulated loss data` | Loss calibration lookup table that is a function of motor speed and load torque.  If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 2-D lookup table using measured data. |
| `Tabulated loss data with temperature` | Loss calibration lookup table that is a function of motor speed, load torque, and operating temperature.  If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 3-D lookup table using measured data. |
| `Tabulated loss data with temperature and voltage` | Loss calibration lookup table that is a function of load torque, motor speed, supplied DC voltage, and operating temperature.  To directly import your own 4-D loss calibration table, click **Import Loss Calibration**. |
| `Tabulated efficiency data` | 2-D efficiency calibration lookup table that is a function of motor speed and load torque. The block:  - Converts the efficiency values you provide into losses and   uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or   zero torque. Losses are assumed zero when either torque or   speed is zero. - Uses linear interpolation to determine losses. Provide   tabulated data for low speed and low torque values, as   required, to get the desired level of accuracy for lower   power conditions. - Does not extrapolate loss values for speed and torque   magnitudes that exceed the range of the table. |
| `Tabulated efficiency data with temperature` | 3-D efficiency calibration lookup table that is a function of motor speed, load torque, and operating temperature. The block:    - Converts the efficiency values you provide into losses and   uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or   zero torque. Losses are assumed zero when either torque or   speed is zero. - Uses linear interpolation to determine losses. Provide   tabulated data at low speed and low torque values, as   required, to get the desired level of accuracy for lower   power conditions. - Does not extrapolate loss values for speed, torque, or   temperature magnitudes that exceed the range of the   table. |
| `Tabulated efficiency data with temperature and voltage` | Efficiency calibration lookup table that is a function of load torque, motor speed, supplied DC voltage, and operating temperature.  To directly import your own 4-D efficiency calibration table, click **Import Efficiency Calibration**. The block:  - Converts the efficiency values you provide into losses and   uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or zero   torque. Losses are assumed zero when either torque or speed is   zero. - Uses linear interpolation to determine losses. Provide   tabulated data for low speed and low torque values, as required,   to get the desired level of accuracy for lower power   conditions. - Does not extrapolate loss values for speed, torque,   temperature, or voltage magnitudes that exceed the range of the   table. |

As a best practice, use `Tabulated loss data`,
`Tabulated loss data with temperature`, or `Tabulated
loss data with temperature and voltage` instead of `Tabulated
efficiency data`, `Tabulated efficiency data with
temperature`, or `Tabulated efficiency data with temperature and
voltage`:

- Efficiency becomes ill-defined for zero speed or zero torque.
- You can account for fixed losses that are still present for zero speed or torque.

**Note**

Due to losses, the motor drive system can draw a current when the motor torque is
zero.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `param_loss` |
| **Values:** | `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage` |
| **Data Types:** | `character vector` |

### **Motor and drive overall efficiency, eff** — Combined efficiency *η*0 of the motor and motor drive, measured at the efficiency setpoint, in percent `100` (default) | scalar

At the efficiency setpoint, the motor torque is
*τ*0 and motor speed is
*ω*0. The efficiency measured in
this condition is *η*0.

The block defines overall efficiency percentage during operation as:

η=100τωτω+P0+kτ2+kwω2

The equation uses these variables.

|  |  |
| --- | --- |
| *τ* | Motor torque |
| *ω* | Motor speed |
| *P*0 | Fixed losses independent of torque or speed, measured as the base loss at zero motor torque and speed |
| kτ2 | Torque-dependent electrical losses |
| *kw**ω2* | Speed-dependent iron losses, *PIron* = *kw**ω2* |

At initialization, the block sets the value for
*kw* from the iron-loss
equation, using the iron losses measured at the efficiency setpoint torque
*τ*0 and speed
*ω*0:

PIron,0=kwω02

The block then sets the value for *k* from the efficiency
equation, using the value for efficiency
*η*0 measured at the efficiency setpoint:

η0=100τ0ω0τ0ω0+P0+kτ02+kwω02

The block neglects losses associated with rotor damping.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Single efficiency
measurement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eff` |
| **Values:** | `100` (default) | scalar |
| **Data Types:** | `double` |

### **Speed at which efficiency is measured, w\_eff** — Speed `375` (default) | scalar

Motor speed *ω0* at the efficiency
setpoint, in rad/s.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Single efficiency
measurement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_eff` |
| **Values:** | `375` (default) | scalar |
| **Data Types:** | `double` |

### **Torque at which efficiency is measured, T\_eff** — Torque `0.08` (default) | scalar

Torque *τ0* at the efficiency
setpoint, in N·m.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Single efficiency
measurement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_eff` |
| **Values:** | `0.08` (default) | scalar |
| **Data Types:** | `double` |

### **Iron losses, Piron** — Power `0` (default) | scalar

Iron losses
*PIron*,0
at the efficiency setpoint, in W.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Single efficiency
measurement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Piron` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Fixed losses independent of torque and speed, Pbase** — Power `0` (default) | scalar

Constant component *P*0 of power
loss associated with the motor drive, evaluated at zero torque and speed, in
W.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Single efficiency
measurement`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Pbase` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Speed breakpoints for losses, w\_eff\_bp** — Breakpoints `[-800 -400 0 400 800]` (default) | `1`-by-`M` vector

Speed breakpoints for loss lookup table, in rad/s. Array dimensions are
`1` by the number of speed breakpoints
`M`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select one of these options:

- `Tabulated loss data`
- `Tabulated loss data with
  temperature`
- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency
  data`
- `Tabulated efficiency data with
  temperature`
- `Tabulated efficiency data with temperature
  and voltage`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_eff_bp` |
| **Values:** | `[-800 -400 0 400 800]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

### **Torque breakpoints for losses, T\_eff\_bp** — Breakpoints `[0 0.03 0.06 0.09]` (default) | `1`-by-`N` vector

Torque breakpoints for loss lookup table, in N·m. Array dimensions are
`1` by the number of torque breakpoints
`N`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select one of these options:

- `Tabulated loss data`
- `Tabulated loss data with
  temperature`
- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency
  data`
- `Tabulated efficiency data with
  temperature`
- `Tabulated efficiency data with temperature
  and voltage`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_eff_bp` |
| **Values:** | `[0 0.03 0.06 0.09]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

### **Temperature breakpoints for losses, Temp\_eff\_bp** — Breakpoints `[233.15 293.15 373.15]` (default) | `1`-by-`L` vector

Temperature breakpoints for loss lookup table, in K. Array dimensions are
`1` by the number of temperature breakpoints
`L`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select one of these options:

- `Tabulated loss data with
  temperature`
- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency data with
  temperature`
- `Tabulated efficiency data with temperature
  and voltage`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temp_eff_bp` |
| **Values:** | `[233.15 293.15 373.15]` (default) | `1`-by-`L` vector |
| **Data Types:** | `double` |

### **Voltage breakpoints for losses, V\_eff\_bp** — Breakpoints `[500 700 900]` (default) | `1`-by-`K` vector

Voltage breakpoints for loss lookup table, in volts. Array dimensions are
`1` by the number of voltage breakpoints
`K`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select one of these options:

- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency data with temperature
  and voltage`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `V_eff_bp` |
| **Values:** | `[500 700 900]` (default) | `1`-by-`K` vector |
| **Data Types:** | `double` |

### **Loss table, losses\_table** — 2-D lookup table `M`-by-`N` matrix

Array of values for electrical losses as a function of speed and torque,
in W. Each value specifies the losses for a specific combination of speed
and torque. The array dimensions must match the breakpoint vector dimensions
for speed `M` and torque `N`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Tabulated loss
data`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `losses_table` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

### **Loss table, losses\_table\_3d** — 3-D lookup table `M`-by-`N`-by-`L` array

Array of values for electrical losses as a function of speed, torque, and
temperature, in W. Each value specifies the losses for a specific
combination of speed, torque, and temperature. The array dimensions must
match the breakpoint vector dimensions for speed `M`,
torque `N`, and temperature `L`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Tabulated loss data with
temperature`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `losses_table_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

### **Loss table, losses\_table\_4d** — 4-D lookup table `N`-by-`M`-by-`K`-by-`L` array

Array of values for electrical losses as a function of speed, torque,
temperature, and supplied DC voltage, in W. Each value specifies the losses
for a specific combination of speed, torque, temperature, and supplied DC
voltage. The array dimensions must match the breakpoint vector dimensions
for torque `N`, speed `M`, voltage
`K`, and temperature `L`.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Tabulated loss data with
temperature and voltage`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `losses_table_4d` |
| **Values:** | `N`-by-`M`-by-`K`-by-`L` array |
| **Data Types:** | `double` |

### **Efficiency table, efficiency\_table** — 2-D lookup table `M`-by-`N` matrix

Array of efficiency as a function of speed and torque, in percent. Each
value specifies the losses for a specific combination of speed and torque.
The array dimensions must match the breakpoint vector dimensions for speed
`M`, and torque `N`.

The block ignores efficiency values for zero speed or zero torque. Losses
are zero when either torque or speed is zero. The block uses linear
interpolation.

To get the desired level of accuracy for lower power conditions, you can
provide tabulated data for low speed and low torque values.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Tabulated efficiency
data`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `efficiency_table` |
| **Values:** | `M`-by-`N` matrix |
| **Data Types:** | `double` |

### **Efficiency table, efficiency\_table\_3d** — 3-D lookup table `M`-by-`N`-by-`L` array

Array of efficiency as a function of speed, torque, and temperature, in
percent. Each value specifies the losses for a specific combination of
speed, torque, and temperature. The array dimensions must match the
breakpoint vector dimensions for speed `M`, torque
`N`, and temperature `L`.

The block ignores efficiency values for zero speed or zero torque. Losses
are zero when either torque or speed is zero. The block uses linear
interpolation.

To get the desired level of accuracy for lower power conditions, you can
provide tabulated data for low speed and low torque values.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Tabulated efficiency data with
temperature`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `efficiency_table_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `character vector` |

### **Efficiency table, efficiency\_table\_4d** — 4-D lookup table `N`-by-`M`-by-`K`-by-`L` array

Array of efficiency as a function of speed, torque, temperature, and
supplied DC voltage, in percent. Each value specifies the losses for a
specific combination of speed, torque, temperature, and supplied DC voltage.
The array dimensions must match the breakpoint vector dimensions for torque
`N`, speed `M`, voltage
`K`, and temperature `L`.

The block ignores efficiency values for zero speed or zero torque. Losses
are zero when either torque or speed is zero. The block uses linear
interpolation.

To get the desired level of accuracy for lower power conditions, you can
provide tabulated data for low speed and low torque values.

#### Dependencies

To create this parameter, for **Parameterize losses
by**, select `Tabulated efficiency data with
temperature and voltage`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `efficiency_table_4d` |
| **Values:** | `N`-by-`M`-by-`K`-by-`L` array |
| **Data Types:** | `double` |

#### Mechanical

### **Rotor inertia, J** — Inertia `5e-6` (default) | scalar

Rotor resistance to change in angular velocity, in
kg·m2. You can set the value to zero.

#### Dependencies

To create this parameter, set **Port configuration**
to `Torque`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J` |
| **Values:** | `5e-6` (default) | scalar |
| **Data Types:** | `double` |

### **Rotor damping, b** — Damping `1e-5` (default) | scalar

Rotor damping, in N·m/(rad/s). You can set the value to zero.

#### Dependencies

To create this parameter, set **Port configuration**
to `Torque`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b` |
| **Values:** | `1e-5` (default) | scalar |
| **Data Types:** | `double` |

### **Initial rotor speed, omega\_o** — Speed `0` (default) | scalar

Rotor speed at the start of the simulation, in rad/s.

#### Dependencies

To create this parameter, set **Port configuration**
to `Torque`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_o` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Propulsion / Electric Motors and Inverters Vehicle Dynamics Blockset / Powertrain / Propulsion

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2025a: Import motor load torque

R2025a introduces the motor load torque input port `LdTrq`. To
enable the port, set **Port configuration** to
`Torque`.

The motor output shaft torque, `MtrTrq`, is output in the Info
bus.

### R2024b: Directly import calibration tables for mapped motors

Starting in R2024b, to improve calibration workflows, you can directly import
mapped motor calibration tables into a Mapped Motor block as a
function of four parameters:

- Motor torque
- Motor speed
- Supplied voltage
- Motor temperature

On the block mask, set **Port Configuration** to
`Torque`, click the **Electrical
Losses** tab, and set **Parameterize losses
by:** to `Tabulated loss data with temperature and
voltage`. Then, click **Import
Calibration**.

## Description

Mapped motor and drive electronics operating in torque-control mode

The Mapped Motor block implements a mapped motor and drive electronics
operating in torque-control mode. The output torque tracks the torque reference demand
while including a time constant for the combined motor and motor drive. Use the block
for fast system-level simulations when you do not know detailed physical parameters of
the motor, for example, for motor power and torque tradeoff studies. Depending on your
needs, you can use maps having different levels of detail.

You can specify:

- Port configuration — Input torque or motor shaft speed.
- Electrical torque range — Parameterize by a torque-speed envelope,
  maximum motor power and torque, or a torque-speed-voltage envelope. If you
  have your own torque torque-speed-voltage envelope, you can directly import
  it.
- Electrical loss — Parameterize by using either a single measured
  operating point, a measured loss table, or a measured efficiency table. If
  you have Model-Based Calibration Toolbox™, you can virtually calibrate the measured loss table. If you
  have your own calibration table, you can directly import it.

Wherever voltage is used in calibration tables, it refers to the DC voltage supplied
to the motor drive electronics.

### Electrical Torque

To specify the range of torque that the block allows, on the **Electrical
Torque** tab, for **Parameterized by**, select one of
these options.

| Setting | Block Implementation |
| --- | --- |
| `Tabulated torque-speed envelope` | Range specified as a set of shaft speed data points with corresponding maximum torque values. Minimum torque is set to the negative of maximum torque. |
| `Maximum torque and power` | Range specified using the maximum torque and maximum power values. |
| `Tabulated torque-speed-voltage envelope` | Range specified as a set of speed and supplied DC voltage data points with their corresponding maximum and minimum torque values.  To directly import your own torque-limits calibration tables, click **Import Torque Limits Calibration**. |

For any of these methods, the block implements a torque envelope similar
to the one in this figure. If **Parameterized by** is set to
`Tabulated torque-speed-voltage envelope`, the envelope
adds supplied DC voltage as a third axis.

Plot of torque envelope versus speed, indicating permissible steady-state operation

### Direct Import of Electrical Torque

If you have your own torque-speed-voltage envelope calibration,
you can directly import it. This table steps through the tasks.

| Task | Description |
| --- | --- |
| Select parameterization | On the **Electrical Torque** tab, set **Parameterized by** to `Tabulated torque-speed-voltage envelope`. |
| Select electrical torque calibration data file | Navigate to the calibration data file folder, for example, `<matlabroot>/toolbox/autoblks/`.  Select the calibration data file, for example, `MotorCalibrationImportData.xlsx`.  Click **Open**. |
| Import torque limits data | Click **Import Torque Limits Calibration**. The block reads and imports the data in the spreadsheet **MaxTorque** and **MinTorque** tabs. |

### Electrical Losses

To specify the electrical losses, on the **Electrical Losses**
tab, for **Parameterize losses by**, select one of these
options.

| Setting | Block Implementation |
| --- | --- |
| `Single efficiency measurement` | Efficiency calculated using three loss terms. One term is constant, and measured at zero speed and torque:    - Fixed losses independent of torque and speed,   *P*0. Use   *P*0 to account   for fixed converter losses.    Two terms depend on operating conditions. The block determines their coefficients from the efficiency *η*0 measured at an efficiency setpoint, where motor torque is *τ*0 and motor speed is *ω*0:    - A torque-dependent electrical loss *k**τ*2, where *k* is a constant   and *τ* is the torque. This term represents   ohmic losses in the copper windings. - A speed-dependent electrical loss *kw**ω*2, where   *kw* is a   constant and *ω* is the speed. This term   represents iron losses due to eddy currents. |
| `Tabulated loss data` | Loss calibration lookup table that is a function of motor speed and load torque.  If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 2-D lookup table using measured data. |
| `Tabulated loss data with temperature` | Loss calibration lookup table that is a function of motor speed, load torque, and operating temperature.  If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the 3-D lookup table using measured data. |
| `Tabulated loss data with temperature and voltage` | Loss calibration lookup table that is a function of load torque, motor speed, supplied DC voltage, and operating temperature.  To directly import your own 4-D loss calibration table, click **Import Loss Calibration**. |
| `Tabulated efficiency data` | 2-D efficiency calibration lookup table that is a function of motor speed and load torque. The block:  - Converts the efficiency values you provide into losses and   uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or   zero torque. Losses are assumed zero when either torque or   speed is zero. - Uses linear interpolation to determine losses. Provide   tabulated data for low speed and low torque values, as   required, to get the desired level of accuracy for lower   power conditions. - Does not extrapolate loss values for speed and torque   magnitudes that exceed the range of the table. |
| `Tabulated efficiency data with temperature` | 3-D efficiency calibration lookup table that is a function of motor speed, load torque, and operating temperature. The block:    - Converts the efficiency values you provide into losses and   uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or   zero torque. Losses are assumed zero when either torque or   speed is zero. - Uses linear interpolation to determine losses. Provide   tabulated data at low speed and low torque values, as   required, to get the desired level of accuracy for lower   power conditions. - Does not extrapolate loss values for speed, torque, or   temperature magnitudes that exceed the range of the   table. |
| `Tabulated efficiency data with temperature and voltage` | Efficiency calibration lookup table that is a function of load torque, motor speed, supplied DC voltage, and operating temperature.  To directly import your own 4-D efficiency calibration table, click **Import Efficiency Calibration**. The block:  - Converts the efficiency values you provide into losses and   uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or zero   torque. Losses are assumed zero when either torque or speed is   zero. - Uses linear interpolation to determine losses. Provide   tabulated data for low speed and low torque values, as required,   to get the desired level of accuracy for lower power   conditions. - Does not extrapolate loss values for speed, torque,   temperature, or voltage magnitudes that exceed the range of the   table. |

As a best practice, use `Tabulated loss data`,
`Tabulated loss data with temperature`, or `Tabulated
loss data with temperature and voltage` instead of `Tabulated
efficiency data`, `Tabulated efficiency data with
temperature`, or `Tabulated efficiency data with temperature and
voltage`:

- Efficiency becomes ill-defined for zero speed or zero torque.
- You can account for fixed losses that are still present for zero speed or torque.

**Note**

Due to losses, the motor drive system can draw a current when the motor torque is
zero.

### Virtual Calibration of Electrical Losses

If you have Model-Based Calibration Toolbox, you can virtually calibrate a 2-D or 3-D measured loss lookup table.

1. On the **Electrical Losses** tab, set **Parameterize
   losses by** to either:

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. Click **Calibrate Maps**.

The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import loss data | Import loss data from a file, for example, open `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).    | **Parameterize losses by** | Required Data | | --- | --- | | `Tabulated loss data` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `Tabulated loss data with temperature` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  Collect motor data at steady-state operating conditions. Data should cover the motor speed, torque, and temperature operating range.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate response models | Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate calibration | Model-Based Calibration Toolbox calibrates the response model and generates the calibrated table.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these parameters with the calibration.  | **Parameterize losses by** | Parameters | | --- | --- | | `Tabulated loss data` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Loss table,   losses\_table** | | `Tabulated loss data with temperature` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Temperature breakpoints for   losses, Temp\_eff\_bp** - **Loss table,   losses\_table\_3d** | |

### Direct Import of Electrical Losses

If you have your own loss calibration versus torque, speed,
supplied DC voltage, and temperature, you can directly import it. This table steps through the
tasks.

| Task | Description |
| --- | --- |
| Select parameterization | On the **Electrical Losses** tab, set **Parameterize losses by** to `Tabulated loss data with temperature and voltage`. |
| Select calibration data file | Navigate to the calibration data file folder, for example, `<matlabroot>/toolbox/autoblks/`.  Select the calibration data file, for example, `MotorCalibrationImportData.xlsx`.  Click **Open**. |
| Import loss data | Click **Import Loss Calibration**. The block reads and imports the data in the spreadsheet **PowerLoss** tab. |

### Direct Import of Electrical Efficiency

If you have your own efficiency calibration versus torque,
speed, supplied DC voltage, and temperature, you can directly import it. This table steps
through the tasks.

| Task | Description |
| --- | --- |
| Select parameterization | On the **Electrical Losses** tab, set **Parameterize losses by** to `Tabulated efficiency data with temperature and voltage`. |
| Select calibration data file | Navigate to the calibration data file folder, for example, `<matlabroot>/toolbox/autoblks/`.  Select the calibration data file, for example, `MotorCalibrationImportData.xlsx`.  Click **Open**. |
| Import efficiency data | Click **Import Efficiency Calibration**. The block reads and imports the data in the spreadsheet **Efficiency** tab. |

### Battery Current

The block calculates the battery current using the mechanical power, power loss,
and battery voltage. Positive current indicates battery discharge. Negative current
indicates battery charge.

BattAmp=MechPwr+PwrLossBattVolt

The equation uses these variables.

|  |  |
| --- | --- |
| *BattVolt* | DC voltage into motor drive electronics |
| *MechPwr* | Mechanical power |
| *PwrLoss* | Power loss |
| *BattCurr* | DC current into motor drive electronics |

### Power Accounting

For power accounting, the block implements these equations.

| Bus Signal | | | Description | Definition | Units |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd`  - Positive signals indicate power flow into the   block. - Negative signals indicate power flow out of   the block. | `PwrMtr` | Mechanical power | **Port configuration** setting:  - `Torque`: Pmot= Tloadω    - `Speed`: Pmot= −Teω | W |
| `PwrBus` | Electrical power | Pbus= BattVolt×BattAmp | W |
| `PwrNotTrnsfrd`  - Negative signals indicate power loss to   heat. | `PwrLoss` | Motor power loss — includes electrical and mechanical losses | Ploss,total= PwrLoss+PdWhere Pd=−bω2 | W |
| `PwrStored`  - Positive value indicates kinetic energy   increase. | `PwrStoredShft` | Rotor kinetic energy storage rate | Pstored= Jω˙ω | W |

The equations use these variables.

|  |  |
| --- | --- |
| *Te* | Motor torque applied to shaft, assuming constant rotor speed |
| *Tload* | Motor torque load |
| *ω* | Rotor speed |
| *b* | Rotational damping coefficient |
| *J* | Rotor inertia |
| *Pd* | Damping loss separate from any in loss table |
| *Ploss,total* | Total losses to heat, equal to `PwrNotTrnsfrd` |
