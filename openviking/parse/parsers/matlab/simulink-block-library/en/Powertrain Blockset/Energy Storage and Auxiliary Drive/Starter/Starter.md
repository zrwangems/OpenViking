---
type: simulink-block
title: 'Starter'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage and Auxiliary Drive / Starter'
documentation_page: 'starter'
documentation_source_path: 'ref/starter.html'
language: en
---

# Starter

## Ports
```yaml
ports:
- name: MtrSpd
  summary: Angular speed scalar
  direction: input
- name: StartVolt
  summary: Armature and field voltage scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: LdCurr
  summary: Starter motor load current scalar
  direction: output
- name: MtrTrq
  summary: Starter motor shaft torque scalar
  direction: output
```

### Inputs

### **MtrSpd** — Angular speed `scalar`

Motor shaft angular speed, in rad/s.

### **StartVolt** — Armature and field voltage `scalar`

- Armature winding voltage
  *Va* and
  field winding voltage
  *Vf*, in
  V.
- In series excited DC motor, armature and field winding
  voltage
  *Vaf*.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `ArmCurr` | | | Armature winding current | A |
| `FldCurr` | | | Field winding current | A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | Mechanical power | W |
| `PwrBus` | Electrical power | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Motor power loss | W |
| `PwrStored` | `PwrInd` | Electrical inductance | W |

### **LdCurr** — Starter motor load current `scalar`

Starter motor load current, in A.

### **MtrTrq** — Starter motor shaft torque `scalar`

Starter motor shaft torque, in N·m.
## Parameters
```yaml
parameters:
- name: Motor Type
  summary: Select motor type Separately Excited DC Motor (default) | Permanent Magnet Excited DC Motor | Series Connection
    DC Motor
  group: ''
  block_parameter: machine_type
  values: Separately Excited DC Motor (default) | Permanent Magnet Excited DC Motor | Series Connection DC Motor
- name: Armature winding resistance, Ra
  summary: Resistance 1 (default) | scalar
  group: ''
  block_parameter: Ra
  values: 1 (default) | scalar
- name: Armature winding inductance, La
  summary: Inductance .1 (default) | scalar
  group: ''
  block_parameter: La
  values: .1 (default) | scalar
- name: Field winding resistance, Rf
  summary: Resistance .3 (default) | scalar
  group: ''
  block_parameter: Rf
  values: .3 (default) | scalar
- name: Field winding inductance, Lf
  summary: Inductance .2 (default) | scalar
  group: ''
  block_parameter: Lf
  values: .2 (default) | scalar
- name: Mutual inductance, Laf
  summary: Inductance .3 (default) | scalar
  group: ''
  block_parameter: Laf
  values: .3 (default) | scalar
- name: Initial armature current and field current, Iaf
  summary: Current [0 0] (default) | vector
  group: ''
  block_parameter: Iaf
  values: '[0 0] (default) | vector'
- name: Armature winding resistance, Rapm
  summary: Resistance .5 (default) | scalar
  group: ''
  block_parameter: Rapm
  values: .5 (default) | scalar
- name: Armature winding inductance, Lapm
  summary: Inductance .1 (default) | scalar
  group: ''
  block_parameter: Lapm
  values: .1 (default) | scalar
- name: Torque constant, Kt
  summary: Motor torque constant .1 (default) | scalar
  group: ''
  block_parameter: Kt
  values: .1 (default) | scalar
- name: Initial armature current, Ia
  summary: Current .1 (default) | scalar
  group: ''
  block_parameter: Ia
  values: .1 (default) | scalar
- name: Total resistance, Rser
  summary: Resistance .1 (default) | scalar
  group: ''
  block_parameter: Rser
  values: .1 (default) | scalar
- name: Total inductance, Lser
  summary: Inductance .1 (default) | scalar
  group: ''
  block_parameter: Lser
  values: .1 (default) | scalar
- name: Initial current, Iafser
  summary: Current 0 (default) | scalar
  group: ''
  block_parameter: Iafser
  values: 0 (default) | scalar
- name: Mutual inductance, Lafser
  summary: Inductance .3 (default) | scalar
  group: ''
  block_parameter: Lafser
  values: .3 (default) | scalar
```

#### Configuration

### **Motor Type** — Select motor type `Separately Excited DC Motor` (default) | `Permanent Magnet Excited DC Motor` | `Series Connection DC Motor`

Select one of the three motor types.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `machine_type` |
| **Values:** | `Separately Excited DC Motor` (default) | `Permanent Magnet Excited DC Motor` | `Series Connection DC Motor` |
| **Data Types:** | `character vector` |

#### Dependencies

The table summarizes the motor parameter dependencies.

| Motor Type | Enables Motor Parameter |
| --- | --- |
| `Separately Excited DC Motor` | **Armature winding resistance, Ra** |
| **Armature winding inductance, La** |
| **Field winding resistance Rf** |
| **Field winding inductance, Lf** |
| **Mutual inductance, Laf** |
| **Initial armature and field current, Iaf** |
| `Permanent Magnet Excited DC Motor` | **Armature winding resistance, Rapm** |
| **Armature winding inductance, Lapm** |
| **Torque constant, Kt** |
| **Initial armature current, Ia** |
| `Series Connection DC Motor` | **Total resistance, Rser** |
| **Total inductance, Lser** |
| **Initial current, Iafser** |
| **Mutual inductance, Lafser** |

#### Separately Excited DC Motor

### **Armature winding resistance, Ra** — Resistance `1` (default) | `scalar`

Armature winding resistance, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ra` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Separately Excited DC
Motor` for the **Motor Type**
parameter.

### **Armature winding inductance, La** — Inductance `.1` (default) | `scalar`

Armature winding inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `La` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Separately Excited DC
Motor` for the **Motor Type**
parameter.

### **Field winding resistance, Rf** — Resistance `.3` (default) | `scalar`

Field winding resistance, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rf` |
| **Values:** | `.3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Separately Excited DC
Motor` for the **Motor Type**
parameter.

### **Field winding inductance, Lf** — Inductance `.2` (default) | `scalar`

Field winding inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lf` |
| **Values:** | `.2` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Separately Excited DC
Motor` for the **Motor Type**
parameter.

### **Mutual inductance, Laf** — Inductance `.3` (default) | `scalar`

Mutual inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Laf` |
| **Values:** | `.3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Separately Excited DC
Motor` for the **Motor Type**
parameter.

### **Initial armature current and field current, Iaf** — Current `[0 0]` (default) | `vector`

Initial armature and field current, in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Iaf` |
| **Values:** | `[0 0]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Separately Excited DC
Motor` for the **Motor Type**
parameter.

#### Permanent Magnet Excited DC Motor

### **Armature winding resistance, Rapm** — Resistance `.5` (default) | `scalar`

Armature winding resistance, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rapm` |
| **Values:** | `.5` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Permanent Magnet Excited
DC Motor` for the **Motor Type**
parameter.

### **Armature winding inductance, Lapm** — Inductance `.1` (default) | `scalar`

Armature winding inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lapm` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Permanent Magnet Excited
DC Motor` for the **Motor Type**
parameter.

### **Torque constant, Kt** — Motor torque constant `.1` (default) | `scalar`

Motor torque constant, in N·m/A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kt` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Permanent Magnet Excited
DC Motor` for the **Motor Type**
parameter.

### **Initial armature current, Ia** — Current `.1` (default) | `scalar`

Initial armature current, in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ia` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Permanent Magnet Excited
DC Motor` for the **Motor Type**
parameter.

#### Series Connection DC Motor

### **Total resistance, Rser** — Resistance `.1` (default) | `scalar`

Series connected field and armature resistance, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rser` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Series Excited DC
Motor` for the **Motor Type**
parameter.

### **Total inductance, Lser** — Inductance `.1` (default) | `scalar`

Series connected field and armature inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lser` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Series Excited DC
Motor` for the **Motor Type**
parameter.

### **Initial current, Iafser** — Current `0` (default) | `scalar`

Initial series current, in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Iafser` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Series Excited DC
Motor` for the **Motor Type**
parameter.

### **Mutual inductance, Lafser** — Inductance `.3` (default) | `scalar`

Field and armature mutual inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lafser` |
| **Values:** | `.3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select `Series Excited DC
Motor` for the **Motor Type**
parameter.
## Libraries

Powertrain Blockset / Energy Storage and Auxiliary Drive / Starter

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Starter as a DC motor

The Starter block implements a starter assembly as a separately excited DC
motor, permanent magnet DC motor, or series connection DC motor. The motor operates as a
torque source to an internal combustion engine.

Use the Starter block:

- In an engine model with a front-end accessory drive
  (FEAD)
- To model engine start and stop scenarios

The Starter block supports only an angular speed
input to the DC motor. A load torque input requires engine dynamics.

### Separately Excited DC Motor

In a separately excited DC motor, the field winding is connected to a separate
source of DC power.

The relationship between the field winding voltage, field resistance, and field
inductance is given by:

Vf=Lfdifdt+Rfif

The counter-electromotive force is a product of the field resistance, mutual
inductance, and motor shaft angular speed:

EMF=LaifLafω

The armature voltage is given by:

Va=Ladiadt+Raia+ EMF

The starter motor current load is the sum of the field winding current and
armature winding current:

iload= if+ ia

The starter motor shaft torque is the product of the armature current, field
current, and mutual inductance:

Tmech= iaifLaf

### Permanent Magnet DC Motor

In a permanent magnet DC motor, the magnets establish the excitation flux, so
there is no field current.

The counter-electromotive force is proportional to the motor shaft angular speed:

EMF= Ktω

The armature voltage is given by:

Va=Ladiadt+Raia+ EMF

The starter motor current load is equal to the armature winding current:

iload= ia

The starter motor shaft torque is proportional to the armature winding current:

Tmech= Ktia

### Series Excited DC Motor

A series excited DC motor connects the armature and field windings in series with
a common DC power source.

The counter-electromotive force is a product of the field and armature initial
series current, field, and armature mutual inductance and motor shaft angular speed:

EMF=iafLafω

The field and armature winding voltage is given by:

Vaf=Lserdiafdt+Rseriaf+ EMF

The starter motor current load is equal to the field and armature series current:

iload= iaf

The starter motor shaft torque is the product of the squared field and armature
series current and the field and armature mutual inductance:

Tmech= iaf2Laf

For motor stability, the motor shaft angular speed must be greater than the ratio
of the series connected field and armature resistance to the mutual inductance:

ω>−RserLaf

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Mechanical power | *Pmot* | Pmot= −ωTmech |
| `PwrBus` | Electrical power | *Pbus* | Separately excited DC motor  Pbus= vaia+vfif |
| PM excited DC motor  Pbus= vaia |
| Series excited DC motor  Pbus= vafiaf |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLoss` | Motor losses | *Ploss* | Ploss= −(Pmot+Pbus−Pind) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrInd` | Electrical inductance | *Pind* | Separately excited DC motor  Pind= Lfifdifdt+Laiadiadt |
| PM excited DC motor  Pind= Laiadiadt |
| Series excited DC motor  Pind=Lseriafdiafdt |

The equations use these variables.

|  |  |
| --- | --- |
| *Ra* | Armature winding resistance |
| *La* | Armature winding inductance |
| *EMF* | Counter-electromotive force |
| *Rf* | Field winding resistance |
| *Lf* | Field winding inductance |
| *Laf* | Field and armature mutual inductance |
| *ia* | Armature winding current |
| *if* | Field winding current |
| *Kt* | Motor torque constant |
| *ω* | Motor shaft angular speed |
| *Va* | Armature winding voltage |
| *Vf* | Field winding voltage |
| *Vaf* | Field and armature winding voltage |
| *iaf* | Field and armature series current |
| *Rser* | Series connected field and armature resistance |
| *Lser* | Series connected field and armature inductance |
| *iload* | Starter motor current load |
| *Tmech* | Starter motor shaft torque |
