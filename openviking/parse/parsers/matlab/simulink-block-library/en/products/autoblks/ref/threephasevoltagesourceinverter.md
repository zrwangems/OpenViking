---
type: simulink-block
title: 'Three-Phase Voltage Source Inverter'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors, Inverters, and Controllers'
documentation_page: 'threephasevoltagesourceinverter'
documentation_source_path: 'ref/threephasevoltagesourceinverter.html'
language: en
---

# Three-Phase Voltage Source Inverter

## Ports

### Input

### **PhaseVoltCmd** — Phase a, b, c line-to-neutral voltage command `1`-by-`3` array

Phase a, b, c line-to-neutral voltage command,
*Va\_cmd*,
*Vb\_cmd*, and
*Vc\_cmd*, in V.

#### Dependencies

To create this port, set **Switching voltage
function** to `Commanded phase
voltage`.

### **SwitchCmd** — Switch commands `1`-by-`3` array

Switch commands, *Sa*,
*Sb*, and
*Sc*,
dimensionless.

#### Dependencies

To create this port, set **Switching voltage
function** to `Switch
inputs`.

### **BusVolt** — Power source bus voltage `bus`

Power source bus voltage,
*Vbus*, in V.

### **PhaseCurr** — Phase a, b, c current `1`-by-`3` array

Phase a, b, c current, *ia*,
*ib*, and
*ic*, in A.

### **MtrTrq** — Motor torque `scalar`

Motor torque, *Tmtr*, in
N·m.

### **MtrSpd** — Motor speed `scalar`

Angular speed of the motor,
*ωmtr*, in rad/s.

### **InvrtrTemp** — Inverter operating temperature `scalar`

Inverter operating temperature,
*TempInvrtr*, in
K.

#### Dependencies

To create this port, select **Input inverter
temperature**.
### Output

### **Info** — Bus signal bus

The bus signal contains these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `BusCurr` | | | Power source bus current | *ibus* | A |
| `PwrLossInv` | | | Inverter power loss | *εinv* | dimensionless |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | Power delivered to the motor | *PTrnsfrdMtr* | W |
| `PwrBus` | Power from input bus | *PTrnsfrdBus* | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Power loss | *PNotTrnsfrd* | W |
| `PwrStored` | | *Not used* | | |

### **PhaseVolt** — Phase a, b, c line-to-neutral voltage `1`-by-`3` array

Phase a, b, c line-to-neutral voltage,
*Van*,
*Vbn*, and
*Vcn*, in V.

### **BusCurr** — Power source bus current `scalar`

Power source bus current,
*ibus*, in A.

## Parameters

#### Block Options

### **Input inverter temperature** — Create input port `off` (default) | `on`

Select this parameter to create the `InvrtrTemp` input
port.

The block enables you to specify inverter
power loss lookup tables that are functions of motor torque,
*Tmtr*, and motor speed,
*ωmtr*. If you select
**Input inverter temperature**, the tables are also a
function of the inverter temperature,
*TempInvrtr*.

| **Input Inverter Temperature** Parameter Setting | Enables Efficiency Table | Function Of |
| --- | --- | --- |
| `off` | **Corresponding power loss, ploss\_table** | *ƒ*(*Tmtr*, *ωmtr*) |
| `on` | **Corresponding power loss, ploss\_table\_3d** | *ƒ*(*Tmtr*, *ωmtr*, *TempInvrtr*) |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InvrtrTmpInpEnbl` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

If you select **Input inverter temperature** to
specify a 3D power loss lookup table as a function of motor torque,
motor speed, and inverter temperature, you cannot select
**Enable memory optimized 2D LUT** to enable a
memory optimization.

### **Enable memory optimized 2D LUT** — Selection `off` (default) | `on`

Enable generation of memory-optimized lookup tables, suitable code
generation targets that limit memory.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `enable_hdl` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

If you select **Enable memory optimized 2D LUT**, you
cannot select **Input inverter temperature**.

### **Calibrate Maps** — Calibrate tables with measured data `selection`

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually calibrate the lookup
tables using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import Loss Data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedInverterDataset.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).    | **Input inverter temperature** Setting | Required Data | | --- | --- | | `off` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `on` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  Collect inverter data at steady-state operating conditions. Data should cover the inverter speed, torque, and temperature operating range.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate Response Models | Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate Calibration | Model-Based Calibration Toolbox calibrates the response models and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these parameters with the calibration.  | **Input inverter temperature** Setting | Parameters | | --- | --- | | `off` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Corresponding power loss,   ploss\_table** | | `on` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Breakpoints for temperature input,   Temp\_eff\_bp** - **Corresponding power loss,   ploss\_table\_3d** | |

#### Electrical Model

### **Switching voltage function** — Selection `Commanded phase voltage` (default) | `Switch inputs`

Use the **Switching voltage function**
parameter to set the switching voltage function.

| Setting | Implementation | Illustration |
| --- | --- | --- |
| **Commanded phase voltage** | Phase a, b, c line-to-neutral voltage command input. Suitable for continuous sinusoidal or space vector modulation input signals. | Circuit diagram when the parameter Switching voltage function is set to Commanded phase voltage |
| **Switch inputs** (default) | Inverter switch input command. Suitable for hardware-in-the-loop (HIL) simulation.  The inverter switches S1, S3, and S5 using complemented control for S2, S4, and S6. | Circuit diagram when the parameter Switching voltage function is set to Switch inputs |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `model_type` |
| **Values:** | `Commanded phase voltage` (default) | `Switch inputs` |
| **Data Types:** | `character vector` |

### **Breakpoints for speeds (w), w\_eff\_bp** — Speed breakpoints `[-1000 -500 0 500 1000]` (default) | `1`-by-`M` vector

Vector of motor speed, *ωmtr*,
breakpoints for power loss, in rad/s. If you set **Enable memory
optimized 2D LUT**, the block converts the data to single
precision.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_eff_bp` |
| **Values:** | `[-1000 -500 0 500 1000]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

### **Resample storage size for w\_eff\_bp, n1** — Speed bit size `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256`

Speed breakpoint storage size, *n1*, dimensionless. The
block resamples the **Corresponding power loss,
ploss\_table** data based on the storage size.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `n1` |
| **Values:** | `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D
LUT**.

### **Breakpoints for load input (T), T\_eff\_bp** — Torque breakpoints `[-200 -100 0 100 200]` (default) | `1`-by-`N` vector

Vector of motor torque, *Tmtr*,
breakpoints for power loss, in N·m. If you set **Enable memory
optimized 2D LUT**, the block converts the data to single
precision.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_eff_bp` |
| **Values:** | `[-200 -100 0 100 200]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

### **Resample storage size for T\_eff\_bp, n2** — Torque bit size `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256`

Torque breakpoint storage size, *n2*, dimensionless. The
block resamples the **Corresponding power loss,
ploss\_table** data based on the storage size.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `n2` |
| **Values:** | `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D
LUT**.

### **Breakpoints for temperature input, Temp\_eff\_bp** — Temperature breakpoints `[213.15 293.15 373.15]` (default) | `1`-by-`L` vector

Vector of inverter temperature,
*TempInvrtr*, breakpoints for
power loss, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temp_eff_bp` |
| **Values:** | `[213.15 293.15 373.15]` (default) | `1`-by-`L` vector |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Input inverter
temperature**.

### **Corresponding power loss, ploss\_table** — 2D lookup table `[1 0.999 0.989 0.997 0.996;0.995 0.994 0.993 0.992 0.991;0.990 0.989 0.988 0.987 0.986;0.985 0.984 0.983 0.982 0.981;0.980 0.979 0.978 0.977 0.976]` (default) | `M`-by-`N` array

Array of values for power loss as a function of `M` motor
speeds, *ωmtr*, and
`N` motor torques,
*Tmtr*, in W. Each value
specifies the power loss for a specific combination of motor speed and motor
torque. The array size must match the dimensions defined by the speed and
torque vectors.

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually
calibrate the lookup table using measured data.

If you set **Enable memory optimized 2D LUT**, the block
converts the data to single precision.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ploss_table` |
| **Values:** | `M`-by-`N` array |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, clear **Input inverter
temperature**.

### **Corresponding power loss, ploss\_table\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

Array of values for power loss as a function of `M` motor
speeds, *ωmtr*, `N`
motor torques, *Tmtr*, and
`L` motor temperatures,
*TempInvrtr*, in W. Each
value specifies the power loss for a specific combination of motor speed,
motor torque, and temperature. The array size must match the dimensions
defined by the speed, torque, and temperature vectors.

If you have Model-Based Calibration Toolbox, click **Calibrate Maps** to virtually
calibrate the lookup table using measured data.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ploss_table_3d` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Input inverter
temperature**.

#### Specify Extraction

### **w\_eff\_bp max endpoint, u1max** — Speed breakpoint `1000` (default) | `scalar`

Speed breakpoint maximum extrapolation endpoint, *u1max*,
in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `u1max` |
| **Values:** | `1000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **w\_eff\_bp min endpoint, u1min** — Speed breakpoint `-1000` (default) | `scalar`

Speed breakpoint minimum extrapolation endpoint, *u1min*,
in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `u1min` |
| **Values:** | `-1000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **T\_eff\_bp max endpoint, u2max** — Torque breakpoint `200` (default) | `scalar`

Torque breakpoint maximum extrapolation endpoint,
*u2max*, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `u2max` |
| **Values:** | `200` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **T\_eff\_bp min endpoint, u2min** — Torque breakpoint `-200` (default) | `scalar`

Torque breakpoint minimum extrapolation endpoint,
*u2min*, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `u2min` |
| **Values:** | `-200` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

## Libraries

Powertrain Blockset / Propulsion / Electric Motors and Inverters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Three-phase voltage source inverter

The Three-Phase Voltage Source Inverter block implements a three-phase
voltage source inverter that generates neutral voltage commands for a balanced
three-phase load. Configure the voltage switching function for continuous vector
modulation or inverter switch input signals. You can incorporate the block into a
closed-loop model to simulate a power inverter. The block controls the ideal switch
states.

To enable power loss calculations suitable for code generation targets that limit
memory, select **Enable memory optimized 2D LUT**. Click
**Calibrate Maps** to virtually calibrate an inverter power loss
lookup table as a function of motor torque and motor speed.

If you select **Input inverter temperature**, click
**Calibrate Maps** to virtually calibrate the power loss table as a
function of motor torque, motor speed, and inverter temperature. You cannot enable
memory optimization for the 3D power loss lookup table.

Use the **Switching voltage function**
parameter to set the switching voltage function.

| Setting | Implementation | Illustration |
| --- | --- | --- |
| **Commanded phase voltage** | Phase a, b, c line-to-neutral voltage command input. Suitable for continuous sinusoidal or space vector modulation input signals. | Circuit diagram when the parameter Switching voltage function is set to Commanded phase voltage |
| **Switch inputs** (default) | Inverter switch input command. Suitable for hardware-in-the-loop (HIL) simulation.  The inverter switches S1, S3, and S5 using complemented control for S2, S4, and S6. | Circuit diagram when the parameter Switching voltage function is set to Switch inputs |

### Virtual Calibration

If you have Model-Based Calibration Toolbox™, click **Calibrate Maps** to virtually calibrate the lookup
tables using measured data. The dialog box steps through these tasks.

| Task | Description |
| --- | --- |
| Import Loss Data | Import this loss data from a file. For example, open `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedInverterDataset.xlsx`.  For more information, see Using Data (Model-Based Calibration Toolbox).    | **Input inverter temperature** Setting | Required Data | | --- | --- | | `off` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `on` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  Collect inverter data at steady-state operating conditions. Data should cover the inverter speed, torque, and temperature operating range.  To filter or edit the data, select **Edit in Application**. The Model-Based Calibration Toolbox Data Editor opens. |
| Generate Response Models | Model-Based Calibration Toolbox uses test plans to fit data to Gaussian process models (GPMs).  To assess or adjust the response model fit, select **Edit in Application**. The Model-Based Calibration Toolbox Model Browser opens. For more information, see Model Assessment (Model-Based Calibration Toolbox). |
| Generate Calibration | Model-Based Calibration Toolbox calibrates the response models and generates calibrated tables.  To assess or adjust the calibration, select **Edit in Application**. The Model-Based Calibration Toolbox CAGE Browser opens. For more information, see Calibration Lookup Tables (Model-Based Calibration Toolbox). |
| Update block parameters | Update these parameters with the calibration.  | **Input inverter temperature** Setting | Parameters | | --- | --- | | `off` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Corresponding power loss,   ploss\_table** | | `on` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Breakpoints for temperature input,   Temp\_eff\_bp** - **Corresponding power loss,   ploss\_table\_3d** | |

### Switching Function

For the switch voltage, the block implementation depends on the
**Switching voltage function** setting.

| Setting | Calculation | Equations |
| --- | --- | --- |
| `Commanded phase voltage` | Continuous line-to-neutral voltage commands set to phase a, b, c line-to-neutral voltage command input | van=va\_cmdvbn=vb\_cmdvcn=vc\_cmd |
| Line-to-line voltage | vab= van− vbnvbc= vbn− vcnvca= vcn− van |
| `Switch inputs` | Switching function | SFa={1      S1 on and S2 off−1   S1 off and S2 onSFb={1      S3 on and S4 off−1   S3 off and S4 onSFc={1      S5 on and S6 off−1   S5 off and S6 on |
| Line-to-center point voltage | vao= vbus2 SFavbo= vbus2 SFbvco= vbus2 SFc |
| Line-to-neutral voltage | van= vao− vnovbn= vbo− vnovcn= vco− vnovan+ vbn+ vcn= 0vno= 13(vao+ vbo+ vco)van= vao− 13(vao+ vbo+ vco)vbn= vbo−13(vao+ vbo+ vco)vcn= vco− 13(vao+ vbo+ vco) |
| Line-to-line voltage | vab= van− vbnvbc= vbn− vcnvca= vcn− van |

The equations use these variables.

|  |  |
| --- | --- |
| *SFa*, *SFb*, *SFc* | Phase a, b, c line switching functions, respectively |
| *vbus* | Power source bus voltage |
| *Vao*, *Vbo*, *Vco* | Phase a, b, c line-to-center voltage, respectively |
| *Van*, *Vbn*, *Vcn* | Phase a, b, c line-to-neutral voltage, respectively |
| *Vab*, *Vbc*, *Vca* | Phase ab, bc, ca line-to-neutral voltage, respectively |
| *Va\_cmd*, *Vb\_cmd*, *Vc\_cmd* | Phase a, b, c line-to-neutral voltage commands, respectively |

### Current and Power Loss

For the line-to-center, line-to-neutral, and line-to-line voltage, the block
implements these equations.

| Calculation | | Equations |
| --- | --- | --- |
| Motor and bus power | | Pmtr= vania+vbnib+vcnicPbus= vbusibus |
| Inverter power loss and bus current | | Pin= Pbus= vbusibusPout= Pmtr= vania+vbnib+vcnic+PLossInvibus= vania+vbnib+vcnic+PLossInv vbus |

The equations use these variables.

|  |  |
| --- | --- |
| *Pmtr* | Power delivered to the motor |
| *Pbus* | Power from input bus |
| *Ploss* | Power loss |
| *ibus* | Power source bus current |
| *ia*, *ib*, *ic* | Phase a, b, c line current, respectively |
| *Van*, *Vbn*, *Vcn* | Phase a, b, c line-to-neutral voltage, respectively |
| *vbus* | Power source bus voltage |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equation |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Power delivered to the motor | *PTrnsfrdMtr* | PTrnsfrdMtr= −(vania+vbnib+vcnic ) |
| `PwrBus` | Power from input bus | *PTrnsfrdBus* | PTrnsfrdBus= Pbus |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLoss` | Power loss  Negative value indicates power loss | *PNotTrnsfrd* | PNotTrnsfrd= −(PTrnsfrdBus+PTrnsfrdMtr) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | | *Not used* | | |

### Lookup Table Memory Optimization

The inverter power loss table parameter **Corresponding power loss,
ploss\_table** data is a function of motor torque and motor speed at
different battery voltages. Positive current indicates battery discharge. Negative
current indicates battery charge.

To enable power loss calculations suitable for code generation targets that limit
memory, select **Enable memory optimized 2D LUT**. The block uses
linear interpolation to optimize the inverter power loss lookup table values for
code generation. This table summarizes the optimization
implementation.

| Use Case | | Implementation |
| --- | --- | --- |
| Motor speed and torque input align with the lookup table breakpoint values. | | Memory-optimized power loss is power loss lookup table value at intersection of motor speed and torque. |
| Motor speed and torque input do not align with the lookup table breakpoint values, but are within range. | | Memory-optimized power loss is linear interpolation between corresponding motor speed and torque. |
| Motor speed and torque input do not align with the lookup table breakpoint values, and are out of range. | | Cannot compute a memory-optimized power loss. Block uses extrapolated data. |

**Extrapolation**

The lookup tables optimized for code generation do not support extrapolation
for data that is out of range. However, you can include pre-calculated
extrapolation values in the power loss lookup table by selecting
**Specify Extrapolation**.

The block uses the endpoint parameters to resize the table data.

| User Input | Extrapolation |
| --- | --- |
| Lookup table to extrapolate to cover desired operating range | Extrapolated lookup table shown along with original table |
