---
type: simulink-block
title: 'SM AC3C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac3c'
documentation_source_path: 'ref/smac3c.html'
language: en
---

# SM AC3C

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

Terminal voltage magnitude in per-unit representation, specified as a
scalar.

**Data Types:** `single` | `double`

### **I\_T** — Terminal current scalar

Terminal current magnitude in per-unit representation, specified as a
scalar.

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
  the take-over point, set **Alternate SCL input
  locations (V\_SCL)** to
  `Take-over`.

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
  summary: Initial output voltage 1 (default) | real number
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
  summary: Proportional gain of the voltage regulator 1 (default)
  group: Control
- name: Voltage regulator integral gain, K_IR (pu/s)
  summary: Integral gain of voltage regulator 0 (default)
  group: Control
- name: Voltage regulator derivative gain, K_DR (pu.s)
  summary: Derivative gain of voltage regulator 0 (default)
  group: Control
- name: Lag time constant for derivative channel of PID controller, T_DR (s)
  summary: Lag time constant for PID derivative channel 1 (default) | positive number
  group: Control
- name: Maximum PID regulator output, V_PIDmax (pu)
  summary: Maximum output of the PID regulator 3.2 (default) | positive number
  group: Control
- name: Minimum PID regulator output, V_PIDmin (pu)
  summary: Minimum output of the PID regulator -3.2 (default) | positive number
  group: Control
- name: Regulator denominator (lag) time constant, T_B (s)
  summary: Regulator lag time constant 0 (default) | positive number
  group: Control
- name: Regulator numerator (lead) time constant, T_C (s)
  summary: Regulator lead time constant 0 (default) | positive number
  group: Control
- name: Regulator output gain, K_A (pu)
  summary: Regulator gain 45.62 (default) | positive number
  group: Control
- name: Regulator output time constant, T_A (s)
  summary: Regulator time constant 0.013 (default) | positive number
  group: Control
- name: Maximum regulator output, V_Amax (pu)
  summary: Upper limit of the regulator output 1 (default) | real number
  group: Control
- name: Minimum regulator output, V_Amin (pu)
  summary: Lower limit of the regulator output -0.95 (default) | real number
  group: Control
- name: Rate feedback time constant, T_F (s)
  summary: Rate feedback time constant 1 (default) | positive number
  group: Control
- name: Value of EFD at which feedback gain changes, E_FDN (pu)
  summary: Value of EFD at which feedback gain changes 2.36 (default) | positive number
  group: Control
- name: Rate feedback excitation system stabilizer gain, K_F (pu)
  summary: Rate feedback gain 0.143 (default) | positive number
  group: Control
- name: Rate feedback excitation system stabilizer gain, K_N (pu)
  summary: Rate feedback gain 0.05 (default) | positive number
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
- name: Exciter field proportional constant, K_E (pu)
  summary: Exciter field gain 1 (default) | positive number
  group: Exciter
- name: Exciter field time constant, T_E (s)
  summary: Exciter field time constant 0.17 (default) | positive number
  group: Exciter
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: Rectifier loading factor 0.104 (default) | positive number
  group: Exciter
- name: Demagnetizing factor, function of exciter alternator reactances, K_D (pu)
  summary: Demagnetization factor 0.499 (default) | positive number
  group: Exciter
- name: Exciter output voltage for saturation factor S_E(E_1), E_1 (pu)
  summary: First saturation output voltage 6.24 (default) | positive number
  group: Exciter
- name: Exciter saturation factor at exciter output voltage E_1, S_E(E_1) (1)
  summary: First saturation lookup voltage 1.143 (default) | positive number
  group: Exciter
- name: Exciter output voltage for saturation factor S_E(E_2), E_2 (pu)
  summary: Second saturation output voltage 4.68 (default) | positive number
  group: Exciter
- name: Exciter saturation factor at exciter output voltage E_2, S_E(E_2) (1)
  summary: Second saturation lookup voltage 0.1 (default) | positive number
  group: Exciter
- name: Gain associated with regulator and alternator field power supply, K_R (pu)
  summary: Regulator and alternator field power supply gain 3.77 (default) | real number
  group: Exciter
- name: Minimum exciter voltage output, V_Emin (pu)
  summary: Exciter lower limit 0.1 (default) | real number
  group: Exciter
- name: Exciter field current limit, V_FEmax (pu)
  summary: Exciter upper limit 16 (default) | real number
  group: Exciter
```

### General

### **Initial field voltage, Efd0 (pu)** — Initial output voltage `1` (default) | real number

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

### **Voltage regulator proportional gain, K\_PR (pu)** — Proportional gain of the voltage regulator `1` (default)

Per-unit proportional gain of the voltage regulator.

### **Voltage regulator integral gain, K\_IR (pu/s)** — Integral gain of voltage regulator `0` (default)

Per-unit over second integral gain of the voltage regulator.

### **Voltage regulator derivative gain, K\_DR (pu.s)** — Derivative gain of voltage regulator `0` (default)

Derivative gain of the voltage regulator.

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — Lag time constant for PID derivative channel `1` (default) | positive number

Equivalent lag time constant for the derivative channel of the PID
controller.

### **Maximum PID regulator output, V\_PIDmax (pu)** — Maximum output of the PID regulator `3.2` (default) | positive number

Maximum admissible per-unit output of the PID regulator.

### **Minimum PID regulator output, V\_PIDmin (pu)** — Minimum output of the PID regulator `-3.2` (default) | positive number

Minimum admissible per-unit output of the PID regulator.

### **Regulator denominator (lag) time constant, T\_B (s)** — Regulator lag time constant `0` (default) | positive number

Equivalent lag time constant in the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Regulator numerator (lead) time constant, T\_C (s)** — Regulator lead time constant `0` (default) | positive number

Equivalent lead time constant in the voltage regulator. Set this parameter to
`0` when the additional lead dynamics are
negligible.

### **Regulator output gain, K\_A (pu)** — Regulator gain `45.62` (default) | positive number

Gain associated with the voltage regulator.

### **Regulator output time constant, T\_A (s)** — Regulator time constant `0.013` (default) | positive number

Major time constant of the voltage regulator.

### **Maximum regulator output, V\_Amax (pu)** — Upper limit of the regulator output `1` (default) | real number

Maximum per-unit output voltage of the regulator.

### **Minimum regulator output, V\_Amin (pu)** — Lower limit of the regulator output `-0.95` (default) | real number

Minimum per-unit output voltage of the regulator.

### **Rate feedback time constant, T\_F (s)** — Rate feedback time constant `1` (default) | positive number

Rate feedback block time constant for the stabilization of the excitation system.

### **Value of EFD at which feedback gain changes, E\_FDN (pu)** — Value of EFD at which feedback gain changes `2.36` (default) | positive number

Per-unit value of EFD at which the feedback gain changes.

### **Rate feedback excitation system stabilizer gain, K\_F (pu)** — Rate feedback gain `0.143` (default) | positive number

Rate feedback block gain for stabilization of excitation
system.

### **Rate feedback excitation system stabilizer gain, K\_N (pu)** — Rate feedback gain `0.05` (default) | positive number

Rate feedback block gain for stabilization of excitation
system.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the overexcitation limiter input.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the underexcitation limiter input.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the stator current limiter input :

- If you select `Summation point`,
  use the **V\_SCLsum** input port.
- If you select `Take-over`, use
  the **V\_SCLoel** and
  **V\_SCLuel** input ports.

### Exciter

### **Exciter field proportional constant, K\_E (pu)** — Exciter field gain `1` (default) | positive number

Proportional constant for the exciter field.

### **Exciter field time constant, T\_E (s)** — Exciter field time constant `0.17` (default) | positive number

Time constant for the exciter field.

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.104` (default) | positive number

Rectifier loading factor proportional to the commutating reactance.

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — Demagnetization factor `0.499` (default) | positive number

Demagnetization factor related to the exciter alternator reactances.

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — First saturation output voltage `6.24` (default) | positive number

Exciter output voltage for the first saturation factor.

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — First saturation lookup voltage `1.143` (default) | positive number

Saturation factor for the first exciter.

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — Second saturation output voltage `4.68` (default) | positive number

Exciter output voltage for the second saturation factor.

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — Second saturation lookup voltage `0.1` (default) | positive number

Saturation factor for the second exciter.

### **Gain associated with regulator and alternator field power supply, K\_R (pu)** — Regulator and alternator field power supply gain `3.77` (default) | real number

Per-unit regulator and alternator field power supply gain.

### **Minimum exciter voltage output, V\_Emin (pu)** — Exciter lower limit `0.1` (default) | real number

Minimum per-unit exciter voltage output.

### **Exciter field current limit, V\_FEmax (pu)** — Exciter upper limit `16` (default) | real number

Per-unit exciter field current upper limit.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time synchronous machine AC3C excitation system including an automatic voltage regulator and an exciter

The SM AC3C block implements a synchronous machine type AC3C excitation
system model in conformance with IEEE 421.5-2016[1].

Use this block to model the control and regulation of the field voltage of a
synchronous machine that operates as a generator using an AC rotating exciter.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

The SM AC3C block is made up of four major components:

- The Current Compensator modifies the measured terminal voltage as a
  function of terminal current.
- The Voltage Measurement Transducer simulates the dynamics of a terminal
  voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error. This
  voltage error is then passed through a voltage regulator to produce the
  exciter field voltage.
- The AC Rotating Exciter models the AC rotating exciter, which produces a
  field voltage that is applied to the controlled synchronous machine. The
  block also feeds the exciter field current (which is given the standard
  symbol *VFE*) back to the excitation
  system.

This diagram shows the overall structure of the AC3C excitation system
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
- *EFE* and
  *VFE* are the exciter field
  voltage and current, respectively.
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
Filter block with time constant
*TR*. Refer to the documentation for
this block for the discrete and continuous implementations.

### Excitation Control Elements

This diagram illustrates the overall structure of the excitation control elements:

In the diagram:

- The Summation Point Logic subsystem models the summation point input
  location for the overexcitation limiter (OEL), underexcitation limiter
  (UEL), and stator current limiter (SCL) voltages. For more information
  about using limiters with this block, see Field Current Limiters.
- The PID\_R subsystem models a PID controller and it allows the
  representation of retrofit projects, where a modern digital exciter is
  added to the exciter. It is possible to model a SM AC3A excitation
  system model by tuning the PID parameters.
- The Lead-Lag block models additional dynamics associated with
  the voltage regulator. Here,
  *TC* is the lead time
  constant and *TB* is the lag
  time constant. Refer to the documentation for the Lead-Lag block for the
  discrete and continuous implementations.
- The Take-over Logic subsystem models the take-over point input
  location for the OEL, UEL, and SCL voltages. For more information about
  using limiters with this block, see Field Current Limiters.
- The Low-Pass Filter block models the major dynamics of the
  voltage regulator. Here, *KA* is
  the regulator gain and *TA* is
  the major time constant of the regulator. The minimum and maximum
  anti-windup saturation limits for the block are
  *VAmin* and
  *VAmax*,
  respectively.
- The voltage regulator power is derived from the exciter output
  voltage. The voltage regulator command signal,
  *VA*, is multiplied by
  the exciter output voltage,
  *EFD*, and multiplied by
  *KR*. This adds a level
  of nonlinearity to the system.
- The Filtered Derivative block models the rate feedback path for
  stabilization of the excitation system. In this case, the stabilizer has
  a nonlinear characteristic. If the exciter output voltage,
  *EFD*, is less than the
  **Value of EFD at which feedback gain changes, E\_FDN
  (pu)** parameter, the feedback gain is
  *KF*. If the exciter
  output voltage is greater than the **Value of EFD at which
  feedback gain changes, E\_FDN (pu)** parameter, the feedback
  gain is *KN*. Refer to the
  documentation for the Filtered Derivative block for the exact discrete
  and continuous implementations.
- *EFEmin* and
  *EFEmax* are the minimum
  and maximum saturation limits for the output exciter field voltage
  *EFE*.

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

### AC Rotating Exciter

This diagram shows the structure of the AC rotating exciter:

In the diagram:

- The exciter field current
  *VFE* is
  the sum of three signals:

  - The nonlinear function
    *Vx*
    models the saturation of the exciter output
    voltage.
  - The proportional term
    *KE*
    models the linear relationship between the exciter
    output voltage and the exciter field
    current.
  - The subsystem models the demagnetizing
    effect of the load current on the exciter output
    voltage using the demagnetization constant
    *KD* in
    the feedback loop.
- The Integrator with variable limits
  subsystem integrates the difference between
  *EFE* and
  *VFE* to
  generate the exciter alternator output voltage
  *VE*.
  *TE* is
  the time constant for this process.
- The nonlinear function
  *FEX*
  models the exciter output voltage drop from the
  rectifier regulation. This function depends on the
  constant
  *KC*,
  which itself is a function of commutating
  reactance.
- The parameters
  *VEmin*
  and
  *VFEmax*
  model the lower and upper limits of the rotating
  exciter.
