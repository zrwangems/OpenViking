---
type: simulink-block
title: 'Attenuator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'attenuator'
documentation_source_path: 'ref/attenuator.html'
language: en
---

# Attenuator

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Attenuation (dB)
  summary: Level of insertion loss or attenuation 3 (default) | scalar
  group: ''
- name: Input impedance (Ohm)
  summary: Input impedance 50 (default) | scalar
  group: ''
- name: Output impedance (Ohm)
  summary: Output impedance 50 (default) | scalar
  group: ''
- name: Simulate noise
  summary: Simulate thermal noise on (default) | off
  group: ''
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: ''
```

### **Attenuation (dB)** — Level of insertion loss or attenuation `3` (default) | scalar

Level of insertion loss or attenuation to apply to the signal,
specified as a scalar in dB.

### **Input impedance (Ohm)** — Input impedance `50` (default) | scalar

Input impedance of the attenuator, specified as a scalar in
ohms.

### **Output impedance (Ohm)** — Output impedance `50` (default) | scalar

Output impedance of the attenuator, specified as a scalar in
ohms.

### **Simulate noise** — Simulate thermal noise on (default) | off

Select this parameter to simulate thermal noise in the attenuator.
You must select **Simulate noise** in the Configuration block.

This parameter inserts a current noise source with the single-sided power density of 4
*k**T*/*R*
A2/Hz, where:

- *T* is the value of the **Temperature** parameter
  in the Configuration block. Units
  are in degrees Kelvin.
- *k* is the Boltzmann constant.

### **Ground and hide negative terminals** — Ground RF circuit terminals on (default) | off

Select this parameter to ground and hide the negative terminals.
To expose the negative terminals, clear this parameter. By exposing
these terminals, you can connect them to other parts of your model.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

### R2021b: Attenuator block icon updated

Starting in R2021b, the Attenuator block icon is now
updated. The block icons are now dynamic and show the current state
of the noise parameter.

When you open a model created before R2021b containing an
Attenuator block, the software replaces the
block icon with the R2021b version.

## Description

Model attenuator for RF circuit

The Attenuator block to attenuates the signal
power by a given factor known as *Insertion Loss* in
dB. Commonly, the block matches the impedance of the RF circuit at
the input and output ports. You can use attenuators to dampen the
power of the incoming signal to protect RF circuits.

Attenuator block mask icons are dynamic and indicate the current state of the
applied noise parameter. This table shows you how the icons on this block
vary based on the state of the **Simulate noise** parameter
on the block.

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| Attenuator block icon with Simulate noise is set to on. | Attenuator block icon with Simulate noise is set to off. |
