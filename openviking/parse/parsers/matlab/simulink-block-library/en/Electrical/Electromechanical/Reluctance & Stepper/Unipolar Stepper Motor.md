---
type: simulink-block
title: 'Unipolar Stepper Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'unipolarsteppermotor'
documentation_source_path: 'ref/unipolarsteppermotor.html'
language: en
---

# Unipolar Stepper Motor

## Ports
```yaml
ports:
- name: A+
  summary: Top A-phase electrical connection electrical
  direction: conserving
- name: A0
  summary: A-phase center tap connection electrical
  direction: conserving
- name: A-
  summary: Lower A-phase electrical connection electrical
  direction: conserving
- name: B+
  summary: Top B-phase electrical connection electrical
  direction: conserving
- name: B0
  summary: B-phase center tap connection electrical
  direction: conserving
- name: B-
  summary: Lower B-phase electrical connection electrical
  direction: conserving
- name: C
  summary: Case mechanical
  direction: conserving
- name: R
  summary: Rotor mechanical
  direction: conserving
- name: HA+
  summary: Thermal port for winding between A+ and A0 thermal
  direction: conserving
- name: HA-
  summary: Thermal port for winding between A- and A0 thermal
  direction: conserving
- name: HB+
  summary: Thermal port for winding between B+ and B0 thermal
  direction: conserving
- name: HB-
  summary: Thermal port for winding between B- and B0 thermal
  direction: conserving
- name: HR
  summary: Rotor thermal port thermal
  direction: conserving
```

### Conserving

### **A+** — Top A-phase electrical connection electrical

Electrical conserving port associated with the top A-phase electrical
connection.

### **A0** — A-phase center tap connection electrical

Electrical conserving port associated with the A-phase center tap
connection.

### **A-** — Lower A-phase electrical connection electrical

Electrical conserving port associated with the lower A-phase
electrical connection.

### **B+** — Top B-phase electrical connection electrical

Electrical conserving port associated with the top B-phase electrical
connection.

### **B0** — B-phase center tap connection electrical

Electrical conserving port associated with the B-phase center tap
connection.

### **B-** — Lower B-phase electrical connection electrical

Electrical conserving port associated with the lower B-phase
electrical connection.

### **C** — Case mechanical

Mechanical rotational conserving port associated with the case.

### **R** — Rotor mechanical

Mechanical rotational conserving port associated with the
rotor.

### **HA+** — Thermal port for winding between A+ and A0 thermal

Thermal port for winding between **A+** and
**A0**. For more information, see Model Thermal Effects.

### **HA-** — Thermal port for winding between A- and A0 thermal

Thermal port for winding between **A-** and
**A0**.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB+** — Thermal port for winding between B+ and B0 thermal

Thermal port for winding between **B+** and
**B0**.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB-** — Thermal port for winding between B- and B0 thermal

Thermal port for winding between **B-** and
**B**.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal port thermal

Thermal port for rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal ports No thermal port (default) | Show thermal port
  group: ''
- name: Simulation mode
  summary: Simulation mode Stepping (default) | Averaged
  group: Electrical Torque
- name: Vector of rotational speeds
  summary: Vector of rotational speeds [0, 1000, 3000] rpm (default)
  group: Electrical Torque
- name: Vector of maximum torque values
  summary: Vector of maximum torque values [2, 2, 1] N*m (default)
  group: Electrical Torque
- name: Action on slipping
  summary: Action upon detecting slip none (default) | warn | error
  group: Electrical Torque
- name: Approximate total load inertia
  summary: Approximate total load inertia 1e-4 kg*m^2 (default)
  group: Electrical Torque
- name: Maximum step rate command
  summary: Maximum step rate command 10 Hz (default)
  group: Electrical Torque
- name: Half-winding resistance
  summary: Half-winding resistance 0.55 Ohm (default)
  group: Electrical Torque
- name: Half-winding inductance
  summary: Half-winding inductance 1.5e-3 H (default)
  group: Electrical Torque
- name: Motor torque constant
  summary: Motor torque constant 0.19 N*m/A (default)
  group: Electrical Torque
- name: Detent torque
  summary: Detent torque 0 N*m (default)
  group: Electrical Torque
- name: Magnetizing resistance
  summary: Magnetizing resistance inf Ohm (default) | positive scalar
  group: Electrical Torque
- name: Full step size
  summary: Full step size 1.8 deg (default)
  group: Electrical Torque
- name: Coefficient of coupling
  summary: Coefficient of coupling for mutual inductance 0 (default)
  group: Electrical Torque
- name: Rotor inertia
  summary: Rotor inertia 4.5e-5 kg*m^2 (default)
  group: Mechanical
- name: Rotor damping
  summary: Rotor damping 8.0e-4 N*m/(rad/s) (default)
  group: Mechanical
- name: Initial rotor speed
  summary: Initial rotor speed 0 rpm (default)
  group: Mechanical
- name: Initial rotor angle
  summary: Initial rotor angle 0 deg (default)
  group: Mechanical
- name: Resistance temperature coefficient
  summary: Resistance temperature coefficient 3.93e-3 1/K (default)
  group: Temperature Dependence
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default)
  group: Temperature Dependence
- name: Vector of maximum torque values at second measurement temperature
  summary: Vector of maximum torque values at second measurement temperature [1.7, 1.7, .85] N*m (default)
  group: Temperature Dependence
- name: Second measurement temperature
  summary: Second measurement temperature 125 degC (default)
  group: Temperature Dependence
- name: Stepping mode
  summary: Stepping mode Full stepping (default) | Half stepping
  group: Temperature Dependence
- name: Half-winding thermal mass
  summary: Half-winding thermal mass 100 J/K (default)
  group: Thermal Port
- name: Half-winding initial temperatures, [T_A+ T_A- T_B+ T_B-]
  summary: Half-winding initial temperatures [25, 25, 25, 25] degC (default)
  group: Thermal Port
- name: Rotor thermal mass
  summary: Rotor thermal mass 50 J/K (default)
  group: Thermal Port
- name: Rotor initial temperature
  summary: Rotor initial temperature 25 degC (default)
  group: Thermal Port
- name: Percentage of magnetizing resistance associated with the rotor
  summary: Percentage of magnetizing resistance associated with the rotor 90 (default)
  group: Thermal Port
```

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that convert
power to heat.

### Electrical Torque

### **Simulation mode** — Simulation mode `Stepping` (default) | `Averaged`

Select `Stepping` or
`Averaged`. Use
`Averaged` only if the block is connected
directly to a Unipolar Stepper Motor
Driver block also running in Averaged mode.

### **Vector of rotational speeds** — Vector of rotational speeds `[0, 1000, 3000]` `rpm` (default)

Vector of rotational speeds at which to define maximum torque values,
for slip prediction.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Averaged`.

### **Vector of maximum torque values** — Vector of maximum torque values `[2, 2, 1]` `N*m` (default)

Vector of maximum torque values, to be used for slip prediction in
conjunction with the **Vector of rotational speeds**
parameter. The maximum torque values are often given on a datasheet, and
should correspond to the supply voltage and stepping type (half step or
full step) specified in the driver.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Averaged`.

### **Action on slipping** — Action upon detecting slip `none` (default) | `warn` | `error`

Select the action for the block to perform during simulation upon
detecting slip:

- `none` — Continue simulation,
  limiting the load torque according to the **Vector of
  maximum torque values**.
- `warn` — Continue simulation,
  limiting the load torque according to the **Vector of
  maximum torque values**, and generate a warning
  that the rotor is slipping.
- `error` — Stop the simulation
  and generate an error message that the rotor is slipping.

Note that if you choose an action that lets the simulation continue,
simulation results may be incorrect: when slipping occurs, the torque
generated by the motor will not generally be the maximum available
torque; the maximum torque is only achieved if the stepper controller
detects slip and adjusts the step rate command accordingly.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Averaged`.

### **Approximate total load inertia** — Approximate total load inertia `1e-4` `kg*m^2` (default)

The approximate total load inertia, including the rotor inertia. This
value is used to help predict when slipping will occur due to rapid
acceleration demands.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Averaged`.

### **Maximum step rate command** — Maximum step rate command `10` `Hz` (default)

The maximum step rate that your system will command. It is used to
determine a suitable bandwidth for the second order system approximation
to the stepper motor and driver.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Averaged`.

### **Half-winding resistance** — Half-winding resistance `0.55` `Ohm` (default)

Half of the resistance of the A and B phase windings as measured
between the **A+** and **A-**, and the
**B+** and **B-** ports.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Stepping`.

### **Half-winding inductance** — Half-winding inductance `1.5e-3` `H` (default)

Half of the inductance of the A and B phase windings as measured
between the **A+** and **A-**, and the
**B+** and **B-** ports.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Stepping`.

### **Motor torque constant** — Motor torque constant `0.19` `N*m/A` (default)

Motor torque constant *Km*.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Stepping`.

### **Detent torque** — Detent torque `0` `N*m` (default)

The amplitude of the sinusoidal torque variation observed when
rotating the shaft of the unpowered motor.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Stepping`.

### **Magnetizing resistance** — Magnetizing resistance `inf` `Ohm` (default) | positive scalar

The total magnetizing resistance seen from each of the phase windings,
for example across **A+** and **A0**.
The value must be greater than zero. The default value is
`Inf`, which implies that there are no iron
losses.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter to
`Stepping`.

### **Full step size** — Full step size `1.8` `deg` (default)

Step size when changing the polarity of the A or B phase
current.

This value is equal to
(π/2)/*Nr* where
*Nr* is the number of
teeth on each of the two rotor poles.

### **Coefficient of coupling** — Coefficient of coupling for mutual inductance `0` (default)

Coefficient of coupling of the windings for mutual inductance.

### Mechanical

### **Rotor inertia** — Rotor inertia `4.5e-5` `kg*m^2` (default)

Resistance of the rotor to change in motor motion. The value can be
zero.

### **Rotor damping** — Rotor damping `8.0e-4` `N*m/(rad/s)` (default)

Energy dissipated by the rotor. The value can be zero.

### **Initial rotor speed** — Initial rotor speed `0` `rpm` (default)

Speed of the rotor at the start of the simulation.

### **Initial rotor angle** — Initial rotor angle `0` `deg` (default)

Angle of the rotor at the start of the simulation.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Parameter α in the equation defining resistance as a function of
temperature, as described in Thermal Model for Actuator Blocks. It is assumed that all
windings are made of the same material, and therefore have the same
resistance temperature coefficient.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter in the
**Electrical Torque** setting to
`Stepping`.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

The temperature for which motor parameters are defined.

### **Vector of maximum torque values at second measurement temperature** — Vector of maximum torque values at second measurement temperature `[1.7, 1.7, .85]` `N*m` (default)

Vector of maximum torque values at second measurement
temperature.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter in the
**Electrical Torque** setting to
`Averaged`.

### **Second measurement temperature** — Second measurement temperature `125` `degC` (default)

Second measurement temperature.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter in the
**Electrical Torque** setting to
`Averaged`.

### **Stepping mode** — Stepping mode `Full stepping` (default) | `Half stepping`

Specify stepping mode.

#### Dependencies

This parameter is visible only when you set the
**Simulation mode** parameter in the
**Electrical Torque** setting to
`Averaged`.

### Thermal Port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Half-winding thermal mass** — Half-winding thermal mass `100` `J/K` (default)

The thermal mass for half of either the A or B winding. The thermal
mass is the energy required to raise the temperature by one degree. It
is assumed that all four half-windings have the same thermal
mass.

### **Half-winding initial temperatures, [T\_A+ T\_A- T\_B+ T\_B-]** — Half-winding initial temperatures `[25, 25, 25, 25]` `degC` (default)

A 1 by 4 row vector defining the temperature of the four half-windings
at the start of simulation.

### **Rotor thermal mass** — Rotor thermal mass `50` `J/K` (default)

The thermal mass of the rotor, that is, the energy required to raise
the temperature of the rotor by one degree.

### **Rotor initial temperature** — Rotor initial temperature `25` `degC` (default)

The temperature of the rotor at the start of simulation.

### **Percentage of magnetizing resistance associated with the rotor** — Percentage of magnetizing resistance associated with the rotor `90` (default)

The percentage of the magnetizing resistance associated with the
magnetic path through the rotor. It determines how much of the iron loss
heating is attributed to the rotor thermal port HR, and how much is
attributed to the four winding thermal ports.
## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Permanent magnet stepper motor with center taps on each of the two windings

The Unipolar Stepper Motor block models a unipolar
stepper motor. Unipolar stepper motors have a permanent magnet rotor and two wound
stator windings with center taps. The center taps simplify the stepper driver design
because the polarity of the driver output does not need to change. If your motor does
not have a center tap on each of the stator windings, use the Stepper Motor block instead.

Stepper motors with small step sizes typically have north and south pole rotors with
teeth. Stepper motors with large step sizes typically have multiple magnets distributed
around the rotor circumference. You can model both types of motor using the
Unipolar Stepper Motor block and drive the motor
using the Unipolar Stepper Motor Driver
block.

You can use stepper motors to avoid the need for a position measurement. You can use
stepper motors in devices such as printers and in applications like robotics and factory
automation.

These equations define the winding currents and mechanical output,

eA+=−Kmωsin(Nrθ)

eA−=Kmωsin(Nrθ)

eB+=Kmωcos(Nrθ)

eB−=−Kmωcos(Nrθ)

diA+dt=(vA+−RiA+−eA+)/L

diA−dt=(vA−−RiA−−eA−)/L

diB+dt=(vB+−RiB+−eB+)/L

diB−dt=(vB−−RiB−−eB−)/L

Jdωdt+Bω=Te

Te=−Km(iA+−iA−−eA+−eA−Rm)sin(Nrθ)+Km(iB+−iB−−eB+−eB−Rm)cos(Nrθ)−Tdsin(4Nrθ)

dθdt=ω

where:

- *eA+* is the back electromotive
  force (EMF) induced across the **A+** to
  **A0** half-winding.
- *eA-* is the back EMF induced
  across the **A-** to **A0**
  half-winding.
- *eB+* is the back EMF induced
  across the **B+** to **B0**
  half-winding.
- *eB-* is the back EMF induced
  across the **B-** to **B0**
  half-winding.
- *iA+* is the current that flows
  from the **A+** port to the **A0** center
  tap port.
- *iA-* is the current that flows
  from the **A-** port to the **A0** center
  tap port.
- *iB+* is the current that flows
  from the **B+** port to the **B0** center
  tap port.
- *iB-* is the current that flows
  from the **B-** port to the **B0** center
  tap port.
- *vA+* is the voltage at the
  **A+** port relative to the **A0**
  center tap port.
- *vA-* is the voltage at the
  **A-** port relative to the **A0**
  center tap port.
- *vB+* is the voltage at the
  **B+** port relative to the **B0**
  center tap port.
- *vB-* is the voltage at the
  **B-** port relative to the **B0**
  center tap port.
- *Km* is the motor torque
  constant.
- *Nr* is the number of teeth on
  each of the two rotor poles.
- *R* is the half-winding resistance. For example, it is
  the resistance between the **A+** and
  **A0** ports.
- *L* is the half-winding inductance. For example, it is
  the inductance between the **A+** and
  **A0** ports.
- *R*m is the magnetizing
  resistance.
- *B* is the rotational damping.
- *J* is the inertia.
- *ω* is the rotor speed.
- *Θ* is the rotor angle.
- *Td* is the detent torque
  amplitude.
- *Te* is the electrical
  torque.

If the initial rotor angle is zero or a multiple of
(π/2)/*N*r, the rotor is aligned with the
A-phase winding. If a positive current flows from the **A+** port to
the **A0** center tap port, then the stepper acts to stay aligned with
the A-phase. Equivalently, a positive current flowing from the **A0**
center tap port to the **A-** port also acts on the rotor to stay
aligned with the A-phase.

The Unipolar Stepper Motor block produces a positive torque acting from
the mechanical **C** to **R** ports for the four sequences listed in
this table. The sequences assume the rotor initial angle is zero or a multiple of
(π/2)/*N*r.

| Sequence | Center Taps Connected to Ground | Center Taps Connected to Positive Supply |
| --- | --- | --- |
| 1 | Positive current from **A+** to **A0** | Positive current from **A0** to **A-** |
| 2 | Positive current from **B+** to **B0** | Positive current from **B0** to **B-** |
| 3 | Positive current from **A-** to **A0** | Positive current from **A0** to **A-** |
| 4 | Positive current from **B-** to **B0** | Positive current from **B0** to **B-** |

### Averaged Mode

If you set the **Simulation mode** parameter to
`Averaged`, both for a Unipolar Stepper
Motor block and for the Unipolar Stepper Motor
Driver block that controls it, then the individual steps are not
simulated. This can be a good way to speed up simulation. In Averaged mode, under
non-slipping conditions, the motor and driver are represented by a second-order
linear system that tracks the specified step rate. The demanded step rate is
determined directly from voltage across **A+** and
**A-**. So, for example, a voltage of +10V across the
**A+** and **A-** terminals is interpreted as
a step rate demand of ten steps per second. See the Unipolar Stepper Motor Driver reference page for more
information on how to connect the Unipolar Stepper Motor
Driver to your step angle controller.

Averaged mode includes a slip estimator to predict whether the stepper motor would
have slipped if running in Stepping simulation mode. Slip is predicted if the motor
torque exceeds the **Vector of maximum torque values** parameter
value for longer than one step period, the step period being determined from the
current step rate demand. Upon detecting slip, the simulation will proceed or stop
with an error, according to the **Action on slipping** parameter
value. If you choose the action that lets the simulation continue, note that
simulation results may be incorrect: when slipping occurs, the torque generated by
the motor will not generally be the maximum available torque; the maximum torque is
only achieved if the stepper controller detects slip and adjusts the step rate
command accordingly.

The dynamics of the equivalent second-order system are determined from the values
that you specify for the **Approximate total load inertia** and
**Maximum step rate command** parameters. It is important that
you set as accurate values as possible for these parameters, so that the step rate
command is tracked, and the block does not generate false slipping warnings or
errors.

If you run the motor in Averaged mode with the optional thermal ports exposed (see
Model Thermal Effects), then heat is added to the thermal ports assuming that
the windings are always powered, even when the step rate command is zero. The block
makes adjustments for half stepping and for reduced torque (and winding currents) at
higher speeds. For these adjustments to be correct, the **Vector of maximum
torque** parameter values must be correct. For half stepping, at zero
speed the heat generated by the block is the average of that generated when stopped
at a half step and at a full step.

If you simulate or predict slip, do some validation runs comparing Stepping and
Averaged modes before using the averaged model representation for simulation
studies.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses
that convert power to heat. To expose the thermal ports, set the **Modeling
option** parameter to either:

- `No thermal port` — The block does not contain thermal
  ports.
- `Show thermal port` — The block contains multiple thermal
  conserving ports.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.
