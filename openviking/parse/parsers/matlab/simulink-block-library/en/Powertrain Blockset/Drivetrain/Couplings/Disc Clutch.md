---
type: simulink-block
title: 'Disc Clutch'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Couplings'
documentation_page: 'discclutch'
documentation_source_path: 'ref/discclutch.html'
language: en
---

# Disc Clutch

## Ports
```yaml
ports:
- name: Press
  summary: Applied clutch pressure scalar
  direction: input
- name: BTrq
  summary: Applied input torque scalar
  direction: input
- name: FTrq
  summary: Applied load torque scalar
  direction: input
- name: B
  summary: Applied drive shaft angular speed and torque two-way connector port
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: BSpd
  summary: Angular speed scalar
  direction: output
- name: FSpd
  summary: Angular speed scalar
  direction: output
- name: F
  summary: Output velocity and torque two-way connector port
  direction: output
```

### Input

### **Press** — Applied clutch pressure `scalar`

Base gear input torque, *Pc*,
in N·m^2.

### **BTrq** — Applied input torque `scalar`

Applied input torque, *Ti*,
typically from the engine crankshaft or dual mass flywheel damper, in
N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **FTrq** — Applied load torque `scalar`

Applied load torque, *To*,
typically from the differential or drive shaft, in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **B** — Applied drive shaft angular speed and torque two-way connector port

Applied drive shaft angular speed, *ωi*,
in rad/s. Applied drive shaft torque, *Ti*,
in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Two-way connection`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Base` | `BTrq` | | Applied input torque, typically from the engine crankshaft or dual mass flywheel damper | N·m |
| `BSpd` | | Applied drive shaft angular speed input | rad/s |
| `Flwr` | `FTrq` | | Applied load torque, typically from the differential | N·m |
| `FSpd` | | Drive shaft angular speed output | rad/s |
| `Cltch` | `CltchForce` | | Applied clutch force | N |
| `CltchLocked` | | Clutch lock status | NA |
| `CltchSpdRatio` | | Clutch speed ratio | NA |
| `CltchEta` | | Clutch power transmission efficiency | NA |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBase` | Applied base power | W |
| `PwrFlwr` | Applied follower output power | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Damping power loss | W |
| `PwrCltchSlipLoss` | Clutch slip power loss | W |
| `PwrStored` | `PwrStoredBase` | Rate change in base rotational kinetic energy | W |
| `PwrStoredFlwr` | Rate change in follower rotational kinetic energy | W |

### **BSpd** — Angular speed `scalar`

Applied drive shaft angular speed input,
*ωi*, in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **FSpd** — Angular speed `scalar`

Drive shaft angular speed output,
*ωo*, in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **F** — Output velocity and torque two-way connector port

Output drive shaft angular speed, *ωoi*,
in rad/s. Output drive shaft torque, *To*,
in N·m.

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
- name: Clutch force equivalent net radius, Reff
  summary: Radius 1 (default) | positive scalar
  group: ''
  block_parameter: Reff
  values: 1 (default) | positive scalar
- name: Number of disks, Ndisk
  summary: Ratio 1 (default) | positive scalar
  group: ''
  block_parameter: Ndisk
  values: 1 (default) | positive scalar
- name: Effective applied pressure area, Aeff
  summary: Pressure area .01 (default) | positive scalar
  group: ''
  block_parameter: Aeff
  values: .01 (default) | positive scalar
- name: Engagement pressure threshold, Peng
  summary: Pressure threshold 0 (default) | scalar
  group: ''
  block_parameter: Peng
  values: 0 (default) | scalar
- name: Input shaft inertia, Jin
  summary: Inertia .1 (default) | positive scalar
  group: ''
  block_parameter: Jin
  values: .1 (default) | positive scalar
- name: Output shaft inertia, Jout
  summary: Inertia .1 (default) | positive scalar
  group: ''
  block_parameter: Jout
  values: .1 (default) | positive scalar
- name: Kinetic friction coefficient, muk
  summary: Coefficient .3 (default) | positive scalar
  group: ''
  block_parameter: muk
  values: .3 (default) | positive scalar
- name: Static friction coefficient, mus
  summary: Coefficient .5 (default) | positive scalar
  group: ''
  block_parameter: mus
  values: .5 (default) | positive scalar
- name: Input shaft viscous damping, bin
  summary: Damping .001 (default) | positive scalar
  group: ''
  block_parameter: bin
  values: .001 (default) | positive scalar
- name: Output shaft viscous damping, bout
  summary: Damping .001 (default) | positive scalar
  group: ''
  block_parameter: bout
  values: .001 (default) | positive scalar
- name: Initial input shaft velocity, win_o
  summary: Initial velocity 0 (default) | scalar
  group: ''
  block_parameter: win_o
  values: 0 (default) | scalar
- name: Initial output shaft velocity, wout_o
  summary: Initial velocity 0 (default) | scalar
  group: ''
  block_parameter: wout_o
  values: 0 (default) | scalar
- name: Clutch actuation time constant, tauC
  summary: Constant .01 (default) | scalar
  group: ''
  block_parameter: tauC
  values: .01 (default) | scalar
- name: Start simulation with clutch locked
  summary: Select to initially lock clutch off (default) | on
  group: ''
  block_parameter: InitiallyLocked
  values: off (default) | on
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

### **Clutch force equivalent net radius, Reff** — Radius `1` (default) | positive scalar

Clutch force equivalent net radius, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Reff` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Number of disks, Ndisk** — Ratio `1` (default) | positive scalar

Number of disks, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ndisk` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Effective applied pressure area, Aeff** — Pressure area `.01` (default) | positive scalar

Effective applied pressure area, in m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aeff` |
| **Values:** | `.01` (default) | positive scalar |
| **Data Types:** | `double` |

### **Engagement pressure threshold, Peng** — Pressure threshold `0` (default) | scalar

Pressure to engage clutch, in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Peng` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Input shaft inertia, Jin** — Inertia `.1` (default) | positive scalar

Input shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jin` |
| **Values:** | `.1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Output shaft inertia, Jout** — Inertia `.1` (default) | positive scalar

Output shaft inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jout` |
| **Values:** | `.1` (default) | positive scalar |
| **Data Types:** | `double` |

### **Kinetic friction coefficient, muk** — Coefficient `.3` (default) | positive scalar

Kinetic friction coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `muk` |
| **Values:** | `.3` (default) | positive scalar |
| **Data Types:** | `double` |

### **Static friction coefficient, mus** — Coefficient `.5` (default) | positive scalar

Static friction coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mus` |
| **Values:** | `.5` (default) | positive scalar |
| **Data Types:** | `double` |

### **Input shaft viscous damping, bin** — Damping `.001` (default) | positive scalar

Input shaft viscous damping, in N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bin` |
| **Values:** | `.001` (default) | positive scalar |
| **Data Types:** | `double` |

### **Output shaft viscous damping, bout** — Damping `.001` (default) | positive scalar

Output shaft viscous damping, in N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bout` |
| **Values:** | `.001` (default) | positive scalar |
| **Data Types:** | `double` |

### **Initial input shaft velocity, win\_o** — Initial velocity `0` (default) | `scalar`

Input shaft initial velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `win_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial output shaft velocity, wout\_o** — Initial velocity `0` (default) | `scalar`

Input shaft initial velocity, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `wout_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch actuation time constant, tauC** — Constant `.01` (default) | `scalar`

Clutch actuation time constant, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tauC` |
| **Values:** | `.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Start simulation with clutch locked** — Select to initially lock clutch `off` (default) | `on`

Select to lock clutch initially.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitiallyLocked` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |
## Libraries

Powertrain Blockset / Drivetrain / Couplings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Idealized disc clutch coupler

The Disc Clutch block implements an idealized
disc clutch coupler. The block couples the rotary input and output
shafts through an idealized friction model. To determine the output
torque, the block uses friction parameters, relative slip velocity,
and applied input pressure.

In fuel economy and powertrain efficiency studies, you can use
the Disc Clutch block to model the mechanical power
transfer between common driveline elements such as transmissions,
engines, and differentials.

To approximate the torque response, the Disc Clutch block
implements friction and dynamic models that depend on the clutch lockup
condition. The block determines the locked or unlocked condition based
on an idealized dry clutch friction model. This table summarizes the
logic the block uses to determine the clutch condition.

| Clutch Condition | When |
| --- | --- |
| Unlocked | ωi≠ωoorTfmax<|JoTi−(Jobi−Jibo)ωi/oJo+Ji| |
| Locked | ωi=ωoandTfmax<|Ti−Ji(bi+bo)ωiJo+Ji+boωi| |

This table summarizes the friction and dynamic models that the
block uses for locked or unlocked clutch conditions.

| Clutch Condition | Friction Model | Dynamic Model |
| --- | --- | --- |
| Unlocked | Tfmax=Tkwhere,Tk=NdiscPcAeffReffμktanh[4(ωi−ωo)]Reff=2(Ro3-Ri3)3(Ro2-Ri2) andPc=max(Pc−Peng,0) | ω˙iJi=Ti−Tf−ωibiω˙oJo=Tf+To−ωobo |
| Locked | Tfmax=Tswhere,Ts=NdiscPcAeffReffμsReff=2(Ro3-Ri3)3(Ro2-Ri2) | ω˙i(Jo+Ji)=To−ωi(bi+bo)+Tiωi=ωo |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrBase` | Applied base power | ωiTi |
| `PwrFlwr` | Applied follower output power | ωoTo |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrDampLoss` | Damping power loss | −boωo2 −biωi2 |
| `PwrCltchSlipLoss` | Clutch slip power loss | −Tk(ωi−ωo) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredBase` | Rate change in base rotational kinetic energy | ω˙iωiJi |
| `PwrStoredFlwr` | Rate change in follower rotational kinetic energy | ω˙oωoJo |

The equations use these variables.

|  |  |
| --- | --- |
| *ωi* | Input shaft angular speed |
| *ωo* | Output shaft angular speed |
| *bi* | Input shaft viscous damping |
| *bo* | Output shaft viscous damping |
| *Ji* | Input shaft moment of inertia |
| *Jo* | Output shaft moment of inertia |
| *Tf* | Frictional torque |
| *Ti* | Net input torque |
| *Tk* | Kinetic frictional torque |
| *To* | Net output torque |
| *Ts* | Static frictional torque |
| *Tfmax* | Maximum frictional torque before slipping |
| *Pc* | Applied clutch pressure |
| *Peng* | Engagement pressure |
| *Aeff* | Effective area |
| *Ndisc* | Number of frictional discs |
| *Reff* | Effective clutch radius |
| *Ro* | Annular disk outer radius |
| *Ri* | Annular disk inner radius |
| *Re* | Effective tire radius while under load and for a given pressure |
| *μs* | Coefficient of static friction |
| *μk* | Coefficient of kinetic friction |
