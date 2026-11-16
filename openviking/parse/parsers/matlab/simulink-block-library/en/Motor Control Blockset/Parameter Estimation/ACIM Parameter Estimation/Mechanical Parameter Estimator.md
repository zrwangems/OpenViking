---
type: simulink-block
title: 'ACIM Mechanical Parameter Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'acimmechanicalparameterestimator'
documentation_source_path: 'ref/acimmechanicalparameterestimator.html'
language: en
---

# ACIM Mechanical Parameter Estimator

## Ports

### Input

### **Iabc** — Three-phase current response scalar

The three-phase current response of the motor measured by the current
sensors.

**Note**

Providing phase-*c* current input is optional. The block
functionality is not impacted if you do not provide the phase-*c*
current input.

**Data Types:** `single`

### **Vdc** — DC link voltage scalar

DC bus voltage that you provide to the inverter.

**Data Types:** `single`

### **Speed** — Rotor speed scalar

Current motor speed.

**Data Types:** `single`

### **Id0** — Estimated magnetizing current scalar

Estimated magnetizing current of the induction motor. You can either connect this
input port to the `Id0` output of the Id0 Estimator
block or provide the magnetizing current value manually using a
Constant block.

**Data Types:** `single`

### **Rtotal** — Sum of stator and inverter-board resistances scalar

Sum of estimated stator resistance *Rs*
and inverter board resistance. You can either provide this input by utilizing the
`Rs` output of the ACIM Rs Estimator block or
provide this value manually using a Constant block.

**Data Types:** `single`

### **Rr** — Estimated rotor resistance scalar

Estimated rotor resistance of the induction motor. You can either connect this
input port to the `Rr` output of the RrL Estimator
block or provide the rotor resistance value manually using a Constant
block.

**Data Types:** `single`

### **Lm** — Estimated magnetizing inductance scalar

Estimated magnetizing inductance of the induction motor. You can either connect
this input port to the `Lm` output of the RrL
Estimator block or provide the magnetizing inductance value manually using a
Constant block.

**Data Types:** `single`

### **Lls** — Estimated stator leakage inductance scalar

Estimated stator leakage inductance of the induction motor. You can either connect
this input port to the `Lls` output of the RrL
Estimator block or provide the stator leakage inductance value manually
using a Constant block.

**Data Types:** `single`

### **StartStop** — Control signal for mechanical parameter estimation logical

Signal that either starts or stops block execution:

- `1` (rising edge of a pulse) — This signal initiates block
  execution.
- `0` (falling edge of a pulse) — This signal immediately stops
  block execution and any tests that the block is running. If you interrupt the
  estimation process abruptly before completion, the block does not compute or
  output the mechanical parameter values.

**Data Types:** `Boolean`

### **Config** — Bus signal input bus

This table summarizes the expected configuration elements in the bus signal
input.

| Category | Configuration element | | | Units |
| --- | --- | --- | --- | --- |
| Elements for motor and inverter hardware | Number of pole pairs | | | - |
| Rated frequency | | | Hz |
| Nominal motor current | | | A |
| Nominal voltage | | | V |
| Maximum measurable inverter current | | | A |
| Board resistance | | | ohm |
| Current sense gain | | | A/ADC Count |
| Voltage sense gain | | | V/ADC Count |
| Elements for estimating magnetizing current *Id0* | Measurement time | | | seconds |
| Open-loop ramp time | | | seconds |
| Elements for estimating motor resistance (*Rs*) | Estimation time | | | seconds |
| *Vd* reference voltage 1 | | | PU voltage |
| *Vd* reference voltage 2 | | | PU voltage |
| Elements for estimating rotor resistance (*Rr*), magnetizing inductance (*Lm*), stator leakage inductance (*Lls*), and rotor leakage inductance (*Llr*) | Frequency 1 as a ratio of rated frequency | | | PU frequency |
| Frequency 2 as a ratio of rated frequency | | | PU frequency |
| High frequency for *Lm* | | | Hz |
| Start voltage for voltage sweep | | | PU voltage |
| Voltage step for voltage sweep | | | PU voltage |
| High-frequency injection voltage | | | PU voltage |
| Elements for estimating motor inertia (*J*) and friction constant (*B*) | Closed-loop speed duration | | | seconds |
| Closed-loop speed | | | RPM |
| *Iq* Reference current for FOC | | | PU current |
| Proportional gain | | | - |
| Integral gain | | | - |
| Lower speed limit for inertia estimation | | | RPM |
| - | Parameter estimation sample time | | | seconds |

You can connect this input port to the `Config` output port of
the ACIM Parameter Estimation Configurator block.

**Data Types:** `single`
### Output

### **Vabc** — *a*, *b*, and *c*-axis stator reference voltage components scalar

Stator reference voltage components along the *a*,
*b*, and *c* axes of the *abc*
reference frame.

**Data Types:** `single`

### **J** — Estimated rotor inertia scalar

Estimated inertia of the induction motor (in
kg.m2).

**Data Types:** `single`

### **B** — Estimated viscous damping scalar

Estimated viscous damping of the induction motor (in N.s/m).

**Data Types:** `single`

### **InverterEn** — Inverter control signal logical

Signal that switches on or switches off the inverter:

- `1` (logical high) — For the duration when this signal is
  high, all six switches of the inverter are switched on.
- `0` (logical low) — For the duration when this signal is low,
  all six switches of the inverter are switched off.

**Data Types:** `single`

### **Log** — Debug signals bus

Debug signals that the block provides for examination. The bus includes these
debug signals.

| Debug signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| *status* | | `0` | Did not complete mechanical parameter estimation | - |
| `1` | Mechanical parameter estimation completed successfully | - |
| *CoastDownTime* | | | Measured coast-down duration | seconds |
| *Vdq* | | | Voltages across *d* and *q* axes | Volts |
| *Idq* | | | Currents across *d* and *q* axes | Amperes |
| *VIAlphaBeta* | | | Voltages and currents across *α* and *β* axes | Volts, Amperes |
| *SlipPU* | | | Slip in speed (in per-units) during closed-loop operation of motor | - |

**Data Types:** `single`

## Parameters

Not documented in R2025b.

## Libraries

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Estimate rotor inertia and viscous damping of AC induction motor (ACIM)

The ACIM Mechanical Parameter Estimator block uses the phase currents and
voltages, DC voltage across the motor, motor speed, magnetizing current, rotor and complete
motor resistances, magnetizing and stator leakage inductances, as well as the other test
configuration elements to compute the following mechanical parameters of an induction
motor:

- Rotor inertia (*J*)
- Viscous damping (*B*)

The block runs the motor using closed-loop field-oriented control (FOC) with a limited
speed. While running the motor, the block also runs the tests to estimate viscous damping
(*B*). After a preconfigured duration, the block concludes these tests to
compute *B*, and then triggers coast-down by shutting down all six inverter
switches. The coast-down results in a gradual decline in the motor speed, which eventually
reaches zero. The block measures the time taken by the motor to reach a speed of zero and uses
it to calculate the rotor inertia (*J*).
