---
type: simulink-block
title: 'Flux-Based PM Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motor Controllers'
documentation_page: 'fluxbasedpmcontroller'
documentation_source_path: 'ref/fluxbasedpmcontroller.html'
language: en
---

# Flux-Based PM Controller

## Ports
```yaml
ports:
- name: SpdReq
  summary: Rotor speed command scalar
  direction: input
- name: TrqCmd
  summary: Torque command scalar
  direction: input
- name: BusVolt
  summary: DC bus voltage scalar
  direction: input
- name: PhaseCurrA
  summary: Current scalar
  direction: input
- name: PhaseCurrB
  summary: Current scalar
  direction: input
- name: SpdFdbk
  summary: Rotor speed scalar
  direction: input
- name: PosFdbk
  summary: Rotor electrical angle scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: BusCurr
  summary: Bus current scalar
  direction: output
- name: PhaseVolt
  summary: Stator terminal voltages array
  direction: output
```

### Input

### **SpdReq** — Rotor speed command `scalar`

Rotor speed command, *ω\*m*, in
rad/s.

#### Dependencies

To create this port, select `Speed
Control` for the **Control Type**
parameter.

### **TrqCmd** — Torque command `scalar`

Torque command, *T\**, in N·m.

#### Dependencies

To create this port, select `Torque
Control` for the **Control Type**
parameter.

### **BusVolt** — DC bus voltage `scalar`

DC bus voltage, *vbus*, in
V.

### **PhaseCurrA** — Current `scalar`

Stator current phase a, *ia*,
in A.

### **PhaseCurrB** — Current `scalar`

Stator current phase b, *ib*,
in A.

### **SpdFdbk** — Rotor speed `scalar`

Rotor speed, *ωm*, in
rad/s.

### **PosFdbk** — Rotor electrical angle `scalar`

Rotor electrical angle, *Θm*,
in rad.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | Description | Units |
| --- | --- | --- |
| `SrcPwr` | Source power | W |
| `LdPwr` | Load power | W |
| `PwrLoss` | Power loss | W |
| `MtrTrqEst` | Estimated motor torque | N·m |

### **BusCurr** — Bus current `scalar`

Estimated DC bus current,
*ibus*, in A.

### **PhaseVolt** — Stator terminal voltages `array`

Stator terminal voltages,
*Va*,
*Vb*, and
*Vc*, in V.
## Parameters
```yaml
parameters:
- name: Control Type
  summary: Select control Torque Control (default) | Speed Control
  group: ''
  block_parameter: control_type
  values: Torque Control (default) | Speed Control
- name: Number of pole pairs, PolePairs
  summary: Poles 4 (default) | scalar
  group: ''
  block_parameter: PolePairs
  values: 4 (default) | scalar
- name: Vector of d-axis current breakpoints, id_index
  summary: Current vector
  group: ''
  block_parameter: id_index
  values: vector
- name: Vector of q-axis current breakpoints, iq_index
  summary: current vector
  group: ''
  block_parameter: iq_index
  values: vector
- name: Corresponding d-axis flux, lambda_d
  summary: Flux vector
  group: ''
  block_parameter: lambda_d
  values: vector
- name: Corresponding q-axis flux, lambda_q
  summary: Flux vector
  group: ''
  block_parameter: lambda_q
  values: vector
- name: Sample time for the torque control, Tst
  summary: Time 1e-4 (default) | scalar
  group: ''
  block_parameter: Tst
  values: 1e-4 (default) | scalar
- name: D-axis proportional gain, Kp_d
  summary: Gain 2.4056 (default) | scalar
  group: ''
  block_parameter: Kp_d
  values: 2.4056 (default) | scalar
- name: Q-axis proportional gain, Kp_q
  summary: Gain 2.4056 (default) | scalar
  group: ''
  block_parameter: Kp_q
  values: 2.4056 (default) | scalar
- name: D-axis integral gain, Ki_d
  summary: Gain 192.45 (default) | scalar
  group: ''
  block_parameter: Ki_d
  values: 192.45 (default) | scalar
- name: Q-axis integral gain, Ki_q
  summary: Gain 192.45 (default) | scalar
  group: ''
  block_parameter: Ki_q
  values: 192.45 (default) | scalar
- name: Vector of speed breakpoints, wbp
  summary: Breakpoints vector
  group: ''
  block_parameter: wbp
  values: vector
- name: Vector of torque breakpoints, tbp
  summary: Breakpoints vector
  group: ''
  block_parameter: tbp
  values: vector
- name: Corresponding d-axis current reference, id_ref
  summary: Current vector
  group: ''
  block_parameter: id_ref
  values: vector
- name: Corresponding q-axis current reference, iq_ref
  summary: Current vector
  group: ''
  block_parameter: iq_ref
  values: vector
- name: Speed regulation time constant, Ksf
  summary: Time .1 (default) | scalar
  group: ''
  block_parameter: Ksf
  values: .1 (default) | scalar
- name: Proportional gain, Kp_w
  summary: Gain 0.40475 (default) | scalar
  group: ''
  block_parameter: Kp_w
  values: 0.40475 (default) | scalar
- name: Integral gain, Ki_w
  summary: Gain 10.1615 (default) | scalar
  group: ''
  block_parameter: Ki_w
  values: 10.1615 (default) | scalar
- name: Inertia compensation, Jcomp
  summary: Inertia 0.0027 (default) | scalar
  group: ''
  block_parameter: Jcomp
  values: 0.0027 (default) | scalar
- name: Static friction, Fs
  summary: Friction 0 (default) | scalar
  group: ''
  block_parameter: Fs
  values: 0 (default) | scalar
- name: Viscous damping compensation, Fv
  summary: Dampint 0.0004924 (default) | scalar
  group: ''
  block_parameter: Fv
  values: 0.0004924 (default) | scalar
- name: Parameterize losses by
  summary: Select type Single efficiency measurement (default) | Tabulated loss data | Tabulated efficiency data
  group: ''
  block_parameter: param_loss
  values: Single efficiency measurement (default) | Tabulated loss data | Tabulated efficiency data
- name: Overall inverter efficiency, eff
  summary: Constant 98 (default) | scalar
  group: ''
  block_parameter: eff
  values: 98 (default) | scalar
- name: Vector of speeds (w) for tabulated loss, w_loss_bp
  summary: Breakpoints [0 200 400 600 800 1000] (default) | 1-by-M vector
  group: ''
  block_parameter: w_loss_bp
  values: '[0 200 400 600 800 1000] (default) | 1-by-M vector'
- name: Vector of torques (T) for tabulated loss, T_loss_bp
  summary: Breakpoints [0 25 50 75 100] (default) | 1-by-N vector
  group: ''
  block_parameter: T_loss_bp
  values: '[0 25 50 75 100] (default) | 1-by-N vector'
- name: Corresponding losses, losses_table
  summary: Table [100 100 100 100 100;100 150 200 250 300;100 200 300 400 500;100 250 400 550 700;100 300 500 700 900;100
    350 600 850 1100] (default) | M-by-N array
  group: ''
  block_parameter: losses_table
  values: M-by-N array
- name: Vector of speeds (w) for tabulated efficiency, w_eff_bp
  summary: Breakpoints [200 400 600 800 1000] (default) | 1-by-M vector
  group: ''
  block_parameter: w_eff_bp
  values: '[200 400 600 800 1000] (default) | 1-by-M vector'
- name: Vector of torques (T) for tabulated efficiency, T_eff_bp
  summary: Breakpoints [25 50 75 100] (default) | 1-by-N vector
  group: ''
  block_parameter: T_eff_bp
  values: '[25 50 75 100] (default) | 1-by-N vector'
- name: Corresponding efficiency, efficiency_table
  summary: Table [96.2 98.1 98.7 99;98.1 99 99.4 99.5;98.7 99.4 99.6 99.7;99 99.5 99.7 99.8;99.2 99.6 99.7 99.8] (default)
    | M-by-N array
  group: ''
  block_parameter: efficiency_table
  values: M-by-N array
```

#### Block Options

### **Control Type** — Select control `Torque Control` (default) | `Speed Control`

If you select `Torque Control`, the block does
not implement the speed controller.

This table summarizes the port configurations.

| Port Configuration | Creates Ports |
| --- | --- |
| `Speed Control` | `SpdReq` |
| `Torque Control` | `TrqCmd` |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `control_type` |
| **Values:** | `Torque Control` (default) | `Speed Control` |
| **Data Types:** | `character vector` |

#### Motor Parameters

### **Number of pole pairs, PolePairs** — Poles `4` (default) | `scalar`

Motor pole pairs, *P*.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `PolePairs` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Vector of d-axis current breakpoints, id\_index** — Current `vector`

*d*-axis current,
*id\_index*, in A.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `id_index` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Vector of q-axis current breakpoints, iq\_index** — current `vector`

*q*-axis current,
*iq\_index*, in A.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `iq_index` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Corresponding d-axis flux, lambda\_d** — Flux `vector`

*d*-axis flux,
*λd*, in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `lambda_d` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Corresponding q-axis flux, lambda\_q** — Flux `vector`

*q*-axis flux,
*λq*, in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `lambda_q` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Current Controller

### **Sample time for the torque control, Tst** — Time `1e-4` (default) | `scalar`

Torque control sample time, *Tst*,
in s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Tst` |
| **Values:** | `1e-4` (default) | `scalar` |
| **Data Types:** | `double` |

### **D-axis proportional gain, Kp\_d** — Gain `2.4056` (default) | `scalar`

*d*-axis proportional gain,
*Kpd*, in V/A.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp_d` |
| **Values:** | `2.4056` (default) | `scalar` |
| **Data Types:** | `double` |

### **Q-axis proportional gain, Kp\_q** — Gain `2.4056` (default) | `scalar`

*q*-axis proportional gain,
*Kpq*, in V/A.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp_q` |
| **Values:** | `2.4056` (default) | `scalar` |
| **Data Types:** | `double` |

### **D-axis integral gain, Ki\_d** — Gain `192.45` (default) | `scalar`

*d*-axis integral gain,
*Kid*, in V/A·s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Ki_d` |
| **Values:** | `192.45` (default) | `scalar` |
| **Data Types:** | `double` |

### **Q-axis integral gain, Ki\_q** — Gain `192.45` (default) | `scalar`

*q*- axis integral gain,
*Kiq*, in V/A·s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Ki_q` |
| **Values:** | `192.45` (default) | `scalar` |
| **Data Types:** | `double` |

### **Vector of speed breakpoints, wbp** — Breakpoints `vector`

Speed breakpoints, *ωbp*, in
rad/s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `wbp` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Vector of torque breakpoints, tbp** — Breakpoints `vector`

Torque breakpoints, *Tbp*, in
N·m.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `tbp` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Corresponding d-axis current reference, id\_ref** — Current `vector`

*d*-axis reference current,
*idref*, in A.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `id_ref` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Corresponding q-axis current reference, iq\_ref** — Current `vector`

*q*-axis reference current,
*iqref*, in A.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `iq_ref` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Speed Controller

### **Speed regulation time constant, Ksf** — Time `.1` (default) | `scalar`

Speed regulator time constant,
*Ksf*, in 1/s.

#### Dependencies

To enable this parameter, for the **Control Type**
parameter, select `Speed Control`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Ksf` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Proportional gain, Kp\_w** — Gain `0.40475` (default) | `scalar`

Proportional gain, *Kpω*, in
N·m/(rad/s).

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp_w` |
| **Values:** | `0.40475` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Control Type**
parameter, select `Speed Control`.

### **Integral gain, Ki\_w** — Gain `10.1615` (default) | `scalar`

Integral gain, *Kiω*
N·m/rad.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Ki_w` |
| **Values:** | `10.1615` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Control Type**
parameter, select `Speed Control`.

### **Inertia compensation, Jcomp** — Inertia `0.0027` (default) | `scalar`

Inertia compensation, in kg·m^2.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Jcomp` |
| **Values:** | `0.0027` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Control Type**
parameter, select `Speed Control`.

### **Static friction, Fs** — Friction `0` (default) | `scalar`

Static friction, in N·m.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Fs` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Control Type**
parameter, select `Speed Control`.

### **Viscous damping compensation, Fv** — Dampint `0.0004924` (default) | `scalar`

Viscous damping compensation, in N·m/(rad/s).

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Fv` |
| **Values:** | `0.0004924` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Control Type**
parameter, select `Speed Control`.

#### Electrical Losses

### **Parameterize losses by** — Select type `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated efficiency data`

| Setting | Block Implementation |
| --- | --- |
| `Single efficiency measurement` | Electrical loss calculated using a constant value for inverter efficiency. |
| `Tabulated loss data` | Electrical loss calculated as a function of motor speeds and load torques. |
| `Tabulated efficiency data` | Electrical loss calculated using inverter efficiency that is a function of motor speeds and load torques.    - Converts the efficiency values you provide into losses and uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or zero torque. Losses are assumed zero when either torque or speed is zero. - Uses linear interpolation to determine losses. Provide tabulated data for low speeds and low torques, as required, to get the desired level of accuracy for lower power conditions. - Does not extrapolate loss values for speed and torque magnitudes that exceed the range of the table. |

For best practice, use `Tabulated loss data` instead of `Tabulated efficiency data`:

- Efficiency becomes ill defined for zero speed or zero torque.
- You can account for fixed losses that are still present for zero speed or torque.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `param_loss` |
| **Values:** | `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated efficiency data` |
| **Data Types:** | `character vector` |

### **Overall inverter efficiency, eff** — Constant `98` (default) | `scalar`

Overall inverter efficiency, *Eff*, in %.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eff` |
| **Values:** | `98` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Vector of speeds (w) for tabulated loss, w\_loss\_bp** — Breakpoints `[0 200 400 600 800 1000]` (default) | `1`-by-`M` vector

Speed breakpoints for lookup table when calculating losses, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_loss_bp` |
| **Values:** | `[0 200 400 600 800 1000]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Vector of torques (T) for tabulated loss, T\_loss\_bp** — Breakpoints `[0 25 50 75 100]` (default) | `1`-by-`N` vector

Torque breakpoints for lookup table when calculating losses, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_loss_bp` |
| **Values:** | `[0 25 50 75 100]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Corresponding losses, losses\_table** — Table `[100 100 100 100 100;100 150 200 250 300;100 200 300 400 500;100 250 400 550 700;100 300 500 700 900;100 350 600 850 1100]` (default) | `M`-by-`N` array

Array of values for electrical losses as a function of `M` speeds
and `N` torques, in W. Each value specifies the losses for a
specific combination of speed and torque. The matrix size must match the dimensions
defined by the speed and torque vectors.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `losses_table` |
| **Values:** | `M`-by-`N` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated loss data`.

### **Vector of speeds (w) for tabulated efficiency, w\_eff\_bp** — Breakpoints `[200 400 600 800 1000]` (default) | `1`-by-`M` vector

Speed breakpoints for lookup table when calculating efficiency, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `w_eff_bp` |
| **Values:** | `[200 400 600 800 1000]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated efficiency data`.

### **Vector of torques (T) for tabulated efficiency, T\_eff\_bp** — Breakpoints `[25 50 75 100]` (default) | `1`-by-`N` vector

Torque breakpoints for lookup table when calculating efficiency, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_eff_bp` |
| **Values:** | `[25 50 75 100]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated efficiency data`.

### **Corresponding efficiency, efficiency\_table** — Table `[96.2 98.1 98.7 99;98.1 99 99.4 99.5;98.7 99.4 99.6 99.7;99 99.5 99.7 99.8;99.2 99.6 99.7 99.8]` (default) | `M`-by-`N` array

Array of efficiency as a function of `M` speeds and
`N` torque, in %. Each value specifies the efficiency for a
specific combination of speed and torque. The matrix size must match the dimensions
defined by the speed and torque vectors.

The block ignores efficiency values for zero speed or zero torque. Losses are zero
when either torque or speed is zero. The block uses linear interpolation.

To get the desired level of accuracy for lower power conditions, you can provide
tabulated data for low speeds and low torques.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `efficiency_table` |
| **Values:** | `M`-by-`N` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for **Parameterize losses by**, select
`Tabulated efficiency data`.
## Libraries

Powertrain Blockset / Propulsion / Electric Motor Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Controller for a flux-based permanent magnet synchronous motor

The Flux Based PM Controller block implements a flux-based,
field-oriented controller for an interior permanent magnet synchronous motor (PMSM) with
an optional outer-loop speed controller. The internal torque control implements
strategies for achieving maximum torque per ampere (MTPA) and weakening the magnetic
flux. You can specify either the speed or torque control type.

The Flux Based PM Controller implements equations for speed control,
torque determination, regulators, transforms, and motors.

The figure illustrates the information flow in the block.

Schematic showing information flow for speed control, torque determination, regulators, transforms, and motors.

The block implements equations using these variables.

|  |  |
| --- | --- |
| *ω* | Rotor speed |
| *ω\** | Rotor speed command |
| *T\** | Torque command |
| *id*  *i\*d* | *d*-axis current  *d*-axis current command |
| *iq*  *i\*q* | *q*-axis current  *q*-axis current command |
| *vd*,  *v\*d* | *d*-axis voltage  *d*-axis voltage command |
| *vq*  *v\*q* | *q*-axis voltage  *q*-axis voltage command |
| *va*, *vb*, *vc* | Stator phase a, b, c voltages |
| *ia*, *ib*, *ic* | Stator phase a, b, c currents |

### Speed Controller

To implement the speed controller, select the **Control Type**
parameter `Speed Control`. If you select the
**Control Type** parameter `Torque
Control`, the block does not implement the speed controller.

The speed controller determines the torque command by implementing a state filter,
and calculating the feedforward and feedback commands. If you do not implement the
speed controller, input a torque command to the Flux Based PM
Controller block.

Schematic showing state filter connected to command feedforward block via acceleration and speed signals. State filter also connected to state feedback via speed signal.

**State Filter**

The state filter is a low-pass filter that generates the acceleration command
based on the speed command. The discrete form of characteristic equation is
given by:

z+KsfTsm−1

The filter calculates the gain using this equation.

Ksf=1−exp(−Tsm2πEVsf)Tsm

The equations use these variables.

|  |  |
| --- | --- |
| *EVsf* | Bandwidth of the speed command filter |
| *Tsm* | Motion controller sample time |
| *Ksf* | Speed regulator time constant |

**State Feedback**

To generate the state feedback torque, the block uses the filtered speed error
signal from the state filter. To filter the speed, the block uses a proportional
integral (PI) controller.

Tcmd=Kpω(ωm\*−ωm)+KiωzTsmz−1(ωm\*−ωm)

The equations use these variables.

|  |  |
| --- | --- |
| *ωm* | Rotor speed |
| *ω\*m* | Rotor speed command |
| *Tcmd* | Torque command |
| *Kpω* | Speed regulator proportional gain |
| *Kiω* | Speed regulator integral gain |
| *Tsm* | Speed regulator sample rate |

**Command Feedforward**

To generate the state feedforward torque, the block uses the filtered speed
and acceleration from the state filter. Also, the feedforward torque calculation
uses the inertia, viscous damping, and static friction. To achieve zero tracking
error, the torque command is the sum of the feedforward and feedback torque
commands.

The feedforward torque command uses this equation.

Tcmd\_ff= Jpω˙m+Fvωm+Fs ωm|ωm|

where:

|  |  |
| --- | --- |
| *Jp* | Rotor inertia |
| *Tcmd\_ff* | Torque command feedforward |
| *Fs* | Static friction torque constant |
| *F*v** | Viscous friction torque constant |
| *Fs* | Static friction torque constant |
| *ωm* | Rotor speed |

**Current Command**

The block uses lookup tables to determine the *d*-axis and
*q*-axis current commands. The lookup tables are
functions of mechanical speed and torque. To determine the lookup tables, you
can use an external finite element analysis (FEA) models or dynamometer test
results.

idref=f(|ωm|,|Tref|)iqref=sign(Tref)∗f(|ωm|,|Tref|)

The equations use these variables.

|  |  |
| --- | --- |
| *ωm* | Rotor speed |
| *Tref* | Torque command |
| *idref*, *iqref* | *d*- and *q*-axis reference current, respectively |

**Voltage Command**

The block uses these equations to calculate the voltage in the motor reference
frame.

vd=dψddt+Rsid−ωeψqvq=dψqdt+Rsiq+ωeψd

dψddt+Rsid=Kpd(id\*−id)+KidzTstz−1(id\*−id)dψqdt+Rsiq=Kpq(iq\*−iq)+KiqzTstz−1(iq\*−iq)vd=Kpi(id\*−id)+KidzTstz−1(id\*−id)+ωeψqvq=Kpi(iq\*−iq)+KiqzTstz−1(iq\*−iq)−ωeψdψq=f(id,iq)ψd=f(id,iq)

The equations use these variables.

|  |  |
| --- | --- |
| *ωm* | Rotor mechanical speed |
| *ωe* | Rotor electrical speed |
| *Rs*, *Rr* | Resistance of the stator and rotor windings, respectively |
| *iq*, *id* | *q*- and *d*-axis current, respectively |
| *vq*, *vd* | *q*- and *d*-axis voltage, respectively |
| *Ψq*, *Ψd* | *q*- and *d*-axis magnet flux, respectively |
| *Tst* | Current regulator sample rate |
| *Kid*, *Kiq* | *d*- and *q*- axis integral gain, respectively |
| *Kpd*, *Kpq* | *d*- and *q*- axis proportional gain, respectively |

### Transforms

To calculate the voltages and currents in balanced three-phase
(*a*, *b*) quantities, quadrature two-phase
(*α*, *β*) quantities, and rotating
(*d*, *q*) reference frames, the block uses
the Clarke and Park Transforms.

In the transform equations.

ωe=Pωmdθedt= ωe

| Transform | Description | Equations |
| --- | --- | --- |
| Clarke | Converts balanced three-phase quantities (*a*, *b*) into balanced two-phase quadrature quantities (*α*, *β*). | xα= 23xa− 13xb −13xcxβ= 32xb− 32xc |
| Park | Converts balanced two-phase orthogonal stationary quantities (*α*, *β*) into an orthogonal rotating reference frame (*d*, *q*). | xd= xαcosθe+ xβsinθexq= −xαsinθe+ xβcosθe |
| Inverse Clarke | Converts balanced two-phase quadrature quantities (*α*, *β*) into balanced three-phase quantities (*a*, *b*). | xa= xaxb= −12xα+ 32xβxc= −12xα− 32xβ |
| Inverse Park | Converts an orthogonal rotating reference frame (*d*, *q*) into balanced two-phase orthogonal stationary quantities (*α*, *β*). | xα= xdcosθe− xqsinθexβ= xdsinθe+ xqcosθe |

The transforms use these variables.

|  |  |
| --- | --- |
| *ωm* | Rotor speed |
| *P* | Rotor pole pairs |
| *ωe* | Rotor electrical speed |
| *Θe* | Rotor electrical angle |
| *x* | Phase current or voltage |

### Motor

The block uses the phase currents and phase voltages to estimate the DC bus
current. Positive current indicates battery discharge. Negative current indicates
battery charge.

The block uses these equations.

|  |  |
| --- | --- |
| Load power | LdPwr=va ia+ vb ib+ vc ic |
| Source power | SrcPwr= LdPwr+PwrLoss |
| DC bus current | ibus= SrcPwrvbus |
| Estimated rotor torque | Te=1.5P[ψdiq−ψqid] |
| Power loss for single efficiency source to load | PwrLoss=100−EffEff⋅LdPwr |
| Power loss for single efficiency load to source | PwrLoss=100−Eff100⋅|LdPwr| |
| Power loss for tabulated efficiency | PwrLoss= f(ωm,MtrTrqest) |

The equations use these variables.

|  |  |
| --- | --- |
| *va*, *vb*, *vc* | Stator phase a, b, c voltages |
| *vbus* | Estimated DC bus voltage |
| *ia*, *ib*, *ic* | Stator phase a, b, c currents |
| *ibus* | Estimated DC bus current |
| *Eff* | Overall inverter efficiency |
| *ωm* | Rotor mechanical speed |
| *Lq*, *Ld* | *q*- and *d*-axis winding inductance, respectively |
| *Ψq*, *Ψd* | *q*- and *d*-axis magnet flux, respectively |
| *iq*, *id* | *q*- and *d*-axis current, respectively |
| *λ* | Permanent magnet flux linkage |
| *P* | Rotor pole pairs |

### Electrical Losses

To specify the electrical losses, on the **Electrical Losses** tab, for **Parameterize losses by**, select one of these options.

| Setting | Block Implementation |
| --- | --- |
| `Single efficiency measurement` | Electrical loss calculated using a constant value for inverter efficiency. |
| `Tabulated loss data` | Electrical loss calculated as a function of motor speeds and load torques. |
| `Tabulated efficiency data` | Electrical loss calculated using inverter efficiency that is a function of motor speeds and load torques.    - Converts the efficiency values you provide into losses and uses the tabulated losses for simulation. - Ignores efficiency values you provide for zero speed or zero torque. Losses are assumed zero when either torque or speed is zero. - Uses linear interpolation to determine losses. Provide tabulated data for low speeds and low torques, as required, to get the desired level of accuracy for lower power conditions. - Does not extrapolate loss values for speed and torque magnitudes that exceed the range of the table. |

For best practice, use `Tabulated loss data` instead of `Tabulated efficiency data`:

- Efficiency becomes ill defined for zero speed or zero torque.
- You can account for fixed losses that are still present for zero speed or torque.
