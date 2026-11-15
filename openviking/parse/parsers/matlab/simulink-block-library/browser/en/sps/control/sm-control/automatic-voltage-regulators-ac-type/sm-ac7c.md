---
type: simulink-block
title: 'SM AC7C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — AC Type'
documentation_page: 'smac7c'
documentation_source_path: 'ref/smac7c.html'
language: en
---

# SM AC7C

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

### **Voltage regulator proportional gain, K\_PR (pu)** — Proportional gain of the voltage regulator `40` (default)

Per-unit proportional gain of the voltage regulator.

### **Voltage regulator integral gain, K\_IR (pu/s)** — Integral gain of the voltage regulator `5.6` (default)

Per-unit integral gain of the voltage regulator.

### **Voltage regulator derivative gain, K\_DR (pu.s)** — Derivative gain of the voltage regulator `0` (default)

Derivative gain of the voltage regulator.

### **Lag time constant for derivative channel of PID controller, T\_DR (s)** — Lag time constant for PID derivative channel `1` (default) | positive number

Equivalent lag time constant for the derivative channel of the PID
controller.

### **Maximum regulator output, V\_Rmax (pu)** — Upper limit of the regulator output `3.2` (default) | real number

Maximum per-unit output voltage of the regulator.

### **Minimum regulator output, V\_Rmin (pu)** — Lower limit of the regulator output `-3.2` (default) | real number

Minimum per-unit output voltage of the regulator.

### **Field current regulator proportional gain, K\_PA (pu)** — Proportional gain of the field current regulator `112` (default) | real number

Per-unit proportional gain associated with the field current
regulator.

### **Field current regulator integral gain, K\_IA (pu/s)** — Integral gain of the field current regulator `0` (default) | real number

Per-unit integral gain associated with the field current
regulator.

### **Maximum field current regulator output, V\_Amax (pu)** — Maximum field current regulator output `65.2` (default) | real number

Maximum per-unit field current regulator output.

### **Minimum field current regulator output, V\_Amin (pu)** — Minimum field current regulator output `-54` (default) | real number

Minimum per-unit field current regulator output.

### **Generator field voltage feedback gain, K\_F1 (pu)** — Generator field voltage feedback gain `0` (default) | real number

Per-unit field voltage feedback gain associated with the generator.

### **Exciter field current feedback gain, K\_F2 (pu)** — Exciter field current feedback gain `0.08` (default) | real number

Per-unit field current feedback gain associated with the exciter.

### **Rate feedback gain, K\_F3 (pu)** — Rate feedback gain `0.01` (default) | real number

Per-unit rate feedback block gain.

### **Rate feedback time constant, T\_F (s)** — Rate feedback time constant `1` (default) | positive number

Rate feedback block time constant for the stabilization of the excitation system.

### **Alternate PSS input locations (V\_S)** — PSS input location `Voltage error calculation` (default) | `After take-over UEL`

Location of the power system stabilizer input.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Unused` (default) | `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output` | `Take-over at output of inner loop regulator`

Location of the overexcitation limiter input:

- If you select `Summation point at voltage
  error`, **V\_OEL** is an
  input of the **Summation Point Logic**
  subsystem.
- If you select `Take-over at voltage
  error`, **V\_OEL** is an
  input of the **Take-over Logic**
  subsystem.
- If you select `Take-over at voltage regulator
  output`, **V\_OEL** is an
  input of the **Take-over Logic 1**
  subsystem.
- If you select `Take-over at output of inner
  loop regulator`, **V\_OEL**
  is an input of the **Take-over Logic 2**
  subsystem.

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Unused` (default) | `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

Location of the underexcitation limiter input:

- If you select `Summation point at voltage
  error`, **V\_UEL** is an
  input of the **Summation Point Logic**
  subsystem.
- If you select `Take-over at voltage
  error`, **V\_UEL** is an
  input of the **Take-over Logic**
  subsystem.
- If you select `Take-over at voltage regulator
  output`, **V\_UEL** is an
  input of the **Take-over Logic 1**
  subsystem.

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Unused` (default) | `Summation point at voltage error` | `Take-over at voltage error` | `Take-over at voltage regulator output`

Loction of the stator current limiter input:

- If you select `Summation point`,
  use the **V\_SCLsum** input port.
- If you select any of the
  `Take-over` options, use the
  **V\_OELscl** and
  **V\_UELscl** input ports.

### Exciter

### **Exciter field proportional constant, K\_E (pu)** — Exciter field gain `1` (default) | positive number

Proportional constant for the exciter field.

### **Exciter field time constant, T\_E (s)** — Exciter field time constant `1.2` (default) | positive number

Time constant for the exciter field.

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.12` (default) | positive number

Rectifier loading factor proportional to the commutating reactance.

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — Demagnetization factor `3.3` (default) | positive number

Demagnetization factor related to the exciter alternator reactances.

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — First saturation output voltage `13.6` (default) | positive number

Exciter output voltage for the first saturation factor.

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — First saturation lookup voltage `3.74` (default) | positive number

Saturation factor for the first exciter.

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — Second saturation output voltage `10.2` (default) | positive number

Exciter output voltage for the second saturation factor.

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — Second saturation lookup voltage `0.32` (default) | positive number

Saturation factor for the second exciter.

### **Maximum exciter field current limit reference, V\_FEmax (pu)** — Exciter upper limit `23.2` (default) | real number

Maximum per-unit field current limit reference.

### **Minimum exciter voltage output, V\_Emin (pu)** — Exciter lower limit `0` (default) | real number

Minimum per-unit exciter voltage output.

### **Potential circuit gain coefficient, K\_P (pu)** — Potential circuit gain coefficient `1` (default) | real number

Per-unit potential circuit gain coefficient.

#### Dependencies

This parameter is visible only when you set the **Power
source selector SW1** parameter to
`Position A: power source derived from terminal
voltage` and the **Power source selector
SW2** parameter to `Position A: use
variable V_B`.

### **Potential circuit phase angle (degrees)** — Potential circuit phase angle `0` (default) | real number

Potential circuit phase angle, in degrees.

#### Dependencies

To enable this parameter, set **Power source selector SW1** to
`Position A: power source derived from terminal
voltage` and **Power source selector
SW2** to `Position A: use variable
V_B`.

### **Potential circuit (current) gain coefficient, K\_I (pu)** — Potential circuit current gain coefficient `0` (default) | real number

Per-unit potential circuit current gain coefficient.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from terminal voltage` and **Power source
selector SW2** to `Position A: use variable
V_B`.

### **Reactance associated with potential source, X\_L (pu)** — Reactance associated with potential source `0` (default) | real number

Per-unit reactance associated with the potential source.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from terminal voltage` and **Power source
selector SW2** to `Position A: use variable
V_B`.

### **Gain related to regulator and alternator field power supply, K\_R (pu)** — Gain related to regulator and alternator field power supply `0` (default) | real number

Per-unit gain related to the regulator and alternator field power supply.

#### Dependencies

To enable this parameter, set **Power source selector SW2** to
`Position B: do not use variable
V_B`.

### **Gain related to negative exciter field current capability, K\_L (pu)** — Gain related to negative exciter field current capability `0` (default) | real number

Per-unit gain related to the negative exciter field current capability.

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — Loading factor of rectifier proportional to commutating reactance `0` (default) | real number

*Since R2024b*

Per-unit loading factor of the rectifier, proportional to the
commutating reactance.

#### Dependencies

To enable this parameter, set **Power source selector
SW2** to `Position A: use variable
V_B`.

### **Maximum available exciter field voltage, V\_Bmax (pu)** — Maximum available field voltage of exciter `999` (default) | real number

*Since R2024b*

Maximum per-unit available field voltage of the exciter.

#### Dependencies

To enable this parameter, set **Power source selector
SW2** to `Position A: use variable
V_B`.

### **Power source selector SW1** — Power source selector `Position A: power source derived from terminal voltage` (default) | `Position B: power source independent of terminal conditions`

Position of the power source selector SW1.

#### Dependencies

To enable this parameter, set **Power source selector SW2** to
`Position A: use variable V_B`.

### **Power source selector SW2** — Power source selector `Position A: use variable V_B` (default) | `Position B: do not use variable V_B`

Position of the power source selector SW2.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time synchronous machine AC7C excitation system including an automatic voltage regulator and an exciter

The SM AC7C block implements a synchronous machine type AC7C excitation
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

The SM AC7C block is made up of five major components:

- The Current Compensator modifies the measured terminal voltage as a
  function of the terminal current.
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
- The Power Source and Self-excitation models the power source for the
  controlled rectifier when it is independent from the terminal voltage. It
  also allows the representation of self-excitation for the exciter.

This diagram shows the overall structure of the AC7C excitation system
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
- *SW1* and
  *SW2* are the user-selected
  power source switches for the controlled rectifier.
- *VB* is the exciter field
  voltage.
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
  (UEL), stator current limiter (SCL), and the power switch selector (V\_S)
  voltages. For more information about using limiters with this block, see
  Field Current Limiters.
- There are three Take-over Logic subsystems. They model the take-over
  point input locations for the OEL, UEL, SCL and PSS voltages. For more
  information about using limiters with this block, see Field Current Limiters.
- The PID\_R subsystem models a PID controller that functions as a
  control structure for the automatic voltage regulator. The minimum and
  maximum anti-windup saturation limits for the block are
  *VRmin* and
  *VRmax*,
  respectively.
- The PI\_R subsystem models a PI controller that functions as a control
  structure for the field current regulator. The minimum and maximum
  anti-windup saturation limits for the block are
  *VAmin* and
  *VAmax*,
  respectively.
- In case of self-excitation, with a nonzero
  *KR* and the
  **Power source selector SW2** parameter set to
  `Position B: do not use variable V_B`, the
  voltage regulator power is derived from the exciter output voltage. The
  voltage regulator command signal is multiplied by the exciter output
  voltage, *EFD*, times
  *KR*. For more
  information about the user-selected logical switches for the power
  source of the controlled rectifier, see Power Source and Self-Excitation.
- *KF1* and
  *KF2* model a
  high-bandwidth regulator inner loop that regulates the generator field
  or exciting current.
- The Filtered Derivative block models the rate feedback path for
  the stabilization of the excitation system if the automatic voltage
  regulator does not have a derivative term. Here,
  *KF3* and
  *TF* are the gain and
  time constants of this system, respectively. Refer to the documentation
  for the Filtered Derivative block for the discrete and continuous
  implementations.
- *-K\_L\*VFE* and
  *inf* are the minimum and maximum saturation limits
  for the output exciter field voltage
  *EFE*.
- The **initialOffset1** Constant block ensures the
  simulation can start from a steady state. The SM AC7C block
  calculates this value by using saturation and exciter parameters,
  including the exciter field current feedback gain, the generator field
  voltage feedback gain, and the initial field voltage.

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

### Power Source and Self-Excitation

It is possible to use different power source representations for the controlled rectifier
by selecting the relevant option in the **Power source selector
SW1** parameter. The power source for the controlled rectifier can be
either derived from the terminal voltage (`Position A: power source
derived from terminal voltage`) or it can be independent of the
terminal voltage (`Position B: power source independent from the
terminal conditions`). Note that this switch is dependent on the
state of the second logical switch.

The second logical switch, **Power source selector SW2**, determines
whether the exciter employs self-excitation or not. The exciter is self-excited if
the **Power source selector SW2** parameter is set to
`Position B: do not use variable V_B`, as the model
parameters associated with the variable *VB*
do not impact the simulation.
