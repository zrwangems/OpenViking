---
type: simulink-block
title: 'Half-Bridge Driver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'halfbridgedriver'
documentation_source_path: 'ref/halfbridgedriver.html'
language: en
---

# Half-Bridge Driver

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

### **HO** — High-side gate connection electrical

Electrical conserving port associated with the gate on the high side
of the half bridge. Connect this port to the gate of a MOSFET or IGBT
block.

### **HS** — High-side source or emitter connection electrical

Electrical conserving port associated with the source or emitter on
the high side of the half bridge. Connect this port to the source of a
MOSFET block or the emitter of an IGBT block.

### **LO** — Low-side gate connection electrical

Electrical conserving port associated with the gate on the low side of
the half bridge. Connect this port to the gate of a MOSFET or IGBT
block.

### **LS** — Low-side source or emitter connection electrical

Electrical conserving port associated with the source or emitter on
the low side of the half bridge. Connect this port to the source of a
MOSFET block or the emitter of an IGBT block.

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

### **Low-side propagation delay (logic 0->logic 1)** — *t*pLH in timing diagram 50 ns (default)

Low-side propagation delay when the input logic goes from 0 to
1.

### **High-side dead time (logic 0->logic 1)** — *t*dLH in timing diagram 100 ns (default)

High-side dead time when the input logic goes from 0 to 1.

### **High-side propagation delay (logic 1->logic 0)** — *t*pHL in timing diagram 50 ns (default)

High-side propagation delay when the input logic goes from 1 to
0.

### **Low-side dead time (logic 1->logic 0)** — *t*dHL in timing diagram 100 ns (default)

Low-side dead time when the input logic goes from 1 to 0.

### Dynamics

### **Parameterization** — Select driver parameterization `Output impedance` (default) | `Rise and fall times`

Select the type of driver parameterization:

- `Output impedance` — Specify
  on-state and off-state gate drive resistances.
- `Rise and fall times` —
  Specify rise time, fall time, and load capacitance.

### **On-state gate drive resistance** — Demanded output voltage for on state 2 Ω (default)

Demanded output voltage when the driver is in on state.

#### Dependencies

Enabled when the **Parameterization** parameter
is set to `Output impedance`.

### **Off-state gate drive resistance** — Demanded output voltage for off state 2 Ω (default)

Demanded output voltage when the driver is in off state.

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

### **State fault** — Option to model faulty state in half-bridge driver `Add fault` (default)

Option to model a faulty state in the Half-Bridge Driver block.

To add a fault, click the **Add fault**
hyperlink.

### **Failure mode** — State of driver after failure `Fail input fixed at logic 0` (default) | `Fail input fixed at logic 1` | `Fail high side off` | `Fail high side on` | `Fail low side off` | `Fail low side on` | `Fail high and low sides off` | `Fail high and low sides on`

Select the driver state after the failure.

#### Dependencies

To enable this parameter, add a fault to the Half-Bridge Driver block by
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

Behavioral model of half-bridge driver integrated circuit

The Half-Bridge Driver block provides an abstracted representation of
an integrated circuit for driving MOSFET and IGBT half-bridges. The block models input
hysteresis, propagation delay, and turn-on/turn-off dynamics. Unless modeling a gate
driver circuit explicitly, always use this block or the Gate Driver block
to set gate-source voltage on a MOSFET block or gate-emitter voltage on an IGBT block.
Do not connect a controlled voltage source directly to a semiconductor gate, because
this omits the gate driver output impedance that determines switching dynamics.

You can model electrical or physical signal input ports by setting the **Modeling option** parameter to either:

- `PS input` — The driver output state is controlled by a physical signal input u. Use this modeling option if all of your controller, including PWM waveform generation, is determined by Simulink® blocks. This modeling option is the default.
- `Electrical input ports` — The driver output state is controlled by two electrical input connections, PWM and REF. Use this option if your model has upstream analog components, such as the Controlled PWM Voltage source.

The first pair of output electrical ports, HO and HS, behave in the same way as the G
and S ports of the Gate
Driver block. Connect these ports to the high-side MOSFET or IGBT of
the half-bridge. The second pair of ports, LO and LS, connect to the low-side MOSFET or
IGBT of the half-bridge. They behave in a similar way, except that their logic is
inverted with respect to that of the high side.

The diagram shows the timing properties for the half-bridge driver, where:

- *t*pLH is low-side propagation delay
  when the input logic goes from 0 to 1.
- *t*dLH is high-side dead time when the
  input logic goes from 0 to 1.
- *t*pHL is high-side propagation delay
  when the input logic goes from 1 to 0.
- *t*dHL is low-side dead time when the
  input logic goes from 1 to 0.

### Faults

To model a fault in the Half-Bridge Driver block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

You can insert a fault into one or both of the outputs at a specified simulation
time. The fault options are:

- Fail input fixed at logic 0
- Fail input fixed at logic 1
- Fail high side off
- Fail high side on
- Fail low side off
- Fail low side on
- Fail high and low sides off
- Fail high and low sides on
