---
type: simulink-block
title: 'Mechanical Translational Properties (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Utilities'
documentation_page: 'mechanicaltranslationalpropertiespb'
documentation_source_path: 'ref/mechanicaltranslationalpropertiespb.html'
language: en
---

# Mechanical Translational Properties (PB)

## Ports

### Conserving

### **R** — Port that connects block to the circuit position-based mechanical translational

Position-based mechanical translational conserving port that connects the block to
the physical network.

## Parameters

### **Downward gravitational acceleration, g** — Gravitational acceleration acting on network `9.81 m/s^2` (default) | nonnegative scalar

Gravitational acceleration acting on all the blocks in the connected circuit.

### **Positive direction incline angle, θ** — Incline angle of the rail `0 deg` (default) | scalar

Angle between the rail positive direction and the positive horizontal.

## Libraries

Simscape / Foundation Library / Translational / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Specify gravitational acceleration and rail incline angle for circuit

The Mechanical Translational Properties (PB) block
specifies the global parameters for all the blocks in the attached circuit, such as the
gravitational acceleration and the incline angle. In a position-based translational network,
blocks have a fixed orientation aligned with the global positive direction. Imagine all parts
assembled on a rail.

Schematic of gravity and incline angle

Incline angle, *θ*, is the angle between the rail positive direction and
the horizontal. The angle is measured counterclockwise from the positive horizontal. The rail
positive direction has an upward slope for angles between 0 and 180 degrees and a downward
slope for angles between 0 and -180 degrees.

Gravity, *g*, acts downwards. Depending on the incline angle, gravity can
have two components:

- Parallel component, acting along the rail,
  *g*·sin(*θ*). This is the component that induces
  motion. Positive *g*·sin(*θ*) corresponds to a positive
  incline angle that induces motion in the negative direction along the rail.
- Perpendicular component, acting normal to the rail,
  *g*·|cos(*θ*)|. This is the component that induces
  normal force between the mass and the rail and affects friction.

Here are some examples of rail orientation.

|  |  |  |
| --- | --- | --- |
| Vertical rail | *g* = 9.81 m/s^2  *θ* = 90 deg | Gravity causes mass acceleration in the negative direction  Schematic of vertical rail |
| Horizontal rail | *g* = 9.81 m/s^2  *θ* = 0 deg | Weight increases normal force  Schematic of horizontal rail |
