---
type: simulink-block
title: 'PMSM Mechanical Parameter Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Parameter Estimation'
documentation_page: 'pmsmmechanicalparameterestimator'
documentation_source_path: 'ref/pmsmmechanicalparameterestimator.html'
language: en
---

# PMSM Mechanical Parameter Estimator

## Ports

### Input

### **Iabc** — Three-phase current response vector

The three-phase current response (in amperes) of the motor measured by the current
sensors.

**Note**

Providing phase-*c* current input is optional. The block
functionality is not impacted if you do not provide the phase-*c*
current input.

**Data Types:** `single`

### **Vdc** — DC link voltage scalar

DC bus voltage (in volts) that you provide to the inverter.

**Data Types:** `single`

### **Theta** — Rotor position scalar

Current position (in per-unit) of the rotor. For more details about the per-unit
system, see Per-Unit System.

**Data Types:** `single`

### **Speed** — Rotor speed scalar

Current motor speed (in RPM).

**Data Types:** `single`

### **Rs** — Estimated stator resistance scalar

Estimated stator resistance (in ohms) of the PMSM. You can either connect this
input port to the `Rs` output of the PMSM Rs Estimator
block or provide the resistance value manually using a Constant
block.

**Data Types:** `single`

### **Ld** — Estimated *d*-axis stator inductance scalar

Estimated *d*-axis stator inductance (in henries) of the PMSM.
You can either connect this input port to the `Ld` output of the
Ld Estimator block or provide the *d*-axis
inductance value manually using a Constant block.

**Data Types:** `single`

### **StartFOC** — Begin closed loop FOC logical

Signal that starts running the motor in closed-loop FOC mode:

- `1` (rising edge of a pulse) — This signal initiates
  mechanical parameter estimation by running the motor in closed-loop using
  FOC.
- `0` (falling edge of a pulse) — This signal starts running
  the motor using open-loop control.

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
| Rated speed of motor | | | RPM |
| Rated current of motor | | | A |
| Maximum measurable inverter current | | | A |
| Board resistance | | | ohms |
| Current sense gain | | | A/ADC Count |
| Voltage sense gain | | | V/ADC Count |
| Parameter estimation sample time | | | seconds |
| Elements for estimating motor inductances (*Ld* and *Lq*) | Maximum frequency | | | Hz |
| Minimum frequency | | | Hz |
| Step for frequency sweep | | | Hz |
| Frequency step size for estimation | | | Hz |
| Number of frequencies for estimation | | | - |
| Elements for estimating back EMF constant (*Ke*), motor inertia (*J*), and friction constant (*B*) | Back EMF estimation time | | | seconds |
| Back EMF estimation maximum speed limit | | | RPM |
| Specify current controller gains (off/on) | | | - |
| Proportional gain | | | - |
| Integral gain | | | - |
| *Iq* reference current as a ratio of rated motor current | | | PU current |
| Lower speed limit for inertia estimation | | | RPM |

You can connect this input port to the `Config` output port of
the PMSM Parameter Estimation Configurator block.

**Data Types:** `single`
### Output

### **Vabc** — *a*, *b*, and *c*-axis stator reference voltage components vector

Stator reference voltage components along the *a*,
*b*, and *c* axes of the *abc*
reference frame. Each voltage component has a range between `-1` and
`1`.

**Data Types:** `single`

### **Ke** — Estimated back EMF constant scalar

Estimated back EMF constant of the PMSM (in V/m/s).

**Data Types:** `single`

### **J** — Estimated rotor inertia scalar

Estimated inertia of the PMSM (in kg.m2).

**Data Types:** `single`

### **B** — Estimated viscous damping scalar

Estimated viscous damping of the PMSM (in N.s/m).

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
| *status* | | `0` | Mechanical parameter estimation did not start yet. | - |
| `1` | Mechanical parameter estimation is in progress. | - |
| `2` | Mechanical parameter estimation completed successfully. | - |
| `8300` | Back EMF estimation failed because the motor failed to reach 90% of **Back EMF estimation maximum speed limit (RPM)** within the period of **Back EMF estimation time (s)**+10 seconds.  For more details about the **Back EMF estimation maximum speed limit (RPM)** and **Back EMF estimation time (s)** parameters, see PMSM Parameter Estimation Configurator. | - |
| *CoastDownTime* | | | Measured coast-down duration | seconds |
| *Vdq* | | | Voltages across *d* and *q* axes | volts |
| *Idq* | | | Currents across *d* and *q* axes | amperes |
| *VIAlphaBeta* | | | Voltages and currents across *α* and *β* axes | volts, amperes |

**Data Types:** `single`

## Parameters

### **Slowdown factor for current PI controller gains [1,20]** — Slowdown factor for current PI controllers when estimating back-EMF `5` (default) | `scalar`

Slowdown factor (specified as an integer between `1` and
`20`) for the current PI controllers during back-EMF estimation. A
smaller value results in more aggressive controllers.

## Libraries

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: New block parameter added

The Block Parameters dialog box now includes advanced options for configuring the
parameter estimation process.

## Description

Estimate back EMF constant, rotor inertia, and viscous damping of permanent magnet synchronous motor (PMSM)

The PMSM Mechanical Parameter Estimator block uses the phase currents and
voltages, DC voltage across the motor, motor position and speed, stator resistance,
*d*-axis inductance, as well as the other test configuration elements to
compute the following mechanical parameters of a PMSM:

- Back EMF constant (*Ke*)
- Rotor inertia (*J*)
- Viscous damping (*B*)

The block runs the motor using closed-loop field-oriented control (FOC) with a limited
speed during which it runs the tests to estimate the back-EMF constant
(*Ke*) and viscous damping (*B*).
After a pre-configured duration, the block concludes these tests to compute
*Ke* and *B*, and then, triggers
coast-down by shutting down all six inverter switches. The coast-down results in gradual
decline in motor speed which eventually reaches zero. The block measures and uses the time to
reach zero-speed to calculate rotor inertia (*J*).
