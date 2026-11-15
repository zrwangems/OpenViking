---
type: simulink-block
title: 'SM AC11C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — AC Type'
documentation_page: 'smac11c'
documentation_source_path: 'ref/smac11c.html'
language: en
---

# SM AC11C

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
  `Summation point`.
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

### General

### **Initial field voltage, Efd0 (pu)** — Initial output voltage `1` (default) | real scalar

Initial per-unit voltage to apply to the field circuit of the
synchronous machine.

### **Initial terminal voltage, Vt0 (pu)** — Initial terminal voltage `1` (default) | real scalar

Initial per-unit voltage to apply to the terminal.

#### Dependencies

To enable this parameter, in the Exciter section, set
**Power source selector SW1** to
`Position A: power source derived from terminal
voltage`.

### **Initial terminal current, It0 (pu)** — Initial terminal current `1` (default) | real scalar

Initial per-unit current to apply to the terminal.

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

### **Voltage regulator proportional gain, K\_PA (pu)** — Proportional gain of voltage regulator `30` (default)

Per-unit proportional gain of the voltage regulator.

### **Voltage regulator integral time constant, T\_IA (s)** — Integral time constant of voltage regulator `2` (default)

Integral time constant of the voltage regulator, in seconds.

### **UEL regulator proportional gain, K\_PU (pu)** — Proportional gain of UEL regulator `30` (default)

Per-unit proportional gain of the UEL regulator.

### **UEL regulator integral time constant, T\_IU (s)** — Integral time constant of UEL regulator `2` (default)

Integral time constant of the UEL regulator, in seconds.

### **Voltage and UEL regulator derivative gain, K\_B (pu)** — Derivative gain of voltage and UEL regulator `3` (default)

Per-unit derivative gain for both the voltage regulator and the UEL
regulator.

### **Time constant for derivative element, T\_B (s)** — Time constant for derivative element `0.4` (default)

Time constant for the derivative element, in seconds.

### **OEL regulator proportional gain, K\_PO (pu)** — Proportional gain of OEL regulator `30` (default)

Per-unit proportional gain of the OEL regulator.

### **OEL regulator integral time constant, T\_IO (s)** — Integral time constant of OEL regulator `2` (default)

Integral time constant of the OEL regulator, in seconds.

### **Maximum regulator output, V\_Rmax (pu)** — Maximum regulator output `20` (default) | real scalar

Maximum per-unit regulator output.

### **Minimum regulator output, V\_Rmin (pu)** — Minimum regulator output `-20` (default) | real scalar

Minimum per-unit regulator output.

### **Maximum PSS regulator output, V\_RSmax (pu)** — Maximum PSS regulator output `3` (default) | real scalar

Maximum per-unit output of the power system stabilizer
regulator.

### **Minimum PSS regulator output, V\_RSmin (pu)** — Minimum PSS regulator output `-3` (default) | real scalar

Minimum per-unit output of the power system stabilizer
regulator.

### **Maximum exciter output, V\_Amax (pu)** — Maximum exciter output `20` (default) | real scalar

Maximum per-unit output of the excitation system.

### **Minimum exciter output, V\_Amin (pu)** — Minimum exciter output `0` (default) | real scalar

Minimum per-unit output of the excitation system.

### **Alternate PSS input locations (V\_S)** — PSS input location `Output of AVR (after take-over limits)` (default) | `Voltage error calculation` | `Voltage error or after take-over limits`

Location of the power system stabilizer input.

### **Alternate OEL input locations (V\_OEL)** — OEL input location `Take-over at voltage error` (default) | `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

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

### **Alternate UEL input locations (V\_UEL)** — UEL input location `Take-over at voltage error` (default) | `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

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

### **Alternate SCL input locations (V\_SCL)** — SCL input location `Take-over at voltage error` (default) | `Unused` | `Summation point at voltage error` | `Take-over at voltage regulator output`

Location of the stator current limiter input, specified as one of these options:

- `Summation point` — Use the
  **V\_SCLsum** input port.
- Any of the `Take-over` options —
  Use the **V\_OELscl** and
  **V\_UELscl** input ports.

### Exciter

### **Exciter field proportional constant, K\_E (pu)** — Exciter field gain `1` (default) | positive scalar

Proportional constant for the exciter field.

### **Exciter field time constant, T\_E (s)** — Exciter field time constant `0.4` (default) | positive scalar

Time constant for the exciter field.

### **Rectifier loading factor proportional to commutating reactance, K\_C (pu)** — Rectifier loading factor `0.173` (default) | positive scalar

Rectifier loading factor. This value is proportional to the commutating
reactance.

### **Demagnetizing factor, function of exciter alternator reactances, K\_D (pu)** — Demagnetization factor `1` (default) | positive scalar

Demagnetization factor related to the exciter alternator
reactances.

### **Exciter output voltage for saturation factor S\_E(E\_1), E\_1 (pu)** — First saturation output voltage `7.4` (default) | positive scalar

Exciter output voltage for the first saturation factor.

### **Exciter saturation factor at exciter output voltage E\_1, S\_E(E\_1) (1)** — First saturation lookup voltage `0.214` (default) | positive scalar

Saturation factor for the first exciter.

### **Exciter output voltage for saturation factor S\_E(E\_2), E\_2 (pu)** — Second saturation output voltage `5.55` (default) | positive scalar

Exciter output voltage for the second saturation factor.

### **Exciter saturation factor at exciter output voltage E\_2, S\_E(E\_2) (1)** — Second saturation lookup voltage `0.044` (default) | positive scalar

Saturation factor for the second exciter.

### **Maximum exciter field current, V\_FEmax (pu)** — Exciter upper limit `20` (default) | real scalar

Maximum per-unit field current limit reference.

### **Minimum exciter output limit, V\_Emin (pu)** — Exciter lower limit `0` (default) | real scalar

Minimum per-unit exciter voltage output.

### **Potential circuit (voltage) gain coefficient, K\_P (pu)** — Potential circuit gain coefficient `1` (default) | real scalar

Per-unit potential circuit gain coefficient.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from terminal voltage`.

### **Potential circuit phase angle (degrees)** — Potential circuit phase angle `0` (default) | real scalar

Potential circuit phase angle, in degrees.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from terminal voltage`.

### **Potential circuit (current) gain coefficient, K\_I (pu)** — Potential circuit current gain coefficient `0` (default) | real scalar

Per-unit potential circuit current gain coefficient.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from terminal voltage`.

### **Reactance associated with potential source, X\_L (pu)** — Reactance associated with potential source `0` (default) | real scalar

Per-unit reactance associated with the potential source.

#### Dependencies

To enable this parameter, set **Power source selector
SW1** to `Position A: power source derived
from terminal voltage`.

### **Rectifier loading factor proportional to commutating reactance, K\_C1 (pu)** — Rectifier loading factor proportional to commutating reactance `0` (default) | real scalar

Per-unit loading factor of the rectifier. This value is proportional to the commutating
reactance.

### **Power source selector SW1** — Power source selector `Position B: power source independent of the terminal conditions` (default) | `Position A: power source derived from terminal voltage`

Position of the power source selector SW1.

### **Maximum available exciter voltage, V\_B1max (pu)** — Maximum available exciter field voltage `1.5` (default) | real scalar

Maximum per-unit available field voltage for the exciter.

### **Rectifier loading factor proportional to commutating reactance, K\_C2 (pu)** — Rectifier loading factor proportional to commutating reactance `0` (default) | real scalar

Per-unit loading factor of the rectifier. This value is proportional to the commutating
reactance, derived from the generator terminal current through a
separate series diode bridge.

### **Additive potential circuit (current) gain coefficient, K\_I2 (pu)** — Additive circuit current gain coefficient `0` (default) | real scalar

Per-unit additive circuit current gain coefficient derived from the generator terminal
current through a separate series diode bridge. Set this parameter to
`0` to disable the separate additive power source
completely.

### **Maximum available exciter voltage, V\_B2max (pu)** — Maximum available exciter voltage `0` (default) | real scalar

Maximum per-unit available field voltage for the exciter, derived from the generator
terminal current through a separate series diode bridge.

### **Additive independent source, K\_BOOST (pu)** — Additive independent source `0` (default)

Per-unit additive independent source for the boost circuit.

### **Reference value for applying additive (boost) circuit, V\_BOOST (pu)** — Reference value for applying boost circuit `0` (default)

Per-unit reference value for activating the additive boost circuit in
the excitation system.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Discrete-time or continuous-time synchronous machine AC11C excitation system including an automatic voltage regulator and an exciter

The SM AC11C block implements a synchronous machine type AC11C excitation
system model in conformance with IEEE Std 421.5-2016 [1].

Use this block to model the control and regulation of the field voltage of a
synchronous machine that operates as a generator using an AC rotating exciter.

Switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** parameter
to a positive scalar. To inherit the sample time from an upstream block, set the
**Sample time (-1 for inherited)** parameter to
`-1`.

The SM AC11C block comprises five major components:

- The Current Compensator component modifies the measured terminal voltage
  as a function of the terminal current.
- The Voltage Measurement Transducer component simulates the dynamics of a
  terminal voltage transducer using a low-pass filter.
- The Excitation Control Elements component compares the voltage transducer
  output with a terminal voltage reference to produce a voltage error value.
  The component then passes this value through a voltage regulator to produce
  the exciter field voltage.
- The AC Rotating Exciter component models the AC rotating exciter, which
  produces a field voltage that is applied to the controlled synchronous
  machine. The block also feeds the exciter field current
  (*VFE*) back to the
  excitation system.
- The Power Source component models the dependency of the power source for
  the controlled rectifier from the terminal voltage. The Power Source
  comprises multiple compound circuits. You can select this additive circuit
  as a boost circuit, that is applied when the faulted conditions in the
  system cause a drop in the terminal voltage of the generator. The SM
  AC11C block then releases the circuit when the generator voltage
  recovers.

This diagram shows the structure of the AC11C excitation system
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
- *SW1* is the power source switch
  that you specify for the controlled rectifier.
- *VB* is the exciter field
  voltage.
- *EFE* and
  *VFE* are the exciter field
  voltage and current, respectively.
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
- The SM AC11C block models the controller of the
  automatic voltage regulator by using three different PID controls. The
  activation of a specific limiter (UEL or OEL) immediately changes the
  transfer function of the automatic voltage regulator to the controller
  path which corresponds to the activated limiter. The SW\_UEL and SW\_OEL
  Switch blocks activate the appropriate control path when the
  *VUEL* and/or
  *VOEL* signals are
  connected to their respective alternate positions. The SW\_UEL and SW\_OEL
  Switch blocks are on position B when you set the **Alternate UEL
  input locations (V\_UEL)** and **Alternate OEL input
  locations (V\_OEL)** parameters to `Take-over at
  voltage error`.
- The **Power source selector SW1** parameter controls
  the origin of the power source for the controlled rectifier. The power
  source comprises a boost circuit that you can apply when the faulted
  conditions in the system cause a drop in the terminal voltage of the
  generator. The voltage regulator command signal
  *VR* is then summed to
  and/or multiplied by the exciter field voltages,
  *VB1* and
  *VB2*. For more
  information about the logical switch for the power source of the
  controlled rectifier, see Power Source and Boost Circuit.

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
*VOELscl*, and the underexcitation
input *VUELscl*.

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

### Power Source and Boost Circuit

You can use different power source representations for the controlled rectifier by
setting the **Power source selector SW1** parameter value. To
derive the power source for the controlled rectifier from the terminal voltage, set
the **Power source selector SW1** parameter to
`Position A: power source derived from terminal
voltage`. To specify that the power source is independent of the
terminal voltage, set the **Power source selector SW1** parameter
to `Position B: power source independent from the terminal
conditions`.

The power source section also contains an additive circuit that you can use as a
boost circuit. This additive circuit is applied when the faulted conditions in the
system cause a drop in the terminal voltage of the generator. The SW\_Boost Switch
block controls the logic associated with the boost circuit. If the terminal voltage,
*VT*, is greater than the value of
the **Reference value for applying additive (boost) circuit, V\_BOOST
(pu)** parameter, the switch is on position “A,” otherwise the switch
is on position “B.”

If you set the **Reference value for applying additive (boost) circuit,
V\_BOOST (pu)** parameter to a high value, the additive component is
always active.
