---
type: simulink-block
title: 'Tire (Simple)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Tires and Vehicles'
documentation_page: 'tiresimple'
documentation_source_path: 'ref/tiresimple.html'
language: en
---

# Tire (Simple)

## Ports

### Conserving

### **A** — Axle mechanical rotational

Mechanical rotational port associated with the axle that the tire sits
on.

### **H** — Hub mechanical rotational

Mechanical rotational port associated with the wheel hub.

## Parameters

The table shows how the visibility of some Tire
(Simple) parameters depends on the option that you choose for other
parameters.

**Parameter Dependencies**

| Parameter | |
| --- | --- |
| Rolling Radius | |
| Compliance — Choose `No compliance - Suitable for HIL simulation` or `Specify stiffness and damping` | |
| **No compliance - Suitable for HIL simulation** | **Specify stiffness and damping** |
| Longitudinal stiffness |
| Longitudinal damping |
| Inertia — Choose `No Inertia` or `Specify inertia and initial velocity` | |
| **No Inertia** | **Specify inertia and initial velocity** |
| Tire inertia |
| Initial velocity |

### **Rolling radius** — Radius `0.3` `m` (default) | positive scalar

Rolling radius of the tire. The rolling radius must be greater than
zero.

### **Compliance** — Compliance model `No compliance - Suitable for HIL simulation` (default) | `Specify stiffness and damping`

Include or neglect longitudinal stiffness and damping.

#### Dependencies

Selecting `Specify stiffness and damping`
exposes other parameters. For more information, see Parameter Dependencies.

### **Longitudinal stiffness** — Longitudinal stiffness `1e6` `N/m` (default) | positive scalar

Longitudinal stiffness of the tire. The parameter must be greater than
zero.

#### Dependencies

This parameter appears only if the **Compliance**
parameter is set to `Specify stiffness and
damping`. For more information, see Parameter Dependencies.

### **Longitudinal damping** — Longitudinal damping `1000` `N/(m/s)` (default) | positive scalar

Longitudinal damping of the tire. The parameter must be greater than
zero.

#### Dependencies

This parameter appears only if the **Compliance**
parameter is set to `Specify stiffness and
damping`. For more information, see Parameter Dependencies.

### **Inertia** — Inertia model `No inertia` (default) | `Specify inertia and initial velocity`

Include or neglect tire inertia.

#### Dependencies

Selecting `Specify inertia and initial
velocity` exposes other parameters. For more
information, see Parameter Dependencies.

### **Tire inertia** — Tire inertia `1` `kg*/m^2` (default) | positive scalar

Rotational inertia of the tire.

#### Dependencies

This parameter appears only if the **Inertia**
parameter is set to `Specify inertia and initial
velocity`. For more information, see Parameter Dependencies.

### **Initial velocity** — Initial velocity `0` `rad/s` (default)

Initial rotational velocity of the tire.

#### Dependencies

This parameter appears only if the **Inertia**
parameter is set to `Specify inertia and initial
velocity`. For more information, see Parameter Dependencies.

## Libraries

Simscape / Driveline / Tires & Vehicles

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

No-slip tire model with minimal parameters

The Tire (Simple) block represents a simple, no-slip
model of a tire that you parameterize by tire radius.

You can optionally add inertia, stiffness, or damping. These dynamics require
additional computation that tends to make models less suitable for real-time
simulation.
