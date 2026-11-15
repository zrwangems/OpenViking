---
type: simulink-block
title: 'Delta Reference (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'deltareferencethreephase'
documentation_source_path: 'ref/deltareferencethreephase.html'
language: en
---

# Delta Reference (Three-Phase)

## Ports

### Conserving

### **~** — Expandable three-phase port electrical

Expandable composite (**a**,**b**,
**c**) three-phase
port.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

## Libraries

Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Internal reference point for delta-connected network

In a Simscape™
Electrical™ model, connect a Delta Reference
(Three-Phase) block to any part of the three-phase system that is
connected in a delta winding configuration. The block provides a reference point for the
delta winding, representing the center of the line-line vector voltage triangle. The
software calculates absolute node voltages relative to the voltage at this reference
point.

For example, suppose you model a transmission system that consists of a generator
connected in a wye configuration, a wye-delta transformer, a delta-wye transformer, and
a load connected in wye. Connect a Delta Reference
(Three-Phase) block to the part of the circuit between the two
transformers.
