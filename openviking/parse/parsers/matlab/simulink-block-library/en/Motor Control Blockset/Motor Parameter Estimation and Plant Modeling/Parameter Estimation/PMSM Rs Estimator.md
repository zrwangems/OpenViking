---
type: simulink-block
title: 'PMSM Rs Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Parameter Estimation'
documentation_page: 'pmsmrsestimator'
documentation_source_path: 'ref/pmsmrsestimator.html'
language: en
---

# PMSM Rs Estimator

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

### **StartStop** — Control signal for *Rs* estimation logical

Signal that either starts or stops *Rs*
estimation:

- `1` (rising edge of a pulse) — This signal initiates the
  *Rs* estimation process.
- `0` (falling edge of a pulse) — This signal immediately stops
  the *Rs* estimation process. If you
  interrupt the estimation process abruptly before completion, the block does not
  compute or output the *Rs* value.

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

### **Rs** — Estimated stator resistance scalar

Estimated stator resistance (in ohms) of the PMSM.

**Data Types:** `single`

### **Log** — Debug signals bus

Debug signals that the block provides for examination. The bus includes these
debug signals.

| Debug signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| *I1* | | | First measured phase current | A |
| *V1* | | | First injected phase voltage | V |
| *I2* | | | Second measured phase current | A |
| *V2* | | | Second injected phase voltage | V |
| *Rs1* | | | Estimated *a* axis resistance | ohms |
| *Rs2* | | | Estimated *b* axis resistance | ohms |
| *Rs3* | | | Estimated *c* axis resistance | ohms |
| *status* | | `0` | *Rs* estimation did not start yet. | - |
| `1` | *Rs* estimation is in progress. | - |
| `2` | *Rs* estimation completed successfully. | - |
| `8000` | *Rs* estimation failed because the current feedback from motor did not increase proportionally to the rise in the injected voltage. Observe all three phase resistances from the log output and if they are in the acceptable range, increase the threshold in the block mask to accommodate the imbalance in resistances. | - |
| `8001` | *Rs1* estimation failed due to issues in the *Ia* phase current. Check if the motor is properly connected and that the ADC is correctly measuring *Ia*. | - |
| `8002` | *Rs2* estimation failed due to issues in the *Ib* phase current. Check if the motor is properly connected and that the ADC is correctly measuring *Ib*. | - |
| `8003` | *Rs3* estimation failed due to issues in the *Ic* phase current. Check if the motor is properly connected and that the ADC is correctly measuring *Ic*. | - |

**Data Types:** `single`

## Parameters

### **Maximum current limit (A)** — Maximum allowed current during testing `15` (default) | `scalar`

Maximum allowed current (in amperes) during testing.

### **Step size during injected voltage ramp up (per-unit)** — Step size during injected voltage ramp up `0.0001` (default) | `scalar`

Step size (in per-units) during ramp up of injected voltage.

### **Maximum voltage ramp up time limit (s)** — Maximum voltage ramp up duration `0.25` (default) | `scalar`

Maximum allowed duration (in seconds) for ramp up of injected voltage.

### **Number of voltage and current samples per voltage injection instance** — Number of voltage and current samples considered for Rs estimation `1000` (default) | `scalar`

Number of voltage and current samples for each voltage injection that are used for
Rs estimation.

### **Dwell time between voltage injections (s)** — Wait duration between voltage injections `0.25` (default) | `scalar`

Wait duration (in seconds) between successive voltage injections.

### **Threshold to determine imbalance in phase resistances (0,1)** — Threshold to determine phase resistance imbalance `0.2` (default) | `scalar`

Threshold (specified as a value between `0` and
`1`) above which to determine the imbalance among the phase
resistances.

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

Estimate stator resistance ( R s ) of permanent magnet synchronous motor (PMSM)

The PMSM Rs Estimator block computes the stator resistance of a PMSM using
the phase currents, DC voltage across the motor, and the test configuration elements.

The block injects two voltages *V1* and
*V2* for each phase and measures the respective
current responses *I1* and
*I2* to estimate each phase resistance. It then
estimates the motor resistance by averaging the three phase resistances.
