---
type: simulink-block
title: 'Voltage-Controlled Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Passives'
documentation_page: 'voltagecontrolledswitch'
documentation_source_path: 'ref/voltagecontrolledswitch.html'
language: en
---

# Voltage-Controlled Switch

## Ports

### Conserving

### **1+** — Positive input port electrical

Electrical conserving port associated with the voltage controlled
switch positive input.

### **1-** — Negative input port electrical

Electrical conserving port associated with the voltage controlled
switch negative input.

### **2+** — Positive output port electrical

Electrical conserving port associated with the voltage controlled
switch positive output.

### **2-** — Negative output port electrical

Electrical conserving port associated with the voltage controlled
switch negative output.

## Parameters

### **Switch model** — Switch model `Abrupt transition after delay` (default) | `Smooth transition between Ion and Ioff`

Whether the transition between on state and off state current is
instantaneous or not. To model this block as a variable-resistance switch,
select `Smooth transition between Ion and Ioff`. To
model this block as a short-transition switch, select `Abrupt
transition after delay`.

### **Threshold voltage, VT** — Threshold voltage `0` `V` (default)

Voltage above which the block interprets the controlling voltage as
HIGH.

**Note**

The controlling voltage must differ from the threshold voltage by at
least the **Hysteresis voltage, VH** parameter value to
change the state of the switch.

#### Dependencies

To enable this parameter, set **Switch model** to
`Abrupt transition after delay`.

### **Hysteresis voltage, VH** — Hysteresis voltage `0` `V` (default)

Amount by which the controlling voltage must exceed or fall below the
**Threshold voltage, VT** parameter value to change the
state of the switch.

#### Dependencies

To enable this parameter, set **Switch model** to
`Abrupt transition after delay`.

### **Control voltage for on state, VON** — Control voltage for on state `1e-3` `V` (default)

Switch control voltage for the on state.

#### Dependencies

To enable this parameter, set **Switch model** to
`Smooth transition between Von and
Voff`.

### **Control voltage for off state, IOFF** — Control voltage for off state `0` `V` (default)

Switch control voltage for the off state.

#### Dependencies

To enable this parameter, set **Switch model** to
`Smooth transition between Von and
Voff`.

### **On resistance, RON** — Closed switch resistance `1` `Ohm` (default)

Resistance of the switch when it is closed.

### **Use 1/GMIN as Off resistance** — Whether to use 1/GMIN as off resistance `No` (default) | `Yes`

Whether to automatically calculate the off resistance of this switch as
`1/GMIN`.

**Note**

The value of the parallel conductance, *GMIN*, depends on whether your model contains an
Environment Parameters
block.

By default, *GMIN* matches the
**GMIN** parameter of the
Environment Parameters block,
whose default value is 1e–12. To change *GMIN*, add
an Environment Parameters block to
your model and set the **GMIN** parameter to the
desired value.

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
  `Smooth transition between Von and
  Voff`. The default value is
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

Voltage-controlled switch with hysteresis

The Voltage-Controlled Switch block represents the
electrical characteristics of a switch whose state is controlled by the voltage across
the input ports (the *controlling voltage*).

This block models either a variable-resistance or a short-transition switch. For a
variable-resistance switch, set the **Switch model** parameter to
`Smooth transition between Von and Voff`. For a
short-transition switch, set **Switch model** to `Abrupt
transition after delay`.

### Short-transition Switch

In a short-transition switch, the transition between the off and on states is
instantaneous:

- When the controlling voltage is greater than or equal to the sum of the
  **Threshold voltage, VT** and **Hysteresis
  voltage, VH** parameter values, the switch is closed and has a
  resistance equal to the **On resistance, RON** parameter
  value.
- When the controlling voltage is less than the **Threshold voltage,
  VT** parameter value minus the **Hysteresis voltage,
  VH** parameter value, the switch is open and has a resistance
  equal to the **Off resistance, ROFF** parameter
  value.
- When the controlling voltage is greater than or less than the
  **Threshold voltage, VT** parameter value by an amount
  less than or equal to the **Hysteresis voltage, VH**
  parameter value, the voltage is in the *crossover
  region* and the state of the switch remains unchanged.

**Note**

If the **Hysteresis voltage, VH** parameter value is less
than `0`, the block models a variable-resistance switch
independently of the value you set for the **Switch model**
parameter.

### Variable-resistance Switch

In a variable-resistance switch, the transition between the off and on states is exponential:

- When the **Control voltage for on state, VON** is
  greater than the **Control voltage for off state,
  VOFF**:

  - If the controlling voltage is greater than the
    **Control voltage for on state, VON**
    parameter value, the switch is closed and has a resistance
    equal to the **On resistance, RON**
    parameter value.
  - If the controlling voltage is less than the
    **Control voltage for off state, VOFF**
    parameter value, the switch is open and has a resistance
    equal to the **Off resistance, ROFF**
    parameter value.
  - If the controlling voltage is greater than the
    **Control voltage for off state, VOFF**
    parameter value or less than the **Control voltage
    for on state, VON** parameter value, the
    resistance is defined by:

    Rs=exp[Lm+3Lr(Vc−Vm2Vd)−2Lr((Vc−Vm)3Vd3)]

    where:

    - *Rs* is the switch
      resistance.
    - Lm=ln[(RON\*ROFF)12] is the log-mean of resistor
      values.
    - Lr=ln(RONROFF) is the log-ratio of resistor
      values.
    - *Vc* is the controlling
      voltage.
    - Vm=VON+VOFF2 is the mean of the control
      voltages.
    - Vd=VON−VOFF is the difference between the
      control voltages.
- When the **Control voltage for on state, VON** is
  less than the **Control voltage for off state, VOFF**:

  - If the controlling voltage is less than the
    **Control voltage for on state, VON**
    parameter value, the switch is closed and has a resistance
    equal to the **On resistance, RON**
    parameter value.
  - If the controlling voltage is greater than the
    **Control voltage for off state, VOFF**
    parameter value, the switch is open and has a resistance
    equal to the **Off resistance, ROFF**
    parameter value.
  - If the controlling voltage is less than the
    **Control voltage for off state, VOFF**
    parameter value or greater than the **Control
    voltage for on state, VON** parameter value,
    the resistance is defined by:

    Rs=exp[Lm+3Lr(Ic−Im2Id)−2Lr((Ic−Im)3Id3)]
