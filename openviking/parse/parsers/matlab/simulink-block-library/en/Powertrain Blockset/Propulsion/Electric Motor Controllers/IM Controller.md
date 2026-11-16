---
type: simulink-block
title: 'IM Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motor Controllers'
documentation_page: 'imcontroller'
documentation_source_path: 'ref/imcontroller.html'
language: en
---

# IM Controller

## Ports

### Input

### **SpdReq** — Rotor mechanical speed command `scalar`

Rotor mechanical speed command,
*ω\*m*, in rad/s.

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

### **SpdFdbk** — Rotor mechanical speed `scalar`

Rotor mechanical speed, *ωm*,
in rad/s.
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

#### Block Options

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

#### Motor

### **Stator resistance, Rs** — Resistance `1.77` (default) | `scalar`

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
| **Values:** | `1.77` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Stator resistance, Rs** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |
| **D and Q axis integral gain, Ki** | **Current Controller** |

### **Stator leakage inductance, Lls** — Inductance `0.0139` (default) | `scalar`

Stator leakage inductance, *Lls*,
in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lls` |
| **Values:** | `0.0139` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Stator leakage inductance, Lls** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |
| **D and Q axis proportional gain, Kp**  **D and Q axis integral gain, Ki** | **Current Controller** |

### **Rotor resistance, Rr** — Resistance `1.34` (default) | `scalar`

Rotor resistance, *Rr*, in
ohm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rr` |
| **Values:** | `1.34` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rotor resistance, Rr** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Rotor leakage inductance, Llr** — Inductance `0.0121` (default) | `scalar`

Rotor leakage inductance, *Llr*,
in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Llr` |
| **Values:** | `0.0121` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rotor leakage inductance, Llr** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |
| **D and Q axis proportional gain, Kp** | **Current Controller** |

### **Rotor magnetizing inductance, Lm** — Inductance `0.3687` (default) | `scalar`

Rotor magnetizing inductance,
*Lm*, in H.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lm` |
| **Values:** | `0.3687` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rotor leakage inductance, Llr** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |
| **D and Q axis proportional gain, Kp** | **Current Controller** |

### **Number of pole pairs, PolePairs** — Poles `2` (default) | `scalar`

Motor pole pairs, *P*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PolePairs` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rotor leakage inductance, Llr** | **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Physical inertia, viscous damping, static friction, Mechanical** — Mechanical properties of motor `[0.025, 0, 0]` (default) | `vector`

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
| **Values:** | `[0.025, 0, 0]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set the **Control Type**
parameter to `Speed Control`.

For the gain calculations, the block uses the inertia from the
**Physical inertia, viscous damping, static
friction** parameter value that is on the **Motor
Parameters** tab.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Physical inertia, viscous damping, static friction, Mechanical** | **Proportional gain, ba**  **Angular gain, Ksa**  **Rotational gain, Kisa**  **Inertia compensation, Jcomp**  **Viscous damping compensation, Fv**  **Static friction, Fs** | **Speed Controller** |

#### Id and Iq Calculation

### **Rated synchronous speed, Frate** — Motor frequency `60` (default) | `scalar`

Motor-rated electrical frequency,
*Frate*, in Hz.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Frate` |
| **Values:** | `60` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rated synchronous speed, Frate** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Rated line to line voltage RMS, Vrate** — Motor voltage `460` (default) | `scalar`

Motor-rated line-to-line voltage,
*Vrate*, in V.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Vrate` |
| **Values:** | `460` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rated synchronous speed, Frate** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Rated slip, Srate** — Motor slip speed `0.0172` (default) | `scalar`

Motor-rated slip speed, *Srate*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Srate` |
| **Values:** | `0.0172` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

This table summarizes the parameter dependencies.

| Parameter | Used to Derive | |
| --- | --- | --- |
| Parameter | Tab |
| **Rated slip, Srate** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Calculate Rated Stator Flux Current** — Derive parameters button

Click to derive parameters.

#### Dependencies

On the **Id and Iq Calculation** tab, when
you select **Calculate Rated Stator Flux Current**,
the block calculates derived parameters. The table summarizes the
derived parameters that depend on other block parameters.

| Derived Parameter on **Id and Iq Calculation** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **D-axis rated current, Isd\_0** — Derived `3.1004` (default) | `scalar`

Derived d-axis rated current, in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Isd_0` |
| **Values:** | `3.1004` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

On the **Id and Iq Calculation** tab, when
you select **Calculate Rated Stator Flux Current**,
the block calculates derived parameters. The table summarizes the
derived parameters that depend on other block parameters.

| Derived Parameter on **Id and Iq Calculation** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **Q-axis rated current, Isq\_0** — Derived `5.7131` (default) | `scalar`

Derived q-axis rated current, in A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Isq_0` |
| **Values:** | `5.7131` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

On the **Id and Iq Calculation** tab, when
you select **Calculate Rated Stator Flux Current**,
the block calculates derived parameters. The table summarizes the
derived parameters that depend on other block parameters.

| Derived Parameter on **Id and Iq Calculation** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **Torque at rated current, Tem** — Derived `12.6467` (default) | `scalar`

Torque at rated current, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tem` |
| **Values:** | `12.6467` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

On the **Id and Iq Calculation** tab, when
you select **Calculate Rated Stator Flux Current**,
the block calculates derived parameters. The table summarizes the
derived parameters that depend on other block parameters.

| Derived Parameter on **Id and Iq Calculation** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

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
| **Bandwidth of the current regulator, EV\_current** | **D and Q axis integral gain, Ki**  **D and Q axis proportional gain, Kp** | **Current Controller** |

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
| **D and Q axis proportional gain, Kp**  **D and Q axis integral gain, Ki** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **D and Q axis proportional gain, Kp** — Derived `32.1894` (default) | `scalar`

Derived proportional gain, in V/A.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kp` |
| **Values:** | `32.1894` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

On the **Current Controller** tab, when you
select **Calculate Current Regulator Gains**, the
block calculates derived parameters. The table summarizes the derived
parameters that depend on other block parameters.

| Derived Parameter on **Current Controller** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D and Q axis proportional gain, Kp**  **D and Q axis integral gain, Ki** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **D and Q axis integral gain, Ki** — Derived `2224.2476` (default) | `scalar`

Derived integral gain, in V/A\*s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ki` |
| **Values:** | `2224.2476` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

On the **Current Controller** tab, when you
select **Calculate Current Regulator Gains**, the
block calculates derived parameters. The table summarizes the derived
parameters that depend on other block parameters.

| Derived Parameter on **Current Controller** tab | Dependency | |
| --- | --- | --- |
| Parameter | Tab |
| **D and Q axis proportional gain, Kp**  **D and Q axis integral gain, Ki** | **Bandwidth of the current regulator, EV\_current** | **Current Controller** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

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

Powertrain Blockset / Propulsion / Electric Motor Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Internal torque-based, field-oriented controller for an induction motor with an optional outer-loop speed controller

The IM Controller block implements an internal torque-based,
field-oriented controller for an induction motor (IM) with an optional outer-loop speed
controller. The torque control implements a strategy to control the motor flux. You can
specify either speed or torque control.

The IM Controller implements equations for speed control, torque
determination, regulators, transforms, and motors.

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
speed controller, input a torque command to the IM Controller block.

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

The equation uses these variables.

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
Speed Regulator Gains** to compute:

- **Proportional gain, ba**
- **Angular gain, Ksa**
- **Rotational gain, Kisa**

For the gain calculations, the block uses the inertia from the
**Physical inertia, viscous damping, static friction**
parameter value on the **Motor Parameter** tab.

The gains for the state feedback are calculated using these
equations.

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
Parameter** tab.

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
| *ωm* | Rotor mechanical speed |

### Torque Determination

The block uses a quadrature current to determine the base speed and the current
commands. The motor ratings determine the rated electrical speed.

| Calculation | Equations |
| --- | --- |
| Current commands | iqref=Tcmdisq\_0⋅P⋅(L2mLr)  ``` If |ωe|≤ωrated 		idref= isd_0	 Else 		idref= isd_0⋅ωrated|ωe| End ``` |
| Inductance | Lr=Llr+LmLs=Lls+Lm |

The equations use these variables.

|  |  |
| --- | --- |
| *idref* | d-axis reference current |
| *iqref* | q-axis reference current |
| *isd\_0* | d-axis rated current |
| *isq\_0* | q-axis rated current |
| *ωe* | Rotor electrical speed |
| *ωrated* | Rated electrical speed |
| *Llr* | Rotor leaking inductance |
| *Lr* | Rotor winding inductance |
| *Lls* | Stator leaking inductance |
| *Ls* | Stator winding inductance |
| *Lm* | Motor magnetizing inductance |
| *P* | Motor pole pairs |
| *Tcmd* | Commanded motor maximum torque |

### Current Regulators

The block regulates the current with an anti-windup feature. Classic
proportional-integrator (PI) current regulators do not consider the d-axis and
q-axis coupling or the back-electromagnetic force (EMF) coupling. As a result,
transient performance deteriorates. To account for the coupling, the block
implements the complex vector current regulator (CVCR) in the scalar format of the
rotor reference frame. The CVCR decouples:

- d-axis and q-axis current cross-coupling
- Back-EMF cross-coupling

The current frequency response is a first-order system, with a
bandwidth of *EVcurrent*.

The block implements these equations.

| Calculation | Equations |
| --- | --- |
| Motor voltage, in the stator reference frame | σ=1−L2mLsLrvsd=Rsisd+σLsdisddt+LmLrdλrddt−PωmσLsisqvsq=Rsisq+σLsdisqdt+ωdLmLrdλrddt+PωmσLsisd |
| Current regulator gains | ωb=2πEVcurrentKp=σLdωbKi=Rsωb |
| Transfer functions | ididref= ωbs+ωbiqiqref= ωbs+ωb |

The equations use these variables.

|  |  |
| --- | --- |
| *EVcurrent* | Current regulator bandwidth |
| *id* | d-axis current |
| *iq* | q-axis current |
| *isq* | Stator q-axis current |
| *isd* | Stator d-axis current |
| *vsd* | Stator d-axis voltage |
| *vsq* | Stator q-axis voltage |
| *Kp* | Current regulator d-axis gain |
| *Ki* | Current regulator integrator gain |
| *Ls* | Stator winding inductance |
| *Lm* | Motor magnetizing inductance |
| *Lr* | Rotor winding inductance |
| *Rs* | Stator phase winding resistance |
| *λrd* | Rotor d-axis magnetic flux |
| *σ* | Leakage factor |
| *p* | Motor pole pairs |

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
| *ωm* | Rotor mechanical speed |
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
| Estimated rotor torque | MtrTrqest=PλrdisqLmLr |
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
| *Lr* | Rotor winding inductance |
| *Lm* | Motor magnetizing inductance |
| *λrd* | Rotor d-axis magnetic flux |
| *isq* | q-axis current |
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
