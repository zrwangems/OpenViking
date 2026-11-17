---
type: simulink-block
title: 'SM AC4C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac4c'
documentation_source_path: 'ref/smac4c.html'
language: en
---

# SM AC4C

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
- name: V_OELscl
  summary: Take-over stator current limit for overexcitation limiter scalar
  direction: input
  data_types: single | double
- name: V_UELscl
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

- To ignore the input from the overexcitation limiter, set
  **Alternate OEL input locations
  (V\_OEL)** to
  `Unused`.
- To use the input from the overexcitation limiter at the
  summation point, set **Alternate OEL input locations
  (V\_OEL)** to `Summation
  point`.
- To use the input from the overexcitation limiter at the
  take-over point, set **Alternate OEL input locations
  (V\_OEL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **V\_UEL** — Underexcitation limit signal scalar

Input from the underexcitation limiter, in per-unit representation, specified as a
scalar.

#### Dependencies

- To ignore the input from the underexcitation limiter, set
  **Alternate UEL input locations
  (V\_UEL)** to
  `Unused`.
- To use the input from the underexcitation limiter at the
  summation point, set **Alternate UEL input locations
  (V\_UEL)** to `Summation
  point`.
- To use the input from the underexcitation limiter at the
  take-over point, set **Alternate UEL input locations
  (V\_UEL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **V\_SCLsum** — Summation point stator current limit signal scalar

Input from the stator current limiter when using the summation point, in per-unit
representation, specified as a scalar.

#### Dependencies

- To ignore the input from the stator current limiter, set
  **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at the
  summation point, set **Alternate SCL input locations
  (V\_SCL)** to `Summation
  point`.

**Data Types:** `single` | `double`

### **V\_OELscl** — Take-over stator current limit for overexcitation limiter scalar

Input from the stator current limiter to prevent field overexcitation when
using the take-over point, in per-unit representation, specified as a
scalar.

#### Dependencies

- To ignore the input from the stator current limiter, set
  **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at the
  take-over point, set **Alternate SCL input locations
  (V\_SCL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **V\_UELscl** — Take-over stator current limit for underexcitation limiter scalar

Input from the stator current limiter to prevent field underexcitation
when using the take-over point, in per-unit representation, specified as a
scalar.

#### Dependencies

- To ignore the input from the stator current limiter, set
  **Alternate SCL input locations
  (V\_SCL)** to
  `Unused`.
- To use the input from the stator current limiter at the
  take-over point, set **Alternate SCL input locations
  (V\_SCL)** to
  `Take-over`.

**Data Types:** `single` | `double`

### **Ifd\_pu** — Measured field current scalar

Measured per-unit field current of the synchronous machine, specified as a scalar.

**Data Types:** `single` | `double`
### Output

### **Efd\_pu** — Field voltage scalar

Per-unit field voltage to apply to the field circuit of the synchronous machine, returned as a
scalar.

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
- name: Regulator output gain, K_A (pu)
  summary: Regulator gain 300 (default) | positive number
  group: Control
- name: Regulator output time constant, T_A (s)
  summary: Regulator time constant 0.015 (default) | positive number
  group: Control
- name: Regulator denominator (lag) time constant, T_B (s)
  summary: Regulator lag time constant 10 (default) | positive number
  group: Control
- name: Regulator numerator (lead) time constant, T_C (s)
  summary: Regulator lead time constant 1 (default) | positive number
  group: Control
- name: Maximum regulator output, V_Rmax (pu)
  summary: Upper limit of the regulator output 5.64 (default) | real number
  group: Control
- name: Minimum regulator output, V_Rmin (pu)
  summary: Lower limit of the regulator output -4.53 (default) | real number
  group: Control
- name: Voltage regulator input (voltage error) maximum limit, V_Imax (pu)
  summary: Maximum limit of the voltage error 10 (default) | real number
  group: Control
- name: Voltage regulator input (voltage error) minimum limit, V_Imin (pu)
  summary: Minimum limit of the voltage error -10 (default) | real number
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
- name: Rectifier loading factor proportional to commutating reactance, K_C (pu)
  summary: Rectifier loading factor 0 (default) | positive number
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

### **Regulator output gain, K\_A (pu)** — Regulator gain `300` (default) | positive number

Gain associated with the voltage regulator.

### **Regulator output time constant, T\_A (s)** — Regulator time constant `0.015` (default) | positive number

Major time constant of the voltage regulator.

### **Regulator denominator (lag) time constant, T\_B (s)** — Regulator lag time constant `10` (default) | positive number

Equivalent lag time constant in the voltage regulator. Set this
parameter to `0` when the additional lag dynamics are
negligible.

### **Regulator numerator (lead) time constant, T\_C (s)** — Regulator lead time constant `1` (default) | positive number

Equivalent lead time constant in the voltage regulator. Set this parameter to
`0` when the additional lead dynamics are
negligible.

### **Maximum regulator output, V\_Rmax (pu)** — Upper limit of the regulator output `5.64` (default) | real number

Maximum per-unit output voltage of the regulator.

### **Minimum regulator output, V\_Rmin (pu)** — Lower limit of the regulator output `-4.53` (default) | real number

Minimum per-unit output voltage of the regulator.

### **Voltage regulator input (voltage error) maximum limit, V\_Imax (pu)** — Maximum limit of the voltage error `10` (default) | real number

Maximum per-unit limit of the voltage regulator input.

### **Voltage regulator input (voltage error) minimum limit, V\_Imin (pu)** — Minimum limit of the voltage error `-10` (default) | real number

Minimum per-unit limit of the voltage regulator input.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the overexcitation limiter input.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the underexcitation limiter input.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point` | `Take-over`

Location of the stator current limiter input:

- If you select `Summation point`,
  use the **V\_SCLsum** input port.
- If you select `Take-over`, use
  the **V\_OELscl** and
  **V\_UELscl** input ports.

### Exciter

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0` (default) | positive number

Rectifier loading factor proportional to the commutating reactance.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time synchronous machine AC4C excitation system including an automatic voltage regulator and an exciter

The SM AC4C block implements a synchronous machine type AC4C excitation
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

The SM AC4C block is made up of four major components:

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

This diagram shows the overall structure of the AC4C excitation system
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

Contrary to the other AC excitation models, the SM AC4C
block includes a full thyristor bridge that models the exciter output circuit and a
voltage regulator that controls the firing of the thyristor bridges. Rather than
having a rate feedback, the excitation system stabilization is implemented through a
lead-lag network and low-pass filter.

In the diagram:

- The Summation Point Logic subsystem models the summation point input
  location for the overexcitation limiter (OEL), underexcitation limiter
  (UEL), and stator current limiter (SCL) voltages. For more information
  about using limiters with this block, see Field Current Limiters.
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
  *VRmin* and
  *VRmax*,
  respectively.
- The bottom part of the diagram models the *Ifd*-based
  limitations.
- The **initialOffset** Constant block ensures the
  simulation can start from a steady state. The SM AC4C block
  calculates this value by using the maximum and minimum regulator output
  values, the regulator output gain, the rectifier loading factor
  proportional to the commutating reactance, and the initial field
  voltage.

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
input, *VOELscl*, and the underexcitation
input, *VUELscl*.
