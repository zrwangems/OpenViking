---
type: simulink-block
title: 'Motorcycle Chain'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Motion'
documentation_page: 'motorcyclechain'
documentation_source_path: 'ref/motorcyclechain.html'
language: en
---

# Motorcycle Chain

## Ports

### Input

### **MDshft** — Drive shaft moment on front sprocket `scalar`

Drive shaft moment on front sprocket about
*ym*, in N·m.

### **FCpR** — Longitudinal and vertical forces at rear wheel contact patch `vector`

Longitudinal and vertical forces at rear wheel contact patch *OCpR*, along *iCpR* and *kCpR*, in N. Signal vector dimensions are `[1x2]` or `[2x1]`.

### **ThetaFrm** — Main frame pitch angle `scalar`

Main frame pitch angle, *ϴfrm*, in rad.

### **ThetaArmR** — Rear arm pitch angle `scalar`

Rear arm pitch angle, *ϴra*, in rad.

### **MBrkR** — Brake moment at rear wheel `scalar`

Brake moment at the rear wheel *GWhlRr*, about *jWhlRr*, in N·m.

### **AngAWhlR** — Rear wheel angular acceleration `scalar`

Rear wheel angular acceleration, in
rad/s2.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | Description | Units |
| --- | --- | --- |
| `FChn` | Chain force applied to rear arm | N |
| `AngVSprtR` | Angular velocity of rear sprocket | rad/s |
| `MDrvSprtR` | Wheel damper moment applied to rear sprocket | N·m |
| `WhlDmpAng` | Angle between rear sprocket and rear wheel | rad |

### **MDrvSprtR** — Wheel damper moment at rear sprocket `scalar`

Wheel damper moment applied to rear sprocket, in N·m.

### **MDrvArmR** — Drive chain moment at rear arm `scalar`

Drive chain moment at rear arm *OArmRr*, about *jArmRr*, in N·m.

### **MDrvFrm** — Drive chain moment at frame `scalar`

Drive chain moment at the frame *OFrm*, about *jFrm*, in N·m.

## Parameters

This figure shows how the chain relates geometrically to the motorcycle frame, rear
arm, and rear wheel.

Motorcycle chain diagram

#### Front Sprocket

### **Coordinates, SprktFrPxz** — Front sprocket position `[0.05 -0.05]` (default) | `vector`

Position of front sprocket, *SprktFrPxz*, along
*xm*
*zm*, respectively, in m.

### **Mass moment of inertia, SprktFrIyy** — Front sprocket inertia `0.005` (default) | `scalar`

Front sprocket mass moment of inertia, *SprktFrIyy*, in
kg·m2.

### **Radius, SprktFrR** — Front sprocket radius `0.04` (default) | `scalar`

Front sprocket radius, *SprktFrR*, in m.

#### Rear Sprocket

### **Mass moment of inertia, SprktRrIyy** — Rear sprocket inertia `0.01` (default) | `scalar`

Rear sprocket mass moment of inertia, *SprktRrIyy*, in
kg·m2.

### **Radius, SprktRrR** — Rear sprocket radius `0.12` (default) | `scalar`

Rear sprocket radius, *SprktRrR*, in m.

#### Rear Wheel

### **Mass moment of inertia, WhlRrIyy** — Rear wheel inertia `0.66` (default) | `scalar`

Rear wheel mass moment of inertia, *WhlRrIyy*, in
kg·m2.

### **Radius, WhlRrR** — Rear wheel radius `0.33` (default) | `scalar`

Rear wheel radius, *WhlRrR*, in m.

#### Swing Arm

### **Arm length, ArmRrLen** — Swing arm length `0.535` (default) | `scalar`

Arm length, *ArmRrLen*, in m.

#### Wheel Damper

### **Stiffness, WhlDmpK** — Wheel damper stiffness `1e4` (default) | `scalar`

Wheel damper stiffness, *WhlDmpK*, in N/rad.

### **Damping, WhlDmpC** — Wheel damping `1e2` (default) | `scalar`

Wheel damper damping, *WhlDmpC*, in N·s/rad.

### **Equilibrium angle** — Wheel damper equilibrium angle `-15e-3` (default) | `scalar`

Equilibrium angle, *WhlDmpAng0*, in rad.

#### Initial Conditions

### **Rear sprocket angular velocity, SprktRrAngV0** — Angular velocity `0` (default) | `scalar`

Rear sprocket angular velocity, *SprktRrAngV0*, in
rad/s.

### **Rear wheel angular velocity, WhlRrAngV0** — Angular velocity `0` (default) | `scalar`

Rear wheel angular velocity, *WhlRrAngV0*, in
rad/s.

## Libraries

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Implement motorcycle chain

The Motorcycle Chain block implements the dynamic effects of a
motorcycle chain on the Motorcycle Body Longitudinal In-Plane block,
including dynamic tension and moment drive coupling.

This figure shows how the chain relates geometrically to the motorcycle frame, rear
arm, and rear wheel.

Motorcycle chain diagram

| Frame | Variable in Figure | Description |
| --- | --- | --- |
| Motorcycle main frame  - *xm* – Forward   along vector pointing to front fork - *zm* –   Downward - *ym* –   Orthogonal to motorcycle plane | *Om* | Main frame origin |
