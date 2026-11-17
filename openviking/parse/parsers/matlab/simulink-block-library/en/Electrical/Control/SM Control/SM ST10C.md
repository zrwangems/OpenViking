---
type: simulink-block
title: 'SM ST10C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smst10c'
documentation_source_path: 'ref/smst10c.html'
language: en
---

# SM ST10C

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
  `Summation point at voltage
  error`.
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
  error`.
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
  error`.

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
  error`.
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
  summary: Regulator time constant 0.01 (default) | positive scalar
  group: Pre-Control
- name: Regulator gain, K_R (pu)
  summary: Regulator gain 500 (default) | positive scalar
  group: Control
- name: Voltage regulator denominator (lag) time constant 1, T_B1 (s)
  summary: Regulator lag time constant 1 12.5 (default) | positive scalar
  group: Control
- name: Voltage regulator numerator (lead) time constant 1, T_C1 (s)
  summary: Regulator lead time constant 1 1.5 (default) | positive scalar
  group: Control
- name: Voltage regulator denominator (lag) time constant 2, T_B2 (s)
  summary: Regulator lag time constant 2 0.1 (default) | positive scalar
  group: Control
- name: Voltage regulator numerator (lead) time constant 2, T_C2 (s)
  summary: Regulator lead time constant 2 0.1 (default) | positive scalar
  group: Control
- name: UEL regulator denominator (lag) time constant 1, T_UB1 (s)
  summary: UEL regulator lag time constant 1 12.5 (default)
  group: Control
- name: UEL regulator numerator (lead) time constant 1, T_UC1 (s)
  summary: UEL regulator lead time constant 1 1.5 (default)
  group: Control
- name: UEL regulator denominator (lag) time constant 2, T_UB2 (s)
  summary: UEL regulator lag time constant 2 0.1 (default)
  group: Control
- name: UEL regulator numerator (lead) time constant 2, T_UC2 (s)
  summary: UEL regulator lead time constant 2 0.1 (default)
  group: Control
- name: OEL regulator denominator (lag) time constant 1, T_OB1 (s)
  summary: OEL regulator lag time constant 1 12.5 (default)
  group: Control
- name: OEL regulator numerator (lead) time constant 1, T_OC1 (s)
  summary: OEL regulator lead time constant 1 1.5 (default)
  group: Control
- name: OEL regulator denominator (lag) time constant 2, T_OB2 (s)
  summary: OEL regulator lag time constant 2 0.1 (default)
  group: Control
- name: OEL regulator numerator (lead) time constant 2, T_OC2 (s)
  summary: OEL regulator lead time constant 2 0.1 (default)
  group: Control
- name: Maximum regulator output, V_Rmax (pu)
  summary: Maximum regulator output 10 (default) | real scalar
  group: Control
- name: Minimum regulator output, V_Rmin (pu)
  summary: Minimum regulator output -8.7 (default) | real scalar
  group: Control
- name: Maximum PSS regulator output, V_RSmax (pu)
  summary: Maximum PSS regulator output 5 (default) | real scalar
  group: Control
- name: Minimum PSS regulator output, V_RSmin (pu)
  summary: Minimum PSS regulator output -5 (default) | real scalar
  group: Control
- name: Alternate PSS input locations (V_S)
  summary: PSS input location Summation point at output of AVR (default) | Summation point at voltage error calculation |
    Summation point at voltage error or take-over limits
  group: Control
- name: Alternate OEL input locations (V_OEL)
  summary: OEL input location Summation point at voltage error (default) | Unused | Take-over at voltage error | Take-over
    at voltage regulator output
  group: Control
- name: Alternate UEL input locations (V_UEL)
  summary: UEL input location Summation point at voltage error (default) | Unused | Take-over at voltage error | Take-over
    at voltage regulator output
  group: Control
- name: Alternate SCL input locations (V_SCL)
  summary: SCL input location Summation point at voltage error (default) | Unused | Take-over at voltage error | Take-over
    at voltage regulator output
  group: Control
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: Rectifier loading factor 0.01 (default) | positive scalar
  group: Exciter
- name: Equivalent time constant for rectifier bridge, T_1 (s)
  summary: Time constant for rectifier bridge 0.004 (default) | positive scalar
  group: Exciter
- name: Potential circuit (voltage) gain coefficient, K_P (pu)
  summary: Potential circuit voltage gain coefficient 1 (default) | positive scalar
  group: Exciter
- name: Potential circuit (current) gain coefficient, K_I (pu)
  summary: Potential circuit current gain coefficient 0 (default) | positive scalar
  group: Exciter
- name: Reactance associated with the potential source, X_L (pu)
  summary: Potential source reactance 0 (default) | positive scalar
  group: Exciter
- name: Potential circuit phase angle (degrees)
  summary: Potential circuit phase angle 0 (default) | positive scalar
  group: Exciter
- name: Maximum available exciter voltage, V_Bmax (pu)
  summary: Exciter voltage upper limit 1.5 (default) | positive scalar
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

### **Regulator input filter time constant, T\_R (s)** — Regulator time constant `0.01` (default) | positive scalar

Equivalent time constant for the voltage transducer filtering.

### Control

### **Regulator gain, K\_R (pu)** — Regulator gain `500` (default) | positive scalar

Gain of the regulator.

### **Voltage regulator denominator (lag) time constant 1, T\_B1 (s)** — Regulator lag time constant 1 `12.5` (default) | positive scalar

Equivalent lag time constant in the second Lead-Lag (Discrete
or Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Voltage regulator numerator (lead) time constant 1, T\_C1 (s)** — Regulator lead time constant 1 `1.5` (default) | positive scalar

Equivalent lead time constant in the second Lead-Lag (Discrete
or Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lead dynamics are
negligible.

### **Voltage regulator denominator (lag) time constant 2, T\_B2 (s)** — Regulator lag time constant 2 `0.1` (default) | positive scalar

Equivalent lag time constant in the first Lead-Lag (Discrete or
Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Voltage regulator numerator (lead) time constant 2, T\_C2 (s)** — Regulator lead time constant 2 `0.1` (default) | positive scalar

Equivalent lead time constant in the first Lead-Lag (Discrete
or Continuous) block of the voltage regulator. Set this
parameter to `0` when the additional lead dynamics are
negligible.

### **UEL regulator denominator (lag) time constant 1, T\_UB1 (s)** — UEL regulator lag time constant 1 `12.5` (default)

Equivalent lag time constant in the second Lead-Lag (Discrete
or Continuous) block of the underexcitation limiter
regulator. Set this parameter to `0` when the
additional lag dynamics are negligible.

### **UEL regulator numerator (lead) time constant 1, T\_UC1 (s)** — UEL regulator lead time constant 1 `1.5` (default)

Equivalent lead time constant in the second Lead-Lag (Discrete
or Continuous) block of the underexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **UEL regulator denominator (lag) time constant 2, T\_UB2 (s)** — UEL regulator lag time constant 2 `0.1` (default)

Equivalent lag time constant in the first Lead-Lag (Discrete or
Continuous) block of the underexcitation limiter regulator.
Set this parameter to `0` when the additional lag
dynamics are negligible.

### **UEL regulator numerator (lead) time constant 2, T\_UC2 (s)** — UEL regulator lead time constant 2 `0.1` (default)

Equivalent lead time constant in the first Lead-Lag (Discrete
or Continuous) block of the underexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **OEL regulator denominator (lag) time constant 1, T\_OB1 (s)** — OEL regulator lag time constant 1 `12.5` (default)

Equivalent lag time constant in the second Lead-Lag (Discrete
or Continuous) block of the overexcitation limiter
regulator. Set this parameter to `0` when the
additional lag dynamics are negligible.

### **OEL regulator numerator (lead) time constant 1, T\_OC1 (s)** — OEL regulator lead time constant 1 `1.5` (default)

Equivalent lead time constant in the second Lead-Lag (Discrete
or Continuous) block of the overexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **OEL regulator denominator (lag) time constant 2, T\_OB2 (s)** — OEL regulator lag time constant 2 `0.1` (default)

Equivalent lag time constant in the first Lead-Lag (Discrete or
Continuous) block of the overexcitation limiter regulator.
Set this parameter to `0` when the additional lag
dynamics are negligible.

### **OEL regulator numerator (lead) time constant 2, T\_OC2 (s)** — OEL regulator lead time constant 2 `0.1` (default)

Equivalent lead time constant in the first Lead-Lag (Discrete
or Continuous) block of the overexcitation limiter
regulator. Set this parameter to `0` when the
additional lead dynamics are negligible.

### **Maximum regulator output, V\_Rmax (pu)** — Maximum regulator output `10` (default) | real scalar

Maximum per-unit regulator output.

### **Minimum regulator output, V\_Rmin (pu)** — Minimum regulator output `-8.7` (default) | real scalar

Minimum per-unit regulator output.

### **Maximum PSS regulator output, V\_RSmax (pu)** — Maximum PSS regulator output `5` (default) | real scalar

Maximum per-unit output of the power system stabilizer
regulator.

### **Minimum PSS regulator output, V\_RSmin (pu)** — Minimum PSS regulator output `-5` (default) | real scalar

Minimum per-unit output of the power system stabilizer
regulator.

### **Alternate PSS input locations (V\_S)** — PSS input location `Summation point at output of AVR` (default) | `Summation point at voltage error calculation` | `Summation point at voltage error or take-over limits`

Location of the power system stabilizer input.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Summation point at voltage error` (default) | `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

Location of the overexcitation limiter input, specified as one of these options:

- `Summation point at voltage
  error` — **V\_OEL** is an
  input of the **Summation Point Logic**
  subsystem.
- `Take-over at voltage error` —
  **V\_OEL** is an input of the
  **Take-over Logic** subsystem.
- `Take-over at voltage regulator
  output` — **V\_OEL** is an
  input of the **Take-over Logic 1**
  subsystem.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Summation point at voltage error` (default) | `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

Location of the underexcitation limiter input, specified as one of these options:

- `Summation point at voltage
  error` — **V\_UEL** is an
  input of the **Summation Point Logic**
  subsystem.
- `Take-over at voltage error` —
  **V\_UEL** is an input of the
  **Take-over Logic** subsystem.
- `Take-over at voltage regulator
  output` — **V\_UEL** is an
  input of the **Take-over Logic 1**
  subsystem.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Summation point at voltage error` (default) | `Unused` | `Take-over at voltage error` | `Take-over at voltage regulator output`

Loction of the stator current limiter input, specified as one of these options:

- `Summation point` — Use the
  **V\_SCLsum** input port.
- Any of the `Take-over` options —
  Use the **V\_OELscl** and
  **V\_UELscl** input ports.

### Exciter

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.01` (default) | positive scalar

Rectifier loading factor. This value is proportional to the commutating
reactance.

### **Equivalent time constant for rectifier bridge, T\_1 (s)** — Time constant for rectifier bridge `0.004` (default) | positive scalar

Equivalent time constant of the rectifier bridge, in seconds.

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — Potential circuit voltage gain coefficient `1` (default) | positive scalar

Per-unit voltage gain coefficient in the power source circuit.

### **Potential circuit (current) gain coefficient, K\_I (pu)** — Potential circuit current gain coefficient `0` (default) | positive scalar

Per-unit current gain coefficient in the power source circuit.

#### Dependencies

To enable this parameter, set **Power source
selector** to `Position A: power source
derived from generator terminal voltage`.

### **Reactance associated with the potential source, X\_L (pu)** — Potential source reactance `0` (default) | positive scalar

Per-unit reactance in the potential source.

#### Dependencies

To enable this parameter, set **Power source
selector** to `Position A: power source
derived from generator terminal voltage`.

### **Potential circuit phase angle (degrees)** — Potential circuit phase angle `0` (default) | positive scalar

Phase angle of the power source circuit, in degrees.

#### Dependencies

To enable this parameter, set **Power source
selector** to `Position A: power source
derived from generator terminal voltage`.

### **Maximum available exciter voltage, V\_Bmax (pu)** — Exciter voltage upper limit `1.5` (default) | positive scalar

Maximum per-unit available exciter voltage value.

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

Discrete-time or continuous-time synchronous machine ST10C static excitation system with automatic voltage regulator

The SM ST10C block implements a synchronous-machine-type ST10C static
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

The SM ST10C block comprises four major components:

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

This diagram shows the structure of the ST10C excitation system
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
  (UEL), and stator current limiter (SCL). For more information about
  using limiters with this block, see Field Current Limiters.
- There are two Take-over Logic subsystems. They model the take-over
  point input location for the OEL, UEL and SCL voltages. For more
  information about using limiters with this block, see Field Current Limiters.
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
  *TC2* (or
  *TUC2* and
  *TOC2*) is the lead time
  constant and *TB2* (or
  *TUB2* and
  *TOB2*) is the lag time
  constant. The second Lead-Lag block allows the possibility of
  representing a transient gain increase, where
  *TC1* (or
  *TUC1* and
  *TOC1*) is the lead time
  constant and *TB1* (or
  *TUB1* and
  *TOB1*) is the lag time
  constant. See the documentation for the Lead-Lag block for information
  about the discrete and continuous implementations.
- The SM ST10C block also offers the option to apply the
  PSS signal at the AVR summing junction after the first Take-over Logic
  subsystem or at the output of the gate structure, through a separate
  path (the bottom path in the model). This separate path comprises the
  same control elements as the main summing junction path.
- The **Power source selector** parameter controls the
  origin of the power source for the controlled rectifier. The subsystem
  multiplies the voltage regulator command signal
  *VR*by the exciter field
  voltage *VB*. For more
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
- Take-over points — Override the usual behavior of the AVR.

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
