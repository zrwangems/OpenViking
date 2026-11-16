---
type: simulink-block
title: 'Average Value Inverter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'averagevalueinverter'
documentation_source_path: 'ref/averagevalueinverter.html'
language: en
---

# Average Value Inverter

## Ports

### Input

### **Dabc** — Duty cycle for three-phase voltage `1`-by-`3` array

Three-phase modulation indices in the range [0,1] for generating voltages that run
the motor.

**Data Types:** `single` | `double` | `fixed point`

### **Vdc** — Inverter DC voltage scalar

DC bus voltage input to the inverter.

**Data Types:** `single` | `double` | `fixed point` | `uint8` | `uint16` | `uint32`
### Output

### **Vabc** — Three-phase voltage output `1`-by-`3` array

Three-phase voltage (Volts) corresponding to the input duty cycle that runs the
motor.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

Not documented in R2025b.

## Libraries

Motor Control Blockset / Electrical Systems / Inverters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute three-phase AC voltage from inverter DC voltage

The Average-Value Inverter block models an average-value and full-wave
inverter. It computes the three-phase AC voltage output from inverter DC voltage by using the
duty cycle information.

### Equations

These equations describe how the block computes the three-phase AC voltage.

D0=(Da+Db+Dc)3

Va=Vdc×(Da−D0)

Vb=Vdc×(Db−D0)

Vc=Vdc×(Dc−D0)

where:

- Da, Db, and Dc are the modulation indices ranging between 0 and 1.
- Vdc is the DC bus voltage of the inverter (Volts).
- Va, Vb, and Vc are the output three-phase voltages (Volts).
