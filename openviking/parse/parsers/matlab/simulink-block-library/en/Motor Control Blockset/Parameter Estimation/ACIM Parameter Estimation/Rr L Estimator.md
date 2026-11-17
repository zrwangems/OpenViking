---
type: simulink-block
title: 'RrL Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'rrlestimator'
documentation_source_path: 'ref/rrlestimator.html'
language: en
---

# RrL Estimator

## Ports
```yaml
ports:
- name: Iabc
  summary: Three-phase current response scalar
  direction: input
  data_types: single
- name: Vdc
  summary: DC link voltage scalar
  direction: input
  data_types: single
- name: StartStop
  summary: Control signal for *Ld* estimation logical
  direction: input
  data_types: Boolean
- name: Config
  summary: Bus signal input bus
  direction: input
  data_types: single
- name: Vabc
  summary: '*a*, *b*, and *c*-axis stator reference voltage components scalar'
  direction: output
  data_types: single
- name: Rr
  summary: Estimated rotor resistance scalar
  direction: output
  data_types: single
- name: Lm
  summary: Estimated magnetizing inductance scalar
  direction: output
  data_types: single
- name: Lls
  summary: Estimated stator leakage inductance scalar
  direction: output
  data_types: single
- name: Llr
  summary: Estimated rotor leakage inductance scalar
  direction: output
  data_types: single
- name: Log
  summary: Debug signals bus
  direction: output
  data_types: single
```

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

### **StartStop** — Control signal for *Ld* estimation logical

Signal that either starts or stops the estimation process:

- `1` (rising edge of a pulse) — This signal initiates the
  estimation process.
- `0` (falling edge of a pulse) — This signal immediately stops
  the estimation process. If you interrupt the estimation process abruptly before
  completion, the block does not compute or output the
  *Rr*,
  *Lm*,
  *Lls*, and
  *Llr* values.

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

### **Rr** — Estimated rotor resistance scalar

Estimated rotor resistance of the induction motor (in Ohms).

**Data Types:** `single`

### **Lm** — Estimated magnetizing inductance scalar

Estimated magnetizing inductance of the induction motor (in Henry).

**Data Types:** `single`

### **Lls** — Estimated stator leakage inductance scalar

Estimated stator leakage inductance of the induction motor (in Henry).

**Data Types:** `single`

### **Llr** — Estimated rotor leakage inductance scalar

Estimated rotor leakage inductance of the induction motor (in Henry).

**Data Types:** `single`

### **Log** — Debug signals bus

Debug signals that the block provides for examination. The bus includes these
debug signals.

| Debug signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| *Id* | | | *D*-axis current | Amperes |
| *InjFreq* | | | Frequency that the block currently injects | Hertz |
| *status* | | `0` | Did not complete estimation | - |
| `1` | Estimation completed successfully | - |
| *Vd* | | | *D*-axis voltage | Volts |

**Data Types:** `single`
## Parameters
```yaml
parameters: []
```

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

Estimate rotor resistance ( R r ), magnetizing inductance ( L m ), stator leakage inductance ( L ls ), and rotor leakage inductance ( L lr ) of AC induction motor (ACIM)

The RrL Estimator block computes the rotor resistance
(*Rr*), magnetizing inductance
(*Lm*), stator leakage inductance
(*Lls*), and rotor leakage inductance
(*Llr*) of an AC induction motor using the phase
currents, DC voltage across the motor, and the test configuration elements.

To estimate these values, the block injects the following three signals across the motor
phases:

- First low-frequency signal (of varying voltage)
- Second low-frequency signal (of varying voltage)
- High-frequency signal (of fixed voltage)

Using the given initial voltage and the step size, the block performs a voltage sweep on
the first and second low-frequency signals until the resulting motor phase current becomes
equal to 50 percent of the motor rated current. At this point, the block measures the phase
difference between the injected voltage (of the low-frequency signals) and the resulting
current response to estimate *Rr*,
*Lm*,
*Lls*, and
*Llr*.
