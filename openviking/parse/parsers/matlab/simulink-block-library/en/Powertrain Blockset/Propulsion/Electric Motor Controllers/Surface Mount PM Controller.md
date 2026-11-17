---
type: simulink-block
title: 'Surface Mount PM Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motor Controllers'
documentation_page: 'surfacemountpmcontroller'
documentation_source_path: 'ref/surfacemountpmcontroller.html'
language: en
---

# Surface Mount PM Controller

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

DC bus voltage *vbus*, in
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
  summary: Select control Speed Control (default) | Torque Control
  group: ''
  block_parameter: control_type
  values: Speed Control (default) | Torque Control
- name: Stator resistance, Rs
  summary: Resistance 0.02 (default) | scalar
  group: ''
  block_parameter: Rs
  values: 0.02 (default) | scalar
- name: DQ axis inductance, Ldq
  summary: Inductance 1.7e-3 (default) | scalar
  group: ''
  block_parameter: Ldq
  values: 1.7e-3 (default) | scalar
- name: Permanent magnet flux, lambda_pm
  summary: Flux 0.2205 (default) | scalar
  group: ''
  block_parameter: lambda_pm
  values: 0.2205 (default) | scalar
- name: Number of pole pairs, PolePairs
  summary: Poles 4 (default) | scalar
  group: ''
  block_parameter: PolePairs
  values: 4 (default) | scalar
- name: Physical inertia, viscous damping, static friction, Mechanical
  summary: Inertia, damping, friction [0.0027, 4.924e-4, 0] (default) | vector
  group: ''
  block_parameter: Mechanical
  values: '[0.0027, 4.924e-4, 0] (default) | vector'
- name: Maximum torque, T_max
  summary: Torque 60 (default) | scalar
  group: ''
  block_parameter: T_max
  values: 60 (default) | scalar
- name: Bandwidth of the current regulator, EV_current
  summary: Bandwidth 200 (default) | scalar
  group: ''
  block_parameter: EV_current
  values: 200 (default) | scalar
- name: Sample time for the torque control, Tst
  summary: Time 5e-5 (default) | scalar
  group: ''
  block_parameter: Tst
  values: 5e-5 (default) | scalar
- name: Calculate Current Regulator Gains
  summary: Derive parameters button
  group: ''
- name: D-axis proportional gain, Kp_d
  summary: Derived 0.47149 (default) | scalar
  group: ''
  block_parameter: Kp_d
  values: 0.47149 (default) | scalar
- name: Q-axis proportional gain, Kp_q
  summary: Derived 0.52125 (default) | scalar
  group: ''
  block_parameter: Kp_q
  values: 0.52125 (default) | scalar
- name: D and Q axis integral gain, Ki
  summary: Derived 251.3274 (default) | scalar
  group: ''
  block_parameter: Ki
  values: 251.3274 (default) | scalar
- name: Bandwidth of the motion controller, EV_motion
  summary: Bandwidth [20, 4, 0.8] (default) | vector
  group: ''
  block_parameter: EV_motion
  values: '[20, 4, 0.8] (default) | vector'
- name: Bandwidth of the state filter, EV_sf
  summary: Bandwidth 200 (default) | scalar
  group: ''
  block_parameter: EV_sf
  values: 200 (default) | scalar
- name: Calculate Speed Regulator Gains
  summary: Derive parameters button
  group: ''
- name: Proportional gain, ba
  summary: Derived 3.7477 (default) | scalar
  group: ''
  block_parameter: ba
  values: 3.7477 (default) | scalar
- name: Angular gain, Ksa
  summary: Derived 94.0877 (default) | scalar
  group: ''
  block_parameter: Ksa
  values: 94.0877 (default) | scalar
- name: Rotational gain, Kisa
  summary: Derived 381.7822 (default) | scalar
  group: ''
  block_parameter: Kisa
  values: 381.7822 (default) | scalar
- name: Speed regulation time constant, Ksf
  summary: Derived 1217.9727 (default) | scalar
  group: ''
  block_parameter: Ksf
  values: 1217.9727 (default) | scalar
- name: Inertia compensation, Jcomp
  summary: Derived 0.025 (default) | scalar
  group: ''
  block_parameter: Jcomp
  values: 0.025 (default) | scalar
- name: Viscous damping compensation, Fv
  summary: Derived 0 (default) | scalar
  group: ''
  block_parameter: Fv
  values: 0 (default) | scalar
- name: Static friction, Fs
  summary: Derived 0 (default) | scalar
  group: ''
  block_parameter: Fs
  values: 0 (default) | scalar
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

#### Configuration

### **Control Type** — Select control `Speed Control` (default) | `Torque Control`

If you select `Torque Control`, the block does
not implement the speed controller.

This table summarizes the port configurations.

| Port Configuration | Creates Ports |
| --- | --- |
| `Speed Control` | `SpdReq` |
| `Torque Control` | `TrqCmd` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `control_type` |
| **Values:** | `Speed Control` (default) | `Torque Control` |
| **Data Types:** | `character vector` |

#### Motor Parameters

### **Stator resistance, Rs** — Resistance `0.02` (default) | `scalar`

Stator phase winding resistance,
*Rs*, in ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rs` |
| **Values:** | `0.02` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Stator resistance, Rs** | **D and Q axis integral gain, Ki** | **Current Controller** |

### **DQ axis inductance, Ldq** — Inductance `1.7e-3` (default) | `scalar`

D-axis winding inductance, *Ldq*,
in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ldq` |
| **Values:** | `1.7e-3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **DQ axis inductance, Ldq** | **D-axis proportional gain, Kp\_d**  **Q-axis proportional gain, Kp\_q**  **D and Q axis integral gain, Ki** | **Current Controller** |

### **Permanent magnet flux, lambda\_pm** — Flux `0.2205` (default) | `scalar`

Permanent magnet flux, *λpm*, in
Wb.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lambda_pm` |
| **Values:** | `0.2205` (default) | `scalar` |
| **Data Types:** | `double` |

### **Number of pole pairs, PolePairs** — Poles `4` (default) | `scalar`

Motor pole pairs, *P*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PolePairs` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Physical inertia, viscous damping, static friction, Mechanical** — Inertia, damping, friction `[0.0027, 4.924e-4, 0]` (default) | `vector`

Mechanical properties of the motor:

- Motor inertia, *F*v**, in kgm^2
- Viscous friction torque constant,
  *F*v**, in
  N·m/(rad/s)
- Static friction torque constant,
  *Fs*, in
  N·m

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Mechanical` |
| **Values:** | `[0.0027, 4.924e-4, 0]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set the **Control Type**
parameter to `Speed Control`.

For the gain calculations, the block uses the inertia from the
**Physical inertia, viscous damping, static
friction** parameter value that is on the **Motor
Parameters** tab.

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Physical inertia, viscous damping, static friction, Mechanical** | **Proportional gain, ba**  **Angular gain, Ksa**  **Rotational gain, Kisa**  **Inertia compensation, Jcomp**  **Viscous damping compensation, Fv**  **Static friction, Fs** | **Speed Controller** |

#### Id and Iq Calculation

### **Maximum torque, T\_max** — Torque `60` (default) | `scalar`

Maximum torque, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `T_max` |
| **Values:** | `60` (default) | `scalar` |
| **Data Types:** | `double` |

#### Current Controller

### **Bandwidth of the current regulator, EV\_current** — Bandwidth `200` (default) | `scalar`

Current regulator bandwidth, in Hz.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EV_current` |
| **Values:** | `200` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Bandwidth of the current regulator, EV\_current** | **D-axis proportional gain, Kp\_d**  **Q-axis proportional gain, Kp\_q**  **D and q axis proportional gain, Ki** | **Current Controller** |

### **Sample time for the torque control, Tst** — Time `5e-5` (default) | `scalar`

Torque control sample time, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tst` |
| **Values:** | `5e-5` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Sample time for the torque control, Tst** | **Speed regulation time constant, Ksf** | **Speed Controller** |

### **Calculate Current Regulator Gains** — Derive parameters button

Click to derive parameters.

#### Dependencies

On the **Current Controller** tab, when you
select **Calculate Current Regulator Gains**, the
block calculates derived parameters. The table summarizes the derived
parameters that depend on other block parameters.

| Derived Parameter on **Current Controller** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D-axis proportional gain, Kp\_d**  **Q-axis proportional gain, Kp\_q**  **D and Q axis integral gain, Ki** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **Stator resistance, Rs**  **DQ-axis inductance, Ldq** | **Motor Parameters** |

### **D-axis proportional gain, Kp\_d** — Derived `0.47149` (default) | `scalar`

Derived d-axis proportional gain, in V/A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp_d` |
| **Values:** | `0.47149` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D-axis proportional gain, Kp\_d** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **DQ-axis inductance, Ldq** | **Motor Parameters** |

### **Q-axis proportional gain, Kp\_q** — Derived `0.52125` (default) | `scalar`

Derived q-axis proportional gain, in V/A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp_q` |
| **Values:** | `0.52125` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Q-axis proportional gain, Kp\_q** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **DQ-axis inductance, Ldq** | **Motor Parameters** |

### **D and Q axis integral gain, Ki** — Derived `251.3274` (default) | `scalar`

Derived axis integral gain, in V/A\*s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ki` |
| **Values:** | `251.3274` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D and Q axis integral gain, Ki** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **Stator resistance, Rs**  **DQ-axis inductance, Ldq** | **Motor Parameters** |

#### Speed Controller

### **Bandwidth of the motion controller, EV\_motion** — Bandwidth `[20, 4, 0.8]` (default) | `vector`

Motion controller bandwidth, in Hz. Set the first element of the vector to the
desired cutoff frequency. Set the second and third elements of the vector to the
higher-order cut off frequencies. You can set the value of the next element to
`1/5` the value of the previous element. For example, if the
desired cutoff frequency is `20` Hz, specify `[20 4
0.8]`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EV_motion` |
| **Values:** | `[20, 4, 0.8]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

The parameter is enabled when the **Control Type** parameter
is set to `Speed Control`.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Bandwidth of the motion controller, EV\_motion** | **Proportional gain, ba**  **Angular gain, Ksa**  **Rotational gain, Kisa** | **Speed Controller** |

### **Bandwidth of the state filter, EV\_sf** — Bandwidth `200` (default) | `scalar`

State filter bandwidth, in Hz.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EV_sf` |
| **Values:** | `200` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

The parameter is enabled when the **Control Type** parameter
is set to `Speed Control`.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Bandwidth of the state filter, EV\_sf** | **Speed regulation time constant, Ksf** | **Speed Controller** |

### **Calculate Speed Regulator Gains** — Derive parameters button

Click to derive parameters.

#### Dependencies

On the **Speed Controller** tab, when you select **Calculate
Speed Regulator Gains**, the block calculates derived parameters.
The table summarizes the derived parameters that depend on other block
parameters.

| Derived Parameter on **Speed Controller** tab | | Depends On | |
| --- | --- | --- | --- |
| Parameter | Tab |
| **Proportional gain, ba** | ba=Jp−Jpp1p2p3Tsm | **Bandwidth of the motion controller, EV\_motion**  **Bandwidth of the state filter, EV\_sf** | **Speed Controller** |
| **Angular gain, Ksa** | Ksa=Jp(p1p2+p2p3+p3p1)−3Jp+2baTsmTsm2 | **Sample time for the torque control, Tst** | **Current Controller** |
| **Rotational gain, Kisa** | Kisa=−Jp(p1+p2+p3)+3Jp−baTsm−KsaTsm2Tsm3 | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Speed regulation time constant, Ksf** | Ksf=1−exp(−Tsm2πEVsf)Tsm |
| **Inertia compensation, Jcomp** | *Jcomp* = *Jp* | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Viscous damping compensation, Fv** | *F*v** |
| **Static friction, Fs** | *Fs* |

The equations use these variables.

|  |  |
| --- | --- |
| *P* | Motor pole pairs |
| *ba* | Speed regulator proportional gain |
| *Ksa* | Speed regulator integral gain |
| *Kisa* | Speed regulator double integral gain |
| *Ksf* | Speed regulator time constant |
| *Jp* | Motor inertia |
| *EVsf* | State filter bandwidth |
| *EVmotion* | Motion controller bandwidth |

### **Proportional gain, ba** — Derived `3.7477` (default) | `scalar`

Derived proportional gain, in N·m/(rad/s).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ba` |
| **Values:** | `3.7477` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Proportional gain, ba** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Angular gain, Ksa** — Derived `94.0877` (default) | `scalar`

Derived angular gain, in N·m/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ksa` |
| **Values:** | `94.0877` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Angular gain, Ksa** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Rotational gain, Kisa** — Derived `381.7822` (default) | `scalar`

Derived rotational gain, in N·m/(rad\*s).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kisa` |
| **Values:** | `381.7822` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Rotational gain, Kisa** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Speed regulation time constant, Ksf** — Derived `1217.9727` (default) | `scalar`

Derived speed regulation time constant, in 1/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ksf` |
| **Values:** | `1217.9727` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Speed regulation time constant, Ksf** | **Sample time for the torque control, Tst** | **Current Controller** |
| **Bandwidth of the state filter, EV\_sf** | **Speed Controller** |

### **Inertia compensation, Jcomp** — Derived `0.025` (default) | `scalar`

Derived inertia compensation, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jcomp` |
| **Values:** | `0.025` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Inertia compensation, Jcomp** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |

### **Viscous damping compensation, Fv** — Derived `0` (default) | `scalar`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fv` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Viscous damping compensation, Fv** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |

### **Static friction, Fs** — Derived `0` (default) | `scalar`

Derived static friction, in N·m/(rad/s).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fs` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **Static friction, Fs** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |

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

Powertrain Blockset / Propulsion / Electric Motors and Inverters Motor Control Blockset / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Torque-based, field-oriented controller for a surface mount permanent magnet synchronous motor

The Surface Mount PM Controller block implements a torque-based,
field-oriented controller for a surface mount permanent magnet synchronous motor (PMSM)
with an optional outer-loop speed controller. The torque control utilizes quadrature
current and does not weaken the magnetic flux. You can specify either speed or torque
control.

The Surface Mount PM Controller implements equations for speed control,
torque determination, regulators, transforms, and motors.

The figure illustrates the information flow in the block.

The block implements equations that use these variables.

|  |  |
| --- | --- |
| *ω* | Rotor speed |
| *ω\** | Rotor speed command |
| *T\** | Torque command |
| *id*  *i\*d* | d-axis current  d-axis current command |
| *iq*  *i\*q* | q-axis current  q-axis current command |
| *vd*,  *v\*d* | d-axis voltage  d-axis voltage command |
| *vq*  *v\*q* | q-axis voltage  q-axis voltage command |
| *va*, *vb*, *vc* | Stator phase a, b, c voltages |
| *ia*, *ib*, *ic* | Stator phase a, b, c currents |

### Speed Controller

To implement the speed controller, select the **Control Type**
parameter `Speed Control`. If you select the
**Control Type** parameter `Torque
Control`, the block does not implement the speed controller.

The speed controller determines the torque command by implementing a state filter,
and calculating the feedforward and feedback commands. If you do not implement the
speed controller, input a torque command to the Surface Mount PM
Controller block.

**State Filter**

The state filter is a low-pass filter that generates the acceleration command
based on the speed command. On the **Speed Controller** tab:

- To make the speed-command lag time negligible, specify a
  **Bandwidth of the state filter**
  parameter.
- To calculate a **Speed regulation time constant,
  Ksf** gain based on the state filter bandwidth, select
  **Calculate Speed Regulator Gains**.

The discrete form of characteristic equation is given by:

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
signal from the state filter. The feedback torque calculation also requires
gains for speed regulator.

On the **Speed Controller** tab, select **Calculate
Speed Regulator Gains** to calculate:

- **Proportional gain, ba**
- **Angular gain, Ksa**
- **Rotational gain, Kisa**

For the gain calculations, the block uses the inertia from the
**Physical inertia, viscous damping, static friction**
parameter value on the **Motor Parameters** tab.

The gains for the state feedback are calculated using these equations.

| Calculation | Equations |
| --- | --- |
| Discrete forms of characteristic equation | z3+(−3Jp+Tsba+ Ts2Ksa+Ts3Kisa)Jpz2+(3Jp− 2Tsba− Ts2Ksa)Jpz+−Jp+TsbaJp  (z−p1)(z−p2)(z−p3)=z3+(p1+p2+p3)z2+(p1p2+p2p3+p13)z2−p1p2p3 |
| Speed regulator proportional gain | ba=Jp−Jpp1p2p3Tsm |
| Speed regulator integral gain | Ksa=Jp(p1p2+p2p3+p3p1)−3Jp+2baTsmTsm2 |
| Speed regulator double integral gain | Kisa=−Jp(p1+p2+p3)+3Jp−baTsm−KsaTsm2Tsm3 |

The equations use these variables.

|  |  |
| --- | --- |
| *P* | Motor pole pairs |
| *ba* | Speed regulator proportional gain |
| *Ksa* | Speed regulator integral gain |
| *Kisa* | Speed regulator double integral gain |
| *Jp* | Motor inertia |
| *Tsm* | Motion controller sample time |

**Command Feedforward**

To generate the state feedforward torque, the block uses the filtered speed
and acceleration from the state filter. Also, the feedforward torque calculation
uses the inertia, viscous damping, and static friction. To achieve zero tracking
error, the torque command is the sum of the feedforward and feedback torque
commands.

Selecting **Calculate Speed Regulator Gains** on the
**Speed Controller** tab updates the inertia, viscous
damping, and static friction with the **Physical inertia, viscous
damping, static friction** parameter values on the **Motor
Parameters** tab.

The feedforward torque command uses this equation.

Tcmd\_ff= Jpω˙m+Fvωm+Fs ωm|ωm|

The equation uses these variables.

|  |  |
| --- | --- |
| *Jp* | Motor inertia |
| *Tcmd\_ff* | Torque command feedforward |
| *Fs* | Static friction torque constant |
| *F*v** | Viscous friction torque constant |
| *Fs* | Static friction torque constant |
| *ωm* | Rotor speed |

### Torque Determination

The block uses a quadrature current to determine the base speed and the current
commands. The available bus voltage determines the base speed. The direct (d) and
quadrature (q) permanent magnet (PM) determines the induced voltage.

| Calculation | Equations |
| --- | --- |
| Motor maximum torque | Tmax= 32P(λpmiq+(Ld− Lq)idiq) |
| Maximum q-axis phase current | iq\_max=Tcmd32Pλpm |
| Electrical base speed | ωbase=  vmax(Lqiq)2+( λpm)2 |
| d-axis voltage | vd=−ωeLqiq\_max |
| q-axis voltage | vq=ωeλpm |
| Maximum phase current | imax= |iq\_max| |
| Maximum voltage | vmax= vbus 3 |
| Current command | ``` idref= 0iq_tmp=min(iq_max,Tcmd32Pλpm) If|ωe|≤ ωbase 		iqref= iq_tmp Else 		iqfw= sqrt(min(0,1Lq((vmaxωe)2− ( λpm)2)) 		If  iq_tmp<iqfw 			iqref= iq_tmp 		Else 			iqref= iqfw 		End End ``` |

The equations use these variables.

|  |  |
| --- | --- |
| *imax* | Maximum phase current |
| *id* | d-axis current |
| *iq* | q-axis current |
| *idref* | d-axis reference current |
| *iqref* | q-axis reference current |
| *iq\_max* | Maximum q-axis phase current |
| *ωe* | Rotor electrical speed |
| *λpm* | Permanent magnet flux linkage |
| *vd* | d-axis voltage |
| *vq* | q-axis voltage |
| *vmax* | Maximum line to neutral voltage |
| *vbus* | DC bus voltage |
| *Ld* | d-axis winding inductance |
| *Lq* | q-axis winding inductance |
| *P* | Motor pole pairs |
| *Tmax* | Motor maximum torque |
| *Tcmd* | Commanded motor maximum torque |

### Current Regulators

The block regulates the current with an anti-windup feature. Classic
proportional-integrator (PI) current regulators do not consider the d-axis and
q-axis coupling or the back-electromagnetic force (EMF) coupling. As a result,
transient performance deteriorates. To account for the coupling, the block
implements the complex vector current regulator (CVCR) in the scalar format of the
rotor reference frame. The CVCR decouples:

- d-axis and q-axis current cross-coupling
- back-EMF cross-coupling

The current frequency response is a first-order system, with a
bandwidth of *EVcurrent*.

The block implements these equations.

| Calculation | Equations |
| --- | --- |
| Motor voltage, in the rotor reference frame | Lddiddt= vd−Rsid+pωmLqiqLqdiqdt= vq−Rsiq−pωmLdid−pωmλpm |
| Current regulator gains | ωb=2πEVcurrentKp\_d=LdωbKp\_q=LqωbKi=Rsωb |
| Transfer functions | ididref= ωbs+ωbiqiqref= ωbs+ωb |

The equations use these variables.

|  |  |
| --- | --- |
| *EVcurrent* | Current regulator bandwidth |
| *id* | d-axis current |
| *iq* | q-axis current |
| *Kp\_d* | Current regulator d-axis gain |
| *Kp\_q* | Current regulator q-axis gain |
| *Ki* | Current regulator integrator gain |
| *Ld* | d-axis winding inductance |
| *Lq* | q-axis winding inductance |
| *Rs* | Stator phase winding resistance |
| *ωm* | Rotor speed |
| *vd* | d-axis voltage |
| *vq* | q-axis voltage |
| *λpm* | Permanent magnet flux linkage |
| *P* | Motor pole pairs |

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
| *P* | Motor pole pairs |
| *ωe* | Rotor electrical speed |
| *Θe* | Rotor electrical angle |
| *x* | Phase current or voltage |

### Motor

The block uses the phase currents and phase voltages to estimate the DC bus
current. Positive current indicates battery discharge. Negative current indicates
battery charge. The block uses these equations.

|  |  |
| --- | --- |
| Load power | LdPwr=va ia+ vb ib+ vc ic |
| Source power | SrcPwr= LdPwr+PwrLoss |
| DC bus current | ibus= SrcPwrvbus |
| Estimated rotor torque | MtrTrqest=1.5P[λiq+(Ld−Lq)idiq] |
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
| *Lq* | q-axis winding inductance |
| *Ld* | d-axis winding inductance |
| *iq* | q-axis current |
| *id* | d-axis current |
| *λ* | Permanent magnet flux linkage |
| *P* | Motor pole pairs |

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
