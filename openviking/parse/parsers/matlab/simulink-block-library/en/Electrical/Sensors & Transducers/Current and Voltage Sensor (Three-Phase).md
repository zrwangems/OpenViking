---
type: simulink-block
title: 'Current and Voltage Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'currentandvoltagesensorthreephase'
documentation_source_path: 'ref/currentandvoltagesensorthreephase.html'
language: en
---

# Current and Voltage Sensor (Three-Phase)

## Ports

### Output

### **V** — Voltage physical signal

Three-element physical signal vector output port associated with the
*a*-, *b*-, and
*c*-phase voltages.

### **I** — Current physical signal

Three-element physical signal vector output port associated with the
*a*-, *b*-, and
*c*-phase currents.
### Conserving

### **~1** — Three-phase voltage and current electrical

Expandable three-phase
electrical conserving port 1 associated with three-phase
voltage and current.

### **~2** — Three-phase voltage and current electrical

Expandable three-phase
electrical conserving port 2 associated with three-phase
voltage and current.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Voltage measurement type** — Voltage measurement type `phase-to-phase voltage` (default) | `phase-to-ground voltage`

Type of voltage measurement.

### **Measurement output unit** — Measurement system `Per unit` (default) | `SI`

System of units for output current and voltage measurements.

### **Nominal power** — Nominal power `100e6` `V*A` (default)

Nominal power.

#### Dependencies

To enable this parameter, set **Measurement output unit** to
`Per unit`.

### **Nominal voltage (phase-to-phase RMS)** — Nominal voltage `24e3` `V` (default)

Nominal phase-to-phase root-mean-square (RMS) voltage.

#### Dependencies

To enable this parameter, set **Measurement output
unit** to `Per unit`.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Ideal three-phase current and voltage sensor

The Current and Voltage Sensor (Three-Phase) block measures
the voltage and current of a three-phase electrical node.

**Note**

You must connect the Current and Voltage Sensor
(Three-Phase) block in series with a three-phase element.
For more information on how to use this block, see Build and Simulate Composite and Expanded Three-Phase Models.
