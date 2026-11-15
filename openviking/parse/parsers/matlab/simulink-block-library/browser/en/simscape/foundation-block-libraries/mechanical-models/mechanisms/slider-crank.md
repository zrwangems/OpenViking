---
type: simulink-block
title: 'Slider-Crank'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanisms'
documentation_page: 'slidercrank'
documentation_source_path: 'ref/slidercrank.html'
language: en
---

# Slider-Crank

## Ports

### Conserving

### **C** — Crank mechanical rotational

Mechanical rotational conserving port associated with the
crank.

### **S** — Slider mechanical translational

Mechanical translational conserving port associated with the
slider.

## Parameters

### **Crank radius** — Radius of the crank `0.1 m` (default)

The radius of the crank. The parameter value must be greater than zero.

### **Rod length** — Length of the rod `0.2 m` (default)

Length of the rod connecting the crank and the slider. The parameter value
must be greater than **Crank radius**.

### **Crank inertia** — Inertia of the crank `0.01 kg*m^2` (default)

The inertia of the crank, which helps move the mechanism through the
positions at the top and bottom when the rod is exactly aligned with the
center of the crank. The parameter value must be greater than zero.

### **Slider stiffness** — Stiffness applied to the slider position `1e6 N/m` (default)

Together with **Slider damping**, introduces a compliance
that helps reduce inertia coupling between the ports. Higher stiffness
causes the motion to be closer to ideal, but increases the system stiffness.
The parameter value must be greater than zero.

### **Slider damping** — Damping applied to the slider position `1e3 N/(m/s)` (default)

Together with **Slider stiffness**, introduces a
compliance that helps reduce inertia coupling between the ports. Higher
damping values smooth the ringing that can be caused by the stiffness. The
parameter value must be greater than zero.

## Libraries

Simscape / Foundation Library / Mechanical / Mechanisms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Generic slider-crank mechanism

The Slider-Crank block represents the slider-crank
mechanism as a converter between the continuous rotational motion of the crank and the
oscillating translational motion of the slider.

The mechanism has two connections:

- Port C corresponds to the crank and is a mechanical rotational conserving
  port.
- Port S corresponds to the slider and is a mechanical translational conserving
  port.

The **Crank radius** and **Rod length** parameters
describe the mechanism geometry. The **Crank inertia** parameter helps
move the mechanism through the positions at the top and bottom when the rod is exactly
aligned with the center of the crank.

The purpose of the **Slider stiffness** and **Slider
damping** parameters is to reduce inertia coupling between the ports, which
can cause computational issues. The block applies the stiffness and damping between the
ideal position of the slider (as calculated by the geometry) and the actual position of
the translational conserving port, **S**. This compliance avoids a
direct nonlinear coupling between the ports. Higher stiffness causes the motion to be
closer to ideal, but increases the system stiffness. The damping helps smooth the
ringing that can be caused by the stiffness.

### Variables

You can set initialization targets for the crank angle and velocity at the start
of simulation, using both positive and negative values.

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
