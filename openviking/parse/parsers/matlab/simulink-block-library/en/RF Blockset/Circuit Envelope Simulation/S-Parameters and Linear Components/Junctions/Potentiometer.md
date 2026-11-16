---
type: simulink-block
title: 'Potentiometer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
documentation_page: 'potentiometer'
documentation_source_path: 'ref/potentiometer.html'
language: en
---

# Potentiometer

## Ports

Not documented in R2025b.

## Parameters

### **Minimum resistance** — Minimum input resistance of potentiometer `10 Ohm` (default) | positive scalar

Minimum input resistance of the potentiometer, specified as a positive
scalar in ohms.

**Data Types:** `double`

### **Maximum resistance** — Maximum input resistance of potentiometer `1e6 Ohm` (default) | positive scalar

Maximum input resistance of potentiometer, specified as a positive scalar
in ohms. This value must be greater than the minimum resistance.

**Data Types:** `double`

### **Potentiometer type** — Curve type of potentiometer `Linear` (default) | `Logarithmic` | `Antilog`

Curve type of the potentiometer, specified as
`Linear`,
`Logarithmic`,
`Antilog`.

**Data Types:** `char`

### **Percentage of resistance at half wiper** — Maximum input resistance of potentiometer positive scalar

Percentage of resistance at half wiper for logarithmic and antilog
potentiometer types, specified as a positive scalar. The valid values depend
on the potentiometer type:

- `Logarithmic` - Greater than 0 and
  less than 50. The default is 20.
- `Antilog` - Greater than 50 and less
  than 100. The default is 80.

#### Dependencies

To enable this parameter, select
`Logarithmic` or
`Antilog` in **Potentiometer
type**.

**Data Types:** `double`

## Libraries

RF Blockset / Circuit Envelope / Junctions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Simulink controlled potentiometer

The Potentiometer block models a variable resistor. The
Potentiometer block uses Simulink® signal as input control signal to vary the resistance between the positive
and the negative terminals.

The equations for the potentiometer voltage–current relationships when the control
signal varies between zero and one are:

Linear:            Vpot=Ipot.(Roff.Ctl+Ron.(1−Ctl))Logarithmic:   Vpot=Ipot.(C1.exp (C2.Ctl)+C3)Antilog:           Vpot=Ipot.(C1.log  (1+C2.Ctl)+C3.Ctl+Ron)

- Linear, Logarithmic, Antilog — Electrical characteristic of the
  potentiometer.
- `Ctl` — Simulink signal
- `Ron` — Minimum resistance
  of the potentiometer
- `Roff` — Maximum resistance
  of the potentiometer
