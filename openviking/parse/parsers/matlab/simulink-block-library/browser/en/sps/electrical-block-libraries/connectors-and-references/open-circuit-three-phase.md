---
type: simulink-block
title: 'Open Circuit (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'opencircuitthreephase'
documentation_source_path: 'ref/opencircuitthreephase.html'
language: en
---

# Open Circuit (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase port electrical

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

### R2019b: Capping unconnected ports is no longer required

This block is no longer required. Starting in R2019b, the restriction that
disallowed unconnected conserving ports in Simscape™ models has been lifted. Now, if you leave a conserving port
unconnected, the physical network sets all the Through variables at this port to 0.
However, you can still use terminator blocks to improve diagram readability.

There are no plans to remove the terminator blocks. All the existing models using
these blocks work the same as in previous releases.

## Description

Three-phase terminator that draws no current

The Open Circuit (Three-Phase) block models a
three-phase connection that draws no current on any of the three phases.
