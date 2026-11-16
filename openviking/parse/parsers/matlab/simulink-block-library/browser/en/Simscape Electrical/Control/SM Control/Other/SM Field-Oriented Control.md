---
type: simulink-block
title: 'SM Field-Oriented Control'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Other'
documentation_page: 'smfieldorientedcontrol'
documentation_source_path: 'ref/smfieldorientedcontrol.html'
language: en
---

# SM Field-Oriented Control

## Ports

### Input

### **Reference** — System reference scalar

System reference specified as torque reference in N\*m or velocity
reference in rad/s, depending on the control mode selected.

**Data Types:** `single` | `double`

### **iabcSens** — Measured phase currents vector

Measured stator phase currents, in A.

**Data Types:** `single` | `double`

### **ifSens** — Measured field current scalar

Measured rotor field current, in A.

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

### **G** — Stator converter gate pulses vector

Six pulse waveforms that determine switching behavior in the attached
power converter.

**Data Types:** `single` | `double`

### **Gr** — Excitation chopper gate pulses vector

Waveforms that determine switching behavior in the attached excitation
chopper. The size of the waveform depends on the selected chopper type.
To specify the chopper type, use the **Chopper type** parameter:

- `First and fourth quadrant
  chopper` — The output waveform has two
  pulses.
- `Four-quadrant chopper` — The
  output waveform has four pulses.

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
- `idqf`
- `vdqRef`
- `modWave`
- `DCexcit`

**Data Types:** `single` | `double`

## Parameters

### General

### **Control mode** — Control mode strategy `Velocity control` (default) | `Torque control`

Specify either a torque control or velocity control strategy.

### **Nominal dc-link voltage (V)** — Rated DC voltage `300` `V` (default) | positive number

Nominal DC-link voltage of the electrical source.

### **Maximum power (W)** — Maximum power `60000` `W` (default) | positive number

Maximum machine power.

### **Maximum torque (N\*m)** — Maximum torque `250` `N*m` (default) | positive number

Maximum machine torque.

### **Maximum field current (A)** — Maximum field current `25` `A` (default) | positive number

Maximum current in the field winding.

### **Inverter dc-link voltage threshold (V)** — DC-link voltage threshold `100` `V` (default) | positive number

Voltage threshold to activate the power inverter.

### **Number of rotor pole pairs** — Pole pairs `4` (default) | positive integer

Number of pole pairs on the rotor.

### **Fundamental sample time (s)** — Block sample time `5e-6` (default) | positive number

Fundamental sample time for the block.

### Outer Loop

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

### **Current references** — Current reference strategy `Zero d-axis control` (default) | `Lookup-table based`

Select the current reference strategy.

### **Mechanical speed vector, wMechanical (rpm)** — Rotor speed lookup vector `[0, 3000]` `rpm` (default) | positive monotonically increasing vector

Speed vector used in the lookup tables for determining current
references.

### **Torque reference vector, TqRef (N\*m)** — Torque reference lookup vector `[-100, 0, 100]` `N*m` (default) | positive monotonically increasing vector

Torque vector used in the lookup tables for determining current
references.

### **DC-link voltage vector, Vdc (V)** — DC-link voltage lookup vector `[300, 350]` `V` (default) | positive monotonically increasing vector

DC-link voltage vector used in the lookup tables for determining current
references.

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)** — Reference d-axis current values `zeros(2,3,2)` `A` (default) | real matrix

Direct-axis current reference lookup data.

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)** — Reference q-axis current values `zeros(2,3,2)` `A` (default) | real matrix

Quadrature-axis current reference lookup data.

### **Field current reference matrix, if(wMechanical,TqRef,Vdc), (A)** — Reference field current values `zeros(2,3,2)` `A` (default) | real matrix

Field current reference lookup data.

### **Torque constant** — Motor torque constant `0.04` `N*m/A` (default) | positive scalar

Synchronous machine torque constant. This value is numerically
equivalent to the back EMF constant expressed in
`V/(rad/s)`.

### Inner Loop

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

Proportional gain of the PI controller used for quadrature-axis
current control.

### **Q-axis current integral gain** — Q-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for quadrature-axis current
control.

### **Q-axis current anti-windup gain** — Q-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for quadrature-axis current
control.

### **Field current proportional gain** — Field winding proportional gain `10` (default) | positive number

Proportional gain of the PI controller used for field current
control.

### **Field current integral gain** — Field winding integral gain `1000` (default) | positive number

Integral gain of the PI controller used for field current
control.

### **Field current anti-windup gain** — Field winding anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for field current
control.

### **Axis prioritization** — Axis prioritization for voltage limiter `q-axis` (default) | `d-axis` | `d-q equivalence`

Prioritize or maintain ratio between *d*- and
*q*-axis when the block limits voltage.

### **Enable zero cancellation** — Feedforward zero cancellation `off` (default) | `on`

Enable or disable zero cancellation on the feedforward path.

### **Enable pre-control voltage** — pre-control voltage `on` (default) | `off`

Enable or disable pre-control voltage.

### **Machine parameters** — Machine parameterization `Constant parameters` (default) | `Lookup table based parameters`

Specify how to parameterize the machine.

- `Constant parameters` — Specify
  machine parameters that are constant throughout the
  simulation.
- `Lookup table based parameters` —
  Specify machine parameters as lookup tables that depend on
  current.

#### Dependencies

Enabled when the **Enable pre-control voltage**
parameter is selected.

### **D-axis inductance (H)** — Feedforward d-axis inductance `0.00024` (default) | positive scalar

Direct-axis inductance for feedforward pre-control.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Constant parameters`.

### **Q-axis inductance (H)** — Feedforward q-axis inductance `0.00029` (default) | positive scalar

Quadrature-axis inductance for feedforward pre-control.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Constant parameters`.

### **Mutual field armature inductance (H)** — Mutual inductance between field and armature `0.007` (default)

Mutual inductance between the field and armature windings.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Constant parameters`.

### **D-axis current vector, id (A)** — D-axis current breakpoint vector `[-200,0,200]` `A` (default) | monotonically increasing vector

Direct-axis current vector used in the lookup tables for parameters
determination.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Lookup table based
parameters`.

### **Q-axis current vector, iq (A)** — Q-axis current breakpoint vector `[-200,0,200]` `A` (default) | monotonically increasing vector

Quadrature-axis current vector used in the lookup tables for parameters
determination.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Lookup table based
parameters`.

### **Field current vector, if (A)** — Field winding current vector `[0,20]` `A` (default) | monotonically increasing vector

Field current vector used in the lookup tables for parameters determination.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Lookup table based
parameters`.

### **Ld matrix, Ld(id,iq) (H)** — D-axis inductance lookup data `0.0002 * ones(3, 3)` `H` (default) | positive matrix

*Ld* matrix used as lookup table data.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Lookup table based
parameters`.

### **Lq matrix, Lq(id,iq) (H)** — Q-axis inductance lookup data `0.0002 * ones(3, 3)` `H` (default) | positive matrix

*Lq* matrix used as lookup table data.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Lookup table based
parameters`.

### **Lmf matrix, Lmf(id,iq,if), (H)** — Field-armature mutual inductance lookup `0.007 * ones(2,2,2)` `H` (default) | positive matrix

*Lmf* matrix used as lookup table data.

#### Dependencies

Enabled when the **Machine parameters** parameter
is set to `Lookup table based
parameters`.

### PWM

### **PWM method** — Pulse width modulation method `SVM: space vector modulation` (default) | `SPWM: sinusoidal PWM`

Specify the waveform technique.

### **Sampling mode** — Wave-sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

Specify whether the block samples the modulation waveform when the
waves intersect or when the carrier wave is at one or both of its
boundary conditions.

### **Switching frequency (Hz)** — Switching rate `1000` `Hz` (default) | positive integer

Specify the rate at which you want the switches in the power converter
to switch.

### **Chopper type** — DC-DC chopper type `First and fourth quadrant chopper` (default) | `Four-quadrant chopper`

Specify DC-DC chopper type.

### **Switching frequency excitation (Hz)** — Excitation system switching frequency `1000` `Hz` (default) | positive integer

Specify PWM switching frequency for excitation system.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Synchronous machine field-oriented control

The SM Field-Oriented Control block implements a synchronous machine (SM)
field-oriented control structure. Field Oriented Control (FOC) is a performant AC motor
control strategy that decouples torque and flux by transforming the stationary phase
currents to a rotating frame. Use FOC when rotor speed and position are known and your
application requires:

- High torque and low current at startup
- High efficiency

### Equations

The SM FOC is made up of several control blocks from the Control library. To see and modify
these blocks and the FOC's internal structure, right-click the block in Simulink and
select **Mask** > **Look Under Mask**.
The overall control structure is made up of several parts:

- The outer loop controller converts the reference signal you supply to
  the reference *d*-axis, *q*-axis, and
  field currents.

  You can choose the type of reference signal you provide using the
  `Control mode` parameter:

  - `Velocity control` — Control or
    regulate the rotation speed of the synchronous machine. An
    internal Velocity Controller block generates a reference
    torque from the rotor speed error.
  - `Torque control` — Control or
    regulate the mechanical torque of the SM.

  An internal SM
  Current Reference Generator block generates the reference
  currents using a proportional-integral (PI) controller, minimizing the
  torque error.
- The inner loop controller converts the current references into voltage
  references. An internal SM
  Current Controller generates the voltage references using a
  PI controller minimizing the current error, and the feedforward terms:

  vd\_FF=−ωeLqiqvq\_FF=ωe(Ldid+Lmfif)vf\_FF=0

  where:

  - *ωe* is the rotor
    electrical angular velocity.
  - *Ld* and
    *Lq* are the
    *d*- and *q*-axis
    stator inductances.
  - *Lmf* is the
    mutual field armature inductance.
  - *id*,
    *iq*, and
    *if*, are
    the stator *d*-*q* and
    field excitation currents, respectively.
- The PWM Generator converts the reference stator voltages into gate
  pulses to be passed to a Power Converter that is powering the stator
  windings of the synchronous machine.
- The Excitation PWM Generator converts the reference field voltage into
  gate pulses to be passed to a DC-DC Chopper powering the SM field
  winding.

This diagram shows the overall architecture of the block.

In the diagram:

- *ω* and
  *ωref* are the measured and
  reference angular velocities, respectively.
- *Tref* is the reference
  electromagnetic torque. If you configure the block for speed control, a
  Velocity Controller generates this reference torque.
- *i* and *v* are stator currents and
  voltages. Subscripts *d*, *q*, and
  *f*, represent the *d*-axis,
  *q*-axis, and field winding. Subscripts
  *a*, *b*, and
  *c*, represent the three stator windings.
- *θe* is the rotor electrical
  angle.
- *G* is a gate pulse, subscripts *H*
  and *L* represent high and low, and subscripts
  *a*, *b*, and
  *c*, represent the three stator windings. Subscript
  *ex* represents the field excitation pulses.

You can choose to implement either velocity or torque control with
the `Control mode` parameter. The block implements velocity
control exactly as shown in the diagram. The block implements torque control by
removing the Velocity Controller block and accepting the reference torque
directly.

### Assumptions

The machine parameters are known.

### Limitations

The control structure is implemented with a single sample rate.
