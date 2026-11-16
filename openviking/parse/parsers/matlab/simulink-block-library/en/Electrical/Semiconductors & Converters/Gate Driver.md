---
type: simulink-block
title: 'Gate Driver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'gatedriver'
documentation_source_path: 'ref/gatedriver.html'
language: en
---

# Gate Driver

## Ports

### Input

### **u** — Control signal, unitless physical signal

Input physical signal that specifies the input control value.

#### Dependencies

To enable this port, set **Modeling option** to
`PS input`.
### Conserving

### **PWM** — Pulse-width modulated signal electrical

Electrical conserving port associated with the pulse-width modulated
signal.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical input ports`.

### **REF** — Floating zero volt reference electrical

Electrical conserving port associated with the floating zero volt
reference.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical input ports`.

### **G** — Gate connection electrical

Electrical conserving port associated with the gate. Connect this port
to the gate of a MOSFET or IGBT block.

### **S** — Source or emitter connection electrical

Electrical conserving port associated with the source or emitter.
Connect this port to the source of a MOSFET block or the emitter of an IGBT block.

## Parameters

### **Modeling option** — Whether to model electrical or physical signal input ports `PS input` (default) | `Electrical input ports`

Whether to model physical signal or electrical input ports.

### Input Logic

### **Logic 1 input value** — Signal value for logic 1 0.7 (default)

Value of the input signal corresponding to the logic 1 level.

#### Dependencies

To enable this port, set **Modeling option** to
`PS input`.

### **Logic 0 input value** — Signal value for logic 0 0.3 (default)

Value of the input signal corresponding to the logic 0 level.

#### Dependencies

To enable this port, set **Modeling option** to
`PS input`.

### **Logic 1 input voltage** — Voltage value for logic 1 2.0 V (default)

Value of the input voltage corresponding to the logic 1 level.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical input ports`.

### **Logic 0 input voltage** — Voltage value for logic 0 0.8 V (default)

Value of the input voltage corresponding to the logic 0 level.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical input ports`.

### Outputs

### **On-state gate-source voltage** — Demanded output voltage for on state 15 V (default)

Demanded output voltage when the driver is in on state.

### **Off-state gate-source voltage** — Demanded output voltage for off state 0 V (default)

Demanded output voltage when the driver is in off state.

### Timing

### **Propagation delay (logic 0->logic 1)** — Turn-on propagation delay 50 ns (default)

When the input rises above the logic 1 input level, the transition of
the output state from off to on is initiated after a delay equal to the
turn-on propagation delay.

### **Propagation delay (logic 1->logic 0)** — Turn-off propagation delay 50 ns (default)

When the input falls below the logic 0 input value, the transition of
the output state from on to off is initiated after a delay equal to the
turn-off propagation delay.

### Dynamics

### **Parameterization** — Select driver parameterization `Output impedance` (default) | `Rise and fall times`

Select the type of driver parameterization:

- `Output impedance` — Specify
  on-state and off-state gate drive resistances.
- `Rise and fall times` —
  Specify rise time, fall time, and load capacitance.

### **On-state gate drive resistance** — Gate drive resistance for on state 2 Ω (default)

Gate drive resistance when the driver is in on state.

#### Dependencies

Enabled when the **Parameterization** parameter
is set to `Output impedance`.

### **Off-state gate drive resistance** — Gate drive resistance for off state 2 Ω (default)

Gate drive resistance when the driver is in off state.

#### Dependencies

Enabled when the **Parameterization** parameter
is set to `Output impedance`.

### **Rise time** — Driver rise time 20 ns (default)

Driver rise time from 10% to 90%.

#### Dependencies

Enabled when the **Parameterization** parameter
is set to `Rise and fall times`.

### **Fall time** — Driver fall time 20 ns (default)

Driver fall time from 90% to 10%.

#### Dependencies

Enabled when the **Parameterization** parameter
is set to `Rise and fall times`.

### **Load capacitance for rise and fall times** — Driver load capacitance 10 nF (default)

Driver load capacitance.

#### Dependencies

Enabled when the **Parameterization** parameter
is set to `Rise and fall times`.

### Faults

### **State fault** — Option to model faulty state in gate driver `Add fault` (default)

Option to model a faulty state in the Gate Driver block.

To add a fault, click the **Add fault**
hyperlink.

### **Failure mode** — State of driver after failure `Fail off` (default) | `Fail on`

Select whether the driver fails by making the connected semiconductor
device permanently turned off or on.

#### Dependencies

To enable this parameter, add a fault to the Gate Driver block by
clicking the **Add fault** hyperlink in the
**State fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Behavioral model of gate driver integrated circuit

The Gate Driver block provides an abstracted
representation of a gate driver integrated circuit. The block models input hysteresis,
propagation delay, and turn-on/turn-off dynamics. Unless modeling a gate driver circuit
explicitly, always use this block or the Half-Bridge
Driver block to set gate-source voltage on a MOSFET block or
gate-emitter voltage on an IGBT block. Do not connect a controlled voltage source
directly to a semiconductor gate, because this omits the gate driver output impedance
that determines switching dynamics.

You can model electrical or physical signal input ports by setting the **Modeling option** parameter to either:

- `PS input` — The driver output state is controlled by a physical signal input u. Use this modeling option if all of your controller, including PWM waveform generation, is determined by Simulink® blocks. This modeling option is the default.
- `Electrical input ports` — The driver output state is controlled by two electrical input connections, PWM and REF. Use this option if your model has upstream analog components, such as the Controlled PWM Voltage source.

When the input rises above the logic 1 input level, the transition of the output state
from off to on is initiated after a delay equal to the turn-on propagation delay. The
demanded output voltage across the **G** and **S**
ports steps in value from the off-state output voltage to the on-state output voltage,
but the actual output voltage is set by the RC time constant associated with the
**On-state gate drive resistance** value and the total load
capacitance. Similarly, when the input falls below the logic 0 input value, the
transition of the output state from on to off is initiated after a delay equal to the
turn-off propagation delay and with dynamics now set by the **Off-state gate
drive resistance** value.

### Faults

To model a fault in the Gate Driver block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

You can insert a fault into the output of the gate driver at a specified
simulation time, to make the connected semiconductor device either permanently off
or permanently on. Use this feature to represent a failed semiconductor device as
failed at open-circuit or at normal on-state conditions.
