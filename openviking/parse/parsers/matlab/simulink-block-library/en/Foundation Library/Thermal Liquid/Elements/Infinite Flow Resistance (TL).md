---
type: simulink-block
title: 'Infinite Flow Resistance (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'infiniteflowresistancetl'
documentation_source_path: 'ref/infiniteflowresistancetl.html'
language: en
---

# Infinite Flow Resistance (TL)

## Ports

### Conserving

### **A** — Flow rate is zero thermal liquid

Thermal liquid conserving port with no fluid or heat flow.

### **B** — Flow rate is zero thermal liquid

Thermal liquid conserving port with no fluid or heat flow.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Perfectly insulated break in thermal liquid network

The Infinite Flow Resistance (TL) block represents a break
in a thermal liquid network. There is no mass or energy flow through the break. However, the
liquid properties, specified by the Thermal
Liquid Settings (TL) block connected to the circuit, are the same on both
sides of the break. Use this block to set the priority and initial target value to the
differences in pressure and temperature between port **A** and port
**B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
