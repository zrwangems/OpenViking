---
type: simulink-block
title: 'PMSM Parameter Estimation Configurator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Parameter Estimation'
documentation_page: 'pmsmparameterestimationconfigurator'
documentation_source_path: 'ref/pmsmparameterestimationconfigurator.html'
language: en
---

# PMSM Parameter Estimation Configurator

## Ports

### Output

### **Config** — Bus signal bus

The bus signal includes these configuration elements.

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

The configuration elements are analogous to the block parameters. For more
information about these elements, see .

**Data Types:** `single`

## Parameters

#### Motor and Inverter

### **Number of pole pairs** — Number of motor pole pairs `4` (default) | `scalar`

Number of pole pairs available in the PMSM.

### **Rated speed (RPM)** — Motor rated speed `4000` (default) | `scalar`

Rated speed of the PMSM (in RPM).

### **Rated motor current (A)** — Motor rated current `7` (default) | `scalar`

Rated current of the PMSM (in amperes).

### **Maximum inverter current (A)** — Maximum measurable current `21` (default) | `scalar`

Maximum current (in amperes) that the system
(including inverter and controller) can measure.

### **Board resistance (ohm)** — Inverter bridge resistance `0.0043` (default) | `scalar`

Resistance (in ohms) in the path of phase currents
(excluding motor resistance). You can obtain this value from the datasheet of the
inverter hardware.

### **Current sense gain (A/ADC Count)** — Current per ADC count `0.0105` (default) | `scalar`

Gain of the current sense circuit of the inverter.
This value determines the current (in Amperes) corresponding to one analog-to-digital
converter (ADC) count (resolution of the measurable current range).

### **Voltage sense gain (V/ADC Count)** — Voltage per ADC count `0.0098` (default) | `scalar`

Gain of the voltage sense circuit of the inverter.
This value determines the voltage (in Volts) corresponding to one analog-to-digital
converter (ADC) count (resolution of the measurable voltage range).

#### Ld and Lq Estimation

### **Maximum frequency (Hz)** — Maximum frequency injected for frequency sweep `1000` (default) | `scalar`

Maximum frequency (in Hertz) injected by the
Ld Estimator and Lq Estimator blocks to begin the
frequency sweep. For more details, see Ld Estimator and
Lq
Estimator.

### **Minimum frequency (Hz)** — Minimum frequency injected for frequency sweep `400` (default) | `scalar`

Minimum frequency (in Hertz) injected by the
Ld Estimator and Lq Estimator blocks to conclude the
frequency sweep. For more details, see Ld Estimator and
Lq
Estimator.

### **Step for frequency sweep (Hz)** — Step size for frequency sweep `100` (default) | `scalar`

Step size (in Hertz) using which the Ld
Estimator and Lq Estimator blocks decrement the frequency
during the frequency sweep. For more details, see Ld Estimator and
Lq
Estimator.

### **Frequency step size for estimation (Hz)** — Frequency step size for *Ld* and *Lq* estimation `10` (default) | `scalar`

Step size (in Hertz) using which the Ld
Estimator and Lq Estimator blocks increment the frequency
during the *Ld* and
*Lq* estimation process. For more details,
see Ld Estimator and
Lq
Estimator.

### **Number of frequencies for estimation** — Number of injected frequencies for *Ld* and *Lq* estimation `10` (default) | `scalar`

Number of frequencies (with a step size defined by
the **Frequency step size for estimation (Hz)** parameter) that the
Ld Estimator and Lq Estimator blocks inject after the
frequency sweep to estimate *Ld* and
*Lq* parameters. For more details, see
Ld Estimator and
Lq
Estimator.

### **Current measurement delay (s)** — Delay in current measurement `2 * 50e-6` (default) | `scalar`

Time delay (in seconds) between an instance of
current change and the point of time when the changed current is measured in the
microcontroller.

#### Ke, J, B Estimation

### **Back EMF estimation time (s)** — Motor run duration when estimating back-EMF `5` (default) | `scalar`

Duration (in seconds) for which the PMSM
Mechanical Parameter Estimator block runs the motor using closed-loop control
to estimate back-EMF, *Ke*. For more details,
see PMSM Mechanical Parameter
Estimator.

### **Back EMF estimation maximum speed limit (RPM)** — Motor speed when estimating back-EMF `3500` (default) | `scalar`

Speed (in RPM) at which the PMSM Mechanical
Parameter Estimator block runs the motor using closed-loop control to estimate
back-EMF, *Ke*. For more details, see PMSM Mechanical Parameter
Estimator.

### **Iq reference current as a ratio of rated motor current** — Reference current for FOC when estimating *Ke*, *J*, and *B* `0.2` (default) | `scalar`

Reference current,
*Iq* (in units of the motor rated current),
to achieve the reference speed specified in the **Back EMF estimation maximum
speed limit (RPM)** parameter. For more information about the estimation
process, see PMSM Mechanical Parameter
Estimator.

### **Specify current controller gains** — Specify PI current controller gains `off` (default) | `on`

Select this parameter to enable these
fields:

- **Proportional gain**
- **Integral gain**

You can use these fields to enter the proportional
and integral gains of the PI current controllers that implement closed-loop control to
estimate *Ke*, *J*, and
*B*.

If you clear this parameter, the block automatically computes the proportional and
integral gains.

For more information about the estimation process,
see PMSM Mechanical Parameter
Estimator.

### **Proportional gain** — Proportional gain of PI controller `1` (default) | `scalar`

Proportional gain,
*kp*, of the PI current controller that
implements field-oriented control to run the motor in closed-loop control and estimate
*Ke*, *J*, and
*B*.

#### Dependencies

To enable this parameter, select the **Specify current controller
gains** parameter.

### **Integral gain** — Integral gain of PI controller `1000` (default) | `scalar`

Integral gain,
*ki*, of the PI current controller that
implements field-oriented control to run the motor in closed-loop control and estimate
*Ke*, *J*, and
*B*.

#### Dependencies

To enable this parameter, select the **Specify current controller
gains** parameter.

### **Speed lower limit for inertia estimation (RPM)** — Lower speed limit during coast-down `1000` (default) | `scalar`

Lower speed limit (in RPM) during coast-down at
which the PMSM Mechanical Parameter Estimation block registers the
timestamp for estimating motor inertia. For more information about the estimation
process, see PMSM Mechanical Parameter
Estimator.

### **Parameter estimation sample time (s)** — Sample time for parameter estimation `50e-6` (default) | `scalar`

Sample time (in seconds) for the parameter
estimation algorithm. This parameter defines the sample time in these parameter
estimation blocks for PMSMs:

- PMSM Rs Estimator
- Ld Estimator
- Lq Estimator
- PMSM Mechanical Parameter Estimator

## Libraries

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Generate configuration elements for PMSM parameter estimation

The PMSM Parameter Estimation Configurator block generates the following
configuration elements for estimating the parameters of a permanent magnet synchronous motor
(PMSM):

- Elements for motor and inverter hardware
- Elements for estimating motor resistance
  (*Rs*)
- Elements for estimating motor inductances
  (*Ld* and
  *Lq*)
- Elements for estimating back EMF constant
  (*Ke*), motor inertia (*J*),
  and friction constant (*B*)

The block uses the parameter settings to generate an output bus containing the
configuration elements. You can use the configuration elements in these PMSM parameter
estimation blocks:

- Rs Estimator
- Ld Estimator
- Lq Estimator
- PMSM Mechanical Parameter
  Estimator
