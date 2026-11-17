---
type: simulink-block
title: 'Sinusoidal Force Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinusoidalforcesource'
documentation_source_path: 'ref/sinusoidalforcesource.html'
language: en
---

# Sinusoidal Force Source

## Ports
```yaml
ports:
- name: B
  summary: Base interface mechanical translational
  direction: conserving
- name: F
  summary: Follower interface mechanical translational
  direction: conserving
```

### Conserving

### **B** — Base interface mechanical translational

Mechanical translational conserving port associated with the
base interface.

### **F** — Follower interface mechanical translational

Mechanical translational conserving port associated with the
follower interface.
## Parameters
```yaml
parameters:
- name: Offset
  summary: Output average value 0 N (default)
  group: ''
- name: Sinusoid peak amplitude
  summary: Output peak amplitude 1 N (default)
  group: ''
- name: Phase shift
  summary: Output phase shift 0 deg (default)
  group: ''
- name: Frequency
  summary: Output frequency 1 Hz (default)
  group: ''
```

### **Offset** — Output average value `0` `N` (default)

Average value that the output sinusoidal force oscillates about.

### **Sinusoid peak amplitude** — Output peak amplitude `1` `N` (default)

Peak amplitude of the output sinusoidal force.

### **Phase shift** — Output phase shift `0` `deg` (default)

Phase shift of the output sinusoidal force.

### **Frequency** — Output frequency `1` `Hz` (default)

Frequency of the output sinusoidal force. The frequency must be greater
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

Produce sinusoidal force

The Sinusoidal Force Source block produces sinusoidal force with a
constant offset. A positive force value generates force acting from port B to port
F.

The defining equation for the sinusoidal force that the block generates is

F=Fo+A\*sin(2πft+φ),

where:

- *F* is the output force.
- *Fo* is the offset force of the
  output.
- A is the peak amplitude of the sinusoid.
- *f* is frequency of the sinusoid in Hz.
- *t* is time.
- φ is phase shift of the sinusoid.
