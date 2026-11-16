---
type: simulink-block
title: 'Infinite Hydraulic Resistance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'infinitehydraulicresistance'
documentation_source_path: 'ref/infinitehydraulicresistance.html'
language: en
---

# Infinite Hydraulic Resistance

## Ports

The block has two hydraulic conserving ports.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Hydraulic element for setting initial pressure difference between two nodes

The Infinite Hydraulic Resistance block represents a break in a
hydraulic network. There is no fluid flow through the break. However, the fluid
properties, specified by the Custom Hydraulic Fluid block connected to the circuit, are the same
on both sides of the break. Use this block to set the priority and initial target value
to the difference in pressure between port **A** and port
**B**.

The **Variables** tab lets you set the priority and initial target
value for the **Pressure difference** variable prior to simulation. For
more information, see Set Priority and Initial Target for Block Variables.
