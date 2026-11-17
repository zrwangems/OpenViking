---
type: simulink-block
title: 'Current-Controlled Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Passives'
documentation_page: 'currentcontrolledswitch'
documentation_source_path: 'ref/currentcontrolledswitch.html'
language: en
---

# Current-Controlled Switch

## Ports
```yaml
ports:
- name: 1+
  summary: Positive input port electrical
  direction: conserving
- name: 1-
  summary: Negative input port electrical
  direction: conserving
- name: 2+
  summary: Positive output port electrical
  direction: conserving
- name: 2-
  summary: Negative output port electrical
  direction: conserving
```

### Conserving

### **1+** — Positive input port electrical

Electrical conserving port associated with the current controlled
switch positive input.

### **1-** — Negative input port electrical

Electrical conserving port associated with the current controlled
switch negative input.

### **2+** — Positive output port electrical

Electrical conserving port associated with the current controlled
switch positive output.

### **2-** — Negative output port electrical

Electrical conserving port associated with the current controlled
switch negative output.
## Parameters
```yaml
parameters:
- name: Switch model
  summary: Switch model Abrupt transition after delay (default) | Smooth transition between Ion and Ioff
  group: ''
- name: Threshold current, IT
  summary: Threshold current 0 A (default)
  group: ''
- name: Hysteresis current, IH
  summary: Hysteresis current 0 A (default)
  group: ''
- name: Control current for on state, ION
  summary: Control current for on state 1e-3 A (default)
  group: ''
- name: Control current for off state, IOFF
  summary: Control current for off state 0 A (default)
  group: ''
- name: On resistance, RON
  summary: Closed switch resistance 1 Ohm (default)
  group: ''
- name: Use 1/GMIN as Off resistance
  summary: Whether to use 1/GMIN as off resistance No (default) | Yes
  group: ''
- name: Off resistance, ROFF
  summary: Open switch resistance 1e12 Ohm (default) | 1e6
  group: ''
- name: Time delay, TD
  summary: Time delay 0 s (default)
  group: ''
```

### **Switch model** — Switch model `Abrupt transition after delay` (default) | `Smooth transition between Ion and Ioff`

Whether the transition between on state and off state current is
instantaneous or not. To model this block as a variable-resistance switch,
select `Smooth transition between Ion and Ioff`. To
model this block as a short-transition switch, select `Abrupt
transition after delay`.

### **Threshold current, IT** — Threshold current `0` `A` (default)

Current above which the block interprets the controlling current as
HIGH.

**Note**

The controlling current must differ from the threshold current by at
least the **Hysteresis current, IH** parameter value to
change the state of the switch.

#### Dependencies

To enable this parameter, set **Switch model** to
`Abrupt transition after delay`.

### **Hysteresis current, IH** — Hysteresis current `0` `A` (default)

Amount by which the controlling current must exceed or fall below the
**Threshold current, IT** parameter value to change the
state of the switch.

#### Dependencies

To enable this parameter, set **Switch model** to
`Abrupt transition after delay`.

### **Control current for on state, ION** — Control current for on state `1e-3` `A` (default)

Switch control current for the on state.

#### Dependencies

To enable this parameter, set **Switch model** to
`Smooth transition between Ion and
Ioff`.

### **Control current for off state, IOFF** — Control current for off state `0` `A` (default)

Switch control current for the off state.

#### Dependencies

To enable this parameter, set **Switch model** to
`Smooth transition between Ion and
Ioff`.

### **On resistance, RON** — Closed switch resistance `1` `Ohm` (default)

Resistance of the switch when it is closed.

### **Use 1/GMIN as Off resistance** — Whether to use 1/GMIN as off resistance `No` (default) | `Yes`

Whether to automatically calculate the off resistance of this switch as
`1/GMIN`.

**Note**

The value of the parallel conductance, *GMIN*, depends on whether your model contains an
Environment Parameters block.

By default, *GMIN* matches the
**GMIN** parameter of the
Environment Parameters block, whose
default value is 1e–12. To change *GMIN*, add an
Environment Parameters block to your
model and set the **GMIN** parameter to the desired
value.

#### Dependencies

To enable this parameter, set **Switch model** to
`Abrupt transition after delay`.

### **Off resistance, ROFF** — Open switch resistance `1e12` `Ohm` (default) | `1e6`

Resistance of the switch when it is open.

#### Dependencies

To enable this parameter either:

- Set **Switch model** to
  `Abrupt transition after delay`
  and **Use 1/GMIN as Off resistance** to
  `No`. The default value is
  `1e12`.
- Set **Switch model** to
  `Smooth transition between Ion and
  Ioff`. The default value is
  `1e6`.

### **Time delay, TD** — Time delay `0` `s` (default)

Time delay after which the switch transition takes place.

#### Dependencies

To enable this parameter, set **Switch model** to
`Abrupt transition after delay`.
## Libraries

Simscape / Electrical / Additional Components / SPICE Passives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Current-controlled switch with hysteresis

The Current-Controlled Switch block represents the
electrical characteristics of a switch whose state is controlled by the current through
the input ports (the *controlling current*).

This block models either a variable-resistance or a short-transition switch. For a
variable-resistance switch, set the **Switch model** parameter to
`Smooth transition between Ion and Ioff`. For a
short-transition switch, set **Switch model** to `Abrupt
transition after delay`.

### Short-transition Switch

In a short-transition switch, the transition between the off and on states is
instantaneous:

- When the controlling current is greater than or equal to the sum of
  the **Threshold current, IT** and **Hysteresis
  current, IH** parameter values, the switch is closed and
  has a resistance equal to the **On resistance, RON**
  parameter value.
- When the controlling current is less than the **Threshold
  current, IT** parameter value minus the
  **Hysteresis current, IH** parameter value, the
  switch is open and has a resistance equal to the **Off
  resistance, ROFF** parameter value.
- When the controlling current is greater than or less than the
  **Threshold current, IT** parameter value by an
  amount less than or equal to the **Hysteresis current,
  IH** parameter value, the current is in the
  *crossover region* and the state of the switch
  remains unchanged.

**Note**

If the **Hysteresis current, IH** parameter value is less
than `0`, the block models a variable-resistance switch
independently of the value you set for the **Switch model**
parameter.

### Variable-resistance Switch

In a variable-resistance switch, the transition between the off and on states is exponential:

- When the **Control current for on state, ION** is
  greater than the **Control current for off state,
  IOFF**:

  - If the controlling current is greater than the
    **Control current for on state, ION**
    parameter value, the switch is closed and has a resistance
    equal to the **On resistance, RON**
    parameter value.
  - If the controlling current is less than the
    **Control current for off state, IOFF**
    parameter value, the switch is open and has a resistance
    equal to the **Off resistance, ROFF**
    parameter value.
  - If the controlling current is greater than the
    **Control current for off state, IOFF**
    parameter value or less than the **Control current
    for on state, ION** parameter value, the
    resistance is defined by:

    Rs=exp[Lm+3Lr(Ic−Im2Id)−2Lr((Ic−Im)3Id3)]

    where:

    - *Rs* is the switch
      resistance.
    - Lm=ln[(RON\*ROFF)12] is the log-mean of resistor
      values.
    - Lr=ln(RONROFF) is the log-ratio of resistor
      values.
    - *Ic* is the controlling
      current.
    - Im=ION+IOFF2 is the mean of the control
      currents.
    - Id=ION−IOFF is the difference between the
      control currents.
- When the **Control current for on state, ION** is
  less than the **Control current for off state, IOFF**:

  - If the controlling current is less than the
    **Control current for on state, ION**
    parameter value, the switch is closed and has a resistance
    equal to the **On resistance, RON**
    parameter value.
  - If the controlling current is greater than the
    **Control current for off state, IOFF**
    parameter value, the switch is open and has a resistance
    equal to the **Off resistance, ROFF**
    parameter value.
  - If the controlling current is less than the
    **Control current for off state, IOFF**
    parameter value or greater than the **Control
    current for on state, ION** parameter value,
    the resistance is defined by:

    Rs=exp[Lm+3Lr(Ic−Im2Id)−2Lr((Ic−Im)3Id3)]
