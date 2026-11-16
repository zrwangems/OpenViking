---
type: simulink-block
title: 'Sinusoidal Rotational Velocity Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinusoidalrotationalvelocitysource'
documentation_source_path: 'ref/sinusoidalrotationalvelocitysource.html'
language: en
---

# Sinusoidal Rotational Velocity Source

## Ports

### Conserving

### **B** — Base interface mechanical rotational

Mechanical rotational conserving port associated with the base
interface.

### **F** — Follower interface mechanical rotational

Mechanical rotational conserving port associated with the follower
interface.

## Parameters

### **Offset** — Output average value `0` `rad/s` (default)

Average value that the output sinusoidal rotational velocity oscillates
about.

### **Sinusoid peak amplitude** — Output peak amplitude `1` `rad/s` (default)

Peak amplitude of the output sinusoidal rotational velocity.

### **Phase shift** — Output phase shift `0` `deg` (default)

Phase shift of the output sinusoidal rotational velocity.

### **Frequency** — Output frequency `1` `Hz` (default)

Frequency of the output sinusoidal rotational velocity. The frequency must
be greater than or equal to 0.

## Libraries

Simscape / Driveline / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Produce sinusoidal rotational velocity

The Sinusoidal Rotational Velocity Source block produces sinusoidal
rotational velocity with a constant offset.

The relative rotational velocity between the base and follower interfaces is

vFB=vF−vB,

where:

- *v FB* is the relative rotational
  velocity.
- *vF* is the absolute rotational
  velocity at the follower interface.
- *vB* is the absolute rotational
  velocity at the base interface.

The defining equation for the sinusoidal rotational velocity that the block generates is

v=vo+A\*sin(2πft+φ),

where:

- *v* is the output rotational velocity.
- *vo* is the offset rotational
  velocity of the output.
- *A* is the peak amplitude of the sinusoid.
- *f* is frequency of the sinusoid in Hz.
- *t* is time.
- φ is phase shift of the sinusoid.
