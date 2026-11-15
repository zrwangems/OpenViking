---
type: simulink-block
title: 'Logic-Controlled Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'logiccontrolledclutch'
documentation_source_path: 'ref/logiccontrolledclutch.html'
language: en
---

# Logic-Controlled Clutch

## Ports

### Input

### **E** — Control clutch engagement physical signal

Physical signal port associated with the clutch logic.
### Conserving

### **B** — Base interface mechanical rotational

Mechanical rotational conserving port associated with the base
interface.

### **F** — Follower interface mechanical rotational

Mechanical rotational conserving port associated with the follower
interface.

## Parameters

### **Transition model** — Clutch engagement parameterization `Instantaneous` (default) | `First-order lag` | `Scaled by input`

Clutch engagement transition control. When you select:

- `Instantaneous` — The clutch engages
  when the input signal at port **E** rounds to
  1, and the clutch does not engage when the input signal rounds
  to 0.
- `First-order lag` — The block
  introduces a first-order delay to the clutch engagement
  according to the value that you specify for the
  **Transition time constant**
  parameter.
- `Scaled by input` — The block smooths
  the signal input at port **E**. The block
  applies full static and kinetic friction when the input signal
  is greater than or equal to 1 and no static or kinetic friction
  torque when the signal is nonpositive. The block linearly scales
  the friction torques when the input signal is between 0 and
  1.

### **Transition time constant** — First-order lag time constant `0.1` `s` (default) | positive scalar

Time constant for first-order lag clutch engagement.

#### Dependencies

To enable this parameter, set **Transition model** to
`First-order lag`.

### **Kinetic friction torque** — Kinetic friction torque threshold `10` `N*m` (default) | nonnegative scalar

Minimum torque threshold to maintain relative motion between the clutch
plates.

### **Static friction torque** — Static friction torque threshold `20` `N*m` (default) | positive scalar

Minimum torque threshold to cause relative motion between the clutch
plates.

### **Clutch velocity tolerance** — Motion boundary condition `0.001` `rad/s` (default) | nonnegative scalar

Clutch minimum angular velocity.

### **Initial State** — Clutch condition at simulation start `Unlocked` (default) | `Locked`

Option to start the simulation with the clutch unlocked or locked.

## Libraries

Simscape / Driveline / Clutches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Friction clutch with input control

The Logic-Controlled Clutch represents a
logic-controlled mechanism that transmits rotational power through friction. The block
is an advanced version of the Fundamental Friction Clutch block. You control the
Logic-Controlled Clutch block with physical signal at
port **E**.

If the clutch is engaging and in motion, the block applies the kinetic torque. If the
clutch is engaging and not in motion, the block applies the static torque.
