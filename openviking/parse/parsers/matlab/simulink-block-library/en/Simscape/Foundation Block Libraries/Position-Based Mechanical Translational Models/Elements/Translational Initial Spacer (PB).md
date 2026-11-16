---
type: simulink-block
title: 'Translational Initial Spacer (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Elements'
documentation_page: 'translationalinitialspacerpb'
documentation_source_path: 'ref/translationalinitialspacerpb.html'
language: en
---

# Translational Initial Spacer (PB)

## Ports

### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection. For positive length, port **F** has a more
positive position than port **B**.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Initial distance between blocks

The Translational Initial Spacer (PB) block provides an
initial distance between ports **B** and **F**.

Connections **B** and **F** are position-based
mechanical translational conserving ports. Length is positive when port **F**
has a more positive position than port **B**. The block does not transmit
force.

The block has no parameters. You specify length as an initial variable target.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
