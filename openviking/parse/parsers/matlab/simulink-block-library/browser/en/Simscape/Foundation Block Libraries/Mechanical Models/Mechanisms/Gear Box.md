---
type: simulink-block
title: 'Gear Box'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanisms'
documentation_page: 'gearbox'
documentation_source_path: 'ref/gearbox.html'
language: en
---

# Gear Box

## Ports

### Conserving

### **S** — Input shaft mechanical rotational

Mechanical rotational conserving port associated with the input
shaft.

### **O** — Output shaft mechanical rotational

Mechanical rotational conserving port associated with the output
shaft.

## Parameters

### **Gear ratio** — Ratio of gear velocities `5` (default)

The ratio of the input shaft angular velocity to that of the output shaft.
You can specify both positive and negative values.

## Libraries

Simscape / Foundation Library / Mechanical / Mechanisms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Gear box in mechanical systems

The Gear Box block represents an ideal, nonplanetary,
fixed gear ratio gear box. The gear ratio is determined as the ratio of the input shaft
angular velocity to that of the output shaft.

The gear box is described with the following equations:

ωS=N·ωO

TO=N⋅TS

PS=ωS⋅TS

PO=−ωO⋅TO

where

- *ω*S is input shaft angular
  velocity.
- *ω*O is output shaft angular
  velocity.
- *N* is gear ratio.
- *T*S is torque on the input
  shaft.
- *T*O is torque on the output
  shaft.
- *P*S is power on the input
  shaft.
- *P*O is power on the output shaft.
  Notice the minus sign in computing *P*O.
  One of the network rules is that the power flowing through a conserving port is
  positive if it is removed (dissipated) from the circuit, and is negative if the
  component generates power into the system.

Connections S and O are mechanical rotational conserving ports associated with the box
input and output shaft, respectively. The block positive directions are from S to the
reference point and from the reference point to O.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
