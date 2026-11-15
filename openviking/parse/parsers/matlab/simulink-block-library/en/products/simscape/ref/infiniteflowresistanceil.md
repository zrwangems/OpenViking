---
type: simulink-block
title: 'Infinite Flow Resistance (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Elements'
documentation_page: 'infiniteflowresistanceil'
documentation_source_path: 'ref/infiniteflowresistanceil.html'
language: en
---

# Infinite Flow Resistance (IL)

## Ports

### Conserving

### **A** — Flow rate is zero isothermal liquid

Isothermal liquid conserving port with no fluid flow.

### **B** — Flow rate is zero isothermal liquid

Isothermal liquid conserving port with no fluid flow.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Isothermal liquid element for setting initial pressure difference between two nodes

The Infinite Flow Resistance (IL) block represents a break
in an isothermal liquid network. There is no liquid flow through the break. However, the
liquid properties, specified by the Isothermal Liquid
Properties (IL) block connected to the circuit, are the same on both sides
of the break. Use this block to set the priority and initial target value to the difference in
pressure between port **A** and port **B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
