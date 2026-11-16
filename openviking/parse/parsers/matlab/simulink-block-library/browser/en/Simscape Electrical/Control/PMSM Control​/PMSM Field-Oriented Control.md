---
type: simulink-block
title: 'PMSM Field-Oriented Control'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control\u200b'
documentation_page: 'pmsmfieldorientedcontrol'
documentation_source_path: 'ref/pmsmfieldorientedcontrol.html'
language: en
---

# PMSM Field-Oriented Control

## Ports

### Input

### **Reference** — System reference scalar

System reference specified as torque reference in N\*m or velocity
reference in rad/s, depending on the control mode selected.

**Data Types:** `single` | `double`

### **iabcSens** — Measured phase currents vector

Measured stator phase currents, in A.

**Data Types:** `single` | `double`

### **wSens** — Rotor speed scalar

Measured mechanical angular velocity of rotor, in rad/s.

**Data Types:** `single` | `double`

### **thSens** — Rotor angle scalar

Measured mechanical angle of rotor, in rad.

**Data Types:** `single` | `double`

### **vdcSens** — DC-link voltage scalar

Measured DC-link voltage, in V.

**Data Types:** `single` | `double`
### Output

### **G** — Gate pulses vector

Six pulse waveforms that determine switching behavior in the attached
power converter.

**Data Types:** `single` | `double`

### **Visualization** — Visualization signals bus

Bus containing signals for visualization, including:

- `Reference`
- `wElectrical`
- `iabc`
- `theta`
- `Vdc`
- `PwmEnable`
- `TqRef`
- `TqLim`
- `idqRef`
- `idq`
- `vdqRef`
- `modWave`

**Data Types:** `single` | `double`

## Parameters

#### General

### **Winding Type** — Control parameterization `Wye-wound` (default) | `Delta-wound`

Specify either a wye-wound or a delta-wound parameterization for the
reference values of the controller.

### **Control Mode** — Control mode strategy `Torque control` (default) | `Velocity control`

Specify either a torque control or velocity control strategy.

### **Nominal dc-link voltage (V)** — Rated DC voltage `300` (default) | positive number

Nominal DC-link voltage of the electrical source, in
`V`.

### **Maximum power (W)** — Maximum power `35000` (default) | positive number

Maximum machine power, in `W`.

### **Maximum torque (N\*m)** — Maximum torque `250` (default) | positive number

Maximum machine torque, in `N*m`.

### **Number of rotor pole pairs** — Pole pairs `8` (default) | positive integer

Number of permanent magnet pole pairs on the rotor.

### **Inverter dc-link voltage threshold (V)** — DC-link voltage threshold `100` (default) | positive number

Voltage threshold to activate the power inverter, in
`V`.

### **Fundamental sample time (s)** — Block sample time `5e-6` (default) | positive number

Fundamental sample time for the block, in
`s`.

### **Control sample time (s)** — Control sample time `1e-4` (default) | positive number

Sample time for the control system, in
`s`.

#### Outer Loop

### **Control Type** — Control type strategy `PI control` (default) | `P control` | `P-PI control`

Specify the type of the control strategy.

### **Controller proportional gain** — Proportional gain of PI controller `1` (default) | positive number

Proportional gain of the PI controller.

### **Controller integral gain** — Integral gain of PI controller `1` (default) | positive number

Integral gain of the PI controller.

### **P controller proportional gain** — Proportional gain of P controller `1` (default) | positive number

Proportional gain of P controller.

### **Integral anti-windup gain** — Anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller.

### **Current references** — Current reference strategy `Zero d-axis control` (default) | `Lookup-table based` | `Automatically generated lookup-table`

Select the current reference strategy.

### **Mechanical speed vector, wMechanical (rpm)** — Rotor speed lookup vector `[0, 3000]` (default) | positive monotonically increasing vector

Speed vector, in `rpm`, used in the lookup tables
for determining current references.

### **Torque reference vector, TqRef (N\*m)** — Torque reference lookup vector `[-100, 0, 100]` (default) | positive monotonically increasing vector

Torque vector, in `N*m`, used in the lookup
tables for determining current references.

### **DC-link voltage vector, Vdc (V)** — DC-link voltage lookup vector `[300, 350]` (default) | positive monotonically increasing vector

DC-link voltage vector, in `V`, used in the
lookup tables for determining current references.

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)** — Reference d-axis current values `zeros(2,3,2)` (default) | real matrix

Direct-axis current reference lookup data, in
`A`.

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)** — Reference q-axis current values `zeros(2,3,2)` (default) | real matrix

Quadrature-axis current reference lookup data, in
`A`.

### **Modulation factor** — Modulation factor `1` (default) | positive scalar

Safety factor used to compute the maximum allowed phase voltage for
current references generation.

#### Dependencies

This parameter is only visible when **Current
references** is set to `Automatically generated
lookup-table`.

### **Permanent magnet flux linkage (Wb)** — PM Flux Linkage `0.04` (default) | positive scalar

Peak permanent magnet flux linkage, in
`Wb`.

### **D-axis inductance (H)** — Inductance of d-axis `0.00024` (default) | positive scalar

Direct-axis inductance, in `H`.

### **Q-axis inductance (H)** — Inductance of q-axis `0.00029` (default) | positive scalar

Quadrature-axis inductance, in `H`.

### **Stator resistance (Ohm)** — Resistance of stator `0.01` (default) | positive scalar

Stator resistance per phase, in `Ohm`.

#### Inner Loop

### **D-axis current proportional gain** — D-axis proportional gain `1` (default) | positive number

Proportional gain of the PI controller used for direct-axis current
control.

### **D-axis current integral gain** — D-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for direct-axis current
control.

### **D-axis current anti-windup gain** — D-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for direct-axis current
control.

### **Q-axis current proportional gain** — Q-axis proportional gain `1` (default) | positive number

Proportional gain of the PI controller used for quadrature-axis current
control.

### **Q-axis current integral gain** — Q-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for quadrature-axis current
control.

### **Q-axis current anti-windup gain** — Q-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for quadrature-axis current
control.

### **Axis prioritization** — Axis prioritization for voltage limiter `q-axis` (default) | `d-axis` | `d-q equivalence`

Prioritize or maintain ratio between *d*- and
*q*-axis when the block limits voltage.

### **Enable zero cancellation** — Feedforward zero cancellation `off` (default) | `on`

Enable or disable zero cancellation on the feedforward path.

### **Enable pre-control voltage** — Precontrol voltage `on` (default) | `off`

Enable or disable precontrol voltage.

### **Machine parameters** — Machine parameterization `Constant parameters` (default) | `Lookup table based parameters`

Specify how to parameterize the machine.

- `Constant parameters` — Specify
  machine parameters that are constant throughout the
  simulation.
- `Lookup table based parameters` —
  Specify machine parameters as lookup tables that depend on
  current.

### **D-axis inductance for feed-forward pre-control (H)** — Feedforward d-axis inductance `0.00024` (default) | positive scalar

Direct-axis inductance for feedforward precontrol, in
`H`.

### **Q-axis inductance for feed-forward pre-control (H)** — Feedforward q-axis inductance `0.00029` (default) | positive scalar

Quadrature-axis inductance for feed-forward pre-control, in
`H`.

### **Permanent magnet flux linkage for feed-forward pre-control (H)** — Feedforward flux linkage `0.04` (default) | scalar

Permanent magnet flux linkage for feedforward pre-control, in
`H`.

### **D-axis current vector, id (A)** — D-axis current breakpoint vector `[-200,0,200]` (default) | monotonically increasing vector

Direct-axis current vector, in `A`, used in the
lookup tables for parameters determination. For constant machine parameters,
do not change the default.

### **Q-axis current vector, iq (A)** — Q-axis current breakpoint vector `[-200,0,200]` (default) | monotonically increasing vector

Quadrature-axis current vector, in `A`, used in
the lookup tables for parameters determination. For constant machine
parameters, do not change the default.

### **Ld matrix, Ld(id,iq) (H)** — D-axis inductance lookup data `0.0002 * ones(3, 3)` (default) | positive matrix

*Ld* matrix used as lookup table
data, in `H`. For constant machine parameters
change only the constant factor, for example,
*Ld* \* `ones(3,
3)`.

### **Lq matrix, Lq(id,iq) (H)** — Q-axis inductance lookup data `0.0002 * ones(3, 3)` (default) | positive matrix

*Lq* matrix used as lookup table
data, in `H`. For constant machine parameters
change only the constant factor, for example,
*Lq* \* `ones(3,
3)`.

### **Permanent magnet flux linkage matrix, PM(id,iq) (Wb)** — Flux linkage lookup data `0.04 * ones(3, 3)` (default) | real matrix

Permanent magnet flux linkage matrix used in the lookup table, in
`Wb`. For constant machine parameters change
only the constant factor, for example, *psim* \*
`ones(3, 3)`.

#### PWM

### **PWM method** — Pulse width modulation method `SVM: space vector modulation` (default) | `SPWM: sinusoidal PWM`

Specify the waveform technique.

### **Sampling mode** — Wave-sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

Specify whether the block samples the modulation waveform when the waves
intersect or when the carrier wave is at one or both of its boundary
conditions.

### **Switching frequency (Hz)** — Switching rate `1000` (default) | positive integer

Specify the rate at which you want the switches in the power converter to
switch.

## Libraries

Simscape / Electrical / Control / PMSM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Permanent magnet synchronous machine field-oriented control

The PMSM Field-Oriented Control block implements a field-oriented
control structure for a permanent magnet synchronous machine (PMSM). Field Oriented
Control (FOC) is a performant AC motor control strategy that decouples torque and flux
by transforming the stationary phase currents to a rotating frame. Use FOC when rotor
speed and position are known and your application requires:

- High torque and low current at startup.
- High efficiency.

### Equations

The PMSM FOC structure decouples the torque and flux by using the rotor d-q
reference frame. This diagram shows the overall architecture of the block.

In the diagram:

- *ω* and
  *ωref* are the measured and
  reference angular velocities, respectively.
- *Tref* is the reference
  electromagnetic torque.
- *i* and *v* are stator currents and
  voltages and subscripts *d* and *q*
  represent the *d*-axis and
  *q*-axis, and subscripts *a*,
  *b*, and *c*, represent the three
  stator windings.
- *θe* is the rotor electrical
  angle.
- *G* is a gate pulse, subscripts *H*
  and *L*, represent high and low, and subscripts
  *a*, *b*, and *c*
  represent the three stator windings.

You can choose to implement either velocity or torque control with
the `Control mode` parameter. The block implements velocity
control exactly as shown in the diagram. The block implements torque control by
removing the Velocity Controller block and accepting the reference torque
directly.

### Assumptions

The machine parameters are known.

### Limitations

The control structure is implemented with a single sample rate.
