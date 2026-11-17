---
type: simulink-block
title: 'Planetary Gear'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Couplings'
documentation_page: 'planetarygear'
documentation_source_path: 'ref/planetarygear.html'
language: en
---

# Planetary Gear

## Ports
```yaml
ports:
- name: SunTrq
  summary: Sun gear applied torque scalar
  direction: input
- name: CarrTrq
  summary: Carrier gear applied torque scalar
  direction: input
- name: RingTrq
  summary: Ring gear applied torque scalar
  direction: input
- name: C
  summary: Carrier gear angular speed and torque two-way connector port
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: SunSpd
  summary: Sun gear angular speed scalar
  direction: output
- name: CarrSpd
  summary: Carrier gear angular speed scalar
  direction: output
- name: RingSpd
  summary: Ring gear angular speed scalar
  direction: output
- name: S
  summary: Sun gear angular speed and torque two-way connector port
  direction: output
- name: R
  summary: Ring gear angular speed and torque two-way connector port
  direction: output
```

### Input

### **SunTrq** — Sun gear applied torque `scalar`

Sun gear input torque, *Ts*,
in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **CarrTrq** — Carrier gear applied torque `scalar`

Carrier gear input torque,
*Tc*, in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **RingTrq** — Ring gear applied torque `scalar`

Ring gear applied torque,
*Tr*, in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **C** — Carrier gear angular speed and torque two-way connector port

Carrier gear angular speed, *ωc*,
in rad/s. Carrier gear applied torque, *Tc*,
in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Two-way connection`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| Sun | `SunTrq` | | Sun gear applied torque | N·m |
| `SunSpd` | | Sun gear angular speed | rad/s |
| Carr | `CarrTrq` | | Carrier gear applied torque | N·m |
| `CarrSpd` | | Carrier gear angular speed | rad/s |
| Ring | `RingTrq` | | Ring gear applied torque | N·m |
| PwrInfo | `PwrTrnsfrd` | `PwrSun` | Sun gear applied power | W |
| `PwrCarr` | Carrier gear applied power | W |
| `PwrRing` | Ring gear applied power | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Mechanical damping loss | W |
| `PwrStored` | `PwrStoredPlntry` | Rate change in rotational kinetic energy | W |

### **SunSpd** — Sun gear angular speed `scalar`

Sun gear angular speed, *ωs*,
in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **CarrSpd** — Carrier gear angular speed `scalar`

Carrier gear angular speed,
*ωc*, in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **RingSpd** — Ring gear angular speed `scalar`

Ring gear angular speed, *ωr*,
in rad/s.

#### Dependencies

To create this port, for **Port Configuration**,
select `Simulink`.

### **S** — Sun gear angular speed and torque two-way connector port

Sun gear angular speed, *ωs*,
in rad/s. Sun gear applied torque,
*Ts*, in N·m.

#### Dependencies

To create this port, for **Port Configuration**,
select `Two-way connection`.

### **R** — Ring gear angular speed and torque two-way connector port

Ring gear angular speed, *ωr*,
in rad/s. Ring gear applied torque,
*Tr*, in N·m.

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
- name: Sun to planet ratio, Nsp
  summary: Ratio 30/23 (default) | positive scalar
  group: ''
  block_parameter: Nsp
  values: 30/23 (default) | positive scalar
- name: Sun to ring ratio, Nsr
  summary: Ratio 30/78 (default) | positive scalar
  group: ''
  block_parameter: Nsr
  values: 30/78 (default) | positive scalar
- name: Sun inertia, Js
  summary: Inertia .003 (default) | positive scalar
  group: ''
  block_parameter: Js
  values: .003 (default) | positive scalar
- name: Planet inertia, Jp
  summary: Inertia .001 (default) | positive scalar
  group: ''
  block_parameter: Jp
  values: .001 (default) | positive scalar
- name: Ring inertia, Jr
  summary: Inertia .01 (default) | positive scalar
  group: ''
  block_parameter: Jr
  values: .01 (default) | positive scalar
- name: Carrier inertia, Jc
  summary: Inertia .002 (default) | positive scalar
  group: ''
  block_parameter: Jc
  values: .002 (default) | positive scalar
- name: Sun viscous damping, bs
  summary: Damping .001 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: bs
  values: .001 (default) | scalar greater than or equal to 0
- name: Ring viscous damping, br
  summary: Damping .001 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: br
  values: .001 (default) | scalar greater than or equal to 0
- name: Planet viscous damping, bp
  summary: Damping .001 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: bp
  values: .001 (default) | scalar greater than or equal to 0
- name: Carrier viscous damping, bc
  summary: Damping .001 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: bc
  values: .001 (default) | scalar greater than or equal to 0
- name: Initial sun velocity, ws_o
  summary: Angular speed 0 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: ws_o
  values: 0 (default) | scalar greater than or equal to 0
- name: Initial carrier velocity, wc_o
  summary: Angular speed 0 (default) | scalar greater than or equal to 0
  group: ''
  block_parameter: wc_o
  values: 0 (default) | scalar greater than or equal to 0
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

- `SunTrq`
- `CarrTrq`
- `RingTrq`
- `SunSpd`
- `CarrSpd`
- `RingSpd`

Specifying `Two-way connection` creates these ports:

- `C`
- `S`
- `R`

### **Sun to planet ratio, Nsp** — Ratio `30/23` (default) | positive scalar

Sun-to-planet gear ratio, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Nsp` |
| **Values:** | `30/23` (default) | positive scalar |
| **Data Types:** | `double` |

### **Sun to ring ratio, Nsr** — Ratio `30/78` (default) | positive scalar

Sun-to-ring gear ratio, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Nsr` |
| **Values:** | `30/78` (default) | positive scalar |
| **Data Types:** | `double` |

### **Sun inertia, Js** — Inertia `.003` (default) | positive scalar

Sun gear inertia, *Js*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Js` |
| **Values:** | `.003` (default) | positive scalar |
| **Data Types:** | `double` |

### **Planet inertia, Jp** — Inertia `.001` (default) | positive scalar

Planet gear inertia, *Jp*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jp` |
| **Values:** | `.001` (default) | positive scalar |
| **Data Types:** | `double` |

### **Ring inertia, Jr** — Inertia `.01` (default) | positive scalar

Ring gear inertia, *Jr*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jr` |
| **Values:** | `.01` (default) | positive scalar |
| **Data Types:** | `double` |

### **Carrier inertia, Jc** — Inertia `.002` (default) | positive scalar

Carrier gear inertia, *Jc*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jc` |
| **Values:** | `.002` (default) | positive scalar |
| **Data Types:** | `double` |

### **Sun viscous damping, bs** — Damping `.001` (default) | scalar greater than or equal to 0

Sun gear viscous damping, *bs*,
N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bs` |
| **Values:** | `.001` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Ring viscous damping, br** — Damping `.001` (default) | scalar greater than or equal to 0

Ring gear viscous damping, *br*,
N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `br` |
| **Values:** | `.001` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Planet viscous damping, bp** — Damping `.001` (default) | scalar greater than or equal to 0

Planet gear viscous damping, *bp*,
N·m· s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bp` |
| **Values:** | `.001` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Carrier viscous damping, bc** — Damping `.001` (default) | scalar greater than or equal to 0

Carrier gear viscous damping,
*bc*, N·m· s/rad.

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

### **Initial sun velocity, ws\_o** — Angular speed `0` (default) | scalar greater than or equal to 0

Initial sun gear angular speed, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ws_o` |
| **Values:** | `0` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Initial carrier velocity, wc\_o** — Angular speed `0` (default) | scalar greater than or equal to 0

Initial carrier gear angular speed, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `wc_o` |
| **Values:** | `0` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |
## Libraries

Powertrain Blockset / Drivetrain / Couplings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Ideal planetary gear with sun, ring, and carrier

The Planetary Gear block implements an ideal
planetary gear coupling consisting of a rigidly coupled sun, ring,
and carrier gears. The block calculates the dynamic response to the
sun, carrier, and ring input torques.

In fuel economy and powertrain studies, you can use the Planetary
Gear block as a power-split device by coupling it to common
driveline elements such as transmissions, engines, clutches, and differentials.

These equations of motion represent the dynamic response of
the planetary gear.

ω˙sJs=ω˙sbs+Ts+Tpsω˙cJc=ω˙cbc+Tc+Tpcω˙sJr=ω˙rbr+Tr+Tprω˙pJp=ωpbp+Trp+Tsp+Tcp

To reduce the equations of motion, the block uses these kinematic
and geometric constraints.

ωcrc=rsωs+rpωpωrrr=rcωc+rpωprc=rs+rprr=rc+rp

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrSun` | Sun gear applied power | ωsTs |
| `PwrCarr` | Carrier gear applied power | ωcTc |
| `PwrRing` | Ring gear applied power | ωrTr |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrDampLoss` | Mechanical damping loss | −(bsωs2+bcωc2+brωr2+bpωp2) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredPlntry` | Rate change in rotational kinetic energy | ω˙sωsJs+ ω˙cωcJc+ω˙rωrJr+ ω˙pωpJp |

The equations use these variables.

|  |  |
| --- | --- |
| *ωc*, *ωp*, *ωr*, *ωs* | Carrier, planet, ring, and sun gear angular speed |
| *rc*, *rp*, *rr*, *rs* | Carrier, planet, ring, and sun gear angular radius |
| *Jc*, *Jp*, *Jr*, *Js* | Carrier, planet, ring, and sun gear inertia |
| *bc*, *bp*, *br*, *bs* | Carrier, planet, ring, and sun gear damping |
| *Tc*, *Tp*, *Tr*, *Ts* | Applied carrier, planet, ring, and sun gear torque |
| *Tps* | Torque applied from planet gear on sun gear |
| *Tpc* | Torque applied from planet gear on carrier gear |
| *Tpr* | Torque applied from planet gear on ring gear |
| *Trp* | Torque applied from ring gear on planet gear |
| *Tsp* | Torque applied from sun gear on planet gear |
| *Tcp* | Torque applied from carrier gear on planet gear |
