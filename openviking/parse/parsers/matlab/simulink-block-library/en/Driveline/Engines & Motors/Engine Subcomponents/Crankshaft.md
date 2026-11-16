---
type: simulink-block
title: 'Crankshaft'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'crankshaft'
documentation_source_path: 'ref/crankshaft.html'
language: en
---

# Crankshaft

## Ports

### Input

### **CylPwr** — Cylinder power array physical signal

Physical signal input associated with the cylinder power when the
block acts as a subcomponent.

#### Dependencies

To enable this port, clear **Input power separately**.

### **CylPwr1** — Cylinder 1 power physical signal

Physical signal input associated with the power from cylinder 1.

#### Dependencies

To enable this port, select **Input power separately**.

### **CylPwr2** — Cylinder 2 power physical signal

Physical signal input associated with the power from cylinder
2.

#### Dependencies

To enable this port, set **Number of cylinders** to `Two
Cylinders`, `Three
Cylinders`, or `Four
Cylinders` and select **Input power
separately**.

### **CylPwr3** — Cylinder 3 power physical signal

Physical signal input associated with the power from cylinder
3.

#### Dependencies

To enable this port, set **Number of cylinders** to `Three
Cylinders` or `Four
Cylinders` and select **Input power
separately**.

### **CylPwr4** — Cylinder 4 power physical signal

Physical signal input associated with the power from cylinder
4.

#### Dependencies

To enable this port, set **Number of cylinders** to `Four
Cylinders` and select **Input power
separately**.
### Output

### **CrkPos** — Crank position, deg physical signal

Physical signal output associated with the crank position, in degrees.

### **Spd** — Engine rotational speed, rad/s physical signal

Physical signal output associated with the engine rotational speed, in rad/s.

### **AvrSpd** — Cycle-average crank speed, rad/s physical signal

Physical signal output associated with the cycle-average crank speed, in rad/s.

### **AvrTrq** — Cycle-average net-indicated crank torque, N\*m physical signal

Physical signal output associated with the cycle-average net-indicated crank torque, in
Nm.

### **Trq** — Instantaneous net-indicated crank torque, N\*m physical signal

Physical signal output associated with the instantaneous net-indicated crank torque, in
Nm.
### Conserving

### **F** — Crankshaft mechanical rotational

Mechanical rotational conserving port associated with the crankshaft
follower.

## Parameters

### Mechanical

### **Initial crank position, ca0 (0-720 CAdeg)** — Crank position when simulation begins `0` `deg` (default) | nonnegative scalar in the range [0,720)

Initial crank position.

### **Number of cylinders** — Total cylinder count `Single Cylinder` (default) | `Two Cylinders` | `Three Cylinders` | `Four Cylinders`

Number of spark ignition cylinders.

### **Input power separately** — Option to input power `on` (default) | `off`

Whether to input power as an array or to assign each combustion
cylinder to its own port.

### **Spark angle difference** — Two cylinder engine spark angle phase `270` `deg` (default) | positive scalar

Spark angle difference for two cylinder engines. This value can vary
from engine to engine.

#### Dependencies

To enable this parameter, set **Number of
cylinders** to `Two
Cylinders`.

### **Firing order** — Ignition order for four cylinder engines `1-3-4-2` (default) | `1-3-2-4`

Firing order for four-cylinder engines. Firing order is engine-specific, but your
selection for this parameter will not affect the block performance. You
can use the firing order information for controller development.

#### Dependencies

To enable this parameter, set **Number of
cylinders** to `Four
Cylinders`.

### Simulation

### **Threshold to avoid divide-by-zero** — Threshold engine speed `0.1` `rad/s` (default)

Engine rotational speed at which the block applies linearization to
avoid discontinuities at *ω* = 0.

### Output

### **Cycle-average speed** — Option to output cycle-average speed `on` (default) | `off`

Whether to output the cycle-average speed.

### **Cycle-average net indicated torque** — Option to output cycle-average net indicated torque `on` (default) | `off`

Whether to output the cycle-average net indicated torque.

### **Instantaneous net indicated torque** — Option to output instantaneous net indicated torque `on` (default) | `off`

Whether to output the instantaneous net indicated torque.

## Libraries

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

### R2025a: Enumeration Updates

These parameters now use a checkbox.

- **Input power separately**
- **Cycle-average speed**
- **Cycle-average net indicated torque**
- **Instantaneous net indicated torque**

These parameters used drop downs in previous releases.

## Description

Combustion engine crankshaft that connects to one or more pistons

The Crankshaft block represents the crankshaft component of
an abstracted internal combustion engine. Connect this block to one or more
SI Combustion
Cylinder blocks to compute the crank-angle-resolved instantaneous
torque.

### Equations

The generic torque-speed-power relationship governs the block, such that

τ⋅ω=P,

where

- *τ* is the torque.
- *ω* is the rotational speed, which the block assumes
  is nonnegative.
- *P* is the power.

The block calculates the power as

P=∑i=1NPi,

where *N* is the value of the **Number
of cylinders** parameter. The block calculates *ω* as
the time derivative of the crank position, *θ*, such that

ddtθ=ω.

The constant *ωc* is the
**Threshold to avoid divide-by-zero** parameter. When *ω* <
*ωc*, the block applies 1/*ω* linearization.

τ={PωP⋅(2ω−ωωc2)ω≥ωcω<ωc

**Crank Position**

The block calculates the crank position with respect to the top dead center position for
each combustion cylinder, where 0 ≤ *θi* ≤
720 degrees. How the block performs this calculation depends on
*N*. For all values of *N*, *θ1* =
*θ*. For *N* = 2, *θ2* =
*θ1*+*Δ*, where *Δ* is the **Spark angle
difference** parameter. This parameter value is specific to the
engine you want to model. It may be a value such as 270° or 360°. When *N* = 3, the block assumes that the cylinders are evenly phased such that

θ2=θ1+(1⋅7203)θ3=θ1+(2⋅7203)

When *N* = 4, the block assumes that the cylinders are evenly phased at
180° and enables the **Firing order** parameter.
