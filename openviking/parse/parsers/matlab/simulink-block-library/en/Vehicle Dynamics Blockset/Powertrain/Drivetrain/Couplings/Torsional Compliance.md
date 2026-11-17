---
type: simulink-block
title: 'Torsional Compliance'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Couplings'
documentation_page: 'torsionalcompliance'
documentation_source_path: 'ref/torsionalcompliance.html'
language: en
---

# Torsional Compliance

## Ports
```yaml
ports:
- name: RSpd
  summary: Driveshaft R angular velocity scalar
  direction: input
- name: CSpd
  summary: Driveshaft C angular velocity scalar
  direction: input
- name: R
  summary: Angular velocity and torque two-way connector port
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: RTrq
  summary: Driveshaft R torque scalar
  direction: output
- name: CTrq
  summary: Driveshaft C torque scalar
  direction: output
- name: C
  summary: Angular velocity and torque two-way connector port
  direction: output
```

### Input

### **RSpd** — Driveshaft R angular velocity `scalar`

Input driveshaft angular velocity, in rad/s.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **CSpd** — Driveshaft C angular velocity `scalar`

Output driveshaft angular velocity, in rad/s.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **R** — Angular velocity and torque two-way connector port

Angular velocity in rad/s. Torque is in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Two-way connection`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| Trq | `R` | | Input driveshaft torque | *TR* | N·m |
| `C` | | Output driveshaft torque | *TC* | N·m |
| `Damp` | | Damping torque | Ts=bθ˙ | N·m |
| `Spring` | | Spring torque | *Td* = *k**θ* | N·m |
| Spd | `R` | | Input driveshaft angular velocity | *ωR* | rad/s |
| `C` | | Output driveshaft angular velocity | *ωC* | rad/s |
| `deltadot` | | Difference in input and output driveshaft angular velocity | θ˙ | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrR` | Mechanical power from driveshaft R | *PTR* | W |
| `PwrC` | Mechanical power from driveshaft C | *PTC* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Power loss due to damping | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | Rate change of stored internal kinetic energy | *Ps* | W |

#### Dependencies

To enable this port, select **Output Info bus**.

### **RTrq** — Driveshaft R torque `scalar`

Input drive shaft torque, in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **CTrq** — Driveshaft C torque `scalar`

Applied output driveshaft torque, in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Simulink`.

### **C** — Angular velocity and torque two-way connector port

Angular velocity in rad/s. Torque is in N·m.

#### Dependencies

To enable this port, for **Port Configuration**,
select `Two-way connection`.
## Parameters
```yaml
parameters:
- name: Port Configuration
  summary: Specify configuration Simulink (default) | Two-way connection
  group: ''
  block_parameter: port_config
  values: Simulink (default) | Two-way connection
- name: Output Info bus
  summary: Selection off (default) | on
  group: ''
- name: Torsional stiffness, k
  summary: Inertia 1e4 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: k
  values: 1e4 (default) | scalar greater than or equal to 0
- name: Torsional damping, b
  summary: Damping 1e2 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: b
  values: 1e2 (default) | scalar greater than or equal to 0
- name: Initial deflection, theta_o
  summary: Angular 0 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: theta_o
  values: 0 (default) | scalar greater than or equal to 0
- name: Initial velocity difference, domega_o
  summary: Angular 0 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: domega_o
  values: 0 (default) | scalar greater than or equal to 0
- name: Damping cut-off frequency, omega_c
  summary: Frequency 3000 (default) | positive scalar
  group: ''
  block_parameter: omega_c
  values: 3000 (default) | positive scalar
```

#### Block Options

### **Port Configuration** — Specify configuration `Simulink` (default) | `Two-way connection`

Specify the port configuration.

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

#### Dependencies

Specifying `Simulink` creates these ports:

- `RSpd`
- `CSpd`
- `RTrq`
- `CTrq`

Specifying `Two-way connection` creates these ports:

- `R`
- `C`

### **Output Info bus** — Selection `off` (default) | `on`

Select to create the `Info` output port.

### **Torsional stiffness, k** — Inertia `1e4` (default) | scalar greater than or equal to 0

Torsional stiffness, in N·m/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `k` |
| **Values:** | `1e4` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Torsional damping, b** — Damping `1e2` (default) | scalar greater than or equal to 0

Torsional damping, in N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b` |
| **Values:** | `1e2` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Initial deflection, theta\_o** — Angular `0` (default) | scalar greater than or equal to 0

Initial deflection, in rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `theta_o` |
| **Values:** | `0` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Initial velocity difference, domega\_o** — Angular `0` (default) | scalar greater than or equal to 0

Initial velocity difference, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `domega_o` |
| **Values:** | `0` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Damping cut-off frequency, omega\_c** — Frequency `3000` (default) | positive scalar

Damping cut-off frequency, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_c` |
| **Values:** | `3000` (default) | positive scalar |
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

Parallel spring-damper

The Torsional Compliance block implements a parallel spring-damper to
couple two rotating driveshafts. The block uses the driveshaft angular velocities,
torsional stiffness, and torsional damping to determine the torques.

TR=−(ωR−ωC)b−θkTC=(ωR−ωC)b+θkθ˙=(ωR−ωC)

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrR` | Mechanical power from driveshaft R | *PTR* | PTR= TRωR |
| `PwrC` | Mechanical power from driveshaft C | *PTC* | PTC= Tcωc |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrDampLoss` | Mechanical damping loss | *Pd* | Pd=−b|θ˙|2 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredShft` | Rate change in spring energy | *PS* | Ps=−θkθ˙ |

The equations use these variables.

|  |  |
| --- | --- |
| *TR* | Driveshaft R torque |
| *TC* | Driveshaft C torque |
| *ωR* | Driveshaft R angular velocity |
| *ωC* | Driveshaft C angular velocity |
| *θ* | Coupled driveshaft rotation |
| *k* | Driveshaft torsional stiffness |
| *b* | Rotational viscous damping |
| *Pd* | Power loss due to damping |
| *Ps* | Rate change of stored spring energy |
