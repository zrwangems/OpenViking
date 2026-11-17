---
type: simulink-block
title: 'Resistor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'resistor'
documentation_source_path: 'ref/resistor.html'
language: en
---

# Resistor

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Resistance
  summary: Resistance value 50 Ohm (default) | real number in ohms
  group: ''
- name: Simulate noise
  summary: Simulate thermal noise on (default) | off
  group: ''
```

### **Resistance** — Resistance value `50 Ohm` (default) | real number in ohms

Resistance value , specified as a real number in ohms greater
than zero. Specify the units of the resistance from the corresponding
drop-down menu.

### **Simulate noise** — Simulate thermal noise `on` (default) | `off`

Select this parameter, to simulate thermal noise in a resistor.
Then, in the Configuration block dialog
box, also select the **Simulate noise** check box.
By default, both **Simulate noise** check boxes are
selected.

This parameter inserts a current noise source with the single-sided power density of 4
*k**T*/*R*
A2/Hz, where:

- k is the Boltzmann constant
- T is the value of the **Temperature** parameter,
  in degrees Kelvin. (Also located in the Configuration block.)
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

### R2021b: Resistor block icon updated

Starting in R2021b, the Resistor block icon is now
updated. The block icons are now dynamic and show the current state
of the noise parameter.

When you open a model created before R2021b containing a
Resistor block, the software replaces the
block icon with the R2021b version.

## Description

Model resistor for circuit envelope analysis

The Resistor block models a resistor within the RF Blockset™ circuit
envelope simulation environment. For an introduction to RF simulation,
see the example, Simulate High Frequency Components.

The block implements the relation

v(t)=Ri(t)

where:

- *R* represents the resistance, as
  a function of temperature.
- *i*(*t*) represents
  the current through the capacitor at time *t*.
- *v*(*t*) represents
  the voltage across the terminals of the capacitor at time *t*.

RF Blockset current and voltage signals consist of in-phase
(*Ik*) and quadrature (*Qk*)
components at each frequency *fk* specified
in the Configuration block:

i(t)=∑{fk}(iIk(t)+j⋅iQk(t))ej(2πfk)tv(t)=∑{fk}(vIk(t)+j⋅vQk(t))ej(2πfk)t

Resistor block mask icons are dynamic and indicate the current
state of the applied noise parameter. This table shows you how the icons on
this block vary based on the state of the **Simulate
noise** parameter on the block.

| Simulate noise: on | Simulate noise: off |
| --- | --- |
| Resistor block icon with Simulate noise is set to on. | Resistor block icon with Simulate noise is set to off. |

To learn how you can use the Resistor block to design output
matching network, open *RF Receiver Front End*  subsystem
and select *Linear* → *Output
Matching* in Radar System Modeling example.
