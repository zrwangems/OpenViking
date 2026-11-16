---
type: simulink-block
title: 'SM DC2C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smdc2c'
documentation_source_path: 'ref/smdc2c.html'
language: en
---

# SM DC2C

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

### **V\_OELscl** — Take-over stator current limit (OEL) scalar

Input from the stator current limiter to prevent field overexcitation when using the
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

### **V\_UELscl** — Take-over stator current limit (UEL) scalar

Input from the stator current limiter to prevent field underexcitation when using the
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
### Output

### **Efd\_pu** — Field voltage scalar

Per-unit field voltage to be applied to the field circuit of the synchronous machine,
returned as a scalar.

**Data Types:** `single` | `double`

## Parameters

### General

### **Initial field voltage, Efd0 (pu)** — Initial output voltage `1` (default) | real number

Initial per-unit voltage to be applied to the field circuit of the synchronous
machine.

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

Resistance used in the current compensation system. Set this and
**Reactance component of load compensation, X\_C
(pu)** to `0` to disable current
compensation.

### **Reactance component of load compensation, X\_C (pu)** — Compensation reactance `0` (default) | positive number

Reactance used in the current compensation system. Set this and
**Resistive component of load compensation, R\_C
(pu)** to `0` to disable current
compensation.

### **Regulator input filter time constant, T\_R (s)** — Regulator time constant `0` (default) | positive number

Equivalent time constant for the voltage transducer filtering.

### Control

### **Regulator output gain, K\_A (pu)** — Regulator gain `300` (default) | positive number

Gain associated with the voltage regulator.

### **Regulator time constant, T\_A (s)** — Regulator time constant `0.01` (default) | positive number

Major time constant of the voltage regulator.

### **Regulator denominator (lag) time constant, T\_B (s)** — Regulator lag time constant `0` (default) | positive number

Equivalent lag time constant in the voltage regulator. Set this to
`0` when the additional lag dynamics are
negligible.

### **Regulator numerator (lead) time constant, T\_C (s)** — Regulator lead time constant `0` (default) | positive number

Equivalent lead time constant in the voltage regulator. Set this to
`0` when the additional lead dynamics are
negligible.

### **Rate feedback gain, K\_F (pu)** — Rate feedback gain `0.02` (default) | positive number

Rate feedback block gain for the stabilization of the excitation system.

### **Rate feedback time constant, T\_F (s)** — Rate feedback time constant `0.675` (default) | positive number

Rate feedback block time constant for the stabilization of the excitation system.

### **Maximum controller output, V\_Rmax (pu)** — Controller output upper limit `4.95` (default) | real number

Maximum per-unit output voltage of the controller.

### **Minimum controller output, V\_Rmin (pu)** — Controller output lower limit `-4.90` (default) | real number

Minimum per-unit output voltage of the controller.

### **Alternate OEL input locations (V\_OEL)** — Overexcitation limiter input location `Unused` (default) | `Summation point` | `Take-over`

Select the overexcitation limiter input location.

### **Alternate UEL input locations (V\_UEL)** — Underexcitation limiter input location `Unused` (default) | `Summation point` | `Take-over`

Select the underexcitation limiter input location.

### **Alternate SCL input locations (V\_SCL)** — Stator current limiter input location `Unused` (default) | `Summation point` | `Take-over`

Select stator current limiter input location. To specify the SCL input:

- If you select `Summation point`,
  use the **V\_SCLsum** input port.
- If you select `Take-over`, use
  the **V\_OELscl** and
  **V\_UELscl** input ports.

### Exciter

### **Exciter field proportional constant, K\_E (pu)** — Exciter field gain `1` (default) | positive number

Proportional constant for exciter field.

### **Exciter field time constant, T\_E (s)** — Exciter field time constant `1.33` (default) | positive number

Time constant for exciter field.

### **Lower limit, E\_FDmin (pu)** — Field voltage lower limit `-99` (default) | positive number

Lower limit for the field voltage.

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — First saturation output voltage `3.05` (default) | positive number

Exciter output voltage for first saturation factor.

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — First saturation lookup voltage `0.279` (default) | positive number

First exciter saturation factor.

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — Second saturation output voltage `2.29` (default) | positive number

Exciter output voltage for second saturation factor.

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — Second saturation lookup voltage `0.117` (default) | positive number

Second exciter saturation factor.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time synchronous machine DC2C excitation system including an automatic voltage regulator and an exciter

The SM DC2C block models a synchronous machine type DC2C excitation system
that conforms to IEEE 421.5-2016[1].

Use this block to model the control and regulation of the field voltage of a synchronous
machine that operates as a generator using a DC commutator rotating exciter.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

The SM DC2C block is made up of four major components:

- The current compensator modifies the measured terminal voltage as a
  function of terminal current.
- The voltage measurement transducer simulates the dynamics of a terminal
  voltage transducer by using a low-pass filter.
- The excitation control elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error. This
  voltage error is then passed through a voltage regulator to produce the
  exciter field voltage.
- The DC rotating exciter models the DC commutator rotating exciter and
  produces a field voltage that is applied to the controlled synchronous
  machine. The block also feeds the field voltage back to the excitation
  system.

This diagram shows the overall structure of the DC2C excitation system
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
- *EFE* is the exciter field
  voltage.
- *EFD* is the field voltage.

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
*TR*. Refer to the documentation for
this block for the exact discrete and continuous implementations.

### Excitation Control Elements

This diagram illustrates the overall structure of the excitation control elements:

In the diagram:

- The Summation Point Logic subsystem models the summation point input
  location for the overexcitation limiter (OEL), underexcitation limiter
  (UEL), and stator current limiter (SCL) voltages. For more information
  about using limiters with this block, see Field Current Limiters.
- The Lead-Lag block models additional dynamics associated with
  the voltage regulator. Here,
  *TC* is the lead time
  constant and *TB* is the lag
  time constant. Refer to the Lead-Lag block documentation for the exact
  discrete and continuous implementations.
- The Low-Pass Filter block models the major dynamics of the
  voltage regulator. Here, *KA* is
  the regulator gain and *TA* is
  the major time constant of the regulator. The minimum and maximum
  anti-windup saturation limits for the block are
  *VRmin* and
  *VRmax*,
  respectively.
- The Take-over Logic subsystem models the take-over point input
  location for the OEL, UEL, and SCL voltages. For more information about
  using limiters with this block, see Field Current Limiters.
- The Filtered Derivative block models the rate feedback path for
  stabilization of the excitation system. Here,
  *KF* and
  *TF* are the gain and
  time constant of this system, respectively. Refer to the documentation
  for the Filtered Derivative block for the exact discrete and continuous
  implementations.
- *VT\*VRmax*
  and
  *VT\*VRmin*
  are the minimum and maximum saturation limits for the output exciter
  field voltage *EFE*.

### Field Current Limiters

You can use various field current limiters to modify the output of the voltage
regulator under unsafe operating conditions:

- Use an overexcitation limiter to prevent overheating of the field
  winding due to excessive field current demand.
- Use an underexcitation limiter to boost field excitation when it is
  too low, which can risk desynchronization.
- Use a stator current limiter to prevent overheating of the stator
  windings due to excessive current.

Attach the output of any of these limiters at one of these points:

- The summation point as part of the automatic voltage regulator (AVR)
  feedback loop
- The take-over point to override the usual behavior of the AVR

If you are using the stator current limiter at the summation point,
use the single input *VSCLsum*. If you are
using the stator current limiter at the take-over point, use both an overexcitation
input *VOELscl* and an underexcitation input
*VUELscl*.

### DC Rotating Exciter

This diagram illustrates the overall structure of the DC commutator rotating exciter:

In the diagram:

- The exciter field current *VFE* is modeled as the summation of two signals:

  - The nonlinear function *Vx* models the saturation of the exciter output voltage.
  - The proportional term *KE* models the linear relationship between exciter output voltage and the exciter field current.
- The **Integrator** subsystem integrates the difference
  between *EFE* and
  *VFE* to generate the output
  field voltage *Efd*.
  *TE* is the time constant for
  this process.
