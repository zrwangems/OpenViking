---
type: simulink-block
title: 'Mechanical Translational Reference'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'mechanicaltranslationalreference'
documentation_source_path: 'ref/mechanicaltranslationalreference.html'
language: en
---

# Mechanical Translational Reference

## Ports
```yaml
ports:
- name: V
  summary: Velocity is zero mechanical translational
  direction: conserving
```

### Conserving

### **V** — Velocity is zero mechanical translational

Mechanical translational conserving port where velocity is equal to zero.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Reference connection for mechanical translational ports

The Mechanical Translational Reference block represents a
reference point, or frame, for mechanical translational ports. All translational ports that
are rigidly clamped to the frame must be connected to a Mechanical
Translational Reference block. For more information, see Grounding Rules.
