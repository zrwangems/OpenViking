---
type: simulink-block
title: 'Variable Attenuator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variableattenuator'
documentation_source_path: 'ref/variableattenuator.html'
language: en
---

# Variable Attenuator

## Ports

### Input

### **Att** — Simulink control signal scalar

Simulink control signal, specified as a
scalar. This control signal is an *Insertion Loss*  in dB.

**Data Types:** `double`

## Parameters

### **Minimum attenuation (dB)** — Lowest value for insertion loss or attenuation `0.001` (default) | scalar

Lowest value of insertion loss or attenuation to apply to the
signal, specified as a scalar in dB.

### **Maximum attenuation (dB)** — Highest value of insertion loss or attenuation `1000` (default) | scalar

Highest value of insertion loss or attenuation to apply to the
signal, specified as a scalar in dB.

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

### R2021b: Variable Attenuator block icon updated

Starting in R2021b, the Variable Attenuator block icon
is now updated. The block icons are now dynamic and show the current
state of the noise parameter.

When you open a model created before R2021b containing a
Variable Attenuator block, the software
replaces the block icon with the R2021b version.

## Description

Model variable attenuator

The Variable Attenuator block attenuates the
signal power by a given factor known as *Insertion Loss* in
dB. Using the Variable Attenuator block, you can vary
the attenuation of the input Simulink® signal during simulation.
Commonly, the block matches the impedance of the RF circuit at the
input and output ports. You can use attenuators to dampen the power
of the incoming signal to protect RF circuits.

Variable Attenuator block mask icons are dynamic and show the
current state of the applied noise parameter. This table shows you how the
icons on this block vary based on the state of the **Simulate
noise** parameter on the block.

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| Variable Attenuator block icon with Simulate noise is set to on. | Variable Attenuator block icon with Simulate noise is set to off. |
