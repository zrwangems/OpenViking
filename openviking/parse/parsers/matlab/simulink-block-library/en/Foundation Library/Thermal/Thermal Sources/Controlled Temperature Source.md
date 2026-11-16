---
type: simulink-block
title: 'Controlled Temperature Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'controlledtemperaturesource'
documentation_source_path: 'ref/controlledtemperaturesource.html'
language: en
---

# Controlled Temperature Source

## Ports

### Input

### **S** — Temperature control signal, K physical signal

Input physical signal that specifies the temperature difference across
the source.
### Conserving

### **A** — Source inlet thermal

Thermal conserving port associated with the source inlet.

### **B** — Source outlet thermal

Thermal conserving port associated with the source outlet.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Thermal / Thermal Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

## Description

Variable source of thermal energy, characterized by temperature

The Controlled Temperature Source block represents an ideal source of
thermal energy that is powerful enough to maintain specified temperature difference
across the source regardless of the heat flow consumed by the system.

Connections A and B are thermal conserving ports corresponding to the source inlet and
outlet, respectively. Port S is a physical signal port, through which the control signal
that drives the source is applied. You can use the entire variety of Simulink® signal sources to generate the desired heat flow variation profile. The
temperature differential across the source is directly proportional to the signal at the
control port S.

The block positive direction is from port A to port B. This means that the temperature
differential is determined as *TB* –
*TA*, where
*TB* and
*TA* are the temperatures at source
ports.
