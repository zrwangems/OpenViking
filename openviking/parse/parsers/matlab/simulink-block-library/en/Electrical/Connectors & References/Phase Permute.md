---
type: simulink-block
title: 'Phase Permute'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'phasepermute'
documentation_source_path: 'ref/phasepermute.html'
language: en
---

# Phase Permute

## Ports

### Conserving

### **~123** — Expandable three-phase port electrical

Expandable composite (**a1**,**b1**,
**c1**) three-phase
port.

### **~231** — Expandable three-phase port electrical

Expandable composite (**a2**,**b2**,
**c2**) three-phase port.

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

Permute phases of three-phase system

The Phase Permute block cyclically permutes (changes
the order of) the phases of a three-phase system.

The block has two three-phase connections associated with its terminals. If you
consider the side of the block labeled **~123**
(**a1**,**b1**, **c1** in
expanded view) as side 1 and the side of the block labeled **~231**
(**a2**,**b2**, **c2**) as side
2, then the block connects phases as shown in the table.

| Side 1 Phase | Connects to Side 2 Phase |
| --- | --- |
| *a1* | *c2* |
| *b1* | *a2* |
| *c1* | *b2* |
