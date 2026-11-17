---
type: simulink-block
title: 'SM ST4C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst4c'
documentation_source_path: 'ref/smst4c.html'
language: en
---

# SM ST4C

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

Voltage regulator reference set point, in per-unit representation, specified as a
scalar.

**Data Types:** `single` | `double`

### **V\_S** — Input from stabilizer scalar

Input from the power system stabilizer, in per-unit representation, specified as a
scalar.

**Data Types:** `single` | `double`

### **V\_T** — Terminal voltage scalar

Terminal voltage magnitude in per-unit representation, specified as a scalar.

**Data Types:** `single` | `double`

### **I\_T** — Terminal current scalar

Terminal current magnitude in per-unit representation, specified as a scalar.

**Data Types:** `single` | `double`

### **V\_OEL** — Overexcitation limit signal scalar

Input from the overexcitation limiter, in per-unit representation, specified as a
scalar.

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

Input from the underexcitation limiter, in per-unit representation, specified as a
scalar.

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

Input from the stator current limiter when using the summation point, in per-unit
representation, specified as a scalar.

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

Input from the stator current limiter that prevents field overexcitation when using the
take-over point, in per-unit representation, specified as a
scalar.

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

Input from the stator current limiter that prevents field underexcitation when using the
take-over point, in per-unit representation, specified as a
scalar.

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

Measured per-unit field current of the synchronous machine, specified as a
scalar.

**Data Types:** `single` | `double`
### Output

### **Efd\_pu** — Field voltage scalar

Per-unit field voltage to apply to the field circuit of the synchronous machine,
returned as a scalar.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Initial field voltage, Efd0 (pu)
  summary: Initial output voltage 1 (default) | real number
  group: General
- name: Initial terminal voltage, Vt0 (pu)
  summary: Initial terminal voltage 1 (default) | real number
  group: General
- name: Initial terminal current, It0 (pu)
  summary: Initial terminal current 1 (default) | real number
  group: General
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: General
- name: Resistive component of load compensation, R_C (pu)
  summary: Compensation resistance 0 (default) | positive number
  group: Pre-Control
- name: Reactance component of load compensation, X_C (pu)
  summary: Compensation reactance 0 (default) | positive number
  group: Pre-Control
- name: Regulator input filter time constant, T_R (s)
  summary: Regulator time constant 0 (default) | positive number
  group: Pre-Control
- name: Voltage regulator proportional gain, K_PR (pu)
  summary: Regulator proportional gain 10.75 (default) | positive number
  group: Control
- name: Voltage regulator integral gain, K_IR (pu/s)
  summary: Regulator integral gain 10.75 (default) | positive number
  group: Control
- name: Thyristor bridge firing control equivalent time constant, T_A (s)
  summary: Regulator lag time constant for first lead-lag block 0.02 (default) | positive number
  group: Control
- name: Maximum regulator output, V_Rmax (pu)
  summary: Upper limit of regulator output 1 (default) | real number
  group: Control
- name: Minimum regulator output, V_Rmin (pu)
  summary: Lower limit of regulator output -0.87 (default) | real number
  group: Control
- name: Forward proportional gain of inner loop field regulator, K_PM (pu)
  summary: Inner loop forward proportional gain 1 (default) | positive number
  group: Control
- name: Forward integral gain of inner loop field regulator, K_IM (pu/s)
  summary: Inner loop forward integral gain 0 (default) | positive number
  group: Control
- name: Maximum output of field current regulator, V_Mmax (pu)
  summary: Upper limit of field current regulator output 99 (default) | real number
  group: Control
- name: Minimum output of field current regulator, V_Mmin (pu)
  summary: Lower limit of field current regulator output -99 (default) | real number
  group: Control
- name: Maximum exciter output, V_Amax (pu)
  summary: Upper limit of exciter output 99 (default) | real number
  group: Control
- name: Minimum exciter output, V_Amin (pu)
  summary: Lower limit of exciter output -99 (default) | real number
  group: Control
- name: Feedback gain of field current regulator, K_G (pu)
  summary: Feedback gain of field current regulator 0 (default) | positive number
  group: Control
- name: Feedback time constant of field current regulator, T_G (s)
  summary: Feedback time constant of field current regulator 0 (default) | positive number
  group: Control
- name: Maximum feedback voltage for field current regulator, V_Gmax (pu)
  summary: Maximum feedback voltage for field current regulator 99 (default) | positive number
  group: Control
- name: Alternate PSS input locations (V_S)
  summary: PSS input location Summation point before take-over UEL (default) | Summation point after take-over UEL
  group: Control
- name: Alternate OEL input locations (V_OEL)
  summary: OEL input location Unused (default) | Summation point at voltage error | Take-over at voltage regulator input |
    Take-over at inner-loop output
  group: Control
- name: Alternate UEL input locations (V_UEL)
  summary: UEL input location Unused (default) | Summation point at voltage error | Take-over at voltage regulator input |
    Take-over at inner-loop output
  group: Control
- name: Alternate SCL input locations (V_SCL)
  summary: SCL input location Unused (default) | Summation point at voltage error | Take-over at voltage regulator input |
    Take-over at inner-loop output
  group: Control
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: Rectifier loading factor 0.113 (default) | positive number
  group: Exciter
- name: Potential circuit (voltage) gain coefficient, K_P (pu)
  summary: Potential circuit voltage gain coefficient 9.3 (default) | positive number
  group: Exciter
- name: Compound circuit (current) gain coefficient, K_I (pu)
  summary: Potential circuit current gain coefficient 0 (default) | positive number
  group: Exciter
- name: Reactance associated with potential source, X_L (pu)
  summary: Potential source reactance 0.124 (default) | positive number
  group: Exciter
- name: Potential circuit phase angle (degrees)
  summary: Potential circuit phase angle 0 (default) | positive number
  group: Exciter
- name: Maximum available exciter voltage, V_Bmax (pu)
  summary: Exciter voltage upper limit 11.63 (default) | positive number
  group: Exciter
- name: Power source selector
  summary: 'Power source selector Position A: power source derived from generator terminal voltage (default) | Position B:
    power source independent of generator terminal conditions'
  group: Exciter
```

### General

### **Initial field voltage, Efd0 (pu)** — Initial output voltage `1` (default) | real number

Initial per-unit voltage to apply to the field circuit of the
synchronous machine.

### **Initial terminal voltage, Vt0 (pu)** — Initial terminal voltage `1` (default) | real number

Initial per-unit terminal voltage.

### **Initial terminal current, It0 (pu)** — Initial terminal current `1` (default) | real number

Initial per-unit terminal current.

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

### **Resistive component of load compensation, R\_C (pu)** — Compensation resistance `0` (default) | positive number

Resistance used in the current compensation system. Set this parameter
and **Reactance component of load compensation, X\_C
(pu)** to `0` to disable current
compensation.

### **Reactance component of load compensation, X\_C (pu)** — Compensation reactance `0` (default) | positive number

Reactance used in the current compensation system. Set this parameter
and **Resistive component of load compensation, R\_C
(pu)** to `0` to disable current
compensation.

### **Regulator input filter time constant, T\_R (s)** — Regulator time constant `0` (default) | positive number

Equivalent time constant for the voltage transducer filtering.

### Control

### **Voltage regulator proportional gain, K\_PR (pu)** — Regulator proportional gain `10.75` (default) | positive number

Proportional gain associated with the voltage regulator PI control
block.

### **Voltage regulator integral gain, K\_IR (pu/s)** — Regulator integral gain `10.75` (default) | positive number

Integral gain associated with the voltage regulator PI control
block.

### **Thyristor bridge firing control equivalent time constant, T\_A (s)** — Regulator lag time constant for first lead-lag block `0.02` (default) | positive number

Equivalent time constant in the thyristor bridge firing control.

### **Maximum regulator output, V\_Rmax (pu)** — Upper limit of regulator output `1` (default) | real number

Maximum per-unit output voltage of the regulator.

### **Minimum regulator output, V\_Rmin (pu)** — Lower limit of regulator output `-0.87` (default) | real number

Minimum per-unit output voltage of the regulator.

### **Forward proportional gain of inner loop field regulator, K\_PM (pu)** — Inner loop forward proportional gain `1` (default) | positive number

Per-unit forward proportional gain of the PI control block in the
inner loop field regulator.

### **Forward integral gain of inner loop field regulator, K\_IM (pu/s)** — Inner loop forward integral gain `0` (default) | positive number

Forward integral gain of the PI control block in the inner loop field
regulator.

### **Maximum output of field current regulator, V\_Mmax (pu)** — Upper limit of field current regulator output `99` (default) | real number

Maximum per-unit output voltage of the field current regulator.

### **Minimum output of field current regulator, V\_Mmin (pu)** — Lower limit of field current regulator output `-99` (default) | real number

Minimum per-unit output voltage of the field current regulator.

### **Maximum exciter output, V\_Amax (pu)** — Upper limit of exciter output `99` (default) | real number

Maximum per-unit output voltage of the exciter.

### **Minimum exciter output, V\_Amin (pu)** — Lower limit of exciter output `-99` (default) | real number

Minimum per-unit output voltage of the exciter.

### **Feedback gain of field current regulator, K\_G (pu)** — Feedback gain of field current regulator `0` (default) | positive number

Per-unit feedback gain of the field current regulator.

### **Feedback time constant of field current regulator, T\_G (s)** — Feedback time constant of field current regulator `0` (default) | positive number

Per-unit feedback time constant of the field current regulator.

### **Maximum feedback voltage for field current regulator, V\_Gmax (pu)** — Maximum feedback voltage for field current regulator `99` (default) | positive number

Maximum per-unit feedback voltage for the field current regulator.

### **Alternate PSS input locations (V\_S)** — PSS input location `Summation point before take-over UEL` (default) | `Summation point after take-over UEL`

Power system stabilizer input.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point at voltage error` | `Take-over at voltage regulator input` | `Take-over at inner-loop output`

Overexcitation limiter input location:

- If you select `Summation point at voltage
  error`, **V\_OEL** is an
  input of the Summation Point Logic subsystem.
- If you select `Take-over at voltage regulator
  input`, **V\_OEL** is an
  input of the Take-over Logic subsystem.
- If you select `Take-over at inner-loop
  output`, **V\_OEL** is an
  input of the Take-over Logic 1 subsystem.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point at voltage error` | `Take-over at voltage regulator input` | `Take-over at inner-loop output`

Underexcitation limiter input location:

- If you select `Summation point at voltage
  error`, **V\_UEL** is an
  input of the Summation Point Logic subsystem.
- If you select `Take-over at voltage regulator
  input`, **V\_UEL** is an
  input of the Take-over Logic subsystem.
- If you select `Take-over at inner-loop
  output`, **V\_UEL** is an
  input of the Take-over Logic 1 subsystem.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point at voltage error` | `Take-over at voltage regulator input` | `Take-over at inner-loop output`

Stator current limiter input location:

- If you select `Summation point`,
  use the **V\_SCLsum** input port.
- If you select any of the
  `Take-over` options, use the
  **V\_SCLoel** and
  **V\_SCLuel** input ports.

### Exciter

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.113` (default) | positive number

Rectifier loading factor proportional to the commutating reactance.

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — Potential circuit voltage gain coefficient `9.3` (default) | positive number

Per-unit voltage gain coefficient in the power source circuit.

#### Dependencies

To enable this parameter, set **Power source selector** to
`Position A: power source derived from generator
terminal voltage`.

### **Compound circuit (current) gain coefficient, K\_I (pu)** — Potential circuit current gain coefficient `0` (default) | positive number

Per-unit current gain coefficient in the power source circuit.

#### Dependencies

To enable this parameter, set **Power source selector** to
`Position A: power source derived from generator
terminal voltage`.

### **Reactance associated with potential source, X\_L (pu)** — Potential source reactance `0.124` (default) | positive number

Per-unit reactance in the power source circuit.

#### Dependencies

To enable this parameter, set **Power source selector** to
`Position A: power source derived from generator
terminal voltage`.

### **Potential circuit phase angle (degrees)** — Potential circuit phase angle `0` (default) | positive number

Phase angle of the power source circuit, in degrees.

#### Dependencies

To enable this parameter, set **Power source selector** to
`Position A: power source derived from generator
terminal voltage`.

### **Maximum available exciter voltage, V\_Bmax (pu)** — Exciter voltage upper limit `11.63` (default) | positive number

Maximum per-unit available exciter voltage value.

### **Power source selector** — Power source selector `Position A: power source derived from generator terminal voltage` (default) | `Position B: power source independent of generator terminal conditions`

Position of the power source selector, specified as `Position A: power
source derived from generator terminal voltage` or
`Position B: power source independent of generator
terminal conditions`.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time synchronous machine ST4C static excitation system with an automatic voltage regulator

The SM ST4C block implements a synchronous-machine-type ST4C static
excitation system model in conformance with IEEE 421.5-2016[1].

Use this block to model the control and regulation of the field voltage of a
synchronous machine.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

The SM ST4C block comprises of four major components:

- The Current Compensator modifies the measured terminal voltage as a
  function of the terminal current.
- The Voltage Measurement Transducer simulates the dynamics of a terminal
  voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error. This
  voltage error is then passed through a voltage regulator to produce the
  field voltage.
- The Power Source component models the power source for the controlled
  rectifier when it is independent from the terminal voltage.

This diagram shows the overall structure of the ST4C excitation system
model:

In the diagram:

- *VT* and
  *IT* are the measured
  terminal voltage and current of the synchronous machine.
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

The following sections describe each of the major parts of the block in detail.

### Current Compensator and Voltage Measurement Transducer

The current compensator is modeled as:

VC1=VT+ITRC2+XC2,

where:

- *RC* is the load compensation
  resistance.
- *XC* is the load compensation
  reactance.

The voltage measurement transducer is implemented as a Low-Pass
Filter block with the time constant
*TR*. Refer to the documentation for the
Low-Pass Filter block for the exact discrete and continuous implementations.

### Excitation Control Elements

This diagram illustrates the overall structure of the excitation control elements:

In the diagram:

- The Summation Point Logic subsystem models the summation point input
  location for the overexcitation limiter (OEL), underexcitation limiter
  (UEL), stator current limiter (SCL), and the power switch selector (V\_S)
  voltages. For more information about using limiters with this block, see
  Field Current Limiters.
- There are two Take-over Logic subsystems. The subsystems model the
  take-over point input location for the OEL, UEL, SCL and PSS voltages.
  For more information about using limiters with this block, see Field Current Limiters.
- The PI\_R subsystem models a PI controller that functions as a control
  structure for the automatic voltage regulator and allows the
  representation of an equipment retrofit with a modern digital
  controller. The minimum and maximum anti-windup saturation limits for
  the block are *VPImin* and
  *VPImax*,
  respectively.
- The PI\_M subsystem models a PI controller and replaces the Lead-Lag block in SM
  ST3C. The minimum and maximum anti-windup saturation limits
  for the block are *VMmin* and
  *VMmax*,
  respectively.
- An inner field voltage control loop is utilized to linearize the
  exciter control characteristic and it is composed of the gains
  *KM* and
  *KG* and the time
  constants *TM* and
  *TG*. The minimum and
  maximum anti-windup saturation limits for the Low-Pass Filter block are
  *VAmin* and
  *VAmax*,
  respectively.

### Field Current Limiters

You can use various field current limiters to modify the output of the voltage
regulator under unsafe operating conditions:

- Use an overexcitation limiter to prevent overheating of the field
  winding due to excessive field current demand.
- Use an underexcitation limiter to boost field excitation when it is
  too low, which risks desynchronization.
- Use a stator current limiter to prevent overheating of the stator
  windings due to excessive current.

Attach the output of any of these limiters at one of these points:

- The summation point as part of the automatic voltage regulator (AVR)
  feedback loop
- The take-over point to override the usual behavior of the AVR

If you are using the stator current limiter at the summation point,
use the single input *VSCLsum*. If you are
using the stator current limiter at the take-over point, use both the overexcitation
input, *VSCLoel*, and the underexcitation
input, *VSCLuel*.

### Power Source

It is possible to adopt a different representation of the power source for the controlled
rectifier by selecting the relevant option in the **Power source
selector** parameter. The power source for the controlled rectifier can
be either derived from the terminal voltage (`Position A: power source
derived from generator terminal voltage`) or it can be independent
of the terminal voltage (`Position B: power source independent of
generator terminal conditions`).

This diagram shows a model of the exciter power source utilizing a phasor
combination of the terminal voltage, *VT*,
and terminal current, *IT*:
