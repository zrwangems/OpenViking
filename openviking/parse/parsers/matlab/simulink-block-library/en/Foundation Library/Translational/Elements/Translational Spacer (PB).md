---
type: simulink-block
title: 'Translational Spacer (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalspacerpb'
documentation_source_path: 'ref/translationalspacerpb.html'
language: en
---

# Translational Spacer (PB)

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

Fixed length between blocks during simulation

The Translational Spacer (PB) block maintains a fixed
length between ports **B** and **F** during simulation:

length=xF−xB

vB=vF

Connections **B** and **F** are position-based
mechanical translational conserving ports. Length is positive when port **F**
has a more positive position than port **B**. The spacer force acts from port
**B** on port **F**. Positive spacer force drives port
**F** in the positive direction. When length is positive, positive spacer
force corresponds to the spacer in a state of compression.

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

To specify length:

- For a known length, specify it as a high-priority target.
- For an unknown fixed length, specify any value and set the priority to low or none.
  Then the solver computes a value for the length during model initialization.
