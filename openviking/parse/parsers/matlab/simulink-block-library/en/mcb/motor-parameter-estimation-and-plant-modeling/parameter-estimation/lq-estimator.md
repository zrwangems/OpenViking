---
type: simulink-block
title: 'Lq Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Parameter Estimation'
documentation_page: 'lqestimator'
documentation_source_path: 'ref/lqestimator.html'
language: en
---

# Lq Estimator

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

### **Rs** — Estimated stator resistance scalar

Estimated stator resistance (in ohms) of the PMSM. You can either connect this
input port to the `Rs` output of the PMSM Rs Estimator
block or provide the resistance value manually using a Constant
block.

**Data Types:** `single`

### **StartStop** — Control signal for *Lq* estimation logical

Signal that either starts or stops *Lq*
estimation:

- `1` (rising edge of a pulse) — This signal initiates the
  *Lq* estimation.
- `0` (falling edge of a pulse) — This signal immediately stops
  the *Lq* estimation process. If you
  interrupt the estimation process abruptly before completion, the block does not
  compute or output the *Lq* value.

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

### **Lq** — Estimated *q*-axis stator inductance scalar

Estimated *q*-axis stator inductance (in henries).

**Data Types:** `single`

### **Log** — Debug signals bus

Debug signals that the block provides for examination. The bus includes these
debug signals.

| Debug signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| *InjFreq* | | | Frequency of signal injected most recently | Hz |
| *status* | | `0` | *Lq* estimation did not start yet. | - |
| `1` | *Lq* estimation is in progress. | - |
| `2` | *Lq* estimation completed successfully. | - |
| `8200` | *Lq* estimation failed because the current feedback from motor did not increase proportionally to the rise in the injected voltage. Check the motor connections and ensure the ADC correctly measures *Ia* and *Ib*. | - |
| `8201` | Estimated *Lq* is negative because the phase difference is greater than `90°`. Check the phase difference in the log output, and adjust the injected frequency range as needed. Make sure the **Current measurement delay** parameter is accurately configured in the PMSM Parameter Estimation Configurator block, and try increasing the PWM frequency. | - |
| *Iq* | | | *Q*-axis current | A |
| *Vq* | | | *Q*-axis voltage | V |
| *PhaseDiff\_rad* | | | Phase difference between the injected voltage and current response | radians |

**Data Types:** `single`

## Parameters

### **Maximum current limit (A)** — Maximum allowed current during test `15` (default) | `scalar`

Maximum allowed current (in amperes) during testing.

### **Step size during injected voltage ramp up (per-unit)** — Step size during injected voltage ramp up `0.0001` (default) | `scalar`

Step size (in per-units) during ramp up of injected voltage.

### **Number of sinusoidal voltage injections per frequency sweep step** — Number of sinusoidal voltage injections per frequency during frequency sweep `5` (default) | `scalar`

Number of sinusoidal voltage injections per frequency for each frequency sweep
step.

### **Number of sinusoidal voltage injections per frequency during Lq estimation** — Number of sinusoidal voltage injections per frequency during Lq estimation `5` (default) | `scalar`

Number of sinusoidal voltage injections per frequency for each Lq estimation
step.

## Libraries

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: New block parameters added

The Block Parameters dialog box now includes advanced options for configuring the
parameter estimation process.

## Description

Estimate stator inductance ( L q ) of permanent magnet synchronous motor (PMSM)

The Lq Estimator block computes the *q*-axis stator
inductance of a PMSM using the phase currents, stator resistance, and the test configuration
elements.

At first, the block locks the rotor along the *d*-axis by injecting a
constant voltage (*Vd*). This ensures that the rotor
remains stationary (aligned with *d*-axis) during frequency injection. To
estimate *q*-axis stator inductance, the block injects a high-frequency
voltage signal along the *q*-axis and then performs the frequency sweep
process by gradually reducing the injected signal frequency using the step size defined by
**Step for frequency sweep (Hz)** parameter. During frequency sweep, the
block monitors the magnitude of the motor phase current. When the injected signal frequency
reaches the minimum value (**Minimum frequency (Hz)** parameter), the block
starts the estimation process by injecting a signal with rising frequency having a step size
of **Frequency step size for estimation (Hz)** with number of steps defined
by the **Number of frequencies for estimation** parameter. For details about
these parameters, see PMSM Parameter Estimation
Configurator.

This image shows the frequency sweep and the incremental steps of rising frequency.

The *Lq* estimation process uses the measured
frequency sweep time duration as well as the step size of the changing frequency to estimate
the *q*-axis stator inductance,
*Lq*.
