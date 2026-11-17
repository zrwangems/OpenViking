---
type: simulink-block
title: 'SM ST7C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst7c'
documentation_source_path: 'ref/smst7c.html'
language: en
---

# SM ST7C

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
  summary: Take-over stator current limit for overexcitation limiter scalar
  direction: input
  data_types: single | double
- name: V_SCLuel
  summary: Take-over stator current limit for underexcitation limiter scalar
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
  `Summation point at voltage
  reference`.
- To use the input from the overexcitation limiter at
  the Take-over Logic subsystem, set **Alternate
  OEL input locations (V\_OEL)** to
  `Take-over at voltage
  error`.
- To use the input from the overexcitation limiter at
  the Take-over Logic1 subsystem, set **Alternate
  OEL input locations (V\_OEL)** to
  `Take-over at voltage regulator
  output`.

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
  `Summation point at voltage
  reference`.
- To use the input from the underexcitation limiter at
  the Take-over Logic subsystem, set **Alternate
  UEL input locations (V\_UEL)** to
  `Take-over at voltage
  error`.
- To use the input from the underexcitation limiter at
  the Take-over Logic1 subsystem, set **Alternate
  UEL input locations (V\_UEL)** to
  `Take-over at voltage regulator
  output`.

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
  `Summation point at voltage
  reference`.

**Data Types:** `single` | `double`

### **V\_SCLoel** — Take-over stator current limit for overexcitation limiter scalar

Input from the stator current limiter to prevent field overexcitation
when using the take-over point, in per-unit representation, specified as
a scalar.

#### Dependencies

- To ignore the input from the stator current limiter,
  set **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at
  the Take-over Logic subsystem, set **Alternate
  SCL input locations (V\_SCL)** to
  `Take-over at voltage
  reference`.
- To use the input from the stator current limiter at
  the Take-over Logic1 subsystem, set **Alternate
  SCL input locations (V\_SCL)** to
  `Take-over at voltage regulator
  output`.

**Data Types:** `single` | `double`

### **V\_SCLuel** — Take-over stator current limit for underexcitation limiter scalar

Input from the stator current limiter to prevent field underexcitation
when using the take-over point, in per-unit representation, specified as
a scalar.

#### Dependencies

- To ignore the input from the stator current limiter,
  set **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at
  the Take-over Logic subsystem, set **Alternate
  SCL input locations (V\_SCL)** to
  `Take-over at voltage
  error`.
- To use the input from the stator current limiter at
  the Take-over Logic1 subsystem, set **Alternate
  SCL input locations (V\_SCL)** to
  `Take-over at voltage regulator
  output`.

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
  summary: Regulator time constant 0 (default) | positive scalar
  group: Pre-Control
- name: Regulator input filter time constant, T_G (s)
  summary: Time constant for voltage filtering 1 (default) | positive scalar
  group: Control
- name: Voltage regulator denominator (lag) time constant, T_F (s)
  summary: Lag time constant of the voltage regulator 1 (default) | positive scalar
  group: Control
- name: Maximum voltage reference, V_max (pu)
  summary: Maximum voltage reference 1.1 (default) | real scalar
  group: Control
- name: Minimum voltage reference, V_min (pu)
  summary: Minimum voltage referenc 0.9 (default) | real scalar
  group: Control
- name: Voltage regulator gain, K_PA (pu)
  summary: Voltage regulator gain 40 (default) | positive scalar
  group: Control
- name: Voltage regulator denominator (lag) time constant, T_B (s)
  summary: Voltage regulator lag time constant 1 (default) | positive scalar
  group: Control
- name: Voltage regulator numerator (lead) time constant, T_C (s)
  summary: Voltage regulator lead time constant 1 (default) | positive scalar
  group: Control
- name: Thyristor bridge firing control equivalent time constant, T_A (s)
  summary: Regulator lag time constant for first lead-lag block 0 (default) | positive scalar
  group: Control
- name: Maximum regulator output, V_Rmax (pu)
  summary: Maximum regulator output 5 (default) | real scalar
  group: Control
- name: Minimum regulator output, V_Rmin (pu)
  summary: Minimum regulator output -4.5 (default) | real scalar
  group: Control
- name: Alternate OEL input locations (V_OEL)
  summary: OEL input location Unused (default) | Summation point at voltage reference | Take-over at voltage reference | Take-over
    at voltage regulator output
  group: Control
- name: Alternate UEL input locations (V_UEL)
  summary: UEL input location Unused (default) | Summation point at voltage reference | Take-over at voltage reference | Take-over
    at voltage regulator output
  group: Control
- name: Alternate SCL input locations (V_SCL)
  summary: SCL input location Unused (default) | Summation point at voltage reference | Take-over at voltage reference | Take-over
    at voltage regulator output
  group: Control
- name: Minimum excitation limit gain, K_L (pu)
  summary: Minimum excitation limit gain 1 (default) | real scalar
  group: Exciter
- name: Maximum excitation limit gain, K_H (pu)
  summary: Maximum excitation limit gain 1 (default) | real scalar
  group: Exciter
- name: PI regulator feedback gain, K_IA (pu)
  summary: PI regulator feedback gain 1 (default) | real scalar
  group: Exciter
- name: PI regulator feedback time constant, T_IA (s)
  summary: PI regulator feedback time constant 3 (default) | positive scalar
  group: Exciter
```

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

### **Regulator input filter time constant, T\_R (s)** — Regulator time constant `0` (default) | positive scalar

Equivalent time constant for the voltage transducer filtering.

### Control

### **Regulator input filter time constant, T\_G (s)** — Time constant for voltage filtering `1` (default) | positive scalar

Equivalent time constant for the voltage filtering.

### **Voltage regulator denominator (lag) time constant, T\_F (s)** — Lag time constant of the voltage regulator `1` (default) | positive scalar

Equivalent lag time constant of the voltage regulator, in seconds.

### **Maximum voltage reference, V\_max (pu)** — Maximum voltage reference `1.1` (default) | real scalar

Maximum per-unit voltage reference of the voltage regulator.

### **Minimum voltage reference, V\_min (pu)** — Minimum voltage referenc `0.9` (default) | real scalar

Minimum per-unit voltage reference of the voltage regulator.

### **Voltage regulator gain, K\_PA (pu)** — Voltage regulator gain `40` (default) | positive scalar

Per-unit gain of the voltage regulator.

### **Voltage regulator denominator (lag) time constant, T\_B (s)** — Voltage regulator lag time constant `1` (default) | positive scalar

Equivalent lag time constant of the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Voltage regulator numerator (lead) time constant, T\_C (s)** — Voltage regulator lead time constant `1` (default) | positive scalar

Equivalent lead time constant of the voltage regulator. Set this
parameter to `0` when the additional lead dynamics are
negligible.

### **Thyristor bridge firing control equivalent time constant, T\_A (s)** — Regulator lag time constant for first lead-lag block `0` (default) | positive scalar

Equivalent time constant in the thyristor bridge firing
control.

### **Maximum regulator output, V\_Rmax (pu)** — Maximum regulator output `5` (default) | real scalar

Maximum per-unit output of the regulator.

### **Minimum regulator output, V\_Rmin (pu)** — Minimum regulator output `-4.5` (default) | real scalar

Minimum per-unit output of the regulator.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

Overexcitation limiter input location, specified as one of these options:

- `Summation point at voltage
  reference` — **V\_OEL** is
  an input of the Summation Point Logic subsystem.
- `Take-over at voltage reference`
  — **V\_OEL** is an input of the Take-over
  Logic subsystem.
- `Take-over at voltage regulator
  output` — **V\_OEL** is an
  input of the Take-over Logic 1 subsystem.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

Underexcitation limiter input location, specified as one of these options:

- `Summation point at voltage
  reference` — **V\_UEL** is
  an input of the Summation Point Logic subsystem.
- `Take-over at voltage reference`
  — **V\_UEL** is an input of the Take-over
  Logic subsystem.
- `Take-over at voltage regulator
  output` — **V\_UEL** is an
  input of the Take-over Logic 1 subsystem.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

Stator current limiter input location. specified as one of these options:

- `Summation point` — Use the
  **V\_SCLsum** input port.
- Any of the `Take-over` options —
  Use the **V\_SCLoel** and
  **V\_SCLuel** input ports.

### Exciter

### **Minimum excitation limit gain, K\_L (pu)** — Minimum excitation limit gain `1` (default) | real scalar

Minimum per-unit gain of the exciter.

### **Maximum excitation limit gain, K\_H (pu)** — Maximum excitation limit gain `1` (default) | real scalar

Maximum per-unit gain of the exciter.

### **PI regulator feedback gain, K\_IA (pu)** — PI regulator feedback gain `1` (default) | real scalar

Per-unit feedback gain of the PI regulator.

### **PI regulator feedback time constant, T\_IA (s)** — PI regulator feedback time constant `3` (default) | positive scalar

Feedback time constant of the Pi regulator, in seconds.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Discrete-time or continuous-time synchronous machine ST7C static excitation system with automatic voltage regulator

The SM ST7C block implements a synchronous-machine-type ST7C static
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

The SM ST7C block comprises three major components:

- The Current Compensator component modifies the measured terminal voltage
  as a function of the terminal current.
- The Voltage Measurement Transducer component simulates the dynamics of a
  terminal voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error value.
  The component then passes this value through a voltage regulator to produce
  the field voltage.

This diagram shows the structure of the ST7C excitation system
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
- *EFD* is the field voltage.

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
  (UEL), and stator current limiter (SCL) voltages. For more information
  about using limiters with this block, see Field Current Limiters.
- There are two Take-over Logic subsystems. The subsystems model the
  take-over point input location for the OEL, UEL and SCL voltages. For
  more information about using limiters with this block, see Field Current Limiters.
- A Lead-Lag block in series introduces a derivative function
  and transforms the regulator in a PID. This is typically used only with
  brushless excitation systems.
- *KL* and
  *KH* model a
  high-bandwidth regulator inner loop that regulates the generator
  exciting current.

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
