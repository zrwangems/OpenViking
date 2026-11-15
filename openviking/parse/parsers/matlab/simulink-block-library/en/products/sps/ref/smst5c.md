---
type: simulink-block
title: 'SM ST5C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — ST Type'
documentation_page: 'smst5c'
documentation_source_path: 'ref/smst5c.html'
language: en
---

# SM ST5C

## Ports

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
  locations** to `Summation
  point`.

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

### General

### **Initial field voltage, Efd0 (pu)** — Initial output voltage `1` (default) | real scalar

Initial per-unit voltage to apply to the field circuit of the
synchronous machine.

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

### **Regulator input filter time constant, T\_R (s)** — Regulator time constant `0.02` (default) | positive scalar

Equivalent time constant for the voltage transducer filtering.

### Control

### **Regulator gain, K\_R (pu)** — Regulator gain `200` (default) | positive scalar

Gain of the regulator.

### **Voltage regulator denominator (lag) time constant (first block), T\_B1 (s)** — Regulator lag time constant 1 `6` (default) | positive scalar

Equivalent lag time constant in the fist Lead-Lag (Discrete or
Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Voltage regulator numerator (lead) time constant (first block), T\_C1 (s)** — Regulator lead time constant 1 `0.8` (default) | positive scalar

Equivalent lead time constant in the first Lead-Lag (Discrete
or Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lead dynamics are
negligible.

### **Voltage regulator denominator (lag) time constant (second block), T\_B2 (s)** — Regulator lag time constant 2 `0.01` (default) | positive scalar

Equivalent lag time constant in the second Lead-Lag (Discrete
or Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Voltage regulator numerator (lead) time constant (second block), T\_C2 (s)** — Regulator lead time constant 2 `0.08` (default) | positive scalar

Equivalent lead time constant in the second Lead-Lag (Discrete
or Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lead dynamics are
negligible.

### **UEL regulator denominator (lag) time constant (first block), T\_UB1 (s)** — UEL regulator lag time constant 1 `10` (default)

Equivalent lag time constant in the first Lead-Lag (Discrete or
Continuous) block of the underexcitation limiter regulator.
Set this parameter to `0` when the additional lag
dynamics are negligible.

### **UEL regulator numerator (lead) time constant (first block), T\_UC1 (s)** — UEL regulator lead time constant 1 `2` (default)

Equivalent lead time constant in the first Lead-Lag (Discrete
or Continuous) block of the underexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **UEL regulator denominator (lag) time constant (second block), T\_UB2 (s)** — UEL regulator lag time constant 2 `0.05` (default)

Equivalent lag time constant in the second Lead-Lag (Discrete
or Continuous) block of the underexcitation limiter
regulator. Set this parameter to `0` when the
additional lag dynamics are negligible.

### **UEL regulator numerator (lead) time constant (second block), T\_UC2 (s)** — UEL regulator lead time constant 2 `0.1` (default)

Equivalent lead time constant in the second Lead-Lag (Discrete
or Continuous) block of the underexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **OEL regulator denominator (lag) time constant (first block), T\_OB1 (s)** — OEL regulator lag time constant 1 `2` (default)

Equivalent lag time constant in the first Lead-Lag (Discrete or
Continuous) block of the overexcitation limiter regulator.
Set this parameter to `0` when the additional lag
dynamics are negligible.

### **OEL regulator numerator (lead) time constant (first block), T\_OC1 (s)** — OEL regulator lead time constant 1 `0.1` (default)

Equivalent lead time constant in the first Lead-Lag (Discrete
or Continuous) block of the overexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **OEL regulator denominator (lag) time constant (second block), T\_OB2 (s)** — OEL regulator lag time constant 2 `0.08` (default)

Equivalent lag time constant in the second Lead-Lag (Discrete
or Continuous) block of the overexcitation limiter
regulator. Set this parameter to `0` when the
additional lag dynamics are negligible.

### **OEL regulator numerator (lead) time constant (second block), T\_OC2 (s)** — OEL regulator lead time constant 2 `0.08` (default)

Equivalent lead time constant in the second Lead-Lag (Discrete
or Continuous) block of the overexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **Maximum regulator output, V\_Rmax (pu)** — Maximum regulator output `5` (default) | real scalar

Maximum per-unit regulator output.

### **Minimum regulator output, V\_Rmin (pu)** — Minimum regulator output `-4` (default) | real scalar

Minimum per-unit regulator output.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point` | `Take-over`

Overexcitation limiter input location.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point` | `Take-over`

Underexcitation limiter input location.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point` | `Take-over`

Stator current limiter input location, specified as one of these options:

- `Summation point` — Use the
  **V\_SCLsum** input port.
- `Take-over` — Use the
  **V\_SCLoel** and
  **V\_SCLuel** input ports.

### Exciter

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.004` (default) | positive scalar

Per-unit rectifier loading factor. This value is proportional to the commutating
reactance.

### **Thyristor bridge firing control equivalent time constant, T\_1 (s)** — Time constant for thyristor bridge firing control `0.004` (default) | positive scalar

Equivalent time constant of the firing control for the thyristor
bridge, in seconds.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Discrete-time or continuous-time synchronous machine ST5C static excitation system with automatic voltage regulator

The SM ST5C block implements a synchronous-machine-type ST5C static
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

The SM ST5C block comprises three major components:

- The Current Compensator component modifies the measured terminal voltage
  as a function of the terminal current.
- The Voltage Measurement Transducer component simulates the dynamics of a
  terminal voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error value.
  The component then passes this value through a voltage regulator to produce
  the field voltage.

This diagram shows the structure of the ST5C excitation system
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
  (UEL), stator current limiter (SCL), and power switch selector (V\_S)
  voltages. For more information about using limiters with this block, see
  Field Current Limiters.
- The Take-over Logic subsystem models the take-over point input
  location for the OEL, UEL, SCL and PSS voltages. For more information
  about using limiters with this block, see Field Current Limiters.
- A parallel configuration of Lead-Lag (Discrete or Continuous) blocks
  offer independent control settings when a limiter is active. The model
  offers a common gain factor *KR*
  and two Lead-Lag (Discrete or Continuous) blocks for the AVR and for the
  underexcitation and overexcitation limiters. The SW\_UEL and SW\_OEL
  Switch blocks activate the appropriate control path when the
  *VUEL* and/or
  *VOEL* signals are
  connected to their respective alternate positions. The SW\_UEL and SW\_OEL
  Switch blocks are on position B when you set the **Alternate UEL
  input locations (V\_UEL)** and **Alternate OEL input
  locations (V\_OEL)** parameters to `Take-over at
  voltage error`.
- The two Lead-Lag blocks in each control path model additional
  dynamics associated with the voltage regulator and with the
  underexcitation and overexcitation limiters. The first Lead-Lag block in
  each respective path represents a transient gain reduction, where
  *TC* (or
  *TC2* and
  *TUC2*) is the lead time
  constant and *TB* (or
  *TB2* and
  *TUB2*) is the lag time
  constant. The second Lead-Lag block allows the possibility of
  representing a transient gain increase, where
  *TC1* is the lead time
  constant and *TB1* is the lag
  time constant. See the documentation for the Lead-Lag block for
  information about the discrete and continuous implementations.

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
