---
type: simulink-block
title: 'SM ST3C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — ST Type'
documentation_page: 'smst3c'
documentation_source_path: 'ref/smst3c.html'
language: en
---

# SM ST3C

## Ports

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

### **Voltage regulator gain, K\_A (pu)** — Regulator gain `200` (default) | positive number

Gain associated with the voltage regulator.

### **Regulator denominator (lag) time constant, T\_B (s)** — Regulator lag time constant for first lead-lag block `10` (default) | positive number

Equivalent lag time constant in the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Regulator numerator (lead) time constant, T\_C (s)** — Regulator lead time constant for first lead-lag block `1` (default) | positive number

Equivalent lead time constant in the voltage regulator. Set this parameter to
`0` when the additional lead dynamics are
negligible.

### **Voltage regulator proportional gain, K\_PR (pu)** — Regulator proportional gain `1` (default) | positive number

Proportional gain associated with the voltage regulator PI control
block.

### **Voltage regulator integral gain, K\_IR (pu/s)** — Regulator integral gain `0` (default) | positive number

Integral gain associated with the voltage regulator PI control
block.

### **Maximum voltage regulator output, V\_PImax (pu)** — Upper limit of regulator output for PI control `99` (default) | real number

Maximum per-unit output voltage of the regulator PI control
block.

### **Minimum voltage regulator output, V\_PImin (pu)** — Lower limit of regulator output for PI control `-99` (default) | real number

Minimum per-unit output voltage of the regulator PI control
block.

### **Maximum regulator output, V\_Rmax (pu)** — Upper limit of regulator output `10` (default) | real number

Maximum per-unit output voltage of the regulator.

### **Minimum regulator output, V\_Rmin (pu)** — Lower limit of regulator output `-10` (default) | real number

Minimum per-unit output voltage of the regulator.

### **Maximum voltage error (regulator input), V\_Imax (pu)** — Voltage upper limit `0.2` (default) | real number

Maximum per-unit voltage given as input to the regulator.

### **Minimum voltage error (regulator input), V\_Imax (pu)** — Voltage lower limit `-0.2` (default) | real number

Minimum per-unit voltage given as input to the regulator.

### **Forward gain of inner loop field regulator, K\_M (pu)** — Inner loop forward gain `7.93` (default) | positive number

Per-unit forward gain in the inner loop field regulator.

### **Forward time constant of inner loop field regulator, T\_M (s)** — Inner loop forward time constant `0.4` (default) | positive number

Forward time constant in the inner loop field regulator, in
seconds.

### **Maximum output of field current regulator, V\_Mmax (pu)** — Upper limit of field current regulator output `1` (default) | real number

Maximum per-unit output voltage of the field current regulator.

### **Minimum regulator output, V\_Mmin (pu)** — Lower limit of field current regulator output `0` (default) | real number

Minimum per-unit output voltage of the field current regulator.

### **Feedback gain of field current regulator, K\_G (pu)** — Feedback gain of field current regulator `1` (default) | positive number

Per-unit feedback gain in the field current regulator.

### **Maximum feedback voltage for field current regulator, V\_Gmax (pu)** — Maximum feedback voltage for field current regulator `5.8` (default) | positive number

Maximum per-unit feedback voltage for the field current regulator.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point` | `Take-over`

Overexcitation limiter input location.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point` | `Take-over`

Underexcitation limiter input location.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point` | `Take-over`

Stator current limiter input location:

- If you select `Summation point`,
  use the **V\_SCLsum** input port.
- If you select `Take-over`, use
  the **V\_SCLoel** and
  **V\_SCLuel** input ports.

### Exciter

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.2` (default) | positive number

Rectifier loading factor proportional to the commutating reactance.

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — Potential circuit voltage gain coefficient `6.15` (default) | positive number

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

### **Reactance associated with potential source, X\_L (pu)** — Potential source reactance `0.081` (default) | positive number

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

### **Maximum available exciter voltage, V\_Bmax (pu)** — Upper limit of exciter voltage `6.9` (default) | positive number

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

Discrete-time or continuous-time synchronous machine ST3C static excitation system with an automatic voltage regulator

The SM ST3C block implements a synchronous-machine-type ST3C static
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

The SM ST3C block comprises four major components:

- The Current Compensator modifies the measured terminal voltage as a
  function of the terminal current.
- The Voltage Measurement Transducer simulates the dynamics of a terminal
  voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error. This
  voltage error is then passed through a voltage regulator to produce the
  field voltage.
- The Power Source models the power source for the controlled rectifier when
  it is independent from the terminal voltage.

This diagram shows the overall structure of the ST3C excitation system
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
Low-Pass Filter block for the discrete and continuous implementations.

### Excitation Control Elements

This diagram illustrates the overall structure of the excitation control elements:

In the diagram:

- The Summation Point Logic subsystem models the summation point input
  location for the overexcitation limiter (OEL), underexcitation limiter
  (UEL), stator current limiter (SCL), and the power switch selector (V\_S)
  voltages. For more information about using limiters with this block, see
  Field Current Limiters.
- The Take-over Logic subsystem models the take-over point input
  location for the OEL, UEL, and SCL voltages. For more information about
  using limiters with this block, see Field Current Limiters.
- The PI subsystem models a PI controller that functions as a control
  structure for the automatic voltage regulator and allows the
  representation of an equipment retrofit with a modern digital
  controller. The minimum and maximum anti-windup saturation limits for
  the block are *VPImin* and
  *VPImax*,
  respectively.
- The Lead-Lag block models additional dynamics associated with
  the voltage regulator and represents the system stabilizer. Here,
  *TC* is the lead time
  constant and *TB* is the lag
  time constant. Refer to the documentation for this block for the exact
  discrete and continuous implementations.
- An inner field voltage control loop is utilized to linearize the
  exciter control characteristic and it is composed of the gains
  *KM* and
  *KG* and the time
  constant *TM*. The minimum and
  maximum anti-windup saturation limits for the block are
  *VMmin* and
  *VMmax*,
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
