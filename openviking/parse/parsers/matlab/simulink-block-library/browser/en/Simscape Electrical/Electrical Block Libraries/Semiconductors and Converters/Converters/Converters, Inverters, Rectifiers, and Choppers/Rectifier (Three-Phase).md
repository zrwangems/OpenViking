---
type: simulink-block
title: 'Rectifier (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'rectifierthreephase'
documentation_source_path: 'ref/rectifierthreephase.html'
language: en
---

# Rectifier (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
port.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
terminal.

## Parameters

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Forward voltage** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the `+` and
`-` ports of each diode for the gradient of the
diode i-v characteristic to be
1/*Ron*, where
*Ron*is the value of
**On resistance**.

### **On resistance** — On resistance `0.001` `Ohm` (default)

Rate of change of voltage versus current above the forward voltage for
each diode.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

Conductance of each reverse-biased diode.

### Charge Dynamics

### **Model dynamics** — Diode charge dynamics `No dynamics` (default) | `Model charge dynamics`

Diode charge dynamics. The default value is `No
dynamics`.

The charge dynamics options you can select are:

- `No dynamics`
- `Model charge dynamics`

### **Junction capacitance** — Junction capacitance `50e-9` `F` (default)

Diode junction capacitance.

#### Dependencies

This parameter is visible only when the **Model dynamics** parameter is set
to `Model charge dynamics`.

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit. This value must be less than
zero.

#### Dependencies

This parameter is visible only when the **Model dynamics** parameter is set
to `Model charge dynamics`.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current. This value must be greater than zero.

#### Dependencies

This parameter is visible only when the **Model dynamics**
parameter is set to `Model charge dynamics`.

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-50``A/μs` (default) | negative scalar

Rate of change of current when measuring peak reverse current. This value must be less than zero.

#### Dependencies

This parameter is visible only when the **Model dynamics**
parameter is set to `Model charge dynamics`.

### **Reverse recovery time parameterization** — Reverse recovery time parameterization `Specify stretch factor` (default) | `Specify reverse recovery time directly` | `Specify reverse recovery charge`

Determines how you specify reverse recovery time in the block. The default value is `Specify reverse recovery time directly`.

If you select `Specify stretch factor` or `Specify reverse recovery charge`, you specify a value that the block uses to derive the reverse recovery time. For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

This parameter is visible only when the **Model dynamics**
parameter is set to `Model charge dynamics`.

### **Reverse recovery time, trr** — Reverse recovery time `15` `μs` (default)

Interval between the time when the current initially goes to zero (when the diode turns off) and the time when the current falls to less than 10% of the peak reverse current. The value of the **Reverse recovery time, trr** parameter must be greater than the value of the **Peak reverse current, iRM** parameter divided by the value of the **Rate of change of current when measuring iRM** parameter.

#### Dependencies

This parameter is visible only when the **Model dynamics** parameter is set
to `Model charge dynamics` and the **Reverse
recovery time parameterization** parameter is set to
`Specify reverse recovery time directly`.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default)

Value that the block uses to calculate **Reverse recovery time, trr**. This value must be greater than `1`. Specifying the stretch factor is an easier way to parameterize the reverse recovery time than specifying the reverse recovery charge. The larger the value of the stretch factor, the longer it takes for the reverse recovery current to dissipate.

#### Dependencies

This parameter is visible only when the **Model dynamics** parameter is set
to `Model charge dynamics` and the **Reverse
recovery time parameterization** parameter is set to
`Specify stretch factor`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `μAs` (default)

Value that the block uses to calculate **Reverse recovery time, trr**. Use this parameter if the data sheet for your diode device specifies a value for the reverse recovery charge instead of a value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to dissipate when the diode turns off. The value must be less than −i2RM2a,

where:

- *iRM* is the value specified for **Peak reverse current, iRM**.
- *a* is the value specified for **Rate of change of current when measuring iRM**.

#### Dependencies

This parameter is visible only when the **Model dynamics** parameter is set
to `Model charge dynamics` and the **Reverse
recovery time parameterization** parameter is set to
`Specify reverse recovery charge`.

For more information on these parameters, see Diode.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Uncontrolled three-phase AC to DC voltage

The Rectifier (Three-Phase) block models a three-arm diode bridge
circuit that converts a three-phase AC voltage to a DC voltage. The figure shows the
equivalent circuit for the three-arm diode bridge.

Using the Charge Dynamics tab of the block dialog box, you can choose the type of
diode that the three-arm bridge circuit uses. The table shows you how to set the
**Model dynamics** parameter based on your goals.

| Goal | Value to Select | Block Behavior |
| --- | --- | --- |
| Prioritize simulation speed. | `No dynamics` | Each arm of the bridge circuit uses a copy of the Diode block. The block dialog box does not display additional parameters. |
| Precisely specify reverse-mode charge dynamics. | `Model charge dynamics` | Each arm of the bridge circuit uses a copy of the commutation model of the Diode block. The block dialog box shows parameters relating to the commutation model of the block. |
