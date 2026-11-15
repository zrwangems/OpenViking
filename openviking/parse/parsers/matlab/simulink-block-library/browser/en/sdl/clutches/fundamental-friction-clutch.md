---
type: simulink-block
title: 'Fundamental Friction Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'fundamentalfrictionclutch'
documentation_source_path: 'ref/fundamentalfrictionclutch.html'
language: en
---

# Fundamental Friction Clutch

## Ports

### Input

### **tK** — Kinetic friction torque, N\*m physical signal

Physical signal input port for the kinetic friction torque.

### **t+** — Static friction torque upper bound, N\*m physical signal

Physical signal input port for the upper static friction torque
limit.

### **t-** — Static friction torque lower bound, N\*m physical signal

Physical signal input port for the lower static friction torque
limit.
### Output

### **S** — Clutch slip velocity, rad/sec physical signal

Physical signal output port for the clutch slip velocity.

### **M** — Clutch state physical signal

Physical signal output port for the clutch state.
### Conserving

### **B** — Rotational velocity, rad/sec mechanical rotational

Rotational conserving ports associated with the driving shaft.

### **F** — Rotational speed, rad/sec mechanical rotational

Rotational conserving ports associated with the driven shaft.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Thermal ports allow
you to model heat flow between a block and the connected network. For
more information, see Model Thermal Losses in Driveline Components.

#### Dependencies

To enable these settings, set **Thermal Port** to
`Model`.

## Parameters

### **Directionality** — Permissible inter-plate slip directions `Bidirectional` (default) | `Unidirectional`

Slip directions the clutch allows between its plates. A bidirectional
clutch allows positive and negative slip velocities. A unidirectional clutch
allows only positive slip velocities.

The unidirectional clutch is equivalent to a friction clutch connected in
parallel to a one-way clutch that disengages only when the slip velocity
becomes positive. To model a unidirectional clutch with slip in the negative
direction, reverse the base and follower port connections.

### **Thermal port** — Thermal model `Omit` (default) | `Model`

Model for heat flow and temperature change:

- `Omit` — Neglect thermal
  dynamics.
- `Model` — Include thermal
  dynamics.

### **Thermal mass** — Resistance to temperature change `50` `kJ/K` (default) | scalar

Thermal energy required to change the component temperature by a single
thermal unit. The greater the thermal mass, the more resistant the component
is to temperature change.

#### Dependencies

To enable this parameter, set **Thermal Port** to
`Model`.

### **Clutch velocity tolerance** — Slip velocity threshold `0.001` `rad/s` (default) | scalar

Slip velocity below which the clutch can lock. The clutch locks if, after
falling below the clutch velocity tolerance, the kinetic friction torque is
nonzero and the transferred torque is between the static friction torque
limits.

### **Initial state** — Initial clutch state `Unlocked` (default) | `Locked`

Clutch state at the start of simulation. The clutch can be in one of two
states, locked and unlocked. A locked clutch constrains the base and
follower shafts to spin at the same velocity, that is, as a single unit. An
unlocked clutch allows the two shafts to spin at different velocities,
resulting in slip between the clutch plates.

A clutch that starts simulation unlocked lacks a direction of motion. For
this reason, after checking that the unlocked state is valid, the block
automatically determines the appropriate direction of motion based on the
driveline dynamics. Based on the direction of motion, the clutch then
transitions to an unlocked-reverse or unlocked-forward state.

## Libraries

Simscape / Driveline / Clutches / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

## Description

Friction clutch with kinetic and static-limit friction torques as inputs

The Fundamental Friction Clutch block represents a mechanism that
transmits rotational power through friction. The clutch contains two friction plate
sets, each rigidly connected to a driveshaft, that come into contact to engage. Once in
contact, the plates experience frictional torques that enable power to flow between the
driveshafts.

The clutch can be bidirectional or unidirectional. A bidirectional clutch can slip in
the positive and negative directions. A unidirectional clutch can slip only in the
positive direction. The slip direction is positive if the follower shaft spins faster
than the base shaft and negative if it spins slower. The block defines the slip velocity
as the difference

ω=ωF−ωB,

where:

- *ω* is the slip velocity.
- *ωF* is the angular velocity of
  the follower driveshaft.
- *ωB* is the angular velocity of
  the base driveshaft.

### Clutch States

The clutch can be in three states:

- Locked — Real clutch state in which the friction plates spin as a
  unit. A locked clutch has one rotational degree of freedom. It
  experiences no power losses due to friction.
- Unlocked — Real clutch state in which the friction plates slip with
  respect to each other. An unlocked clutch has two rotational degrees of
  freedom. It experiences power losses equal to the product of the slip
  velocity and the kinetic friction torque.
- Wait — Virtual clutch state that maintains the motion of the previous
  state while testing for locking and unlocking. The clutch degrees of
  freedom and power losses depend on the previous clutch state.

The schematic shows the conditions under which the clutch is locked and unlocked.
The clutch is generally locked if the torque it transfers lies between its static
friction torque limits and the magnitude of the slip velocity is smaller than its
velocity tolerance. The clutch unlocked otherwise.

In the schematic:

- *τ* is the torque transferred between the clutch
  plates.
- *τS*-
  and
  *τ*S+
  are the static friction torque limits.
- *τK* is the kinetic friction
  torque between the clutch plates.
- *ωTol* is the slip velocity
  tolerance of the clutch.
- *ω* is the slip velocity between the clutch
  plates.

The block identifies the clutch state through physical signal port
**M** using values -1, 0, and +1. The table summarizes the
correspondence between the states and the output values.

| State | Value |
| --- | --- |
| Unlocked Forward or Wait Forward | +1 |
| Unlocked Reverse or Wait Reverse | -1 |
| Locked or Unlocked Initial State | 0 |

### State Transitions

At the start of simulation, the clutch is in one of two states — locked or initial
unlocked. The initial unlocked state is unique in that it lacks a direction of
motion. The clutch remains in this state until the clutch slip velocity becomes
nonzero. The clutch then transitions to the appropriate state, unlocked reverse or
unlocked forward, according to the schematic.

During
simulation, the clutch tests various dynamic conditions to determine the appropriate
state transitions, if any. The schematics show the possible transitions, their
dynamic conditions, and the resulting states. If the clutch is unidirectional, the
schematic reduces to the right half. The diagram shows transitions for a one-way clutch.

The diagram shows transitions for a two-way clutch.

### Thermal Model

The Fundamental Friction Clutch block simulates the effects of heat
flow and heat generated relative to the amount of power dissipated when you enable
the thermal port. To simulate heat flow, you must connect the port to another block
with an enabled thermal port. Many Simscape™
Driveline™ blocks have thermal modelling options. When a parameter that supports
thermal modeling is available, it appears as a vector whose length corresponds to
the length of **Temperature**. For more information, see Model Thermal Losses in Driveline Components.

To enable the thermal port, set **Thermal Port** to
`Model`. Enabling the thermal port also enables these settings:

- **Parameters** > **Thermal Mass**
- **Variables** > **Temperature**

### Variables

Use the **Variables** settings to set the priority and initial
target values for the block variables before simulating. For more information, see
Set Priority and Initial Target for Block Variables.

**Dependencies**

To enable these settings, set **Thermal port** to
`Model`.
