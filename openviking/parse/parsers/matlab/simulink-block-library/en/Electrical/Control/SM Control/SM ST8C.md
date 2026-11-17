---
type: simulink-block
title: 'SM ST8C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst8c'
documentation_source_path: 'ref/smst8c.html'
language: en
---

# SM ST8C

## Ports
```yaml
ports:
- name: V_REF
  summary: Voltage reference scalar
  direction: input
  data_types: single | double
- name: V_S
  summary: Input from stabilizer scalar
  direction: input
  data_types: single | double
- name: V_T
  summary: Terminal voltage scalar
  direction: input
  data_types: single | double
- name: I_T
  summary: Terminal current scalar
  direction: input
  data_types: single | double
- name: V_OEL
  summary: Overexcitation limit signal scalar
  direction: input
  data_types: single | double
- name: V_UEL
  summary: Underexcitation limit signal scalar
  direction: input
  data_types: single | double
- name: V_SCLsum
  summary: Summation point stator current limit signal scalar
  direction: input
  data_types: single | double
- name: V_SCLoel
  summary: Take-over stator current limit (OEL) scalar
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: Take-over stator current limit (UEL) scalar
  direction: input
  data_types: single | double
- name: Ifd_pu
  summary: Measured field current scalar
  direction: input
  data_types: single | double
- name: Efd_pu
  summary: Field voltage scalar
  direction: output
  data_types: single | double
```

### Input

### **V\_REF** — Voltage reference scalar

Voltage regulator reference set point, in per-unit representation,
specified as a scalar.

**Data Types:** `single` | `double`

### **V\_S** — Input from stabilizer scalar

Input from the power system stabilizer, in per-unit representation,
specified as a scalar.

**Data Types:** `single` | `double`

### **V\_T** — Terminal voltage scalar

Terminal voltage magnitude, in per-unit representation, specified as a scalar.

**Data Types:** `single` | `double`

### **I\_T** — Terminal current scalar

Terminal current magnitude, in per-unit representation, specified as a scalar.

**Data Types:** `single` | `double`

### **V\_OEL** — Overexcitation limit signal scalar

Input from the overexcitation limiter, in per-unit representation,
specified as a scalar.

#### Dependencies

- To ignore the input from the overexcitation limiter,
  set **Alternate OEL input locations
  (V\_OEL)** to
  `Unused`.
- To use the input from the overexcitation limiter at
  the summation point, set **Alternate OEL input
  locations (V\_OEL)** to
  `Summation point`.
- To use the input from the overexcitation limiter at
  the take-over point, set **Alternate OEL input
  locations (V\_OEL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **V\_UEL** — Underexcitation limit signal scalar

Input from the underexcitation limiter, in per-unit representation,
specified as a scalar.

#### Dependencies

- To ignore the input from the underexcitation limiter,
  set **Alternate UEL input locations
  (V\_UEL)** to
  `Unused`.
- To use the input from the underexcitation limiter at
  the summation point, set **Alternate UEL input
  locations (V\_UEL)** to
  `Summation point`.
- To use the input from the underexcitation limiter at
  the take-over point, set **Alternate UEL input
  locations (V\_UEL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **V\_SCLsum** — Summation point stator current limit signal scalar

Input from the stator current limiter when using the summation point,
in per-unit representation, specified as a scalar.

#### Dependencies

- To ignore the input from the stator current limiter,
  set **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at
  the summation point, set **Alternate SCL input
  locations (V\_SCL)** to
  `Summation point`.

**Data Types:** `single` | `double`

### **V\_SCLoel** — Take-over stator current limit (OEL) scalar

Input from the stator current limiter that prevents field
overexcitation when using the take-over point, in per-unit
representation, specified as a scalar.

#### Dependencies

- To ignore the input from the stator current limiter,
  set **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at
  the take-over point, set **Alternate SCL input
  locations (V\_SCL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **V\_SCLuel** — Take-over stator current limit (UEL) scalar

Input from the stator current limiter that prevents field
underexcitation when using the take-over point, in per-unit
representation, specified as a scalar.

#### Dependencies

- To ignore the input from the stator current limiter,
  set **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at
  the take-over point, set **Alternate SCL input
  locations (V\_SCL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **Ifd\_pu** — Measured field current scalar

Measured per-unit field current of the synchronous machine, specified
as a scalar.

**Data Types:** `single` | `double`
### Output

### **Efd\_pu** — Field voltage scalar

Per-unit field voltage to apply to the field circuit of the
synchronous machine, returned as a scalar.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: Initial output voltage 1 (default) | real scalar
  group: General
- name: Initial terminal voltage, Vt0 (pu)
  summary: Initial terminal voltage 1 (default) | real scalar
  group: General
- name: Initial terminal current, It0 (pu)
  summary: Initial terminal current 1 (default) | real scalar
  group: General
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: General
- name: Resistive component of load compensation, R_C (pu)
  summary: Compensation resistance 0 (default) | positive scalar
  group: Pre-Control
- name: Reactance component of load compensation, X_C (pu)
  summary: Compensation reactance 0 (default) | positive scalar
  group: Pre-Control
- name: Regulator input filter time constant, T_R (s)
  summary: Regulator time constant 0.0226 (default) | positive scalar
  group: Pre-Control
- name: Voltage regulator proportional gain, K_PR (pu)
  summary: Proportional gain of the voltage regulator 6.6 (default)
  group: Control
- name: Voltage regulator integral gain, K_IR (pu/s)
  summary: Integral gain of the voltage regulator 30 (default)
  group: Control
- name: Maximum voltage regulator output, V_PImax (pu)
  summary: Maximum output of PI regulator 16 (default) | positive scalar
  group: Control
- name: Minimum voltage regulator output, V_PImin (pu)
  summary: Minimum output of PI regulator -16 (default) | positive scalar
  group: Control
- name: Field current regulator proportional gain, K_PA (pu)
  summary: Proportional gain of the field current regulator 2.38 (default)
  group: Control
- name: Field current regulator integral gain, K_IA (pu/s)
  summary: Integral gain of field current regulator 0 (default)
  group: Control
- name: Maximum exciter output, V_Amax (pu)
  summary: Upper limit of exciter output 1 (default) | real scalar
  group: Control
- name: Minimum exciter output, V_Amin (pu)
  summary: Lower limit of exciter output -1 (default) | real scalar
  group: Control
- name: Controlled rectifier bridge equivalent gain, K_A (pu)
  summary: Rectifier bridge gain 4.295 (default) | positive scalar
  group: Control
- name: Controlled rectifier bridge equivalent time constant, T_A (s)
  summary: Rectifier bridge time constant 0.0017 (default) | positive scalar
  group: Control
- name: Maximum field current regulator output, V_Rmax (pu)
  summary: Maximum output of field current regulator 4.27 (default) | positive scalar
  group: Control
- name: Minimum field current regulator output, V_Amin (pu)
  summary: Minimum output of field current regulator -3.64 (default) | positive scalar
  group: Control
- name: Exciter field current feedback gain, K_F (pu)
  summary: Exciter field current feedback gain 1 (default) | real scalar
  group: Control
- name: Field current feedback time constant, T_F (s)
  summary: Feedback time constant 0.0226 (default) | positive scalar
  group: Control
- name: Alternate OEL input locations (V_OEL)
  summary: OEL input location Unused (default) | Summation point | Take-over
  group: Control
- name: Alternate UEL input locations (V_UEL)
  summary: UEL input location Unused (default) | Summation point | Take-over
  group: Control
- name: Alternate SCL input locations (V_SCL)
  summary: SCL input location Unused (default) | Summation point | Take-over
  group: Control
- name: Rectifier loading factor proportional to commutating reactance, K_C1 (pu)
  summary: Rectifier loading factor 0.062 (default) | positive scalar
  group: Exciter
- name: Potential circuit (voltage) gain coefficient, K_P (pu)
  summary: Potential circuit gain coefficient 1 (default) | real scalar
  group: Exciter
- name: Compound circuit (current) gain coefficient, K_I (pu)
  summary: Potential circuit current gain coefficient 0 (default) | real scalar
  group: Exciter
- name: Reactance associated with potential source, X_L (pu)
  summary: Reactance associated with potential source 0 (default) | real scalar
  group: Exciter
- name: Potential circuit phase angle (degrees)
  summary: Potential circuit phase angle 0 (default) | real scalar
  group: Exciter
- name: Maximum available exciter voltage, V_B1max (pu)
  summary: Maximum available exciter field voltage 2 (default) | real scalar
  group: Exciter
- name: Rectifier loading factor proportional to commutating reactance, K_C2 (pu)
  summary: Rectifier loading factor proportional to commutating reactance 0 (default) | real scalar
  group: Exciter
- name: Compound circuit (current) gain coefficient, K_I2 (pu)
  summary: Compound circuit current gain coefficient 0 (default) | real scalar
  group: Exciter
- name: Maximum available exciter field voltage, V_B2max (pu)
  summary: Maximum available exciter field voltage 0 (default) | real scalar
  group: Exciter
- name: Power source selector
  summary: 'Power source selector Position A: power source derived from generator terminal voltage (default) | Position B:
    power source independent of generator terminal conditions'
  group: Exciter
```

### General

### **Initial field voltage, Efd0 (pu)** — Initial output voltage `1` (default) | real scalar

Initial per-unit voltage to apply to the field circuit of the
synchronous machine.

### **Initial terminal voltage, Vt0 (pu)** — Initial terminal voltage `1` (default) | real scalar

Initial per-unit voltage to apply to the terminal.

#### Dependencies

To enable this parameter, in the Exciter section, set
**Power source selector** to
`Position A: power source derived from generator
terminal voltage`.

### **Initial terminal current, It0 (pu)** — Initial terminal current `1` (default) | real scalar

Initial per-unit current to apply to the terminal.

#### Dependencies

To enable this parameter, in the Exciter section, set
**Power source selector** to
`Position A: power source derived from generator
terminal voltage`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

### Pre-Control

### **Resistive component of load compensation, R\_C (pu)** — Compensation resistance `0` (default) | positive scalar

Resistance used in the current compensation system. Set this parameter
and **Reactance component of load compensation, X\_C
(pu)** to `0` to disable current
compensation.

### **Reactance component of load compensation, X\_C (pu)** — Compensation reactance `0` (default) | positive scalar

Reactance used in the current compensation system. Set this parameter
and **Resistive component of load compensation, R\_C
(pu)** to `0` to disable current
compensation.

### **Regulator input filter time constant, T\_R (s)** — Regulator time constant `0.0226` (default) | positive scalar

Equivalent time constant for the voltage transducer filtering.

### Control

### **Voltage regulator proportional gain, K\_PR (pu)** — Proportional gain of the voltage regulator `6.6` (default)

Per-unit proportional gain of the voltage regulator.

### **Voltage regulator integral gain, K\_IR (pu/s)** — Integral gain of the voltage regulator `30` (default)

Per-unit integral gain of the voltage regulator.

### **Maximum voltage regulator output, V\_PImax (pu)** — Maximum output of PI regulator `16` (default) | positive scalar

Maximum admissible per-unit output of the PI regulator.

### **Minimum voltage regulator output, V\_PImin (pu)** — Minimum output of PI regulator `-16` (default) | positive scalar

Minimum admissible per-unit output of the PI regulator.

### **Field current regulator proportional gain, K\_PA (pu)** — Proportional gain of the field current regulator `2.38` (default)

Per-unit proportional gain of the field current regulator.

### **Field current regulator integral gain, K\_IA (pu/s)** — Integral gain of field current regulator `0` (default)

Per-unit integral gain of the field current regulator.

### **Maximum exciter output, V\_Amax (pu)** — Upper limit of exciter output `1` (default) | real scalar

Maximum per-unit output voltage of the exciter.

### **Minimum exciter output, V\_Amin (pu)** — Lower limit of exciter output `-1` (default) | real scalar

Minimum per-unit output voltage of the exciter.

### **Controlled rectifier bridge equivalent gain, K\_A (pu)** — Rectifier bridge gain `4.295` (default) | positive scalar

Gain of the controlled rectifier bridge.

### **Controlled rectifier bridge equivalent time constant, T\_A (s)** — Rectifier bridge time constant `0.0017` (default) | positive scalar

Time constant of the controlled rectifier bridge.

### **Maximum field current regulator output, V\_Rmax (pu)** — Maximum output of field current regulator `4.27` (default) | positive scalar

Maximum admissible per-unit output of the field current
regulator.

### **Minimum field current regulator output, V\_Amin (pu)** — Minimum output of field current regulator `-3.64` (default) | positive scalar

Minimum admissible per-unit output of the field current
regulator.

### **Exciter field current feedback gain, K\_F (pu)** — Exciter field current feedback gain `1` (default) | real scalar

Per-unit field current feedback gain of the exciter.

### **Field current feedback time constant, T\_F (s)** — Feedback time constant `0.0226` (default) | positive scalar

Feedback time constant for the stabilization of the excitation
system.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the overexcitation limiter input, specified as one of these options:

- `Summation point` —
  **V\_OEL** is an input of the Summation
  Point Logic subsystem.
- `Take-over` —
  **V\_OEL** is an input of the Take-over
  Logic subsystem.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the underexcitation limiter input, specified as one of these options:

- `Summation point` —
  **V\_UEL** is an input of the Summation
  Point Logic subsystem.
- `Take-over` —
  **V\_UEL** is an input of the Take-over
  Logic subsystem.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the stator current limiter input, specified as one of these options:

- `Summation point` — Use the
  **V\_SCLsum** input port.
- `Take-over` — Use the
  **V\_SCLoel** and
  **V\_SCLuel** input ports.

### Exciter

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — Rectifier loading factor `0.062` (default) | positive scalar

Per-unit rectifier loading factor. This value is proportional to the commutating
reactance.

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — Potential circuit gain coefficient `1` (default) | real scalar

Per-unit potential circuit gain coefficient.

### **Compound circuit (current) gain coefficient, K\_I (pu)** — Potential circuit current gain coefficient `0` (default) | real scalar

Per-unit potential circuit current gain coefficient.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from generator terminal voltage`.

### **Reactance associated with potential source, X\_L (pu)** — Reactance associated with potential source `0` (default) | real scalar

Per-unit reactance associated with the potential source.

#### Dependencies

To enable this parameter, set **Power source
selector** to `Position A: power source
derived from generator terminal voltage`.

### **Potential circuit phase angle (degrees)** — Potential circuit phase angle `0` (default) | real scalar

Potential circuit phase angle, in degrees.

#### Dependencies

To enable this parameter, set **Power source
selector** to `Position A: power source
derived from generator terminal voltage`.

### **Maximum available exciter voltage, V\_B1max (pu)** — Maximum available exciter field voltage `2` (default) | real scalar

Maximum per-unit available field voltage for the exciter.

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — Rectifier loading factor proportional to commutating reactance `0` (default) | real scalar

Per-unit loading factor of the rectifier. This value is proportional to the commutating
reactance, derived from the generator terminal current through a
separate series diode bridge.

### **Compound circuit (current) gain coefficient, K\_I2 (pu)** — Compound circuit current gain coefficient `0` (default) | real scalar

Per-unit compound circuit current gain coefficient derived from the generator terminal
current through a separate series diode bridge. Set this parameter to
`0` to disable the separate compound power source
completely.

### **Maximum available exciter field voltage, V\_B2max (pu)** — Maximum available exciter field voltage `0` (default) | real scalar

Maximum per-unit available field voltage for the exciter, derived from the generator
terminal current through a separate series diode bridge.

### **Power source selector** — Power source selector `Position A: power source derived from generator terminal voltage` (default) | `Position B: power source independent of generator terminal conditions`

Position of the power source selector.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Discrete-time or continuous-time synchronous machine ST8C static excitation system with automatic voltage regulator

The SM ST8C block implements a synchronous-machine-type ST8C static
excitation system model in conformance with IEEE Std 421.5-2016 [1].

Use this block to model the control and regulation of the field voltage of a
synchronous machine.

Switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** parameter
to a positive scalar. To inherit the sample time from an upstream block, set the
**Sample time (-1 for inherited)** parameter to
`-1`.

The SM ST8C block comprises four major components:

- The Current Compensator component modifies the measured terminal voltage
  as a function of the terminal current.
- The Voltage Measurement Transducer component simulates the dynamics of a
  terminal voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error value.
  The component then passes this value through a voltage regulator to produce
  the field voltage.
- The Power Source component models the power source for the controlled
  rectifier when it is independent from the terminal voltage.

This diagram shows the structure of the ST8C excitation system
model:

In the diagram:

- *VT* and
  *IT* are the measured
  terminal voltage and current of the synchronous machine,
  respectively.
- *VC1* is the current-compensated
  terminal voltage.
- *VC* is the filtered,
  current-compensated terminal voltage.
- *VREF* is the reference terminal
  voltage.
- *VS* is the power system
  stabilizer voltage.
- *VB* is the exciter field
  voltage.
- *EFD* and
  *IFD* are the field voltage
  and current, respectively.

### Current Compensator and Voltage Measurement Transducer

The block models the current compensator by using this equation:

VC1=VT+ITRC2+XC2,

where:

- *RC* is the load compensation
  resistance.
- *XC* is the load compensation
  reactance.

The block implements the voltage measurement transducer as a Low-Pass
Filter block with the time constant
*TR*. Refer to the documentation for the
Low-Pass Filter block for information about the exact discrete and continuous
implementations.

### Excitation Control Elements

This diagram shows the structure of the excitation control elements:

In the diagram:

- The Summation Point Logic subsystem models the summation point input
  location for the overexcitation limiter (OEL), underexcitation limiter
  (UEL) and stator current limiter (SCL) voltages. For more information
  about using limiters with this block, see Field Current Limiters.
- The Take-over Logic subsystem models the take-over point input
  location for the OEL, UEL, and SCL voltages. For more information about
  using limiters with this block, see Field Current Limiters.
- The PI subsystem models a PI controller that functions as a control
  structure for the automatic voltage regulator and allows the
  representation of an equipment retrofit with a modern digital
  controller. The minimum and maximum anti windup saturation limits for
  the block are *VPImin* and
  *VPImax*, respectively.
  A current PI regulator follows the voltage PI regulator in
  cascade.
- The PI1 subsystem models a PI controller that functions as a control
  structure for the field current regulator. The minimum and maximum anti
  windup saturation limits for the block are
  *VAmin* and
  *VAmax*,
  respectively.
- The top Low-Pass Filter block models the major dynamics of the
  controlled rectified bridge.
  *KA* is the controlled
  rectifier bridge equivalent gain and
  *TA* is the major time
  constant of the controlled rectifier bridge. The minimum and maximum
  anti windup saturation limits for the block are
  *VRmin* and
  *VRmax*,
  respectively.
- The **Power source selector** parameter controls the
  origin of the power source for the controlled rectifier. The
  contribution factor is summed and/or multiplied to the power stage
  output. The summation component
  *VB2* corresponds to a
  compound power source derived from generator terminal current. If you
  set the **Potential circuit (current) gain coefficient, K\_I2
  (pu)** and **Rectifier loading factor proportional
  to commutating reactance, K\_C2 (pu)** parameters to
  `0`, this summation component is disabled. For more
  information about the logical switch for the power source of the
  controlled rectifier, see Power Source.

### Field Current Limiters

You can use different types of field current limiter to modify the output of the voltage
regulator under unsafe operating conditions:

- Use an overexcitation limiter to prevent overheating of the field
  winding due to excessive field current demand.
- Use an underexcitation limiter to boost field excitation when it is
  too low, which risks desynchronization.
- Use a stator current limiter to prevent overheating of the stator
  windings due to excessive current.

Attach the output of any of these limiters at one of these points:

- Summation point — Use the limiter as part of the automatic voltage
  regulator (AVR) feedback loop.
- Take-over point — Override the usual behavior of the AVR.

If you are using the stator current limiter at the summation point,
use the input *VSCLsum*. If you are using
the stator current limiter at the take-over point, use the overexcitation input
*VSCLoel*, and the underexcitation
input *VSCLuel*.

### Power Source

You can use different power source representations for the controlled rectifier by
setting the **Power source selector** parameter value. To derive
the power source for the controlled rectifier from the terminal voltage, set the
**Power source selector** parameter to `Position A:
power source derived from generator terminal voltage`. To specify
that the power source is independent of the terminal voltage, set the
**Power source selector** parameter to `Position B:
power source independent of generator terminal conditions`.

This diagram shows a model of the exciter power source utilizing a phasor combination of
the terminal voltage *VT* and terminal
current *IT*:

The summation component *VB2* corresponds
to a compound power source derived from generator terminal current. If you set the
**Potential circuit (current) gain coefficient, K\_I2 (pu)** and
**Rectifier loading factor proportional to commutating reactance, K\_C2
(pu)** parameters to `0`, this summation component is
disabled.
