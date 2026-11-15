---
type: simulink-block
title: 'Variable Phase Shift'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Simulink Controlled Elements'
documentation_page: 'variablephaseshift'
documentation_source_path: 'ref/variablephaseshift.html'
language: en
---

# Variable Phase Shift

## Ports

### Input

### **Phase** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`

## Parameters

### **Phase shift unit** — Angle units for controlling phase of circuit `rad` (default) | `deg`

Angle units for controlling the phase of the signal, specified
as `rad` for radians or `deg` for
degrees.

### **Reference impedances (Ohm)** — Reference impedance for phase shifter `50` (default) | vector of real positive scalars | real scalar

Reference impedance for phase shifter, specified as a scalar or vector of positive scalars in ohms.

**Note**

For non-50 ohm reference impedances, the model inside the Phase
Shift block is normalized to 50 ohms.

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

### R2021b: Variable Phase Shift block icon updated

Starting in R2021b, the Variable Phase Shift block icon is now
updated. When you open a model created before R2021b containing a Variable
Phase Shift block, the software replaces the block icon with the R2021b
version.

## Description

Model variable phase device

The Variable Phase Shift block controls the phase
of the output signal of a RF Blockset™ circuit. The block uses
a Simulink® signal to control the phase of the circuit. One input
terminal is for the Simulink control signal and one input terminal
is for the RF Blockset signal.

Phase shifter are commonly used in phased array antenna systems.
In these systems, electronically controlled phase shifters steer the
antenna beam in space. Phase shifters are also used in test and measurement
systems.
