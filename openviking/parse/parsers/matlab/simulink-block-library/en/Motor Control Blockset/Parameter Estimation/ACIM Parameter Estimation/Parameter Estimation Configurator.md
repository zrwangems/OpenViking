---
type: simulink-block
title: 'ACIM Parameter Estimation Configurator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'acimparameterestimationconfigurator'
documentation_source_path: 'ref/acimparameterestimationconfigurator.html'
language: en
---

# ACIM Parameter Estimation Configurator

## Ports
```yaml
ports:
- name: Config
  summary: Bus signal bus
  direction: output
  data_types: single
```

### Output

### **Config** — Bus signal bus

The bus signal includes these configuration elements.

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

The configuration elements are analogous to the block parameters. For more
information about these elements, see Parameters.

**Data Types:** `single`
## Parameters
```yaml
parameters:
- name: Number of pole pairs
  summary: Number of motor pole pairs 2 (default) | scalar
  group: ''
- name: Rated frequency (Hz)
  summary: Motor rated frequency 50 (default) | scalar
  group: ''
- name: Nominal motor current (A)
  summary: Motor nominal current 2 (default) | scalar
  group: ''
- name: Nominal voltage (V)
  summary: Motor nominal voltage 24 (default) | scalar
  group: ''
- name: Maximum inverter current (A)
  summary: Maximum measurable current 21 (default) | scalar
  group: ''
- name: Board resistance (ohm)
  summary: Inverter bridge resistance 0.0043 (default) | scalar
  group: ''
- name: Current sense gain (A/ADC Count)
  summary: Current per ADC count 0.0105 (default) | scalar
  group: ''
- name: Voltage sense gain (V/ADC Count)
  summary: Voltage per ADC count 0.0098 (default) | scalar
  group: ''
- name: Measurement time (sec)
  summary: Time used to measure and average-out current 5 (default) | scalar
  group: ''
- name: Open loop ramp time (sec)
  summary: Time allotted to ramp up frequency 3 (default) | scalar
  group: ''
- name: Estimation time (sec)
  summary: Time to run *Rs* estimation algorithm 2 (default) | scalar
  group: ''
- name: Vd reference voltage 1 (PU)
  summary: First reference voltage for *Rs* estimation 0.1 (default) | scalar
  group: ''
- name: Vd reference voltage 2 (PU)
  summary: Second reference voltage for *Rs* estimation 0.2 (default) | scalar
  group: ''
- name: Frequency 1 as a ratio of rated frequency (PU)
  summary: Ratio of first injected low frequency over rated frequency 0.1 (default) | scalar
  group: ''
- name: Frequency 2 as a ratio of rated frequency (PU)
  summary: Ratio of second injected low frequency over rated frequency 0.2 (default) | scalar
  group: ''
- name: High Frequency for Lm (Hz)
  summary: Frequency of third injected signal 200 (default) | scalar
  group: ''
- name: Voltage sweep start value voltage (PU)
  summary: Initial voltage at which voltage sweep begins 0.1 (default) | scalar
  group: ''
- name: Voltage sweep step value voltage (PU)
  summary: Step size for voltage sweep 0.0125 (default) | scalar
  group: ''
- name: High frequency injection voltage (PU)
  summary: Voltage of third injected signal 0.1 (default) | scalar
  group: ''
- name: Current measurement delay (s)
  summary: Delay in current measurement 2 * 50e-6 (default) | scalar
  group: ''
- name: Closed loop duration (sec)
  summary: Closed-loop motor run duration 5 (default) | scalar
  group: ''
- name: Closed loop speed (RPM)
  summary: Closed-loop motor speed 950 (default) | scalar
  group: ''
- name: Iq reference current for FOC (PU)
  summary: Reference current for FOC when estimating *J* and *B* 0.2 (default) | scalar
  group: ''
- name: Specify current controller gains
  summary: Specify PI current controller gains off (default) | on
  group: ''
- name: Proportional gain
  summary: Proportional gain of PI controller 1 (default) | scalar
  group: ''
- name: Integral gain
  summary: Integral gain of PI controller 1000 (default) | scalar
  group: ''
- name: Speed lower limit for inertia estimation (RPM)
  summary: Lower speed limit during coast-down 100 (default) | scalar
  group: ''
- name: Parameter estimation sample time (sec)
  summary: Sample time for parameter estimation 50e-6 (default) | scalar
  group: ''
```

#### Motor and Inverter

### **Number of pole pairs** — Number of motor pole pairs `2` (default) | `scalar`

Number of pole pairs available in the induction
motor.

### **Rated frequency (Hz)** — Motor rated frequency `50` (default) | `scalar`

Rated frequency of the induction motor (in
Hertz).

### **Nominal motor current (A)** — Motor nominal current `2` (default) | `scalar`

Rated current of the induction motor (in
Amperes).

### **Nominal voltage (V)** — Motor nominal voltage `24` (default) | `scalar`

Rated voltage of the induction motor (in
Volts).

### **Maximum inverter current (A)** — Maximum measurable current `21` (default) | `scalar`

Maximum current (in Amperes) that the system
(including inverter and controller) can measure.

### **Board resistance (ohm)** — Inverter bridge resistance `0.0043` (default) | `scalar`

Resistance in the path of phase currents (excluding
motor resistance). You can obtain this value from the datasheet of the inverter
hardware.

### **Current sense gain (A/ADC Count)** — Current per ADC count `0.0105` (default) | `scalar`

Gain of the current sense circuit of the inverter.
This value determines the current (in Amperes) corresponding to one analog-to-digital
converter (ADC) count (resolution of the measurable current range).

### **Voltage sense gain (V/ADC Count)** — Voltage per ADC count `0.0098` (default) | `scalar`

Gain of the voltage sense circuit of the inverter.
This value determines the voltage (in Volts) corresponding to one analog-to-digital
converter (ADC) count (resolution of the measurable voltage range).

#### Id0 Estimation

### **Measurement time (sec)** — Time used to measure and average-out current `5` (default) | `scalar`

Time used to measure and average-out the peaks in
the current response to the open-loop operation of the induction motor. For more details
about *Id0* estimation, see Id0
Estimator.

### **Open loop ramp time (sec)** — Time allotted to ramp up frequency `3` (default) | `scalar`

Time that you want to allot for the motor operation
frequency to ramp up and reach 90 percent of the motor rated frequency. For more details
about *Id0* estimation, see Id0
Estimator.

#### Rs Estimation

### **Estimation time (sec)** — Time to run *Rs* estimation algorithm `2` (default) | `scalar`

Time that you want to allot to run the motor
resistance (*Rs*) estimation algorithm. This
value defines the time duration for which the ACIM Rs Estimator block
injects each voltage to measure the motor resistance. For more details about
*Rs* estimation, see ACIM Rs
Estimator.

### **Vd reference voltage 1 (PU)** — First reference voltage for *Rs* estimation `0.1` (default) | `scalar`

The first reference motor-phase voltage (in
per-unit) that the ACIM Rs Estimator block uses for measuring motor
resistance (*Rs*). By default, the block sets
this field to 10 percent of the inverter DC voltage. For more details about
*Rs* estimation, see ACIM Rs
Estimator. For more details about the per-unit system, see Per-Unit System.

### **Vd reference voltage 2 (PU)** — Second reference voltage for *Rs* estimation `0.2` (default) | `scalar`

The second reference motor-phase voltage (in
per-unit) that the ACIM Rs Estimator block uses for measuring motor
resistance (*Rs*). By default, the block sets
this field to 20 percent of the inverter DC voltage. For more details about
*Rs* estimation, see ACIM Rs
Estimator. For more details about the per-unit system, see Per-Unit System.

#### Rr, Lm, Lls, Llr Estimation

### **Frequency 1 as a ratio of rated frequency (PU)** — Ratio of first injected low frequency over rated frequency `0.1` (default) | `scalar`

Ratio of the first injected low frequency over the
rated frequency of the induction motor (in per-unit). For more details about the
estimation process, see RrL Estimator.
For more details about the per-unit system, see Per-Unit System.

### **Frequency 2 as a ratio of rated frequency (PU)** — Ratio of second injected low frequency over rated frequency `0.2` (default) | `scalar`

Ratio of the second injected low frequency over the
rated frequency of the induction motor (in per-unit). For more details about the
estimation process, see RrL Estimator.
For more details about the per-unit system, see Per-Unit System.

### **High Frequency for Lm (Hz)** — Frequency of third injected signal `200` (default) | `scalar`

Frequency of the third (high frequency) signal (in
Hertz) injected by the block for mechanical parameter estimation. For more details about
the estimation process, see RrL
Estimator.

### **Voltage sweep start value voltage (PU)** — Initial voltage at which voltage sweep begins `0.1` (default) | `scalar`

Initial voltage (of the first and second
low-frequency signals that the block injects, in per-unit) at which the voltage sweep
begins. For more details about the estimation process, see RrL Estimator.
For more details about the per-unit system, see Per-Unit System.

### **Voltage sweep step value voltage (PU)** — Step size for voltage sweep `0.0125` (default) | `scalar`

Step size that the block uses to perform voltage
sweep on the two injected low frequency signals (in per-unit). For more details about
the estimation process, see RrL Estimator.
For more details about the per-unit system, see Per-Unit System.

### **High frequency injection voltage (PU)** — Voltage of third injected signal `0.1` (default) | `scalar`

Voltage of the third (high frequency) signal (in
per-unit) injected by the block for mechanical parameter estimation. For more details
about the estimation process, see RrL Estimator.
For more details about the per-unit system, see Per-Unit System.

### **Current measurement delay (s)** — Delay in current measurement `2 * 50e-6` (default) | `scalar`

Time delay between an instance of current change
and the point of time when the changed current is measured in the
microcontroller.

#### J, B Estimation

### **Closed loop duration (sec)** — Closed-loop motor run duration `5` (default) | `scalar`

Duration (in seconds) for which the ACIM
Mechanical Parameter Estimator block runs the motor using closed-loop control
before initiating coast-down. For more information about the estimation process, see
ACIM Mechanical Parameter
Estimator.

### **Closed loop speed (RPM)** — Closed-loop motor speed `950` (default) | `scalar`

Speed (in RPM) at which the ACIM Mechanical
Parameter Estimator block runs the motor using closed-loop control. For more
information about the estimation process, see ACIM Mechanical Parameter
Estimator.

### **Iq reference current for FOC (PU)** — Reference current for FOC when estimating *J* and *B* `0.2` (default) | `scalar`

Reference current,
*Iq* (in units of the motor rated current),
to achieve the reference speed specified in the **Closed loop speed
(RPM)** parameter. For more information about the estimation process, see
ACIM Mechanical Parameter
Estimator.

### **Specify current controller gains** — Specify PI current controller gains `off` (default) | `on`

Select this parameter to enable these
fields:

- **Proportional gain**
- **Integral gain**

You can use these fields to enter the proportional
and integral gains of the PI current controllers that implement closed-loop control to
estimate *J* and *B*.

If you clear this parameter, the block automatically computes the proportional and
integral gains.

To know more about the estimation process, see
ACIM Mechanical Parameter
Estimator.

### **Proportional gain** — Proportional gain of PI controller `1` (default) | `scalar`

Proportional gain,
*kp*, of the PI current controller that
implements field-oriented control to run the motor in closed-loop control and estimate
*J* and *B*.

#### Dependencies

To enable this parameter, select the **Specify current controller
gains** parameter.

### **Integral gain** — Integral gain of PI controller `1000` (default) | `scalar`

Integral gain,
*ki*, of the PI current controller that
implements field-oriented control to run the motor in closed-loop control and estimate
*J* and *B*.

#### Dependencies

To enable this parameter, select the **Specify current controller
gains** parameter.

### **Speed lower limit for inertia estimation (RPM)** — Lower speed limit during coast-down `100` (default) | `scalar`

Lower speed limit during coast-down at which the
ACIM Mechanical Parameter Estimation block registers the timestamp for
estimating motor inertia. For more details about the estimation process, see ACIM
Mechanical Parameter Estimation.

### **Parameter estimation sample time (sec)** — Sample time for parameter estimation `50e-6` (default) | `scalar`

Sample time for the parameter estimation algorithm.
This parameter defines the sample time for these parameter estimation blocks for AC
induction motors:

- Id0 Estimator
- ACIM Rs Estimator
- Rr L Estimator
- ACIM Mechanical Parameter Estimator
## Libraries

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Generate configuration elements for AC induction motor (ACIM) parameter estimation

The ACIM Parameter Estimation Configurator block generates the following
configuration elements for estimating the parameters of an AC induction motor:

- Elements for motor and inverter hardware
- Elements for estimating magnetizing current
  *Id0*
- Elements for estimating motor resistance
  (*Rs*)
- Elements for estimating:

  - Rotor resistance, *Rr*
  - Magnetizing inductance, *Lm*
  - Stator leakage inductance, *Lls*
  - Rotor leakage inductance, *Llr*
- Elements for estimating motor inertia (*J*) and friction constant
  (*B*)

The block uses the parameter settings to generate an output bus containing the
configuration elements. You can use the configuration elements in these ACIM parameter
estimation blocks:

- Id0
  Estimator
- ACIM Rs
  Estimator
- RrL
  Estimator
- ACIM Mechanical Parameter
  Estimator
