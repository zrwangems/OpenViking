---
type: simulink-block
title: 'Incandescent Lamp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'incandescentlamp'
documentation_source_path: 'ref/incandescentlamp.html'
language: en
---

# Incandescent Lamp

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the lamp positive
voltage.

### **-** — Negative terminal electrical

Electrical conserving port associated with the lamp negative
voltage.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Block parameterization Specify resistance values directly (default) | Specify currents
  group: Resistance
- name: Initial resistance at turn-on
  summary: Initial resistance at turn-on 0.15 Ohm (default)
  group: Resistance
- name: Steady-state resistance when on
  summary: Steady-state resistance when on 1 Ohm (default)
  group: Resistance
- name: Inrush current at turn-on
  summary: Inrush current at turn-on 70 A (default)
  group: Resistance
- name: Steady-state current when on
  summary: Steady-state current when on 10 A (default)
  group: Resistance
- name: Rated voltage
  summary: Lamp rated voltage 12 V (default)
  group: Resistance
- name: Resistance temperature coefficient
  summary: Resistance temperature coefficient 0.004 1/K (default)
  group: Resistance
- name: Thermal time constant
  summary: Thermal time constant 25 ms (default)
  group: Dynamics
- name: Initial lamp state
  summary: Initial lamp state Off (default) | On
  group: Dynamics
- name: Open circuit fault
  summary: Option to add open circuit fault Add fault (default)
  group: Faults
- name: Open-circuit resistance
  summary: Open-circuit resistance 1e6 Ohm (default)
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state 0 s (default) | nonnegative scalar
  group: Faults
```

### Resistance

### **Parameterization** — Block parameterization `Specify resistance values directly` (default) | `Specify currents`

Select one of the following methods for block parameterization:

- `Specify resistance values
  directly` — Provide the values for
  filament resistance at turn-on and when on in steady state.
  The block determines the value for the heat transfer
  coefficient based on these values. This is the default
  option.
- `Specify currents` —
  Provide the values for filament current at turn-on and when
  on in steady state. The block determines the value for the
  heat transfer coefficient based on these values.

### **Initial resistance at turn-on** — Initial resistance at turn-on `0.15` `Ohm` (default)

The resistance seen by the external circuit when the lamp is initially
turned on.

#### Dependencies

This parameter is visible only when you select
`Specify resistance values directly`
for the **Parameterization** parameter.

### **Steady-state resistance when on** — Steady-state resistance when on `1` `Ohm` (default)

The resistance seen by the external circuit when the lamp is on and in
steady state. This resistance should be greater than the
**Initial resistance at turn-on**.

#### Dependencies

This parameter is visible only when you select
`Specify resistance values directly`
for the **Parameterization** parameter.

### **Inrush current at turn-on** — Inrush current at turn-on `70` `A` (default)

The current through the lamp when it is initially turned on.

#### Dependencies

This parameter is visible only when you select
`Specify currents` for the
**Parameterization** parameter.

### **Steady-state current when on** — Steady-state current when on `10` `A` (default)

The current through the lamp when it is on and in steady state. This
current should be less than the **Inrush current at
turn-on**.

#### Dependencies

This parameter is visible only when you select
`Specify currents` for the
**Parameterization** parameter.

### **Rated voltage** — Lamp rated voltage `12` `V` (default)

The rated voltage for the lamp, and the voltage value for which the
resistance or current values are provided in the on and turn-on
states.

### **Resistance temperature coefficient** — Resistance temperature coefficient `0.004` `1/K` (default)

The fractional increase in resistance per unit increase in
temperature.

### Dynamics

### **Thermal time constant** — Thermal time constant `25` `ms` (default)

The first-order thermal time constant for filament temperature when
the lamp is turned on or off.

### **Initial lamp state** — Initial lamp state `Off` (default) | `On`

Select between `On` and
`Off`.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an open-circuit fault in the Incandescent Lamp block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit resistance** — Open-circuit resistance `1e6` `Ohm` (default)

Value of the filament resistance when the lamp goes
open-circuit.

#### Dependencies

To enable this parameter, add a fault to the Incandescent Lamp block by
clicking the **Add fault** hyperlink in the
**Open circuit fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

For simulation times greater than this parameter value the filament
resistance becomes equal to the **Open-circuit
resistance**. Specifying a finite value for this parameter
lets you simulate the fault dynamics when the bulb burns out.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Incandescent lamp with temperature dependent resistance

The Incandescent Lamp block models an incandescent
lamp, the key characteristic of which is that the resistance increases as the filament
warms up.

Under the simplifying assumption that the rate of heat loss from the filament is
proportional to temperature difference to ambient, the temperature of the filament is
governed by

ktcdTdt=i2R−kT

and the filament resistance is governed by the following equation

R=R0(1+αT)

where:

- *R0* is the initial resistance at
  turn-on (when filament is at ambient temperature).
- *T* is the filament temperature relative to ambient
  temperature.
- α is the resistance temperature coefficient.
- *tc* is the thermal time constant.
- *k* is the heat transfer coefficient.
- *R* is the filament resistance.
- *i* is the filament current.

There are two parameterization options:

- If you select `Specify resistance values directly`,
  the block uses values that you provide for filament resistance when on and at
  turn-on to determine the value for the heat transfer coefficient.
- If you select `Specify currents`, the block uses
  values that you provide for filament current when on and at turn-on to determine
  the value for the heat transfer coefficient.

### Faults

To model a fault in the Incandescent Lamp block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Incandescence Lamp block allows you to model an
electrical fault as an open circuit resistance. The block can trigger fault events
at a specific time. When in the open-circuit state, the lamp resistance is set to
be the value of the **Open-circuit resistance** parameter.
