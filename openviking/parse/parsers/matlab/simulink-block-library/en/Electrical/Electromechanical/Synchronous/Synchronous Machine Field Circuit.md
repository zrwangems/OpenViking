---
type: simulink-block
title: 'Synchronous Machine Field Circuit'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinefieldcircuit'
documentation_source_path: 'ref/synchronousmachinefieldcircuit.html'
language: en
---

# Synchronous Machine Field Circuit

## Ports
```yaml
ports:
- name: Efd
  summary: Field voltage physical
  direction: input
- name: Efd_pu
  summary: Per unit field voltage physical
  direction: input
- name: Ifd
  summary: Field current physical
  direction: output
- name: Ifd_pu
  summary: Per-unit field current physical
  direction: output
- name: fd+
  summary: Field winding positive terminal electrical
  direction: conserving
- name: fd-
  summary: Field winding negative terminal electrical
  direction: conserving
```

### Input

### **Efd** — Field voltage physical

Physical input port associated with the field voltage.

#### Dependencies

This port is visible only when you set the **PS input and
output unit** parameter to
`SI`.

### **Efd\_pu** — Per unit field voltage physical

Physical input port associated with the field voltage, in per-unit..

#### Dependencies

This port is visible only when you set the **PS input and
output unit** parameter to `Per
unit`.
### Output

### **Ifd** — Field current physical

Physical input port associated with the field current.

#### Dependencies

This port is visible only when you set the **PS input and
output unit** parameter to
`SI`.

### **Ifd\_pu** — Per-unit field current physical

Physical input port associated with the field current, in per-unit..

#### Dependencies

This port is visible only when you set the **PS input and
output unit** parameter to `Per
unit`.
### Conserving

### **fd+** — Field winding positive terminal electrical

Electrical conserving port associated with the field winding positive
terminal.

### **fd-** — Field winding negative terminal electrical

Electrical conserving port associated with the field winding negative
terminal.
## Parameters
```yaml
parameters:
- name: PS input and output unit
  summary: Unit-system configuration SI (default) | Per unit
  group: Main
- name: Rated apparent power
  summary: Rated apparent power 555e6 V*A (default)
  group: Main
- name: Rated electrical frequency
  summary: Nominal electrical frequency 60 Hz (default)
  group: Main
- name: Specify field circuit input required to produce rated terminal voltage at no load by
  summary: Specify field circuit input required to produce rated terminal voltage at no load by Field circuit current (default)
    | Field circuit voltage
  group: Main
- name: Field circuit current
  summary: Field circuit current 1300 A (default)
  group: Main
- name: Field circuit voltage
  summary: Field circuit voltage 92.95 V (default)
  group: Main
- name: Specify parameterization by
  summary: Machine parameterization Fundamental Parameters (default) | Standard Parameters
  group: Machine Parameters
- name: Stator d-axis mutual inductance (unsaturated), Ladu
  summary: Stator d-axis mutual inductance (unsaturated) 1.66 (default)
  group: Machine Parameters
- name: Rotor field circuit resistance, Rfd
  summary: Rotor field circuit resistance 0.0006 (default)
  group: Machine Parameters
- name: Stator leakage reactance, Xl
  summary: Stator leakage reactance 0.15 (default)
  group: Machine Parameters
- name: d-axis synchronous reactance, Xd
  summary: d-axis synchronous reactance 1.81 (default)
  group: Machine Parameters
- name: d-axis transient reactance, Xd'
  summary: d-axis transient reactance 0.3 (default)
  group: Machine Parameters
- name: d-axis subtransient reactance, Xd''
  summary: d-axis subtransient reactance 0.23 (default)
  group: Machine Parameters
- name: Specify d-axis time constant
  summary: d-axis time constant specification Open-circuit value (default) | Short-circuit value
  group: Machine Parameters
- name: d-axis transient open-circuit, Td0'
  summary: d-axis transient open-circuit 8 s (default)
  group: Machine Parameters
- name: d-axis transient short-circuit, Td'
  summary: d-axis transient short-circuit 1.3260 s (default)
  group: Machine Parameters
- name: d-axis subtransient open-circuit, Td0''
  summary: d-axis subtransient open-circuit 0.03 (default)
  group: Machine Parameters
- name: d-axis subtransient short-circuit, Td''
  summary: d-axis subtransient short-circuit 0.0230 (default)
  group: Machine Parameters
```

The additional parameters for this block are visibile only if you set the **PS
input and output unit** parameter to `Per
unit`.

### Main

### **PS input and output unit** — Unit-system configuration `SI` (default) | `Per unit`

Unit-system configuration for the block.

Selecting:

- `SI` exposes the SI ports.
- `Per unit` exposes the per-unit
  ports and parameters.

### **Rated apparent power** — Rated apparent power `555e6` `V*A` (default)

Rated apparent power of the connected machine.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default)

Nominal electrical frequency at which rated apparent power of the
connected machine is quoted.

### **Specify field circuit input required to produce rated terminal voltage at no load by** — Specify field circuit input required to produce rated terminal voltage at no load by `Field circuit current` (default) | `Field circuit voltage`

Choose between `Field circuit voltage` and
`Field circuit current`.

### **Field circuit current** — Field circuit current `1300` `A` (default)

This value is used to calculate the per-unit bases for the field
circuit (nonreciprocal per-unit system).

#### Dependencies

This parameter is visible only when you set the **Specify
field circuit input required to produce rated terminal voltage
at no load by** parameter to `Field circuit
current`.

### **Field circuit voltage** — Field circuit voltage `92.95` `V` (default)

This value is used to calculate the per-unit bases for the field
circuit (nonreciprocal per-unit system).

#### Dependencies

This parameter is visible only when you set the **Specify
field circuit input required to produce rated terminal voltage
at no load by** parameter to `Field circuit
voltage`.

### Machine Parameters

### **Specify parameterization by** — Machine parameterization `Fundamental Parameters` (default) | `Standard Parameters`

Choose between `Fundamental Parameters` and
`Standard Parameters`.

### **Stator d-axis mutual inductance (unsaturated), Ladu** — Stator d-axis mutual inductance (unsaturated) `1.66` (default)

Unsaturated stator d-axis mutual inductance.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Fundamental Parameters`.

### **Rotor field circuit resistance, Rfd** — Rotor field circuit resistance `0.0006` (default)

Rotor field-circuit resistance.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Fundamental Parameters`.

### **Stator leakage reactance, Xl** — Stator leakage reactance `0.15` (default)

Stator leakage reactance.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters`.

### **d-axis synchronous reactance, Xd** — d-axis synchronous reactance `1.81` (default)

The *d*-axis synchronous reactance.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters`.

### **d-axis transient reactance, Xd'** — d-axis transient reactance `0.3` (default)

The *d*-axis transient reactance.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters`.

### **d-axis subtransient reactance, Xd''** — d-axis subtransient reactance `0.23` (default)

*d*-axis subtransient reactance.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters`.

### **Specify d-axis time constant** — d-axis time constant specification `Open-circuit value` (default) | `Short-circuit value`

Choose between `Open-circuit value` and
`Short-circuit value`.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters`.

### **d-axis transient open-circuit, Td0'** — d-axis transient open-circuit `8` `s` (default)

The *d*-axis transient open-circuit time constant.
This parameter is visible only when **Specify d-axis transient
time constant** is set to `Open-circuit
value`.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters` and the
**Specify d-axis transient time constant** to
`Open-circuit value`.

### **d-axis transient short-circuit, Td'** — d-axis transient short-circuit `1.3260` `s` (default)

The *d*-axis transient short-circuit time constant.
This parameter is visible only when **Specify d-axis transient
time constant** is set to `Short-circuit
value`.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters` and the
**Specify d-axis transient time constant** to
`Short-circuit value`.

### **d-axis subtransient open-circuit, Td0''** — d-axis subtransient open-circuit `0.03` (default)

*d*-axis subtransient open-circuit.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters` and the
**Specify d-axis transient time constant** to
`Open-circuit value`.

### **d-axis subtransient short-circuit, Td''** — d-axis subtransient short-circuit `0.0230` (default)

*d*-axis subtransient short-circuit.

#### Dependencies

This parameter is visible only when you set the **Specify
parameterization by** parameter to
`Standard Parameters` and the
**Specify d-axis transient time constant** to
`Short-circuit value`.
## Libraries

Simscape / Electrical / Electromechanical / Synchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Synchronous machine field circuit per-unit interface with voltage input and current output

The Synchronous Machine Field Circuit block applies
specified voltage to, and measures current through, the field circuit of the synchronous
machine that it is connected to.

The SI model converts the SI values that you enter in the dialog box to per-unit
values for simulation. For information on the relationship between SI and per-unit
machine parameters, see Per-Unit Conversion for Machine Parameters.
For information on per-unit parameterization, see Per-Unit System of Units.

The block includes an electrical reference. The physical signal input
**Efd\_pu** defines the voltage and the physical signal output
**Ifd\_pu** provides the current, both in per-unit. The physical
signal input **Efd** defines the voltage, in V, and the physical signal
output **Ifd** provides the current, in A.

The per-unit bases are the nonreciprocal per-unit system, *Efd* and
*Ifd*, rather than the reciprocal per-unit system,
*efd* and *ifd*.

This figure shows the pu model of the Synchronous Machine Field
Circuit block.

This figure shows the SI model of the Synchronous Machine Field
Circuit block.
