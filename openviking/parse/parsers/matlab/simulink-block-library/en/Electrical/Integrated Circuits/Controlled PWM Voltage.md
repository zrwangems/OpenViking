---
type: simulink-block
title: 'Controlled PWM Voltage'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'controlledpwmvoltage'
documentation_source_path: 'ref/controlledpwmvoltage.html'
language: en
---

# Controlled PWM Voltage

## Ports
```yaml
ports:
- name: u
  summary: Control signal, unitless physical signal
  direction: input
- name: ref+
  summary: Positive terminal electrical
  direction: conserving
- name: ref-
  summary: Negative terminal electrical
  direction: conserving
- name: PWM
  summary: Pulse-width modulated signal electrical
  direction: conserving
- name: REF
  summary: Floating zero volt reference electrical
  direction: conserving
```

### Input

### **u** — Control signal, unitless physical signal

Input physical signal that specifies the duty cycle.

#### Dependencies

To enable this port, set **Modeling option** to
`PS input`.
### Conserving

### **ref+** — Positive terminal electrical

Positive electrical reference voltage.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical input ports`.

### **ref-** — Negative terminal electrical

Negative electrical reference voltage

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical input ports`.

### **PWM** — Pulse-width modulated signal electrical

Electrical conserving port associated with the pulse-width modulated
signal.

### **REF** — Floating zero volt reference electrical

Electrical conserving port associated with the floating zero volt
reference.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to model electrical or physical signal input ports Electrical input ports (default) | PS input
  group: ''
- name: PWM frequency
  summary: PWM output signal frequency 1000 Hz (default)
  group: PWM
- name: Pulse delay time
  summary: Turn-on delay 0 s (default)
  group: PWM
- name: Pulse width offset
  summary: Lengthens or shortens the pulse 0 s (default)
  group: PWM
- name: Minimum pulse width
  summary: Minimum length of pulse 0 s (default)
  group: PWM
- name: Simulation mode
  summary: Select type of output voltage PWM (default) | Averaged
  group: PWM
- name: Switching event type
  summary: Select type of switching event Asynchronous – Best for variable-step solvers (default) | Discrete-time – Best for
    fixed-step solvers
  group: PWM
- name: Sample time
  summary: Discrete sampling time 1e-6 s (default)
  group: PWM
- name: Input voltage for 0% duty cycle
  summary: Vmin 0 V (default)
  group: Input Scaling
- name: Input voltage for 100% duty cycle
  summary: Vmax 5 V (default)
  group: Input Scaling
- name: Input value for 0% duty cycle
  summary: Minimum signal value 0 (default)
  group: Input Scaling
- name: Input value for 100% duty cycle
  summary: Maximum signal value 1 (default)
  group: Input Scaling
- name: Output voltage amplitude
  summary: Signal amplitude for high output 5 V (default)
  group: Output Voltage
```

### **Modeling option** — Whether to model electrical or physical signal input ports `Electrical input ports` (default) | `PS input`

Whether to model electrical or physical signal input ports.

### PWM

### **PWM frequency** — PWM output signal frequency 1000 Hz (default)

Frequency of the PWM output signal.

### **Pulse delay time** — Turn-on delay 0 s (default)

The pulse train does not start until the simulation time is equal to
the **Pulse delay time**. You can specify a small value
for **Pulse delay time** to fine-tune switching times
and ensure that an off-going device is fully off before the on-going
device starts to turn on. You can also use larger delay times, for
example, if you need the pulse train to start only after a number of
cycles. The value you provide must be greater than or equal to
zero.

#### Dependencies

Enabled when the **Simulation mode** parameter is
set to `PWM`.

### **Pulse width offset** — Lengthens or shortens the pulse 0 s (default)

The demanded pulse width as defined by the product of the demanded
duty cycle and one over the pulse frequency can be offset by the value
you provide for **Pulse width offset**. A positive
value acts to lengthen the pulse by a fixed amount. A negative value
acts to shorten the pulse. You can use this parameter, along with the
**Pulse delay time**, to fine-tune switching times
so as to minimize switching losses in some circuits.

#### Dependencies

Enabled when the **Simulation mode** parameter is
set to `PWM`.

### **Minimum pulse width** — Minimum length of pulse 0 s (default)

The minimum pulse length, based on the internal clock or defined
programmatically, to protect the device being driven. The value you
provide must be greater than or equal to zero.

#### Dependencies

Enabled when the **Simulation mode** parameter is
set to `PWM`.

### **Simulation mode** — Select type of output voltage `PWM` (default) | `Averaged`

Select the type of output voltage:

- `PWM` — Produces a pulse-width
  modulated signal.
- `Averaged` — The output is a
  constant whose value is equal to the average value of the PWM
  signal.

### **Switching event type** — Select type of switching event `Asynchronous – Best for variable-step solvers` (default) | `Discrete-time – Best for fixed-step solvers`

Select the switching event type when moving between output high and
output low states:

- `Asynchronous – Best for variable-step
  solvers` — This option is more efficient
  for desktop simulation with variable-step solvers, because it
  requires fewer simulation steps for the same level of
  accuracy.
- `Discrete-time – Best for fixed-step
  solvers` — Use with fixed-step solvers,
  including the local solver. For more information, see Simulating with Fixed Time Step — Local and Global Fixed-Step Solvers.

#### Dependencies

Enabled when the **Simulation mode** parameter is
set to `PWM`.

### **Sample time** — Discrete sampling time 1e-6 s (default)

The time between updates of the block output state. The sample time
must be a multiple of the simulation step size. In order for the PWM
control to have sufficient resolution, set the sample time to less than
one hundredth of the PWM period. (The PWM period is one over the PWM
frequency.)

#### Dependencies

Enabled when the **Switching event type**
parameter is set to `Discrete-time – Best for fixed-step
solvers`.

### Input Scaling

### **Input voltage for 0% duty cycle** — Vmin 0 V (default)

Value of the input voltage at which the PWM signal has a 0% duty
cycle.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Electrical input ports`.

### **Input voltage for 100% duty cycle** — Vmax 5 V (default)

Value of the input voltage at which the PWM signal has a 100% duty
cycle.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Electrical input ports`.

### **Input value for 0% duty cycle** — Minimum signal value 0 (default)

Value of the input signal at which the PWM signal has a 0% duty
cycle.

#### Dependencies

To enable this parameter, set **Modeling option**
to `PS input`.

### **Input value for 100% duty cycle** — Maximum signal value 1 (default)

Value of the input signal at which the PWM signal has a 100% duty
cycle

#### Dependencies

To enable this parameter, set **Modeling option**
to `PS input`.

### Output Voltage

### **Output voltage amplitude** — Signal amplitude for high output 5 V (default)

Amplitude of the PWM signal when the output is high.
## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008b**

## Description

Pulse-width modulated voltage source

The Controlled PWM Voltage block represents a
pulse-width modulated (PWM) voltage source. You can model electrical or physical signal
input ports by setting the **Modeling option** parameter to
either:

- `Electrical input ports` — The block
  calculates the duty cycle based on the reference voltage across its
  **ref+** and **ref-** ports. This option
  is the default.
- `PS input` — Specify the duty cycle value
  directly by using an input physical signal port.

If you set **Modeling option** to `Electrical input
ports`, the demanded duty cycle is

100\*Vref−VminVmax−Vmin percent

where:

- *V*ref is the reference voltage across
  the **ref+** and **ref-** ports.
- *V*min is the minimum reference
  voltage.
- *V*max is the maximum reference
  voltage.

The value of the **Output voltage amplitude** parameter determines
amplitude of the output voltage.

At time zero, the pulse is initialized as high, unless the **Pulse delay
time** parameter is greater than zero, or the demanded duty cycle is
zero.

You can use parameters **Pulse delay time** and **Pulse width
offset** to add a small turn-on delay and a small turn-off advance. This
can be useful when fine-tuning switching times so as to minimize switching
losses.

In PWM mode, the block has two options for the type of switching event when moving
between output high and output low states:

- `Asynchronous – Best for variable-step solvers`
  — Asynchronous events are better suited to variable step solvers, because
  they require fewer simulation steps for the same level of accuracy. In
  asynchronous mode the PWM switching events generate zero crossings, and
  therefore switching times are always determined accurately, regardless of the
  simulation maximum step size.
- `Discrete—time – Best for fixed-step solvers`
  — Discrete-time events are better suited to fixed-step operation, because
  then the switching events are always synchronized with the simulation step.
  Using an asynchronous implementation with fixed-step solvers may sometimes
  result in events being up to one simulation step late. For more information, see
  Simulating with Fixed Time Step — Local and Global Fixed-Step Solvers.

If you use a fixed-step or local solver and the discrete-time switching event type,
the following restrictions apply to the **Sample time** parameter
value:

- The sample time must be a multiple of the simulation step size.
- The sample time must be small compared to the PWM period, to ensure sufficient
  resolution.

### Assumptions and Limitations

The model is based on the following assumptions:

- The REF output of this block is floating, it is not tied to the
  Electrical Reference. One consequence of this is that if
  you connect the PWM and REF electrical ports directly to the PWM and REF
  electrical ports of an H-bridge or a gate driver, you must attach an
  Electrical Reference block to the REF connection
  line.
- Do not connect the Controlled PWM block directly to a
  semiconductor gate, because this omits the gate driver output impedance that
  determines switching dynamics. Use a Gate Driver or a
  Half-Bridge Driver block to set the gate-source or the
  gate-emitter voltage.
- Do not use the Controlled PWM block to drive a motor block
  directly. A PWM motor driver goes open circuit in between pulses. Use the
  H-Bridge block to drive a motor block.
- When driving a motor via the H-Bridge block, set the
  **Simulation mode** parameter to
  `Averaged` to speed up simulations. You must
  also set the **Simulation mode** parameter of the
  H-Bridge block to `Averaged`
  mode. This applies the average of the demanded PWM voltage to the motor. The
  `Averaged` mode assumes that the impedance of
  the motor inductive term is small at the **PWM frequency**.
  To verify this assumption, run the simulation using the
  `PWM` mode and compare the results to those
  obtained from using the `Averaged` mode.
- If you are linearizing your model, set the **Simulation
  mode** parameter to `Averaged` and
  ensure that you have specified the operating point of the block correctly.
  You can only linearize the block for inputs corresponding to a duty cycle
  greater than zero and less than 100 percent.
- When you use this block in `PWM` mode with the
  **Use local solver option** selected in the Solver
  Configuration block, set the **Switching event type**
  parameter to `Discrete—time – Best for fixed-step
  solvers`. Using the `Asynchronous – Best for
  variable-step solvers` option in this situation may produce
  inaccuracies, because simulation with the local solver implies fixed step,
  and the PWM events will not always coincide precisely with the simulation
  steps. This results in PWM events sometimes occurring one simulation step
  late.
