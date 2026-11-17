---
type: simulink-block
title: 'Unidirectional Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'unidirectionalclutch'
documentation_source_path: 'ref/unidirectionalclutch.html'
language: en
---

# Unidirectional Clutch

## Ports
```yaml
ports:
- name: H
  summary: Hub velocity mechanical rotational
  direction: conserving
- name: R
  summary: Ring velocity mechanical rotational
  direction: conserving
```

### Conserving

### **H** — Hub velocity mechanical rotational

Velocity of the hub driveshaft axis.

### **R** — Ring velocity mechanical rotational

Velocity of the ring driveshaft axis.
## Parameters
```yaml
parameters:
- name: Transmission direction
  summary: Relative rotation direction From hub to ring for positive rotation (default) | From hub to ring for negative rotation
  group: ''
- name: Initial state
  summary: Clutch initial state Unlocked (default) | Locked
  group: ''
```

### **Transmission direction** — Relative rotation direction `From hub to ring for positive rotation` (default) | `From hub to ring for negative rotation`

Relative rotation direction for which the clutch locks and transfers
torque.

### **Initial state** — Clutch initial state `Unlocked` (default) | `Locked`

Clutch state at the start of simulation. The clutch can be in one of two
states, locked and unlocked. A locked clutch constrains the base and
follower shafts to spin at the same velocity, that is, as a single unit. An
unlocked clutch allows the two shafts to spin at different velocities,
resulting in slip between the clutch plates.
## Libraries

Simscape / Driveline / Clutches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

## Description

Clutch that transmits power in a single direction

The Unidirectional Clutch block models an ideal one-way
clutch based on a coupled ring-hub. It transmits torque when the relative velocity of
hub and ring becomes positive or negative, depending on how you set the transmission
direction. For model details, see Equations.

### Equations

The figure displays the geometry of the unidirectional clutch. The table
summarizes the unidirectional clutch variables.

If locked, the clutch transmits torque from the hub to the ring. If unlocked, the
clutch transmits no torque. The clutch does not have a state of being unlocked but
engaged (transmitting torque). The relative angular velocity (slip),
*ω*, is the angular velocity of hub,
*ωH*, relative to the velocity of
the ring, *ωR*, that is, *ω*=*ωH* –
*ωR*.

The Unidirectional Clutch block implements an ideal model of a one-way clutch and
does not include any internal dynamics, such as the rollers and springs.

**Locking Condition**

The transmission direction determines the condition for locking.

- If you choose transmission for the positive direction, the clutch
  locks if *ω* =
  *ω*H –
  *ω*R ≥
  0 and becomes zero from positive values. The slip
  *ω* then remains zero, and the clutch transfers
  torque.

  If the driveline dynamics then causes *ω* < 0 later in the simulation, the clutch abruptly unlocks
  and stops transferring torque.
- If you choose transmission for the negative direction, the clutch
  locks if *ω* =
  *ω*H –
  *ω*R ≤
  0 and becomes zero from negative values. The slip
  *ω* then remains zero, and the clutch transfers
  torque.

  If the driveline dynamics then causes *ω* > 0 later in the simulation, the clutch abruptly unlocks
  and stops transferring torque.

For example, locking and torque transfer in the positive direction as
follows.

- When the hub rotates faster than the ring (*ω* > 0), the small gap prearranged between the hub and the
  ring is cleared. The spring-loaded rollers wedge between the hub and the
  ring, causing the two to contact, lock, and rotate together;
  *ω* resets to zero. (The rotation convention in the
  figure is clockwise.)
- If the ring rotates faster than the hub (*ω* < 0), the rollers are pushed out of contact and the clutch
  unlocks.

For a clutch schematic, see Equations.

**Power Dissipated by the Clutch**

The unidirectional clutch is ideal and does not dissipate power. Either the
clutch is unlocked and applies no kinetic friction, or it is locked (no slip)
and applies only static friction.
