---
type: simulink-block
title: 'Sinusoidal Torque Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinusoidaltorquesource'
documentation_source_path: 'ref/sinusoidaltorquesource.html'
language: en
---

# Sinusoidal Torque Source

## Ports
```yaml
ports:
- name: B
  summary: Base interface mechanical rotational
  direction: conserving
- name: F
  summary: Follower interface mechanical rotational
  direction: conserving
```

### Conserving

### **B** — Base interface mechanical rotational

Mechanical rotational conserving port associated with the base
interface.

### **F** — Follower interface mechanical rotational

Mechanical rotational conserving port associated with the follower
interface.
## Parameters
```yaml
parameters:
- name: Offset
  summary: Output average value 0 N*m (default)
  group: ''
- name: Sinusoid peak amplitude
  summary: Output peak amplitude 1 N*m (default)
  group: ''
- name: Phase shift
  summary: Output phase shift 0 deg (default)
  group: ''
- name: Frequency
  summary: Output frequency 1 Hz (default)
  group: ''
```

### **Offset** — Output average value `0` `N*m` (default)

Average value that the sinusoidal output torque oscillates about.

### **Sinusoid peak amplitude** — Output peak amplitude `1` `N*m` (default)

Peak amplitude of the sinusoidal output torque.

### **Phase shift** — Output phase shift `0` `deg` (default)

Peak amplitude of the sinusoidal output torque.

### **Frequency** — Output frequency `1` `Hz` (default)

Frequency of the sinusoidal output torque. The frequency must be greater
than or equal to 0.
## Libraries

Simscape / Driveline / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Produce sinusoidal torque

The Sinusoidal Torque Source block produces sinusoidal torque with a
constant offset. A positive torque value generates torque acting from port B to port
F.

The defining equation for the sinusoidal torque that the block generates is

T=To+A\*sin(2πft+φ),

where:

- T is the output torque.
- *To* is the offset torque of the
  output.
- *A* is the peak amplitude of the sinusoid.
- *f* is frequency of the sinusoid in Hz.
- *t* is time.
- φ is phase shift of the sinusoid.
