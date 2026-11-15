---
type: simulink-block
title: 'Strain Gauge'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'straingauge'
documentation_source_path: 'ref/straingauge.html'
language: en
---

# Strain Gauge

## Ports

### Input

### **E** — Strain input physical signal

Physical signal port associated with the strain input.
### Conserving

### **+** — Positive port electrical

Electrical conserving port associated with the strain gauge positive
port.

### **-** — Negative port electrical

Electrical conserving port associated with the strain gauge negative
port.

## Parameters

### **Gauge resistance** — Unstressed gauge resistance `100` `Ohm` (default)

Unstressed gauge resistance.

### **Gauge factor** — Gauge factor `2` (default)

The ratio *K* of the fractional change in resistance to
the fractional change in length.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Deformation sensor

The Strain Gauge block represents a sensor that
generates a change in resistance as a function of strain using the following equation:

ΔRR=Kε

where:

- Δ*R*/*R* is the fractional change in
  resistance.
- ε is the strain at port E.
- *K* is the **Gauge factor** parameter
  value.
