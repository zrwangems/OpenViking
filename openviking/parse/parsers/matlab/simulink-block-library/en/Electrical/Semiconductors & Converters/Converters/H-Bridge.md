---
type: simulink-block
title: 'H-Bridge'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'hbridge'
documentation_source_path: 'ref/hbridge.html'
language: en
---

# H-Bridge

## Ports
```yaml
ports:
- name: +
  summary: Positive load connection port electrical
  direction: conserving
- name: '-'
  summary: Negative load connection port electrical
  direction: conserving
- name: V+
  summary: Positive supply connection electrical
  direction: conserving
- name: V-
  summary: Negative supply connection electrical
  direction: conserving
- name: PWM
  summary: Pulse-width modulated signal electrical
  direction: conserving
- name: REF
  summary: Reference electrical
  direction: conserving
- name: REV
  summary: REV electrical
  direction: conserving
- name: BRK
  summary: BRK electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **+** — Positive load connection port electrical

Electrical conserving port associated with the positive load
connection.

### **-** — Negative load connection port electrical

Electrical conserving port associated with the negative load
connection.

### **V+** — Positive supply connection electrical

Electrical conserving port associated with the positive electrical
supply connection.

#### Dependencies

This port is visible only when you select
`External` for the **Power
supply** parameter.

### **V-** — Negative supply connection electrical

Electrical conserving port associated with the negative electrical
supply connection.

#### Dependencies

This port is visible only when you select
`External` for the **Power
supply** parameter.

### **PWM** — Pulse-width modulated signal electrical

Electrical conserving port associated with the pulse-width modulated
signal. The voltage is defined relative to the **REF**
port.

### **REF** — Reference electrical

Electrical conserving port associated with the floating zero volt
reference.

### **REV** — REV electrical

Electrical conserving port associated with the voltage that controls
when to reverse the polarity of the
H-Bridge block output. The voltage is
defined relative to the **REF** port.

### **BRK** — BRK electrical

Electrical conserving port associated with the voltage that controls
when to short circuit the H-Bridge block
output. The voltage is defined relative to the **REF**
port.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Power supply
  summary: Visibility of power supply ports Internal (default) | External
  group: Simulation Mode & Load Assumptions
- name: Simulation mode
  summary: Simulation mode PWM (default) | Averaged
  group: Simulation Mode & Load Assumptions
- name: Freewheeling mode
  summary: Freewheeling mode Via one semiconductor switch and one freewheeling diode (default) | Via two freewheeling diodes
    | Via two semiconductor switches and one freewheeling diode
  group: Simulation Mode & Load Assumptions
- name: Regenerative braking
  summary: Regenerative braking Depends on REV flag and current sign (default) | Always enabled (suitable for linearization)
  group: Simulation Mode & Load Assumptions
- name: Load current characteristics
  summary: Load current characteristics Smoothed (default) | Unsmoothed or discontinuous
  group: Simulation Mode & Load Assumptions
- name: Load total series resistance
  summary: Load total series resistance 10Ohm (default)
  group: Simulation Mode & Load Assumptions
- name: Load total series inductance
  summary: Load total series inductance 1e-5H (default)
  group: Simulation Mode & Load Assumptions
- name: PWM frequency
  summary: PWM Frequency 10kHz (default)
  group: Simulation Mode & Load Assumptions
- name: Freewheeling diode off-state conductance
  summary: Freewheeling diode off-state conductance 1e-6S (default)
  group: Simulation Mode & Load Assumptions
- name: Enable threshold voltage
  summary: Enable threshold voltage 2.5V (default)
  group: Input Thresholds
- name: PWM signal amplitude
  summary: PWM signal amplitude 5.0V (default)
  group: Input Thresholds
- name: Reverse threshold voltage
  summary: Reverse threshold voltage 2.5V (default)
  group: Input Thresholds
- name: Braking threshold voltage
  summary: Braking threshold voltage 2.5V (default)
  group: Input Thresholds
- name: Output voltage amplitude
  summary: Output voltage amplitude 12V (default)
  group: Bridge Parameters
- name: Total bridge on resistance
  summary: Total bridge on resistance 0.1Ohm (default)
  group: Bridge Parameters
- name: Freewheeling diode on resistance
  summary: Freewheeling diode on resistance 0.05Ohm (default)
  group: Bridge Parameters
- name: Measurement temperature
  summary: Measurement temperature 298.15K (default)
  group: Bridge Parameters
- name: Total bridge on resistance at second measurement temperature
  summary: Total bridge on resistance at second measurement temperature 0.1Ohm (default)
  group: Temperature Dependence
- name: Freewheeling diode on resistance at second measurement temperature
  summary: Freewheeling diode on resistance at second measurement temperature 0.05Ohm (default)
  group: Temperature Dependence
- name: Second measurement temperature
  summary: Second measurement temperature 398.15K (default)
  group: Temperature Dependence
- name: Thermal mass
  summary: Thermal mass 100J/K (default)
  group: Thermal Port
- name: Initial temperature
  summary: Initial temperature 298.15K (default)
  group: Thermal Port
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model thermal parameters.

### Simulation Mode & Load Assumptions

### **Power supply** — Visibility of power supply ports `Internal` (default) | `External`

Select one of the following options for the type of power supply:

- `Internal` — The power
  supply ports are internal and not visible. This is the
  default option.
- `External` — The power
  supply ports are exposed.

### **Simulation mode** — Simulation mode `PWM` (default) | `Averaged`

Select one of the following options for the type of output voltage:

- `PWM` — The output voltage
  is a pulse-width modulated signal. This is the default
  option.
- `Averaged` — The output
  voltage is a constant whose value is equal to the average
  value of the PWM signal.

### **Freewheeling mode** — Freewheeling mode `Via one semiconductor switch and one freewheeling diode` (default) | `Via two freewheeling diodes` | `Via two semiconductor switches and one freewheeling diode`

Select one of the following options for the type of H-bridge
dissipation circuit:

- `Via one semiconductor switch and one
  freewheeling diode` — In this mode,
  the block controls the load by maintaining one high-side
  bridge arm permanently on and using the PWM signal to
  modulate the corresponding low-side bridge arm. This means
  that the block uses only one of the freewheeling diodes in
  completing the dissipation circuit when the bridge turns
  off. This option is the default.
- `Via two freewheeling diodes`
  — In this mode, all bridge arms are off during the
  bridge off-state. This means that the block dissipates the
  load current across the power supply by two freewheeling
  diodes.
- `Via two semiconductor switches and one
  freewheeling diode` — In this mode,
  the block controls the load by maintaining one high-side
  bridge arm permanently on and using the PWM signal to toggle
  between enabling the corresponding low-side bridge arm and
  the opposite high-side bridge arm. This means that the block
  uses a freewheeling diode in parallel with a bridge arm,
  plus another series bridge arm, to complete the dissipation
  circuit when the bridge turns off.

#### Dependencies

This parameter is visible only when you select
`PWM` for the **Simulation
mode** parameter, or when you select
`Averaged` for the **Simulation
mode** parameter and `Unsmoothed or
discontinuous` for the **Load current
characteristics** parameter.

### **Regenerative braking** — Regenerative braking `Depends on REV flag and current sign` (default) | `Always enabled (suitable for linearization)`

Select one of the following options for the type of H-bridge
dissipation circuit:

- `Depends on REV flag and current
  sign` — This option is the
  default.
- `Always enabled (suitable for
  linearization)` — This option can be
  used when the controller always sets the
  **REV** flag to ensure regenerative
  braking. It is useful if you need to linearize the model for
  control purposes, to ensure that the H-Bridge is
  linearizable around zero duty cycle demand.

#### Dependencies

This parameter is visible only when you select
`Averaged` for the **Simulation
mode** parameter.

### **Load current characteristics** — Load current characteristics `Smoothed` (default) | `Unsmoothed or discontinuous`

Select one of the following options for the type of load current:

- `Smoothed` — Assumes that
  the current is practically continuous due to load
  inductance. This option is the default.
- `Unsmoothed or discontinuous`
  — Use this option for cases where the current is not
  smooth, or possibly discontinuous (that is, it goes to zero
  between PWM cycles). For this option, you must also provide
  values for the **Total load series
  resistance**, **Total load series
  inductance**, and **PWM
  frequency** parameters. During simulation, the
  block uses these values to calculate a more accurate value
  for H-bridge output voltage that achieves the same average
  current as would be present if simulating in PWM
  mode.

#### Dependencies

This parameter is only visible when you select
`Averaged` for the **Simulation
mode** parameter.

### **Load total series resistance** — Load total series resistance `10``Ohm` (default)

The total load series resistance seen by the H-bridge.

#### Dependencies

This parameter is only visible when you select
`Averaged` for the **Simulation
mode** parameter and `Unsmoothed or
discontinuous` for the **Load current
characteristics** parameter.

### **Load total series inductance** — Load total series inductance `1e-5``H` (default)

The total load series inductance seen by the H-bridge. As well as
motor inductance, you should include any series inductance added
external to the motor to smooth current.

#### Dependencies

This parameter is only visible when you select
`Averaged` for the **Simulation
mode** parameter and `Unsmoothed or
discontinuous` for the **Load current
characteristics** parameter.

### **PWM frequency** — PWM Frequency `10``kHz` (default)

The PWM frequency at which the H-bridge is driven. For consistency,
this should be the same value as the PWM frequency specified by the
Controlled PWM Voltage block driving
the H-Bridge block.

#### Dependencies

This parameter is only visible when you select
`Averaged` for the **Simulation
mode** parameter and `Unsmoothed or
discontinuous` for the **Load current
characteristics** parameter.

### **Freewheeling diode off-state conductance** — Freewheeling diode off-state conductance `1e-6``S` (default)

The conductance of the reverse-biased freewheeling diode.

#### Dependencies

This parameter is visible only when you select
`External` for the **Power
supply** parameter or
`Averaged` for the **Simulation
mode** parameter and `Depends on REV flag
and current sign` for the **Regenerative
braking** parameter.

### Input Thresholds

### **Enable threshold voltage** — Enable threshold voltage `2.5``V` (default)

Threshold above which the voltage at the **PWM** port
must rise to enable the H-Bridge block
output.

#### Dependencies

This parameter is used only when **Simulation
mode**, a **Simulation Mode & Load
Assumptions** parameter, is set to
`PWM`.

### **PWM signal amplitude** — PWM signal amplitude `5.0``V` (default)

The amplitude of the signal at the PWM input.

#### Dependencies

The H-Bridge block uses this
parameter only when the **Simulation mode**
parameter on the **Simulation Mode & Load
Assumptions** tab is set to
`Averaged`.

### **Reverse threshold voltage** — Reverse threshold voltage `2.5``V` (default)

When the voltage at the **REV** port is greater than
this threshold, the output polarity becomes negative.

### **Braking threshold voltage** — Braking threshold voltage `2.5``V` (default)

When the voltage at the **BRK** port is greater than
this threshold, the H-Bridge block output
terminals are short-circuited via the following series of devices:

- One bridge arm
- One bridge arm in parallel with a conducting freewheeling
  diode

### Bridge Parameters

### **Output voltage amplitude** — Output voltage amplitude `12``V` (default)

The amplitude of the voltage across the
H-Bridge block output ports when the
output is on.

#### Dependencies

This parameter is visible only when you select
`Internal` for the **Power
supply** parameter.

### **Total bridge on resistance** — Total bridge on resistance `0.1``Ohm` (default)

The total effective resistance of the two semiconductor switches that
connect the load to the two power rails when the voltage at the
**PWM** port is greater than the value of the
**Enable threshold voltage** parameter on the
**Input Thresholds** tab.

### **Freewheeling diode on resistance** — Freewheeling diode on resistance `0.05``Ohm` (default)

The total resistance in the freewheeling diodes that dissipate the
current that flows through the motor when the voltage at the
**PWM** port is less than the value of the
**Enable threshold voltage** parameter on the
**Input Thresholds** tab.

### **Measurement temperature** — Measurement temperature `298.15``K` (default)

The temperature for which the resistance values on the
**Bridge Parameters** tab are specified.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Total bridge on resistance at second measurement temperature** — Total bridge on resistance at second measurement temperature `0.1``Ohm` (default)

The total effective resistance of the two semiconductor switches that
connect the load to the two power rails (as described in the
**Total bridge on resistance** parameter
definition), quoted at the **Second measurement
temperature**.

### **Freewheeling diode on resistance at second measurement temperature** — Freewheeling diode on resistance at second measurement temperature `0.05``Ohm` (default)

The total resistance in the freewheeling diodes that dissipate the
current that flows through the motor (as described in the
**Total bridge on resistance** parameter
definition), quoted at the **Second measurement
temperature**.

### **Second measurement temperature** — Second measurement temperature `398.15``K` (default)

The temperature for which for which the resistance values on the
**Temperature Dependence** tab are
specified.

### Thermal Port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Thermal mass** — Thermal mass `100``J/K` (default)

Thermal mass associated with the thermal port **H**.
It represents the energy required to raise the temperature of the
thermal port by one degree. The default value is `100`
J/K.

### **Initial temperature** — Initial temperature `298.15``K` (default)

The temperature of the thermal port at the start of simulation.
## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2019b: Freewheeling mode

From R2019b forward, the H-Bridge block has the
option to expose the internal supply rail connections.

As a result from this change, inside a model saved in an earlier release, check if
the `Freewheeling mode` parameter of a
H-Bridge block in Averaged mode with the
assumption of `Unsmoothed or discontinuous` current is
still set to the option you require.

### R2019b: Regenerative braking

Prior to R2019b, in `Averaged` simulation mode,
regardless of the voltage applied at the **REV** port for
controlling block output polarity reversal, the H-Bridge block assumed regenerative
braking. A model saved from an earlier release that contains an H-Bridge block in
`Averaged` simulation mode will open in later releases
with the **Regenerative braking** parameter set to
`Always enabled (suitable for parameterization)` and
results will be unchanged. It is recommended that you change this parameter to
`Depends on REV flag and current sign` so that the
**REV** flag is correctly interpreted if not set by the
controller for regenerative braking.

## Description

H-bridge motor driver

The H-Bridge block represents an H-bridge motor driver.
The block has the following two **Simulation mode** options:

- `PWM` — The
  H-Bridge block output is a controlled voltage
  that depends on the input signal at the **PWM** port. If the
  input signal has a value greater than the **Enable threshold
  voltage** parameter value, the
  H-Bridge block output is on and has a value
  equal to the value of the **Output voltage amplitude**
  parameter. If it has a value less than the **Enable threshold
  voltage** parameter value, the block maintains the load circuit
  using one of the following three **Freewheeling mode**
  options:

  - `Via one semiconductor switch and one freewheeling
    diode`
  - `Via two freewheeling diodes`
  - `Via two semiconductor switches and one freewheeling
    diode`

  The first and third options are sometimes referred to as synchronous
  operation.

  The signal at the **REV** port determines the polarity of the
  output. If the value of the signal at the **REV** port is less
  than the value of the **Reverse threshold voltage** parameter,
  the output has positive polarity; otherwise, it has negative polarity.
- `Averaged` — This mode has two **Load
  current characteristics** options:

  - `Smoothed`
  - `Unsmoothed or discontinuous`

  The `Smoothed` option assumes that the current is
  practically continuous due to load inductance. In this case, the
  H-Bridge block output is:

  VOVPWMAPWM−IOUTRON

  where:

  - *VO* is the value of the
    **Output voltage amplitude** parameter.
  - *VPWM* is the value of the
    voltage at the **PWM** port.
  - *APWM* is the value of the
    **PWM signal amplitude** parameter.
  - *IOUT* is the value of the
    output current.
  - *RON* is the **Bridge
    on resistance** parameter.

  The current will be smooth if the PWM frequency is large enough. Synchronous
  operation where freewheeling is via a bridge arm back to the supply also helps
  smooth the current. For cases where the current is not smooth, or possibly
  discontinuous (that is, it goes to zero between PWM cycles), use the
  `Unsmoothed or discontinuous` option. For this
  option, you must also provide values for the **Total load series
  resistance**, **Total load series inductance**,
  and **PWM frequency**. During simulation, the block uses these
  values to calculate a more accurate value for H-bridge output voltage that
  achieves the same average current as would be present if simulating in PWM
  mode.

Set the **Simulation mode** parameter to
`Averaged` to speed up simulations when driving the
H-Bridge block with a Controlled PWM
Voltage block. You must also set the **Simulation
mode** parameter of the Controlled PWM
Voltage block to `Averaged` mode. This
applies the average of the demanded PWM voltage to the motor. The accuracy of the
`Averaged` mode simulation results relies on the validity
of your assumption about the load current. If you specify that the current is
`Unsmoothed or discontinuous`, then the accuracy also
depends on the values you provide for load resistance and inductance being
representative. This mode also makes some simplifying assumptions about the underlying
equations for the case when current is discontinuous. For typical motor and bridge
parameters, accuracy should be within a few percent. To verify
`Averaged` mode accuracy, run the simulation using the
`PWM` mode and compare the results to those obtained from
using the `Averaged` mode.

Braking mode is invoked when the voltage presented at the **BRK**
port is larger than the **Braking threshold voltage**. Regardless of
whether in `PWM` or `Averaged` mode,
when in braking mode the H-bridge is modeled by a series combination of two resistances
*R1* and *R2* where:

- *R1* is the resistance of a single bridge arm, that is, half
  the value of the **Total bridge on resistance**
  parameter.
- *R2* is the resistance of a single bridge arm in parallel
  with a diode resistance, that is, *R1* · *Rd* / (
  *R1* + *Rd* ), where *Rd* is the diode resistance.

### External Power Supply

To model the demands placed on the DC supply, you can choose to expose the power
supply ports of the H-Bridge block by setting the
**Power supply** parameter to
`External`. If the power supply ports are exposed, then
only PWM simulation mode is supported.

**Note**

If the **Power supply** parameter is set to
`External`, the block is able to figure out the
load-side voltage offset by referencing to the supply rail voltages. However, if
the supply rail connections are not exposed, you must add an
Electrical Reference block on the load
side.

### Model Thermal Effects

This block has one optional thermal port. To control the
visibility of the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a thermal
  port.
- `Show thermal port` — The block contains one thermal
  conserving port.

When you expose the thermal port:

- The heat generated by the bridge on-resistance and freewheeling diodes is
  added to the thermal port. The thermal port has an associated thermal mass
  and initial temperature that you can set from the **Thermal
  Port** parameters.
- The bridge on-resistance and freewheeling diode resistance become
  functions of temperature. You can define the values for these resistances
  and the second measurement temperature from the **Temperature
  Dependence** parameters. Resistance is assumed to vary linearly
  between the two measurement temperatures. Extrapolation is used for
  temperatures outside of this range, except for when simulating in averaged
  mode with discontinuous load current characteristics.
