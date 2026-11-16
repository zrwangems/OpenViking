---
type: simulink-block
title: 'Variable Inductor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variableinductor'
documentation_source_path: 'ref/variableinductor.html'
language: en
---

# Variable Inductor

## Ports

### Input

### **L** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`

## Parameters

The Variable Inductor block has no parameters.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

### R2021b: Variable Inductor block icon updated

Starting in R2021b, the Variable Inductor block icon is now
updated. When you open a model created before R2021b containing a Variable
Capacitor block, the software replaces the block icon with the R2021b
version.

## Description

Model variable inductor

The Variable Inductor block controls the output
of RF Blockset™ feedback circuits using Simulink® controlled
inductance in henries. The minimum value of the inductance (*Lmin*)
is a RF Blockset defined constant independent of the Simulink control
signal. The block has two electrical terminals. One terminal is for
the Simulink control signal and one terminal is for the RF Blockset
signal.
