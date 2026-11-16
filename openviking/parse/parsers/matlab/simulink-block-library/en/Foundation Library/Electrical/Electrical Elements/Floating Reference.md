---
type: simulink-block
title: 'Floating Reference'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'floatingreference'
documentation_source_path: 'ref/floatingreference.html'
language: en
---

# Floating Reference

## Ports

### Conserving

### **n** — DC current is zero electrical

Electrical conserving port where the DC current is zero. Use this port to measure
the voltage of other nodes in a floating electrical network.

## Parameters

### **Capacitance** — Capacitance that blocks DC current `1 uF` (default) | positive scalar

Represents the physical capacitance between the floating network and the electrical
ground. This capacitance blocks the DC current.

### **Parasitic parallel conductance** — Small parasitic effects `0 1/Ohm` (default) | nonnegative scalar

Represents small parasitic effects. A nonzero value is required for the simulation
of some circuit topologies.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Reference for measuring voltage of other nodes in floating electrical network

The Floating Reference block provides an electrical
reference that you can use to measure the voltage of other nodes in a floating electrical
network.

Unlike the Electrical Reference block, which provides a
connection to ground, this block uses a capacitance to block the DC current.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
