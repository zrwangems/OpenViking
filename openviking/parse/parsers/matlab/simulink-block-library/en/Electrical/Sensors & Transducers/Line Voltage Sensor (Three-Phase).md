---
type: simulink-block
title: 'Line Voltage Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'linevoltagesensorthreephase'
documentation_source_path: 'ref/linevoltagesensorthreephase.html'
language: en
---

# Line Voltage Sensor (Three-Phase)

## Ports

### Output

### **V** — Three-elements vector physical signal

Three-element physical signal vector output port associated with the
voltages between the phases
### Conserving

### **~1** — Three-phase port electrical

Expandable three-phase
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

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Ideal three-phase line voltage measurement

The Line Voltage Sensor (Three-Phase) block represents
an ideal three-phase line voltage sensor. The block measures the line-line voltages of a
three-phase system and outputs a three-element physical signal vector. Each element of
the physical signal output vector is proportional to the voltage between the phases as
follows:

- Element 1: *Vab* =
  *Va* -
  *Vb*
- Element 2: *Vbc* =
  *Vb* -
  *Vc*
- Element 3: *Vca* =
  *Vc* -
  *Va*

where *Va*,
*Vb*, and
*Vc* are the absolute
*a*-, *b*-, and *c*-phase
voltages.

**Note**

You must connect the Line Voltage Sensor
(Three-Phase) block in shunt with the three-phase element. For
more information on how to use this block, see Build and Simulate Composite and Expanded Three-Phase Models.
