---
type: simulink-block
title: 'Stepper Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Reluctance and Stepper'
documentation_page: 'steppermotor'
documentation_source_path: 'ref/steppermotor.html'
language: en
---

# Stepper Motor

## Ports

### Conserving

### **A+** — A-phase positive terminal electrical

Electrical conserving port associated with the A-phase positive
terminal.

### **A-** — A-phase negative terminal electrical

Electrical conserving port associated with the A-phase negative
terminal.

### **B+** — B-phase positive terminal electrical

Electrical conserving port associated with the B-phase positive
terminal.

### **B-** — B-phase negative terminal electrical

Electrical conserving port associated with the B-phase negative
terminal.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port connected to the motor
case.

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port connected to the rotor.

### **HA** — Winding A thermal mass thermal

Thermal conserving port associated with the thermal mass of winding A.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB** — Winding B thermal mass thermal

Thermal conserving port associated with the thermal mass of winding B.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal mass thermal

Thermal conserving port associated with the thermal mass of the
rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations.

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that convert
power to heat.

### Electrical Torque

### **Simulation mode** — Simulation mode `Stepping` (default) | `Averaged`

Use `Averaged` only if the block is connected
directly to a Stepper Motor Driver block
also running in Averaged mode.

### **Vector of rotational speeds** — Rotor speeds `[0, 1000, 3000]` `rpm` (default) | positive vector

Vector of rotational speeds at which to define maximum torque values,
for slip prediction.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Averaged`.

### **Vector of maximum torque values** — Maximum torques `[2, 2, 1]` `N*m` (default) | positive vector

Vector of maximum torque values, to be used for slip prediction with
the **Vector of rotational speeds** parameter. These
values are often given on a datasheet, and correspond to the supply
voltage and stepping type (half step or full step) specified in the
driver.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Averaged`.

### **Action on slipping** — Slip response `none` (default) | `warn` | `error`

Select the action for the block to perform during simulation upon
detecting slip:

- `none` — Continue simulation,
  limiting the load torque according to the **Vector of
  maximum torque values**.
- `warn` — Continue simulation,
  limiting the load torque according to the **Vector of
  maximum torque values**, and generate a warning
  that the rotor is slipping.
- `error` — Stop the simulation and
  generate an error message that the rotor is slipping.

If you choose an action that lets the simulation continue, simulation
results might be incorrect. When slipping occurs, the motor does not
always generate maximum torque. The maximum torque is only achieved if
the stepper controller detects slip and adjusts the step rate command
accordingly.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Averaged`.

### **Approximate total load inertia** — Total load inertia `1e-4` `kg*m^2` (default) | positive number

Approximate total load inertia, including the rotor inertia. This
value is used to help predict slip due to rapid acceleration
demands.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Averaged`.

### **Maximum step rate command** — Maximum command frequency `10` `Hz` (default) | positive number

Maximum commanded step rate of the system. It is used to determine a
suitable bandwidth for the second order system approximation to the
stepper motor and driver.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Averaged`.

### **Phase winding resistance** — Phase resistance `0.55` `Ohm` (default) | positive number

Resistance of the A and B phase windings.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Stepping`.

### **Phase winding inductance** — Phase inductance `1.5e-3` `Ohm` (default) | positive number

Inductance of the A and B phase windings.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Stepping`.

### **Motor torque constant** — Torque constant `0.19` `N*m/A` (default) | positive number

Motor torque constant,
*Km*.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Stepping`.

### **Detent torque** — Torque variation amplitude `0` `N*m` (default) | positive number

Amplitude of the sinusoidal torque variation observed when rotating
the shaft of the unpowered motor.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Stepping`.

### **Magnetizing resistance** — Phase magnetizing resistance `inf` (default) | strictly positive number

Total magnetizing resistance seen from each of the phase windings. The
value must be greater than zero. The default value is
`Inf`, which implies that there are no iron
losses.

#### Dependencies

To enable this parameter, set **Simulation mode**
to `Stepping`.

### **Full step size** — Step size `1.8` `deg` (default) | positive number

Step size when changing the polarity of the A or B phase
current.

This value is equal to
(π/2)/*Nr* where
*Nr* is the number of
teeth on each of the two rotor poles.

### Mechanical

### **Rotor inertia** — Rotational inertia `4.5e-5` `kg*m^2` (default) | zero or positive number

Conservative force resisting rotor acceleration.

### **Rotor damping** — Rotational damping `8.0e-4` `N*m/(rad/s)` (default) | zero or positive number

Dissipative force resisting rotor speed.

### **Initial rotor speed** — Initial speed `0` `rpm` (default) | real number

Speed of the rotor at the start of the simulation.

### **Initial rotor angle** — Initial angle `0` `rad` (default) | real number

Angle of the rotor at the start of the simulation.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficients, [alpha\_A alpha\_B]** — Temperature coefficients `[.00393, .00393]` `1/K` (default) | positive vector

Two-element row vector defining the coefficient α in the equation
relating resistance to temperature, as described in Model Thermal Effects. The first element corresponds to winding A,
and the second to winding B. The default value is for copper.

### **Measurement temperature** — Reference temperature `25` `degC` (default) | real number

Temperature for which motor parameters are defined.

### Thermal Port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Winding thermal masses, [M\_A M\_B]** — Winding thermal masses `[100, 100]` `J/K` (default) | positive vector

Two-element row vector defining the thermal mass for the A and B
windings. The thermal mass is the energy required to raise the
temperature by one degree.

### **Winding initial temperatures, [T\_A T\_B]** — Initial winding temperatures `[25, 25]` `degC` (default) | real number

Two-element row vector defining the temperature of the A and B thermal
ports at the start of simulation.

### **Rotor thermal mass** — Rotor thermal mass `50` `J/K` (default) | positive number

Thermal mass of the rotor, that is, the energy required to raise the
temperature of the rotor by one degree.

### **Rotor initial temperature** — Initial rotor temperature `25` `degC` (default) | real number

Temperature of the rotor at the start of simulation.

### **Percentage of magnetizing resistance associated with the rotor** — Magnetizing resistance rotor percentage `90` (default) | positive number between `0` and `100`

Percentage of the magnetizing resistance associated with the magnetic
path through the rotor. It determines how much of the iron loss heating
is attributed to the rotor thermal port, **HR**, and
winding thermal ports, **HA** and
**HB**.

## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Permanent magnet stepper motor suitable for whole-, half-, and micro-stepping

The Stepper Motor block models a stepper motor. Stepper
motors have a permanent magnet rotor and two wound stator windings. If your stepper
motor has a center tap on each of the stator windings, use the Unipolar Stepper Motor block instead.

Stepper motors with small step sizes typically have north and south pole rotors with
teeth. Stepper motors with large step sizes typically have multiple magnets distributed
around the rotor circumference. You can model both types of motor using the
Stepper Motor block and drive the motor using the
Stepper Motor Driver block.

You can use stepper motors to avoid the need for a position measurement. You can use
stepper motors in devices such as printers and in applications like robotics and factory
automation.

The Stepper Motor block uses the input pulse trains,
`A` and `B`, to control the mechanical output
according to these equations,

eA=−Kmωsin(Nrθ)

eB=Kmωcos(Nrθ)

diAdt=(vA−RiA−eA)/L

diBdt=(vB−RiB−eB)/L

Jdωdt+Bω=Te

Te=−Km(iA−eARm)sin(Nrθ)+Km(iB−eBRm)cos(Nrθ)−Tdsin(4Nrθ)

dθdt=ω

where:

- *eA* and
  *eB* are the back
  electromotive forces (EMFs) induced in the *A*- and
  *B*-phase windings, respectively.
- *iA* and
  *iB* are the
  *A*- and *B*-phase winding
  currents.
- *vA* and
  *vB* are the
  *A*- and *B*-phase winding
  voltages.
- *Km* is the motor torque
  constant.
- *Nr* is the number of teeth on
  each of the two rotor poles.
- *R* is the winding resistance.
- *L* is the winding inductance.
- *Rm* is the magnetizing
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
phase winding of pulse A. This alignment happens when there is a positive current
flowing from the **A+** to the **A-** ports and there
is no current flowing from the **B+** to the **B-**
ports.

Use the Stepper Motor Driver block to create the pulse
trains for the Stepper Motor block.

The Stepper Motor block produces a positive torque that
acts from the mechanical **C** to **R** ports when the
phase of pulse `A` leads the phase of pulse
`B`.

### Averaged Mode

If you set the **Simulation mode** parameter to
`Averaged`, both for a Stepper
Motor block and for the Stepper Motor
Driver block that controls it, then the individual steps are not
simulated. This can be a good way to speed up simulation. In Averaged mode, under
nonslipping conditions, the motor and driver are represented by a second-order
linear system that tracks the specified step rate. The demanded step rate is
determined directly from voltage across **A+** and
**A-**. So, for example, a voltage of +10 V across the
**A+** and **A-** terminals is interpreted as
a step rate demand of 10 steps per second. See the Stepper Motor Driver block reference page for more information
on how to connect the driver block to your step angle controller.

Averaged mode includes a slip estimator to predict whether the stepper motor would
have slipped if running in Stepping simulation mode. Slip is predicted if the motor
torque exceeds the **Vector of maximum torque values** parameter
value for longer than one step period, the step period being determined from the
current step rate demand. Upon detecting slip, the simulation will proceed or stop
with an error, according to the **Action on slipping** parameter
value. If you choose the action that lets the simulation continue, note that
simulation results may be incorrect. When slipping occurs, the torque generated by
the motor is not generally the maximum available torque; the maximum torque is only
achieved if the stepper controller detects slip and adjusts the step rate command
accordingly.

The dynamics of the equivalent second-order system are determined from the values
that you specify for the **Approximate total load inertia** and
**Maximum step rate command** parameters. It is important that
you set as accurate values as possible for these parameters, so that the step rate
command is tracked, and the block does not generate false slipping warnings or
errors.

If you run the motor in Averaged mode with the optional thermal ports exposed (see
Model Thermal Effects), then heat is added to the thermal ports, assuming that
the windings are always powered even when the step rate command is zero. The block
makes adjustments for half stepping and for reduced torque (and winding currents) at
higher speeds. For these adjustments to be correct, the **Vector of maximum
torque** parameter values must be correct. For half stepping, at zero
speed the heat generated by the block is the average of that generated when stopped
at a half step and at a full step.

To validate Averaged mode model configurations where you predict slip to occur,
compare results with the same simulation performed in stepping mode.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses
that convert power to heat. To expose the thermal ports, set the **Modeling
option** parameter to either:

- `No thermal port` — The block does not contain thermal
  ports.
- `Show thermal port` — The block contains multiple thermal
  conserving ports.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

If you expose these ports, winding resistance is assumed
linearly dependent on temperature, and is given by:

*R* = *R0* (1 +
α (*T* – *T0*
))

where:

- *R* is the resistance at temperature
  *T*.
- *R0* is the resistance at the
  measurement (or reference) temperature
  *T0*. Specify the reference
  temperature using the **Measurement temperature**
  parameter.
- α is the resistance temperature coefficient, which you specify with the
  **Resistance temperature coefficients, [alpha\_A
  alpha\_B]** parameter. A typical value for copper is
  0.00393/K.

The block calculates temperature of each of the windings and
the rotor by

MdTdt=Q

where

- *M* is the thermal mass. Specify this value for the
  windings using the **Winding thermal masses, [M\_A
  M\_B]** parameter, and for the rotor using the
  **Rotor thermal mass** parameter.
- *T* is the temperature. Specify the initial values
  for the windings using the **Winding initial temperatures, [T\_A
  T\_B]** parameter, and for the rotor using the
  **Rotor initial temperature** parameter.
- *Q* is the heat flow, which is calculated from the
  iron losses of the windings:

  QA=ia2RA(1−ρm/100)QB=iB2RB(1−ρm/100)QR=QA(ρm/100)+QB(ρm/100)

  where *ρm* is
  the percentage of magnetizing resistance associated with the rotor.
  Specify this percentage using the **Percentage of magnetizing
  resistance associated with the rotor** parameter.

### Predefined Parameterization

There are multiple available built-in parameterizations for the Stepper Motor block.

This pre-parameterization data allows you to set up the block to represent a
specific supplier component. To load a predefined parameterization, double-click the
Stepper Motor block, click the **<click to select>**
hyperlink of the **Selected part** parameter and, in the Block
Parameterization Manager window, select the part you want to use from the list of
available components.

**Note**

The predefined parameterizations of Simscape™ components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about pre-parameterization and for a list of the available
components, see List of Pre-Parameterized Components.
