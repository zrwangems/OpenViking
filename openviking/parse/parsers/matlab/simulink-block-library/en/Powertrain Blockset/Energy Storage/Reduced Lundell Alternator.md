---
type: simulink-block
title: 'Reduced Lundell Alternator'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'reducedlundellalternator'
documentation_source_path: 'ref/reducedlundellalternator.html'
language: en
---

# Reduced Lundell Alternator

## Ports

### Inputs

### **RefVolt** — Alternator output voltage command `scalar`

Alternator output voltage command, in V.

### **AltSpd** — Angular speed `scalar`

Motor shaft input angular speed, in rad/s.

### **LdCurr** — Alternator load current `scalar`

Alternator load current, in A.

Do not connect the port to the alternator rated current, which is a
constant value. The block uses the alternator load current as the stator
winding current, *is*, to
determine the alternator voltage and motor torque. If you connect the
port to the rated alternator current, the block does not model the
dynamic effect of load current changes on the voltage and motor
torque.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `FldVolt` | | | Field winding voltage | A |
| `FldFlux` | | | Field flux | Wb |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | Mechanical power | W |
| `PwrBus` | Electrical power | W |
| `PwrNotTrnsfrd` | `PwrLoss` | Motor power loss | W |
| `PwrStored` | `PwrInd` | Electrical winding loss | W |

### **AltVolt** — Alternator output voltage `scalar`

Alternator output voltage, in V.

### **LdTrq** — Motor shaft torque `scalar`

Motor shaft torque, in N·m.

## Parameters

#### Machine Configuration

### **Voltage constant, Kv** — Constant `.1` (default) | `scalar`

Voltage constant, in V/rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kv` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Field winding resistance, Rf** — Resistance `0.2` (default) | `scalar`

Field winding resistance, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rf` |
| **Values:** | `0.2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Field winding inductance, Lf** — Inductance `0.002` (default) | `scalar`

Field winding inductance, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lf` |
| **Values:** | `0.002` (default) | `scalar` |
| **Data Types:** | `double` |

### **Stator winding resistance, Rs** — Resistance `0.01` (default) | `scalar`

Stator winding resistance, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rs` |
| **Values:** | `0.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Diode voltage drop, Vd** — Voltage `0.7` (default) | `scalar`

Diode voltage drop, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vd` |
| **Values:** | `0.7` (default) | `scalar` |
| **Data Types:** | `double` |

#### Voltage Regulator

### **Regulator bandwidth, Fv** — Bandwidth `2000` (default) | `scalar`

The regulator bandwidth, in Hz.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fv` |
| **Values:** | `2000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Current filter bandwidth, Fc** — Bandwidth `1000` (default) | `scalar`

The current filter bandwidth, in Hz.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fc` |
| **Values:** | `1000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Field voltage max, Vfmax** — Maximum field voltage `100` (default) | `scalar`

The maximum field voltage, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vfmax` |
| **Values:** | `100` (default) | `scalar` |
| **Data Types:** | `double` |

### **Field voltage min, Vfmin** — Minimum field voltage `-100` (default) | `scalar`

The minimum field voltage, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vfmin` |
| **Values:** | `-100` (default) | `scalar` |
| **Data Types:** | `double` |

#### Mechanical Losses

### **Coulomb friction, Kc** — Friction `0` (default) | `scalar`

Coulomb friction, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kc` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Viscous friction, Kb** — Friction `0` (default) | `scalar`

Viscous friction, in N·m/rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kb` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Windage, Kw** — Windage `0` (default) | `scalar`

Windage, in
N·m/rad2/s2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kw` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Energy Storage and Auxiliary Drive / Alternator

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Reduced Lundell (claw-pole) alternator with an external voltage regulator

The Reduced Lundell Alternator block implements a reduced Lundell (claw-pole)
alternator with an external voltage regulator. The back-electromotive force (EMF)
voltage is proportional to the input velocity and field current. The motor operates as a
source torque to the internal combustion engine.

Use the Reduced Lundell Alternator block:

- To model an automotive electrical system
- In an engine model with a front-end accessory drive
  (FEAD)

The calculated motor shaft torque is in the opposite direction
of the engine speed. You can:

- Tune the external voltage regulator to a desired bandwidth.
  The stator current and two diode drops reduce the stator voltage.
- Filter the load current to desired bandwidth. The
  load current has a lower saturation of 0 A.

The Reduced Lundell Alternator block implements equations for the
electrical, control, and mechanical systems that use these variables.

### Electrical

To calculate voltages, the block uses these equations.

| Calculation | Equations |
| --- | --- |
| Alternator output voltage | vs=Kvifω−Rsis−2Vd |
| Field winding voltage | vf= Rfif+Lfdifdt |

### Control

The controller assumes no resistance or voltage drop.

| Calculation | Equations |
| --- | --- |
| Field winding voltage transform | Vf(s)=RfIf(s)+sLfIf(s) |
| Field winding current transform | If(s)=Vf(s)(Rf+sLf) |
| Open loop electrical transfer function | G(s)= Vs(s)Vf(s)= Kvω(Rf+sLf) |
| Open loop voltage regulator transfer function | GC(s)=  Vf(s)Vref(s) |
| Closed loop transfer function | T(s)= G(s)Gc(s)1+G(s)Gc(s) |
| Closed loop controller design | T(s)=1τs+1→ G(s)Gc(s)= 1τs  GC(s)= Kg (Kp+ Kis)  G(s)GC(s)= Kvω(Rf+sLf)Kg (Kp+ Kis)  Kp=Lf  ,Ki=Rf ,and Kg=2πfKvω |

### Mechanical

To calculate torques, the block uses these equations.

| Calculation | Equations |
| --- | --- |
| Electrical torque | τelec= (Kvifω)iload |
| Frictional torque | τfriction= Kbω |
| Windage torque | τwindage=Kwω2 |
| Torque at start | τstart=Kc when ω=0 |
| Motor shaft torque | τmech=τelec+τfriction+τwindage+τstart |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Mechanical power | *Pmot* | Pmot= ωτmech |
| `PwrBus` | Electrical power | *Pbus* | Pbus= − vsiload |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrLoss` | Motor power loss | *Ploss* | Ploss= −(Pmot+Pbus−Pind) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrInd` | Electrical winding loss | *Pind* | Pind= Lfifdifdt |

The equations use these variables.

|  |  |
| --- | --- |
| *vref* | Alternator output voltage command |
| *vf* | Field winding voltage |
| *if* | Field winding current |
| *is* | Stator winding current |
| *Vd* | Diode voltage drop |
| *Rf* | Field winding resistance |
| *Rs* | Stator winding resistance |
| *Lf* | Field winding inductance |
| *Kv* | Voltage constant |
| *Fv* | Voltage regulator bandwidth |
| *Fc* | Input current filter bandwidth |
| *Vfmax* | Field control voltage upper saturation limit |
| *Vfmin* | Field control voltage lower saturation limit |
| *Kc* | Coulomb friction coefficient |
| *Kb* | Viscous friction coefficient |
| *Kw* | Windage coefficient |
| *ω* | Motor shaft angular speed |
| *iload* | Alternator load current |
| *vs* | Alternator output voltage |
| *τmech*, *Tmech* | Motor shaft torque |
