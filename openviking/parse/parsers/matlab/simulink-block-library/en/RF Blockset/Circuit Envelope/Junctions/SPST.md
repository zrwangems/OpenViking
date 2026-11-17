---
type: simulink-block
title: 'SPST'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'spst'
documentation_source_path: 'ref/spst.html'
language: en
---

# SPST

## Ports
```yaml
ports:
- name: Vctl
  summary: Simulink control signal scalar
  direction: input
  data_types: double
```

### Input

### **Vctl** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Threshold voltage
  summary: Threshold voltage 0 (default) | positive scalar
  group: ''
- name: Characterization
  summary: Characterization Resistance (default) | Insertion loss
  group: ''
- name: On resistance
  summary: On resistance 10 (default) | positive scalar
  group: ''
- name: Off resistance
  summary: Off resistance 1e-6 (default) | positive scalar
  group: ''
- name: Insertion loss (dB)
  summary: Insertion loss 1 (default) | scalar
  group: ''
- name: Isolation (dB)
  summary: Isolation value 70 (default) | scalar
  group: ''
- name: Loading type
  summary: Loading type Reflective (default) | Absorptive
  group: ''
- name: Port terminations (Ohm)
  summary: Port terminations 50 (default) | scalar | vector of size 1-by-2
  group: ''
- name: Ground and hide reference terminals
  summary: Ground RF circuit terminals on (default) | off
  group: ''
```

### **Threshold voltage** — Threshold voltage `0` (default) | positive scalar

Threshold voltage of the switch, specified as a positive scalar in volts.

### **Characterization** — Characterization `Resistance` (default) | `Insertion loss`

Characterization of the switch, specified as `Resistance`
or `Insertion loss`.

### **On resistance** — On resistance `10` (default) | positive scalar

On resistance value of the switch, specified as a positive scalar in ohms.
**On resistance** is available when you set
**Characterization** to `Resistance`.

### **Off resistance** — Off resistance `1e-6` (default) | positive scalar

Off resistance value of the switch, specified as a positive scalar in ohms.
**Off resistance** is available when you set
**Characterization** to `Resistance`.

### **Insertion loss (dB)** — Insertion loss `1` (default) | scalar

Insertion loss value of the switch, specified as a positive scalar in decibels.
**Insertion loss (dB)** is available when you set
**Characterization** to `Insertion
loss`.

### **Isolation (dB)** — Isolation value `70` (default) | scalar

Isolation value of the switch, specified as a scalar in decibels.
**Isolation (dB)** is available when you set
**Characterization** to `Insertion
loss`.

### **Loading type** — Loading type `Reflective` (default) | `Absorptive`

Loading type of the switch, specified as `Reflective` or
`Absorptive`.

### **Port terminations (Ohm)** — Port terminations `50` (default) | scalar | vector of size 1-by-2

Port terminations that match the impedance conditions of the `SPDT`
switch, specified as a scalar in ohms or a vector of size 1-by-2 with each element unit
in ohms. If the value is a scalar, then the input port and the output port impedances
are the same. If the value is a vector, the first value is the matching required at the
inport of the block and the second values is the matching required at the output
port.

**Note**

**Port terminations** is available when you set the
`SPST` switch **Characterization** to
`Insertion loss` or when you set **Loading
type** to `Absorptive`.

### **Ground and hide reference terminals** — Ground RF circuit terminals on (default) | off

Select this parameter to internally ground and hide the reference terminals. To
expose the reference terminals, clear this parameter. By exposing these terminal, you
can connect them to other parts of your model.
## Libraries

RF Blockset / Circuit Envelope / Junctions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Single pole single throw switch

The SPST block models a single pole single throw switch. This block
supports both reflective and absorptive switches. The control signal is a Simulink® signal connected to the `Vctl` port of the block. The control
signal specifies when the output port, `Out`, transmits the input signal at
the input port, `In`.
