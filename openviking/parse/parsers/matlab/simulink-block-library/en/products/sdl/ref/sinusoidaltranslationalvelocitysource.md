---
type: simulink-block
title: 'Sinusoidal Translational Velocity Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Drivetrain Disturbances'
documentation_page: 'sinusoidaltranslationalvelocitysource'
documentation_source_path: 'ref/sinusoidaltranslationalvelocitysource.html'
language: en
---

# Sinusoidal Translational Velocity Source

## Ports

### Conserving

### **B** — Base interface mechanical translational

Mechanical translational conserving port associated with the
base interface.

### **F** — Follower interface mechanical translational

Mechanical translational conserving port associated with the
follower interface.

## Parameters

### **Offset** — Output average value `0` `m/s` (default)

Average value that the output sinusoidal translational velocity oscillates
about.

### **Sinusoid peak amplitude** — Output peak amplitude `1` `m/s` (default)

Peak amplitude of the output sinusoidal translational velocity.

### **Phase shift** — Output phase shift `0` `deg` (default)

Phase shift of the output sinusoidal translational velocity

### **Frequency** — Output frequency `1` `Hz` (default)

Frequency of the output sinusoidal translational velocity. The frequency
must be greater than or equal to 0.

## Libraries

Simscape / Driveline / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Produce sinusoidal translational velocity

The Sinusoidal Translational Velocity Source block produces sinusoidal
translational velocity with a constant offset.

The relative translational velocity between the base and follower interfaces is

vFB=vF−vB,

where:

- *v FB* is the relative
  translational velocity.
- *vF* is the absolute translational
  velocity at the follower interface.
- *vB* is the absolute translational
  velocity at the base interface.

The defining equation for the sinusoidal translational velocity that the block
generates is

v=vo+A\*sin(2πft+φ),

where:

- *v* is the output translational velocity.
- *vo* is the offset translational
  velocity of the output.
- *A* is the peak amplitude of the sinusoid.
- *f* is frequency of the sinusoid in Hz.
- *t* is time.
- φ is phase shift of the sinusoid.
