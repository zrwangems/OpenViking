---
type: simulink-block
title: 'Radiative Heat Transfer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'radiativeheattransfer'
documentation_source_path: 'ref/radiativeheattransfer.html'
language: en
---

# Radiative Heat Transfer

## Ports

### Conserving

### **A** — Body A thermal

Thermal conserving port associated with body A.

### **B** — Body B thermal

Thermal conserving port associated with body B.

## Parameters

### **Area** — Area of heat transfer `0.0001 m^2` (default) | positive scalar

Radiating body area of heat transfer.

### **Radiation coefficient** — Radiation heat transfer coefficient `4e-8 W/m^2/K^4` (default) | positive scalar

Radiation coefficient of the two bodies, based on their geometrical shapes,
dimensions, and surface emissivity. For more information, see [1].

## Libraries

Simscape / Foundation Library / Thermal / Thermal Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

## Description

Heat transfer by radiation

The Radiative Heat Transfer block represents a heat
transfer by radiation between two bodies. The transfer is governed by the Stefan-Boltzmann
law:

Q=k⋅A⋅(TA4−TB4),

where:

- *Q* is the heat flow.
- *k* is the radiation coefficient.
- *A* is the emitting body surface area.
- *T*A and
  *T*B are the temperatures of the two
  bodies.

The radiation coefficient is determined by geometrical shapes, dimensions, and surface
emissivity. For example, the radiation constant for the heat transfer between two parallel
plates is computed as

k=σ1ε1+1ε2−1,

where:

- *σ* is Stefan-Boltzmann constant.
- *ε*1 is surface emissivity for the emitting
  plate.
- *ε*2 is surface emissivity for the receiving
  plate.

Similarly, the radiation coefficient for concentric cylinders is determined with the
formula

k=σ1ε1+1−ε2ε2r1r2,

where *r*1 and *r*
2 are the emitting and receiving cylinder radii, respectively. For more
information, including formulas for a wide variety of shapes, see [1].

Connections **A** and **B** are thermal conserving ports
associated with the emitting and receiving bodies, respectively. The block positive direction
is from port **A** to port **B**. This means that the heat
flow is positive if it flows from **A** to **B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
