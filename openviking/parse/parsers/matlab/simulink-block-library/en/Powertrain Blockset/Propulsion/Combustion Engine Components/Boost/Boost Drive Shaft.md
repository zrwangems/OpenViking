---
type: simulink-block
title: 'Boost Drive Shaft'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Boost'
documentation_page: 'boostdriveshaft'
documentation_source_path: 'ref/boostdriveshaft.html'
language: en
---

# Boost Drive Shaft

## Ports

### Input

### **Cmprs** — Compressor torque two-way connector port

Compressor torque, *τcomp*, in
N·m.

#### Dependencies

To create this port, for the **Configuration**
parameter, select `Turbocharger` or
`Compressor only`.

### **Turb** — Turbine torque two-way connector port

Turbine torque, *τturb*, in N·m.

#### Dependencies

To create this port, for the **Configuration** parameter,
select `Turbocharger` or `Turbine
only`.

### **ExtTrq** — Externally applied torque `scalar`

Externally applied torque,
*τext*, in N·m.

#### Dependencies

For turbocharger configurations, to create this port, set
**Additional torque input** to
`External torque input`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `DriveshftSpd` | | | Shaft speed | rad/s |
| `MechPwrLoss` | | | Mechanical power loss | W |
| `ExtTrq` | | | Applied external torque | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCmpsr` | Shaft power from compressor | W |
| `PwrTurb` | Shaft power from turbine | W |
| `PwrExt` | Externally applied power | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | Mechanical power loss | W |
| `PwrStored` | `PwrStoredDriveshft` | Rate change in rotational kinetic energy | W |

### **Cmprs** — Compressor speed two-way connector port

Compressor speed, *ω*, in rad/s.

#### Dependencies

To create this port, for the **Configuration**
parameter, select `Turbocharger` or
`Compressor only`.

### **Turb** — Turbine speed two-way connector port

Turbine speed, *ω*, in N·m.

#### Dependencies

To create this port, for the **Configuration** parameter,
select `Turbocharger` or `Turbine
only`.

## Parameters

#### Block Options

### **Configuration** — Specify configuration `Turbocharger` (default) | `Turbine only` | `Compressor only`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShaftConfigPopup` |
| **Values:** | `Turbocharger` (default) | `Turbine only` | `Compressor only` |
| **Data Types:** | `character vector` |

#### Dependencies

- Selecting `Turbocharger` or
  `Compressor only` creates the
  `Cmprs` port.
- Selecting `Turbocharger` or
  `Turbine only` creates the
  `Turb` port.

### **Additional torque input** — Specify external torque input `External torque input` (default) | `No external torque`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AddTrqTypePopup` |
| **Values:** | `External torque input` (default) | `No external torque` |
| **Data Types:** | `character vector` |

#### Dependencies

- To enable this parameter, select a
  `Turbocharger`
  configuration.
- To create the `Trq` port, select
  `External torque input`.

### **Shaft inertia, J\_shaft** — Inertia `1.55e-5` (default) | `scalar`

Shaft inertia, *Jshaft*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J_shaft` |
| **Values:** | `1.55e-5` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial shaft speed, w\_0** — Speed `1000` (default) | `scalar`

Initial drive shaft speed, *ω0*,
in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_0` |
| **Values:** | `1000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Min shaft speed, w\_min** — Speed `100` (default) | `scalar`

Minimum drive shaft speed, *ωmin*,
in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_min` |
| **Values:** | `100` (default) | `scalar` |
| **Data Types:** | `double` |

### **Max shaft speed, w\_max** — Speed `20000` (default) | `scalar`

Maximum drive shaft speed, *ωmax*,
in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_max` |
| **Values:** | `20000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Turbine mechanical efficiency, eta\_mech** — Efficiency `0.95` (default) | `scalar`

Mechanical efficiency of turbine
*ηmax*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_mech` |
| **Values:** | `0.95` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select the
`Turbocharger` or `Turbine
only` configuration.

## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Boost drive shaft speed

The Boost Drive Shaft block uses the compressor,
turbine, and external torques to calculate the drive shaft speed.
Use the block to model turbochargers and superchargers in an engine
model.

You can specify these configurations:

- Turbocharger — Connect the compressor to the
  turbine

  - Two-way ports for turbine and compressor connections
  - Option to add an externally applied input torque
- Compressor only — Connect the drive shaft to
  the compressor

  - Two-way port for compressor connection
  - Externally applied input torque
- Turbine only — Connect the drive shaft to the
  turbine

  - Two-way port for turbine connection
  - Externally applied load torque

For the `Turbine only` and `Turbocharger` configurations,
the block modifies the turbine torque with a mechanical efficiency.

### Equations

The Boost Drive Shaft block applies Newton’s
Second Law for Rotation. Positive torques cause the drive shaft to
accelerate. Negative torques impose a load and decelerate the drive
shaft.

The block also calculates the power loss due to mechanical inefficiency.

| Calculation | Equations |
| --- | --- |
| Shaft dynamics | dωdt=1Jshaft(ηmechτturb+τcomp+τext) with initial speed *ω0* |
| Speed constraint | ωmin≤ω≤ωmax |
| Power loss | W˙loss=ωτturb(1−ηmech) |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrCmpsr` | Shaft power from compressor | τcompω |
| `PwrTurb` | Shaft power from turbine | τturbω |
| `PwrExt` | Externally applied power | τextω |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrMechLoss` | Mechanical power loss | −W˙turb |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredDriveshft` | Rate change in rotational kinetic energy | (ηmechτturb+τcomp+τext)ω |

The equations use these variables.

|  |  |
| --- | --- |
| *ω* | Shaft speed |
| *ω0* | Initial drive shaft speed |
| *ωmin* | Minimum drive shaft speed |
| *ωmax* | Maximum drive shaft speed |
| *Jshaft* | Shaft inertia |
| *ηmax* | Mechanical efficiency of turbine |
| *τcomp* | Compressor torque |
| *τturb* | Turbine torque |
| *τext* | Externally applied torque. |
| W˙loss | Power loss due to mechanical inefficiency |
