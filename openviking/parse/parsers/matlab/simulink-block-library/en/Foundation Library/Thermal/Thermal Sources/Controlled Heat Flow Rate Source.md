---
type: simulink-block
title: 'Controlled Heat Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'controlledheatflowratesource'
documentation_source_path: 'ref/controlledheatflowratesource.html'
language: en
---

# Controlled Heat Flow Rate Source

## Ports

### Input

### **S** — Heat flow control signal, W physical signal

Input physical signal that specifies the heat flow through the
source.
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

Variable source of thermal energy, characterized by heat flow

The Controlled Heat Flow Rate Source block represents an ideal source
of thermal energy that is powerful enough to maintain specified heat flow at its outlet
regardless of the temperature difference across the source.

Connections A and B are thermal conserving ports corresponding to the source inlet and
outlet, respectively. Port S is a physical signal port, through which the control signal
that drives the source is applied. You can use the entire variety of Simulink® signal sources to generate the desired heat flow variation profile. The
heat flow through the source is directly proportional to the signal at the control port
S.

The block positive direction is from port A to port B. This means that positive signal
at port S generates heat flow in the direction from A to B.
