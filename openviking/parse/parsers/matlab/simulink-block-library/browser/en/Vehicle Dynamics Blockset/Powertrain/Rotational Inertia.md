---
type: simulink-block
title: 'Rotational Inertia'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain'
documentation_page: 'rotationalinertia'
documentation_source_path: 'ref/rotationalinertia.html'
language: en
---

# Rotational Inertia

## Ports

### Input

### **RTrq** — Input torque `scalar`

Applied input driveshaft torque,
*TR*, in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **CTrq** — Output torque `scalar`

Load driveshaft torque, *TC*,
in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **R** — Angular velocity and torque two-way connector port

Angular velocity in rad/s. Torque is in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Two-way connection`.

### **Inertia** — Input `scalar`

Rotational inertia, in kg·m^2.

#### Dependencies

To create the `Inertia` port, select **External inertia
input**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| Trq | `R` | | Applied input driveshaft torque | *TR* | N·m |
| `C` | | Output driveshaft torque | *TC* | N·m |
| `Damp` | | Damping torque | *Td*=*b**ω* | N·m |
| Spd | | | Angular driveshaft speed | *ω* | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrR` | Mechanical power from base shaft | *PTR* | W |
| `PwrC` | Mechanical power from follower shaft | *PTC* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Power loss due to damping | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | Rate change of stored internal torsional energy | *Ps* | W |

#### Dependencies

To enable this port, select **Output Info bus**.

### **Spd** — Driveshaft speed `scalar`

Angular driveshaft speed, *ω*, in rad/s.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **C** — Angular velocity and torque two-way connector port

Angular velocity in rad/s. Torque is in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Two-way connection`.

## Parameters

#### Block Options

### **Port Configuration** — Specify configuration `Simulink` (default) | `Two-way connection`

Specify the port configuration.

#### Dependencies

Specifying `Simulink` creates these ports:

- `RTrq`
- `CTrq`
- `Spd`

Specifying `Two-way connection` creates these ports:

- `R`
- `C`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **Values:** | `Simulink` (default) | `Two-way connection` |
| **Data Types:** | `character vector` |

### **Output Info bus** — Selection `off` (default) | `on`

Select to create the `Info` output port.

### **External inertia input** — Input rotational inertia `off` (default) | `on`

Input the rotational inertia.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `externJ` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

To create the `Inertia` port, select **External inertia
input**.

#### Parameters

### **Rotational inertia, J** — Inertia `.01` (default) | scalar greater than or equal to 0

Rotational inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J` |
| **Values:** | `.01` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **External inertia
input**.

### **Torsional damping, b** — Damping `.001` (default) | scalar greater than or equal to 0

Torsional damping, in N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bc` |
| **Values:** | `.001` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Initial velocity, omega\_o** — Angular `0` (default) | scalar greater than or equal to 0

Initial angular velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_o` |
| **Values:** | `0` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Ideal mechanical rotational inertia

The Rotational Inertia block implements an ideal mechanical rotational
inertia.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrR` | Mechanical power from base shaft | *PTR* | PTR= TRω |
| `PwrC` | Mechanical power from follower shaft | *PTC* | PTC= TCω |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrDampLoss` | Power loss due to damping | *Pd* | Pd=−b|ω|2 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredShft` | Rate change of stored internal torsional energy | *Ps* | Ps=ωω˙J |

The equations use these variables.

|  |  |
| --- | --- |
| *TR* | Input torque |
| *TC* | Output torque |
| *ω* | Driveshaft angular velocity |
| *J* | Rotational inertia |
| *b* | Rotational viscous damping |
| *Pd* | Power loss due to damping |
| *Ps* | Rate change of stored internal torsional energy |
