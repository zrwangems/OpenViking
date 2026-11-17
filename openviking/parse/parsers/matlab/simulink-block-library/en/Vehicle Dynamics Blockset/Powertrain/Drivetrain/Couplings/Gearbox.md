---
type: simulink-block
title: 'Gearbox'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Couplings'
documentation_page: 'gearbox'
documentation_source_path: 'ref/gearbox.html'
language: en
---

# Gearbox

## Ports
```yaml
ports:
- name: BTrq
  summary: Base gear input torque scalar
  direction: input
- name: FTrq
  summary: Follower gear output torque scalar
  direction: input
- name: B
  summary: Base gear angular velocity and torque two-way connector port
  direction: input
- name: AirTemp
  summary: Ambient air temperature scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: BSpd
  summary: Input gear angular velocity scalar
  direction: output
- name: FSpd
  summary: Output gear angular velocity scalar
  direction: output
- name: F
  summary: Output gear angular velocity and torque two-way connector port
  direction: output
```

### Input

### **BTrq** — Base gear input torque `scalar`

Base gear input torque, *TB*,
in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **FTrq** — Follower gear output torque `scalar`

Follower gear output torque,
*TF*, in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **B** — Base gear angular velocity and torque two-way connector port

Base gear angular velocity, *ωB*,
in rad/s. Base gear torque, *TB*,
in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Two-way connection`.

### **AirTemp** — Ambient air temperature `scalar`

Ambient air temperature, *Tair*, in K.

#### Dependencies

To enable this port:

- Set **Efficiency factors** to `Driveshaft
  torque, speed and temperature`.
- Select **Input ambient temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| Base | `BaseTrq` | | Base gear input torque | *TB* | N·m |
| `BaseSpd` | | Base gear angular velocity | *ωB* | rad/s |
| Flwr | `FlwrTrq` | | Follower gear torque | *TF* | N·m |
| `FlwrSpd` | | Follower gear angular velocity | *ωF* | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrBase` | Mechanical power from base shaft | *PBase* | W |
| `PwrFlwr` | Mechanical power from follower shaft | *PFlwr* | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | Total gear power loss | *Png* | W |
| `PwrDampLoss` | Power loss due to damping | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | Rate change of stored internal kinetic energy | *Ps* | W |

### **BSpd** — Input gear angular velocity `scalar`

Base gear angular velocity,
*ωB*, in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **FSpd** — Output gear angular velocity `scalar`

Follower gear angular velocity,
*ωF*, in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **F** — Output gear angular velocity and torque two-way connector port

Follower gear angular velocity,
*ωF*, in rad/s. Follower
gear torque, *TF*, in
N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Two-way connection`.
## Parameters
```yaml
parameters:
- name: Port Configuration
  summary: Specify configuration Simulink (default) | Two-way connection
  group: ''
  block_parameter: port_config
  values: Simulink (default) | Two-way connection
- name: Efficiency factors
  summary: Specify configuration Constant (default) | Driveshaft torque, speed and temperature
  group: ''
  block_parameter: input_config
  values: Constant (default) | Driveshaft torque, speed and temperature
- name: Interpolation method
  summary: Method Flat | Nearest | Linear point-slope | Linear Lagrange | Cubic spline
  group: ''
  block_parameter: InterpMethod
  values: Flat | Nearest | Linear point-slope | Linear Lagrange | Cubic spline
- name: Output shaft rotates in same direction as input
  summary: Rotation off (default) | on
  group: ''
  block_parameter: dirSwitch
  values: off (default) | on
- name: Input ambient temperature
  summary: Create input port off (default) | on
  group: ''
  block_parameter: extTamb
  values: off (default) | on
- name: Input to output gear ratio, N
  summary: Ratio 2 (default) | positive scalar
  group: ''
  block_parameter: N
  values: 2 (default) | positive scalar
- name: Input shaft inertia, J1
  summary: Inertia .01 (default) | positive scalar
  group: ''
  block_parameter: J1
  values: .01 (default) | positive scalar
- name: Output shaft inertia, J2
  summary: Inertia .01 (default) | positive scalar
  group: ''
  block_parameter: J2
  values: .01 (default) | positive scalar
- name: Input shaft damping, b1
  summary: Damping .001 (default) | positive scalar
  group: ''
  block_parameter: b1
  values: .001 (default) | positive scalar
- name: Output shaft damping, b2
  summary: Damping .001 (default) | positive scalar
  group: ''
  block_parameter: b2
  values: .001 (default) | positive scalar
- name: Input shaft initial velocity, w1_o
  summary: Initial velocity 0 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: w1_o
  values: 0 (default) | scalar greater than or equal to 0
- name: Constant efficiency factor, eta
  summary: Efficiency 1 (default) | positive scalar
  group: ''
  block_parameter: eta
  values: 1 (default) | positive scalar
- name: Efficiency lookup table, eta_tbl
  summary: Lookup table M-by-N-by-L array
  group: ''
  block_parameter: eta_tbl
  values: M-by-N-by-L array
- name: Efficiency torque breakpoints, Trq_bpts
  summary: Torque breakpoints [25, 50, 75, 100, 150, 200, 250] (default) | 1-by-M vector
  group: ''
  block_parameter: Trq_bpts
  values: '[25, 50, 75, 100, 150, 200, 250] (default) | 1-by-M vector'
- name: Efficiency speed breakpoints, omega_bpts
  summary: Speed breakpoints [52.4 78.5 105 131 157 183 209 262 314 419 524] (default) | 1-by-N vector
  group: ''
  block_parameter: omega_bpts
  values: '[52.4 78.5 105 131 157 183 209 262 314 419 524] (default) | 1-by-N vector'
- name: Efficiency temperature breakpoints, Temp_bpts
  summary: Temperature breakpoints [290 358] (default) | 1-by-L vector
  group: ''
  block_parameter: Temp_bpts
  values: '[290 358] (default) | 1-by-L vector'
- name: Air temperature, Tair
  summary: Ambient air temperature 297.15 (default) | scalar greater than 0
  group: ''
  block_parameter: Tair
  values: 297.15 (default) | scalar greater than 0
```

#### Block Options

### **Port Configuration** — Specify configuration `Simulink` (default) | `Two-way connection`

Specify the port configuration.

#### Dependencies

Specifying `Simulink` creates these ports:

- `BSpd`
- `FSpd`
- `BTrq`
- `FTrq`

Specifying `Two-way connection` creates these ports:

- `B`
- `F`

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

### **Efficiency factors** — Specify configuration `Constant` (default) | `Driveshaft torque, speed and temperature`

To account for the block efficiency, use the **Efficiency factors** parameter. This table summarizes the block implementation for each setting.

| Setting | Implementation |
| --- | --- |
| `Constant` | Constant efficiency that you can set with the **Constant efficiency factor, eta** parameter. |
| `Driveshaft torque, temperature and speed` | Efficiency as a function of base gear input torque, air temperature, and driveshaft speed. Use these parameters to specify the lookup table and breakpoints:  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    For the air temperature, you can either:  - Select **Input ambient temperature** to   create an input port. - Set a **Ambient temperature, Tamb**   parameter value.    To select the interpolation method, use the **Interpolation method** parameter. For more information, see Interpolation Methods. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `input_config` |
| **Values:** | `Constant` (default) | `Driveshaft torque, speed and temperature` |
| **Data Types:** | `character vector` |

### **Interpolation method** — Method `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

For more information, see Interpolation Methods.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InterpMethod` |
| **Values:** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Output shaft rotates in same direction as input** — Rotation `off` (default) | `on`

Select to specify that the output shaft rotates in the same direction as
the input.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dirSwitch` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Input ambient temperature** — Create input port `off` (default) | `on`

Select to create input port `AirTemp` for the ambient air
temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `extTamb` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Input to output gear ratio, N** — Ratio `2` (default) | positive scalar

Base-to-follower gear ratio, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N` |
| **Values:** | `2` (default) | positive scalar |
| **Data Types:** | `double` |

### **Input shaft inertia, J1** — Inertia `.01` (default) | positive scalar

Base shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J1` |
| **Values:** | `.01` (default) | positive scalar |
| **Data Types:** | `double` |

### **Output shaft inertia, J2** — Inertia `.01` (default) | positive scalar

Follower shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J2` |
| **Values:** | `.01` (default) | positive scalar |
| **Data Types:** | `double` |

### **Input shaft damping, b1** — Damping `.001` (default) | positive scalar

Base viscous shaft damping, in N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b1` |
| **Values:** | `.001` (default) | positive scalar |
| **Data Types:** | `double` |

### **Output shaft damping, b2** — Damping `.001` (default) | positive scalar

Follower viscous shaft damping, in N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b2` |
| **Values:** | `.001` (default) | positive scalar |
| **Data Types:** | `double` |

### **Input shaft initial velocity, w1\_o** — Initial velocity `0` (default) | scalar greater than or equal to 0

Base shaft initial velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w1_o` |
| **Values:** | `0` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

#### Efficiency

### **Constant efficiency factor, eta** — Efficiency `1` (default) | positive scalar

Constant efficiency, *η*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Constant`.

### **Efficiency lookup table, eta\_tbl** — Lookup table `M`-by-`N`-by-`L` array

Dimensionless array of values for efficiency as a function of:

- `M` input torques
- `N` input speed
- `L` air temperatures

Each value specifies the efficiency for a specific combination of torque,
speed, and temperature. The array size must match the dimensions defined by the torque,
speed, and temperature breakpoint vectors.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_tbl` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Efficiency torque breakpoints, Trq\_bpts** — Torque breakpoints `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector

Vector of input torque, breakpoints for efficiency, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_bpts` |
| **Values:** | `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Efficiency speed breakpoints, omega\_bpts** — Speed breakpoints `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector

Vector of speed, breakpoints for efficiency, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_bpts` |
| **Values:** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Efficiency temperature breakpoints, Temp\_bpts** — Temperature breakpoints `[290 358]` (default) | `1`-by-`L` vector

Vector of ambient temperature breakpoints for efficiency, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temp_bpts` |
| **Values:** | `[290 358]` (default) | `1`-by-`L` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Air temperature, Tair** — Ambient air temperature `297.15` (default) | scalar greater than 0

Ambient air temperature, *Tair*, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tair` |
| **Values:** | `297.15` (default) | scalar greater than 0 |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter:

- Set **Efficiency factors** to `Driveshaft
  torque, speed and temperature`.
- Clear **Input ambient temperature**.
## Libraries

Powertrain Blockset / Drivetrain / Couplings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Ideal rotational gearbox

The Gearbox block implements an ideal rotational
gearbox. The block uses the gear inertias and damping to calculate
the velocity response to the base and follower gear pair input torques.

In fuel economy and powertrain efficiency studies, you can use
the Gearbox block to model ideal gear coupling and
the power transfer between common driveline elements such as transmissions,
engines, clutches, and differentials.

The Gearbox block uses these equations to approximate
the transmission dynamics.

ω˙BJB=ωBbB+ηNTFω˙FJF=ωFbF+ηTF

This constraint equation reduces the system to a one DOF system.

ωB=NωF

To express the ideal torque transfer, the block uses this relationship.

ηNTB+TF=0

### Efficiency

To account for the block efficiency, use the **Efficiency factors** parameter. This table summarizes the block implementation for each setting.

| Setting | Implementation |
| --- | --- |
| `Constant` | Constant efficiency that you can set with the **Constant efficiency factor, eta** parameter. |
| `Driveshaft torque, temperature and speed` | Efficiency as a function of base gear input torque, air temperature, and driveshaft speed. Use these parameters to specify the lookup table and breakpoints:  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    For the air temperature, you can either:  - Select **Input ambient temperature** to   create an input port. - Set a **Ambient temperature, Tamb**   parameter value.    To select the interpolation method, use the **Interpolation method** parameter. For more information, see Interpolation Methods. |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrBase` | Mechanical power from base shaft | *PBase* | PBase= ηTBωB |
| `PwrFlwr` | Mechanical power from follower shaft | *PFlwr* | PFlwr= ηTFωF |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrMechLoss` | Total power loss | *Png* | Png= −(Pt+Pd)+PsPt=ηTBωB+ηTFωF |
| `PwrDampLoss` | Power loss due to damping | *Pd* | Pd=−(bF|ωF|2+bB|ωB|2) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredShft` | Rate change of stored internal kinetic energy | *Ps* | Ps=(ωBω˙BJB+ωFω˙FJF) |

The equations use these variables.

|  |  |
| --- | --- |
| *TB* | Base gear input torque |
| *TF* | Follower gear output torque |
| *ωB* | Base gear angular velocity |
| *ωF* | Follower gear angular velocity |
| *JB* | Base gear rotational inertia |
| *JF* | Follower gear rotational inertia |
| *bB* | Base gear rotational viscous damping |
| *bF* | Follower gear rotational viscous damping |
| *N* | Torque transmission gear ratio |
| *η* | Gear efficiency |
| *Pt* | Total power |
| *Pd* | Power loss due to damping |
| *Ps* | Rate change of stored internal kinetic energy |
