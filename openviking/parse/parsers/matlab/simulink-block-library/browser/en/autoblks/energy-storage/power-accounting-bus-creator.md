---
type: simulink-block
title: 'Power Accounting Bus Creator'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'poweraccountingbuscreator'
documentation_source_path: 'ref/poweraccountingbuscreator.html'
language: en
---

# Power Accounting Bus Creator

## Ports

### Input

### **PwrTrnsfrd** — Power transferred between blocks `bus`

`PwrTrnsfrd` — Power transferred between blocks

- Positive signals indicate flow into block
- Negative signals indicate flow out of block

#### Dependencies

To create this input port, select **Transferred power**.

### **PwrNotTrnsfrd** — Power crossing block boundary, not transferred `bus`

`PwrNotTrnsfrd` — Power crossing the block
boundary, but not transferred

- Positive signals indicate an input
- Negative signals indicate a loss

#### Dependencies

To create this input port, select **Not transferred power**.

### **PwrStored** — Stored energy rate of change `bus`

`PwrStored` — Stored energy rate of change

- Positive signals indicate an increase
- Negative signals indicate a decrease

#### Dependencies

To create this input port, select **Stored power**.
### Output

### **PwrInfo** — Power information bus `bus`

Power information bus

## Parameters

#### Block Options

### **Associated block** — Associated block `Parent` (default) | `Parent reference block`

When you add the Power Accounting Bus Creator to your plant block, you associate the signals to a parent block. There are two association methods.

| Method | Description | Example |
| --- | --- | --- |
| `Parent` | Power Accounting Bus Creator associates the power bus signals with the parent block. | In the conventional vehicle reference application, navigate to the `Passenger Car > Engine > SiMappedEngine > Accessory Load Model` plant subsystem. Open the Power Accounting Bus Creator.  The **Associated block** parameter is set to `Parent`, so the Power Accounting Bus Creator associates the power signals with the `Accessory Load Model` plant subsystem.  Power Accounting Buss Creator block mask with Associated block parameter set to parent. |
| `Parent reference block` | Power Accounting Bus Creator associates the power bus signals with a reference block.  Use the **Library block name** parameter to specify the block. | In the Ideal Fixed Gear Transmission block, navigate to the `Bus Creation` subsystem. Open the Power Accounting Bus Creator.  The Power Accounting Bus Creator block uses these parameter settings to associate the power signals to the Ideal Fixed Gear Transmission block.  - **Associated block** parameter is set to   `Parent reference   block`. - **Library block name** parameter is set   to `'autolibsharedtransfixedgear/Ideal Fixed Gear   Transmission'`.    Power Accounting Buss Creator block mask with Associated block parameter set to parent reference block. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterGroupVar` |
| **Values:** | `Parent` (default) | `Parent reference block` |
| **Data Types:** | `character vector` |

### **Library block name** — Block name `Block name`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RefBlckName` |
| **Values:** | `Block name` |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, set **Associated block** to
`Parent reference block`.

#### Power Input Types

### **Transferred power** — Power transferred between blocks `on` (default) | `off`

Power transferred between blocks.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PwrTrnsfrdCheckBox` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, set **Associated block** to
`Parent reference block`.

Selecting this parameter creates the:

- `PwrTrnsfrd` input port
- **Transferred** parameters

### **Not transferred power** — Power crossing block boundary `on` (default) | `off`

Power crossing block boundary, but not transferred.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PwrNotTrnsfrdCheckBox` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting this parameter creates the:

- `PwrNotTrnsfrd` input port
- **Not Transferred** parameters

### **Stored power** — Stored energy rate of change `on` (default) | `off`

Stored energy rate of change.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PwrStoredCheckBox` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting this parameter creates the:

- `PwrStored` input port
- **Stored** parameters

#### Transferred

### **Signal name** — Name of signal `char`

Signal name.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Transferred** parameter values for the
listed blocks.

| Block | Power Accounting Bus Creator Parameter Values | | |
| --- | --- | --- | --- |
| **Signal Name** | **Associated Port** | **Description** |
| Ideal Fixed Gear Transmission | `PwrTrnsfrd.PwrDiffrntl` | `{'DiffTrq','DiffSpd'}` | `Differential` |
| `PwrTrnsfrd.PwrEng` | `{'EngTrq','EngSpd'}` | `Engine` |
| Gearbox | `PwrTrnsfrd.PwrBase` | `{{'BTrq','BSpd'}'B'}` | `Base input` |
| `PwrTrnsfrd.PwrFlwr` | `{{'FTrq','FSpd'}'F'}` | `Follower output` |
| Boost Drive Shaft | `PwrTrnsfrd.PwrCmpsr` | `'Cmpsr'` | `Compressor` |
| `PwrTrnsfrd.PwrExt` | `'ExtTrq'` | `External` |
| `PwrTrnsfrd.Turb` | `'Turb'` | `Turbine` |

### **Associated Port** — Name of ports that transfer power `{'PortA','PortB','PortC'}`

Name of ports that transfer power.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Transferred** parameter values for the
listed blocks.

| Block | Power Accounting Bus Creator Parameter Values | | |
| --- | --- | --- | --- |
| **Signal Name** | **Associated Port** | **Description** |
| Ideal Fixed Gear Transmission | `PwrTrnsfrd.PwrDiffrntl` | `{'DiffTrq','DiffSpd'}` | `Differential` |
| `PwrTrnsfrd.PwrEng` | `{'EngTrq','EngSpd'}` | `Engine` |
| Gearbox | `PwrTrnsfrd.PwrBase` | `{{'BTrq','BSpd'}'B'}` | `Base input` |
| `PwrTrnsfrd.PwrFlwr` | `{{'FTrq','FSpd'}'F'}` | `Follower output` |
| Boost Drive Shaft | `PwrTrnsfrd.PwrCmpsr` | `'Cmpsr'` | `Compressor` |
| `PwrTrnsfrd.PwrExt` | `'ExtTrq'` | `External` |
| `PwrTrnsfrd.Turb` | `'Turb'` | `Turbine` |

### **Description** — Signal description `char`

Signal description.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Transferred** parameter values for the
listed blocks.

| Block | Power Accounting Bus Creator Parameter Values | | |
| --- | --- | --- | --- |
| **Signal Name** | **Associated Port** | **Description** |
| Ideal Fixed Gear Transmission | `PwrTrnsfrd.PwrDiffrntl` | `{'DiffTrq','DiffSpd'}` | `Differential` |
| `PwrTrnsfrd.PwrEng` | `{'EngTrq','EngSpd'}` | `Engine` |
| Gearbox | `PwrTrnsfrd.PwrBase` | `{{'BTrq','BSpd'}'B'}` | `Base input` |
| `PwrTrnsfrd.PwrFlwr` | `{{'FTrq','FSpd'}'F'}` | `Follower output` |
| Boost Drive Shaft | `PwrTrnsfrd.PwrCmpsr` | `'Cmpsr'` | `Compressor` |
| `PwrTrnsfrd.PwrExt` | `'ExtTrq'` | `External` |
| `PwrTrnsfrd.Turb` | `'Turb'` | `Turbine` |

#### Not Transferred

### **Signal name** — Name of signal `char`

Signal name.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Not Transferred** parameter values for
the listed blocks.

| Block | Power Accounting Bus Creator Parameter Values | |
| --- | --- | --- |
| **Signal Name** | **Description** |
| Ideal Fixed Gear Transmission | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrEffLoss` | `Efficiency loss` |
| Gearbox | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |
| Boost Drive Shaft | `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |

### **Description** — Signal description `char`

Signal description.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Not Transferred** parameter values for
the listed blocks.

| Block | Power Accounting Bus Creator Parameter Values | |
| --- | --- | --- |
| **Signal Name** | **Description** |
| Ideal Fixed Gear Transmission | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrEffLoss` | `Efficiency loss` |
| Gearbox | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |
| Boost Drive Shaft | `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |

#### Stored

### **Signal name** — Name of signal `char`

Signal name.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Stored** parameter values for the listed
blocks.

| Block | Power Accounting Bus Creator Parameter Values | |
| --- | --- | --- |
| **Signal Name** | **Description** |
| Ideal Fixed Gear Transmission | `PwrStored.PwrStoredTrans` | `Rotational` |
| Control Volume System | `PwrStored.PwrHeatStored` | `Stored heat` |
| Datasheet Battery | `PwrStored.PwrStoredBatt` | `Battery stored` |

### **Description** — Signal description `char`

Signal description.

For example, this table summarizes the Power Accounting
Bus Creator parameter **Stored** parameter values for the listed
blocks.

| Block | Power Accounting Bus Creator Parameter Values | |
| --- | --- | --- |
| **Signal Name** | **Description** |
| Ideal Fixed Gear Transmission | `PwrStored.PwrStoredTrans` | `Rotational` |
| Control Volume System | `PwrStored.PwrHeatStored` | `Stored heat` |
| Datasheet Battery | `PwrStored.PwrStoredBatt` | `Battery stored` |

## Libraries

Powertrain Blockset / Utilities / Power Accounting

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Create power information bus

Creates a power information bus for reporting system power and energy consumption. You can
associate the block to a parent system, select types of power signals to track, and add signal
descriptions. If you want to generate a power and energy report, you must use this block to
log the power signals in your plant model blocks. The Powertrain Blockset™ plant blocks use the Power Accounting Bus Creator to log the
power signals. The documentation for each block includes information about the logged power
bus signals.

The system-level power and energy accounting satisfies the conservation of energy.

∑​Ptrans+∑​Pnottrans=∑​Pstore

To add the Power Accounting Bus Creator to your plant block, follow these steps:

1. Add the Power Accounting Bus Creator block to your block.
2. Select the types of power signals that you want to log. See Power Signals.
3. Associate the Power Accounting Bus Creator with a parent subsystem.
   See Block Association.
4. Connect the power signals to the Power Accounting Bus Creator.

   - Follow the sign convention.
   - To ensure that your plant block conserves energy, include all power associated
     with the block.
5. In the Power Accounting Bus Creator:

   - On the **Transferred** power tab, specify these parameters:

     - **Associated Port**
     - **Description**
   - On the **Not Transferred** power tab, specify the
     **Description** parameter:
6. In the plant block, connect the transferred power signals to the Power
   Accounting Bus Creator ports that are specified with the **Associated
   Port** parameter.

### Power Signals

The Power Accounting Bus Creator sorts the signals into three power
types.

| Power Type | | Description | Examples |
| --- | --- | --- | --- |
| *Ptrans* | Transferred | Power transferred between blocks:  - Positive signals indicate flow into block - Negative signals indicate flow out of block | - Crankshaft power transferred from mapped engine to transmission. - Road load power transferred from wheel to vehicle. - Rate of heat flow transferred from throttle to manifold volume. |
| *Pnottrans* | Not transferred | Power crossing the block boundary, but not transferred:  - Positive signals indicate an input - Negative signals indicate a loss | - Rate of heat transfer with the environment.  - From environment is an input (positive     signal)   - To environment is a loss (negative signal) - Flow boundary with the environment.  - From environment is an input (positive     signal)   - To environment is a loss (negative signal) - Mapped engine fuel flow. |
| *Pstore* | Stored | Stored energy rate of change:  - Positive signals indicate an increase - Negative signals indicate a decrease | Energy rate of change:  - Battery storage - Kinetic energy in drivetrain components - Vehicle potential energy - Vehicle velocity |

### Block Association

When you add the Power Accounting Bus Creator to your plant block, you associate the signals to a parent block. There are two association methods.

| Method | Description | Example |
| --- | --- | --- |
| `Parent` | Power Accounting Bus Creator associates the power bus signals with the parent block. | In the conventional vehicle reference application, navigate to the `Passenger Car > Engine > SiMappedEngine > Accessory Load Model` plant subsystem. Open the Power Accounting Bus Creator.  The **Associated block** parameter is set to `Parent`, so the Power Accounting Bus Creator associates the power signals with the `Accessory Load Model` plant subsystem.  Power Accounting Buss Creator block mask with Associated block parameter set to parent. |
| `Parent reference block` | Power Accounting Bus Creator associates the power bus signals with a reference block.  Use the **Library block name** parameter to specify the block. | In the Ideal Fixed Gear Transmission block, navigate to the `Bus Creation` subsystem. Open the Power Accounting Bus Creator.  The Power Accounting Bus Creator block uses these parameter settings to associate the power signals to the Ideal Fixed Gear Transmission block.  - **Associated block** parameter is set to   `Parent reference   block`. - **Library block name** parameter is set   to `'autolibsharedtransfixedgear/Ideal Fixed Gear   Transmission'`.    Power Accounting Buss Creator block mask with Associated block parameter set to parent reference block. |
