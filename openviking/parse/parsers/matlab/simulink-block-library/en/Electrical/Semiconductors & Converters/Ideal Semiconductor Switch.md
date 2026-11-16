---
type: simulink-block
title: 'Ideal Semiconductor Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'idealsemiconductorswitch'
documentation_source_path: 'ref/idealsemiconductorswitch.html'
language: en
---

# Ideal Semiconductor Switch

## Ports

### Input

### **G** — Gate terminal physical signal

Physical signal port associated with the gate terminal.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS control port`.
### Conserving

### **G** — Gate terminal electrical

Electrical conserving port associated with the gate terminal.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical control port`.

### **A** — Anode terminal electrical

Electrical conserving port associated with the anode terminal.

### **K** — Cathode terminal electrical

Electrical conserving port associated with the cathode
terminal.

## Parameters

### Main

### **Gate-control port** — Whether to specify physical or electrical control port `PS` (default) | `Electrical`

Whether to specify physical or electrical control port for the switch
gate.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

### **Off-state conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Anode-cathode conductance when the device is off. The value must be
less than 1/R, where R is the value of **On-state
resistance**.

### **Threshold voltage, Vth** — Threshold voltage `0.5` `V` (default)

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

### Integral Diode

### **Integral protection diode** — Integral protection diode `External diode` (default) | `Protection diode with no dynamics` | `Protection diode with charge dynamics`

Specify whether the block includes an integral protection
diode.

If you want to include an integral protection diode, there are two
options:

- `Protection diode with no
  dynamics`
- `Protection diode with charge
  dynamics`

### **Forward voltage** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the `+` and
`-` block ports for the gradient of the diode I-V
characteristic to be 1/Ron, where
Ron is the value of **On
resistance**.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Protection diode with no
dynamics` or `Protection diode with
charge dynamics`.

### **On resistance** — On resistance `0.001` `Ohm` (default)

Rate of change of voltage versus current above the **Forward
voltage**.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Protection diode with no
dynamics` or `Protection diode with
charge dynamics`.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

Conductance of the reverse-biased diode.

#### Dependencies

This parameter is visible only when the **Integral
protection diode** parameter is set to
`Protection diode with no dynamics` or
`Protection diode with charge
dynamics`.

### **Junction capacitance** — Junction capacitance `50e-9` `F` (default)

Diode junction capacitance.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-50``A/μs` (default) | negative scalar

Rate of change of current when measuring peak reverse current. This value must be less than zero.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Reverse recovery time parameterization** — Reverse recovery time parameterization `Specify reverse recovery time directly` (default) | `Specify stretch factor` | `Specify reverse recovery charge`

Determines how you specify reverse recovery time in the block. The default value is `Specify reverse recovery time directly`.

If you select `Specify stretch factor` or `Specify reverse recovery charge`, you specify a value that the block uses to derive the reverse recovery time. For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Reverse recovery time, trr** — Reverse recovery time `15` `μs` (default) | scalar

Interval between the time when the current initially goes to zero (when the diode turns off) and the time when the current falls to less than 10% of the peak reverse current. The value of the **Reverse recovery time, trr** parameter must be greater than the value of the **Peak reverse current, iRM** parameter divided by the value of the **Rate of change of current when measuring iRM** parameter.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics` and the
**Reverse recovery time parameterization** parameter is set to
`Specify reverse recovery time directly`.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default) | scalar greater than `1`

Stretch factor that the block uses to calculate the reverse recovery time. Specifying
the stretch factor is an easier way to parameterize the reverse recovery time than
specifying the reverse recovery charge. The larger the value of the stretch factor, the
longer it takes for the reverse recovery current to dissipate.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics` and the
**Reverse recovery time parameterization** parameter is set to
`Specify stretch factor`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `μAs` (default)

Reverse recovery charge that the block uses to calculate the reverse recovery time.
Use this parameter if the data sheet for your diode device specifies a value for the
reverse recovery charge instead of a value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to dissipate when the diode
turns off. The value must be less than −i2RM2a, where:

- *iRM* is the value specified for **Peak reverse current, iRM**.
- *a* is the value specified for **Rate of change of current when measuring iRM**.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics` and the
**Reverse recovery time parameterization** parameter is set to
`Specify reverse recovery charge`.

For more information on these parameters, see Diode.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Ideal Semiconductor Switch

The Ideal Semiconductor Switch block models an ideal
semiconductor switching device.

The figure shows a typical *i-v characteristic* for an ideal
semiconductor switch.

If the gate-cathode voltage exceeds the specified threshold voltage, the ideal
semiconductor switch is in the on state. Otherwise the device is in the off
state.

In the on state, the anode-cathode path behaves like a linear resistor with
on-resistance *Ron*.

In the off state, the anode-cathode path behaves like a linear resistor with a low
off-state conductance *Goff*.

Using the **Integral Diode** parameters, you can include an integral
cathode-anode diode. An integral diode protects the semiconductor device by providing a
conduction path for reverse current. An inductive load can produce a high
reverse-voltage spike when the semiconductor device suddenly switches off the voltage
supply to the load.

The table shows you how to set the **Integral protection
diode** parameter based on your goals.

| Goal | Value to Select | Block Behavior |
| --- | --- | --- |
| Prioritize simulation speed. | `Diode with no dynamics` | The block includes an integral copy of the Diode block. To parameterize the internal Diode block, use the **Protection** parameters. |
| Precisely specify reverse-mode charge dynamics. | `Diode with charge dynamics` | The block includes an integral copy of the dynamic model of the Diode block. To parameterize the internal Diode block, use the **Protection** parameters. |
